---
title: Kennlinien des NMOS-Transistors
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / MOS-Feldeffekttransistoren
order: 33030200
summary: Wie der Drainstrom eines n-Kanal-MOSFET von der Gate-Source- und der Drain-Source-Spannung abhängt und warum seine Ausgangskennlinien erst ansteigen und dann fast waagerecht verlaufen. Ausführliche Fassung mit Herleitung der Triodengleichung aus der Bedingung gleichen Stroms in jedem Querschnitt, Kanalpotential und Laufzeit der Elektronen, Quadratgesetz, Bestimmung der Schwellenspannung, Kanallängenmodulation mit Early-Spannung, Großsignalmodell mit Arbeitspunktberechnung und Strom unterhalb der Schwelle, durchgerechnet am Beispieltransistor mit 2 mA/V².
tags: ohmscher Bereich, Abschnürbereich, Quadratgesetz, Kanallängenmodulation, Ausgangskennlinie
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Wer eine Schaltung mit MOS-Feldeffekttransistoren entwirft oder nachrechnet, braucht eine Gleichung für den Drainstrom: Wie viel Strom fließt bei einer gegebenen Gate-Source- und Drain-Source-Spannung? Wie der Kanal entsteht, warum er zum Drain hin dünner wird und wo er abschnürt, zeigt [Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html); dieser Artikel macht daraus den Strom. Alles hängt an einem Prinzip:

**Durch jeden Querschnitt des Kanals fließt derselbe Strom, das Produkt aus Elektronenladung pro Länge und Geschwindigkeit der Elektronen; wo der Kanal zum Drain hin dünner wird, laufen die Elektronen schneller, und aus dieser Bedingung folgt die Triodengleichung, deren Maximum genau an der Abschnürgrenze liegt und die von dort an als Quadratgesetz stehen bleibt, bis auf einen leichten Anstieg, weil der Kanal mit wachsender Drainspannung kürzer wird.**

Vorausgesetzt werden der Aufbau des MOSFET, die örtliche Kanalladung und die Abschnürung aus dem genannten Artikel sowie die Drift von Ladungsträgern im elektrischen Feld aus [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell-ausfuehrlich.html). Auf den Kennlinien bauen der PMOS, der Substrateffekt, das Kleinsignalmodell und alle Transistorschaltungen auf.

:::grafik
Szene: st1/mos-feldeffekttransistoren/02-kennlinienfeld · Vorlage: kennlinienfeld
**Abbildung 1:** (a) Ausgangskennlinienfeld des Beispieltransistors ohne Kanallängenmodulation: Drainstrom $I_D$ über der Drain-Source-Spannung $U_{DS}$ von 0 bis 2,5 V für $U_{GS}$ = 0,75 V, 1 V, 1,25 V und 1,5 V. Jede Kurve steigt im ohmschen Bereich (hellblau) an, erreicht auf der gestrichelten Grenzparabel bei $U_{DS} = U_{GS} - U_{th}$ = 0,25 V, 0,5 V, 0,75 V und 1 V ihren Höchstwert und verläuft im Abschnürbereich (hellorange) waagerecht bei 0,0625 mA, 0,25 mA, 0,5625 mA und 1 mA. (b) Übertragungskennlinie im Abschnürbereich: $I_D$ über $U_{GS}$, null bis zur Schwellenspannung 0,5 V, dann eine Parabel bis 1 mA bei 1,5 V. Der Strom steigt erst mit der Drainspannung und bleibt dann stehen; seine Höhe wächst quadratisch mit der Gate-Übersteuerung.
:::

## Ausgangs- und Übertragungskennlinie

*Wie stellt man dar, dass der Drainstrom von zwei Spannungen zugleich abhängt?*

Alle Spannungen werden gegen die Source gemessen: die Gate-Source-Spannung $U_{GS}$ und die Drain-Source-Spannung $U_{DS}$. Der Bulk liegt an der Source; wie eine Spannung zwischen Bulk und Source die Schwelle verschiebt, behandelt ein eigener Artikel. Der Drainstrom $I_D$ wird in den Drain hinein gezählt. Das Gate ist durch das Oxid isoliert und nimmt bei Gleichspannung keinen Strom auf, deshalb fließt derselbe Strom aus der Source heraus. Ein Strom und zwei Spannungen beschreiben den Transistor vollständig.

Der Strom hängt von beiden Spannungen ab. Der Beispieltransistor, ein NMOS mit der Kanalweite $W$ = 10 µm, der Kanallänge $L$ = 1 µm, der Schwellenspannung $U_{th}$ = 0,5 V, ab der sich ein Kanal bildet, und dem Steilheitskoeffizienten $K_n$ = 2 mA/V², der Größe, die Beweglichkeit der Elektronen, Kapazität des Gateoxids pro Fläche und das Verhältnis $W/L$ zusammenfasst, führt bei $U_{GS}$ = 1 V und $U_{DS}$ = 0,3 V den Strom 0,21 mA, bei derselben Gatespannung und 2 V Drainspannung 0,25 mA und bei 1,5 V Gatespannung und 2 V Drainspannung 1 mA. Eine solche Funktion zweier Spannungen zeichnet man als Schnitte, bei denen jeweils eine Spannung festgehalten wird.

Hält man $U_{GS}$ fest und trägt $I_D$ über $U_{DS}$ auf, erhält man eine __Ausgangskennlinie__. Ausgang heißt die Seite zwischen Drain und Source, weil dort in Schaltungen die Last angeschlossen ist. Mehrere Ausgangskennlinien für verschiedene Werte von $U_{GS}$, dem __Parameter__ der Schar, bilden das __Ausgangskennlinienfeld__ (Abbildung 1a). Hält man umgekehrt $U_{DS}$ fest und trägt $I_D$ über $U_{GS}$ auf, erhält man die __Übertragungskennlinie__, auch Transfer- oder Steuerkennlinie (Abbildung 1b). Sie zeigt, wie die Spannung am Eingang den Strom am Ausgang steuert.

In Abbildung 1a steigt jede Kurve zunächst fast geradlinig an, biegt dann ab und läuft ab einer bestimmten Drainspannung waagerecht weiter. Die Punkte, an denen sie waagerecht werden, liegen bei $U_{DS} = U_{GS} - U_{th}$ auf der gestrichelten Parabel. Links davon reicht der Kanal bis zum Drain, der __ohmsche Bereich__; rechts davon ist er vor dem Drain abgeschnürt, der __Abschnürbereich__. Unterhalb der Schwelle gibt es keinen Kanal, und die Kennlinie liegt im __Sperrbereich__ auf der Nulllinie. Diese drei Bereiche und die Abschnürung selbst erklärt [Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html). Auffällig ist, dass die waagerechten Stücke nicht gleichmäßig höher werden: Von 0,75 V auf 1 V Gatespannung steigt der Strom um 0,19 mA, von 1,25 V auf 1,5 V um 0,44 mA.

Der Kanal des Beispieltransistors ist 1 µm lang. Das ist lang genug, dass die Elektronen im Kanal weit unter ihrer Höchstgeschwindigkeit in Silizium bleiben und das Feld längs des Kanals klein ist gegen das Feld senkrecht zur Oberfläche. Für einen solchen __Langkanaltransistor__ gelten die Gleichungen dieses Artikels. Den leichten Anstieg des Stroms im Abschnürbereich, den die Verkürzung des Kanals bewirkt, lässt der Artikel bis zum Abschnitt *Kanallängenmodulation* außer Acht; alle Zahlen bis dahin, auch die oben genannten, gelten ohne ihn.

## Derselbe Strom in jedem Querschnitt

*Wie kann durch einen Kanal, der zum Drain hin dünner wird, überall derselbe Strom fließen?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/02-kanal-geschwindigkeit · Vorlage: profil-gestapelt
**Abbildung 2:** Drei gestapelte Diagramme über dem Ort $x/L$ von der Source (0) zum Drain (1) bei $U_{GS}$ = 1 V und $U_{DS}$ = 0,3 V, Drainstrom 0,21 mA; darüber der Kanal als Band, dessen Dicke der Ladung folgt. (a) Kanalpotential $U(x)$: 0, 56, 119, 196 und 300 mV bei $x/L$ = 0, 0,25, 0,5, 0,75 und 1, zum Drain hin immer steiler. (b) Elektronenladung in Prozent ihres Werts an der Source: 100, 89, 76, 61 und 40 %. (c) mittlere Geschwindigkeit der Elektronen: 6,1·10⁵ cm/s an der Source, 8,0·10⁵ cm/s in der Mitte, 1,52·10⁶ cm/s am Drain-Ende. Wo der Kanal dünner ist, laufen die Elektronen schneller; das Produkt aus Ladung und Geschwindigkeit, der Strom, ist überall gleich.
:::

**Die Akteure:**

- __$x$__, __$U(x)$__, __$Q'_n(x)$__: Ort längs des Kanals, von 0 an der Source bis $L$ am Drain; __Kanalpotential__, das Potential des Kanals an der Stelle $x$ gegenüber der Source, 0 an der Source und $U_{DS}$ am Drain; Elektronenladung pro Fläche, nach [Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html) proportional zur örtlichen Übersteuerung $U_{GS} - U_{th} - U(x)$, an der Source bei $U_{GS}$ = 1 V −3,45 fC/µm².
- __$v_n(x)$__: mittlere Geschwindigkeit der Elektronen an der Stelle $x$, in cm/s, zum Drain hin gerichtet; 6,1·10⁵ cm/s an der Source bei $U_{GS}$ = 1 V und $U_{DS}$ = 0,3 V. Sie legt zusammen mit der Ladung fest, wie viel Ladung pro Sekunde einen Querschnitt passiert.
- __$E_x(x)$__: treibende Feldstärke längs des Kanals, das negative Gefälle des Kanalpotentials, in V/cm; zum größten Teil das elektrische Feld an der Oberfläche, zu einem kleinen Teil der Antrieb der Diffusion (Herleitung, Annahme (iii)). Weil $U(x)$ zum Drain hin steigt, zeigt sie zur Source; sie treibt die negativ geladenen Elektronen zum Drain. Betrag an der Source im selben Arbeitspunkt 2,1 kV/cm.
- __$\mu_n$__: Beweglichkeit der Elektronen im Kanal, ihre Driftgeschwindigkeit pro Feldstärke; 290 cm²/(V s).

**Das Zusammenspiel:**

**Schritt 1**: Der Strom durch einen Querschnitt ergibt sich aus Ladung und Geschwindigkeit. Liegt auf jedem Zentimeter Kanallänge die Ladung $W|Q'_n|$ und bewegt sie sich mit der Geschwindigkeit $v_n$, so passiert in einer Sekunde die Ladung einer Strecke der Länge $v_n$ den Querschnitt. Der Strom ist Ladung pro Länge mal Geschwindigkeit. Die Elektronen laufen von der Source zum Drain; der Strom fließt, weil ihre Ladung negativ ist, in Gegenrichtung, vom Drain zur Source, und damit in den Drain hinein.

**Schritt 2**: Dieser Strom ist in jedem Querschnitt derselbe. Flösse in ein Stück des Kanals mehr hinein als heraus, sammelte sich dort Ladung an, und das veränderte Potential des Stücks würde den Zufluss bremsen und den Abfluss beschleunigen, bis beide gleich sind; bei Gleichspannungen ist dieser Ausgleich längst abgeschlossen. Seitlich kommt nichts hinzu: Das Gate ist isoliert, und die Übergänge zum Bulk sperren. Es ist die Knotenregel, angewandt auf jedes Stück des Kanals.

**Schritt 3** (entscheidender Schritt): Zum Drain hin nimmt die Ladung ab, weil dort die Spannung zwischen Gate und Kanal kleiner ist. Bei $U_{GS}$ = 1 V und $U_{DS}$ = 0,3 V bleiben am Drain-Ende 40 % der Ladung an der Source. Damit das Produkt aus Ladung und Geschwindigkeit gleich bleibt, müssen die Elektronen dort 2,5-mal so schnell sein, 1,52·10⁶ cm/s statt 6,1·10⁵ cm/s (Abbildung 2c).

**Schritt 4**: Die Geschwindigkeit ist Beweglichkeit mal treibende Feldstärke. Die höhere Geschwindigkeit verlangt ein 2,5-mal so starkes treibendes Feld, 5,25 kV/cm am Drain-Ende statt 2,1 kV/cm an der Source. Das Feld ist das Gefälle des Kanalpotentials, deshalb steigt $U(x)$ zum Drain hin immer steiler an (Abbildung 2a): Auf halber Länge sind erst 119 mV erreicht, nicht die Hälfte von 300 mV.

**Schritt 5**: Ladung und Feld hängen beide vom Kanalpotential ab, die Ladung über die örtliche Spannung zwischen Gate und Kanal, das Feld über das Gefälle. Die Bedingung gleichen Stroms wird so zu einer Gleichung für $U(x)$, die den Strom bereits enthält:

:::formel Formel
$$I_D = \mu_n\,W\,C'_\mathrm{ox}\,\big(U_{GS} - U_{th} - U(x)\big)\,\frac{dU}{dx}$$
:::

