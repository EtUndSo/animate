---
title: Bipolartransistor: Arbeitsbereiche und Transportmodell
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / Bipolartransistor
order: 33040100
summary: Wie der Bipolartransistor als spannungsgesteuerte Stromquelle mit einem kleinen Basisstrom arbeitet und wie das Transportmodell mit zwei Dioden und einer gesteuerten Quelle alle fünf Betriebszustände beschreibt. Kompakte Fassung mit Aufbau, Zählpfeilen, Kennlinien, Sättigung aus dem Transportmodell und Early-Effekt, durchgerechnet an einem integrierten Beispieltransistor.
tags: Bipolartransistor, Arbeitsbereich, Transportmodell, Ebers-Moll, Early-Effekt
stil: 3
fassung: kompakt
---

## Worum es geht

Ein MOSFET steuert seinen Strom über eine Kapazität, ohne Steuerstrom, aber nur mit dem Quadrat der Übersteuerung. Der __Bipolartransistor__ steuert seinen Strom über einen leitenden pn-Übergang: exponentiell, 60 mV für den Faktor zehn, mit zwanzigmal mehr Steilheit, also Stromänderung je Volt Steuerspannung, bei gleichem Strom, aber mit einem Steuerstrom, der sich nie ganz vermeiden lässt. Um damit zu rechnen, braucht man ein Modell, das beide pn-Übergänge und alle Betriebszustände abdeckt. Alles hängt an einem Prinzip:

**Der Bipolartransistor ist eine spannungsgesteuerte Stromquelle mit einem Nebenstrom: Die Basis-Emitter-Spannung legt über eine Diodengleichung den Transportstrom vom Kollektor zum Emitter fest, die Basis liefert davon nur den festen Bruchteil $1/B_N$ als Basisstrom, und das Transportmodell fasst beide pn-Übergänge und beide Stromrichtungen in zwei Dioden und einer gesteuerten Quelle zusammen, sodass alle fünf Betriebszustände aus demselben Modell folgen.**

Vorausgesetzt werden der pn-Übergang und die Diodengleichung aus [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html) und [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html), der physikalische Transistoreffekt aus [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html) und zum Vergleich die Kennlinien des MOSFET aus [Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien.html). Darauf bauen das Kleinsignalmodell des Bipolartransistors, die bipolaren Grundschaltungen, Stromspiegel und Differenzverstärker auf.

:::grafik
Szene: st1/bipolartransistor/01-einstieg · Vorlage: querschnitt-mit-modell
**Abbildung 1:** Links der npn-Transistor im Normalbetrieb, schematisch: Emitter, dünne Basis, Kollektor, beide Raumladungszonen, die ladungsträgerarmen Zonen der Übergänge, grau. Elektronen (blau) laufen vom Emitter durch die Basis in den Kollektor, 1 mA; über den Basisanschluss kommen Löcher (rot) nach, 10 µA. Rechts das vereinfachte Transportmodell: eine Diode zwischen Basis und Emitter mit 10 µA und eine gesteuerte Stromquelle vom Kollektor zum Emitter mit 1 mA, gesteuert von $U_{BE}$ = 774 mV. Die Basis-Emitter-Spannung legt den Kollektorstrom fest; die Basis liefert nur ein Hundertstel davon.
:::

## Aufbau und Zählpfeile

*Woraus besteht der Transistor, und wie zählt man seine Ströme und Spannungen?*

Ein Bipolartransistor besteht aus drei dotierten Gebieten, die zwei pn-Übergänge bilden; __Dotierung__ heißt, dass eingebaute Fremdatome bewegliche Elektronen (n-Gebiet) oder Löcher (p-Gebiet) liefern. Beim __npn-Transistor__ ist der __Emitter__ stark n-dotiert, die __Basis__ schwach p-dotiert und sehr dünn, beim integrierten Beispieltransistor 0,1 µm, der __Kollektor__ schwach n-dotiert. Elektronen und Löcher tragen beide zum Strom bei, daher der Name. Als Einzelbauteil sitzt der Kollektor als Substrat unten mit großflächigem Rückseitenkontakt; auf einem Chip liegt jeder Transistor in einer eigenen n-Wanne im p-Substrat, eine vergrabene, stark n-dotierte Schicht führt den Kollektorstrom niederohmig zu einem Kontakt oben, und der pn-Übergang zwischen Wanne und Substrat, die __Substratdiode__, ist immer gesperrt, weil das Substrat an der negativsten Versorgung liegt. Die aktive Fläche liegt unter dem Emitter; die __Emitterfläche__, beim Beispiel 2 µm × 10 µm, ist der Skalierungsparameter: Alle Ströme sind ihr proportional, so wie beim MOSFET dem Verhältnis $W/L$.

:::frage
„Warum muss das Substrat an die negativste Versorgung?“
Die Substratdiode liegt zwischen dem p-Substrat und jeder n-Wanne; sie sperrt nur, wenn das Substrat tiefer liegt als jeder Kollektor. Läge ein Kollektor im Betrieb unter dem Substratpotential, würde diese Diode leiten, und der Kollektorstrom flösse ins Substrat und in die Wannen der Nachbarn. Durch die gesperrte Diode fließt dagegen nur ihr Sperrstrom, um 10⁻¹⁵ A gegen 1 mA Kollektorstrom; so ist jeder Transistor von allen anderen getrennt.
:::

:::grafik
Szene: st1/bipolartransistor/01-symbole-zaehlpfeile · Vorlage: aufbau-und-symbol
**Abbildung 2:** (a) npn-Transistor: Schichtfolge n, p, n mit den beiden pn-Übergängen als Dioden, die Emitterdiode von der Basis zum Emitter, die Kollektordiode von der Basis zum Kollektor; daneben das Schaltsymbol mit dem Emitterpfeil nach außen. Zählpfeile: $I_B$ und $I_C$ in den Transistor hinein, $I_E$ ebenfalls hinein gezählt und deshalb negativ; Spannungen $U_{BE}$, $U_{CE}$ und $U_{BC}$. Werte im Normalbetrieb: $U_{BE}$ = 0,774 V, $U_{CE}$ = 2,5 V, $U_{BC}$ = −1,73 V, $I_B$ = 10 µA, $I_C$ = 1,05 mA, $I_E$ = −1,06 mA. (b) pnp-Transistor: Schichtfolge p, n, p, Emitterpfeil nach innen, dieselben Zählpfeile; alle Werte mit umgekehrtem Vorzeichen. Alle Ströme werden in den Transistor hinein gezählt, deshalb ist der Emitterstrom des npn negativ; der pnp ist derselbe Transistor mit umgekehrten Vorzeichen.
:::

Abbildung 2a zeigt die beiden Übergänge als Dioden: die __Emitterdiode__ zwischen Basis und Emitter, die __Kollektordiode__ zwischen Basis und Kollektor, beide mit der Anode an der Basis. Im Schaltsymbol trägt nur der Emitter einen Pfeil, in der Richtung, in der der Emitterstrom im Normalbetrieb wirklich fließt.

**Die Akteure:**

- __$I_B$__, __$I_C$__, __$I_E$__: Basis-, Kollektor- und Emitterstrom, alle in den Transistor hinein gezählt; beim npn im Normalbetrieb 10 µA, 1 mA und −1,01 mA.
- __$U_{BE}$__, __$U_{BC}$__, __$U_{CE}$__: Spannung von der Basis zum Emitter, von der Basis zum Kollektor und vom Kollektor zum Emitter, $U_{CE} = U_{BE} - U_{BC}$; beim npn im Normalbetrieb ist $U_{BE}$ positiv und $U_{BC}$ negativ.

Dass auch der Emitterstrom hinein gezählt wird, obwohl er heraus fließt, hat einen Grund: So gilt die Knotenregel in ihrer knappsten Form, und dieselben Gleichungen gelten für den __pnp-Transistor__ in Abbildung 2b, bei dem im Normalbetrieb alle Spannungen und Ströme negativ sind. Alles Weitere ist für den npn formuliert; für den pnp dreht man jedes Vorzeichen um.

