---
title: PMOS-Transistor, Substrateffekt und Latch-Up
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / MOS-Feldeffekttransistoren
order: 33030300
summary: Wie der p-Kanal-MOSFET als Spiegelbild des NMOS arbeitet, warum eine Spannung zwischen Bulk und Source die Schwellenspannung verschiebt und wie in CMOS-Schaltungen ein parasitärer Thyristor die Versorgung kurzschließen kann. Ausführliche Fassung mit den PMOS-Gleichungen in Vorzeichen- und Betragsform, der Herleitung des Substrateffekts aus der Spannungsbilanz, dem Bulk als zweitem Gate, Sourcefolgern mit gemeinsamer und eigener Wanne, Zündbedingung, Haltestrom und Gegenmaßnahmen des Latch-Up, durchgerechnet am Beispiel-Transistorpaar.
tags: PMOS, Substrateffekt, Body-Effekt, Latch-Up, CMOS
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

In einer integrierten CMOS-Schaltung sitzen n-Kanal- und p-Kanal-Transistoren nebeneinander auf derselben Siliziumscheibe. Das Modell des NMOS aus [Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien-ausfuehrlich.html) braucht deshalb drei Ergänzungen: die Gleichungen des PMOS, den Einfluss des vierten Anschlusses, des Bulk, und die Gefahr, die von den vielen pn-Übergängen zwischen den Transistoren ausgeht. Alles hängt an einem Prinzip:

**Ein MOSFET ist nur durch gesperrte pn-Übergänge von seiner Umgebung getrennt, und sein Bulk wirkt wie ein zweites Gate: Beim PMOS sind Gebiete und Vorzeichen vertauscht, eine Sperrspannung zwischen Bulk und Source vergrößert die Verarmungsladung und damit den Betrag der Schwelle, und werden die trennenden Übergänge leitend, bilden Wanne und Substrat einen Thyristor, der die Versorgung kurzschließt.**

Vorausgesetzt werden Aufbau, Schwellenspannung und Bulkregel aus [Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html), die Kennlinien des NMOS und für den Latch-Up der Bipolartransistor aus [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise-ausfuehrlich.html). Auf diesem Artikel bauen die parasitären Kapazitäten, das Kleinsignalmodell mit der Substratsteilheit und alle CMOS-Schaltungen auf.

:::grafik
Szene: st1/mos-feldeffekttransistoren/03-cmos-ueberblick · Vorlage: querschnitt-hervorhebungen
**Abbildung 1:** CMOS-Querschnitt, schematisch: links ein NMOS im p-Substrat mit Substratkontakt an Masse, rechts ein PMOS in der n-Wanne mit Wannenkontakt an der Versorgung $U_B$ = 2,5 V; alle pn-Übergänge als kleine, gesperrte Dioden. Drei Hervorhebungen: (1) der PMOS als Spiegelbild mit Löcherkanal und negativen Spannungen gegen die Source; (2) ein NMOS, dessen Source 1 V über dem Substrat liegt, mit einer Verarmungszone von 66 statt 46 nm unter dem Gate; (3) gestrichelt der Pfad von der PMOS-Source durch Wanne und Substrat zur NMOS-Source, die Schichtfolge p⁺–n–p–n⁺. Die Transistoren sind nur durch gesperrte pn-Übergänge voneinander getrennt, und das Potential von Substrat und Wanne wirkt auf jeden Transistor mit.
:::

## Von Grund auf: pn-Übergang, Schwellenspannung und Bipolartransistor

*Welche drei Bausteine braucht man, bevor PMOS, Substrateffekt und Latch-Up verständlich werden?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/03-grundlagen · Vorlage: grundlagen-dreiteilig
**Abbildung 2:** Die drei Grundbausteine. (a) pn-Übergang zwischen einem n⁺-Gebiet und dem p-Substrat des Beispieltransistors: Querschnitt mit der grauen Raumladungszone, ohne Spannung 48,4 nm breit, bei 1 V Sperrspannung 67,9 nm und bei 2,5 V 89,6 nm, maßstäblich übereinander; daneben die Kennlinie eines Übergangs mit dem Sättigungsstrom 10⁻¹⁶ A, in Sperrrichtung praktisch null, in Durchlassrichtung 1,2 µA bei 0,6 V, 57 µA bei 0,7 V und 1 mA bei 0,774 V, zehnmal so viel je 59,5 mV mehr. (b) Beispiel-NMOS genau an der Schwelle, Source und Bulk an Masse: Gate über 5 nm Oxid, darunter die 45,8 nm tiefe Verarmungszone mit 4,17 fC/µm² aus Akzeptorrümpfen; an der Oberfläche 5,7·10¹⁷ Elektronen pro cm³ statt 176 im Inneren, weil sie 0,923 V über dem Inneren liegt; daneben ein Balken mit der Spannungsbilanz der Schwelle: −1,03 V Flachbandspannung, +0,923 V Anhebung der Oberfläche, +0,604 V über dem Oxid, zusammen 0,500 V. (c) npn-Bipolartransistor: Emitter n, dünne Basis p, Kollektor n; Elektronen (blau) laufen vom Emitter durch die Basis in den Kollektor, 1 mA, über den Basisanschluss fließen 10 µA, bei 0,774 V zwischen Basis und Emitter; daneben der pnp mit umgekehrten Schichten und Strömen. Gesperrte pn-Übergänge trennen Gebiete, und ihre Zonen wachsen mit der Wurzel der Spannung; die Schwelle ist eine Spannungsbilanz, in der die Ladung der Verarmungszone steckt; und im Bipolartransistor ist der Kollektorstrom ein festes Vielfaches des Basisstroms.
:::

### Der pn-Übergang: sperren und leiten

Ein __pn-Übergang__ ist die Grenze zwischen einem p-dotierten Gebiet, in dem bewegliche Löcher den Strom tragen, und einem n-dotierten mit beweglichen Elektronen. An der Grenze liegt die __Raumladungszone__, ein Streifen ohne bewegliche Ladungsträger, in dem nur die ortsfest geladenen Dotieratome zurückbleiben, auf der p-Seite negative, auf der n-Seite positive. Ihre Ladung erzeugt eine Spannungsstufe, die Elektronen und Löcher jeweils auf ihrer Seite hält ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie-ausfuehrlich.html)).

Liegt die n-Seite höher als die p-Seite, ist der Übergang in __Sperrrichtung__ gepolt: Die Stufe wächst, die Zone wird breiter, und es fließt praktisch kein Strom. Die Breite wächst mit der Wurzel der Spannung über der Zone; zwischen einem n⁺-Gebiet und dem p-Substrat des Beispieltransistors sind es ohne Spannung 48,4 nm, bei 1 V Sperrspannung 67,9 nm und bei 2,5 V 89,6 nm (Abbildung 2a). Liegt die p-Seite höher, in __Durchlassrichtung__, sinkt die Stufe; ab rund 0,6 V fließt merklich Strom, und jede weiteren 59,5 mV verzehnfachen ihn.

In einer integrierten Schaltung trennen solche Übergänge die Transistoren voneinander, aber nur, solange keiner von ihnen in Durchlassrichtung gepolt ist. Deshalb liegt das p-Substrat, in dem die NMOS-Transistoren sitzen, an der niedrigsten Spannung der Schaltung, meist an Masse: Dann sperren alle seine Übergänge zu den n-Gebieten.

### Der NMOS-Transistor und seine Schwellenspannung

Im __NMOS__-Transistor liegen zwei stark n-dotierte Gebiete, __Source__ und __Drain__, in p-dotiertem Silizium, dem __Bulk__; zwischen ihnen liegt auf 5 nm Oxid das __Gate__ (Abbildung 2b). Hebt das Gate das Potential der Siliziumoberfläche gegenüber dem Inneren an, verdrängt es die Löcher von dort, und eine __Verarmungszone__ aus Akzeptorrümpfen entsteht, deren Tiefe mit der Wurzel der Anhebung wächst. Zugleich zieht es Elektronen an: Im Inneren gibt es nur 176 pro Kubikzentimeter, und jede 59,5 mV, um die die Oberfläche höher liegt, verzehnfachen ihre Dichte dort, nach der __Boltzmann-Verteilung__. Bei 0,923 V Anhebung sind es 5,7·10¹⁷ pro Kubikzentimeter, so viele wie Dotieratome; ab hier bilden die Elektronen, die aus der Source nachfließen, eine leitende Schicht zum Drain, den __Kanal__. Diese Anhebung an der Schwelle schreibt man $2\Phi_F$ ([Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html)).

Die Gatespannung, bei der das erreicht ist, heißt __Schwellenspannung__ $U_{th}$, beim Beispiel-NMOS 0,5 V. Sie ist eine Bilanz aus drei Teilen: der Anhebung der Oberfläche, 0,923 V; der Spannung über dem Oxid, die das Gate braucht, um die Gegenladung zur Verarmungszone zu tragen, bei 45,8 nm Tiefe 4,17 fC/µm² und damit 0,604 V; und der __Flachbandspannung__ −1,03 V. Sie entsteht, weil das Gate aus n⁺-Silizium und der Bulk aus p-Silizium verschieden dotiert sind: Wie an einem pn-Übergang liegt zwischen ihnen schon ohne äußere Spannung eine innere Spannung, hier 1,03 V mit dem Gate auf der höheren Seite, und um sie braucht das Gate weniger äußere Spannung. Zusammen ergeben die drei Teile 0,500 V. Je mehr Ladung die Verarmungszone trägt, desto höher ist also die Schwelle.

Oberhalb der Schwelle wirkt der Kanal bei kleiner Drain-Source-Spannung wie ein Widerstand, im __ohmschen Bereich__. Übersteigt die Drain-Source-Spannung die __Übersteuerung__ $U_{GS} - U_{th}$, endet der Kanal vor dem Drain, im __Abschnürbereich__; dort wächst der Strom mit dem Quadrat der Übersteuerung, beim Beispiel-NMOS 0,25 mA bei 1 V Gatespannung, und mit jedem Volt Drain-Source-Spannung um ein Zehntel davon, weil sich der Kanal verkürzt ([Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien-ausfuehrlich.html)). In allen diesen Zahlen liegt der Bulk auf dem Potential der Source.

### Der Bipolartransistor: Kollektorstrom und Basisstrom

Ein __Bipolartransistor__ besteht aus drei abwechselnd dotierten Schichten, beim __npn__-Transistor n, p und n: dem __Emitter__, einer dünnen __Basis__ und dem __Kollektor__, also aus zwei pn-Übergängen, die sich die Basis teilen. Leitet der Übergang zwischen Basis und Emitter, ab rund 0,6 V, schickt der Emitter Elektronen in die Basis. Fast alle durchqueren die dünne Schicht und gelangen über den gesperrten Übergang zwischen Basis und Kollektor in den Kollektor; über den Basisanschluss fließt nur ein kleiner Strom, der __Basisstrom__, der die Löcher ersetzt, die unterwegs mit Elektronen rekombinieren oder in den Emitter gelangen.