**So liest man das:** An jeder Stelle $x$ ergibt das Produkt aus der örtlichen Übersteuerung, die die Ladung festlegt, und dem Potentialgefälle, das die Geschwindigkeit festlegt, denselben Strom $I_D$. Wo die örtliche Übersteuerung klein ist, muss das Gefälle groß sein. Ohne Drainspannung ist das Gefälle überall null, und es fließt kein Strom, obwohl der Kanal voller Elektronen ist.

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

::::beispiel Treibendes Feld und Geschwindigkeit an Source und Drain-Ende bei 0,21 mA
**Gegeben:** $\mu_n$ = 290 cm²/(V s), $W$ = 10 µm = 10⁻³ cm, $C'_\mathrm{ox}$ = 6,906·10⁻⁷ F/cm², $U_{th}$ = 0,5 V; Arbeitspunkt $U_{GS}$ = 1 V, $U_{DS}$ = 0,3 V, in dem der Transistor 0,21 mA führt.

**Gesucht:** Ladung pro Länge, Geschwindigkeit und treibende Feldstärke an der Source und am Drain-Ende.

**Rechnung:** Die örtliche Übersteuerung ist an der Source 0,5 V, am Drain-Ende 0,5 V − 0,3 V = 0,2 V. Ladung pro Länge an der Source:

$$W\,|Q'_n(0)| = 10^{-3}\ \mathrm{cm}\cdot6{,}906\cdot10^{-7}\ \mathrm{F/cm^2}\cdot0{,}5\ \mathrm V = 3{,}45\cdot10^{-10}\ \mathrm{C/cm}$$

Am Drain-Ende mit 0,2 V statt 0,5 V das 0,4-Fache, 1,38·10⁻¹⁰ C/cm. Geschwindigkeit als Strom durch Ladung pro Länge:

$$v_n(0) = \frac{2{,}1\cdot10^{-4}\ \mathrm A}{3{,}45\cdot10^{-10}\ \mathrm{C/cm}} = 6{,}08\cdot10^{5}\ \mathrm{cm/s}$$

$$v_n(L) = \frac{2{,}1\cdot10^{-4}\ \mathrm A}{1{,}38\cdot10^{-10}\ \mathrm{C/cm}} = 1{,}52\cdot10^{6}\ \mathrm{cm/s}$$

Treibende Feldstärke als Geschwindigkeit durch Beweglichkeit:

$$|E_x(0)| = \frac{6{,}08\cdot10^{5}\ \mathrm{cm/s}}{290\ \mathrm{cm^2/(V\,s)}} = 2{,}10\ \mathrm{kV/cm}$$

Am Drain-Ende ist die Geschwindigkeit 2,5-mal so groß, ebenso das Feld: 5,25 kV/cm.

**Ergebnis:** **An der Source 3,45·10⁻¹⁰ C/cm, 6,1·10⁵ cm/s und 2,1 kV/cm; am Drain-Ende 1,38·10⁻¹⁰ C/cm, 1,52·10⁶ cm/s und 5,25 kV/cm.**

**Einordnung:** Die Elektronen legen im Kanal 6 bis 15 Kilometer pro Sekunde zurück, rund hundertmillionenmal so schnell wie die Elektronen in einem Kupferdraht mit 1 A pro mm², die sich mit 0,07 mm/s bewegen. Der Grund ist ihre geringe Zahl: Den Strom von 0,21 mA tragen die rund 1,6·10⁵ Elektronen, die sich gerade im Kanal befinden, während im Kupfer auf jeden Kubikzentimeter 8,5·10²² freie Elektronen kommen. Das elektrische Feld selbst ist um den Anteil der Diffusion kleiner, 1,99 kV/cm an der Source und 4,57 kV/cm am Drain-Ende. Selbst am Drain-Ende erreichen die Elektronen nur 15 % ihrer Höchstgeschwindigkeit von rund 10⁷ cm/s; die Annahme einer Geschwindigkeit proportional zum Feld ist beim 1 µm langen Kanal näherungsweise erfüllt. Je nach Modell der Geschwindigkeitssättigung bleibt die Geschwindigkeit am Drain-Ende um 1 bis 13 % hinter dem Produkt aus Beweglichkeit und Feld zurück.
::::

## Die Triodengleichung

*Wie groß ist der Drainstrom, solange der Kanal bis zum Drain reicht?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/02-flaeche-uebersteuerung · Vorlage: flaeche-teilbilder
**Abbildung 3:** Örtliche Übersteuerung $U_{GS} - U_{th} - U$, proportional zur Elektronenladung pro Fläche, aufgetragen über dem Kanalpotential $U$ bei $U_{GS}$ = 1 V: eine fallende Gerade von 0,5 V bei $U$ = 0 auf null bei $U$ = 0,5 V, rechts davon gestrichelt ohne Elektronen. (a) $U_{DS}$ = 0,3 V: Die Fläche von 0 bis 0,3 V ist in drei Streifen von je 0,1 V geteilt, mit den Höhen 0,45 V, 0,35 V und 0,25 V in der Streifenmitte; zusammen 0,105 V², mal $K_n$ ergibt 0,21 mA. (b) $U_{DS}$ = 0,5 V: das volle Dreieck, 0,125 V², 0,25 mA. (c) $U_{DS}$ = 0,75 V: dasselbe Dreieck, denn zwischen 0,5 V und 0,75 V gibt es keinen Kanal; der Strom bleibt 0,25 mA. Der Drainstrom ist $K_n$ mal der Fläche unter der Übersteuerung; sie wächst nur, bis die Übersteuerung am Drain-Ende null ist.
:::

Die Gleichung des vorigen Abschnitts gilt an jeder Stelle des Kanals mit demselben Strom. Wie daraus der Strom folgt, zeigt zunächst ein konkreter Fall. Man teilt die Drain-Source-Spannung von 0,3 V in drei Stufen von je 0,1 V und betrachtet das Stück des Kanals, auf dem das Kanalpotential von 0 auf 0,1 V steigt. Auf ihm beträgt die örtliche Übersteuerung im Mittel 0,45 V. Nach der Stromgleichung ist dieses Stück umso länger, je mehr Ladung es trägt: Der Strom mal seine Länge ist $\mu_n W C'_\mathrm{ox}$ mal 0,45 V mal 0,1 V. Für die Stücke von 0,1 V bis 0,2 V und von 0,2 V bis 0,3 V gilt dasselbe mit 0,35 V und 0,25 V. Die drei Stücke zusammen sind der ganze Kanal:

$$\begin{aligned} I_D\,L &= \mu_n\,W\,C'_\mathrm{ox}\cdot0{,}1\ \mathrm V\cdot\big(0{,}45 + 0{,}35 + 0{,}25\big)\ \mathrm V \\ &= \mu_n\,W\,C'_\mathrm{ox}\cdot0{,}105\ \mathrm{V^2} \end{aligned}$$

Geteilt durch $L$ steht vorn $K_n$, und es folgt $I_D$ = 2 mA/V² · 0,105 V² = 0,21 mA. Nebenbei ergibt sich, wie lang die Stücke sind: Sie verhalten sich wie 0,45 zu 0,35 zu 0,25. Das Stück an der Source ist fast doppelt so lang wie das am Drain, weil dort viele langsame Elektronen den Strom tragen; auf ihm steigt das Potential am langsamsten.

Die Summe ist die Fläche unter der Geraden in Abbildung 3a, die die örtliche Übersteuerung über dem Kanalpotential zeigt. Weil die Übersteuerung linear mit dem Potential fällt, gibt der Wert in der Mitte jedes Streifens dessen Fläche exakt wieder, und die Zahl der Stufen spielt keine Rolle. Allgemein ist $I_D L$ das Produkt aus $\mu_n W C'_\mathrm{ox}$ und der Fläche unter der Übersteuerung zwischen dem Potential der Source und dem des Drains, mathematisch ein Integral über das Kanalpotential:

:::formel Formel
$$I_D = K_n\,\Big[\big(U_{GS} - U_{th}\big)\,U_{DS} - \frac{U_{DS}^2}{2}\Big]$$
:::

**So liest man das:** Die Gleichung gilt im ohmschen Bereich, für $U_{GS} > U_{th}$ und $U_{DS} < U_{GS} - U_{th}$. Eingaben sind beide Spannungen, Ausgabe ist der Drainstrom. Der erste Term ist der Strom eines Widerstands $R_\mathrm{on}$ mit der Übersteuerung an der Source; der zweite zieht ab, was der Kanal zum Drain hin an Ladung verliert. Der Faktor 1/2 macht aus den Übersteuerungen an Source und Drain-Ende ihren Mittelwert: Die Klammer ist $U_{DS}$ mal dem Mittelwert von $U_{GS} - U_{th}$ und $U_{GS} - U_{th} - U_{DS}$. Bei $U_{GS}$ = 1 V und $U_{DS}$ = 0,3 V sind das 0,35 V zwischen 0,5 V und 0,2 V.

**Kurz gesagt:** Im ohmschen Bereich ist der Strom so groß, als hätte der ganze Kanal überall den Mittelwert der Übersteuerungen von Source- und Drain-Ende.

Gemittelt wird dabei über das Kanalpotential, nicht über den Ort. Über die Länge gemittelt trägt der Kanal bei 1 V und 0,3 V 74 % der Ladung an der Source statt 70 %, weil die ladungsreichen Stücke nahe der Source länger sind.

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

::::beispiel Drainstrom im ohmschen Bereich bei 1 V Gatespannung
**Gegeben:** $K_n$ = 2 mA/V², $U_{th}$ = 0,5 V, $U_{GS}$ = 1 V; Drain-Source-Spannungen 0,1 V, 0,3 V und 0,5 V; zum Vergleich der Kanalwiderstand $R_\mathrm{on}$ = 1 kΩ.

**Gesucht:** der Drainstrom und sein Verhältnis zum Strom $U_{DS}/R_\mathrm{on}$ der Widerstandsgeraden.

**Rechnung:** Die Übersteuerung ist 0,5 V. Bei 0,1 V:

$$I_D = 2\ \mathrm{mA/V^2}\cdot\big(0{,}5\ \mathrm V\cdot0{,}1\ \mathrm V - 0{,}005\ \mathrm{V^2}\big) = 0{,}09\ \mathrm{mA}$$

Ebenso bei 0,3 V und 0,5 V:

$$I_D = 2\ \mathrm{mA/V^2}\cdot0{,}105\ \mathrm{V^2} = 0{,}21\ \mathrm{mA}, \qquad I_D = 2\ \mathrm{mA/V^2}\cdot0{,}125\ \mathrm{V^2} = 0{,}25\ \mathrm{mA}\,$$

Die Gerade ergibt 0,1 mA, 0,3 mA und 0,5 mA. Das Verhältnis ist der Mittelwert der Übersteuerungen geteilt durch die Übersteuerung an der Source:

$$\frac{I_D}{U_{DS}/R_\mathrm{on}} = 1 - \frac{U_{DS}}{2\,(U_{GS} - U_{th})} = 0{,}9;\ 0{,}7;\ 0{,}5$$

**Ergebnis:** **0,09 mA, 0,21 mA und 0,25 mA, also 90 %, 70 % und 50 % des Stroms der Widerstandsgeraden.**

**Einordnung:** Als Widerstand ist der Transistor nur bei kleiner Drain-Source-Spannung brauchbar. Bei 1 V Gatespannung weicht er bei 20 mV um 2 % von der Geraden ab (0,0196 mA statt 0,0200 mA), bei 0,75 V Gatespannung schon um 4 %. Wer ihn als steuerbaren Widerstand einsetzt, etwa in einem Analogschalter, hält deshalb die Spannung über ihm klein und die Gatespannung hoch.
::::

Abbildung 3 zeigt auch, warum der Strom langsamer wächst als die Drainspannung. Jede weitere Stufe von 0,1 V fügt einen Streifen hinzu, der niedriger ist als der vorige, weil am Drain-Ende weniger Ladung übrig ist: 0,45 V, 0,35 V, 0,25 V. Deshalb bleibt die Kennlinie hinter der Widerstandsgeraden zurück und krümmt sich nach unten. Weil der Strom in diesem Bereich mit der Drainspannung wächst und zugleich vom Gate gesteuert wird, ähneln die Kennlinien denen einer Triode, einer Elektronenröhre, deren Anodenstrom mit der Anodenspannung wächst und von der Spannung an einem Steuergitter abhängt ([Von der Röhre zum integrierten Schaltkreis](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/einfuhrung/geschichte-der-schaltungstechnik-ausfuehrlich.html)). Deshalb heißt der ohmsche Bereich auch __Triodenbereich__ und die Gleichung __Triodengleichung__.