:::formel Knotengleichung
$$I_E = -\big(I_B + I_C\big)$$
:::

**So liest man das:** Was an Basis und Kollektor hinein fließt, verlässt den Transistor am Emitter; der Emitterstrom ist dem Betrag nach der größte der drei, beim Beispiel 1,01 mA.

**Kurz gesagt:** Die Summe der drei in den Transistor hinein gezählten Ströme ist null.

Die Gleichung ist die Knotenregel für den Transistor als Ganzes: Im stationären Betrieb speichert er keine Ladung.

## Wie die Basis-Emitter-Spannung den Kollektorstrom festlegt

*Warum fließt ein großer Strom durch einen gesperrten Übergang, und welche Rolle spielt die Basis?*

:::grafik
Szene: st1/bipolartransistor/01-kennlinien · Vorlage: kennlinie-semilog-paar
**Abbildung 3:** Kennlinien des Beispieltransistors über $U_{BE}$ von 0,5 bis 0,9 V. (a) Übertragungskennlinie $I_C$ linear: 0,058 mA bei 0,70 V, 0,40 mA bei 0,75 V, 1,0 mA bei 0,774 V, 2,76 mA bei 0,80 V, 19 mA bei 0,85 V; Arbeitspunkt bei 1 mA. (b) Dieselbe Kennlinie halblogarithmisch von 10 nA bis 100 mA: eine Gerade mit 59,5 mV je Dekade. (c) Eingangskennlinie $I_B$: dieselbe Form mit einem Hundertstel der Werte, 10 µA bei 0,774 V und 27,6 µA bei 0,80 V. Übertragungs- und Eingangskennlinie sind dieselbe Exponentialfunktion, um den Faktor 100 verschoben; 60 mV mehr geben zehnmal so viel Strom.
:::

**Die Akteure:**

- __$I_S$__: __Transportsättigungsstrom__, der Vorfaktor der Diodengleichung des Kollektorstroms; 10⁻¹⁶ A beim integrierten Beispieltransistor, proportional zur Emitterfläche.
- __$U_T$__: Temperaturspannung, 25,85 mV bei 300 K; eine Spannungsstufe dieser Höhe ändert jeden Strom um den Faktor $\exp(1) \approx 2{,}72$.
- __$B_N$__: __Stromverstärkung__ im Normalbetrieb, das Verhältnis von Kollektor- zu Basisstrom; 100 beim Beispiel. N steht für normal, im Gegensatz zum Inversbetrieb.
- __$A$__: Verhältnis von Kollektor- zu Emitterstrom mit Minuszeichen; 0,990.

**Das Zusammenspiel:**

**Schritt 1**: Die beiden Übergänge liegen mit entgegengesetzter Durchlassrichtung in Reihe. Mit einer positiven Spannung $U_{CE}$ allein sperrt die Kollektordiode, und nur ihr Sperrstrom fließt.

**Schritt 2**: Eine Basis-Emitter-Spannung von 0,774 V senkt die Barriere der Emitterdiode; Elektronen diffundieren aus dem Emitter in die Basis, weil ihre Dichte am Rand der Raumladungszone um $\exp(U_{BE}/U_T)$ steigt, hier um 10¹³.

**Schritt 3** (entscheidender Schritt): Die Basis ist dünner als der Weg, den ein Elektron im Mittel vor der Rekombination zurücklegt. Fast alle Elektronen erreichen die Raumladungszone der gesperrten Kollektordiode, deren Feld sie in den Kollektor zieht. Der Kollektorstrom ist dieser Diffusionsstrom durch die Basis; er folgt der Diodengleichung mit $U_{BE}$, und $U_{CE}$ kommt darin nicht vor, solange die Kollektordiode sperrt.

**Schritt 4**: Die Basis ersetzt nur die Verluste, die wenigen Elektronen, die in der Basis rekombinieren, und die Löcher, die in den Emitter injiziert werden. Beide wachsen mit demselben Faktor $\exp(U_{BE}/U_T)$ wie der Kollektorstrom, also ist ihr Verhältnis fest: $1/B_N$, beim Beispiel 10 µA zu 1 mA. Abbildung 3c ist darum Abbildung 3a mit einem Hundertstel der Werte.

:::formel Normalbetrieb
$$I_C = I_S\,\Big(\exp\!\Big(\frac{U_{BE}}{U_T}\Big) - 1\Big)$$

$$I_B = \frac{I_C}{B_N}$$

$$I_E = -\Big(1 + \frac{1}{B_N}\Big)\,I_C$$

$$A = -\frac{I_C}{I_E} = \frac{B_N}{1 + B_N}$$
:::

**So liest man das:** Eingabe ist die Basis-Emitter-Spannung, Ausgabe der Kollektorstrom; je 59,5 mV mehr verzehnfacht er sich, je 17,9 mV verdoppelt er sich. Die −1 zählt nur unter etwa 0,1 V. Basis- und Emitterstrom folgen mit festen Faktoren; bei $B_N$ = 100 ist der Emitterstrom nur 1 % größer als der Kollektorstrom, dem Betrag nach sind beide fast gleich.

**Kurz gesagt:** Zehnmal so viel Kollektorstrom braucht 60 mV mehr Basis-Emitter-Spannung, bei jedem Ausgangsstrom gleich, solange die Diodengleichung gilt.

Idee der Herleitung: Der Kollektorstrom ist der Diffusionsstrom der Elektronen durch die Basis, also proportional zu ihrer Randdichte, und die wächst nach dem Gesetz des Übergangs exponentiell mit $U_{BE}$; Basis- und Emitterstrom folgen aus den Verlusten und der Knotenregel.

:::herleitung
**Ausgangspunkt:** Gesetz des Übergangs und Diffusionsstrom aus [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie-ausfuehrlich.html): Am Rand der Raumladungszone eines leitenden Übergangs ist die Dichte der Minoritätsträger, der seltenen Ladungsträgersorte des Gebiets, um $\exp(U/U_T)$ erhöht, und der Diffusionsstrom ist proportional zum Dichtegefälle. Die vollständige Rechnung mit Dotierung, Basisweite und Diffusionskonstante steht in [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise-ausfuehrlich.html).
**Annahmen:** (i) Normalbetrieb: Emitterdiode leitet, Kollektordiode sperrt; (ii) die Basis ist dünn gegen die Diffusionslänge der Elektronen, beim Beispiel 0,1 µm gegen einige Mikrometer, sodass die Rekombination in der Basis klein bleibt; (iii) schwache Injektion: Die Elektronendichte in der Basis bleibt klein gegen die Dotierung, beim Beispiel bis in den Bereich von 10 mA; (iv) stationärer Betrieb, keine Ladungsspeicherung.
**Schritt 1**: Elektronendichte am emitterseitigen Rand der Basis nach dem Gesetz des Übergangs, mit der Gleichgewichtsdichte $n_{B0}$ der Elektronen in der Basis:
$$n_B(0) = n_{B0}\,\exp\!\Big(\frac{U_{BE}}{U_T}\Big)$$
**Schritt 2**: Am kollektorseitigen Rand ist die Dichte praktisch null, weil das Feld der gesperrten Kollektordiode jedes ankommende Elektron abzieht; dazwischen fällt die Dichte nach (ii) geradlinig ab, über die Basisweite $W_B$. Das Gefälle ist $n_B(0)/W_B$.
**Schritt 3** (entscheidender Schritt): Der Diffusionsstrom der Elektronen durch die Basis ist proportional zu diesem Gefälle; mit der Emitterfläche $A_E$, der Diffusionskonstante $D_n$ und der Elementarladung $e$ gilt
$$I_C = e\,A_E\,D_n\,\frac{n_B(0)}{W_B} = \underbrace{\frac{e\,A_E\,D_n\,n_{B0}}{W_B}}_{I_S}\,\exp\!\Big(\frac{U_{BE}}{U_T}\Big)$$
Dieser Strom fließt vollständig in den Kollektor, nicht in die Basis, weil er die Basis nur durchquert. Die −1 der Diodengleichung ergibt sich, wenn man den Gleichgewichtsanteil $n_{B0}$ mitführt; sie ist nur ohne Durchlassspannung von Bedeutung.
**Schritt 4**: Die Basis liefert Löcher für zwei Verluste: Rekombination in der Basis und Injektion von Löchern in den Emitter. Beide sind proportional zur Überschussdichte $n_B(0)$ bzw. zur entsprechenden Randdichte im Emitter, also beide proportional zu $\exp(U_{BE}/U_T)$. Ihr Verhältnis zum Kollektorstrom ist deshalb eine Zahl, die nur von Dotierungen und Abmessungen abhängt:
$$I_B = \frac{I_C}{B_N}$$
**Schritt 5**: Knotenregel für den Transistor und Auflösen nach $I_E$ und $A$:
$$I_E = -(I_B + I_C) = -\Big(1 + \frac{1}{B_N}\Big)\,I_C$$
$$A = -\frac{I_C}{I_E} = \frac{1}{1 + 1/B_N} = \frac{B_N}{1 + B_N}$$
**Ergebnis:**
$$I_C = I_S\,\Big(\exp\!\Big(\frac{U_{BE}}{U_T}\Big) - 1\Big)$$
$$I_B = \frac{I_C}{B_N}$$