Das Verhältnis von Kollektor- zu Basisstrom ist die __Stromverstärkung__ $B$. Beim Beispieltransistor aus [Bipolartransistor: Arbeitsbereiche und Transportmodell](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/bipolartransistor/aufbau-und-transportmodell-ausfuehrlich.html) fließen bei 0,774 V zwischen Basis und Emitter 1 mA in den Kollektor und 10 µA in die Basis, $B$ = 100 (Abbildung 2c). Solange beide Übergänge so gepolt bleiben, gehört zu jedem zusätzlichen Mikroampere Basisstrom das $B$-Fache an Kollektorstrom. Der __pnp__-Transistor ist dasselbe mit vertauschten Schichten, Ladungsträgern und Vorzeichen.

## Der PMOS-Transistor

*Wie arbeitet der p-Kanal-MOSFET, und warum sind bei ihm Spannungen und Strom negativ?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/03-pmos-kennlinien · Vorlage: schaltzeichen-kennlinienfeld
**Abbildung 3:** (a) Schaltzeichen des PMOS mit denselben Zählpfeilen wie beim NMOS: $U_{GS}$ und $U_{DS}$ vom Gate bzw. Drain zur Source, $U_{BS}$ vom Bulk zur Source, $I_D$ in den Drain hinein; daneben das Großsignal-Ersatzschaltbild mit offenem Gate und gesteuerter Stromquelle zwischen Source und Drain, dazu die Betragsgrößen $U_{SG}$, $U_{SD}$ und $I_{SD}$. (b) Ausgangskennlinien des Beispiel-PMOS mit Vorzeichen im dritten Quadranten: $I_D$ über $U_{DS}$ von 0 bis −2,5 V für $U_{GS}$ = −0,75 V, −1 V, −1,25 V und −1,5 V, bei −2,5 V −0,078 mA, −0,3125 mA, −0,703 mA und −1,25 mA; gestrichelt die Bereichsgrenze bei $U_{DS} = U_{GS} - U_{th,p}$. (c) Dieselben Kennlinien in Betragsdarstellung, $I_{SD}$ über $U_{SD}$. Der PMOS verhält sich wie ein NMOS mit umgekehrten Vorzeichen aller Spannungen und Ströme.
:::

Der PMOS ist das Spiegelbild des NMOS aus dem Abschnitt *Von Grund auf*. Source und Drain sind stark p-dotierte Gebiete (p⁺) in einer n-dotierten __Wanne__, einem Gebiet, das in das p-Substrat eingebracht ist und über einen n⁺-Kontakt an der höchsten Spannung der Schaltung liegt. Liegt das Gate weit genug unter der Source, zieht es Löcher an die Oberfläche der Wanne, und eine Löcherschicht verbindet Source und Drain. Die Löcher tragen positive Ladung und laufen vom höheren zum niedrigeren Potential; die Source ist deshalb beim PMOS das p⁺-Gebiet mit dem höheren Potential, und der Strom fließt im Kanal von der Source zum Drain und aus dem Drain heraus.

Gezählt wird mit denselben Pfeilen wie beim NMOS (Abbildung 3a), und dann sind im Betrieb alle Größen negativ: Das Gate liegt unter der Source, $U_{GS}$ < 0; der Drain liegt unter der Source, $U_{DS}$ < 0; der in den Drain hinein gezählte Strom $I_D$ ist negativ, weil der Strom herausfließt. Auch die Schwellenspannung ist negativ, beim Beispiel-PMOS −0,5 V: Erst wenn $U_{GS}$ unter −0,5 V sinkt, entsteht der Kanal. Die Kennlinien liegen deshalb im dritten Quadranten (Abbildung 3b) und gleichen gespiegelt denen des NMOS (Abbildung 3c).

**Die Akteure:**

- __$U_{th,p}$__: Schwellenspannung des PMOS, negativ; −0,5 V beim Beispiel-PMOS.
- __$K_p$__: Steilheitskoeffizient des PMOS, $K'_p W/L$ mit dem Prozessparameter $K'_p = \mu_p C'_\mathrm{ox}$; 2 mA/V² bei 50 µA/V² und $W/L$ = 40.
- __$\mu_p$__: Beweglichkeit der Löcher im Kanal; 72 cm²/(V s), ein Viertel der 290 cm²/(V s) der Elektronen.
- __$U_{SG}$__, __$U_{SD}$__, __$I_{SD}$__: die Betragsgrößen, gezählt von der Source zum Gate bzw. Drain und als Strom von der Source zum Drain; im Betrieb positiv, jeweils das Negative von $U_{GS}$, $U_{DS}$ und $I_D$.
- __$\lambda$__: Kanallängenmodulationsfaktor, hier als positiver Betrag; 0,1 1/V wie beim NMOS.

:::formel Formel
Sperrbereich, $U_{GS} > U_{th,p}$:

$$I_D = 0$$

Ohmscher Bereich, $U_{GS} < U_{th,p}$ und $U_{DS} > U_{GS} - U_{th,p}$:

$$I_D = -K_p\Big[\big(U_{GS} - U_{th,p}\big)\,U_{DS} - \frac{U_{DS}^2}{2}\Big]\big(1 - \lambda\,U_{DS}\big)$$

Abschnürbereich, $U_{GS} < U_{th,p}$ und $U_{DS}$ höchstens $U_{GS} - U_{th,p}$:

$$I_D = -\frac{K_p}{2}\,\big(U_{GS} - U_{th,p}\big)^2\,\big(1 - \lambda\,U_{DS}\big)$$
:::

**So liest man das:** Eingaben sind die negativen Spannungen $U_{GS}$ und $U_{DS}$, Ausgabe ist der negative Drainstrom. Alle Ungleichungen sind gegenüber dem NMOS umgekehrt: Der PMOS sperrt, solange $U_{GS}$ über der Schwelle liegt, also weniger negativ ist, und er ist abgeschnürt, wenn $U_{DS}$ noch negativer ist als $U_{GS} - U_{th,p}$. Der Faktor $(1 - \lambda U_{DS})$ ist bei negativem $U_{DS}$ größer als 1, wie beim NMOS. Üblich ist auch, λ für den PMOS selbst negativ anzugeben; dann steht dort $(1 + \lambda U_{DS})$. Setzt man alle Größen dem Betrag nach ein, erhält man genau die NMOS-Gleichungen, im Abschnürbereich etwa

$$I_{SD} = \frac{K_p}{2}\,\big(U_{SG} - |U_{th,p}|\big)^2\,\big(1 + \lambda\,U_{SD}\big)$$

Mit dieser __Betragsform__ rechnet man meist.

**Kurz gesagt:** Kehrt man beim PMOS die Vorzeichen aller Spannungen, des Stroms und der Schwellenspannung um, gelten genau die Gleichungen des NMOS.

Idee der Herleitung: Man wiederholt die Herleitung des NMOS mit Löchern statt Elektronen und misst alle Spannungen von der Source aus nach unten.

:::herleitung
**Ausgangspunkt:** die Herleitung der Triodengleichung und des Quadratgesetzes aus [Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien-ausfuehrlich.html), dort für Elektronen mit der Ladung pro Fläche $C'_\mathrm{ox}$ mal der örtlichen Übersteuerung.

**Annahmen:**
(i) dieselben wie beim NMOS: Langkanal, allmählicher Kanal, konstante Beweglichkeit, hier die der Löcher $\mu_p$;
(ii) der Bulk, also die Wanne, liegt auf dem Potential der Source.

**Schritt 1**: Beim PMOS sind alle Ladungen und Spannungen gespiegelt. Misst man von der Source nach unten, mit $U_{SG}$, $U_{SD}$ und der Spannung $U_{SC}(x)$ von der Source zum Kanal an der Stelle $x$, trägt der Kanal oberhalb der Schwelle die positive Löcherladung pro Fläche

$$Q'_p(x) = C'_\mathrm{ox}\,\big(U_{SG} - |U_{th,p}| - U_{SC}(x)\big)$$

**Schritt 2**: Die Löcher laufen zum niedrigeren Potential, also zum Drain, mit der Geschwindigkeit $\mu_p\,dU_{SC}/dx$; der Strom fließt in ihrer Richtung, von der Source zum Drain:

$$I_{SD} = \mu_p\,W\,C'_\mathrm{ox}\,\big(U_{SG} - |U_{th,p}| - U_{SC}(x)\big)\,\frac{dU_{SC}}{dx}$$

**Schritt 3**: Das ist die Stromgleichung des NMOS mit vertauschten Namen. Dieselbe Integration und dieselbe Überlegung zur Abschnürung ergeben mit $K_p = \mu_p C'_\mathrm{ox} W/L$ und dem Faktor der Kanallängenmodulation

$$I_{SD} = K_p\Big[\big(U_{SG} - |U_{th,p}|\big)\,U_{SD} - \frac{U_{SD}^2}{2}\Big]\big(1 + \lambda\,U_{SD}\big)$$

im ohmschen Bereich für $U_{SD} < U_{SG} - |U_{th,p}|$, sonst im Abschnürbereich

$$I_{SD} = \frac{K_p}{2}\,\big(U_{SG} - |U_{th,p}|\big)^2\,\big(1 + \lambda\,U_{SD}\big)$$

**Schritt 4** (entscheidender Schritt): Rückübersetzung in die Zählpfeile des NMOS:

$$I_D = -I_{SD}, \qquad U_{SG} = -U_{GS}, \qquad U_{SD} = -U_{DS}, \qquad |U_{th,p}| = -U_{th,p}\,$$

Die Übersteuerung wird dabei zu $-(U_{GS} - U_{th,p})$; das Produkt zweier negativer Größen bleibt positiv, das Quadrat ebenso.

**Schritt 5**: Die Bereichsgrenzen übersetzen sich mit umgekehrtem Ungleichheitszeichen: $U_{SG} > |U_{th,p}|$ wird zu $U_{GS} < U_{th,p}$, und $U_{SD} < U_{SG} - |U_{th,p}|$ wird zu $U_{DS} > U_{GS} - U_{th,p}$.

**Ergebnis:** im Sperrbereich $I_D$ = 0, sonst

$$I_D = -K_p\Big[\big(U_{GS} - U_{th,p}\big)\,U_{DS} - \frac{U_{DS}^2}{2}\Big]\big(1 - \lambda\,U_{DS}\big)$$

$$I_D = -\frac{K_p}{2}\,\big(U_{GS} - U_{th,p}\big)^2\,\big(1 - \lambda\,U_{DS}\big)$$

**Woher die Faktoren kommen:** Das Minuszeichen vor $K_p$ ist die Zählrichtung; $K_p$ enthält die Beweglichkeit der Löcher; $(1 - \lambda U_{DS})$ ist $(1 + \lambda U_{SD})$.

**Proben:** Bei $U_{GS}$ = −1 V und $U_{DS}$ = −0,3 V: $-2\ \mathrm{mA/V^2}\cdot(0{,}15 - 0{,}045)\ \mathrm{V^2}\cdot1{,}03$ = −0,2163 mA, dem Betrag nach derselbe Strom wie beim NMOS mit +1 V und +0,3 V. Grenzfall: An der Bereichsgrenze stimmen beide Ausdrücke überein.

**Grenzen:** Dieselben wie beim NMOS: Langkanal, Kanallängenmodulation als Modell, Unterschwellenstrom vernachlässigt.
:::

::::beispiel PMOS bei −1 V Gatespannung in Vorzeichen- und Betragsform
**Gegeben:** Beispiel-PMOS mit $K_p$ = 2 mA/V², $U_{th,p}$ = −0,5 V, λ = 0,1 1/V; $U_{GS}$ = −1 V; (a) $U_{DS}$ = −0,3 V, (b) $U_{DS}$ = −2 V; (c) der PMOS als Schalter zwischen $U_B$ = 2,5 V und einem Ausgang, Gate auf 0 V oder 2,5 V.