:::frage
„Was geschieht, wenn die Drain-Source-Spannung negativ wird?“
Source und Drain sind baugleich; liegt der Anschluss namens Drain tiefer, übernimmt er die Rolle der Source, und die Elektronen fließen in Gegenrichtung. Setzt man die vertauschten Rollen ein, ergibt sich wieder die Triodengleichung mit $U_{GS}$ und $U_{DS}$. Sie gilt für negative $U_{DS}$, solange $U_{GS}$ über der Schwelle liegt, und abschnüren kann der Kanal in dieser Richtung nicht, weil am Anschluss Source, zu dem die Elektronen jetzt laufen, die Übersteuerung immer $U_{GS} - U_{th}$ bleibt. Bei $U_{GS}$ = 1 V fließen bei −0,1 V −0,11 mA und bei +0,1 V +0,09 mA, denn an der neuen Source beträgt die Übersteuerung 0,6 V statt 0,5 V (vernachlässigt ist dabei der Substrateffekt, der die Schwelle an der neuen Source etwas senkt); in beiden Richtungen leitet der Kanal wie ein Widerstand, und darauf beruhen Analogschalter. Liegt der Bulk auf dem Potential der Source, leitet allerdings ab etwa 0,6 V negativer Drainspannung zusätzlich die Diode zwischen Bulk und Drain.
:::

### Das Kanalpotential längs des Kanals

*Wie steigt das Potential von der Source zum Drain an, und wie lange braucht ein Elektron für den Weg?*

Integriert man die Stromgleichung nicht über den ganzen Kanal, sondern nur von der Source bis zur Stelle $x$, erhält man den Verlauf des Kanalpotentials, den Abbildung 2a zeigt. Am übersichtlichsten wird er für das Quadrat der örtlichen Übersteuerung:

:::formel Formel
$$\begin{aligned} \big(U_{GS} - U_{th} - U(x)\big)^2 &= \Big(1 - \frac{x}{L}\Big)\big(U_{GS} - U_{th}\big)^2 \\ &\quad + \frac{x}{L}\,\big(U_{GS} - U_{th} - U_{DS}\big)^2 \end{aligned}$$
:::

**So liest man das:** Eingaben sind der Ort und beide Spannungen, Ausgabe ist das Kanalpotential an diesem Ort. Das Quadrat der örtlichen Übersteuerung fällt längs des Kanals linear von seinem Wert an der Source auf seinen Wert am Drain-Ende. Die Übersteuerung selbst, die Wurzel daraus, fällt deshalb erst langsam und dann immer schneller, und das Potential steigt zum Drain hin immer steiler an. An der Abschnürgrenze ist der Wert am Drain-Ende null, und die Übersteuerung fällt wie die Wurzel aus $1 - x/L$ auf null.

**Kurz gesagt:** Im ohmschen Bereich nimmt das Quadrat der örtlichen Übersteuerung längs des Kanals gleichmäßig ab.

Idee der Herleitung: Man integriert die Stromgleichung bis zur Stelle $x$ und teilt durch das Ergebnis für den ganzen Kanal.

:::herleitung
**Ausgangspunkt:** Schritt 1 der Herleitung der Triodengleichung:

$$I_D\,dx = \mu_n\,W\,C'_\mathrm{ox}\,\big(U_{GS} - U_{th} - U\big)\,dU$$

**Annahmen:** dieselben wie für die Triodengleichung.

**Schritt 1**: Integration von der Source bis zur Stelle $x$, rechts von 0 bis $U(x)$. Die Stammfunktion lässt sich als Differenz zweier Quadrate schreiben:

$$I_D\,x = \frac{\mu_n\,W\,C'_\mathrm{ox}}{2}\Big[\big(U_{GS} - U_{th}\big)^2 - \big(U_{GS} - U_{th} - U(x)\big)^2\Big]$$

**Schritt 2**: Derselbe Ausdruck für den ganzen Kanal, also bis zum Drain-Ende, wo das Potential $U_{DS}$ erreicht:

$$I_D\,L = \frac{\mu_n\,W\,C'_\mathrm{ox}}{2}\Big[\big(U_{GS} - U_{th}\big)^2 - \big(U_{GS} - U_{th} - U_{DS}\big)^2\Big]$$

**Schritt 3** (entscheidender Schritt): Division von Schritt 1 durch Schritt 2; Strom und Vorfaktor kürzen sich heraus:

$$\frac{x}{L} = \frac{\big(U_{GS} - U_{th}\big)^2 - \big(U_{GS} - U_{th} - U(x)\big)^2}{\big(U_{GS} - U_{th}\big)^2 - \big(U_{GS} - U_{th} - U_{DS}\big)^2}$$

**Schritt 4**: Auflösen nach dem Quadrat der örtlichen Übersteuerung:

**Ergebnis:**

$$\begin{aligned} \big(U_{GS} - U_{th} - U(x)\big)^2 &= \Big(1 - \frac{x}{L}\Big)\big(U_{GS} - U_{th}\big)^2 \\ &\quad + \frac{x}{L}\,\big(U_{GS} - U_{th} - U_{DS}\big)^2 \end{aligned}$$

**Woher die Faktoren kommen:** Die Quadrate stammen aus der Stammfunktion der linear fallenden Übersteuerung; dass sie linear im Ort sind, folgt aus dem gleichen Strom in jedem Querschnitt.

**Proben:** An der Source ergibt sich das Potential null, am Drain-Ende $U_{DS}$. Zahlenwert in der Mitte bei 1 V und 0,3 V: (0,25 V² + 0,04 V²)/2 = 0,145 V², die Wurzel 0,381 V, also $U$ = 0,5 V − 0,381 V = 119 mV.

**Grenzen:** Wie bei der Triodengleichung; nahe der Abschnürgrenze versagt am Drain-Ende die Annahme des allmählichen Kanals.
:::

::::beispiel Kanalpotential und Laufzeit der Elektronen bei 1 V Gatespannung
**Gegeben:** $U_{GS}$ = 1 V, $U_{th}$ = 0,5 V, $U_{DS}$ = 0,3 V; $\mu_n$ = 290 cm²/(V s), $L$ = 1 µm, $W$ = 10 µm, $C'_\mathrm{ox}$ = 6,906·10⁻⁷ F/cm², $I_D$ = 0,21 mA.

**Gesucht:** (a) das Kanalpotential bei einem Viertel, der Hälfte und drei Vierteln der Kanallänge; (b) die Zeit, die ein Elektron von der Source zum Drain braucht, hier und an der Abschnürgrenze.

**Rechnung:** (a) Das Quadrat der Übersteuerung fällt linear von 0,25 V² auf 0,04 V², also um 0,0525 V² je Viertel:

$$\big(0{,}5\ \mathrm V - U\big)^2 = 0{,}1975;\ 0{,}145;\ 0{,}0925\ \mathrm{V^2}$$

$$U = 0{,}5\ \mathrm V - \big(0{,}444;\ 0{,}381;\ 0{,}304\big)\ \mathrm V = 56;\ 119;\ 196\ \mathrm{mV}$$

(b) Die Laufzeit folgt aus einer einfachen Bilanz: Alle Elektronen, die sich gerade im Kanal befinden, haben ihn nach einer Laufzeit verlassen und sind durch neue ersetzt. Die Laufzeit $t_\mathrm{L}$ ist deshalb der Betrag $Q_\mathrm{K}$ der Elektronenladung im Kanal geteilt durch den Strom.

:::herleitung
**Ausgangspunkt:** Laufzeit als Ladung im Kanal durch Strom, mit der Ladung pro Länge $W|Q'_n|$ und $dx$ aus Schritt 1 der Herleitung der Triodengleichung.

**Annahmen:** dieselben wie für die Triodengleichung.

**Schritt 1**: Ladung im Kanal; $dx$ wird durch das Potential ausgedrückt:

$$\begin{aligned} Q_\mathrm{K} &= \int_0^L W\,C'_\mathrm{ox}\big(U_{GS} - U_{th} - U\big)\,dx \\ &= \frac{\mu_n\,W^2\,\big(C'_\mathrm{ox}\big)^2}{I_D}\int_0^{U_{DS}}\big(U_{GS} - U_{th} - U\big)^2\,dU \end{aligned}$$

**Schritt 2**: Integrieren und durch $I_D$ teilen:

$$\begin{aligned} t_\mathrm{L} = \frac{Q_\mathrm{K}}{I_D} &= \frac{\mu_n\,W^2\,\big(C'_\mathrm{ox}\big)^2}{3\,I_D^2} \\ &\quad\cdot\Big[\big(U_{GS} - U_{th}\big)^3 - \big(U_{GS} - U_{th} - U_{DS}\big)^3\Big] \end{aligned}$$

**Schritt 3**: An der Abschnürgrenze ist die Übersteuerung am Drain-Ende null, der zweite Term also null, und die Triodengleichung ergibt dort den Strom

$$I_D = \frac{\mu_n\,C'_\mathrm{ox}\,W}{2\,L}\,\big(U_{GS} - U_{th}\big)^2$$

Eingesetzt in Schritt 2 kürzen sich $W$, $C'_\mathrm{ox}$ und eine Potenz von $\mu_n$:

**Ergebnis:**

$$t_\mathrm{L} = \frac{4\,L^2}{3\,\mu_n\,\big(U_{GS} - U_{th}\big)}$$

**Woher die Faktoren kommen:** Die dritten Potenzen stammen aus dem Integral über das Quadrat der Übersteuerung. An der Grenze trägt der Kanal im Mittel zwei Drittel der Ladung an der Source, und der Strom enthält den Faktor 1/2; zusammen ergibt das 4/3.

**Proben:** Einheit: cm² geteilt durch cm²/(V s) · V ergibt s. Je kürzer der Kanal, desto kürzer die Laufzeit, mit dem Quadrat von $L$: Der Weg wird kürzer und das Feld stärker.

**Grenzen:** Nahe dem Drain-Ende würde die Geschwindigkeit nach dem Modell über alle Grenzen wachsen; tatsächlich begrenzt sie die Höchstgeschwindigkeit. Der Beitrag dieses Stücks zur Laufzeit ist klein.
:::

Mit den Zahlen dieses Arbeitspunkts, 0,5 V Übersteuerung an der Source und 0,2 V am Drain-Ende, zuerst der Vorfaktor:

$$\begin{aligned} \mu_n\,W^2\big(C'_\mathrm{ox}\big)^2 &= 290\ \mathrm{\frac{cm^2}{V\,s}}\cdot10^{-6}\ \mathrm{cm^2}\cdot4{,}77\cdot10^{-13}\ \mathrm{\frac{F^2}{cm^4}} \\ &= 1{,}38\cdot10^{-16}\ \mathrm{\frac{C^2}{V^3\,s}} \end{aligned}$$

Ladung im Kanal und Laufzeit:

$$Q_\mathrm{K} = \frac{1{,}38\cdot10^{-16}\ \mathrm{C^2/(V^3\,s)}\cdot\big(0{,}125 - 0{,}008\big)\ \mathrm{V^3}}{3\cdot2{,}1\cdot10^{-4}\ \mathrm A} = 2{,}57\cdot10^{-14}\ \mathrm C$$

$$t_\mathrm{L} = \frac{2{,}57\cdot10^{-14}\ \mathrm C}{2{,}1\cdot10^{-4}\ \mathrm A} = 122\ \mathrm{ps}$$

An der Abschnürgrenze:

$$t_\mathrm{L} = \frac{4\cdot\big(10^{-4}\ \mathrm{cm}\big)^2}{3\cdot290\ \mathrm{cm^2/(V\,s)}\cdot0{,}5\ \mathrm V} = 92\ \mathrm{ps}$$

**Ergebnis:** **(a) 56 mV, 119 mV und 196 mV; (b) 122 ps bei 0,3 V und 92 ps an der Abschnürgrenze.**

**Einordnung:** Ein Elektron braucht für einen Mikrometer rund 0,1 ns. Bei 0,1 V Drainspannung sind es 347 ps, weil das Feld schwächer ist. Schneller als in dieser Laufzeit kann sich die Ladung im Kanal nicht umordnen; deshalb begrenzt die Kanallänge die Frequenzen, die ein Transistor verarbeiten kann, und das Quadrat von $L$ im Ergebnis erklärt, warum kürzere Transistoren so viel schneller sind.
::::

## Abschnürgrenze und Quadratgesetz

*Warum bleibt der Strom stehen, wenn die Drain-Source-Spannung die Gate-Übersteuerung überschreitet, und wie groß ist er dann?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/02-triode-parabel · Vorlage: kennlinie-gueltigkeit
**Abbildung 4:** Drainstrom über der Drain-Source-Spannung von 0 bis 1,2 V bei $U_{GS}$ = 1 V. Durchgezogen die Triodengleichung bis zu ihrem Maximum 0,25 mA bei 0,5 V, gestrichelt die Tangente im Ursprung mit 1 mS ($R_\mathrm{on}$ = 1 kΩ), die bei 0,1 V 0,1 mA statt 0,09 mA anzeigt. Jenseits von 0,5 V blass gestrichelt und durchgestrichen die rechnerische Fortsetzung der Parabel, die bei 0,75 V auf 0,1875 mA und bei 1 V auf null fiele; dagegen der tatsächliche Verlauf, ohne Kanallängenmodulation waagerecht bei 0,25 mA. Senkrechte Marke „Abschnürgrenze 0,5 V“. Die Triodengleichung erreicht ihr Maximum genau an der Abschnürgrenze; dahinter gilt sie nicht mehr, und der Strom bleibt beim Maximum stehen.
:::

**Das Zusammenspiel:**

**Schritt 1**: Als Funktion von $U_{DS}$ ist die Triodengleichung eine nach unten geöffnete Parabel (Abbildung 4). Sie beginnt im Ursprung mit der Steigung 1 mS des Kanalwiderstands, flacht ab und erreicht bei 0,5 V ihr Maximum von 0,25 mA.

**Schritt 2**: Ihre Steigung ist an jeder Stelle der Leitwert, den der Kanal hätte, wenn er überall so dünn wäre wie an seinem Drain-Ende, also $K_n$ mal der Übersteuerung dort: 0,8 mS bei 0,1 V Drainspannung, 0,4 mS bei 0,3 V. Ein zusätzliches Millivolt am Drain verteilt sich zwar über den ganzen Kanal, bei 0,3 V hebt es das Potential in der Kanalmitte um 0,26 mV. In Abbildung 3 kommt aber nur ein schmaler Streifen am Rand hinzu, dessen Höhe die Übersteuerung am Drain-Ende ist, und um diesen Streifen wächst der Strom.

**Schritt 3** (entscheidender Schritt): Die Steigung wird null, wenn die Übersteuerung am Drain-Ende null wird, bei $U_{DS} = U_{GS} - U_{th}$. Das ist genau die Abschnürgrenze: Das Maximum der Parabel und das Abschnüren des Kanals sind dieselbe Bedingung, keine zufällig zusammenfallenden Punkte. In Abbildung 3b ist die Fläche zum vollen Dreieck geworden.

**Schritt 4**: Jenseits davon fiele die Parabel wieder, bei 0,75 V auf 0,1875 mA und bei 1 V auf null (gestrichelt in Abbildung 4). Ihre Herleitung setzt aber voraus, dass der Kanal bis zum Drain reicht, und das ist nicht mehr der Fall. Der Kanal endet am Abschnürpunkt, an dem seine Ladung null ist; dort hat er also genau das Potential $U_{GS} - U_{th}$. Den Rest der Drainspannung nimmt die kurze verarmte Zone zwischen Abschnürpunkt und Drain auf, deren starkes Feld jedes ankommende Elektron zum Drain zieht ([Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html)).

**Schritt 5**: Der Kanal von der Source bis zum Abschnürpunkt sieht deshalb immer dieselbe Spannung $U_{GS} - U_{th}$ und ist, solange die Zone kurz gegen $L$ bleibt, praktisch so lang wie vorher. Er führt den Strom der Abschnürgrenze, das Maximum der Parabel. In Abbildung 3c kommt keine Fläche mehr hinzu, weil es jenseits von $U_{GS} - U_{th}$ keine Elektronen im Kanal gibt.

:::fehlvorstellung
„Hinter dem Maximum der Parabel nimmt der Strom wieder ab.“ Das liegt nahe, weil die Triodengleichung eine vollständige Parabel ist und man eine Formel gern über ihren ganzen Definitionsbereich benutzt. Der Strom bleibt aber beim Maximum stehen, ohne Kanallängenmodulation bei 0,25 mA für 0,5 V, 1 V und 2 V Drainspannung, statt 0,1875 mA bei 0,75 V und null bei 1 V, wie die fortgesetzte Parabel behaupten würde. Ihr abfallender Ast beschreibt einen Kanal, der bis zum Drain reicht und an seinem Drain-Ende eine negative Zahl von Elektronen hätte; einen solchen Kanal gibt es nicht. Ab der Abschnürgrenze gilt eine andere Gleichung, das Quadratgesetz.
:::

**Die Akteure:**

- __$U_{DS,\mathrm{ab}}$__: Abschnürspannung, die Drain-Source-Spannung an der Grenze zwischen ohmschem Bereich und Abschnürbereich, $U_{GS} - U_{th}$; 0,5 V bei $U_{GS}$ = 1 V.

Für $U_{DS}$ ab der Abschnürspannung gilt:

:::formel Formel
$$I_D = \frac{K_n}{2}\,\big(U_{GS} - U_{th}\big)^2$$
:::

**So liest man das:** Die Gleichung gilt im Abschnürbereich, für $U_{GS} > U_{th}$ und $U_{DS}$ ab $U_{GS} - U_{th}$. Eingabe ist nur die Gate-Source-Spannung; $U_{DS}$ kommt nicht vor. Der Strom wächst mit dem Quadrat der Übersteuerung, weil zwei Größen mit ihr wachsen: die Ladung an der Source und die Spannung über dem Kanal. Der Faktor 1/2 ist der Mittelwert der Übersteuerungen an Source und Abschnürpunkt, die Hälfte des Werts an der Source; in Abbildung 3b ist es die Fläche des Dreiecks. Weil der Strom nicht mehr wächst, heißt der Abschnürbereich auch Sättigungsbereich; mit der Sättigung des Bipolartransistors hat das nichts zu tun.

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
**Gegeben:** $K_n$ = 2 mA/V², $U_{th}$ = 0,5 V; Gate-Source-Spannungen 0,75 V, 1 V, 1,25 V, 1,5 V und 2 V; die Drain-Source-Spannung liegt jeweils über der Abschnürspannung.

**Gesucht:** (a) die Drainströme; (b) der Faktor, um den der Strom wächst, wenn sich die Gatespannung von 1 V auf 2 V verdoppelt, und wenn sich die Übersteuerung von 0,5 V auf 1 V verdoppelt; (c) der Strom einer MOS-Diode, bei der Gate und Drain verbunden sind, bei 1 V.

**Rechnung:** (a) Mit $K_n/2$ = 1 mA/V² und den Übersteuerungen 0,25 V, 0,5 V, 0,75 V, 1 V und 1,5 V:

$$I_D = 1\ \mathrm{mA/V^2}\cdot\big(U_{GS} - 0{,}5\ \mathrm V\big)^2 = 0{,}0625;\ 0{,}25;\ 0{,}5625;\ 1;\ 2{,}25\ \mathrm{mA}$$

(b) Doppelte Gatespannung und doppelte Übersteuerung:

$$\frac{I_D(2\ \mathrm V)}{I_D(1\ \mathrm V)} = \frac{2{,}25\ \mathrm{mA}}{0{,}25\ \mathrm{mA}} = 9, \qquad \frac{I_D(1{,}5\ \mathrm V)}{I_D(1\ \mathrm V)} = \frac{1\ \mathrm{mA}}{0{,}25\ \mathrm{mA}} = 4\,$$

(c) Bei verbundenem Gate und Drain ist $U_{DS} = U_{GS}$, also immer größer als $U_{GS} - U_{th}$: Oberhalb der Schwelle arbeitet die MOS-Diode stets im Abschnürbereich, darunter sperrt sie.

$$I_D = \frac{K_n}{2}\,\big(U_{GS} - U_{th}\big)^2 = 1\ \mathrm{mA/V^2}\cdot\big(1\ \mathrm V - 0{,}5\ \mathrm V\big)^2 = 0{,}25\ \mathrm{mA}$$

**Ergebnis:** **(a) 0,0625 mA, 0,25 mA, 0,5625 mA, 1 mA und 2,25 mA; (b) Faktor 9 bei doppelter Gatespannung, Faktor 4 bei doppelter Übersteuerung; (c) 0,25 mA.**

**Einordnung:** Die Gatespannung von 2 V übersteuert den Transistor dreimal so stark wie 1 V, deshalb wächst der Strom auf das Neunfache. Die MOS-Diode ist genau das Bauelement mit der Parabelkennlinie aus [Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung-ausfuehrlich.html): Ihr Koeffizient von 1 mA/V² ist $K_n/2$ des Beispieltransistors, ihr Arbeitspunkt 1 V und 0,25 mA.
::::

:::fehlvorstellung
„Doppelte Gatespannung, vierfacher Strom.“ Das liegt nahe, weil man das Quadratgesetz verkürzt als „Strom proportional zum Quadrat der Gatespannung“ liest. Quadriert wird aber die Übersteuerung, die Gatespannung abzüglich der Schwelle. Beim Beispieltransistor wächst der Strom von 1 V auf 2 V Gatespannung um den Faktor 9, von 0,25 mA auf 2,25 mA, weil die Übersteuerung von 0,5 V auf 1,5 V steigt. Nur bei doppelter Übersteuerung, von 1 V auf 1,5 V Gatespannung, ist es das Vierfache.
:::

Die Übergangspunkte aller Ausgangskennlinien, an denen sie waagerecht werden, liegen auf einer gemeinsamen Kurve, der gestrichelten Grenzparabel in Abbildung 1a. An der Grenze ist die Übersteuerung gleich der Drain-Source-Spannung, und das Quadratgesetz wird zu

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

:::frage
„Gilt das Quadratgesetz auch für sehr kurze Transistoren?“
Nur näherungsweise. Die Herleitung nimmt an, dass die Geschwindigkeit der Elektronen proportional zum Feld wächst. In Silizium ist bei rund 10⁷ cm/s Schluss; mit $\mu_n$ = 290 cm²/(V s) erreicht das Produkt aus Beweglichkeit und Feld diesen Wert bei 35 kV/cm, dem kritischen Feld der __Geschwindigkeitssättigung__, und merklich wird sie schon bei einem Bruchteil davon. Im Beispieltransistor beträgt das mittlere Feld längs des Kanals an der Abschnürgrenze bei 0,5 V Übersteuerung 5 kV/cm, und die Elektronen an der Source erreichen 7 % der Höchstgeschwindigkeit; bei 0,1 µm Kanallänge wären es nach derselben einfachen Rechnung 50 kV/cm und 72 %. Dann wächst der Strom schwächer als quadratisch mit der Übersteuerung, im Grenzfall nur noch linear, weil die Elektronen an der Source schon mit Höchstgeschwindigkeit laufen und nur noch ihre Zahl mit der Gatespannung zunimmt. Solche __Kurzkanaltransistoren__ beschreiben genauere Modelle.
:::

### Die Schwellenspannung aus der Übertragungskennlinie

*Wie bestimmt man die Schwellenspannung eines Transistors aus einer Messung?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/02-schwellenbestimmung · Vorlage: kennlinie-gestapelt
**Abbildung 5:** Zwei gestapelte Diagramme über $U_{GS}$ von 0 bis 1,5 V im Abschnürbereich. (a) Drainstrom: die Parabel ab 0,5 V bis 1 mA; gestrichelt die Tangente bei 1 V mit der Steigung 1 mS, die die Spannungsachse bei 0,75 V trifft. (b) Wurzel des Drainstroms in √mA: eine Gerade mit der Steigung 1 √mA/V, die die Spannungsachse bei 0,5 V schneidet, mit den Messpunkten 0,5 √mA bei 1 V und 1 √mA bei 1,5 V. Die Wurzel des Sättigungsstroms ist eine Gerade, die die Spannungsachse genau bei der Schwellenspannung schneidet; die Tangente an die Parabel trifft sie nicht.
:::

Die Schwellenspannung lässt sich an der Übertragungskennlinie nicht direkt ablesen: Die Parabel setzt bei $U_{th}$ waagerecht an, und unterhalb der Schwelle fließt ein kleiner, exponentiell abnehmender Strom (Abschnitt *Strom unterhalb der Schwelle*). Das Quadratgesetz bietet einen genaueren Weg. Zieht man auf beiden Seiten die Wurzel, wird aus der Parabel eine Gerade:

$$\sqrt{I_D} = \sqrt{\frac{K_n}{2}}\,\big(U_{GS} - U_{th}\big)$$

Trägt man die Wurzel gemessener Sättigungsströme über $U_{GS}$ auf, liegen die Punkte auf einer Geraden (Abbildung 5b). Ihr Schnittpunkt mit der Spannungsachse ist die Schwellenspannung, ihre Steigung die Wurzel aus $K_n/2$. Den Abschnürbereich sichert man am einfachsten, indem man Gate und Drain verbindet und so die MOS-Diode misst. Ein häufiger Fehler ist, statt der Wurzel die Tangente an die Parabel selbst bis zur Achse zu verlängern: Sie trifft die Achse in der Mitte zwischen Schwelle und Messpunkt, bei 1 V also bei 0,75 V statt bei 0,5 V (Abbildung 5a). Ebenso kann man bei kleiner Drain-Source-Spannung im ohmschen Bereich messen, wo der Strom linear mit $U_{GS}$ wächst. Diese Gerade schneidet die Achse aber um die halbe Drain-Source-Spannung über der Schwelle, bei 0,1 V also bei 0,55 V, denn nach der Triodengleichung wird der Strom null, wenn die Übersteuerung gleich der halben Drain-Source-Spannung ist; diese Hälfte zieht man ab.

Idee der Herleitung: Man zieht im Quadratgesetz auf beiden Seiten die Wurzel.

:::herleitung
**Ausgangspunkt:** das Quadratgesetz aus dem Abschnitt *Abschnürgrenze und Quadratgesetz*.

**Annahmen:** Abschnürbereich und $U_{GS} > U_{th}$, sodass die Übersteuerung positiv ist.

**Schritt 1** (entscheidender Schritt): Beide Seiten sind positiv; die Wurzel der rechten Seite ist das Produkt der Wurzeln, und die Wurzel aus dem Quadrat der positiven Übersteuerung ist die Übersteuerung selbst:

**Ergebnis:**

$$\sqrt{I_D} = \sqrt{\frac{K_n}{2}}\,\big(U_{GS} - U_{th}\big)$$

**Proben:** Bei 1 V: Wurzel aus 1 mA/V² mal 0,5 V ergibt 0,5 √mA, die Wurzel aus 0,25 mA. Bei $U_{GS} = U_{th}$ ist die Wurzel null: Dort schneidet die Gerade die Achse.

**Grenzen:** Mit Kanallängenmodulation hängt der gemessene Strom zusätzlich von $U_{DS}$ ab; bei der MOS-Diode ändert sich $U_{DS}$ mit, was die Gerade leicht krümmt. Nahe der Schwelle verfälscht der Unterschwellenstrom die Punkte, deshalb wertet man Punkte deutlich oberhalb aus.
:::

::::beispiel Schwellenspannung aus zwei Messpunkten
**Gegeben:** zwei Messungen an der MOS-Diode im Abschnürbereich, 0,25 mA bei 1 V und 1 mA bei 1,5 V.

**Gesucht:** Schwellenspannung und Steilheitskoeffizient; zum Vergleich der Achsenschnittpunkt der Tangente an die Parabel bei 1 V.

**Rechnung:** Die Wurzeln der Ströme sind 0,5 √mA und 1 √mA. Steigung der Geraden:

$$\sqrt{\frac{K_n}{2}} = \frac{1\ \sqrt{\mathrm{mA}} - 0{,}5\ \sqrt{\mathrm{mA}}}{1{,}5\ \mathrm V - 1\ \mathrm V} = 1\ \frac{\sqrt{\mathrm{mA}}}{\mathrm V}$$

Daraus $K_n/2$ = 1 mA/V², $K_n$ = 2 mA/V². Achsenschnittpunkt:

$$U_{th} = 1\ \mathrm V - \frac{0{,}5\ \sqrt{\mathrm{mA}}}{1\ \sqrt{\mathrm{mA}}/\mathrm V} = 0{,}5\ \mathrm V$$

Die Tangente bei 1 V hat die Steigung $K_n(U_{GS} - U_{th})$ = 1 mS; sie erreicht null nach 0,25 mA / 1 mS = 0,25 V:

$$U_\mathrm{Tangente} = 1\ \mathrm V - 0{,}25\ \mathrm V = 0{,}75\ \mathrm V$$

**Ergebnis:** **$U_{th}$ = 0,5 V und $K_n$ = 2 mA/V²; die Tangente ergäbe 0,75 V, 0,25 V zu viel.**

**Einordnung:** Zwei Punkte genügen, wenn das Quadratgesetz gilt; in der Praxis misst man viele und passt eine Gerade an. Die Tangente liegt immer in der Mitte zwischen Schwelle und Messpunkt; bei 1,5 V ergäbe sie 1 V. Die Steigung der Übertragungskennlinie, hier 1 mS, ist zugleich die Steilheit, mit der der Transistor kleine Signale verstärkt.
::::

## Kanallängenmodulation

*Warum steigt der Drainstrom im Abschnürbereich mit der Drain-Source-Spannung doch noch leicht an, und wie beschreibt man das?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/02-kanallaengenmodulation · Vorlage: kennlinienfeld-early
**Abbildung 6:** Ausgangskennlinien des Beispieltransistors mit Kanallängenmodulation, λ = 0,1 1/V, für $U_{GS}$ = 0,75 V, 1 V, 1,25 V und 1,5 V und $U_{DS}$ von 0 bis 2,5 V. Im Abschnürbereich steigen sie mit 6,25 µA/V, 25 µA/V, 56,25 µA/V und 100 µA/V an und erreichen bei 2,5 V 0,078 mA, 0,3125 mA, 0,703 mA und 1,25 mA. Nach links gestrichelt verlängert, mit gebrochener Achse zwischen −10 V und 0 V, treffen sich alle Geraden bei $U_{DS}$ = −10 V. Kleines Einsatzbild: das Drain-Ende des Kanals bei $U_{GS}$ = 1 V, der Abschnürpunkt 34 nm vor dem Drain bei 1 V und 58 nm bei 2 V. Weil der Kanal mit wachsender Drainspannung kürzer wird, steigen die Kennlinien im Abschnürbereich leicht an; im Modell treffen sie sich verlängert in einem Punkt.
:::

**Die Akteure:**

- __$\Delta L$__: Länge der verarmten Zone zwischen Abschnürpunkt und Drain, um die der leitende Kanal kürzer ist als $L$; nach eindimensionaler Abschätzung 34 nm bei $U_{DS}$ = 1 V und 58 nm bei 2 V, beide für $U_{GS}$ = 1 V.
- __$\lambda$__: __Kanallängenmodulationsfaktor__, der Anstieg des Stroms im Abschnürbereich je Volt Drain-Source-Spannung, bezogen auf den Strom des Quadratgesetzes, in 1/V; 0,1 1/V beim Beispieltransistor.
- __$U_A$__: __Early-Spannung__, der Kehrwert von λ, in V; 10 V. Der Name stammt vom gleichartigen Effekt beim Bipolartransistor.

**Das Zusammenspiel:**

**Schritt 1**: Steigt $U_{DS}$ über die Abschnürspannung, muss die verarmte Zone vor dem Drain den ganzen Überschuss aufnehmen, und sie wächst. Der Abschnürpunkt rückt zur Source, der leitende Kanal hat nur noch die Länge $L - \Delta L$.

**Schritt 2**: An seinem Ende liegt nach wie vor das Potential $U_{GS} - U_{th}$. Der kürzere Kanal hat also dieselbe Spannung und an der Source dieselbe Ladung wie zuvor, aber einen kürzeren Weg. Weil der Strom umgekehrt proportional zur Kanallänge ist, wie $K_n$ = $\mu_n C'_\mathrm{ox} W/L$ zeigt, führt er mehr Strom.

**Schritt 3** (entscheidender Schritt): Weil $\Delta L$ klein gegen $L$ ist, wächst der Strom um etwa den Bruchteil $\Delta L/L$, und $\Delta L$ nimmt mit $U_{DS}$ zu. Das einfachste Modell setzt diesen Anstieg linear an, als Faktor $(1 + \lambda U_{DS})$. In Abbildung 6 sind die Kennlinien im Abschnürbereich deshalb Geraden mit kleiner Steigung, und die Steigung wächst mit dem Strom, weil der Faktor den ganzen Strom vergrößert.

**Schritt 4**: Jede dieser Geraden wird null, wenn $1 + \lambda U_{DS}$ null wird, bei $U_{DS}$ = −1/λ = −10 V, und dieser Punkt hängt nicht von $U_{GS}$ ab. Nach links verlängert treffen sich deshalb im Modell alle Kennlinien in einem Punkt der Spannungsachse.

:::formel Formel
$$I_D = \frac{K_n}{2}\,\big(U_{GS} - U_{th}\big)^2\,\big(1 + \lambda\,U_{DS}\big), \qquad U_A = \frac{1}{\lambda}\,$$
:::

**So liest man das:** Die Gleichung gilt im Abschnürbereich. Der Faktor $(1 + \lambda U_{DS})$ hebt den Strom bei 2 V um 20 % über den Wert des Quadratgesetzes, an der Abschnürgrenze bei 0,5 V schon um 5 %. Die Steigung ist λ mal der Strom des Quadratgesetzes, 25 µA/V bei 1 V Gatespannung und 100 µA/V bei 1,5 V. Je größer λ, also je kleiner die Early-Spannung, desto stärker steigen die Kennlinien. Üblich ist auch, die Early-Spannung mit dem Vorzeichen ihres Schnittpunkts anzugeben, beim Beispiel −10 V.

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
**Gegeben:** $K_n$ = 2 mA/V², $U_{th}$ = 0,5 V, λ = 0,1 1/V, $U_{GS}$ = 1 V; Drain-Source-Spannungen 0,5 V, 1 V, 2 V und 2,5 V. Für die eindimensionale Abschätzung der Zone $\varepsilon_\mathrm{Si}$ = 1,036·10⁻¹² F/cm und $e N_A$ = 9,10·10⁻² C/cm³.

**Gesucht:** die Drainströme, die Steigung und ihr Kehrwert, die Early-Spannung und der Vergleich mit der eindimensionalen Abschätzung zwischen 1 V und 2 V.

**Rechnung:** Das Quadratgesetz ergibt 0,25 mA; mit dem Faktor:

$$I_D = 0{,}25\ \mathrm{mA}\cdot\big(1 + 0{,}1\ \mathrm{V^{-1}}\cdot U_{DS}\big) = 0{,}2625;\ 0{,}275;\ 0{,}30;\ 0{,}3125\ \mathrm{mA}$$

Steigung, ihr Kehrwert und die Early-Spannung:

$$\lambda\cdot0{,}25\ \mathrm{mA} = 25\ \mathrm{\mu A/V}, \qquad \frac{1}{25\ \mathrm{\mu A/V}} = 40\ \mathrm{k\Omega}, \qquad U_A = \frac{1}{0{,}1\ \mathrm{V^{-1}}} = 10\ \mathrm V\,$$

Eindimensionale Abschätzung der Zone über die Spannung $U_{DS} - 0{,}5\ \mathrm V$ jenseits der Abschnürgrenze, wie bei einer einseitigen Verarmungszone:

$$\Delta L = \sqrt{\frac{2\,\varepsilon_\mathrm{Si}\,\big(U_{DS} - 0{,}5\ \mathrm V\big)}{e\,N_A}} = 33{,}7\ \mathrm{nm}\ \text{bei 1 V}, \qquad 58{,}4\ \mathrm{nm}\ \text{bei 2 V}\,$$

Damit wächst $L/(L - \Delta L)$ zwischen 1 V und 2 V von 1,035 auf 1,062, um 0,027 je Volt. Bezogen auf den Strom des Quadratgesetzes wie λ selbst ergibt die Abschätzung also 0,027 1/V, gegen 0,1 1/V im Modell.

**Ergebnis:** **0,2625 mA, 0,275 mA, 0,30 mA und 0,3125 mA; Steigung 25 µA/V, also 40 kΩ; Early-Spannung 10 V. Die eindimensionale Abschätzung ergibt λ ≈ 0,027 1/V, gut ein Viertel des Modellwerts.**

**Einordnung:** Als Stromquelle hat der Transistor bei 0,25 mA einen Innenwiderstand von 40 kΩ. Der Bipolartransistor aus [Der Transistor als Verstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker-ausfuehrlich.html) hat eine Early-Spannung von 70 V; bei gleichem Strom ist seine Kennlinie siebenmal flacher. Integrierte MOS-Schaltungen, die gute Stromquellen brauchen, verwenden deshalb längere Kanäle oder Schaltungen, die den Innenwiderstand vervielfachen.
::::

:::fehlvorstellung
„Im Abschnürbereich hängt der Strom nicht von der Drain-Source-Spannung ab.“ Das liegt nahe, weil das Quadratgesetz $U_{DS}$ nicht enthält und der Bereich Sättigungsbereich heißt. Der Strom steigt aber weiter, nur langsam: beim Beispieltransistor von 0,2625 mA an der Abschnürgrenze auf 0,30 mA bei 2 V, um 14 %. Der Grund ist die Verkürzung des Kanals (Abschnitt *Kanallängenmodulation*). Für Verstärker ist dieser Rest entscheidend, denn er begrenzt den Innenwiderstand der Stromquelle und damit die erreichbare Verstärkung.
:::

:::frage
„Warum ist λ so viel größer, als die Verkürzung des Kanals ergibt?“
Die eindimensionale Abschätzung behandelt die Zone vor dem Drain wie die Verarmungszone einer Diode und ergibt für den Beispieltransistor zwischen 1 V und 2 V λ ≈ 0,027 1/V. Ihr fehlen zwei Dinge: Das Feld des Drains verteilt sich zweidimensional zwischen Drain, Gate und Substrat, sodass die eindimensionale Länge der Zone nur eine grobe Schätzung ist; und der Drain wirkt über sein Feld auch auf den Kanal selbst, sodass die wirksame Schwellenspannung mit wachsender Drainspannung leicht sinkt, umso stärker, je kürzer der Kanal ist. Beides hängt von Dotierprofilen und Geometrie ab, die keine einfache Formel erfasst; λ wird deshalb an gemessenen Kennlinien bestimmt. Lehrbücher setzen für Prozesse mit 4 bis 6 nm Gateoxid näherungsweise 5 V Early-Spannung je Mikrometer Kanallänge an, für 1 µm also λ ≈ 0,2 1/V; die 0,1 1/V des Beispieltransistors liegen in derselben Größenordnung.
:::

## Das Großsignalmodell

*Wie fasst man das Verhalten in allen Bereichen zu einem Modell zusammen, mit dem man Schaltungen berechnen kann?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/02-ersatzschaltbild · Vorlage: schaltung-ersatzschaltbild
**Abbildung 7:** Links das Schaltzeichen des NMOS mit Gate, Drain, Source und Bulk, den Spannungen $U_{GS}$, $U_{DS}$ und $U_{BS}$ und dem Strom $I_D$ in den Drain hinein. Rechts das Großsignal-Ersatzschaltbild: Das Gate ist ein offener Anschluss ohne Verbindung; zwischen Drain und Source liegt eine gesteuerte Stromquelle mit dem Strom $I_D(U_{GS}, U_{DS})$, gestrichelt den beiden Steuerspannungen zugeordnet; der Bulk ist getrennt eingezeichnet, über $U_{BS}$ wirkt er auf die Schwellenspannung. Darunter die drei Bereiche mit ihren Bedingungen. Für große Signale ist der MOSFET eine Stromquelle zwischen Drain und Source, deren Strom die beiden Spannungen festlegen, bei stromlosem Gate.
:::

Die Gleichungen der vorigen Abschnitte ergeben zusammen ein vollständiges Modell des Transistors. Abbildung 7 zeigt es als Schaltung: Das Gate nimmt keinen Strom auf und ist deshalb ein offener Anschluss. Zwischen Drain und Source liegt eine __gesteuerte Stromquelle__, eine Quelle, deren Strom nicht fest ist, sondern von Spannungen an anderer Stelle der Schaltung abhängt, hier von $U_{GS}$ und $U_{DS}$. __Großsignalmodell__ heißt es, weil es für beliebig große Spannungen gilt; ein Kleinsignalmodell dagegen beschreibt nur kleine Änderungen um einen Arbeitspunkt, dafür linear ([Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung-ausfuehrlich.html)). In Schaltungssimulatoren heißt diese Form __Level-1-Modell__ oder nach seinen Urhebern __Shichman-Hodges-Modell__.

:::frage
„Warum hat das Ersatzschaltbild einen Bulk-Anschluss, wenn $U_{BS}$ in den Gleichungen gar nicht vorkommt?“
Die Gleichungen dieses Artikels gelten für $U_{BS}$ = 0. Liegt der Bulk tiefer als die Source, wird die Verarmungszone unter dem Gate breiter, und die Gatespannung muss deren zusätzliche Ladung mittragen, bevor ein Kanal entsteht: Die Schwellenspannung steigt. Dieser __Substrateffekt__ steckt im Modell in $U_{th}$, das dann von $U_{BS}$ abhängt. Behandelt wird er zusammen mit dem PMOS im Artikel über PMOS-Transistor, Substrateffekt und Latch-Up.
:::

:::formel Formel
Sperrbereich, $U_{GS} < U_{th}$:

$$I_D = 0$$

Ohmscher Bereich, $U_{GS} > U_{th}$ und $U_{DS} < U_{GS} - U_{th}$:

$$I_D = K_n\Big[\big(U_{GS} - U_{th}\big)\,U_{DS} - \frac{U_{DS}^2}{2}\Big]\big(1 + \lambda\,U_{DS}\big)$$

Abschnürbereich, $U_{GS} > U_{th}$ und $U_{DS}$ ab $U_{GS} - U_{th}$:

$$I_D = \frac{K_n}{2}\,\big(U_{GS} - U_{th}\big)^2\,\big(1 + \lambda\,U_{DS}\big)$$
:::

**So liest man das:** Eingaben sind $U_{GS}$ und $U_{DS}$ (nicht negativ), Ausgabe ist $I_D$. Zuerst entscheidet man, welcher Bereich vorliegt: Liegt $U_{GS}$ unter der Schwelle, sperrt der Transistor; ist $U_{DS}$ kleiner als die Übersteuerung, ist er ohmsch, sonst abgeschnürt. Der Faktor $(1 + \lambda U_{DS})$ steht auch im ohmschen Bereich, obwohl der Kanal dort nicht verkürzt ist. So stimmen beide Gleichungen an der Grenze in Wert und Steigung überein, und die Kennlinie hat weder Sprung noch Knick; im ohmschen Bereich ändert der Faktor den Strom um höchstens λ($U_{GS} - U_{th}$), bei 1 V Gatespannung um 5 %. Der Strom null im Sperrbereich ist eine Näherung für einen sehr kleinen Strom (Abschnitt *Strom unterhalb der Schwelle*).

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

Rechnet man eine Schaltung, kennt man den Bereich vorher nicht. Man nimmt einen an, meist den Abschnürbereich, berechnet den Arbeitspunkt und prüft die Bedingung. Ist sie verletzt, war die Annahme falsch, und man rechnet mit dem anderen Bereich neu.

::::beispiel Arbeitspunkt eines Transistors mit Drainwiderstand
**Gegeben:** der Beispieltransistor ($K_n$ = 2 mA/V², $U_{th}$ = 0,5 V, λ = 0,1 1/V), Source an Masse, ein Widerstand $R_D$ = 4 kΩ von der Versorgungsspannung $U_B$ = 2,5 V zum Drain; Gate-Source-Spannung (a) 1 V, (b) 1,5 V.

**Gesucht:** Drainstrom, Drain-Source-Spannung und Bereich.

:::grafik
Szene: st1/mos-feldeffekttransistoren/02-arbeitspunkt · Vorlage: schaltung-arbeitsgerade
**Abbildung 8:** (a) Schaltbild: Versorgungsspannung 2,5 V, Widerstand 4 kΩ zum Drain, NMOS mit Source an Masse, Gate an einer Spannungsquelle $U_{GS}$; Zählpfeile $I_D$ und $U_{DS}$. (b) Ausgangskennlinien mit λ = 0,1 1/V für $U_{GS}$ = 1 V und 1,5 V, dazu die Arbeitsgerade des Widerstands von 0,625 mA bei 0 V nach null bei 2,5 V und gestrichelt die Grenzparabel. Die Schnittpunkte sind die Arbeitspunkte: 1,36 V und 0,284 mA rechts der Grenzparabel, im Abschnürbereich; 0,31 V und 0,546 mA links davon, im ohmschen Bereich. Der Arbeitspunkt liegt im Schnitt von Kennlinie und Arbeitsgerade; auf welcher Seite der Grenzparabel, entscheidet über den Bereich.
:::

**Rechnung:** Für den Widerstand gilt die Maschenregel:

$$U_{DS} = U_B - R_D\,I_D$$

(a) Annahme Abschnürbereich; das Quadratgesetz ergibt $K_n/2 \cdot (0{,}5\ \mathrm V)^2$ = 0,25 mA mal $(1 + \lambda U_{DS})$, und $R_D$ mal 0,25 mA ist 1 V:

$$U_{DS} = 2{,}5\ \mathrm V - 1\ \mathrm V\cdot\big(1 + 0{,}1\ \mathrm{V^{-1}}\cdot U_{DS}\big)$$

$$U_{DS} = \frac{1{,}5\ \mathrm V}{1{,}1} = 1{,}364\ \mathrm V$$

$$I_D = \frac{2{,}5\ \mathrm V - 1{,}364\ \mathrm V}{4\ \mathrm{k\Omega}} = 0{,}284\ \mathrm{mA}$$

Probe: 1,364 V liegt über der Abschnürspannung 0,5 V; die Annahme stimmt.

(b) Annahme Abschnürbereich; das Quadratgesetz ergibt 1 mA mal $(1 + \lambda U_{DS})$, und $R_D$ mal 1 mA ist 4 V:

$$U_{DS} = 2{,}5\ \mathrm V - 4\ \mathrm V\cdot\big(1 + 0{,}1\ \mathrm{V^{-1}}\cdot U_{DS}\big)$$

$$U_{DS} = \frac{-1{,}5\ \mathrm V}{1{,}4} = -1{,}07\ \mathrm V$$

Das widerspricht der Annahme, denn im Abschnürbereich müsste $U_{DS}$ mindestens 1 V betragen. Neue Annahme ohmscher Bereich, zunächst ohne den kleinen Faktor $(1 + \lambda U_{DS})$:

$$2\ \mathrm{\frac{mA}{V^2}}\cdot\Big(1\ \mathrm V\cdot U_{DS} - \frac{U_{DS}^2}{2}\Big)\cdot4\ \mathrm{k\Omega} = 2{,}5\ \mathrm V - U_{DS}$$

$$4\,U_{DS}^2 - 9\ \mathrm V\cdot U_{DS} + 2{,}5\ \mathrm{V^2} = 0$$

$$U_{DS} = \frac{9 - \sqrt{41}}{8}\ \mathrm V = 0{,}325\ \mathrm V$$

Die zweite Lösung, 1,93 V, liegt außerhalb des ohmschen Bereichs. Der Strom ist (2,5 V − 0,325 V)/4 kΩ = 0,544 mA. Mit dem Faktor $(1 + \lambda U_{DS})$ ergibt die numerische Lösung 0,314 V und 0,546 mA.

**Ergebnis:** **(a) 0,284 mA bei 1,36 V, Abschnürbereich; (b) 0,546 mA bei 0,31 V, ohmscher Bereich.**

**Einordnung:** Bei 1 V Gatespannung arbeitet der Transistor als Stromquelle; kleine Änderungen von $U_{GS}$ ändern den Strom und über $R_D$ die Drainspannung, die Schaltung verstärkt. Bei 1,5 V zieht er den Drain auf 0,3 V herunter und wirkt als geschlossener Schalter, zwischen Drain und Source liegen 575 Ω. Ohne die Kanallängenmodulation läge der Arbeitspunkt in (a) bei 0,25 mA und 1,5 V; mit ihr ist der Strom um 14 % größer.
::::

:::vertiefung
**Wie ein Schaltungssimulator diesen Transistor beschreibt.** Die meisten Schaltungssimulatoren folgen SPICE, einem in den 1970er-Jahren an der University of California in Berkeley entwickelten Programm. Dort beschreibt eine Modellzeile den Fertigungsprozess, für den Beispieltransistor etwa `.model NMOS_BSP NMOS (LEVEL=1 VTO=0.5 KP=200u LAMBDA=0.1 TOX=5n GAMMA=0.63 PHI=0.92)`; der einzelne Transistor erhält Anschlüsse und Abmessungen, etwa `M1 d g s b NMOS_BSP W=10u L=1u`. VTO ist die Schwellenspannung bei $U_{BS}$ = 0, KP der Prozessparameter $K'_n = \mu_n C'_\mathrm{ox}$ = 200 µA/V², der Anteil des Steilheitskoeffizienten, den die Fertigung festlegt, LAMBDA ist λ; GAMMA und PHI beschreiben den Substrateffekt, TOX die Oxiddicke für die Kapazitäten. Mit LEVEL=1 rechnet der Simulator genau die Gleichungen dieses Abschnitts und vertauscht bei negativer Drain-Source-Spannung Source und Drain. Entwurfsbibliotheken realer Prozesse benutzen viel genauere Modelle mit Hunderten von Parametern, etwa die BSIM-Modelle, weil die einfachen Gleichungen Kurzkanaleffekte, den Unterschwellenstrom und die Abnahme der Beweglichkeit nicht enthalten.
:::

## Strom unterhalb der Schwelle

*Fließt unterhalb der Schwellenspannung wirklich kein Strom?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/02-unterschwelle · Vorlage: kennlinie-semilog
**Abbildung 9:** Drainstrom des Beispieltransistors halblogarithmisch von 10⁻¹³ A bis 10⁻² A über $U_{GS}$ von 0 bis 1,5 V bei $U_{DS}$ = 1 V. Unterhalb der Schwelle eine Gerade: 0,56 pA bei 0 V, 8,1 pA bei 0,1 V, 0,12 nA bei 0,2 V, 2,0 nA bei 0,3 V und 32 nA bei 0,4 V, mit einem Steigungsdreieck „eine Dekade je 83 mV“; gestrichelt zum Vergleich die Grenze von 59,5 mV je Dekade. Oberhalb der Schwelle der Übergang ins Großsignalmodell mit 0,275 mA bei 1 V und 1,1 mA bei 1,5 V; senkrechte Marke bei $U_{th}$ = 0,5 V. Unterhalb der Schwelle sinkt der Strom nicht auf null, sondern exponentiell, um eine Zehnerpotenz je 83 mV.
:::

**Die Akteure:**

- __$\psi_s$__: Oberflächenpotential, die Spannung, um die die Oberfläche unter dem Gate höher liegt als das neutrale Substrat ([Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html)); 0,566 V bei $U_{GS}$ = 0 und 0,923 V an der Schwelle.
- __$U_T$__: Temperaturspannung $k_B T/e$, 25,85 mV bei 300 K; eine Potentialstufe dieser Höhe ändert die Elektronendichte im Gleichgewicht um den Faktor $\exp(1)$.
- __$Q'_n(0)$__: Elektronenladung pro Fläche am Source-Ende des Kanals; bei $U_{GS}$ = 0 nur −7,48·10⁻¹⁵ C/cm², das sind 4,7·10⁴ Elektronen pro Quadratzentimeter; im ganzen Kanal des Beispieltransistors befindet sich im Mittel nicht einmal ein Elektron.

**Das Zusammenspiel:** Unterhalb der Schwelle ist die Oberfläche nur schwach invertiert. Es gibt Elektronen, aber wenige: Bei $U_{GS}$ = 0 sind es an der Oberfläche 5,6·10¹¹ pro Kubikzentimeter. Zwischen der n⁺-Source und der Oberfläche liegt eine Barriere, die Schwelle eines pn-Übergangs; je höher das Gate das Oberflächenpotential hebt, desto niedriger ist sie. Wie in einer Diode gelangen Elektronen mit ausreichender Wärmeenergie über sie hinweg, nach der Boltzmann-Verteilung umso mehr, je niedriger sie ist ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie-ausfuehrlich.html)).

Längs des Kanals gibt es dann kaum ein Feld: Die wenigen Elektronen verändern das Potential nicht, und das Gate hält die Oberfläche überall auf demselben $\psi_s$. Die Elektronen bewegen sich durch __Diffusion__, die Wanderung von Teilchen vom Ort höherer zum Ort niedrigerer Dichte durch ihre ungeordnete Wärmebewegung. Am Source-Ende ist die Dichte hoch; am Drain-Ende ist sie um den Faktor $\exp(-U_{DS}/U_T)$ kleiner, weil die Barriere vom Drain aus um $U_{DS}$ höher ist. Weil auch hier durch jeden Querschnitt derselbe Strom fließt, fällt die Dichte längs des Kanals linear ab. Schon ab 0,1 V Drainspannung ist das Drain-Ende praktisch leer, die Dichte dort beträgt 2 % des Werts an der Source, und der Strom hängt kaum noch von $U_{DS}$ ab.

Damit ergeben sich zwei Sichtweisen. Oberhalb der Schwelle begrenzt der Kanal den Strom: Die Elektronen driften durch seinen Widerstand. Unterhalb begrenzt die Barriere am Beginn des Kanals: Wie viele Elektronen sie überwinden, bestimmt den Strom, und der Weg danach kostet kaum etwas. Die Bauelementphysik beschreibt beide Fälle mit derselben Barriere, deren Höhe das Gate einstellt ([Der MOSFET](/wissen/elektrotechnik/4-semester/grundlagen-elektronischer-materialien-und-bauelemente/bauelemente/mosfet.html)); für Schaltungsrechnungen oberhalb der Schwelle ist das Driftbild das bequemere.

:::formel Formel
$$I_D = \mu_n\,\frac{W}{L}\,U_T\,\big|Q'_n(0)\big|\,\Big[1 - \exp\Big(-\frac{U_{DS}}{U_T}\Big)\Big]$$
:::

**So liest man das:** Eingaben sind die Elektronenladung am Source-Ende, die über das Oberflächenpotential von $U_{GS}$ abhängt, und $U_{DS}$; Ausgabe ist der Drainstrom. An der Stelle der Spannung über dem Kanal steht die Temperaturspannung: Diffusion treibt so stark wie eine Drift unter 25,85 mV in einem Kanal, der überall die Ladung des Source-Endes trägt. Ab etwa 0,1 V Drainspannung ist die Klammer praktisch 1, der Transistor ist schon dort gesättigt. Weil die Ladung am Source-Ende exponentiell vom Oberflächenpotential abhängt, wächst der Strom exponentiell mit $U_{GS}$.

Idee der Herleitung: Man setzt einen reinen Diffusionsstrom an, dessen Dichtegefälle durch die Boltzmann-Faktoren an beiden Enden des Kanals festliegt.

:::herleitung
**Ausgangspunkt:** die Diffusionsstromdichte der Elektronen mit der Einstein-Beziehung für den Diffusionskoeffizienten $D_n$ ([Diffusion und Einstein-Relation](/wissen/elektrotechnik/4-semester/grundlagen-elektronischer-materialien-und-bauelemente/halbleiter-und-ladungstransport/diffusion-einstein-relation.html)):

$$J_n = e\,D_n\,\frac{dn}{dx}, \qquad D_n = \mu_n\,U_T\,$$

**Annahmen:**
(i) Schwache Inversion: Die Elektronenladung ist klein gegen die Ladung der Verarmungszone und verändert das Potential nicht; $\psi_s$ ist längs des Kanals konstant, es gibt kein Feld längs des Kanals und nur Diffusion.
(ii) Am Source-Ende steht die Elektronendichte im Gleichgewicht mit der Source, am Drain-Ende mit dem Drain. Vom Drain aus ist die Barriere um $U_{DS}$ höher, die Dichte nach der Boltzmann-Verteilung um $\exp(-U_{DS}/U_T)$ kleiner.
(iii) Im Kanal rekombinieren keine Elektronen; durch jeden Querschnitt fließt derselbe Strom.

**Schritt 1**: Über die Dicke der Elektronenschicht integriert, wird aus $e\,n$ die Ladung pro Fläche $|Q'_n|$; mit der Weite $W$ ergibt sich der Strom. Die Elektronen diffundieren zum Drain, wo die Dichte kleiner ist; der Strom fließt in den Drain hinein:

$$I_D = -W\,D_n\,\frac{d\,|Q'_n|}{dx}$$

**Schritt 2** (entscheidender Schritt): Nach (iii) ist der Strom überall gleich, das Gefälle also konstant, und die Ladung fällt linear von $|Q'_n(0)|$ auf $|Q'_n(L)|$:

$$I_D = W\,D_n\,\frac{|Q'_n(0)| - |Q'_n(L)|}{L}$$

**Schritt 3**: Nach (ii) ist die Ladung am Drain-Ende

$$|Q'_n(L)| = |Q'_n(0)|\,\exp\Big(-\frac{U_{DS}}{U_T}\Big)$$

Eingesetzt, zusammen mit der Einstein-Beziehung:

**Ergebnis:**

$$I_D = \mu_n\,\frac{W}{L}\,U_T\,\big|Q'_n(0)\big|\,\Big[1 - \exp\Big(-\frac{U_{DS}}{U_T}\Big)\Big]$$

**Woher die Faktoren kommen:** $\mu_n U_T$ ist der Diffusionskoeffizient, $W/L$ die Geometrie wie bei der Drift; die Klammer ist der Unterschied der Dichten an beiden Enden.

**Proben:** Einheit: cm²/(V s) · V · C/cm² ergibt A. Grenzfall: Bei $U_{DS}$ = 0 ist der Strom null. Zahlenwert bei $U_{GS}$ = 0 und $U_{DS}$ = 1 V: 290 · 10 · 0,02585 · 7,48·10⁻¹⁵ A = 5,6·10⁻¹³ A.

**Grenzen:** Nahe der Schwelle ist die Elektronenladung nicht mehr klein, und Drift kommt hinzu; zwischen beiden Bereichen liegt ein Übergang, den Modelle für alle Bereiche, etwa das EKV-Modell, stetig beschreiben. Leckströme der pn-Übergänge und durch das Oxid kommen hinzu.
:::

::::beispiel Leckstrom des Beispieltransistors und eines großen Chips
**Gegeben:** $\mu_n$ = 290 cm²/(V s), $W/L$ = 10, $U_T$ = 25,85 mV; Elektronenladung am Source-Ende bei $U_{GS}$ = 0 aus der vollständigen Rechnung des MOS-Kondensators 7,48·10⁻¹⁵ C/cm²; $U_{DS}$ = 1 V; zum Vergleich der Strom des eingeschalteten Transistors nach dem Großsignalmodell, 5 mA bei $U_{GS}$ und $U_{DS}$ von je 2,5 V.

**Gesucht:** (a) der Strom bei $U_{GS}$ = 0; (b) das Verhältnis von Ein- zu Ausstrom; (c) der Strom von 10⁹ solchen Transistoren und die Leistung an 2,5 V.

**Rechnung:** (a) Die Klammer ist bei 1 V praktisch 1:

$$I_D = 290\ \mathrm{\frac{cm^2}{V\,s}}\cdot10\cdot0{,}02585\ \mathrm V\cdot7{,}48\cdot10^{-15}\ \mathrm{\frac{C}{cm^2}} = 5{,}6\cdot10^{-13}\ \mathrm A$$

(b) Ein zu aus; der Ausstrom ist ab 0,1 V praktisch unabhängig von $U_{DS}$:

$$\frac{5\cdot10^{-3}\ \mathrm A}{5{,}6\cdot10^{-13}\ \mathrm A} = 8{,}9\cdot10^{9}$$

(c) 10⁹ Transistoren:

$$10^{9}\cdot5{,}6\cdot10^{-13}\ \mathrm A = 0{,}56\ \mathrm{mA}, \qquad 0{,}56\ \mathrm{mA}\cdot2{,}5\ \mathrm V = 1{,}4\ \mathrm{mW}\,$$

**Ergebnis:** **(a) 0,56 pA; (b) rund 9·10⁹; (c) 0,56 mA und 1,4 mW.**

**Einordnung:** Ein einzelner gesperrter Transistor ist ein ausgezeichneter Schalter: Ein- und Ausstrom unterscheiden sich um fast zehn Zehnerpotenzen. Ein Chip mit einer Milliarde Transistoren summiert die kleinen Ströme aber zu einer Leistung, die auch dann fließt, wenn nichts schaltet. Mit dieser Schwelle von 0,5 V ist sie gering; wie schnell sie mit sinkender Schwelle wächst, zeigt die Unterschwellensteigung.
::::

**Die Akteure:**

- __$S_\mathrm{sub}$__: __Unterschwellensteigung__ (sub für englisch subthreshold, unterhalb der Schwelle), die Änderung der Gate-Source-Spannung, die den Strom unterhalb der Schwelle um den Faktor 10 ändert, in mV pro Dekade; 83 mV beim Beispieltransistor.
- __$C'_\mathrm{dep}$__: Kapazität der Verarmungszone pro Fläche, die Änderung ihrer Ladung je Änderung des Oberflächenpotentials ([Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html)); 2,46 fF/µm² bei $U_{GS}$ = 0,3 V, gegen 6,91 fF/µm² für das Oxid.
- __$m$__: Steigungsfaktor, die Änderung der Gatespannung je Änderung des Oberflächenpotentials; 1,36.

Das Gate verschiebt das Oberflächenpotential nur zum Teil. Gate, Oxid und Verarmungszone bilden zwei Kondensatoren in Reihe, die Oxidkapazität und die Kapazität der Verarmungszone. Eine Änderung der Gatespannung teilt sich auf beide auf wie an einem kapazitiven Spannungsteiler, und nur der Anteil über der Verarmungszone erreicht die Oberfläche. Beim Beispieltransistor ist das knapp drei Viertel.

:::formel Formel
$$S_\mathrm{sub} = m\,U_T\,\ln 10, \qquad m = 1 + \frac{C'_\mathrm{dep}}{C'_\mathrm{ox}}\,$$
:::

**So liest man das:** Eingaben sind das Verhältnis der beiden Kapazitäten und die Temperatur, Ausgabe ist die Gatespannung je Dekade Strom. Wäre $m$ = 1, erreichte die ganze Gatespannung die Oberfläche, und $S_\mathrm{sub}$ wäre 59,5 mV bei 300 K. Weniger ist bei einem Strom über eine Barriere, die die Wärmebewegung überwinden muss, nicht möglich: Die Boltzmann-Verteilung ändert die Zahl der Elektronen je 59,5 mV Barrierenhöhe um den Faktor 10. Je dicker das Oxid und je höher die Dotierung, desto größer $m$ und desto flacher fällt der Strom. Beim Beispieltransistor sind es 80,7 mV; die vollständige Rechnung ergibt 82,8 mV.

Idee der Herleitung: Man teilt eine Änderung der Gatespannung auf Oxid und Verarmungszone auf und setzt den Anteil an der Oberfläche in den Boltzmann-Faktor ein.

:::herleitung
**Ausgangspunkt:** die Spannungsbilanz des MOS-Kondensators aus [Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html), Gatespannung gleich Flachbandspannung plus Oberflächenpotential plus Spannung über dem Oxid, und der Unterschwellenstrom aus diesem Abschnitt.

**Annahmen:**
(i) $U_{DS}$ ist groß gegen $U_T$, die Klammer im Unterschwellenstrom also 1.
(ii) Die Elektronenladung am Source-Ende wächst wie die Elektronendichte an der Oberfläche mit $\exp(\psi_s/U_T)$; ihre übrigen Faktoren ändern sich vergleichsweise langsam.
(iii) Schwache Inversion: Eine Änderung der Gateladung wird ganz von der Verarmungszone aufgenommen.

**Schritt 1**: Ändert sich die Gatespannung, ändern sich Oberflächenpotential und Oxidspannung; die Flachbandspannung bleibt:

$$\Delta U_{GS} = \Delta\psi_s + \Delta U_\mathrm{ox}$$

**Schritt 2**: Die Oxidspannung ist Gateladung durch Oxidkapazität; nach (iii) ist die Änderung der Gateladung die der Verarmungsladung, $C'_\mathrm{dep}\,\Delta\psi_s$:

$$\Delta U_\mathrm{ox} = \frac{C'_\mathrm{dep}}{C'_\mathrm{ox}}\,\Delta\psi_s$$

**Schritt 3** (entscheidender Schritt): Zusammen ergibt sich der kapazitive Spannungsteiler:

$$\Delta U_{GS} = \Big(1 + \frac{C'_\mathrm{dep}}{C'_\mathrm{ox}}\Big)\,\Delta\psi_s = m\,\Delta\psi_s$$

**Schritt 4**: Nach (i) und (ii) ist der Strom proportional zu $\exp(\psi_s/U_T)$. Er wächst um den Faktor 10, wenn $\psi_s$ um $U_T\ln 10$ steigt, also wenn $U_{GS}$ um $m$ mal so viel steigt:

**Ergebnis:**

$$S_\mathrm{sub} = m\,U_T\,\ln 10, \qquad m = 1 + \frac{C'_\mathrm{dep}}{C'_\mathrm{ox}}\,$$

**Woher die Faktoren kommen:** $U_T\ln 10$ aus der Boltzmann-Verteilung, $m$ aus dem Spannungsteiler.

**Proben:** Einheit V. Grenzfall: Für $C'_\mathrm{dep}$ viel kleiner als $C'_\mathrm{ox}$ wird $m$ = 1 und $S_\mathrm{sub}$ = 25,85 mV · 2,303 = 59,5 mV. Zahlenwert: 1,356 · 59,5 mV = 80,7 mV.

**Grenzen:** $C'_\mathrm{dep}$ hängt vom Oberflächenpotential ab, $S_\mathrm{sub}$ ändert sich deshalb leicht mit $U_{GS}$; nahe der Schwelle gilt (iii) nicht mehr. $S_\mathrm{sub}$ ist proportional zur Temperatur: Bei 100 °C sind es 24 % mehr.
:::

::::beispiel Unterschwellensteigung des Beispieltransistors
**Gegeben:** $N_A$ = 5,68·10¹⁷ cm⁻³, $\varepsilon_\mathrm{Si}$ = 1,036·10⁻¹² F/cm, $e$ = 1,602·10⁻¹⁹ C, $C'_\mathrm{ox}$ = 6,906·10⁻⁷ F/cm²; Oberflächenpotential bei $U_{GS}$ = 0,3 V aus der vollständigen Rechnung 0,781 V; berechnete Ströme 0,12 nA bei 0,2 V und 32 nA bei 0,4 V.

**Gesucht:** $m$ und $S_\mathrm{sub}$ aus der Formel und aus den Strömen; der Anstieg des Leckstroms, wenn die Schwelle um 0,25 V niedriger liegt.

**Rechnung:** Kapazität der Verarmungszone, die Ableitung ihrer Ladung nach dem Oberflächenpotential:

$$C'_\mathrm{dep} = \sqrt{\frac{e\,\varepsilon_\mathrm{Si}\,N_A}{2\,\psi_s}} = \sqrt{\frac{9{,}43\cdot10^{-14}\ \mathrm{F\,C/cm^4}}{1{,}562\ \mathrm V}} = 2{,}457\cdot10^{-7}\ \mathrm{F/cm^2}$$

$$m = 1 + \frac{2{,}457}{6{,}906} = 1{,}356, \qquad S = 1{,}356\cdot25{,}85\ \mathrm{mV}\cdot2{,}303 = 80{,}7\ \mathrm{mV}\,$$

Aus den Strömen: Zwischen 0,2 V und 0,4 V wächst der Strom um den Faktor 261, also um 2,42 Dekaden:

$$S_\mathrm{sub} = \frac{200\ \mathrm{mV}}{2{,}42} = 82{,}8\ \mathrm{mV}$$

Eine um 0,25 V niedrigere Schwelle verschiebt die Gerade um 0,25 V nach links; der Strom bei $U_{GS}$ = 0 wächst um

$$10^{0{,}25\ \mathrm V/0{,}0828\ \mathrm V} = 10^{3{,}02} \approx 1000$$

**Ergebnis:** **$m$ = 1,356 und $S_\mathrm{sub}$ = 80,7 mV aus der Formel, 82,8 mV aus der vollständigen Rechnung; 0,25 V weniger Schwelle bedeuten den tausendfachen Leckstrom.**

**Einordnung:** Die beiden Werte von $S_\mathrm{sub}$ unterscheiden sich um 2,5 %, weil $m$ zwischen 0,2 V und 0,4 V nicht ganz konstant ist und die Faktoren neben der Exponentialfunktion mitwirken. Die Zahl zeigt das Dilemma integrierter Schaltungen: Eine niedrige Schwelle bringt bei gleicher Versorgungsspannung mehr Strom und damit schnellere Gatter, kostet aber je 83 mV eine Dekade Leckstrom. Weil $S_\mathrm{sub}$ nicht unter 59,5 mV sinken kann, lassen sich Schwellen- und Versorgungsspannung nicht beliebig verkleinern.
::::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Kanalpotential steigt zum Drain immer steiler | ein dünnerer Kanal braucht schnellere Elektronen und damit ein stärkeres Feld |
| Triodengleichung | der gleiche Strom in jedem Querschnitt, über den ganzen Kanal aufsummiert |
| Krümmung der Kennlinie, Faktor 1/2 | jede weitere Drainspannung trifft am Drain-Ende auf weniger Ladung |
| Maximum der Parabel an der Abschnürgrenze | am Drain-Ende ist die Ladung aufgebraucht; weitere Spannung findet keinen Kanal mehr |
| Quadratgesetz | der Kanal bis zum Abschnürpunkt sieht immer die Gate-Übersteuerung; Ladung und Spannung wachsen beide mit ihr |
| Kanallängenmodulation | derselbe Kanal, nur kürzer: bei gleicher Spannung mehr Strom |
| Unterschwellenstrom | auch ohne Feld fließt durch jeden Querschnitt derselbe Strom, getragen von Diffusion |

Durch jeden Querschnitt des Kanals fließt derselbe Strom, das Produkt aus Elektronenladung pro Länge und Geschwindigkeit der Elektronen; wo der Kanal zum Drain hin dünner wird, laufen die Elektronen schneller, und aus dieser Bedingung folgt die Triodengleichung, deren Maximum genau an der Abschnürgrenze liegt und die von dort an als Quadratgesetz stehen bleibt, bis auf einen leichten Anstieg, weil der Kanal mit wachsender Drainspannung kürzer wird.

## Bedeutung und Ausblick

In digitalen CMOS-Schaltungen bestimmt das Quadratgesetz, wie schnell ein Gatter eine Last umlädt: Ein eingeschalteter Transistor liefert zunächst den Sättigungsstrom und geht, wenn die Spannung über ihm sinkt, in den ohmschen Bereich über. Verstärker und Stromquellen arbeiten im Abschnürbereich; dort sind die Steigung der Übertragungskennlinie, 1 mS bei 1 V Gatespannung, und die Steigung der Ausgangskennlinie, 25 µS, die beiden Größen, mit denen das Kleinsignalmodell rechnet; die Stufen im Artikel über [Vierpole](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/vierpole-ausfuehrlich.html) benutzen genau diese Werte. Gemessen werden Kennlinien mit einem Halbleiter-Parameteranalysator, der $U_{GS}$ in Stufen setzt und $U_{DS}$ durchfährt; Schwellenspannung und $K_n$ entnimmt man der Wurzel des Sättigungsstroms, λ der Steigung im Abschnürbereich.

Die Grenzen des Modells liegen bei kurzen Kanälen, wo die Geschwindigkeit der Elektronen sättigt, bei hohen Gatespannungen, wo die Beweglichkeit sinkt, und unterhalb der Schwelle, wo statt null ein exponentieller Strom fließt. Der nächste Artikel, PMOS-Transistor, Substrateffekt und Latch-Up, überträgt die Gleichungen auf den PMOS und zeigt, wie eine Spannung zwischen Bulk und Source die Schwelle verschiebt. Aus Sicht der Bauelementphysik behandelt [Der MOSFET](/wissen/elektrotechnik/4-semester/grundlagen-elektronischer-materialien-und-bauelemente/bauelemente/mosfet.html) dieselben Kennlinien.

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
A: Durch jeden Querschnitt fließt derselbe Strom, Ladung pro Länge mal Geschwindigkeit. Zum Drain hin sinkt die Ladung, weil dort die Spannung zwischen Gate und Kanal kleiner ist; bei 1 V und 0,3 V auf 40 %. Die Elektronen müssen dort 2,5-mal so schnell sein, 1,52·10⁶ statt 6,1·10⁵ cm/s, und das verlangt ein 2,5-mal so starkes treibendes Feld.
F: Warum liegt das Maximum der Triodenparabel genau an der Abschnürgrenze?
A: Die Steigung der Parabel ist $K_n$ mal der Übersteuerung am Drain-Ende, der Leitwert eines Kanals mit der Ladung des Drain-Endes. Sie wird null, wenn diese Ladung null wird, und das ist die Bedingung für das Abschnüren, $U_{DS} = U_{GS} - U_{th}$.
F: Warum bleibt der Strom oberhalb der Abschnürgrenze fast konstant, statt der Parabel folgend zu fallen?
A: Die Parabel setzt einen Kanal bis zum Drain voraus. Jenseits der Grenze endet der Kanal am Abschnürpunkt, an dem das Potential immer $U_{GS} - U_{th}$ beträgt; der Kanal sieht dieselbe Spannung wie an der Grenze und führt denselben Strom, der Rest der Spannung fällt über der kurzen Zone vor dem Drain ab.
F: Warum steigt der Strom im Abschnürbereich mit $U_{DS}$ doch leicht an?
A: Die Zone vor dem Drain wächst mit $U_{DS}$, der leitende Kanal wird kürzer. Bei gleicher Spannung und gleicher Ladung an der Source führt ein kürzerer Kanal mehr Strom; das Modell beschreibt das mit dem Faktor $(1 + \lambda U_{DS})$.
F: Stimmt es, dass der Strom hinter dem Maximum der Parabel wieder abnimmt?
A: Nein. Der abfallende Ast beschreibt einen Kanal mit einer negativen Zahl von Elektronen am Drain-Ende, den es nicht gibt. Der Strom bleibt beim Maximum, beim Beispieltransistor 0,25 mA bei 1 V Gatespannung, statt auf 0,1875 mA bei 0,75 V und null bei 1 V zu fallen.
F: Stimmt es, dass doppelte Gatespannung den vierfachen Strom ergibt?
A: Nein. Quadriert wird die Übersteuerung $U_{GS} - U_{th}$. Von 1 V auf 2 V Gatespannung steigt sie von 0,5 V auf 1,5 V, der Strom von 0,25 mA auf 2,25 mA, also um den Faktor 9.
F: Stimmt es, dass der Drainstrom im Abschnürbereich nicht von $U_{DS}$ abhängt?
A: Nein. Wegen der Kanallängenmodulation steigt er weiter, beim Beispieltransistor mit 25 µA/V bei 1 V Gatespannung, von 0,2625 mA an der Grenze auf 0,30 mA bei 2 V.
F: Welchen Strom führt der Beispieltransistor bei $U_{GS}$ = 1 V und $U_{DS}$ = 0,3 V, und wie viel ergäbe die Widerstandsgerade mit 1 kΩ?
A: $K_n[(0{,}5\ \mathrm V)(0{,}3\ \mathrm V) - (0{,}3\ \mathrm V)^2/2]$ = 2 mA/V² · 0,105 V² = 0,21 mA, gegen 0,3 mA nach der Geraden, also 70 %, weil der Kanal zum Drain hin dünner wird.
F: Wie bestimmt man die Schwellenspannung aus Messungen im Abschnürbereich, und warum nicht mit der Tangente an die Übertragungskennlinie?
A: Man trägt die Wurzel des Stroms über $U_{GS}$ auf; die Punkte liegen auf einer Geraden, die die Achse bei $U_{th}$ schneidet, beim Beispiel aus 0,25 mA bei 1 V und 1 mA bei 1,5 V genau 0,5 V. Die Tangente an die Parabel trifft die Achse in der Mitte zwischen Schwelle und Messpunkt, bei 1 V also bei 0,75 V.
F: Wie groß ist der Strom des Beispieltransistors bei $U_{GS}$ = 0, und wie schnell fällt er unterhalb der Schwelle?
A: Rund 0,56 pA, weil einige Elektronen die Barriere zwischen Source und Kanal thermisch überwinden und zum Drain diffundieren. Der Strom fällt je 83 mV weniger Gatespannung um eine Dekade; schneller als 59,5 mV je Dekade kann er bei Raumtemperatur nicht fallen.
:::