$$I_E = -\Big(1 + \frac{1}{B_N}\Big)\,I_C$$
**Woher die Faktoren kommen:** Die Exponentialfunktion stammt aus dem Gesetz des Übergangs (Schritt 1), $I_S$ aus Fläche, Diffusionskonstante, Gleichgewichtsdichte und Basisweite (Schritt 3): Eine dünnere Basis und eine größere Emitterfläche geben mehr Strom bei gleicher Spannung. $B_N$ ist das Verhältnis zweier Diffusionsströme, die mit derselben Exponentialfunktion wachsen (Schritt 4).
**Proben:** Einheit: A, weil $I_S$ in A ist. Grenzfall $U_{BE}$ = 0: $I_C$ = 0. Vorzeichen: $I_C$ > 0 in den Kollektor hinein, $I_E$ < 0. Zahlenwert: $I_S$ = 10⁻¹⁶ A, $U_{BE}$ = 773,8 mV: $\exp(29{,}93)$ = 10¹³, also 1,00 mA; $I_B$ = 10 µA, $I_E$ = −1,01 mA.
**Grenzen:** Leitet auch die Kollektordiode, fällt Annahme (i); dann gilt das Transportmodell (Abschnitt *Das Transportmodell*). Bei starker Injektion (iii) wächst der Strom langsamer als exponentiell, und bei kleinen Strömen kommt ein zusätzlicher Basisstrom aus der Raumladungszone hinzu.
:::

::::beispiel Ströme des Beispieltransistors im Normalbetrieb
**Gegeben:** Integrierter npn-Transistor mit $I_S$ = 10⁻¹⁶ A und $B_N$ = 100; $U_T$ = 25,85 mV; Kollektordiode gesperrt.

**Gesucht:** (a) die Basis-Emitter-Spannung für 1 mA Kollektorstrom sowie Basis- und Emitterstrom; (b) der Kollektorstrom bei 18 mV und bei 60 mV mehr.

**Rechnung:** (a) Diodengleichung nach $U_{BE}$ aufgelöst (die −1 ist bei 10¹³ bedeutungslos):

$$U_{BE} = U_T\,\ln\frac{I_C}{I_S} = 25{,}85\ \mathrm{mV}\cdot\ln\big(10^{13}\big) = 773{,}8\ \mathrm{mV}, \qquad I_B = 10\ \mathrm{\mu A}, \qquad I_E = -1{,}01\ \mathrm{mA}$$

(b) Jede Spannungsstufe multipliziert den Strom mit $\exp(\Delta U/U_T)$:

$$\exp\!\Big(\frac{18\ \mathrm{mV}}{25{,}85\ \mathrm{mV}}\Big) = 2{,}01, \qquad \exp\!\Big(\frac{60\ \mathrm{mV}}{25{,}85\ \mathrm{mV}}\Big) = 10{,}2$$

**Ergebnis:** **773,8 mV für 1 mA, dazu 10 µA Basisstrom und −1,01 mA Emitterstrom; 18 mV mehr verdoppeln, 60 mV mehr verzehnfachen den Strom.**

**Einordnung:** Von 0,1 mA bis 10 mA liegt $U_{BE}$ zwischen 714 und 833 mV; deshalb rechnet man von Hand oft mit einer festen Spannung um 0,7 bis 0,8 V. Ein diskreter Transistor mit 750-mal größerer Emitterfläche und 10⁻¹⁴ A braucht für 1 mA nur 655 mV.
::::

:::fehlvorstellung
„Der Basisstrom fließt durch den Transistor und wird $B_N$-fach verstärkt; der Kollektorstrom ist der verstärkte Basisstrom.“ Das liegt nahe, weil Datenblätter die Stromverstärkung an erster Stelle nennen und der Kollektorstrom in jeder Rechnung als $B_N$-faches des Basisstroms geschrieben wird. Tatsächlich fließt der Kollektorstrom vom Emitter durch die Basis in den Kollektor, ohne den Basisanschluss zu berühren; seine Größe bestimmt $U_{BE}$ (Schritt 3). Der Basisstrom ersetzt nur Verluste, 10 µA bei 1 mA. Beide Ströme haben dieselbe Ursache; die Gleichung mit $B_N$ verknüpft zwei Wirkungen, sie beschreibt keine Verstärkung eines Stroms.
:::

:::frage
„Wenn $U_{BE}$ den Strom festlegt, wozu braucht man dann überhaupt $B_N$?“
Weil der Basisstrom in jeder Schaltung von irgendwoher kommen muss. Die treibende Quelle muss 10 µA liefern; über einen Basiswiderstand von 10 kΩ fallen dabei 0,1 V ab, die an $U_{BE}$ fehlen. In Stromspiegeln und Differenzverstärkern erzeugt der Basisstrom Fehler von der Größe $1/B_N$. Die Spannung steuert, der Strom ist der Preis dafür; $B_N$ sagt, wie hoch er ist.
:::

Vertauscht man die Rollen, leitet also die Kollektordiode und sperrt die Emitterdiode, arbeitet der Transistor im __Inversbetrieb__. Weil der Kollektor viel schwächer dotiert ist als der Emitter, kostet die Injektion von dort viel mehr Basisstrom: Die Stromverstärkung $B_I$ ist beim Beispiel 2 statt 100. Absichtlich benutzt man den Inversbetrieb fast nie, aber in jedem gesättigten Transistor kommt er als Anteil vor.

## Die fünf Betriebszustände

*Welche Zustände kann der Transistor einnehmen, und woran erkennt man sie?*

:::grafik
Szene: st1/bipolartransistor/01-arbeitsbereiche · Vorlage: zustandsebene-und-kennlinienfeld
**Abbildung 4:** (a) Die Ebene aus $U_{BE}$ und $U_{BC}$, je von −1 bis 1 V, in vier farbige Quadranten geteilt: gesperrt (beide negativ), aktiv normal ($U_{BE}$ > 0, $U_{BC}$ < 0), Sättigung (beide positiv), invers ($U_{BE}$ < 0, $U_{BC}$ > 0); der Ursprung ist der stromlose Zustand, die Diagonale $U_{BC}$ = $U_{BE}$ die Linie $U_{CE}$ = 0. Der Arbeitspunkt (0,774 V, −1,73 V) liegt im aktiven Quadranten, der Sättigungspunkt (0,797 V, 0,697 V) nahe der Diagonale. (b) Ausgangskennlinienfeld $I_C$ über $U_{CE}$ von 0 bis 3 V für $U_{BE}$ = 0,70, 0,75, 0,774 und 0,80 V: steiler Anstieg bis etwa 0,1 V, danach fast waagerechte Geraden mit schwacher Steigung; der Sättigungsbereich links der Grenze bei 0,1 bis 0,3 V ist grau hinterlegt. Welche der beiden Dioden leitet, legt den Betriebszustand fest; im Kennlinienfeld ist die Sättigung der schmale Streifen links, der aktive Bereich sind die flachen Geraden.
:::