**Gesucht:** Drainstrom in beiden Formen; Widerstand des eingeschalteten Schalters.

**Rechnung:** (a) $U_{DS}$ = −0,3 V liegt über $U_{GS} - U_{th,p}$ = −0,5 V: ohmscher Bereich.

$$\begin{aligned} I_D &= -2\ \mathrm{mA/V^2}\cdot\big[(-0{,}5\ \mathrm V)(-0{,}3\ \mathrm V) - 0{,}045\ \mathrm{V^2}\big]\cdot1{,}03 \\ &= -0{,}2163\ \mathrm{mA} \end{aligned}$$

In Betragsform mit $U_{SG}$ = 1 V und $U_{SD}$ = 0,3 V:

$$I_{SD} = 2\ \mathrm{mA/V^2}\cdot\big[0{,}5\ \mathrm V\cdot0{,}3\ \mathrm V - 0{,}045\ \mathrm{V^2}\big]\cdot1{,}03 = 0{,}2163\ \mathrm{mA}$$

(b) $U_{DS}$ = −2 V liegt unter −0,5 V: Abschnürbereich.

$$I_D = -1\ \mathrm{mA/V^2}\cdot(-0{,}5\ \mathrm V)^2\cdot\big(1 + 0{,}2\big) = -0{,}30\ \mathrm{mA}$$

(c) Mit dem Gate auf 0 V ist $U_{GS}$ = −2,5 V; bei kleiner Spannung über dem Schalter ist er ein Widerstand:

$$R_\mathrm{on} = \frac{1}{K_p\,\big(U_{SG} - |U_{th,p}|\big)} = \frac{1}{2\ \mathrm{mA/V^2}\cdot2\ \mathrm V} = 250\ \Omega$$

Mit dem Gate auf 2,5 V ist $U_{GS}$ = 0, also über der Schwelle: Der PMOS sperrt.

**Ergebnis:** **(a) $I_D$ = −0,2163 mA, $I_{SD}$ = 0,2163 mA; (b) −0,30 mA; (c) 250 Ω bei 0 V am Gate, gesperrt bei 2,5 V.**

**Einordnung:** Beide Formen ergeben denselben Strom; die Betragsform vermeidet Vorzeichenfehler. Der PMOS leitet, wenn sein Gate tief liegt, der NMOS, wenn es hoch liegt; zwischen Versorgung und Masse ergänzen sich beide zu einem Schalterpaar, dem Grundprinzip der CMOS-Logik. Mit derselben Weite wie der NMOS, 10 µm statt 40 µm, hätte der PMOS nur 0,5 mA/V² und als Schalter 1 kΩ.
::::

:::frage
„Warum braucht der PMOS die vierfache Weite, um so viel Strom zu führen wie der NMOS?“
Löcher sind in Silizium langsamer als Elektronen: In reinem Silizium beträgt ihre Beweglichkeit 450 cm²/(V s) gegen 1400 cm²/(V s), und im Kanal, wo die Grenzfläche zum Oxid zusätzlich streut, sind es beim Beispielprozess 72 gegen 290 cm²/(V s). Der Prozessparameter $K'_p = \mu_p C'_\mathrm{ox}$ ist deshalb mit 50 µA/V² viermal kleiner als $K'_n$ mit 200 µA/V². Gleiche Ströme verlangen ein viermal größeres $W/L$, also bei gleicher Länge 40 statt 10 µm Weite. Der PMOS braucht dafür mehr Fläche und hat größere Kapazitäten.
:::

:::fehlvorstellung
„Beim PMOS setze ich die negativen Spannungen direkt in die NMOS-Gleichungen ein.“ Das liegt nahe, weil beide Transistoren dieselben Zählpfeile haben. Mit der positiven Schwelle des NMOS geht das schief: Bei $U_{GS}$ = −1 V und $U_{th}$ = +0,5 V meldet die Bereichsprüfung „gesperrt“, und quadriert man trotzdem, ergeben sich mit $(-1{,}5\ \mathrm V)^2$ 2,25 mA. Richtig sind im Abschnürbereich −0,25 mA, ohne Kanallängenmodulation gerechnet: Entweder rechnet man mit den PMOS-Gleichungen und der negativen Schwelle $U_{th,p}$ = −0,5 V, oder man setzt alle Größen dem Betrag nach in die NMOS-Gleichungen ein (Abschnitt *Der PMOS-Transistor*).
:::

## Der Substrateffekt

*Warum hängt die Schwellenspannung von der Spannung zwischen Bulk und Source ab?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/03-substrateffekt-querschnitt · Vorlage: querschnitt-vergleich
**Abbildung 4:** Zwei Querschnitte des Beispiel-NMOS unter dem Gate, jeweils genau an der Schwelle, maßstäblich in der Tiefe. (a) $U_{BS}$ = 0: Die Oberfläche liegt 0,923 V über dem Inneren des Substrats, die Verarmungszone ist 45,8 nm tief und trägt 4,17 fC/µm² feste negative Ladung; Schwelle 0,500 V. (b) $U_{BS}$ = −1 V, Source und Kanal also 1 V über dem Substrat: Die Oberfläche muss 1,923 V über dem Inneren liegen, die Zone ist 66,2 nm tief und trägt 6,02 fC/µm²; Schwelle 0,768 V gegen die Source. Daneben je ein Balken für die Ladung auf dem Gate, in (b) um 1,85 fC/µm² höher. Liegt die Source über dem Bulk, muss die Oberfläche höher angehoben werden; die breitere Verarmungszone bindet mehr Gateladung, und die Schwelle steigt.
:::

Bisher lag der Bulk an der Source. In einer integrierten Schaltung teilen sich aber alle NMOS-Transistoren dasselbe p-Substrat, und das liegt an der niedrigsten Spannung, meist an Masse. Ein NMOS, dessen Source 1 V über Masse liegt, hat deshalb zwischen Bulk und Source −1 V, und seine Schwelle liegt dann nicht mehr bei 0,5 V, sondern bei 0,768 V. Diese Verschiebung heißt __Substrateffekt__, englisch body effect.

**Die Akteure:**

- __$U_{BS}$__: Spannung vom Bulk zur Source; beim NMOS im Betrieb null oder negativ, weil der Bulk an der niedrigsten Spannung liegt. Negativ heißt: Der pn-Übergang zwischen Bulk und Source ist in Sperrrichtung gepolt. −1 V, wenn die Source 1 V über dem Substrat liegt.
- __$2\Phi_F$__: die Anhebung der Oberfläche über das Innere, das __Oberflächenpotential__, an der Schwelle bei $U_{BS}$ = 0 (Abschnitt *Von Grund auf*); 0,923 V.
- __$\gamma$__: __Substratsteuerfaktor__, auch Body-Effekt-Faktor, in √V; er misst, wie stark die Spannung am Bulk die Schwelle verschiebt; 0,63 √V beim Beispiel-NMOS.

**Das Zusammenspiel:**

**Schritt 1**: Die Elektronen des Kanals stammen aus der Source und liegen auf ihrem Potential. Starke Inversion heißt, dass die Elektronendichte an der Oberfläche die Dotierung erreicht; nach der Boltzmann-Verteilung (Abschnitt *Von Grund auf*) zählt dafür, wie hoch die Oberfläche über dem Potential der Elektronen liegt, und das ist das der Source.

**Schritt 2**: Liegt die Source 1 V über dem Bulk, muss die Oberfläche um $2\Phi_F$ über die Source hinaus angehoben werden, gegenüber dem Inneren des Substrats also um 1,923 V statt 0,923 V (Abbildung 4b).

**Schritt 3** (entscheidender Schritt): Ein höheres Oberflächenpotential verlangt eine breitere Verarmungszone. Ihre Tiefe wächst mit der Wurzel der Spannung über ihr, von 45,8 auf 66,2 nm, und ihre feste Ladung aus Akzeptorrümpfen von 4,17 auf 6,02 fC/µm².

**Schritt 4**: Diese zusätzliche Ladung von 1,85 fC/µm² muss das Gate als Gegenladung tragen, bevor ein Kanal entsteht. Über dem Oxid liegen dafür 1,85 fC/µm² geteilt durch 6,906 fF/µm², also 0,268 V mehr.

**Schritt 5**: Gegen die Source gemessen steigt die Schwelle um diese 0,268 V auf 0,768 V. Das um 1 V höhere Oberflächenpotential selbst zählt nicht mit, denn Gate und Oberfläche werden beide gegen die angehobene Source gerechnet; übrig bleibt nur die zusätzliche Ladung der Verarmungszone.

:::grafik
Szene: st1/mos-feldeffekttransistoren/03-schwelle-ubs · Vorlage: kennlinie
**Abbildung 5:** Schwellenspannung über der Sperrspannung zwischen Source und Bulk (beim NMOS −$U_{BS}$, beim PMOS +$U_{BS}$) von −0,4 V bis 2,5 V. NMOS: 0,500 V bei 0, 0,646 V bei 0,5 V, 0,768 V bei 1 V, 0,971 V bei 2 V und 1,059 V bei 2,5 V; links von null, wo der Bulk über der Source liegt, sinkt sie auf 0,431 V, 0,392 V und 0,351 V bei 0,2 V, 0,3 V und 0,4 V Durchlassspannung (grau hinterlegt: Die Diode zwischen Bulk und Source beginnt zu leiten). PMOS, Betrag der Schwelle: 0,500 V bei 0, 0,762 V bei 1 V, 1,048 V bei 2,5 V. Gestrichelt die Tangente im Nullpunkt mit der Steigung 0,327. Die Schwelle wächst mit der Wurzel der Sperrspannung zwischen Source und Bulk; jedes weitere Volt hebt sie weniger.
:::

:::formel Formel
$$U_{th} = U_{th0} + \gamma\,\Big(\sqrt{2\Phi_F - U_{BS}} - \sqrt{2\Phi_F}\Big)$$

