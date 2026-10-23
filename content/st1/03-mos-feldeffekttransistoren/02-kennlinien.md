---
title: Kennlinien des NMOS-Transistors
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / MOS-Feldeffekttransistoren
order: 33030200
summary: Wie der Drainstrom eines n-Kanal-MOSFET von der Gate-Source- und der Drain-Source-Spannung abhängt und warum seine Ausgangskennlinien erst ansteigen und dann fast waagerecht verlaufen. Kompakte Fassung mit Herleitung der Triodengleichung aus der Bedingung gleichen Stroms in jedem Querschnitt, Quadratgesetz, Kanallängenmodulation und Großsignalmodell mit Arbeitspunktberechnung, durchgerechnet am Beispieltransistor mit 2 mA/V².
tags: ohmscher Bereich, Abschnürbereich, Quadratgesetz, Kanallängenmodulation, Ausgangskennlinie
stil: 3
fassung: kompakt
---

## Worum es geht

Wer eine Schaltung mit MOS-Feldeffekttransistoren berechnet, braucht eine Gleichung für den Drainstrom bei gegebener Gate-Source- und Drain-Source-Spannung. Wie der Kanal entsteht, warum er zum Drain hin dünner wird und wo er abschnürt, zeigt [Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise.html); hier wird daraus der Strom. Alles hängt an einem Prinzip:

**Durch jeden Querschnitt des Kanals fließt derselbe Strom, das Produkt aus Elektronenladung pro Länge und Geschwindigkeit der Elektronen; wo der Kanal zum Drain hin dünner wird, laufen die Elektronen schneller, und aus dieser Bedingung folgt die Triodengleichung, deren Maximum genau an der Abschnürgrenze liegt und die von dort an als Quadratgesetz stehen bleibt, bis auf einen leichten Anstieg, weil der Kanal mit wachsender Drainspannung kürzer wird.**

Vorausgesetzt werden der genannte Artikel und die Drift von Ladungsträgern im elektrischen Feld aus [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html). Auf den Kennlinien bauen der PMOS, der Substrateffekt, das Kleinsignalmodell und alle Transistorschaltungen auf.

:::grafik
Szene: st1/mos-feldeffekttransistoren/02-kennlinienfeld · Vorlage: kennlinienfeld
**Abbildung 1:** (a) Ausgangskennlinienfeld des Beispieltransistors ohne Kanallängenmodulation: Drainstrom $I_D$ über der Drain-Source-Spannung $U_{DS}$ von 0 bis 2,5 V für $U_{GS}$ = 0,75 V, 1 V, 1,25 V und 1,5 V. Jede Kurve steigt im ohmschen Bereich (hellblau) an, erreicht auf der gestrichelten Grenzparabel bei $U_{DS} = U_{GS} - U_{th}$ = 0,25 V, 0,5 V, 0,75 V und 1 V ihren Höchstwert und verläuft im Abschnürbereich (hellorange) waagerecht bei 0,0625 mA, 0,25 mA, 0,5625 mA und 1 mA. (b) Übertragungskennlinie im Abschnürbereich: $I_D$ über $U_{GS}$, null bis zur Schwellenspannung 0,5 V, dann eine Parabel bis 1 mA bei 1,5 V. Der Strom steigt erst mit der Drainspannung und bleibt dann stehen; seine Höhe wächst quadratisch mit der Gate-Übersteuerung.
:::

## Ausgangs- und Übertragungskennlinie

*Wie stellt man dar, dass der Drainstrom von zwei Spannungen zugleich abhängt?*

Gemessen wird gegen die Source: Gate-Source-Spannung $U_{GS}$ und Drain-Source-Spannung $U_{DS}$; der Bulk liegt an der Source. Der Drainstrom $I_D$ wird in den Drain hinein gezählt. Weil das isolierte Gate bei Gleichspannung keinen Strom aufnimmt, fließt derselbe Strom aus der Source heraus, und ein Strom und zwei Spannungen beschreiben den Transistor.

Der Beispieltransistor, ein NMOS mit der Kanalweite $W$ = 10 µm, der Kanallänge $L$ = 1 µm, der Schwellenspannung $U_{th}$ = 0,5 V, ab der sich ein Kanal bildet, und dem Steilheitskoeffizienten $K_n$ = 2 mA/V², der Größe, die Beweglichkeit der Elektronen, Kapazität des Gateoxids pro Fläche und das Verhältnis $W/L$ zusammenfasst, führt bei $U_{GS}$ = 1 V und $U_{DS}$ = 0,3 V den Strom 0,21 mA, bei 1 V und 2 V 0,25 mA, bei 1,5 V und 2 V 1 mA. Eine Funktion zweier Spannungen zeichnet man als Schnitte. Die __Ausgangskennlinie__ zeigt $I_D$ über $U_{DS}$ bei fester $U_{GS}$; so heißt sie, weil zwischen Drain und Source in Schaltungen die Last liegt. Mehrere davon mit $U_{GS}$ als __Parameter__ bilden das __Ausgangskennlinienfeld__ (Abbildung 1a). Die __Übertragungskennlinie__ zeigt $I_D$ über $U_{GS}$ bei fester $U_{DS}$, also wie der Eingang den Ausgang steuert (Abbildung 1b).

Jede Ausgangskennlinie steigt erst fast geradlinig an, biegt ab und läuft ab $U_{DS} = U_{GS} - U_{th}$ waagerecht weiter. Links dieser Grenze reicht der Kanal bis zum Drain, der __ohmsche Bereich__; rechts ist er vor dem Drain abgeschnürt, der __Abschnürbereich__; unterhalb der Schwelle gibt es keinen Kanal, den __Sperrbereich__ ([Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise.html)). Die Gleichungen dieses Artikels gelten für einen __Langkanaltransistor__, dessen Kanal wie beim Beispiel mit 1 µm so lang ist, dass die Elektronen weit unter ihrer Höchstgeschwindigkeit bleiben. Den leichten Anstieg des Stroms im Abschnürbereich, den die Verkürzung des Kanals bewirkt, lässt der Artikel bis zum Abschnitt *Kanallängenmodulation* außer Acht; alle Zahlen bis dahin, auch die oben genannten, gelten ohne ihn.

## Derselbe Strom in jedem Querschnitt

*Wie kann durch einen Kanal, der zum Drain hin dünner wird, überall derselbe Strom fließen?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/02-kanal-geschwindigkeit · Vorlage: profil-gestapelt
**Abbildung 2:** Drei gestapelte Diagramme über dem Ort $x/L$ von der Source (0) zum Drain (1) bei $U_{GS}$ = 1 V und $U_{DS}$ = 0,3 V, Drainstrom 0,21 mA; darüber der Kanal als Band, dessen Dicke der Ladung folgt. (a) Kanalpotential $U(x)$: 0, 56, 119, 196 und 300 mV bei $x/L$ = 0, 0,25, 0,5, 0,75 und 1, zum Drain hin immer steiler. (b) Elektronenladung in Prozent ihres Werts an der Source: 100, 89, 76, 61 und 40 %. (c) mittlere Geschwindigkeit der Elektronen: 6,1·10⁵ cm/s an der Source, 8,0·10⁵ cm/s in der Mitte, 1,52·10⁶ cm/s am Drain-Ende. Wo der Kanal dünner ist, laufen die Elektronen schneller; das Produkt aus Ladung und Geschwindigkeit, der Strom, ist überall gleich.
:::

**Die Akteure:**

- __$x$__, __$U(x)$__, __$Q'_n(x)$__: Ort längs des Kanals, von 0 an der Source bis $L$ am Drain; __Kanalpotential__, das Potential des Kanals an der Stelle $x$ gegenüber der Source; Elektronenladung pro Fläche, proportional zur örtlichen Übersteuerung $U_{GS} - U_{th} - U(x)$, an der Source bei $U_{GS}$ = 1 V −3,45 fC/µm².
- __$v_n(x)$__: mittlere Geschwindigkeit der Elektronen zum Drain hin, in cm/s; 6,1·10⁵ cm/s an der Source bei $U_{GS}$ = 1 V und $U_{DS}$ = 0,3 V.
- __$E_x(x)$__: treibende Feldstärke längs des Kanals, das negative Gefälle des Kanalpotentials, in V/cm; zum größten Teil das elektrische Feld an der Oberfläche, zu einem kleinen Teil der Antrieb der Diffusion. Sie zeigt zur Source und treibt die Elektronen zum Drain, 2,1 kV/cm an der Source.
- __$\mu_n$__: Beweglichkeit der Elektronen im Kanal, Driftgeschwindigkeit pro Feldstärke; 290 cm²/(V s).

**Das Zusammenspiel:**

**Schritt 1**: Der Strom durch einen Querschnitt ist Ladung pro Länge mal Geschwindigkeit: In einer Sekunde passiert die Ladung einer Strecke der Länge $v_n$ den Querschnitt. Die Elektronen laufen zum Drain, der Strom wegen ihrer negativen Ladung in Gegenrichtung, in den Drain hinein.