Jede der beiden Dioden kann leiten oder sperren; das gibt vier Zustände und den Sonderfall ohne Spannung (Abbildung 4a):

| Zustand | Dioden (Emitter, Kollektor) | Verhalten |
|---|---|---|
| stromlos | beide 0 V | keine Ströme |
| gesperrt | sperrt, sperrt | nur Sperrströme; Schalter aus |
| aktiv (normal) | leitet, sperrt | Stromquelle, $I_C$ aus $U_{BE}$; Verstärker |
| Sättigung | leitet, leitet | $U_{CE}$ um 0,1 V, Strom vom äußeren Kreis begrenzt; Schalter ein |
| invers | sperrt, leitet | Emitter und Kollektor vertauscht, $B_I$ = 2 |

Der aktive Zustand ist der Zustand aller Verstärkerschaltungen; die Formeln des vorigen Abschnitts gelten genau dort. Im Ausgangskennlinienfeld (Abbildung 4b) erkennt man ihn an den fast waagerechten Kennlinien: $U_{CE}$ ändert den Strom kaum, weil die Kollektordiode sperrt, solange der Kollektor nicht mehr als etwa 0,5 V unter der Basis liegt. Links davon, unter etwa 0,3 V, leitet die Kollektordiode, und die Kennlinien brechen steil ein: der __Sättigungsbereich__, in dem der äußere Kreis den Strom bestimmt und der Transistor ein geschlossener Schalter mit rund 0,1 V Restspannung ist.

:::fehlvorstellung
„Sättigung heißt beim Bipolartransistor dasselbe wie beim MOSFET: der flache Teil der Kennlinie.“ Das liegt nahe, weil beide Kennlinienfelder einen steilen und einen flachen Teil haben. Die Wörter sind aber vertauscht: Beim MOSFET ist der Sättigungsbereich der flache Verstärkerbereich ([Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien.html)); beim Bipolartransistor heißt der flache Teil aktiver Bereich, und Sättigung ist der steile Teil links, in dem beide Dioden leiten und der Transistor als Schalter mit 0,1 V Restspannung arbeitet.
:::

:::frage
„Wie kann die Kollektordiode leiten, wenn $U_{CE}$ doch positiv ist?“
Für die Kollektordiode zählt $U_{BC}$, die Spannung von der Basis zum Kollektor, und nicht $U_{CE}$. Liegt die Basis bei 0,8 V und der Kollektor bei 0,1 V, ist $U_{CE}$ positiv, aber die Basis liegt 0,7 V über dem Kollektor, und die Diode von der Basis zum Kollektor leitet. Die Grenze liegt bei $U_{BC}$ um 0,5 V, also bei $U_{CE}$ um 0,3 V.
:::

## Das Transportmodell

*Wie beschreibt man beide Übergänge und beide Stromrichtungen mit einem Modell?*

:::grafik
Szene: st1/bipolartransistor/01-transportmodell · Vorlage: ersatzschaltbild-paar
**Abbildung 5:** (a) Das Transportmodell: Von der Basis zum Kollektor die Kollektordiode mit dem Strom $I_{B,I}$, von der Basis zum Emitter die Emitterdiode mit $I_{B,N}$, zwischen Kollektor und Emitter die gesteuerte Stromquelle mit dem Transportstrom $I_T = B_N I_{B,N} - B_I I_{B,I}$, vom Kollektor zum Emitter gerichtet. Werte im Arbeitspunkt bei $U_{CE}$ = 2,5 V: $I_{B,N}$ = 10 µA, $I_{B,I}$ praktisch null, $I_T$ = 1,05 mA. (b) Das vereinfachte Transportmodell für den Normalbetrieb: nur die Emitterdiode mit $I_B$ und die Quelle $I_C = B_N I_B$; $I_E = -(1 + B_N)\,I_B$ = −1,01 mA ohne Early-Faktor. Zwei Dioden beschreiben die Basis, eine gesteuerte Quelle den Transportstrom durch sie; im Normalbetrieb bleiben eine Diode und eine Quelle übrig.
:::

In der Sättigung und im Inversbetrieb injiziert auch der Kollektor, und der Strom durch die Basis hat zwei Anteile mit entgegengesetzter Richtung. Das __Transportmodell__ in Abbildung 5a beschreibt beide Fälle zugleich; es ist die Form des __Ebers-Moll-Modells__, mit der Schaltungssimulatoren rechnen.

**Die Akteure:**

- __$I_{B,N}$__: Strom der Emitterdiode, der Anteil des Basisstroms, der zur Injektion vom Emitter gehört; 10 µA im Arbeitspunkt.
- __$I_{B,I}$__: Strom der Kollektordiode, der Anteil des Basisstroms zur Injektion vom Kollektor; im Normalbetrieb praktisch null, in der Sättigung von der Größe von $I_{B,N}$.
- __$B_I$__: Stromverstärkung im Inversbetrieb; 2.
- __$I_T$__: __Transportstrom__, der Strom, der tatsächlich vom Kollektor zum Emitter durch die Basis fließt; 1,05 mA im Arbeitspunkt.

**Das Zusammenspiel:** Jede Diode injiziert nach ihrer eigenen Diodengleichung, und jede Injektion erzeugt zwei Ströme: den, der die Basis durchquert und am anderen Übergang eingesammelt wird, und den Verluststrom, den die Basis nachliefert. Die Emitterinjektion liefert $B_N I_{B,N}$ als Transportstrom vom Kollektor zum Emitter, die Kollektorinjektion $B_I I_{B,I}$ in die Gegenrichtung; beide laufen durch dieselbe Basis, also zieht man sie ab. Die Basis sieht die Summe beider Verlustströme. Weil der Transportstrom in beide Richtungen durch dieselbe dünne Basis läuft, hat er in beiden Richtungen denselben Vorfaktor $I_S$; nur die Verluste, $B_N$ und $B_I$, sind verschieden.

:::formel Transportmodell
$$I_{B,N} = \frac{I_S}{B_N}\Big(\exp\!\Big(\frac{U_{BE}}{U_T}\Big) - 1\Big), \qquad I_{B,I} = \frac{I_S}{B_I}\Big(\exp\!\Big(\frac{U_{BC}}{U_T}\Big) - 1\Big)$$

$$I_T = B_N\,I_{B,N} - B_I\,I_{B,I} = I_S\,\big[\exp(U_{BE}/U_T) - \exp(U_{BC}/U_T)\big]$$

$$I_B = I_{B,N} + I_{B,I}$$

$$I_C = I_T - I_{B,I}$$

$$I_E = -I_T - I_{B,N}$$
:::

**So liest man das:** Eingabe sind die beiden Diodenspannungen, Ausgabe alle drei Anschlussströme. Der Transportstrom ist die Differenz zweier Exponentialfunktionen und hängt nur von den Spannungen ab; die Stromverstärkungen legen nur fest, wie viel Basisstrom jede Injektion kostet. Im Normalbetrieb ist $\exp(U_{BC}/U_T)$ winzig, $I_{B,I}$ wird −5·10⁻¹⁷ A, und das Modell schrumpft auf Abbildung 5b. Die Schreibweise des Transportstroms über die beiden Basisströme sieht wie eine stromgesteuerte Quelle aus; sie ist nur eine Umformung, die Quelle bleibt spannungsgesteuert.

**Kurz gesagt:** Der Basisstrom ist die Summe der Ströme beider Dioden, der Transportstrom die Differenz ihrer verstärkten Ströme.

Idee der Herleitung: Man überlagert die beiden Injektionen, die der Emitter und der Kollektor je nach ihrer Diodengleichung erzeugen, und zählt an jedem Anschluss zusammen, was ankommt.