$$\gamma = \frac{\sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A}}{C'_\mathrm{ox}}$$

beim PMOS (Index p) mit der Schwelle $U_{th0,p}$ bei $U_{BS}$ = 0 und der Dotierung $N_D$ der n-Wanne:

$$|U_{th,p}| = |U_{th0,p}| + \gamma_p\,\Big(\sqrt{2\Phi_{F,p} + U_{BS}} - \sqrt{2\Phi_{F,p}}\Big)$$

$$\gamma_p = \frac{\sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_D}}{C'_\mathrm{ox}}, \qquad \Phi_{F,p} = U_T\ln\frac{N_D}{n_i}\,$$
:::

**So liest man das:** Eingabe ist die Bulk-Source-Spannung, Ausgabe die Schwelle; bei $U_{BS}$ = 0 bleibt $U_{th0}$, die Schwelle ohne Substrateffekt. Je weiter der Bulk in Sperrrichtung gegen die Source gepolt ist, beim NMOS also je negativer $U_{BS}$, desto größer die Wurzel und desto höher die Schwelle. Weil die Verarmungszone nur mit der Wurzel wächst, bringt jedes weitere Volt weniger: Das erste Volt hebt die Schwelle um 0,268 V, das zweite nur noch um 0,203 V. $\gamma$ wächst mit der Wurzel der Dotierung und mit der Oxiddicke; der Beispiel-NMOS hat wegen der hohen Dotierung unter dem Gate, 5,7·10¹⁷ cm⁻³, ein großes $\gamma$, mit 10¹⁷ cm⁻³ wären es 0,26 √V, mit 10¹⁶ cm⁻³ nur 0,08 √V. Beim PMOS ist alles gespiegelt: Die n-Wanne liegt über der Source, positives $U_{BS}$ ist Sperrrichtung, und der Betrag der Schwelle wächst; beim Beispiel-PMOS mit $\gamma_p$ = 0,615 √V und $2\Phi_{F,p}$ = 0,921 V auf 0,762 V bei $U_{BS}$ = 1 V.

**Kurz gesagt:** Je weiter der Bulk in Sperrrichtung gegen die Source gepolt ist, desto größer ist der Betrag der Schwelle; jedes weitere Volt vergrößert ihn weniger als das vorige.

Idee der Herleitung: Man schreibt die Spannungsbilanz der Schwelle mit dem um die Bulk-Source-Spannung höheren Oberflächenpotential und rechnet dann gegen die Source.

:::herleitung
**Ausgangspunkt:** die Spannungsbilanz an der Schwelle und die Verarmungsladung aus [Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html), beide gegen den Bulk gemessen:

$$U_{GB} = U_\mathrm{FB} + \psi_s + \frac{|Q'_\mathrm{dep}|}{C'_\mathrm{ox}}, \qquad |Q'_\mathrm{dep}| = \sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A\,\psi_s}\,$$

**Annahmen:**
(i) Verarmungsnäherung wie dort; die Elektronenladung an der Schwelle ist klein gegen die Verarmungsladung.
(ii) Starke Inversion: Elektronendichte an der Oberfläche gleich $N_A$, gezählt gegen das Potential der Elektronen im Kanal, also das der Source.
(iii) $U_{BS}$ null oder negativ, oder nur so wenig positiv, dass die Diode zwischen Bulk und Source sperrt.

**Schritt 1**: Ohne Bulk-Source-Spannung ist das Oberflächenpotential an der Schwelle $2\Phi_F$. Liegt die Source um $-U_{BS}$ über dem Bulk, gilt nach (ii) dasselbe gegenüber der Source; gegenüber dem Bulk muss die Oberfläche also höher liegen:

$$\psi_s = 2\Phi_F - U_{BS}$$

**Schritt 2**: Eingesetzt in die Spannungsbilanz:

$$U_{GB} = U_\mathrm{FB} + 2\Phi_F - U_{BS} + \frac{\sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A\,\big(2\Phi_F - U_{BS}\big)}}{C'_\mathrm{ox}}$$

**Schritt 3** (entscheidender Schritt): Die Schwelle zählt gegen die Source. Mit der Maschenregel $U_{GS} = U_{GB} + U_{BS}$ hebt sich $-U_{BS}$ heraus:

$$U_{th} = U_\mathrm{FB} + 2\Phi_F + \frac{\sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A\,\big(2\Phi_F - U_{BS}\big)}}{C'_\mathrm{ox}}$$

**Schritt 4**: Bei $U_{BS}$ = 0 ist das $U_{th0}$. Die Differenz zu $U_{th0}$ enthält nur noch die Verarmungsladung; den gemeinsamen Faktor fasst man zu $\gamma$ zusammen:

$$U_{th} - U_{th0} = \frac{\sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A}}{C'_\mathrm{ox}}\,\Big(\sqrt{2\Phi_F - U_{BS}} - \sqrt{2\Phi_F}\Big)$$

**Schritt 5**: Beim PMOS sind alle Vorzeichen vertauscht: Die n-Wanne mit der Dotierung $N_D$ liegt über der Source, die Sperrspannung ist $+U_{BS}$, und dieselbe Rechnung ergibt für den Betrag der Schwelle die zweite Gleichung mit $\gamma_p$ und dem Fermipotential der Wanne:

$$2\Phi_{F,p} = 2\,U_T\ln\frac{N_D}{n_i}$$

**Ergebnis:**

$$U_{th} = U_{th0} + \gamma\,\Big(\sqrt{2\Phi_F - U_{BS}} - \sqrt{2\Phi_F}\Big), \qquad \gamma = \frac{\sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A}}{C'_\mathrm{ox}}\,$$

$$|U_{th,p}| = |U_{th0,p}| + \gamma_p\,\Big(\sqrt{2\Phi_{F,p} + U_{BS}} - \sqrt{2\Phi_{F,p}}\Big)$$

**Woher die Faktoren kommen:** Die Wurzeln stammen aus dem Wurzelgesetz der Verarmungszone; $\gamma$ ist die Verarmungsladung pro Wurzel-Volt geteilt durch die Oxidkapazität.

**Proben:** Einheit: $\sqrt{\mathrm{C\cdot F\cdot cm^{-1}\cdot cm^{-3}}}$ geteilt durch F/cm² ergibt √V, mal √V ergibt V. Zahlenwert: $\sqrt{2\cdot1{,}602\cdot10^{-19}\cdot1{,}036\cdot10^{-12}\cdot5{,}68\cdot10^{17}}$ C/(cm²·√V) geteilt durch 6,906·10⁻⁷ F/cm² ergibt 0,629 √V; bei $U_{BS}$ = −1 V: 0,629 · (1,387 − 0,961) V = 0,268 V. Die vollständige Lösung der Poisson-Gleichung, mit dem Potential der Elektronen um 1 V verschoben, ergibt an der Schwelle dieselben Werte, weil sich der Ausläufer der Löcher am Rand der Zone und die Elektronen an der Oberfläche genau ausgleichen.

**Grenzen:** Ist die Dotierung unter dem Gate nicht gleichmäßig, wie nach einer Implantation, ändert sich $\gamma$ mit der Tiefe der Zone. Ist $U_{BS}$ beim NMOS mehr als einige Zehntel Volt positiv, leitet die Diode zwischen Bulk und Source.
:::

::::beispiel Schwellenspannungen des Beispielpaars mit Substrateffekt
**Gegeben:** NMOS: $U_{th0}$ = 0,5 V, $\gamma$ = 0,629 √V, $2\Phi_F$ = 0,923 V; PMOS: $|U_{th0,p}|$ = 0,5 V, $\gamma_p$ = 0,615 √V, $2\Phi_{F,p}$ = 0,921 V.

**Gesucht:** die Schwelle des NMOS bei $U_{BS}$ = −0,5 V, −1 V und −2 V, die des PMOS bei $U_{BS}$ = 1 V und 2,5 V.

**Rechnung:** NMOS bei −1 V:

$$\begin{aligned} U_{th} &= 0{,}5\ \mathrm V + 0{,}629\ \sqrt{\mathrm V}\cdot\big(\sqrt{1{,}923\ \mathrm V} - \sqrt{0{,}923\ \mathrm V}\big) \\ &= 0{,}5\ \mathrm V + 0{,}268\ \mathrm V = 0{,}768\ \mathrm V \end{aligned}$$

Ebenso bei −0,5 V und −2 V:

$$U_{th} = 0{,}5\ \mathrm V + 0{,}146\ \mathrm V = 0{,}646\ \mathrm V, \qquad U_{th} = 0{,}5\ \mathrm V + 0{,}471\ \mathrm V = 0{,}971\ \mathrm V\,$$

PMOS bei 1 V und 2,5 V:

$$|U_{th,p}| = 0{,}5\ \mathrm V + 0{,}615\ \sqrt{\mathrm V}\cdot\big(\sqrt{1{,}921\ \mathrm V} - \sqrt{0{,}921\ \mathrm V}\big) = 0{,}762\ \mathrm V$$

$$|U_{th,p}| = 0{,}5\ \mathrm V + 0{,}615\ \sqrt{\mathrm V}\cdot\big(\sqrt{3{,}421\ \mathrm V} - \sqrt{0{,}921\ \mathrm V}\big) = 1{,}048\ \mathrm V$$

**Ergebnis:** **NMOS 0,646 V, 0,768 V und 0,971 V; PMOS 0,762 V und 1,048 V dem Betrag nach.**

**Einordnung:** Schon 1 V Sperrspannung hebt die Schwelle um mehr als die Hälfte; bei 2 V hat sie sich fast verdoppelt. Die Übersteuerung, die ein Gatter oder Verstärker zur Verfügung hat, schrumpft entsprechend. Für den Beispiel-NMOS mit 1 V Gatespannung bliebe bei $U_{BS}$ = −1 V nur noch 0,232 V Übersteuerung statt 0,5 V, und der Sättigungsstrom fiele von 0,25 mA auf 0,054 mA.
::::

:::fehlvorstellung
„Die Schwellenspannung ist eine feste Eigenschaft des Transistors, wie sie im Datenblatt steht.“ Das liegt nahe, weil Datenblatt und Modell einen einzigen Wert nennen. Dieser Wert gilt aber für eine bestimmte Bulk-Source-Spannung, meist null. Beim Beispiel-NMOS steigt die Schwelle bei $U_{BS}$ = −1 V von 0,5 V auf 0,768 V und bei −2 V auf 0,971 V (Abschnitt *Der Substrateffekt*); dazu sinkt sie mit steigender Temperatur. In einer integrierten Schaltung haben deshalb baugleiche Transistoren verschiedene Schwellen, je nachdem, wie hoch ihre Source über dem Substrat liegt.
:::

:::frage
„Was geschieht, wenn der Bulk über der Source liegt?“
Dann wird die Verarmungszone schmaler, und die Schwelle sinkt: beim Beispiel-NMOS auf 0,431 V bei $U_{BS}$ = 0,2 V und auf 0,351 V bei 0,4 V. Diese Vorspannung in Durchlassrichtung nutzt man gezielt, um Transistoren schneller zu machen, oder in umgekehrter Richtung, um Leckströme im Ruhezustand zu senken. Weit kann man nicht gehen, denn der Übergang zwischen Bulk und Source ist eine Diode: Ab einigen Zehntel Volt in Durchlassrichtung fließt ein Strom aus dem Bulk in die Source, der mit jeden 60 mV um eine Zehnerpotenz wächst.
:::

### Der Bulk als zweites Gate

*Wie stark wirkt eine Änderung der Bulkspannung im Vergleich zu einer Änderung der Gatespannung?*

Für den Strom zählt die Übersteuerung $U_{GS} - U_{th}$. Hebt man den Bulk etwas an, sinkt die Schwelle, und die Übersteuerung wächst, als hätte man das Gate angehoben, nur schwächer. Der Bulk wirkt wie ein zweites Gate von unten, das über die Verarmungszone an den Kanal koppelt; das obere Gate koppelt über das Oxid. Wie stark der Bulk im Vergleich wirkt, ist das Verhältnis der beiden Kapazitäten:

:::formel Formel
$$\eta = -\frac{\partial U_{th}}{\partial U_{BS}} = \frac{\gamma}{2\sqrt{2\Phi_F - U_{BS}}} = \frac{C'_\mathrm{dep}}{C'_\mathrm{ox}}$$
:::

**So liest man das:** Ändert sich $U_{BS}$ um ein Millivolt, ändert sich die Übersteuerung um η Millivolt, in derselben Richtung. Beim Beispiel-NMOS ist η = 0,327 bei $U_{BS}$ = 0 und 0,227 bei −1 V: Der Bulk wirkt mit einem Drittel bis einem Viertel der Stärke des Gates, und je weiter die Zone schon ist, desto schwächer. $C'_\mathrm{dep}$ ist die Kapazität der Verarmungszone pro Fläche; derselbe Quotient bestimmt den Steigungsfaktor $m$ des Stroms unterhalb der Schwelle ([Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien-ausfuehrlich.html)).

Idee der Herleitung: Man leitet die Schwelle nach $U_{BS}$ ab und vergleicht mit der Kapazität der Verarmungszone.

:::herleitung
**Ausgangspunkt:** die Schwellenspannung mit Substrateffekt aus dem Abschnitt *Der Substrateffekt* und die Kapazität der Verarmungszone pro Fläche aus [Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html):

$$C'_\mathrm{dep} = \sqrt{\frac{e\,\varepsilon_\mathrm{Si}\,N_A}{2\,\psi_s}}$$

**Annahmen:** dieselben wie für die Schwellenspannung mit Substrateffekt.

**Schritt 1**: Ableitung nach $U_{BS}$; die innere Ableitung von $2\Phi_F - U_{BS}$ ist −1:

$$\frac{\partial U_{th}}{\partial U_{BS}} = -\frac{\gamma}{2\sqrt{2\Phi_F - U_{BS}}}$$

**Schritt 2** (entscheidender Schritt): Mit $\gamma$ ausgeschrieben und $\psi_s = 2\Phi_F - U_{BS}$ ist der Betrag

$$\frac{\sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A}}{2\,C'_\mathrm{ox}\sqrt{\psi_s}} = \frac{1}{C'_\mathrm{ox}}\sqrt{\frac{e\,\varepsilon_\mathrm{Si}\,N_A}{2\,\psi_s}} = \frac{C'_\mathrm{dep}}{C'_\mathrm{ox}}$$