**Schritt 2**: Bei Gleichspannung ist dieser Strom in jedem Querschnitt derselbe. Flösse in ein Stück des Kanals mehr hinein als heraus, sammelte sich dort Ladung an, bis Zu- und Abfluss gleich sind; seitlich kommt nichts hinzu, denn das Gate ist isoliert und die Übergänge zum Bulk sperren.

**Schritt 3** (entscheidender Schritt): Zum Drain hin nimmt die Ladung ab, bei 1 V und 0,3 V auf 40 % am Drain-Ende. Damit das Produkt gleich bleibt, sind die Elektronen dort 2,5-mal so schnell, 1,52·10⁶ cm/s statt 6,1·10⁵ cm/s (Abbildung 2c).

**Schritt 4**: Die Geschwindigkeit ist Beweglichkeit mal treibende Feldstärke; die höhere Geschwindigkeit verlangt ein 2,5-mal so starkes treibendes Feld, 5,25 kV/cm statt 2,1 kV/cm. Das Feld ist das Gefälle des Kanalpotentials; $U(x)$ steigt deshalb zum Drain hin immer steiler an, auf halber Länge erst auf 119 mV von 300 mV (Abbildung 2a).

**Schritt 5**: Ladung und Feld hängen beide vom Kanalpotential ab. Die Bedingung gleichen Stroms wird so zu einer Gleichung für $U(x)$, die den Strom enthält:

:::formel Formel
$$I_D = \mu_n\,W\,C'_\mathrm{ox}\,\big(U_{GS} - U_{th} - U(x)\big)\,\frac{dU}{dx}$$
:::

**So liest man das:** An jeder Stelle ergibt das Produkt aus örtlicher Übersteuerung, die die Ladung festlegt, und Potentialgefälle, das die Geschwindigkeit festlegt, denselben Strom. Wo die Übersteuerung klein ist, muss das Gefälle groß sein. Ohne Drainspannung gibt es kein Gefälle und keinen Strom, obwohl der Kanal voller Elektronen ist.

**Kurz gesagt:** Wo der Kanal halb so viel Ladung trägt wie an einer anderen Stelle, laufen die Elektronen doppelt so schnell wie dort.

Idee der Herleitung: Man schreibt den Strom als Ladung pro Länge mal Geschwindigkeit und setzt die örtliche Kanalladung ein.

:::herleitung
**Ausgangspunkt:** die Driftgeschwindigkeit der Elektronen im elektrischen Feld, nach der Definition der Beweglichkeit $\mu_n$ als Driftgeschwindigkeit pro Feldstärke ([Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell-ausfuehrlich.html)), und die örtliche Kanalladung ([Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html)):

$$v_n = -\mu_n\,E_x, \qquad Q'_n(x) = -C'_\mathrm{ox}\,\big(U_{GS} - U_{th} - U(x)\big)\,$$

**Annahmen:**
(i) Gleichbetrieb: Alle Größen sind zeitlich konstant.
(ii) Allmählicher Kanal: Die örtliche Kanalladung gilt an jeder Stelle; das Feld längs des Kanals ist klein gegen das Feld senkrecht zur Oberfläche. Beim Beispieltransistor sind es bei 1 V Gatespannung einige kV/cm längs des Kanals gegen 2 MV/cm im Oxid.
(iii) Angetrieben werden die Elektronen vom Gefälle ihres Potentials $U(x)$: Ihre mittlere Geschwindigkeit ist $\mu_n$ mal der treibenden Feldstärke $E_x = -dU/dx$. Diese setzt sich aus dem elektrischen Feld an der Oberfläche und einem Anteil der Diffusion entlang des Dichtegefälles zusammen, beim Beispieltransistor bei 1 V Gatespannung und 0,3 V Drainspannung an der Source 5 % und am Drain-Ende 13 %; zusammen ergeben beide das Gefälle des Potentials der Elektronen, und das ist $U(x)$.
(iv) Die Beweglichkeit ist längs des Kanals konstant, die Geschwindigkeit also proportional zum Feld.

**Schritt 1**: Auf der Länge $dx$ liegt die Ladung $W\,Q'_n\,dx$; sie bewegt sich mit $v_n$ zum Drain. Pro Zeit passiert den Querschnitt die Ladung $W\,Q'_n\,v_n$ in Richtung Drain. Weil sie negativ ist, fließt der Strom in Gegenrichtung, in den Drain hinein:

$$I_D = -W\,Q'_n(x)\,v_n(x)$$

**Schritt 2**: Mit (iii) ist die Geschwindigkeit

$$v_n(x) = -\mu_n\,E_x(x) = \mu_n\,\frac{dU}{dx}$$

**Schritt 3**: Einsetzen der örtlichen Kanalladung:

$$I_D = W\,C'_\mathrm{ox}\,\big(U_{GS} - U_{th} - U(x)\big)\cdot\mu_n\,\frac{dU}{dx}$$

**Schritt 4** (entscheidender Schritt): Nach (i) und der Ladungserhaltung ist der Strom in jedem Querschnitt gleich, das Gate liefert keinen und der Bulk keinen nennenswerten Strom. Die linke Seite hängt deshalb nicht von $x$ ab; die rechte muss für jedes $x$ denselben Wert ergeben.

**Ergebnis:**

$$I_D = \mu_n\,W\,C'_\mathrm{ox}\,\big(U_{GS} - U_{th} - U(x)\big)\,\frac{dU}{dx}$$

**Woher die Faktoren kommen:** $W\,C'_\mathrm{ox}\,(U_{GS} - U_{th} - U)$ ist die Elektronenladung pro Länge, $\mu_n\,dU/dx$ ihre Geschwindigkeit.

**Proben:** Einheit: cm²/(V s) · cm · F/cm² · V · V/cm ergibt F·V/s, also C/s = A. Grenzfall: Ist $U_{DS}$ = 0, ist $U$ überall null und mit ihm das Gefälle; es fließt kein Strom. Ist $U_{DS}$ sehr klein, ist das Gefälle überall $U_{DS}/L$, und die Gleichung wird zum Kanalwiderstand $R_\mathrm{on}$ = 1/($K_n(U_{GS} - U_{th})$) aus dem Artikel über Aufbau und Funktionsweise. Zahlenwert: An der Source ergeben 0,21 mA bei $U_{GS}$ = 1 V ein Gefälle von 2,1 kV/cm.

**Grenzen:** Annahme (ii) versagt nahe am Abschnürpunkt, wo die Ladung gegen null geht und das Feld längs des Kanals groß wird (Abschnitt *Abschnürgrenze und Quadratgesetz*). Annahme (iv) versagt bei hohen Feldern: Die Geschwindigkeit der Elektronen in Silizium wächst nicht über rund 10⁷ cm/s hinaus.
:::

## Die Triodengleichung

*Wie groß ist der Drainstrom, solange der Kanal bis zum Drain reicht?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/02-flaeche-uebersteuerung · Vorlage: flaeche-teilbilder
**Abbildung 3:** Örtliche Übersteuerung $U_{GS} - U_{th} - U$, proportional zur Elektronenladung pro Fläche, aufgetragen über dem Kanalpotential $U$ bei $U_{GS}$ = 1 V: eine fallende Gerade von 0,5 V bei $U$ = 0 auf null bei $U$ = 0,5 V, rechts davon gestrichelt ohne Elektronen. (a) $U_{DS}$ = 0,3 V: Die Fläche von 0 bis 0,3 V ist in drei Streifen von je 0,1 V geteilt, mit den Höhen 0,45 V, 0,35 V und 0,25 V in der Streifenmitte; zusammen 0,105 V², mal $K_n$ ergibt 0,21 mA. (b) $U_{DS}$ = 0,5 V: das volle Dreieck, 0,125 V², 0,25 mA. (c) $U_{DS}$ = 0,75 V: dasselbe Dreieck, denn zwischen 0,5 V und 0,75 V gibt es keinen Kanal; der Strom bleibt 0,25 mA. Der Drainstrom ist $K_n$ mal der Fläche unter der Übersteuerung; sie wächst nur, bis die Übersteuerung am Drain-Ende null ist.
:::

Aus der Stromgleichung folgt der Strom, wenn man sie über den ganzen Kanal aufsummiert. Am konkreten Fall: Man teilt $U_{DS}$ = 0,3 V in drei Stufen von je 0,1 V. Auf dem Stück des Kanals, auf dem das Potential von 0 auf 0,1 V steigt, beträgt die Übersteuerung im Mittel 0,45 V, und nach der Stromgleichung ist der Strom mal die Länge des Stücks $\mu_n W C'_\mathrm{ox}$ mal 0,45 V mal 0,1 V; die beiden anderen Stücke liefern 0,35 V und 0,25 V. Zusammen ergeben die Stücke den ganzen Kanal:

$$\begin{aligned} I_D\,L &= \mu_n\,W\,C'_\mathrm{ox}\cdot0{,}1\ \mathrm V\cdot\big(0{,}45 + 0{,}35 + 0{,}25\big)\ \mathrm V \\ &= \mu_n\,W\,C'_\mathrm{ox}\cdot0{,}105\ \mathrm{V^2} \end{aligned}$$

Geteilt durch $L$ steht vorn $K_n$, und $I_D$ = 2 mA/V² · 0,105 V² = 0,21 mA. Die Stücke sind verschieden lang, im Verhältnis 0,45 zu 0,35 zu 0,25: An der Source tragen viele langsame Elektronen den Strom, dort steigt das Potential am langsamsten. Die Summe ist die Fläche unter der Geraden in Abbildung 3a; weil die Übersteuerung linear mit dem Potential fällt, ist sie exakt, und allgemein ist $I_D L$ gleich $\mu_n W C'_\mathrm{ox}$ mal dem Integral der Übersteuerung über das Kanalpotential:

:::formel Formel
$$I_D = K_n\,\Big[\big(U_{GS} - U_{th}\big)\,U_{DS} - \frac{U_{DS}^2}{2}\Big]$$
:::

**So liest man das:** Die Gleichung gilt im ohmschen Bereich, für $U_{GS} > U_{th}$ und $U_{DS} < U_{GS} - U_{th}$. Der erste Term ist der Strom eines Widerstands $R_\mathrm{on}$ mit der Übersteuerung an der Source, der zweite zieht ab, was der Kanal zum Drain hin an Ladung verliert. Durch den Faktor 1/2 ist die Klammer $U_{DS}$ mal dem Mittelwert der Übersteuerungen an Source und Drain-Ende, bei 1 V und 0,3 V also 0,35 V zwischen 0,5 V und 0,2 V.

**Kurz gesagt:** Im ohmschen Bereich ist der Strom so groß, als hätte der ganze Kanal überall den Mittelwert der Übersteuerungen von Source- und Drain-Ende.

Idee der Herleitung: Man trennt in der Stromgleichung Ort und Potential und integriert beide über den ganzen Kanal.

:::herleitung
**Ausgangspunkt:** die Stromgleichung des Kanals aus dem Abschnitt *Derselbe Strom in jedem Querschnitt*:

$$I_D = \mu_n\,W\,C'_\mathrm{ox}\,\big(U_{GS} - U_{th} - U(x)\big)\,\frac{dU}{dx}$$

**Annahmen:**
(i) dieselben wie für die Stromgleichung;
(ii) der Kanal reicht bis zum Drain: Die örtliche Übersteuerung ist auch am Drain-Ende nicht negativ, $U_{DS}$ also höchstens $U_{GS} - U_{th}$;
(iii) die Enden des Kanals haben das Potential von Source und Drain, $U(0)$ = 0 und $U(L) = U_{DS}$.

**Schritt 1**: Multiplikation mit $dx$ trennt die Variablen: Links stehen nur der konstante Strom und der Ort, rechts nur das Potential:

$$I_D\,dx = \mu_n\,W\,C'_\mathrm{ox}\,\big(U_{GS} - U_{th} - U\big)\,dU$$

**Schritt 2** (entscheidender Schritt): Integriert wird über den ganzen Kanal, links über den Ort von 0 bis $L$, rechts über das Potential an denselben Stellen, nach (iii) von 0 bis $U_{DS}$. Weil $I_D$ an jeder Stelle denselben Wert hat, steht er vor dem Integral:

$$I_D\int_0^L dx = \mu_n\,W\,C'_\mathrm{ox}\int_0^{U_{DS}}\big(U_{GS} - U_{th} - U\big)\,dU$$

**Schritt 3**: Links ergibt das Integral $L$. Rechts ist $(U_{GS} - U_{th})\,U - U^2/2$ eine Stammfunktion des Integranden; an den Grenzen ausgewertet:

$$I_D\,L = \mu_n\,W\,C'_\mathrm{ox}\,\Big[\big(U_{GS} - U_{th}\big)\,U_{DS} - \frac{U_{DS}^2}{2}\Big]$$

**Schritt 4**: Division durch $L$ und der Steilheitskoeffizient $K_n = \mu_n C'_\mathrm{ox} W/L$:

**Ergebnis:**

$$I_D = K_n\,\Big[\big(U_{GS} - U_{th}\big)\,U_{DS} - \frac{U_{DS}^2}{2}\Big]$$

**Woher die Faktoren kommen:** $K_n$ fasst Beweglichkeit, Oxidkapazität und Abmessungen zusammen. Die Klammer ist das Integral der örtlichen Übersteuerung über das Kanalpotential; das $U_{DS}^2/2$ entsteht, weil die Übersteuerung linear mit dem Potential abnimmt.

**Proben:** Einheit: A/V² · V² = A. Grenzfall: Für kleine $U_{DS}$ fällt der quadratische Term weg, und es bleibt $U_{DS}/R_\mathrm{on}$ mit $R_\mathrm{on}$ = 1/($K_n(U_{GS} - U_{th})$). Zahlenwert: 2 mA/V² · (0,5 V · 0,3 V − 0,045 V²) = 2 mA/V² · 0,105 V² = 0,21 mA.

**Grenzen:** Ist $U_{DS}$ größer als $U_{GS} - U_{th}$, ist Annahme (ii) verletzt, und die Gleichung gilt nicht mehr (Abschnitt *Abschnürgrenze und Quadratgesetz*). Bei großen Gatespannungen sinkt die Beweglichkeit, weil das starke Feld senkrecht zur Oberfläche die Elektronen gegen die Grenzfläche zum Oxid drückt, wo sie stärker gestreut werden; der Strom bleibt dann unter der Gleichung.
:::

::::beispiel Strom, treibendes Feld und Geschwindigkeit bei 1 V Gatespannung und 0,3 V Drainspannung
**Gegeben:** $K_n$ = 2 mA/V², $U_{th}$ = 0,5 V, $U_{GS}$ = 1 V, $U_{DS}$ = 0,3 V; $\mu_n$ = 290 cm²/(V s), $W$ = 10 µm = 10⁻³ cm, $C'_\mathrm{ox}$ = 6,906·10⁻⁷ F/cm².

**Gesucht:** der Drainstrom, sein Verhältnis zum Strom der Widerstandsgeraden mit $R_\mathrm{on}$ = 1 kΩ und Geschwindigkeit der Elektronen und treibende Feldstärke an Source und Drain-Ende.

**Rechnung:** Triodengleichung:

$$I_D = 2\ \mathrm{mA/V^2}\cdot\big(0{,}5\ \mathrm V\cdot0{,}3\ \mathrm V - 0{,}045\ \mathrm{V^2}\big) = 0{,}21\ \mathrm{mA}$$

Die Gerade ergibt 0,3 V / 1 kΩ = 0,3 mA; der Transistor erreicht 70 %. Ladung pro Länge an der Source, bei 0,5 V Übersteuerung:

$$W\,|Q'_n(0)| = 10^{-3}\ \mathrm{cm}\cdot6{,}906\cdot10^{-7}\ \mathrm{F/cm^2}\cdot0{,}5\ \mathrm V = 3{,}45\cdot10^{-10}\ \mathrm{C/cm}$$

Geschwindigkeit als Strom durch Ladung pro Länge und treibendes Feld als Geschwindigkeit durch Beweglichkeit:

$$v_n(0) = \frac{2{,}1\cdot10^{-4}\ \mathrm A}{3{,}45\cdot10^{-10}\ \mathrm{C/cm}} = 6{,}08\cdot10^{5}\ \mathrm{cm/s}, \qquad |E_x(0)| = \frac{6{,}08\cdot10^{5}\ \mathrm{cm/s}}{290\ \mathrm{cm^2/(V\,s)}} = 2{,}10\ \mathrm{kV/cm}\,$$

Am Drain-Ende ist die Übersteuerung 0,2 V, die Ladung das 0,4-Fache, Geschwindigkeit und Feld also das 2,5-Fache: 1,52·10⁶ cm/s und 5,25 kV/cm.

**Ergebnis:** **0,21 mA, 70 % der Widerstandsgeraden; an der Source 6,1·10⁵ cm/s und 2,1 kV/cm, am Drain-Ende 1,52·10⁶ cm/s und 5,25 kV/cm.**

**Einordnung:** Die Elektronen sind mit 6 bis 15 Kilometern pro Sekunde rund hundertmillionenmal so schnell wie die in einem Kupferdraht mit 1 A pro mm², weil den Strom nur die rund 1,6·10⁵ Elektronen tragen, die gerade im Kanal sind. Selbst am Drain-Ende erreichen sie nur 15 % ihrer Höchstgeschwindigkeit von rund 10⁷ cm/s; die Annahme einer Geschwindigkeit proportional zum Feld ist näherungsweise erfüllt.
::::