:::herleitung
**Ausgangspunkt:** Die Diodengleichung des Normalbetriebs aus dem Abschnitt *Wie die Basis-Emitter-Spannung den Kollektorstrom festlegt*: Eine leitende Emitterdiode erzeugt den Transportstrom $I_S(\exp(U_{BE}/U_T) - 1)$ durch die Basis und den Verluststrom $1/B_N$ davon.
**Annahmen:** (i) Beide Übergänge sind unabhängig voneinander durch ihre Spannung beschrieben, und die Basis ist so dünn, dass der Transportstrom nur vom Dichtegefälle zwischen ihren beiden Rändern abhängt (dünne Basis); (ii) schwache Injektion an beiden Übergängen; (iii) Überlagerung: Die Elektronendichte in der Basis ist die Summe der Beiträge beider Ränder, weil die Diffusionsgleichung linear ist; (iv) stationär.
**Schritt 1**: Die Emitterdiode allein (Kollektordiode mit $U_{BC}$ = 0) liefert nach dem Ausgangspunkt
$$I_{T,N} = I_S\,\Big(\exp\!\Big(\frac{U_{BE}}{U_T}\Big) - 1\Big), \qquad I_{B,N} = \frac{I_{T,N}}{B_N}$$
**Schritt 2**: Die Kollektordiode allein ($U_{BE}$ = 0) injiziert Elektronen vom Kollektor in die Basis; sie diffundieren zum Emitter und werden dort eingesammelt. Das Dichtegefälle ist dasselbe wie in Schritt 1, nur gespiegelt, weil es durch dieselbe Basis mit derselben Gleichgewichtsdichte $n_{B0}$ und derselben Weite $W_B$ läuft; der Vorfaktor ist deshalb wieder $I_S$. Die Verluste sind andere, weil der Kollektor schwächer dotiert ist als der Emitter und mehr Löcher aus der Basis aufnimmt: Verstärkung $B_I$ statt $B_N$.
$$I_{T,I} = I_S\,\Big(\exp\!\Big(\frac{U_{BC}}{U_T}\Big) - 1\Big), \qquad I_{B,I} = \frac{I_{T,I}}{B_I}$$
**Schritt 3** (entscheidender Schritt): Nach (iii) addieren sich die Elektronendichten, also auch die Diffusionsströme. Der Strom von Schritt 1 fließt vom Kollektor zum Emitter, der von Schritt 2 umgekehrt; der Netto-Transportstrom vom Kollektor zum Emitter ist die Differenz:
$$I_T = I_{T,N} - I_{T,I} = I_S\,\big[\exp(U_{BE}/U_T) - \exp(U_{BC}/U_T)\big]$$
$$I_T = B_N\,I_{B,N} - B_I\,I_{B,I}$$
Die beiden −1 heben sich auf; die letzte Form folgt durch Einsetzen von Schritt 1 und 2.
**Schritt 4**: Zählen an den Anschlüssen. Die Basis liefert beide Verlustströme. In den Kollektor fließt hinein, was die Quelle aus ihm abzieht, abzüglich des Stroms, der von der Basis über die Kollektordiode in den Kollektor kommt, denn er stammt aus der Basis, nicht aus dem Kollektoranschluss. Am Emitter kommt der Transportstrom an und zusätzlich der Strom der Emitterdiode; beide verlassen den Transistor:
$$I_B = I_{B,N} + I_{B,I}$$

$$I_C = I_T - I_{B,I}$$
$$I_E = -I_T - I_{B,N}$$
**Ergebnis:**
$$I_T = I_S\,\big[\exp(U_{BE}/U_T) - \exp(U_{BC}/U_T)\big]$$
$$I_B = I_{B,N} + I_{B,I}$$

$$I_C = I_T - I_{B,I}$$
$$I_E = -I_T - I_{B,N}$$
**Woher die Faktoren kommen:** Das gemeinsame $I_S$ beider Richtungen stammt aus Schritt 2 (gleiche Basis, gleiches Gefälle); $B_N$ und $B_I$ aus den verschiedenen Verlusten der beiden Übergänge; das Minuszeichen im Transportstrom aus der Gegenrichtung in Schritt 3.
**Proben:** Knotenregel: Die Summe der drei Anschlussströme ist null, weil sich $I_{B,N}$, $I_{B,I}$ und $I_T$ in ihr paarweise aufheben. Normalbetrieb ($U_{BC}$ stark negativ): $I_{B,I} \to -I_S/B_I \approx 0$, und die Formeln des vorigen Abschnitts bleiben übrig. Zahlenwert: $U_{BE}$ = 773,8 mV, $U_{BC}$ = −1,73 V: $I_{B,N}$ = 10 µA, $I_{B,I}$ = −5·10⁻¹⁷ A, $I_T$ = 1,00 mA ohne und 1,05 mA mit Early-Effekt.
**Grenzen:** Bei starker Injektion (ii) wächst der Transportstrom langsamer als exponentiell; die Spannungsabhängigkeit der Basisweite kommt als Early-Faktor hinzu (Abschnitt *Der Early-Effekt*); Ladungsspeicherung bei schnellen Änderungen (iv) braucht zusätzliche Kapazitäten.
:::

## Sättigung: beide Dioden leiten

*Warum bleibt der Kollektorstrom in der Sättigung stehen, obwohl mehr Basisstrom fließt, und woher kommt die kleine Restspannung?*

**Die Akteure:**

- __$U_{CC}$__: Versorgungsspannung des Kollektorkreises; 2,5 V im Beispiel.
- __$R_L$__: Lastwiderstand zwischen Versorgung und Kollektor; 1 kΩ.
- __$U_\mathrm{CE,sat}$__: __Sättigungsspannung__, die Kollektor-Emitter-Spannung, die in der Sättigung übrig bleibt; 100 mV bei 50 µA Basisstrom.

**Das Zusammenspiel:**

**Schritt 1**: Der Kollektorkreis lässt höchstens den Strom zu, bei dem fast die ganze Versorgung am Widerstand abfällt: mit 2,5 V und 1 kΩ rund 2,4 mA, wenn am Transistor 0,1 V bleiben.

**Schritt 2**: Mehr Basisstrom hebt $U_{BE}$ und den Transportstrom, und $U_{CE}$ sinkt. Bei 10 µA liegen noch 1,47 V am Transistor, die Kollektordiode ist mit −0,70 V gesperrt; bei 23 µA sind es 217 mV, und die Kollektordiode hat mit 578 mV zu leiten begonnen.

**Schritt 3** (entscheidender Schritt): Ab jetzt teilt sich der Basisstrom. Was über die Kollektordiode abfließt, treibt den Transportstrom nicht, sondern senkt ihn um $B_I I_{B,I}$. Bei 50 µA gehen 24,7 µA in die Emitterdiode und 25,3 µA in die Kollektordiode (Abbildung 5a mit diesen Werten); der Transportstrom ist 2,42 mA, der Kollektorstrom 2,40 mA statt 5 mA.

**Schritt 4**: Die Dioden stellen sich so ein, dass genau der Strom fließt, den der Widerstand zulässt: Emitterdiode 797 mV, Kollektordiode 697 mV, Differenz 100 mV. Das ist die Sättigungsspannung. Mehr Basisstrom drückt sie nur noch logarithmisch, auf 75 mV bei 100 µA.

:::formel Sättigungsspannung
$$U_\mathrm{CE,sat} = U_T\,\ln\frac{1 + \dfrac{1 + I_C/I_B}{B_I}}{1 - \dfrac{I_C}{B_N\,I_B}}$$
:::

**So liest man das:** Eingabe ist das Verhältnis von Kollektor- zu Basisstrom, das der äußere Kreis erzwingt; Ausgabe die Restspannung. Nähert sich $I_C/I_B$ der Stromverstärkung $B_N$, geht der Nenner gegen null und die Spannung gegen unendlich: die Grenze zum aktiven Bereich. Je mehr Basisstrom bei gleichem Kollektorstrom, desto kleiner die Restspannung; bei offenem Kollektor bleiben 10,5 mV.

Idee der Herleitung: Man schreibt Kollektor- und Basisstrom des Transportmodells mit beiden Exponentialfunktionen, bildet ihr Verhältnis und löst nach dem Quotienten der beiden Exponentialfunktionen auf, der $\exp(U_{CE}/U_T)$ ist.