**Ergebnis:**

$$\eta = -\frac{\partial U_{th}}{\partial U_{BS}} = \frac{\gamma}{2\sqrt{2\Phi_F - U_{BS}}} = \frac{C'_\mathrm{dep}}{C'_\mathrm{ox}}$$

**Woher die Faktoren kommen:** Der Faktor 1/2 stammt aus der Ableitung der Wurzel; als Kapazitätsverhältnis beschreibt η einen Spannungsteiler aus Oxid und Verarmungszone.

**Proben:** Bei $U_{BS}$ = 0: 0,629/(2 · 0,961) = 0,327; $C'_\mathrm{dep}$ ist dort 2,26 fF/µm², geteilt durch 6,906 fF/µm² ebenfalls 0,327.

**Grenzen:** η gilt für kleine Änderungen um einen Arbeitspunkt; für große rechnet man mit der Formel der Schwelle selbst.
:::

## Der Substrateffekt in Schaltungen

*Wo tritt der Substrateffekt auf, und wie lässt er sich vermeiden?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/03-sourcefolger · Vorlage: schaltung-kennlinie
**Abbildung 6:** (a) NMOS-Sourcefolger: T2 mit Drain an $U_B$ = 2,5 V, Gate am Eingang, Source am Ausgang, Bulk am Substrat auf Masse; darunter eine Stromquelle mit 0,25 mA, etwa ein NMOS T1 mit fester Gatespannung. (b) PMOS-Sourcefolger: T3 mit Drain an Masse, Gate am Eingang, Source am Ausgang, Bulk wahlweise an der eigenen Source oder an $U_B$; darüber eine Stromquelle mit 0,25 mA, etwa ein PMOS T4 mit fester Gatespannung. (c) Ausgangs- über Eingangsspannung: NMOS ohne Substrateffekt die Gerade $U_\mathrm{ein}$ − 1 V (0,5 V, 1,0 V und 1,5 V bei 1,5 V, 2 V und 2,5 V Eingangsspannung), mit Substrateffekt 0,385 V, 0,783 V und 1,190 V; PMOS in eigener Wanne $U_\mathrm{ein}$ + 1 V, in der gemeinsamen Wanne an 2,5 V 1,305 V und 1,714 V bei 0 V und 0,5 V. Der Substrateffekt lässt den Ausgang nur mit etwa 0,8 statt 1 folgen; eine eigene Wanne beseitigt ihn beim PMOS.
:::

In einer integrierten Schaltung liegen alle NMOS-Transistoren im selben p-Substrat an Masse. Jeder NMOS, dessen Source nicht auf Masse liegt, hat deshalb eine negative Bulk-Source-Spannung und eine höhere Schwelle: der obere von zwei Transistoren in Reihe, wie in einem NAND-Gatter oder einer Kaskode, und besonders der __Sourcefolger__ (Abbildung 6a). In ihm liegt der Eingang am Gate, der Ausgang an der Source, und eine Stromquelle hält den Strom fest. Der feste Strom hält die Übersteuerung $U_{GS} - U_{th}$ fest, beim Beispiel 0,5 V; ohne Substrateffekt ist damit auch $U_{GS}$ fest, 1 V, und der Ausgang folgt dem Eingang mit 1 V Abstand. Mit Substrateffekt steigt aber die Schwelle, je höher der Ausgang liegt, und der Abstand wächst mit: Der Ausgang folgt nur noch mit etwa 0,8 (Abbildung 6c).

Bei den meisten Einzeltransistoren im eigenen Gehäuse tritt der Substrateffekt nicht auf: Der Bulk ist schon im Gehäuse mit der Source verbunden, $U_{BS}$ ist immer null. Der Preis ist die Diode zwischen Bulk und Drain, die nun zwischen Source und Drain liegt, die __Inversdiode__ ([Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html)): Der Transistor sperrt nur in einer Richtung.

:::grafik
Szene: st1/mos-feldeffekttransistoren/03-wannen-varianten · Vorlage: querschnitt-teilbilder
**Abbildung 7:** Vier Querschnitte, schematisch. (a) Die NMOS T1 und T2 im gemeinsamen p-Substrat an Masse; die Source von T2 liegt am Ausgang: Substrateffekt bei T2. (b) Die PMOS T3 und T4 in einer gemeinsamen n-Wanne an $U_B$; die Source von T3 liegt am Ausgang: Substrateffekt bei T3. (c) T3 in einer eigenen n-Wanne, deren Kontakt an seiner Source liegt: kein Substrateffekt, dafür mehr Fläche und eine zusätzliche Kapazität zwischen Wanne und Substrat am Ausgang. (d) Ein NMOS in einer p-Wanne, die eine tiefe n-Wanne vom Substrat trennt, die p-Wanne an der Source. Den Substrateffekt vermeidet nur ein eigenes, mit der Source verbundenes Gebiet; beim PMOS ist das eine eigene Wanne, beim NMOS braucht es eine tiefe n-Wanne.
:::

Beim PMOS lässt sich der Substrateffekt vermeiden, weil er in einer Wanne sitzt. Üblich ist zwar, mehrere PMOS in eine gemeinsame Wanne an der Versorgung zu setzen (Abbildung 7b); dann hat jeder PMOS, dessen Source unter $U_B$ liegt, einen Substrateffekt. Gibt man einem PMOS aber eine eigene Wanne und verbindet ihren Kontakt mit seiner Source (Abbildung 7c), ist $U_{BS}$ immer null. Das kostet Fläche, weil jede Wanne Abstand zu den Nachbarn braucht, und hängt die Kapazität zwischen Wanne und Substrat an den Ausgang. Man tut es deshalb nur, wo es darauf ankommt, etwa bei Folgern und Eingangsstufen, die genau arbeiten sollen.

:::frage
„Warum verbindet man einen Ausgang über einen PMOS mit der Versorgung und nicht über einen NMOS, der doch mehr Strom liefert?“
Ein NMOS, dessen Drain und Gate an 2,5 V liegen, ist ein Sourcefolger: Er hebt den Ausgang nur, solange zwischen Gate und Source mehr als die Schwelle liegt. Ohne Substrateffekt endete das bei 2,5 V − 0,5 V = 2,0 V; weil die Source dabei immer höher über dem Substrat liegt, steigt die Schwelle aber auf 0,896 V, und der Ausgang erreicht nur 1,6 V. Ein PMOS mit der Source an 2,5 V und dem Gate auf 0 V bleibt dagegen leitend, bis keine Spannung mehr über ihm liegt, und zieht den Ausgang auf volle 2,5 V. Deshalb verbindet in CMOS-Gattern der PMOS mit der Versorgung und der NMOS mit Masse.
:::

::::beispiel Sourcefolger mit und ohne Substrateffekt
**Gegeben:** Beispiel-NMOS ($U_{th0}$ = 0,5 V, $K_n$ = 2 mA/V², $\gamma$ = 0,629 √V, $2\Phi_F$ = 0,923 V) als Folger mit 0,25 mA, Bulk an Masse; Beispiel-PMOS ($\gamma_p$ = 0,615 √V, $2\Phi_{F,p}$ = 0,921 V) als Folger mit 0,25 mA, Bulk an der Source oder an $U_B$ = 2,5 V; Kanallängenmodulation vernachlässigt.

**Gesucht:** (a) die Ausgangsspannung des NMOS-Folgers bei 1,5 V und 2 V Eingangsspannung und seine Steigung; (b) die des PMOS-Folgers bei 0,5 V Eingangsspannung in eigener und in gemeinsamer Wanne.

**Rechnung:** (a) Bei 0,25 mA ist die Übersteuerung nach dem Quadratgesetz $\sqrt{2I_D/K_n}$ = 0,5 V. Der Ausgang liegt um $U_{GS}$ = $U_{th}$ + 0,5 V unter dem Eingang, und die Schwelle hängt über $U_{BS} = -U_\mathrm{aus}$ vom Ausgang ab:

$$U_\mathrm{ein} = U_\mathrm{aus} + U_{th0} + \gamma\,\Big(\sqrt{2\Phi_F + U_\mathrm{aus}} - \sqrt{2\Phi_F}\Big) + 0{,}5\ \mathrm V$$

Ohne Substrateffekt wäre $U_\mathrm{aus}$ = 1,0 V bei 2 V Eingangsspannung. Mit ihm ergibt die Lösung, etwa durch Probieren, $U_\mathrm{aus}$ = 0,783 V; dort ist $U_{th}$ = 0,717 V, und die Summe stimmt:

$$0{,}783\ \mathrm V + 0{,}717\ \mathrm V + 0{,}5\ \mathrm V = 2{,}0\ \mathrm V$$

Bei 1,5 V Eingangsspannung ergibt sich ebenso 0,385 V. Die Steigung zwischen beiden Punkten ist

$$\frac{0{,}783\ \mathrm V - 0{,}385\ \mathrm V}{0{,}5\ \mathrm V} = 0{,}80$$

Für kleine Änderungen folgt sie aus η:

:::herleitung
**Ausgangspunkt:** die Gleichung des Folgers oben und η aus dem Abschnitt *Der Bulk als zweites Gate*.

**Annahmen:** fester Strom, also feste Übersteuerung; Kanallängenmodulation vernachlässigt.

**Schritt 1**: Ableitung der Eingangsspannung nach der Ausgangsspannung; die Schwelle ändert sich mit $U_\mathrm{aus}$ um η, weil $U_{BS} = -U_\mathrm{aus}$:

$$\frac{dU_\mathrm{ein}}{dU_\mathrm{aus}} = 1 + \eta$$

**Ergebnis:**