Abbildung 3 zeigt auch, warum der Strom langsamer wächst als die Drainspannung: Jede weitere Stufe fügt einen niedrigeren Streifen hinzu, weil am Drain-Ende weniger Ladung übrig ist. Die Kennlinie krümmt sich nach unten und bleibt hinter der Widerstandsgeraden zurück, bei 0,1 V um 10 %, bei 0,3 V um 30 %. Weil der Strom hier mit der Drainspannung wächst und zugleich vom Gate gesteuert wird, ähneln die Kennlinien denen einer Triode, einer Elektronenröhre mit Steuergitter, deren Anodenstrom mit der Anodenspannung wächst; deshalb heißt der ohmsche Bereich auch __Triodenbereich__ und die Gleichung __Triodengleichung__.

## Abschnürgrenze und Quadratgesetz

*Warum bleibt der Strom stehen, wenn die Drain-Source-Spannung die Gate-Übersteuerung überschreitet, und wie groß ist er dann?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/02-triode-parabel · Vorlage: kennlinie-gueltigkeit
**Abbildung 4:** Drainstrom über der Drain-Source-Spannung von 0 bis 1,2 V bei $U_{GS}$ = 1 V. Durchgezogen die Triodengleichung bis zu ihrem Maximum 0,25 mA bei 0,5 V, gestrichelt die Tangente im Ursprung mit 1 mS ($R_\mathrm{on}$ = 1 kΩ), die bei 0,1 V 0,1 mA statt 0,09 mA anzeigt. Jenseits von 0,5 V blass gestrichelt und durchgestrichen die rechnerische Fortsetzung der Parabel, die bei 0,75 V auf 0,1875 mA und bei 1 V auf null fiele; dagegen der tatsächliche Verlauf, ohne Kanallängenmodulation waagerecht bei 0,25 mA. Senkrechte Marke „Abschnürgrenze 0,5 V“. Die Triodengleichung erreicht ihr Maximum genau an der Abschnürgrenze; dahinter gilt sie nicht mehr, und der Strom bleibt beim Maximum stehen.
:::

**Das Zusammenspiel:**

**Schritt 1**: Als Funktion von $U_{DS}$ ist die Triodengleichung eine nach unten geöffnete Parabel (Abbildung 4): Sie beginnt mit der Steigung 1 mS des Kanalwiderstands und erreicht bei 0,5 V ihr Maximum von 0,25 mA.

**Schritt 2**: Ihre Steigung ist der Leitwert, den der Kanal hätte, wenn er überall so dünn wäre wie an seinem Drain-Ende: $K_n$ mal der Übersteuerung dort, 0,8 mS bei 0,1 V, 0,4 mS bei 0,3 V. Ein zusätzliches Millivolt verteilt sich zwar über den ganzen Kanal, in Abbildung 3 kommt aber nur ein schmaler Streifen mit der Höhe der Übersteuerung am Drain-Ende hinzu.

**Schritt 3** (entscheidender Schritt): Die Steigung wird null, wenn die Übersteuerung am Drain-Ende null wird, bei $U_{DS} = U_{GS} - U_{th}$, und das ist genau die Abschnürgrenze. Maximum der Parabel und Abschnüren des Kanals sind dieselbe Bedingung; in Abbildung 3b ist die Fläche zum vollen Dreieck geworden.

**Schritt 4**: Jenseits davon fiele die Parabel wieder, auf 0,1875 mA bei 0,75 V und null bei 1 V. Ihre Herleitung setzt aber einen Kanal bis zum Drain voraus. Tatsächlich endet der Kanal am Abschnürpunkt, an dem seine Ladung null und sein Potential deshalb genau $U_{GS} - U_{th}$ ist; den Rest der Drainspannung nimmt die kurze verarmte Zone vor dem Drain auf, deren starkes Feld jedes ankommende Elektron zum Drain zieht.

**Schritt 5**: Der Kanal bis zum Abschnürpunkt sieht also immer dieselbe Spannung $U_{GS} - U_{th}$ und ist praktisch so lang wie vorher. Er führt den Strom der Abschnürgrenze, das Maximum der Parabel; in Abbildung 3c kommt keine Fläche mehr hinzu.

:::fehlvorstellung
„Hinter dem Maximum der Parabel nimmt der Strom wieder ab.“ Das liegt nahe, weil die Triodengleichung eine vollständige Parabel ist. Der Strom bleibt aber beim Maximum stehen, ohne Kanallängenmodulation bei 0,25 mA für 0,5 V, 1 V und 2 V Drainspannung, statt auf 0,1875 mA bei 0,75 V und null bei 1 V zu fallen. Der abfallende Ast beschriebe einen Kanal bis zum Drain mit einer negativen Zahl von Elektronen am Drain-Ende, den es nicht gibt; ab der Abschnürgrenze gilt das Quadratgesetz.
:::

**Die Akteure:**

- __$U_{DS,\mathrm{ab}}$__: Abschnürspannung, die Drain-Source-Spannung an der Grenze zwischen ohmschem Bereich und Abschnürbereich, gleich der Übersteuerung; 0,5 V bei $U_{GS}$ = 1 V.

Für $U_{DS}$ ab der Abschnürspannung gilt:

:::formel Formel
$$I_D = \frac{K_n}{2}\,\big(U_{GS} - U_{th}\big)^2$$
:::

**So liest man das:** Die Gleichung gilt im Abschnürbereich; $U_{DS}$ kommt nicht vor. Der Strom wächst mit dem Quadrat der Übersteuerung, weil zwei Größen mit ihr wachsen, die Ladung an der Source und die Spannung über dem Kanal. Der Faktor 1/2 ist der Mittelwert der Übersteuerungen an Source und Abschnürpunkt, in Abbildung 3b die Fläche des Dreiecks. Der Bereich heißt auch Sättigungsbereich, weil der Strom nicht weiter wächst; mit der Sättigung des Bipolartransistors hat das nichts zu tun.

**Kurz gesagt:** Im Abschnürbereich führt bei gleicher Drain-Source-Spannung die doppelte Gate-Übersteuerung zum vierfachen Drainstrom.

Idee der Herleitung: Man setzt in die Triodengleichung die Spannung am Abschnürpunkt ein, $U_{GS} - U_{th}$, weil der leitende Kanal dort endet.

:::herleitung
**Ausgangspunkt:** die Triodengleichung aus dem Abschnitt *Die Triodengleichung*.

**Annahmen:**
(i) Der leitende Kanal reicht von der Source bis zum Abschnürpunkt; für ihn gelten die Annahmen der Triodengleichung.
(ii) Am Abschnürpunkt ist die örtliche Ladung null, das Kanalpotential dort also $U_{GS} - U_{th}$.
(iii) Die Zone zwischen Abschnürpunkt und Drain ist kurz gegen $L$; beim Beispieltransistor nach eindimensionaler Abschätzung 58 nm bei 2 V, knapp 6 % von $L$.

**Schritt 1**: Ableitung der Triodengleichung nach $U_{DS}$ bei festem $U_{GS}$:

$$\frac{\partial I_D}{\partial U_{DS}} = K_n\,\big(U_{GS} - U_{th} - U_{DS}\big) = \frac{\mu_n\,W\,\big|Q'_n(L)\big|}{L}$$

Die rechte Form ist der Leitwert eines Kanals, der überall die Ladung des Drain-Endes trägt.

**Schritt 2**: Die Ableitung ist null bei $U_{DS} = U_{GS} - U_{th}$, und die zweite Ableitung $-K_n$ ist negativ; dort liegt das Maximum, und es fällt mit der Abschnürgrenze zusammen.

**Schritt 3** (entscheidender Schritt): Für größere $U_{DS}$ ersetzt der Abschnürpunkt den Drain als Ende des Kanals. Nach (i) bis (iii) gilt die Triodengleichung für den Kanal bis dorthin, mit $U_{GS} - U_{th}$ an der Stelle von $U_{DS}$:

$$I_D = K_n\,\Big[\big(U_{GS} - U_{th}\big)^2 - \frac{\big(U_{GS} - U_{th}\big)^2}{2}\Big]$$

**Schritt 4**: Zusammenfassen:

**Ergebnis:**

$$I_D = \frac{K_n}{2}\,\big(U_{GS} - U_{th}\big)^2$$

**Woher die Faktoren kommen:** Das Quadrat entsteht, weil Ladung und Spannung über dem Kanal beide proportional zur Übersteuerung sind; das 1/2 ist der Mittelwert der Übersteuerungen von Source und Abschnürpunkt.

**Proben:** Einheit A/V² · V² = A. Zahlenwert bei 1 V: 1 mA/V² · 0,25 V² = 0,25 mA. An der Grenze stimmen Wert und Steigung (null) mit der Triodengleichung überein; die Kennlinie geht ohne Knick in die Waagerechte über. Grenzfall: Bei $U_{GS} = U_{th}$ ist der Strom null.

**Grenzen:** Annahme (iii) gilt umso schlechter, je größer $U_{DS}$ wird; die Folge ist die Kanallängenmodulation (Abschnitt *Kanallängenmodulation*). In sehr kurzen Kanälen begrenzt die Höchstgeschwindigkeit der Elektronen den Strom schon vor dem Abschnüren.
:::

::::beispiel Sättigungsströme des Beispieltransistors und die MOS-Diode
**Gegeben:** $K_n$ = 2 mA/V², $U_{th}$ = 0,5 V; Gate-Source-Spannungen 0,75 V, 1 V, 1,5 V und 2 V; $U_{DS}$ jeweils über der Abschnürspannung.

**Gesucht:** (a) die Drainströme; (b) der Faktor bei doppelter Gatespannung, 1 V auf 2 V, und bei doppelter Übersteuerung, 1 V auf 1,5 V; (c) der Strom einer MOS-Diode, Gate mit Drain verbunden, bei 1 V.

**Rechnung:** (a) Mit $K_n/2$ = 1 mA/V²:

$$I_D = 1\ \mathrm{mA/V^2}\cdot\big(U_{GS} - 0{,}5\ \mathrm V\big)^2 = 0{,}0625;\ 0{,}25;\ 1;\ 2{,}25\ \mathrm{mA}$$

(b) Die Verhältnisse:

$$\frac{2{,}25\ \mathrm{mA}}{0{,}25\ \mathrm{mA}} = 9, \qquad \frac{1\ \mathrm{mA}}{0{,}25\ \mathrm{mA}} = 4\,$$

(c) Mit $U_{DS} = U_{GS}$ liegt die MOS-Diode oberhalb der Schwelle stets über der Abschnürspannung, im Abschnürbereich; darunter sperrt sie:

$$I_D = 1\ \mathrm{mA/V^2}\cdot\big(1\ \mathrm V - 0{,}5\ \mathrm V\big)^2 = 0{,}25\ \mathrm{mA}$$

**Ergebnis:** **(a) 0,0625 mA, 0,25 mA, 1 mA und 2,25 mA; (b) Faktor 9 bei doppelter Gatespannung, Faktor 4 bei doppelter Übersteuerung; (c) 0,25 mA.**

**Einordnung:** Die Gatespannung von 2 V übersteuert den Transistor dreimal so stark wie 1 V, daher der Faktor 9. Die MOS-Diode ist das Bauelement mit der Parabelkennlinie aus [Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung.html): Ihr Koeffizient 1 mA/V² ist $K_n/2$ des Beispieltransistors.
::::

:::fehlvorstellung
„Doppelte Gatespannung, vierfacher Strom.“ Das liegt nahe, wenn man das Quadratgesetz als „Strom proportional zum Quadrat der Gatespannung“ liest. Quadriert wird aber die Übersteuerung. Von 1 V auf 2 V Gatespannung steigt sie beim Beispieltransistor von 0,5 V auf 1,5 V, und der Strom wächst um den Faktor 9, von 0,25 mA auf 2,25 mA; das Vierfache ergibt nur die doppelte Übersteuerung.
:::

Die Übergangspunkte aller Ausgangskennlinien, an denen sie waagerecht werden, liegen auf der gestrichelten Grenzparabel in Abbildung 1a. Auf ihr ist die Übersteuerung gleich der Drain-Source-Spannung, und das Quadratgesetz wird zu

$$I_D = \frac{K_n}{2}\,U_{DS}^2$$

Links davon liegt der ohmsche Bereich, rechts der Abschnürbereich; bei 0,5 V sind es 0,25 mA, bei 1 V 1 mA.

Idee der Herleitung: Man setzt die Abschnürspannung ins Quadratgesetz ein.

:::herleitung
**Ausgangspunkt:** das Quadratgesetz und die Abschnürspannung $U_{DS,\mathrm{ab}}$, die gleich der Übersteuerung ist, aus dem Abschnitt *Abschnürgrenze und Quadratgesetz*.

**Annahmen:** dieselben wie für das Quadratgesetz.

**Schritt 1** (entscheidender Schritt): Auf der Grenze ist $U_{GS} - U_{th}$ gleich $U_{DS}$; eingesetzt ins Quadratgesetz:

**Ergebnis:**

$$I_D = \frac{K_n}{2}\,U_{DS}^2$$

**Proben:** Zahlenwert: 1 mA/V² · (0,5 V)² = 0,25 mA, der Sättigungsstrom bei 1 V Gatespannung. Grenzfall: Bei $U_{GS} = U_{th}$ liegt der Übergangspunkt im Ursprung.

**Grenzen:** Mit Kanallängenmodulation liegen die Übergangspunkte etwas höher (Abschnitt *Kanallängenmodulation*).
:::

Weil der Sättigungsstrom proportional zum Quadrat der Übersteuerung ist, liegt seine Wurzel, über $U_{GS}$ aufgetragen, auf einer Geraden, die die Spannungsachse genau bei $U_{th}$ schneidet; so bestimmt man die Schwellenspannung aus Messungen.

:::frage
„Gilt das Quadratgesetz auch für sehr kurze Transistoren?“
Nur näherungsweise. Die Herleitung nimmt an, dass die Geschwindigkeit der Elektronen proportional zum Feld wächst; in Silizium ist aber bei rund 10⁷ cm/s Schluss. Mit $\mu_n$ = 290 cm²/(V s) erreicht das Produkt aus Beweglichkeit und Feld diesen Wert bei 35 kV/cm, dem kritischen Feld der __Geschwindigkeitssättigung__, und merklich wird sie schon bei einem Bruchteil davon. Im Beispieltransistor beträgt das mittlere Feld an der Abschnürgrenze bei 0,5 V Übersteuerung 5 kV/cm, bei 0,1 µm Kanallänge wären es 50 kV/cm. Dann wächst der Strom schwächer als quadratisch mit der Übersteuerung, im Grenzfall nur noch linear, weil die Elektronen an der Source schon mit Höchstgeschwindigkeit laufen und nur noch ihre Zahl mit der Gatespannung zunimmt. Solche __Kurzkanaltransistoren__ beschreiben genauere Modelle.
:::

## Kanallängenmodulation

*Warum steigt der Drainstrom im Abschnürbereich mit der Drain-Source-Spannung doch noch leicht an, und wie beschreibt man das?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/02-kanallaengenmodulation · Vorlage: kennlinienfeld-early
**Abbildung 5:** Ausgangskennlinien des Beispieltransistors mit Kanallängenmodulation, λ = 0,1 1/V, für $U_{GS}$ = 0,75 V, 1 V, 1,25 V und 1,5 V und $U_{DS}$ von 0 bis 2,5 V. Im Abschnürbereich steigen sie mit 6,25 µA/V, 25 µA/V, 56,25 µA/V und 100 µA/V an und erreichen bei 2,5 V 0,078 mA, 0,3125 mA, 0,703 mA und 1,25 mA. Nach links gestrichelt verlängert, mit gebrochener Achse zwischen −10 V und 0 V, treffen sich alle Geraden bei $U_{DS}$ = −10 V. Kleines Einsatzbild: das Drain-Ende des Kanals bei $U_{GS}$ = 1 V, der Abschnürpunkt 34 nm vor dem Drain bei 1 V und 58 nm bei 2 V. Weil der Kanal mit wachsender Drainspannung kürzer wird, steigen die Kennlinien im Abschnürbereich leicht an; im Modell treffen sie sich verlängert in einem Punkt.
:::

**Die Akteure:**

- __$\Delta L$__: Länge der verarmten Zone zwischen Abschnürpunkt und Drain, um die der leitende Kanal kürzer ist; nach eindimensionaler Abschätzung 34 nm bei $U_{DS}$ = 1 V und 58 nm bei 2 V, für $U_{GS}$ = 1 V.
- __$\lambda$__: __Kanallängenmodulationsfaktor__, der Anstieg des Stroms im Abschnürbereich je Volt, bezogen auf den Strom des Quadratgesetzes, in 1/V; 0,1 1/V beim Beispieltransistor.
- __$U_A$__: __Early-Spannung__, der Kehrwert von λ; 10 V. Der Name stammt vom gleichartigen Effekt beim Bipolartransistor.

**Das Zusammenspiel:**

**Schritt 1**: Steigt $U_{DS}$ über die Abschnürspannung, nimmt die Zone vor dem Drain den Überschuss auf und wächst; der leitende Kanal ist nur noch $L - \Delta L$ lang.

**Schritt 2**: An seinem Ende liegt weiter $U_{GS} - U_{th}$. Bei gleicher Spannung und gleicher Ladung an der Source führt der kürzere Kanal mehr Strom, denn der Strom ist umgekehrt proportional zur Kanallänge, wie $K_n$ = $\mu_n C'_\mathrm{ox} W/L$ zeigt.

**Schritt 3** (entscheidender Schritt): Weil $\Delta L$ klein gegen $L$ ist, wächst der Strom um etwa $\Delta L/L$, und das wächst mit $U_{DS}$. Das einfachste Modell setzt den Anstieg linear an, als Faktor $(1 + \lambda U_{DS})$; in Abbildung 5 werden die Kennlinien im Abschnürbereich zu schwach steigenden Geraden.

**Schritt 4**: Jede Gerade wird null bei $U_{DS}$ = −1/λ = −10 V, unabhängig von $U_{GS}$; im Modell treffen sich alle verlängerten Geraden in diesem Punkt.

:::formel Formel
$$I_D = \frac{K_n}{2}\,\big(U_{GS} - U_{th}\big)^2\,\big(1 + \lambda\,U_{DS}\big), \qquad U_A = \frac{1}{\lambda}\,$$
:::

**So liest man das:** Die Gleichung gilt im Abschnürbereich. Ein häufiger Irrtum ist, dass der Strom dort gar nicht von $U_{DS}$ abhängt, weil das Quadratgesetz $U_{DS}$ nicht enthält. Tatsächlich steigt er weiter, beim Beispieltransistor bei 1 V Gatespannung mit 25 µA/V, von 0,2625 mA an der Abschnürgrenze auf 0,30 mA bei 2 V. Die Steigung ist λ mal dem Strom des Quadratgesetzes; je kleiner die Early-Spannung, desto steiler. Üblich ist auch die Angabe mit Vorzeichen, −10 V.

**Kurz gesagt:** Im Modell mit konstantem λ treffen sich alle Ausgangskennlinien des Abschnürbereichs, nach links verlängert, in demselben Punkt der Spannungsachse, bei −$U_A$; gemessene Kennlinien tun das nur näherungsweise.

Idee der Herleitung: Man setzt im Quadratgesetz die verkürzte Kanallänge ein und nähert den Anstieg linear.

:::herleitung
**Ausgangspunkt:** das Quadratgesetz aus dem Abschnitt *Abschnürgrenze und Quadratgesetz*, mit $K_n = \mu_n C'_\mathrm{ox} W/L$ ausgeschrieben.

**Annahmen:**
(i) Der leitende Kanal reicht von der Source bis zum Abschnürpunkt, hat die Länge $L - \Delta L$, und an seinem Ende liegt das Potential $U_{GS} - U_{th}$.
(ii) $\Delta L$ ist klein gegen $L$.
(iii) Das Modell setzt die relative Verkürzung proportional zu $U_{DS}$ an, $\Delta L/L = \lambda U_{DS}$. Das ist eine Vereinfachung, denn eigentlich verkürzt erst der Überschuss über die Abschnürspannung den Kanal. Sie hat den Vorteil, dass alle Kennlinien durch einen Punkt gehen; λ wird so gewählt, dass die Steigung zur Messung passt.

**Schritt 1**: Quadratgesetz mit der verkürzten Länge:

$$I_D = \frac{\mu_n\,C'_\mathrm{ox}\,W}{2\,(L - \Delta L)}\,\big(U_{GS} - U_{th}\big)^2$$

$$I_D = \frac{K_n}{2}\,\big(U_{GS} - U_{th}\big)^2\cdot\frac{L}{L - \Delta L}$$

**Schritt 2**: Nach (ii) genügt die erste Näherung des Bruchs:

$$\frac{L}{L - \Delta L} = \frac{1}{1 - \Delta L/L} \approx 1 + \frac{\Delta L}{L}$$

**Schritt 3** (entscheidender Schritt): Mit (iii):

$$I_D = \frac{K_n}{2}\,\big(U_{GS} - U_{th}\big)^2\,\big(1 + \lambda\,U_{DS}\big)$$

**Schritt 4**: Der Strom wird null bei $1 + \lambda U_{DS}$ = 0, also bei $U_{DS}$ = −1/λ, für jedes $U_{GS}$ an derselben Stelle. Den Betrag dieser Spannung nennt man Early-Spannung $U_A$ = 1/λ.

**Ergebnis:**

$$I_D = \frac{K_n}{2}\,\big(U_{GS} - U_{th}\big)^2\,\big(1 + \lambda\,U_{DS}\big), \qquad U_A = \frac{1}{\lambda}\,$$

**Woher die Faktoren kommen:** $(1 + \lambda U_{DS})$ beschreibt die Verkürzung des Kanals. Weil λ für $\Delta L/L$ pro Volt steht, ist es bei gleicher Zone umso größer, je kürzer der Kanal ist.

**Proben:** Einheit: λ$U_{DS}$ ist eine reine Zahl. Grenzfall: Für λ = 0 ergibt sich das Quadratgesetz. Zahlenwert bei 1 V und 2 V: 0,25 mA · 1,2 = 0,30 mA. Steigung: λ · 0,25 mA = 25 µA/V.

**Grenzen:** Annahme (iii) ist ein Modell. Die eindimensionale Abschätzung der Zone ergibt eine Verkürzung, die mit der Wurzel der überschüssigen Spannung wächst, und für den Beispieltransistor einen kleineren Wert; λ wird deshalb gemessen und nicht aus der Dotierung berechnet.
:::

::::beispiel Drainstrom mit Kanallängenmodulation bei 1 V Gatespannung
**Gegeben:** $K_n$ = 2 mA/V², $U_{th}$ = 0,5 V, λ = 0,1 1/V, $U_{GS}$ = 1 V; Drain-Source-Spannungen 0,5 V, 1 V, 2 V und 2,5 V.

**Gesucht:** die Drainströme, die Steigung und ihr Kehrwert und die Early-Spannung.

**Rechnung:** Das Quadratgesetz ergibt 0,25 mA; mit dem Faktor:

$$I_D = 0{,}25\ \mathrm{mA}\cdot\big(1 + 0{,}1\ \mathrm{V^{-1}}\cdot U_{DS}\big) = 0{,}2625;\ 0{,}275;\ 0{,}30;\ 0{,}3125\ \mathrm{mA}$$

Steigung, Kehrwert und Early-Spannung:

$$\lambda\cdot0{,}25\ \mathrm{mA} = 25\ \mathrm{\mu A/V}, \qquad \frac{1}{25\ \mathrm{\mu A/V}} = 40\ \mathrm{k\Omega}, \qquad U_A = 10\ \mathrm V\,$$

**Ergebnis:** **0,2625 mA, 0,275 mA, 0,30 mA und 0,3125 mA; Steigung 25 µA/V, also 40 kΩ; Early-Spannung 10 V.**

**Einordnung:** Als Stromquelle hat der Transistor bei 0,25 mA einen Innenwiderstand von 40 kΩ. Der Bipolartransistor aus [Der Transistor als Verstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker.html) hat eine Early-Spannung von 70 V, seine Kennlinien sind bei gleichem Strom siebenmal flacher. λ wird an gemessenen Kennlinien bestimmt; die eindimensionale Abschätzung der Zone vor dem Drain ergibt für den Beispieltransistor nur 0,027 1/V, gut ein Viertel davon, weil das Feld des Drains sich zweidimensional verteilt und auch auf den Kanal selbst wirkt.
::::

## Das Großsignalmodell

*Wie fasst man das Verhalten in allen Bereichen zu einem Modell zusammen, mit dem man Schaltungen berechnen kann?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/02-ersatzschaltbild · Vorlage: schaltung-ersatzschaltbild
**Abbildung 6:** Links das Schaltzeichen des NMOS mit Gate, Drain, Source und Bulk, den Spannungen $U_{GS}$, $U_{DS}$ und $U_{BS}$ und dem Strom $I_D$ in den Drain hinein. Rechts das Großsignal-Ersatzschaltbild: Das Gate ist ein offener Anschluss ohne Verbindung; zwischen Drain und Source liegt eine gesteuerte Stromquelle mit dem Strom $I_D(U_{GS}, U_{DS})$, gestrichelt den beiden Steuerspannungen zugeordnet; der Bulk ist getrennt eingezeichnet, über $U_{BS}$ wirkt er auf die Schwellenspannung. Darunter die drei Bereiche mit ihren Bedingungen. Für große Signale ist der MOSFET eine Stromquelle zwischen Drain und Source, deren Strom die beiden Spannungen festlegen, bei stromlosem Gate.
:::

Zusammen ergeben die Gleichungen ein Modell des Transistors, das Abbildung 6 als Schaltung zeigt: Das Gate nimmt keinen Strom auf und ist ein offener Anschluss. Zwischen Drain und Source liegt eine __gesteuerte Stromquelle__, deren Strom nicht fest ist, sondern von $U_{GS}$ und $U_{DS}$ abhängt. __Großsignalmodell__ heißt es, weil es für beliebig große Spannungen gilt, im Gegensatz zum Kleinsignalmodell, das kleine Änderungen um einen Arbeitspunkt linear beschreibt ([Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung.html)). In Schaltungssimulatoren heißt es __Level-1-Modell__ oder __Shichman-Hodges-Modell__.

:::frage
„Warum hat das Ersatzschaltbild einen Bulk-Anschluss, wenn $U_{BS}$ in den Gleichungen gar nicht vorkommt?“
Die Gleichungen gelten für $U_{BS}$ = 0. Liegt der Bulk tiefer als die Source, wird die Verarmungszone unter dem Gate breiter, und die Gatespannung muss deren zusätzliche Ladung mittragen, bevor ein Kanal entsteht: Die Schwellenspannung steigt. Dieser __Substrateffekt__ steckt im Modell in $U_{th}$; behandelt wird er im Artikel über PMOS-Transistor, Substrateffekt und Latch-Up.
:::

:::formel Formel
Sperrbereich, $U_{GS} < U_{th}$:

$$I_D = 0$$

Ohmscher Bereich, $U_{GS} > U_{th}$ und $U_{DS} < U_{GS} - U_{th}$:

$$I_D = K_n\Big[\big(U_{GS} - U_{th}\big)\,U_{DS} - \frac{U_{DS}^2}{2}\Big]\big(1 + \lambda\,U_{DS}\big)$$

Abschnürbereich, $U_{GS} > U_{th}$ und $U_{DS}$ ab $U_{GS} - U_{th}$:

$$I_D = \frac{K_n}{2}\,\big(U_{GS} - U_{th}\big)^2\,\big(1 + \lambda\,U_{DS}\big)$$
:::

**So liest man das:** Eingaben sind $U_{GS}$ und das nicht negative $U_{DS}$, Ausgabe ist $I_D$. Zuerst bestimmt man den Bereich, dann den Strom. Der Faktor $(1 + \lambda U_{DS})$ steht auch im ohmschen Bereich, obwohl der Kanal dort nicht verkürzt ist; so stimmen beide Gleichungen an der Grenze in Wert und Steigung überein, und die Kennlinie hat weder Sprung noch Knick. Im ohmschen Bereich ändert er den Strom um höchstens λ($U_{GS} - U_{th}$), bei 1 V Gatespannung um 5 %. Der Strom null im Sperrbereich ist eine Näherung für einen sehr kleinen Strom.

Idee der Herleitung: Man setzt die Gleichungen der drei Bereiche zusammen und wählt den Faktor im ohmschen Bereich so, dass die Kennlinie an der Grenze glatt ist.

:::herleitung
**Ausgangspunkt:** der Sperrbereich aus [Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html), die Triodengleichung und das Quadratgesetz mit Kanallängenmodulation aus den Abschnitten *Die Triodengleichung* und *Kanallängenmodulation*.

**Annahmen:**
(i) Unterhalb der Schwelle wird der Strom vernachlässigt.
(ii) $U_{DS}$ ist nicht negativ; andernfalls tauschen Source und Drain die Rollen.
(iii) Im ohmschen Bereich wird der Faktor $(1 + \lambda U_{DS})$ übernommen; das ist eine Festlegung des Modells, keine Folge der Physik.

**Schritt 1**: Sperrbereich: Ohne Kanal fließt nach (i) kein Strom.

**Schritt 2**: Abschnürbereich: das Quadratgesetz mit dem Faktor der Kanallängenmodulation.

**Schritt 3**: Ohmscher Bereich: die Triodengleichung, nach (iii) mit demselben Faktor.

**Schritt 4** (entscheidender Schritt): Prüfung an der Grenze $U_{DS} = U_{GS} - U_{th}$. Der Wert der Triodengleichung ist dort $K_n(U_{GS} - U_{th})^2/2$; mit dem Faktor stimmen beide Ausdrücke überein. Die Ableitung des ohmschen Ausdrucks nach $U_{DS}$ ist nach der Produktregel

$$\begin{aligned} \frac{\partial I_D}{\partial U_{DS}} &= K_n\big(U_{GS} - U_{th} - U_{DS}\big)\big(1 + \lambda U_{DS}\big) \\ &\quad + \lambda K_n\Big[\big(U_{GS} - U_{th}\big)U_{DS} - \frac{U_{DS}^2}{2}\Big] \end{aligned}$$

An der Grenze verschwindet der erste Summand, und der zweite wird $\lambda K_n(U_{GS} - U_{th})^2/2$, genau die Steigung im Abschnürbereich.

**Ergebnis:** im Sperrbereich $I_D$ = 0, im ohmschen Bereich und im Abschnürbereich

$$I_D = K_n\Big[\big(U_{GS} - U_{th}\big)\,U_{DS} - \frac{U_{DS}^2}{2}\Big]\big(1 + \lambda\,U_{DS}\big)$$

$$I_D = \frac{K_n}{2}\,\big(U_{GS} - U_{th}\big)^2\,\big(1 + \lambda\,U_{DS}\big)$$

**Woher die Faktoren kommen:** Jeder Bereich bringt seine Gleichung mit; der gemeinsame Faktor sorgt für den glatten Übergang.

**Proben:** An der Grenze bei 1 V Gatespannung ergeben beide Ausdrücke 0,2625 mA, beide Steigungen 25 µA/V. Für λ = 0 ergeben sich Triodengleichung und Quadratgesetz.

**Grenzen:** Das Modell enthält weder den Unterschwellenstrom noch Kurzkanaleffekte noch die Abnahme der Beweglichkeit bei hoher Gatespannung; Simulatoren benutzen für den Entwurf genauere Modelle.
:::

Rechnet man eine Schaltung, kennt man den Bereich vorher nicht. Man nimmt einen an, meist den Abschnürbereich, berechnet den Arbeitspunkt und prüft die Bedingung; ist sie verletzt, rechnet man mit dem anderen Bereich neu.

::::beispiel Arbeitspunkt eines Transistors mit Drainwiderstand
**Gegeben:** der Beispieltransistor ($K_n$ = 2 mA/V², $U_{th}$ = 0,5 V, λ = 0,1 1/V), Source an Masse, ein Widerstand $R_D$ = 4 kΩ von der Versorgungsspannung $U_B$ = 2,5 V zum Drain; Gate-Source-Spannung (a) 1 V, (b) 1,5 V.

**Gesucht:** Drainstrom, Drain-Source-Spannung und Bereich.

:::grafik
Szene: st1/mos-feldeffekttransistoren/02-arbeitspunkt · Vorlage: schaltung-arbeitsgerade
**Abbildung 7:** (a) Schaltbild: Versorgungsspannung 2,5 V, Widerstand 4 kΩ zum Drain, NMOS mit Source an Masse, Gate an einer Spannungsquelle $U_{GS}$; Zählpfeile $I_D$ und $U_{DS}$. (b) Ausgangskennlinien mit λ = 0,1 1/V für $U_{GS}$ = 1 V und 1,5 V, dazu die Arbeitsgerade des Widerstands von 0,625 mA bei 0 V nach null bei 2,5 V und gestrichelt die Grenzparabel. Die Schnittpunkte sind die Arbeitspunkte: 1,36 V und 0,284 mA rechts der Grenzparabel, im Abschnürbereich; 0,31 V und 0,546 mA links davon, im ohmschen Bereich. Der Arbeitspunkt liegt im Schnitt von Kennlinie und Arbeitsgerade; auf welcher Seite der Grenzparabel, entscheidet über den Bereich.
:::

**Rechnung:** Für den Widerstand gilt die Maschenregel:

$$U_{DS} = U_B - R_D\,I_D$$

(a) Annahme Abschnürbereich, Strom 0,25 mA mal $(1 + \lambda U_{DS})$; $R_D$ mal 0,25 mA ist 1 V:

$$U_{DS} = 2{,}5\ \mathrm V - 1\ \mathrm V\cdot\big(1 + 0{,}1\ \mathrm{V^{-1}}\cdot U_{DS}\big)$$

$$U_{DS} = \frac{1{,}5\ \mathrm V}{1{,}1} = 1{,}364\ \mathrm V, \qquad I_D = \frac{2{,}5\ \mathrm V - 1{,}364\ \mathrm V}{4\ \mathrm{k\Omega}} = 0{,}284\ \mathrm{mA}\,$$

1,364 V liegt über der Abschnürspannung 0,5 V; die Annahme stimmt.

(b) Annahme Abschnürbereich, Strom 1 mA mal $(1 + \lambda U_{DS})$; $R_D$ mal 1 mA ist 4 V:

$$U_{DS} = 2{,}5\ \mathrm V - 4\ \mathrm V\cdot\big(1 + 0{,}1\ \mathrm{V^{-1}}\cdot U_{DS}\big)$$

$$U_{DS} = \frac{-1{,}5\ \mathrm V}{1{,}4} = -1{,}07\ \mathrm V$$

Das widerspricht der Annahme, die mindestens 1 V verlangt. Neue Annahme ohmscher Bereich, zunächst ohne den kleinen Faktor $(1 + \lambda U_{DS})$:

$$2\ \mathrm{\frac{mA}{V^2}}\cdot\Big(1\ \mathrm V\cdot U_{DS} - \frac{U_{DS}^2}{2}\Big)\cdot4\ \mathrm{k\Omega} = 2{,}5\ \mathrm V - U_{DS}$$

$$4\,U_{DS}^2 - 9\ \mathrm V\cdot U_{DS} + 2{,}5\ \mathrm{V^2} = 0$$

$$U_{DS} = \frac{9 - \sqrt{41}}{8}\ \mathrm V = 0{,}325\ \mathrm V$$

Die zweite Lösung, 1,93 V, liegt außerhalb des ohmschen Bereichs. Der Strom ist (2,5 V − 0,325 V)/4 kΩ = 0,544 mA; mit dem Faktor $(1 + \lambda U_{DS})$ ergibt die numerische Lösung 0,314 V und 0,546 mA.

**Ergebnis:** **(a) 0,284 mA bei 1,36 V, Abschnürbereich; (b) 0,546 mA bei 0,31 V, ohmscher Bereich.**

**Einordnung:** Bei 1 V Gatespannung arbeitet der Transistor als Stromquelle, und kleine Änderungen von $U_{GS}$ ändern über $R_D$ die Drainspannung: Die Schaltung verstärkt. Bei 1,5 V zieht er den Drain auf 0,3 V herunter und wirkt als geschlossener Schalter mit 575 Ω zwischen Drain und Source.
::::

:::frage
„Fließt unterhalb der Schwellenspannung wirklich kein Strom?“
Doch, ein kleiner: Einige Elektronen gelangen mit ihrer Wärmeenergie über die Barriere zwischen Source und Oberfläche, wie in einer Diode, und diffundieren zum Drain. Der Strom fällt exponentiell, beim Beispieltransistor um eine Zehnerpotenz je 83 mV weniger Gatespannung; bei $U_{GS}$ = 0 sind es 0,56 pA, neun Milliarden Mal weniger als die 5 mA, die der Transistor bei $U_{GS}$ und $U_{DS}$ von je 2,5 V führt. Steiler als eine Dekade je 59,5 mV kann er bei Raumtemperatur nicht fallen, weil die Boltzmann-Verteilung die Zahl der Elektronen über einer Barriere je 59,5 mV Barrierenhöhe nur um den Faktor 10 ändert. In einem Chip mit einer Milliarde Transistoren summiert sich der Strom zu 0,56 mA; deshalb lassen sich Schwellenspannungen nicht beliebig senken.
:::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Triodengleichung | der gleiche Strom in jedem Querschnitt, über den ganzen Kanal aufsummiert |
| Krümmung der Kennlinie | jede weitere Drainspannung trifft am Drain-Ende auf weniger Ladung |
| Maximum der Parabel an der Abschnürgrenze | am Drain-Ende ist die Ladung aufgebraucht; weitere Spannung findet keinen Kanal mehr |
| Quadratgesetz | der Kanal bis zum Abschnürpunkt sieht immer die Gate-Übersteuerung; Ladung und Spannung wachsen beide mit ihr |
| Kanallängenmodulation | derselbe Kanal, nur kürzer: bei gleicher Spannung mehr Strom |

Durch jeden Querschnitt des Kanals fließt derselbe Strom, das Produkt aus Elektronenladung pro Länge und Geschwindigkeit der Elektronen; wo der Kanal zum Drain hin dünner wird, laufen die Elektronen schneller, und aus dieser Bedingung folgt die Triodengleichung, deren Maximum genau an der Abschnürgrenze liegt und die von dort an als Quadratgesetz stehen bleibt, bis auf einen leichten Anstieg, weil der Kanal mit wachsender Drainspannung kürzer wird.

## Bedeutung und Ausblick

Digitale CMOS-Gatter laden ihre Lasten erst mit dem Sättigungsstrom und dann im ohmschen Bereich um; Verstärker und Stromquellen arbeiten im Abschnürbereich, wo die Steigungen der Kennlinien, 1 mS und 25 µS bei 1 V Gatespannung, das Kleinsignalmodell bilden. Die Grenzen des Modells liegen bei kurzen Kanälen, bei hohen Gatespannungen, wo die Beweglichkeit sinkt, und unterhalb der Schwelle. Der nächste Artikel, PMOS-Transistor, Substrateffekt und Latch-Up, überträgt die Gleichungen auf den PMOS.

**In der ausführlichen Fassung:** der Verlauf des Kanalpotentials und die Laufzeit der Elektronen, eine negative Drain-Source-Spannung, die Bestimmung der Schwellenspannung aus der Wurzel des Sättigungsstroms, warum gemessene λ größer sind als die eindimensionale Abschätzung, wie ein Schaltungssimulator das Modell verwendet und der Strom unterhalb der Schwelle mit Herleitung und Unterschwellensteigung ([Kennlinien des NMOS-Transistors, ausführlich](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien-ausfuehrlich.html)).

:::kern
- Durch jeden Querschnitt des Kanals fließt derselbe Strom; wo der Kanal dünner ist, laufen die Elektronen schneller.
- Ohmscher Bereich: $I_D = K_n[(U_{GS} - U_{th})U_{DS} - U_{DS}^2/2]$; für kleine Drain-Source-Spannung ein durch die Gatespannung steuerbarer Widerstand.
- Das Maximum der Triodenparabel liegt genau an der Abschnürgrenze $U_{DS} = U_{GS} - U_{th}$; dahinter gilt die Parabel nicht.
- Abschnürbereich: $I_D = \tfrac{K_n}{2}(U_{GS} - U_{th})^2$, quadratisch in der Übersteuerung, nicht in der Gatespannung.
- Kanallängenmodulation: Faktor $(1 + \lambda U_{DS})$; im Modell treffen sich die verlängerten Kennlinien bei der negativen Early-Spannung.
- Großsignalmodell: Gate stromlos, zwischen Drain und Source eine gesteuerte Stromquelle; Bereich annehmen, rechnen, Bedingung prüfen.
:::

:::quiz
F: Warum laufen die Elektronen am Drain-Ende des Kanals schneller als an der Source?
A: Durch jeden Querschnitt fließt derselbe Strom, Ladung pro Länge mal Geschwindigkeit. Zum Drain hin sinkt die Ladung, bei 1 V und 0,3 V auf 40 %; die Elektronen müssen dort 2,5-mal so schnell sein, und dafür braucht es ein 2,5-mal so starkes treibendes Feld.
F: Warum liegt das Maximum der Triodenparabel genau an der Abschnürgrenze?
A: Die Steigung der Parabel ist $K_n$ mal der Übersteuerung am Drain-Ende. Sie wird null, wenn dort keine Ladung mehr ist, und das ist die Bedingung für das Abschnüren, $U_{DS} = U_{GS} - U_{th}$.
F: Stimmt es, dass der Strom hinter dem Maximum der Parabel wieder abnimmt?
A: Nein. Der abfallende Ast beschriebe einen Kanal mit einer negativen Zahl von Elektronen am Drain-Ende. Tatsächlich endet der Kanal am Abschnürpunkt mit dem Potential $U_{GS} - U_{th}$ und führt weiter den Strom der Grenze, beim Beispieltransistor 0,25 mA bei 1 V Gatespannung.
F: Stimmt es, dass doppelte Gatespannung den vierfachen Strom ergibt?
A: Nein. Quadriert wird die Übersteuerung $U_{GS} - U_{th}$. Von 1 V auf 2 V Gatespannung steigt sie von 0,5 V auf 1,5 V, der Strom von 0,25 mA auf 2,25 mA, um den Faktor 9.
F: Welchen Strom führt der Beispieltransistor bei $U_{GS}$ = 1 V und $U_{DS}$ = 0,3 V, und wie viel ergäbe die Widerstandsgerade mit 1 kΩ?
A: 2 mA/V² · (0,15 V² − 0,045 V²) = 0,21 mA gegen 0,3 mA nach der Geraden, also 70 %, weil der Kanal zum Drain hin dünner wird.
F: Wie stellt man fest, ob der Transistor mit 4 kΩ an 2,5 V bei $U_{GS}$ = 1,5 V im Abschnürbereich arbeitet?
A: Man nimmt den Abschnürbereich an und rechnet: Mit 1 mA mal $(1 + \lambda U_{DS})$ ergäbe die Maschenregel −1,07 V, weniger als die nötigen 1 V. Die Annahme ist falsch; im ohmschen Bereich ergeben sich 0,31 V und 0,546 mA.
:::