:::herleitung
**Ausgangspunkt:** das Transportmodell aus dem Abschnitt *Das Transportmodell*.
**Annahmen:** (i) beide Dioden leiten, sodass die −1 in beiden Diodengleichungen entfällt; (ii) kein Early-Effekt; (iii) der äußere Kreis gibt das Verhältnis $k = I_C/I_B$ vor.
**Schritt 1**: Abkürzungen für die beiden Exponentialfunktionen:
$$x = \exp\!\Big(\frac{U_{BE}}{U_T}\Big), \qquad y = \exp\!\Big(\frac{U_{BC}}{U_T}\Big)$$
$$\frac{x}{y} = \exp\!\Big(\frac{U_{BE} - U_{BC}}{U_T}\Big) = \exp\!\Big(\frac{U_{CE}}{U_T}\Big)$$
**Schritt 2**: Kollektor- und Basisstrom aus dem Transportmodell:
$$I_C = I_T - I_{B,I} = I_S\,x - I_S\,y\,\Big(1 + \frac{1}{B_I}\Big)$$
$$I_B = \frac{I_S\,x}{B_N} + \frac{I_S\,y}{B_I}$$
**Schritt 3** (entscheidender Schritt): Das Verhältnis $k = I_C/I_B$ einsetzen; $I_S$ kürzt sich:
$$x - y\,\Big(1 + \frac{1}{B_I}\Big) = k\,\Big(\frac{x}{B_N} + \frac{y}{B_I}\Big)$$
Nach $x$ und $y$ geordnet:
$$x\,\Big(1 - \frac{k}{B_N}\Big) = y\,\Big(1 + \frac{1 + k}{B_I}\Big)$$
**Schritt 4**: Auflösen und logarithmieren:
$$\exp\!\Big(\frac{U_{CE}}{U_T}\Big) = \frac{x}{y} = \frac{1 + (1 + k)/B_I}{1 - k/B_N}$$
**Ergebnis:**
$$U_\mathrm{CE,sat} = U_T\,\ln\frac{1 + (1 + I_C/I_B)/B_I}{1 - I_C/(B_N\,I_B)}$$
**Woher die Faktoren kommen:** Der Zähler stammt aus dem Strom der Kollektordiode, der den Kollektorstrom mindert und den Basisstrom erhöht; der Nenner aus dem Anteil des Basisstroms, der die Emitterdiode treibt. Der Logarithmus kommt daher, dass die Spannung der Exponent ist.
**Proben:** Einheit: V, weil der Logarithmus dimensionslos ist. Grenzfall $k \to B_N$: Nenner null, $U_{CE} \to \infty$, also kein Sättigungszustand; Grenzfall $k$ = 0: $U_T \ln(1 + 1/B_I)$ = 10,5 mV. Vorzeichen: positiv, weil der Zähler größer als der Nenner ist. Zahlenwert: $k$ = 48,0, $B_I$ = 2, $B_N$ = 100: Zähler 25,5, Nenner 0,520, Quotient 49,0, $\ln$ = 3,89, also 100,6 mV; numerisch mit Early-Effekt 100,5 mV.
**Grenzen:** Mit den Widerständen der Zuleitungen im Transistor, den Bahnwiderständen, beim Beispiel 20 Ω am Kollektor und 5 Ω am Emitter, kommt zur Restspannung ihr Spannungsabfall hinzu, bei 2,4 mA rund 60 mV; bei starker Injektion ändert sich der Transportstrom.
:::

::::beispiel Sättigung bei 50 µA Basisstrom
**Gegeben:** Beispieltransistor ($I_S$ = 10⁻¹⁶ A, $B_N$ = 100, $B_I$ = 2, $U_A$ = 50 V) mit der Basis an einer Stromquelle von 50 µA, dem Kollektor über $R_L$ = 1 kΩ an $U_{CC}$ = 2,5 V und dem Emitter an Masse.

**Gesucht:** die Aufteilung des Basisstroms, Kollektorstrom und Sättigungsspannung.

**Rechnung:** Im aktiven Bereich wären es 5 mA, der Widerstand lässt höchstens 2,5 mA zu; also leiten beide Dioden. Die numerische Lösung der beiden Gleichungen (Basisstrom 50 µA, Kollektorstrom gleich $(U_{CC} - U_{CE})/R_L$) ist $U_{BE}$ = 797,2 mV und $U_{BC}$ = 696,6 mV; Probe mit den Diodengleichungen:

$$I_{B,N} = \frac{10^{-16}\ \mathrm A}{100}\,\exp\!\Big(\frac{797{,}2}{25{,}85}\Big) = 24{,}7\ \mathrm{\mu A}, \qquad I_{B,I} = \frac{10^{-16}\ \mathrm A}{2}\,\exp\!\Big(\frac{696{,}6}{25{,}85}\Big) = 25{,}3\ \mathrm{\mu A}$$

$$I_T = \big(100\cdot24{,}7 - 2\cdot25{,}3\big)\ \mathrm{\mu A}\cdot1{,}002 = 2{,}42\ \mathrm{mA}, \qquad I_C = 2{,}42\ \mathrm{mA} - 25{,}3\ \mathrm{\mu A} = 2{,}40\ \mathrm{mA}$$

Probe am Widerstand: 2,5 V minus 2,40 V sind 0,10 V, und $U_{CE}$ = 797,2 − 696,6 = 100,6 mV. Über die Formel mit $k$ = 2,40 mA / 50 µA = 48,0:

$$U_\mathrm{CE,sat} = 25{,}85\ \mathrm{mV}\cdot\ln\frac{1 + 49{,}0/2}{1 - 48{,}0/100}$$

$$U_\mathrm{CE,sat} = 25{,}85\ \mathrm{mV}\cdot\ln 49{,}0 = 100{,}6\ \mathrm{mV}$$

**Ergebnis:** **24,7 µA in die Emitterdiode, 25,3 µA in die Kollektordiode; $I_C$ = 2,40 mA statt 5 mA; $U_\mathrm{CE,sat}$ = 100 mV.**

**Einordnung:** Die Hälfte des Basisstroms fließt in der Sättigung nutzlos über die Kollektordiode ab. Einen Schalter stört das nicht, es kostet nur Steuerstrom; mit 100 µA sinkt die Restspannung auf 75 mV. Mit 10 µA bliebe der Transistor aktiv: 1,03 mA bei 1,47 V. Die Grenze liegt bei etwa 24 µA, dem Quotienten aus 2,4 mA und 100.
::::

## Der Early-Effekt

*Warum steigt der Kollektorstrom im aktiven Bereich doch leicht mit der Kollektorspannung?*

:::grafik
Szene: st1/bipolartransistor/01-early-effekt · Vorlage: kennlinienfeld-extrapolation
**Abbildung 6:** (a) Ausgangskennlinien für $U_{BE}$ = 0,75, 0,774 und 0,80 V über $U_{CE}$ von −50 V bis 5 V mit Achsenbruch: Im aktiven Bereich sind sie Geraden, für 1 mA mit der Steigung 20 µS, also 1,00 mA bei 0 V, 1,02 mA bei 1 V, 1,05 mA bei 2,5 V und 1,10 mA bei 5 V; nach links verlängert treffen sich alle bei −$U_A$ = −50 V. (b) Die Basis im Querschnitt: Zwischen den beiden Raumladungszonen liegt die neutrale Basis der Weite $W_B$; bei $U_{CB}$ = 5 V dringt die Kollektor-Raumladungszone tiefer in die Basis als bei 1 V, und die neutrale Basis wird schmaler. Daneben der Elektronenverlauf in der Basis als Gerade, die bei kürzerer Basis steiler wird. Mehr Kollektorspannung verbreitert die Kollektor-Raumladungszone, verkürzt die Basis und steigert den Strom; alle Tangenten treffen sich bei −$U_A$.
:::

**Die Akteure:**

- __$W_B$__: neutrale Basisweite zwischen den beiden Raumladungszonen; um 0,1 µm. Sie steht im Nenner von $I_S$.
- __$U_A$__: __Early-Spannung__, die Spannung, bei der die verlängerten Ausgangskennlinien die Spannungsachse schneiden; 50 V beim Beispiel. Sie entspricht $1/\lambda$ beim MOSFET, dessen Beispieltransistor mit λ = 0,1 1/V nur 10 V erreicht.