$$\frac{dU_\mathrm{aus}}{dU_\mathrm{ein}} = \frac{1}{1 + \eta}$$

**Proben:** Bei $U_\mathrm{aus}$ = 0,783 V ist η = 0,629/(2 · 1,306) = 0,241, die Steigung 0,806; ohne Substrateffekt ist η = 0 und die Steigung 1.
:::

(b) In der eigenen Wanne hat der PMOS keinen Substrateffekt; der Ausgang liegt um $|U_{GS}|$ = 1 V über dem Eingang, also bei 1,5 V. In der gemeinsamen Wanne an 2,5 V ist $U_{BS}$ = 2,5 V − $U_\mathrm{aus}$, und die Lösung der entsprechenden Gleichung ist 1,714 V mit $|U_{th,p}|$ = 0,714 V:

$$U_\mathrm{aus} = 0{,}5\ \mathrm V + 0{,}714\ \mathrm V + 0{,}5\ \mathrm V = 1{,}714\ \mathrm V$$

**Ergebnis:** **(a) 0,385 V und 0,783 V statt 0,5 V und 1,0 V, Steigung 0,80; (b) 1,5 V in eigener Wanne, 1,714 V in gemeinsamer Wanne.**

**Einordnung:** Ein Sourcefolger soll eine Spannung möglichst unverfälscht weitergeben, etwa an eine niederohmige Last. Mit dem Substrateffekt gibt er nur 80 % einer Änderung weiter, und sein Ausgang liegt bis zu 0,3 V tiefer als ohne ihn. Die eigene Wanne des PMOS stellt die Steigung 1 wieder her; beim NMOS bleibt nur die tiefe n-Wanne.
::::

:::frage
„Lässt sich auch ein NMOS ohne Substrateffekt bauen?“
In einem einfachen Prozess mit n-Wannen nicht, denn alle NMOS liegen im selben Substrat. Prozesse mit einer zusätzlichen tiefen n-Wanne (englisch deep n-well; man spricht dann von einem Triple-Well-Prozess) können eine p-Wanne vom Substrat trennen (Abbildung 7d): Der NMOS darin bekommt einen eigenen Bulk, den man mit seiner Source verbinden kann. Das kostet eine weitere Maske und Fläche; man nutzt es vor allem in Analog- und Hochfrequenzschaltungen, auch um empfindliche Teile vom Störstrom im Substrat abzuschirmen.
:::

## Latch-Up: der parasitäre Thyristor

*Wie kann eine CMOS-Schaltung ihre eigene Versorgung kurzschließen?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/03-latchup-struktur · Vorlage: querschnitt-ersatzschaltbild
**Abbildung 8:** (a) Querschnitt mit Substratkontakt und NMOS-Source an Masse, n-Wanne mit Wannenkontakt und PMOS-Source an $U_B$; eingezeichnet der laterale npn-Transistor (Emitter: NMOS-Source, Basis: Substrat, Kollektor: Wanne), der vertikale pnp-Transistor (Emitter: PMOS-Source, Basis: Wanne, Kollektor: Substrat), der Substratwiderstand $R_\mathrm{sub}$ von der Basis des npn zum Substratkontakt und der Wannenwiderstand $R_\mathrm{well}$ von der Basis des pnp zum Wannenkontakt. (b) Ersatzschaltbild: beide Transistoren über Kreuz verbunden zwischen $U_B$ und Masse, der Kollektor des einen an der Basis des anderen; ein umlaufender Pfeil zeigt die Mitkopplung mit der Schleifenverstärkung $B_\mathrm{npn}B_\mathrm{pnp}$. (c) Die Schichtfolge p⁺–n–p–n⁺ als Thyristor. Die Gebiete einer CMOS-Schaltung bilden zwei parasitäre Bipolartransistoren, von denen jeder den anderen ansteuert: einen Thyristor zwischen Versorgung und Masse.
:::

Die Gebiete eines CMOS-Chips bilden nicht nur MOSFETs. Folgt man in Abbildung 8a dem Weg von der PMOS-Source an der Versorgung durch die Wanne und das Substrat zur NMOS-Source an Masse, durchquert man p⁺, n, p und n⁺: die Schichtfolge eines __Thyristors__, eines Bauelements aus vier abwechselnd dotierten Schichten, das nach dem Zünden von selbst leitend bleibt. In den ersten CMOS-Schaltungen zerstörte dieser ungewollte Thyristor manche Chips schon beim Einschalten. Weil der Kurzschluss danach bestehen bleibt, einrastet, heißt der Vorgang __Latch-Up__.

Vier Schichten ergeben zwei Bipolartransistoren, weil die beiden mittleren Schichten jeweils zu beiden gehören (Abbildung 8b und 8c): Die n-Wanne ist Basis des pnp und zugleich Kollektor des npn, das Substrat Basis des npn und zugleich Kollektor des pnp. Was der eine Transistor als Kollektorstrom abgibt, erhält der andere als Basisstrom.

**Die Akteure:**

- __npn__: der laterale parasitäre Transistor aus NMOS-Source (Emitter), Substrat (Basis) und Wanne (Kollektor).
- __pnp__: der vertikale parasitäre Transistor aus PMOS-Source (Emitter), Wanne (Basis) und Substrat (Kollektor).
- __$R_\mathrm{sub}$__, __$R_\mathrm{well}$__: Widerstand des Substrats vom Gebiet unter dem NMOS zum Substratkontakt und Widerstand der Wanne vom Gebiet unter dem PMOS zum Wannenkontakt; im Rechenbeispiel angenommen 1 kΩ und 2 kΩ.
- __$B_\mathrm{npn}$__, __$B_\mathrm{pnp}$__: Stromverstärkungen der parasitären Transistoren, Kollektorstrom durch Basisstrom wie im Abschnitt *Von Grund auf*; im Rechenbeispiel angenommen 5 und 50. Dieses $B$ hat nichts mit dem Index $B$ für Bulk in $U_{BS}$ zu tun.

**Das Zusammenspiel:**

**Schritt 1**: Im normalen Betrieb liegt das Substrat über seinen Kontakt an Masse, die Wanne an $U_B$. Alle Übergänge des Pfads sind gesperrt oder ohne Spannung, beide Transistoren sind aus, und es fließt nur ein Leckstrom.

**Schritt 2**: Fließt aus irgendeinem Grund ein Störstrom ins Substrat, muss er durch $R_\mathrm{sub}$ zum Substratkontakt und hebt das Substrat unter dem NMOS an. Bei 0,6 mA durch 1 kΩ sind es 0,6 V: Der Übergang zwischen Substrat und NMOS-Source, die Basis-Emitter-Strecke des npn, beginnt zu leiten.

**Schritt 3**: Der npn leitet. Elektronen aus der NMOS-Source durchqueren das Substrat und erreichen die Wanne, seinen Kollektor. Dieser Kollektorstrom fließt von $U_B$ durch $R_\mathrm{well}$ in die Wanne und senkt ihr Potential unter dem PMOS ab.

**Schritt 4**: Erreicht der Spannungsabfall an $R_\mathrm{well}$ 0,6 V, bei 2 kΩ schon mit 0,3 mA, leitet auch die Emitter-Basis-Strecke des pnp, der Übergang zwischen PMOS-Source und Wanne. Löcher aus der PMOS-Source durchqueren die Wanne und erreichen das Substrat, seinen Kollektor.

**Schritt 5** (entscheidender Schritt): Der Kollektorstrom des pnp fließt ins Substrat und durch $R_\mathrm{sub}$, denselben Weg wie der Störstrom: Er verstärkt Schritt 2. Jeder Transistor liefert den Basisstrom des anderen, eine __Mitkopplung__. Kommt ein Strom nach einem Umlauf größer zurück, als er losgelaufen ist, wachsen beide Ströme von selbst.

**Schritt 6**: Begrenzt wird das Wachstum erst von den Widerständen von Wanne und Substrat und von der äußeren Schaltung. Zwischen $U_B$ und Masse liegt nun ein leitender Pfad, über dem im einfachen Modell nur rund 0,8 V liegen, in realen Strukturen wegen der Bahnwiderstände etwas mehr: ein Kurzschluss der Versorgung, und er bleibt bestehen, auch wenn der Störstrom längst vorbei ist (Abbildung 9). Beenden lässt er sich nur, indem man die Versorgung abschaltet oder ihren Strom unter den __Haltestrom__ senkt, den kleinsten Strom, mit dem sich der Pfad noch selbst erhält. Liegt die Versorgung unter der Spannung, die der gezündete Pfad mindestens braucht, kann er sich gar nicht halten; Schaltungen mit sehr niedriger Versorgungsspannung sind deshalb weniger gefährdet.

:::formel Formel
$$B_\mathrm{npn}\,B_\mathrm{pnp} > 1$$
:::

**So liest man das:** Die Bedingung vergleicht die Verstärkung eines Umlaufs mit 1. Liegt das Produkt darunter, klingt jeder Störstrom ab; liegt es darüber, kann sich der Pfad selbst halten. Mit 5 und 50 ist es 250, weit über 1. Die Bedingung ist notwendig, aber nicht hinreichend: Die Widerstände leiten Strom an den Basen vorbei, und erst wenn beide Übergänge die Einsatzspannung erreichen, kann die Mitkopplung greifen. Deshalb braucht es zum Zünden einen Störstrom einer Mindestgröße, im Beispiel 0,66 mA ins Substrat: 0,6 mA, bis der npn leitet, und 0,06 mA mehr, bis sein Kollektorstrom an $R_\mathrm{well}$ 0,6 V erzeugt.

**Kurz gesagt:** Ein Latch-Up hält sich, wenn ein Strom nach einem Umlauf durch beide Transistoren größer zurückkommt, als er losgelaufen ist.

Idee der Herleitung: Man verfolgt einen kleinen zusätzlichen Basisstrom einmal um die Schleife.

:::herleitung
**Ausgangspunkt:** der Zusammenhang zwischen Kollektor- und Basisstrom im aktiven Bereich, $I_C = B\,I_B$, aus [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise-ausfuehrlich.html), und die Verschaltung aus dem Ersatzschaltbild: Der Kollektor des npn liegt an der Basis des pnp, der Kollektor des pnp an der Basis des npn.

**Annahmen:**
(i) Beide parasitären Transistoren sind im aktiven Bereich: Basis-Emitter-Strecke leitend, Basis-Kollektor-Strecke gesperrt.
(ii) Die Stromverstärkungen sind konstant.
(iii) Die Ströme durch $R_\mathrm{sub}$ und $R_\mathrm{well}$ ändern sich nicht, solange die Basis-Emitter-Spannungen fest bei der Einsatzspannung liegen; ein zusätzlicher Strom fließt deshalb ganz in die Basen.

**Schritt 1**: Ein zusätzlicher Basisstrom $\Delta I$ in den npn erzeugt den Kollektorstrom $B_\mathrm{npn}\Delta I$. Er wird aus der Wanne gezogen und ist damit Basisstrom des pnp.

**Schritt 2**: Der pnp verstärkt ihn um $B_\mathrm{pnp}$; sein Kollektorstrom fließt ins Substrat und kommt als Basisstrom beim npn an:

$$\Delta I_\mathrm{zurück} = B_\mathrm{npn}\,B_\mathrm{pnp}\,\Delta I$$

**Schritt 3** (entscheidender Schritt): Ist der zurückkommende Strom größer als $\Delta I$, wächst er bei jedem Umlauf weiter; ist er kleiner, klingt er ab.

**Ergebnis:**

$$B_\mathrm{npn}\,B_\mathrm{pnp} > 1$$

**Woher die Faktoren kommen:** Jeder Transistor trägt seine Stromverstärkung zur Schleife bei; das Produkt ist die Schleifenverstärkung.

**Proben:** Mit 5 und 50 ist sie 250. Senkt man die Verstärkung des lateralen npn durch größeren Abstand auf 0,01, ist sie 0,5, und kein Störstrom kann den Pfad halten.

**Grenzen:** Die Stromverstärkungen parasitärer Transistoren hängen stark vom Strom ab und sind bei kleinen Strömen kleiner; die Widerstände sind über den Chip verteilt. Wann eine reale Struktur zündet, zeigt deshalb nur die Messung.
:::

:::grafik
Szene: st1/mos-feldeffekttransistoren/03-latchup-kennlinie · Vorlage: kennlinie-ruecksprung
**Abbildung 9:** Schematische Kennlinie des Pfads zwischen $U_B$ und Masse: Strom über Spannung von 0 bis 3 V. Gesperrt fließt nur ein Leckstrom; beim Zünden springt der Arbeitspunkt auf den leitenden Ast, der im einfachen Modell ab rund 0,8 V steil ansteigt; der Haltepunkt liegt bei rund 1 mA. Die Arbeitsgerade einer 2,5-V-Versorgung mit 1 Ω Innen- und Leitungswiderstand schneidet den leitenden Ast bei 1,7 A. Stromachse mit Bruch zwischen mA und A. Nach dem Zünden hält sich der Thyristor mit rund 1 V selbst; nur Abschalten oder ein Strom unter dem Haltestrom beendet den Zustand.
:::

::::beispiel Zündstrom, Haltestrom und Kurzschlussstrom eines parasitären Thyristors
**Gegeben:** angenommene Werte: $R_\mathrm{sub}$ = 1 kΩ, $R_\mathrm{well}$ = 2 kΩ, $B_\mathrm{npn}$ = 5, $B_\mathrm{pnp}$ = 50; Einsatzspannung der Basis-Emitter-Übergänge 0,6 V, Sättigungsspannung des npn 0,2 V; Versorgung 2,5 V mit 1 Ω Innen- und Leitungswiderstand.

**Gesucht:** (a) die Störströme, die einen bzw. beide Übergänge leitend machen; (b) der Haltestrom; (c) der Strom und die Leistung nach dem Zünden.

**Rechnung:** (a) Durch das Substrat bzw. die Wanne:

$$\frac{0{,}6\ \mathrm V}{1\ \mathrm{k\Omega}} = 0{,}6\ \mathrm{mA}, \qquad \frac{0{,}6\ \mathrm V}{2\ \mathrm{k\Omega}} = 0{,}3\ \mathrm{mA}\,$$

Zünden kann der Pfad erst, wenn auch der zweite Übergang leitet. Fließt der Störstrom ins Substrat, muss der npn 0,3 mA Kollektorstrom durch $R_\mathrm{well}$ liefern und braucht dafür 0,06 mA Basisstrom zusätzlich; wird er aus der Wanne gezogen, muss der pnp 0,6 mA liefern und braucht 0,012 mA:

$$0{,}6\ \mathrm{mA} + \frac{0{,}3\ \mathrm{mA}}{5} = 0{,}66\ \mathrm{mA}, \qquad 0{,}3\ \mathrm{mA} + \frac{0{,}6\ \mathrm{mA}}{50} = 0{,}312\ \mathrm{mA}\,$$

(b) Am Haltepunkt liegen beide Übergänge gerade auf 0,6 V; die Ströme folgen aus der Knotenregel an Substrat und Wanne:

:::herleitung
**Ausgangspunkt:** Knotenregel am Substrat- und am Wannenknoten, $I_C = B\,I_B$ für beide Transistoren.

**Annahmen:** beide Basis-Emitter-Spannungen dem Betrag nach gleich der Einsatzspannung $U_0$ = 0,6 V; konstante Stromverstärkungen.

**Schritt 1**: Am Substrat teilt sich der Kollektorstrom des pnp in den Strom durch $R_\mathrm{sub}$ und den Basisstrom des npn:

$$I_{C,\mathrm{pnp}} = \frac{U_0}{R_\mathrm{sub}} + \frac{I_{C,\mathrm{npn}}}{B_\mathrm{npn}}$$

**Schritt 2**: An der Wanne setzt sich der Kollektorstrom des npn aus dem Strom durch $R_\mathrm{well}$ und dem Basisstrom des pnp zusammen:

$$I_{C,\mathrm{npn}} = \frac{U_0}{R_\mathrm{well}} + \frac{I_{C,\mathrm{pnp}}}{B_\mathrm{pnp}}$$

**Schritt 3** (entscheidender Schritt): Schritt 1 in Schritt 2 eingesetzt und aufgelöst:

$$I_{C,\mathrm{npn}} = \frac{U_0/R_\mathrm{well} + U_0/\big(B_\mathrm{pnp}R_\mathrm{sub}\big)}{1 - 1/\big(B_\mathrm{npn}B_\mathrm{pnp}\big)}$$

**Ergebnis:** Ein positiver Strom ergibt sich nur für $B_\mathrm{npn}B_\mathrm{pnp} > 1$; mit den Zahlen 0,313 mA, und aus Schritt 1 $I_{C,\mathrm{pnp}}$ = 0,663 mA.

**Proben:** Für eine Schleifenverstärkung gegen 1 geht der Nenner gegen null, und der Haltestrom wächst über alle Grenzen: Gerade noch mitgekoppelte Strukturen brauchen sehr viel Strom, um sich zu halten.
:::

Aus der Versorgung fließen der Emitterstrom des pnp und der Strom durch $R_\mathrm{well}$:

$$I_H = 0{,}663\ \mathrm{mA}\cdot\Big(1 + \frac{1}{50}\Big) + 0{,}3\ \mathrm{mA} = 0{,}98\ \mathrm{mA}$$

(c) Gezündet liegt über dem Pfad die Emitter-Basis-Spannung des pnp plus die Sättigungsspannung des npn, rund 0,8 V; den Rest der Versorgung nimmt der Widerstand auf:

$$I = \frac{2{,}5\ \mathrm V - 0{,}8\ \mathrm V}{1\ \Omega} = 1{,}7\ \mathrm A, \qquad P = 1{,}7\ \mathrm A\cdot0{,}8\ \mathrm V = 1{,}36\ \mathrm W\,$$

**Ergebnis:** **(a) Ein Übergang leitet ab 0,6 mA ins Substrat oder 0,3 mA aus der Wanne, zünden kann der Pfad ab 0,66 mA bzw. 0,312 mA; (b) Haltestrom rund 1 mA; (c) 1,7 A und 1,4 W.**

**Einordnung:** Ein Störstrom unter einem Milliampere genügt, und danach fließen über tausendmal so viel, solange die Versorgung sie liefern kann. 1,4 W auf einer Fläche von wenigen Quadratmikrometern schmelzen Leiterbahnen und Übergänge; mit 10 Ω Innenwiderstand wären es noch 0,17 A. Weil eine Versorgung meist weit mehr als den Haltestrom von rund 1 mA liefern kann, erlischt der Pfad praktisch nur beim Abschalten.
::::

:::fehlvorstellung
„Ein Latch-Up ist eine kurze Störung; ist sie vorbei, arbeitet die Schaltung wieder normal.“ Das liegt nahe, weil die meisten Störungen mit ihrer Ursache verschwinden. Beim Latch-Up hält die Mitkopplung den Pfad aber selbst offen: Im Beispiel genügt ein Strom von rund 1 mA, um ihn zu erhalten, und die Versorgung liefert weit mehr (Abschnitt *Latch-Up: der parasitäre Thyristor*). Erst Abschalten oder ein Versorgungsstrom unter dem Haltestrom beendet den Zustand, wenn er die Schaltung bis dahin nicht zerstört hat.
:::

Die Auslöser sind Ströme, die in Substrat oder Wanne gelangen, wo sie nicht hingehören. Beim Einschalten muss die Kapazität zwischen den Wannen und dem Substrat geladen werden: Ein Chip mit 10 mm² Wannenfläche braucht bei einem Substrat mit 10¹⁵ cm⁻³ und Wannen mit 10¹⁷ cm⁻³ dafür 1,7 nC, die bei einem Anstieg der Versorgung in 1 µs als 1,7 mA durch Substrat und Wannen fließen, bei 10 ns als 0,17 A. Liegt ein Ein- oder Ausgang über der Versorgung oder unter Masse, etwa durch Überschwingen auf einer Leitung, leiten die Dioden von Drain- und Source-Gebieten und speisen Ladungsträger direkt in Wanne oder Substrat. Elektrostatische Entladungen und ionisierende Teilchen, die längs ihrer Bahn Elektron-Loch-Paare erzeugen, wirken ebenso.

:::frage
„Warum zündet der Thyristor nicht ständig, wenn er doch in jeder CMOS-Schaltung steckt?“
Im Ruhezustand sind alle Übergänge des Pfads gesperrt oder ohne Spannung, und durch Substrat und Wannen fließen nur Leckströme von Picoampere bis Nanoampere. Ein Nanoampere erzeugt an 1 kΩ ein Mikrovolt, fast sechs Zehnerpotenzen weniger als die 0,6 V, die einen Übergang leitend machen. Beim Schalten kommen kurze Ströme hinzu, mit denen die Kapazitäten der gesperrten Übergänge umgeladen werden; bei genügend vielen Kontakten bleiben sie weit unter dem Zündstrom. Erst ein Störstrom von der Größenordnung eines Milliamperes an der richtigen Stelle zündet den Pfad.
:::

:::frage
„Warum steigt die Gefahr eines Latch-Up mit der Temperatur?“
Mit der Temperatur steigen die Widerstände von Substrat und Wanne, weil die Beweglichkeit der Ladungsträger sinkt; derselbe Störstrom erzeugt dann eine größere Spannung. Zugleich sinkt die Einsatzspannung der Übergänge, wie bei der Diode um rund 2 mV pro Kelvin ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie-ausfuehrlich.html)), und die Stromverstärkungen wachsen. Alle drei Effekte senken den Störstrom, der zum Zünden genügt; deshalb prüft man die Festigkeit gegen Latch-Up auch bei der höchsten Betriebstemperatur.
:::

## Gegenmaßnahmen gegen Latch-Up

*Wie verhindert man, dass der parasitäre Thyristor zündet?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/03-latchup-gegenmassnahmen · Vorlage: querschnitt-massnahmen
**Abbildung 10:** Querschnitt wie in Abbildung 8, ergänzt um Gegenmaßnahmen: viele Substrat- und Wannenkontakte dicht neben den Transistoren; ein p⁺-Ring an Masse um den NMOS und ein n⁺-Ring an $U_B$ um den PMOS als Schutzringe; ein größerer Abstand zwischen NMOS und Wanne; eine dünne, schwach dotierte Epitaxieschicht auf einem hoch dotierten p⁺-Substrat. Beschriftet ist die Wirkung: kleinere Substrat- und Wannenwiderstände, kleinere Stromverstärkungen, abgefangene Ladungsträger. Kleines Einsatzbild: ein Transistor auf einer Oxidschicht (SOI) ohne gemeinsames Substrat. Gegen Latch-Up senkt man die Widerstände, damit kein Störstrom 0,6 V erzeugt, und die Stromverstärkungen, damit die Schleife unter 1 bleibt.
:::