**Das Zusammenspiel:** Die Raumladungszone der gesperrten Kollektordiode wird mit der Sperrspannung breiter, wie bei jeder Diode, und wächst auch in die Basis hinein (Abbildung 6b). Die neutrale Basis wird schmaler, das Dichtegefälle der Elektronen steiler, und $I_S$ ist umgekehrt proportional zu $W_B$. Mehr Kollektorspannung heißt also mehr Strom bei gleicher $U_{BE}$: 10 % zwischen 0 und 5 V beim Beispiel. Die Basisströme ändern sich dabei nicht, weil die Rückinjektion in den Emitter nur von $U_{BE}$ abhängt und die Rekombination in der kürzeren Basis sogar abnimmt; mit $U_{CE}$ wächst deshalb auch das Verhältnis $I_C/I_B$, von 100 auf 105 bei 2,5 V.

:::formel Early-Effekt
$$I_C = I_S\,\Big(\exp\!\Big(\frac{U_{BE}}{U_T}\Big) - 1\Big)\,\Big(1 + \frac{U_{CE}}{U_A}\Big)$$
:::

**So liest man das:** Zur Diodengleichung kommt ein Faktor, der linear mit $U_{CE}$ wächst; bei $-U_A$ wäre er null, daher der gemeinsame Schnittpunkt. Je größer $U_A$, desto flacher die Kennlinien und desto besser die Stromquelle: Bei 1 mA steigt die Kennlinie mit 20 µS, das entspricht 50 kΩ. Genauer wäre $U_{CB}$ im Faktor, der Unterschied ist beim Beispiel 1,5 %.

**Kurz gesagt:** Im linearisierten Modell wächst der Kollektorstrom je Volt Kollektor-Emitter-Spannung um den Bruchteil $1/U_A$ seines Werts bei null Volt, beim Beispiel um ein Fünfzigstel.

Idee der Herleitung: Man lässt die Basisweite linear mit $U_{CB}$ schrumpfen, setzt sie in $I_S$ ein und linearisiert den Kehrwert.

:::herleitung
**Ausgangspunkt:** der Ausdruck für $I_S$ mit der Basisweite $W_B$ im Nenner aus der Herleitung des Kollektorstroms (Abschnitt *Wie die Basis-Emitter-Spannung den Kollektorstrom festlegt*) und die Sperrschichtweite einer Diode, die mit der Sperrspannung wächst ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie-ausfuehrlich.html)).
**Annahmen:** (i) Die Kollektor-Raumladungszone dringt mit wachsender Sperrspannung in die Basis ein; über den betrachteten Bereich genügt eine lineare Näherung; (ii) die Änderung der Basisweite ist klein gegen die Basisweite ($U_{CB} \ll U_A$); (iii) $U_{BE} \ll U_A$, sodass $U_{CB}$ durch $U_{CE}$ ersetzt werden darf.
**Schritt 1**: Lineare Näherung der Basisweite mit der Weite $W_{B0}$ bei $U_{CB}$ = 0 und der Early-Spannung als Maß für die Steigung:
$$W_B(U_{CB}) = W_{B0}\,\Big(1 - \frac{U_{CB}}{U_A}\Big), \qquad U_A = \frac{W_{B0}}{-\,\mathrm dW_B/\mathrm dU_{CB}}$$
Eine Zone, die bei 5 V um 1 % der Basisweite eindringt, ergibt $U_A$ = 500 V; beim Beispiel sind es 2 % je Volt, also 50 V.
**Schritt 2**: Einsetzen in $I_S$, das umgekehrt proportional zu $W_B$ ist:
$$I_S(U_{CB}) = \frac{I_{S0}}{1 - U_{CB}/U_A}$$
**Schritt 3** (entscheidender Schritt): Linearisieren nach (ii), denn $1/(1 - z) \approx 1 + z$ für kleine $z$:
$$I_C = I_{S0}\,\Big(\exp\!\Big(\frac{U_{BE}}{U_T}\Big) - 1\Big)\,\Big(1 + \frac{U_{CB}}{U_A}\Big)$$
**Schritt 4**: Nach (iii) darf die Basis-Emitter-Spannung gegen die Early-Spannung vernachlässigt werden:
$$U_{CB} = U_{CE} - U_{BE} \approx U_{CE}$$
**Ergebnis:**
$$I_C = I_S\,\Big(\exp\!\Big(\frac{U_{BE}}{U_T}\Big) - 1\Big)\,\Big(1 + \frac{U_{CE}}{U_A}\Big)$$
**Woher die Faktoren kommen:** Der Faktor stammt aus dem Nenner $W_B$ von $I_S$ (Schritt 2); $U_A$ ist eine Eigenschaft der Dotierungen: Je stärker die Basis und je schwächer der Kollektor dotiert ist, desto weniger dringt die Zone in die Basis ein und desto größer ist $U_A$.
**Proben:** Einheit: dimensionsloser Faktor. Grenzfall $U_A \to \infty$: Diodengleichung ohne Spannungsabhängigkeit. Vorzeichen: Der Strom wächst mit $U_{CE}$. Zahlenwert: $U_{CE}$ = 5 V, $U_A$ = 50 V: Faktor 1,10, also 1,10 mA statt 1,00 mA; die exakte Form $1/(1 - U_{CB}/U_A)$ gäbe mit $U_{CB}$ = 4,23 V den Faktor 1,092.
**Grenzen:** Bei großem $U_{CB}$ versagt (ii), und die Zone kann die Basis ganz durchdringen (Durchgriff, englisch punch-through); dann steigt der Strom steil an. Bei starker Injektion verschiebt der Transportstrom selbst die Zone.
:::

::::beispiel Kollektorstrom mit Early-Effekt
**Gegeben:** Beispieltransistor mit $I_S$ = 10⁻¹⁶ A, $U_A$ = 50 V und $B_N$ = 100 bei $U_{BE}$ = 773,8 mV.

**Gesucht:** Kollektorstrom und Verhältnis $I_C/I_B$ bei $U_{CE}$ = 1 V, 2,5 V und 5 V sowie die Steigung der Ausgangskennlinie.

**Rechnung:** Ohne Early-Effekt fließen 1,00 mA, der Basisstrom bleibt 10 µA:

$$I_C(1\ \mathrm V) = 1{,}00\ \mathrm{mA}\cdot1{,}02 = 1{,}02\ \mathrm{mA}, \qquad I_C(2{,}5\ \mathrm V) = 1{,}05\ \mathrm{mA}, \qquad I_C(5\ \mathrm V) = 1{,}10\ \mathrm{mA}$$

$$\frac{I_C}{I_B} = 102, \quad 105, \quad 110, \qquad \frac{\mathrm dI_C}{\mathrm dU_{CE}} = \frac{1{,}00\ \mathrm{mA}}{50\ \mathrm V} = 20\ \mathrm{\mu S}$$

**Ergebnis:** **1,02 mA, 1,05 mA und 1,10 mA; die Kennlinie steigt mit 20 µS, das entspricht 50 kΩ.**

**Einordnung:** Die Stromquelle ist nicht ideal, aber gut: 50 kΩ Innenwiderstand bei 1 mA; der Beispiel-MOSFET hat bei 1 mA und λ = 0,1 1/V nur 10 kΩ. Datenblätter nennen die Stromverstärkung deshalb immer mit der Messbedingung $U_{CE}$.
::::

## Was das Modell weglässt

*Wo weicht ein wirklicher Transistor vom Transportmodell ab?*