Die Zündbedingung und der Zündstrom zeigen zwei Ansatzpunkte. Der erste sind kleine Widerstände: Liegen viele Substrat- und Wannenkontakte dicht neben den Transistoren, erzeugt ein Störstrom nur eine kleine Spannung, und es braucht einen viel größeren Strom, um 0,6 V zu erreichen. Am wirksamsten ist ein Wafer mit einer dünnen, schwach dotierten __Epitaxieschicht__, einer auf das Substrat aufgewachsenen Kristallschicht, in der die Transistoren liegen, auf einem hoch dotierten p⁺-Substrat, das Störströme mit sehr kleinem Widerstand zur Masse leitet. Soll ein Störstrom von 100 mA nicht zünden, darf der Weg zum Substratkontakt höchstens 6 Ω haben.

Der zweite Ansatzpunkt sind kleine Stromverstärkungen. Ein größerer Abstand zwischen NMOS und Wanne verbreitert die Basis des lateralen npn, und weniger Elektronen erreichen die Wanne. __Schutzringe__, stark dotierte Ringe um die Transistoren, die an Masse oder Versorgung liegen, fangen injizierte Ladungsträger ab, bevor sie den anderen Transistor erreichen. Sinkt das Produkt der Stromverstärkungen unter 1, kann sich der Pfad nicht mehr halten, gleich wie groß der Störstrom ist. Besonders sorgfältig schützt man die Transistoren an den Ein- und Ausgängen, weil dort Störströme von außen eingespeist werden. Grundsätzlich beseitigt ist die Gefahr nur, wo es kein gemeinsames Substrat gibt: bei Transistoren auf einer isolierenden Oxidschicht (silicon on insulator, SOI). Gräben, die tiefer als die Wannen reichen, unterbrechen den kurzen Weg zwischen NMOS und Wanne und senken die Stromverstärkung des npn stark; das Substrat darunter bleibt aber gemeinsam.

Welche Abstände und Kontaktdichten nötig sind, schreiben die Entwurfsregeln jedes Prozesses vor. Ob ein fertiger Chip sicher ist, zeigt eine Prüfung nach der Norm JESD78: Man speist in jeden Ein- und Ausgang Strompulse von typisch 100 mA und legt an die Versorgungsanschlüsse das 1,5-Fache der höchsten Betriebsspannung, jeweils für einige Millisekunden, und prüft, ob danach ein erhöhter Versorgungsstrom bestehen bleibt.

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| PMOS mit negativen Spannungen und negativem Strom | Gebiete und Ladungsträger sind gespiegelt; dem Betrag nach gelten die Gleichungen des NMOS |
| Substrat an der niedrigsten, Wanne an der höchsten Spannung | nur so bleiben alle trennenden pn-Übergänge gesperrt |
| Substrateffekt | der Bulk wirkt als zweites Gate: Sperrspannung verbreitert die Verarmungszone, das Gate muss mehr Ladung tragen |
| Wurzel in der Formel | die Verarmungszone wächst mit der Wurzel ihrer Spannung |
| Sourcefolger folgt mit 0,8 | seine Schwelle steigt mit der Spannung am Ausgang |
| eigene Wanne, Bulk an Source im Gehäuse | ein eigenes, mit der Source verbundenes Gebiet hält die Bulk-Source-Spannung auf null |
| Latch-Up | werden die trennenden Übergänge leitend, bilden Wanne und Substrat einen Thyristor |
| Kontakte, Schutzringe, Epitaxie | sie halten die Übergänge gesperrt: kleine Widerstände, kleine Stromverstärkungen |

Ein MOSFET ist nur durch gesperrte pn-Übergänge von seiner Umgebung getrennt, und sein Bulk wirkt wie ein zweites Gate: Beim PMOS sind Gebiete und Vorzeichen vertauscht, eine Sperrspannung zwischen Bulk und Source vergrößert die Verarmungsladung und damit den Betrag der Schwelle, und werden die trennenden Übergänge leitend, bilden Wanne und Substrat einen Thyristor, der die Versorgung kurzschließt.

## Bedeutung und Ausblick

In CMOS-Schaltungen arbeiten beide Transistorarten zusammen: Der PMOS verbindet einen Knoten mit der Versorgung, wenn sein Gate tief liegt, der NMOS mit Masse, wenn sein Gate hoch liegt; daraus entstehen Inverter und alle Logikgatter. In analogen Schaltungen bestimmt der Substrateffekt, wie genau Sourcefolger, Kaskoden und Stromspiegel arbeiten. Gemessen wird $\gamma$ an Teststrukturen, indem man die Schwelle bei mehreren Bulk-Source-Spannungen bestimmt: Beim Beispiel-NMOS ergibt die Differenz der Schwellen bei −1 V und −2 V, 0,203 V, geteilt durch die Differenz der Wurzelterme, 0,323 √V, wieder 0,629 √V. Viele Datenblätter integrierter Schaltungen nennen außerdem ihre Festigkeit gegen Latch-Up.

Im Kleinsignalmodell erscheint die Wirkung des Bulk als zweite gesteuerte Quelle, deren Steilheit η-mal so groß ist wie die des Gates; der Artikel über das Kleinsignalmodell des MOSFET leitet sie her. Der nächste Artikel, Parasitäre Kapazitäten des MOSFET, behandelt die Kapazitäten zwischen den vier Anschlüssen, zu denen auch die gesperrten Übergänge gegen Substrat und Wanne gehören.

:::kern
- Der PMOS ist das Spiegelbild des NMOS: Löcherkanal in der n-Wanne, $U_{GS}$, $U_{DS}$, $I_D$ und $U_{th,p}$ negativ; dem Betrag nach gelten die NMOS-Gleichungen.
- Das Substrat liegt an der niedrigsten, die Wanne an der höchsten Spannung, damit alle pn-Übergänge sperren.
- Substrateffekt: $U_{th} = U_{th0} + \gamma\big(\sqrt{2\Phi_F - U_{BS}} - \sqrt{2\Phi_F}\big)$; eine Sperrspannung zwischen Bulk und Source hebt die Schwelle.
- Ursache: Die Oberfläche muss um die Sperrspannung höher angehoben werden, und die breitere Verarmungszone bindet mehr Gateladung.
- Vermeiden lässt sich der Substrateffekt nur mit einem eigenen, mit der Source verbundenen Gebiet: eigene Wanne beim PMOS, Bulk an Source beim Einzeltransistor.
- Latch-Up: p⁺–n-Wanne–p-Substrat–n⁺ bildet einen Thyristor aus pnp und npn; er zündet durch einen Störstrom, hält sich bei $B_\mathrm{npn}B_\mathrm{pnp} > 1$ selbst und endet erst, wenn die Versorgung abgeschaltet oder ihr Strom unter den Haltestrom gesenkt wird.
- Gegenmittel: kleine Substrat- und Wannenwiderstände (Kontakte, Epitaxie) und kleine Stromverstärkungen (Abstand, Schutzringe).
:::

:::quiz
F: Warum sind beim PMOS Gate-Source-Spannung, Drain-Source-Spannung und Drainstrom negativ?
A: Die Source ist beim PMOS das p⁺-Gebiet mit dem höheren Potential, weil die Löcher zum niedrigeren laufen. Das Gate muss unter der Source liegen, um Löcher anzuziehen, der Drain liegt ebenfalls tiefer, und der Strom fließt aus dem Drain heraus. Mit denselben Zählpfeilen wie beim NMOS sind deshalb alle drei Größen negativ.
F: Warum hebt eine negative Bulk-Source-Spannung die Schwelle eines NMOS?
A: Die Kanalelektronen liegen auf dem Potential der Source. Liegt diese über dem Bulk, muss die Oberfläche um die Sperrspannung höher angehoben werden, die Verarmungszone wird breiter und enthält mehr feste Ladung, und diese muss das Gate zusätzlich tragen: bei −1 V 1,85 fC/µm² mehr, also 0,268 V mehr Schwelle.
F: Warum hebt jedes weitere Volt Sperrspannung die Schwelle weniger als das vorige?
A: Die Verarmungsladung wächst nur mit der Wurzel der Spannung über der Zone. Beim Beispiel-NMOS hebt das erste Volt die Schwelle um 0,268 V, das zweite um 0,203 V.
F: Warum hält sich ein Latch-Up selbst, nachdem der Störstrom vorbei ist?
A: Die beiden parasitären Transistoren sind über Kreuz verbunden: Der Kollektorstrom des einen ist der Basisstrom des anderen. Ist das Produkt ihrer Stromverstärkungen größer als 1, kommt jeder Strom nach einem Umlauf verstärkt zurück, und der Pfad erhält sich selbst, solange die Versorgung mehr als den Haltestrom liefert.
F: Stimmt es, dass man beim PMOS die negativen Spannungen direkt in die NMOS-Gleichungen einsetzen kann?
A: Nein. Mit $U_{GS}$ = −1 V und der positiven NMOS-Schwelle ergäbe sich „gesperrt“ oder quadriert 2,25 mA. Man muss mit der negativen Schwelle und den PMOS-Gleichungen rechnen oder alle Größen dem Betrag nach einsetzen; im Abschnürbereich sind es −0,25 mA.
F: Stimmt es, dass die Schwellenspannung eines Transistors eine feste Größe ist?
A: Nein. Sie hängt von der Bulk-Source-Spannung ab: Beim Beispiel-NMOS steigt sie von 0,5 V bei $U_{BS}$ = 0 auf 0,768 V bei −1 V und 0,971 V bei −2 V; auch die Temperatur verschiebt sie.
F: Stimmt es, dass ein Latch-Up endet, sobald die Störung vorbei ist?
A: Nein. Die Mitkopplung der parasitären Transistoren hält den Pfad offen, solange rund 1 mA fließen kann; erst das Abschalten der Versorgung oder ein Strom unter dem Haltestrom beendet ihn.
F: Welche Schwelle hat der Beispiel-NMOS, wenn seine Source 1 V über dem Substrat liegt?
A: $0{,}5\ \mathrm V + 0{,}629\ \sqrt{\mathrm V}\cdot(\sqrt{1{,}923\ \mathrm V} - \sqrt{0{,}923\ \mathrm V})$ = 0,768 V.
F: Warum liefert ein NMOS-Sourcefolger bei 2 V Eingangsspannung nur 0,78 V statt 1 V?
A: Die Source und damit der Ausgang liegen über dem Substrat; die Schwelle steigt dadurch auf 0,717 V, und der Ausgang liegt um 0,717 V + 0,5 V unter dem Eingang. Kleine Änderungen gibt der Folger nur mit 1/(1 + η) ≈ 0,8 weiter.
F: Welche zwei Größen macht man klein, um Latch-Up zu verhindern, und warum?
A: Die Widerstände von Substrat und Wanne, damit ein Störstrom keine 0,6 V erzeugt, und die Stromverstärkungen der parasitären Transistoren, damit ihr Produkt unter 1 bleibt; dafür sorgen viele Kontakte, Epitaxie-Wafer, Abstände und Schutzringe.
:::