Die Stromverstärkung ist nur in der Mitte des Strombereichs konstant. Bei kleinen Strömen kommt ein Rekombinationsstrom der Basis-Emitter-Raumladungszone hinzu, der nur mit $\exp(U_{BE}/(2U_T))$ wächst und deshalb relativ immer größer wird: Beim Beispiel fällt $B$ von 95 bei 1 mA auf 50 bei 1 µA. Bei großen Strömen übersteigt die Elektronendichte in der Basis die Dotierung, der Transportstrom wächst nur noch mit der Wurzel der Exponentialfunktion, und $B$ fällt auf 83 bei 10 mA und 33 bei 100 mA. Dazu kommen die __Bahnwiderstände__ der Gebiete zwischen den Kontakten und dem aktiven Bereich, beim Beispiel 100 Ω in der Basis, 5 Ω im Emitter und 20 Ω im Kollektor. Der Emitterwiderstand liegt in Reihe mit der steuernden Spannung: 5 mV Abfall bei 1 mA senken den Strom bei fester äußerer Spannung auf 83 %, eine Stromgegenkopplung, die die Technologie mit der vergrabenen Schicht und großen Kontakten klein hält. Im Normalbetrieb ist der Bipolartransistor dem MOSFET bei gleichem Strom in der Steilheit weit überlegen, 38,7 mS gegen 2 mS bei 1 mA, denn seine Steilheit je Strom ist die Naturkonstante $1/U_T$; der Preis ist der Basisstrom, der die Eingänge niederohmig macht.

:::frage
„Kann ich den Basisstrom in Rechnungen weglassen, wenn doch $I_E \approx I_C$ gilt?“
Nur dort, wo er mit dem Kollektorstrom verglichen wird, denn er macht nur 1 % des Emitterstroms aus. Am Eingang ist er die ganze Last: 10 µA, über 10 kΩ Quellwiderstand 100 mV. In einem Stromspiegel fehlen am Ausgang 2 % des Referenzstroms, weil zwei Basisströme abgezweigt werden, und in der Sättigung entscheidet gerade der Basisstrom über die Restspannung (Abschnitt *Sättigung: beide Dioden leiten*).
:::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Diodengleichung des Kollektorstroms | die Spannung an der Emitterdiode steuert den Transportstrom |
| Basisstrom $I_C/B_N$ | der Nebenstrom: ein fester Bruchteil, der die Verluste ersetzt |
| Transportmodell mit zwei Dioden | beide Übergänge injizieren, beide Richtungen durch dieselbe Basis |
| Sättigung mit 0,1 V Restspannung | zwei leitende Dioden, deren Differenz der äußere Kreis festlegt |
| Early-Effekt | der Vorfaktor der Diodengleichung hängt über die Basisweite von $U_{CE}$ ab |

Der Bipolartransistor ist eine spannungsgesteuerte Stromquelle mit einem Nebenstrom: Die Basis-Emitter-Spannung legt über eine Diodengleichung den Transportstrom vom Kollektor zum Emitter fest, die Basis liefert davon nur den festen Bruchteil $1/B_N$ als Basisstrom, und das Transportmodell fasst beide pn-Übergänge und beide Stromrichtungen in zwei Dioden und einer gesteuerten Quelle zusammen, sodass alle fünf Betriebszustände aus demselben Modell folgen.

## Bedeutung und Ausblick

Bipolartransistoren tragen heute vor allem die Hochfrequenztechnik: Eine Bipolar- oder BiCMOS-Technologie, die Bipolar- und CMOS-Transistoren auf einem Chip vereint, mit 180 oder 250 nm Strukturbreite liefert Schaltungen für Funksysteme bei 60 GHz und Fahrzeugradar bei 77 GHz, wofür reine CMOS-Technologien Strukturen unter 65 nm brauchen. Das Transportmodell gilt für schwache Injektion und langsame Änderungen; der nächste Artikel linearisiert es im Arbeitspunkt zum Kleinsignalmodell mit Steilheit $I_C/U_T$, Eingangswiderstand $B_N U_T/I_C$ und Ausgangswiderstand $U_A/I_C$.

**In der ausführlichen Fassung:** der diskrete und der integrierte Aufbau mit vergrabener Schicht und Substratdiode als eigener Abschnitt, das Transportmodell im Normal- und Inversbetrieb durchgerechnet, der Gummel-Plot mit der Stromverstärkung über dem Strom und ihrer Herleitung, das statische Großsignalmodell mit Bahnwiderständen und einem Beispiel zur Stromgegenkopplung sowie eine Vergleichstabelle von Bipolartransistor und MOSFET ([Bipolartransistor: Arbeitsbereiche und Transportmodell, ausführlich](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/bipolartransistor/aufbau-und-transportmodell-ausfuehrlich.html)).

:::kern
- Alle drei Ströme werden in den Transistor hinein gezählt: $I_E = -(I_B + I_C)$; beim npn ist $I_E$ negativ, beim pnp sind alle Vorzeichen umgekehrt.
- Die Basis-Emitter-Spannung steuert den Kollektorstrom exponentiell: $I_C = I_S\exp(U_{BE}/U_T)$, 60 mV je Dekade.
- Der Basisstrom ersetzt nur Verluste und ist der feste Bruchteil $I_C/B_N$; der Kollektorstrom fließt nicht über die Basis.
- Fünf Zustände nach Leiten und Sperren beider Dioden; Verstärker im aktiven Zustand, Schalter in der Sättigung, in der beide Dioden leiten.
- Transportmodell: $I_T = B_N I_{B,N} - B_I I_{B,I}$ und $I_B = I_{B,N} + I_{B,I}$; die Quelle ist spannungsgesteuert.
- In der Sättigung teilt sich der Basisstrom auf beide Dioden, der äußere Kreis bestimmt den Strom, und $U_\mathrm{CE,sat}$ ist die Differenz zweier Durchlassspannungen, um 0,1 V.
- Early-Effekt: Faktor $(1 + U_{CE}/U_A)$ durch die spannungsabhängige Basisweite; $U_A$ = 50 V beim Beispiel.
:::

:::quiz
F: Warum legt die Basis-Emitter-Spannung den Kollektorstrom fest und nicht die Kollektor-Emitter-Spannung?
A: Der Kollektorstrom ist der Diffusionsstrom der Elektronen durch die dünne Basis; sein Antrieb ist die Randdichte am Emitterübergang, die mit $\exp(U_{BE}/U_T)$ wächst. Der gesperrte Kollektorübergang sammelt alles ein, was ankommt; $U_{CE}$ wirkt nur über die Basisweite schwach mit.
F: Warum bleibt der Kollektorstrom in der Sättigung stehen, obwohl der Basisstrom weiter steigt?
A: Der äußere Kreis lässt nur $(U_{CC} - U_{CE})/R_L$ zu. Sobald die Kollektordiode leitet, fließt der zusätzliche Basisstrom über sie ab und senkt den Transportstrom sogar; bei 50 µA gehen 25,3 µA diesen Weg, und $I_C$ bleibt bei 2,40 mA statt 5 mA.
F: Stimmt es, dass der Kollektorstrom der verstärkte Basisstrom ist?
A: Nein. Der Kollektorstrom fließt vom Emitter durch die Basis in den Kollektor und wird von $U_{BE}$ bestimmt; der Basisstrom ersetzt nur Verluste. Beide haben dieselbe Ursache und sind deshalb proportional, aber keiner erzeugt den anderen.
F: Stimmt es, dass Sättigung beim Bipolartransistor dasselbe bedeutet wie beim MOSFET?
A: Nein. Beim MOSFET ist der Sättigungsbereich der flache Verstärkerbereich; beim Bipolartransistor ist Sättigung der steile Bereich links, in dem beide Dioden leiten und der Transistor als Schalter mit 0,1 V Restspannung arbeitet.
F: Warum treffen sich alle verlängerten Ausgangskennlinien in einem Punkt?
A: Der Early-Faktor $(1 + U_{CE}/U_A)$ multipliziert jede Kennlinie mit derselben Geraden, die bei $U_{CE} = -U_A$ null wird; beim Beispiel bei −50 V.
F: Wie groß sind Kollektor-, Basis- und Emitterstrom des Beispieltransistors bei $U_{BE}$ = 0,80 V und $U_{CE}$ = 2,5 V?
A: $I_C$ = 10⁻¹⁶ A · exp(800/25,85) · 1,05 = 2,76 mA · 1,05 = 2,89 mA; $I_B$ = 2,76 mA / 100 = 27,6 µA; $I_E$ = −(2,89 + 0,028) mA = −2,92 mA.
:::
