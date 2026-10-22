---
title: Gleichrichtung und Ladungspumpe
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Halbleiterbauelemente
order: 100600
summary: Wie Dioden aus Wechselspannung eine Gleichspannung machen und mit Kondensatoren eine Spannung sogar vervielfachen: Brückenschaltung nach Graetz, Glättung mit dem Ladekondensator und Ladungspumpe. Kompakte Fassung; die ausführliche enthält zusätzlich den Mittelwert, die Sperrspannung der Dioden, Einschaltströme und weitere Rechnungen.
tags: Gleichrichter, Einweggleichrichter, Brückengleichrichter, Graetz, Glättung, Brummspannung, Ladungspumpe
stil: 3
fassung: kompakt
---

## Worum es geht

Das Stromnetz liefert Wechselspannung, Elektronik braucht Gleichspannung. Dioden legen die Richtung des Stroms fest, weil sie ihn nur in einer Richtung durchlassen.
**Eine Diode lässt Strom nur in eine Richtung: Gleichrichter lenken damit beide Halbwellen in derselben Richtung durch die Last, Kondensatoren halten die Ladung zwischen den Spitzen fest und glätten oder stapeln so die Spannung, und jede leitende Diode kostet ihre Durchlassspannung.**

Vorausgesetzt werden [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html), die Ersatzschaltungen aus [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html) und der [Kondensator](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/kondensator-und-kapazitaet.html).

:::grafik
Szene: get1/halbleiterbauelemente/04-bruecke-strompfade · Vorlage: schaltung-strompfade
**Abbildung 1:** Brückenschaltung nach Graetz mit Wechselspannungsquelle (10 V Scheitelwert), vier Dioden und Lastwiderstand. (a) In der positiven Halbwelle fließt der Strom über D1, die Last und D3; (b) in der negativen über D4, die Last und D2. Durch die Last fließt er in beiden Halbwellen in derselben Richtung.
:::

## Die Brückenschaltung nach Graetz

*Wie macht man aus beiden Halbwellen einen Strom, der die Last immer in derselben Richtung durchfließt?*

**Die Akteure:**

- __$u_e$__: Eingangsspannung, eine Sinusspannung mit dem Scheitelwert $\hat u_e$ = 10 V und 50 Hz.
- __$u_a$__: Spannung an der Last.
- __$U_{F0}$__: Durchlassspannung im Ersatzschaltbild, hier 0,6 V.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: In der positiven Halbwelle leiten D1 und D3, der Strom fließt über D1 von oben in die Last und über D3 zurück; D2 und D4 sperren (Abbildung 1a).

**Schritt 2**: In der negativen Halbwelle leiten D4 und D2: Der Strom fließt über D4 wieder von oben in die Last und über D2 zurück (Abbildung 1b). Die Last sieht in beiden Halbwellen dieselbe Polung, den Betrag der Eingangsspannung; deshalb heißt die Schaltung __Doppelweggleichrichter__. Ein __Einweggleichrichter__ mit einer Diode nutzt nur die positiven Halbwellen.

**Schritt 3**: In jedem Strompfad liegen zwei leitende Dioden in Reihe. Am Ausgang fehlen deshalb 1,2 V, und solange der Betrag der Eingangsspannung unter 1,2 V liegt, sperren alle vier (Abbildung 2).

:::formel Formel
$$\hat u_a = \hat u_e - 2\,U_{F0}$$

$$u_a = |u_e| - 2\,U_{F0} \quad\text{für } |u_e| > 2\,U_{F0}, \qquad u_a = 0 \quad\text{sonst}$$
:::

**So liest man das:** Die Spitze am Ausgang ist um zwei Durchlassspannungen kleiner, 8,8 V statt 10 V. Um jeden Nulldurchgang gibt es eine __Totzone__ von 0,77 ms, in der kein Strom fließt.

**Kurz gesagt:** Bei vier gleichen Dioden ändert sich an der Last nichts, wenn man die beiden Anschlüsse der Quelle vertauscht; es zählt nur der Betrag der Eingangsspannung.

Idee der Herleitung: Maschenregel entlang des Strompfads mit zwei leitenden Dioden im Modell mit Durchlassspannung.

:::herleitung
**Ausgangspunkt:** die Maschenregel ([Kirchhoffsche Gesetze](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/kirchhoffsche-gesetze.html)) und das Modell mit Durchlassspannung aus [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html): Eine leitende Diode ist eine Quelle $U_{F0}$, eine sperrende eine Unterbrechung.

**Annahmen:** (i) Modell mit $U_{F0}$; (ii) die Quelle hat keinen Innenwiderstand; (iii) die Last ist ohmsch.

**Schritt 1**: Positive Halbwelle, Annahme: D1 und D3 leiten, D2 und D4 sperren. Maschenregel entlang Quelle, D1, Last, D3:

$$u_e = U_{F0} + u_a + U_{F0} \quad\Rightarrow\quad u_a = u_e - 2\,U_{F0}$$

**Schritt 2** (entscheidender Schritt): Probe. Der Strom durch die Last und damit durch D1 und D3 ist $u_a/R$; er ist positiv, solange $u_e$ größer als $2U_{F0}$ ist. An D2 und D4 liegt dann die Spannung $-(u_a + U_{F0})$, also negativ: Sie sperren, die Annahme stimmt.

**Schritt 3**: Negative Halbwelle: Mit D2 und D4 ergibt dieselbe Masche, mit vertauschter Rolle der Eingänge,

$$u_a = -u_e - 2\,U_{F0}$$

Beides zusammen ist der Betrag der Eingangsspannung minus zwei Durchlassspannungen. Ist der Betrag kleiner als zwei Durchlassspannungen, ergäbe sich ein negativer Strom durch die angeblich leitenden Dioden; dann sperren alle vier, und die Ausgangsspannung ist null.

**Ergebnis:**

$$\hat u_a = \hat u_e - 2\,U_{F0}$$

$$u_a = |u_e| - 2\,U_{F0} \quad\text{für } |u_e| > 2\,U_{F0}, \qquad u_a = 0 \quad\text{sonst}$$

**Woher die Faktoren kommen:** Die 2 zählt die beiden Dioden, die in jedem Strompfad in Reihe liegen; der Betrag entsteht, weil die Brücke die Polung der negativen Halbwelle umkehrt.

**Proben:** Mit idealen Dioden ist die Ausgangsspannung der Betrag der Eingangsspannung. Mit 0,6 V: Spitze 8,8 V. Mit zwei Beispieldioden und ihrer exakten Kennlinie an 1 kΩ ergeben sich 8,60 V, weil bei 8,6 mA jede 0,70 V braucht.

**Grenzen:** Bei großen Strömen kommen Bahnwiderstände und der Innenwiderstand der Quelle hinzu; Gleichrichterdioden wie die 1N4001 haben bei 1 A bis zu 1,1 V.
:::

:::grafik
Szene: get1/halbleiterbauelemente/04-bruecke-zeitverlauf · Vorlage: zeitverlauf
**Abbildung 2:** Eingangsspannung (gestrichelt, Scheitelwert 10 V) und Ausgangsspannung der Brücke über 40 ms. Der Ausgang ist der Betrag des Eingangs minus 1,2 V, mit der Spitze 8,8 V und einer Totzone von 0,77 ms um jeden Nulldurchgang; die waagrechte Linie zeigt den Mittelwert von 5,21 V.
:::

:::frage
„Warum braucht man vier Dioden? Zwei würden doch reichen.“
Mit zwei Dioden geht es auch, aber nur mit einem Transformator, dessen Ausgangswicklung eine Mittelanzapfung hat (Mittelpunktschaltung); jede Halbwelle nutzt dann nur die halbe Wicklung. Die Brücke braucht keine Anzapfung und nutzt die ganze Wicklung; der Preis sind zwei Durchlassspannungen statt einer.
:::

:::fehlvorstellung
„Hinter dem Brückengleichrichter liegt eine Gleichspannung von 10 V.“
Das liegt nahe, weil die Spannung an der Last ihr Vorzeichen nicht mehr wechselt. Sie pulsiert aber zwischen null und 8,8 V im Takt von 100 Hz; ihr Mittelwert, den ein Multimeter im Gleichspannungsbereich anzeigt, liegt bei 5,21 V. Eine annähernd konstante Spannung entsteht erst mit einem Ladekondensator.
:::

## Glättung mit dem Ladekondensator

*Wie wird aus der pulsierenden Spannung eine fast konstante?*

:::grafik
Szene: get1/halbleiterbauelemente/04-glaettung · Vorlage: schaltung-und-zeitverlauf
**Abbildung 3:** (a) Brücke mit Ladekondensator 470 µF parallel zur Last 470 Ω; die Quelle hat 5 Ω Innenwiderstand. (b) Oben die Kondensatorspannung zwischen 8,05 und 8,34 V, gestrichelt der Betrag der Eingangsspannung minus 1,2 V; unten der Diodenstrom: Pulse von 2,2 ms mit 118 mA Spitze, dazu der Laststrom von 17,4 mA. Der Kondensator wird nur kurz um die Spitzen nachgeladen und speist die Last dazwischen allein.
:::

**Die Akteure:**

- __$C$__: __Ladekondensator__ parallel zur Last; 470 µF im Beispiel.
- __$I_L$__: Laststrom, fast konstant; 17,4 mA.
- __$\Delta U$__: __Brummspannung__, die Schwankung der geglätteten Spannung von Spitze zu Spitze.
- __$f$__: Netzfrequenz, 50 Hz; die Brücke liefert zwei Pulse je Periode.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Nahe jeder Spitze liegt der Betrag der Eingangsspannung um mehr als 1,2 V über der Kondensatorspannung; dann leiten zwei Dioden und laden den Kondensator nach.

**Schritt 2**: Kurz nach der Spitze sinkt der Betrag der Eingangsspannung unter die Kondensatorspannung plus 1,2 V, und alle Dioden sperren. Bis zur nächsten Spitze speist der Kondensator die Last allein, seine Spannung sinkt fast linear um die Brummspannung.

**Schritt 3**: Die Ladung für die ganze Halbperiode muss in den kurzen Ladephasen nachfließen. Die Dioden führen deshalb keinen gleichmäßigen Strom, sondern Pulse von gut 2 ms mit dem Siebenfachen des Laststroms (Abbildung 3b).

:::formel Formel
$$\Delta U \approx \frac{I_L}{2\,f\,C}$$
:::

**So liest man das:** Doppelter Laststrom gibt doppelten Brumm, doppelte Kapazität den halben. Die Formel ist eine obere Schätzung, weil sie annimmt, dass der Kondensator die ganze Halbperiode entladen wird; beim Einweggleichrichter steht $f$ statt $2f$ im Nenner.

Idee der Herleitung: Zwischen zwei Ladepulsen gibt der Kondensator den Laststrom ab; die Spannung sinkt um Ladung durch Kapazität.

:::herleitung
**Ausgangspunkt:** die Beziehung zwischen Strom und Spannung am Kondensator ([Kondensator und Kapazität](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/kondensator-und-kapazitaet.html)):

$$i_C = C\,\frac{\mathrm{d}u_C}{\mathrm{d}t}$$

**Annahmen:** (i) Die Brummspannung ist klein gegen die Ausgangsspannung; der Laststrom ist deshalb fast konstant $I_L$. (ii) Die Ladephasen sind kurz; der Kondensator entlädt sich höchstens eine halbe Netzperiode lang, $1/(2f)$.

**Schritt 1**: Während die Dioden sperren, fließt der Laststrom allein aus dem Kondensator:

$$C\,\frac{\mathrm{d}u_C}{\mathrm{d}t} = -I_L$$

**Schritt 2** (entscheidender Schritt): Bei konstantem Strom sinkt die Spannung linear; über die Entladezeit $1/(2f)$ um

$$\Delta U = \frac{I_L}{C}\cdot\frac{1}{2\,f}$$

**Ergebnis:**

$$\Delta U \approx \frac{I_L}{2\,f\,C}$$

**Woher die Faktoren kommen:** $I_L/C$ ist die Geschwindigkeit, mit der die Spannung sinkt; $1/(2f)$ ist die Zeit zwischen zwei Pulsen der Brücke.

**Proben:** Einheit A durch Hz mal F ergibt A s durch F, also V. Zahlenwert: 17,4 mA durch 100 Hz mal 470 µF ergibt 0,37 V. Die Simulation liefert 0,29 V: Der Kondensator entlädt sich nicht 10 ms, sondern nur etwa 7,8 ms, solange die Dioden sperren, und 0,37 V mal 0,78 ergibt 0,29 V.

**Grenzen:** Bei großem Brumm sinkt der Laststrom mit der Spannung, und die Ladephasen werden lang; die Schätzung wird dann ungenau.
:::

::::beispiel Ladekondensator für ein kleines Netzteil
**Gegeben:** Quelle mit 10 V Scheitelwert, 50 Hz und 5 Ω Innenwiderstand; Brücke im 0,6 V-Modell; Last 470 Ω; Ladekondensator 470 µF; die Werte stammen aus einer Schaltungssimulation.

**Gesucht:** Brummspannung nach der Schätzung und nach der Simulation; Kapazität für 0,1 V Brumm.

**Rechnung:** Die Simulation ergibt im Mittel 8,19 V, also 17,4 mA Laststrom, und eine Kondensatorspannung zwischen 8,05 und 8,34 V. Schätzung:

$$\Delta U \approx \frac{17{,}4\ \mathrm{mA}}{2\cdot50\ \mathrm{Hz}\cdot470\ \mu\mathrm{F}} = 0{,}37\ \mathrm{V}$$

Für 0,1 V Brumm braucht man nach der Schätzung

$$C = \frac{17{,}4\ \mathrm{mA}}{2\cdot50\ \mathrm{Hz}\cdot0{,}1\ \mathrm{V}} = 1740\ \mu\mathrm{F}$$

**Ergebnis:** **Brumm 0,29 V nach der Simulation, 0,37 V nach der Schätzung; für 0,1 V nach der Schätzung rund 1700 µF, nach der Simulation genügen rund 1400 µF.**

**Einordnung:** Die Schätzung liegt höher, weil sich der Kondensator nur etwa 7,8 von 10 ms entlädt; in der übrigen Zeit leiten die Dioden, mit bis zu 118 mA.
::::

## Die Ladungspumpe

*Wie kann eine Schaltung aus 5 V fast das Doppelte machen?*

:::grafik
Szene: get1/halbleiterbauelemente/04-ladungspumpe-takte · Vorlage: schaltung-zustaende
**Abbildung 4:** Die Ladungspumpe mit 5 V Eingangsspannung. (a) Takt 1: Die Unterseite von C1 liegt an Masse, über D1 und R1 lädt C1 auf 4,4 V. (b) Takt 2: Die Unterseite von C1 liegt an 5 V, seine Oberseite damit auf 9,4 V; D1 sperrt, über R2 und D2 fließt Ladung in C2, der sich 8,8 V nähert. Der geladene Kondensator wird auf die Eingangsspannung gestapelt.
:::

**Die Akteure:**

- __$U_e$__: Eingangsspannung, 5 V.
- __$C_1$__, __$C_2$__: __Pumpkondensator__, der abwechselnd geladen und gestapelt wird, und __Ausgangskondensator__; je 1 µF.
- __$f$__: Taktfrequenz des Umschalters, 10 kHz. Eine __Periode__ von 100 µs besteht aus Takt 1 und Takt 2 mit je 50 µs; in der Praxis schalten Transistoren.
- __$R_1$__, __$R_2$__: Widerstände, die die Ströme beim Umladen begrenzen; mit 10 Ω ist die Zeitkonstante 10 µs, kurz gegen einen Takt.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: In Takt 1 liegt die Unterseite von C1 an Masse, und die Quelle lädt C1 über D1 und R1 auf 5 V minus die Durchlassspannung, 4,4 V.

**Schritt 2**: In Takt 2 legt der Umschalter die Unterseite von C1 an die 5 V. Der geladene Kondensator steht damit auf der Quelle, seine Oberseite liegt bei 9,4 V; D1 sperrt, weil ihre Kathode nun höher liegt als ihre Anode. Achtung: Die Unterseite von C1 darf nicht zusätzlich fest mit Masse verbunden sein, sonst schlösse der Umschalter in Takt 2 die Quelle kurz.

**Schritt 3**: Über R2 und D2 fließt Ladung von C1 nach C2, bis die Oberseite von C1 nur noch eine Durchlassspannung über C2 liegt. Periode für Periode nähert sich C2 dem Endwert 8,8 V. Mit idealen Dioden wäre der Endwert das Doppelte der Eingangsspannung; mit Durchlassspannungen sind es 8,8 V statt 10 V.

**Schritt 4**: Zieht eine Last Strom, muss C1 jede Periode die verbrauchte Ladung nachliefern und sich dafür weiter entladen; der Ausgang bleibt unter dem Endwert. D2 bleibt dabei nach dem Ausgleich leitend, und bis zum Ende von Takt 2 speisen C1 und C2 die Last gemeinsam; in Takt 1 speist C2 sie allein.

:::formel Formel
$$U_a = 2\,U_e - 2\,U_{F0} - \frac{I_L}{f\,C_1}$$
:::

**So liest man das:** Die Formel gibt die Spannung an C2 am Ende von Takt 2. Ohne Last ist sie das Doppelte der Eingangsspannung abzüglich zweier Durchlassspannungen. Last zieht sie herunter, als hätte die Pumpe einen Innenwiderstand $1/(f\,C_1)$, bei 10 kHz und 1 µF 100 Ω.

Idee der Herleitung: Ladungserhaltung beim Ausgleich zwischen C1 und C2 und Ladungsbilanz je Periode.

:::herleitung
**Ausgangspunkt:** die Maschenregel, die Beziehung zwischen Ladung und Spannung am Kondensator und die Erhaltung der Ladung beim Umladen.

**Annahmen:** (i) Modell mit Durchlassspannung $U_{F0}$; (ii) jeder Takt dauert lang gegen die Zeitkonstanten, die Kondensatoren gleichen sich vollständig aus; (iii) im eingeschwungenen Zustand hat C2 am Ende jeder Periode wieder dieselbe Spannung.

**Schritt 1**: Takt 1, Masche aus Quelle, D1 und C1:

$$U_{C1} = U_e - U_{F0}$$

**Schritt 2**: Takt 2: Die Oberseite von C1 liegt auf $U_e + U_{C1}$. D2 leitet, solange diese Spannung um mehr als $U_{F0}$ über $U_{C2}$ liegt. Fließt dabei die Ladung $\Delta Q$, sinkt $U_{C1}$ um $\Delta Q/C_1$ und $U_{C2}$ steigt um $\Delta Q/C_2$. Der Ausgleich endet, wenn

$$U_e + U_{C1} - \frac{\Delta Q}{C_1} = U_{C2} + \frac{\Delta Q}{C_2} + U_{F0}$$

**Schritt 3**: Mit Schritt 1 und dem Endwert $U^* = 2U_e - 2U_{F0}$ aufgelöst:

$$\Delta Q\,\Big(\frac{1}{C_1} + \frac{1}{C_2}\Big) = U^* - U_{C2}$$

Ohne Last wächst $U_{C2}$ damit je Periode um den Anteil $C_1/(C_1 + C_2)$ des Abstands zu $U^*$, bei gleichen Kapazitäten um die Hälfte.

**Schritt 4**: Mit Last bleibt D2 nach dem Ausgleich leitend, denn die Last senkt $U_{C2}$ weiter, und an D2 läge sonst mehr als $U_{F0}$. Am Ende von Takt 2 gilt deshalb die Masche über Quelle, C1, D2 und C2:

$$U_a = U_e + U_{C1,\mathrm{Ende}} - U_{F0}$$

**Schritt 5** (entscheidender Schritt): Ladungsbilanz. Weil C2 am Ende jeder Periode wieder dieselbe Spannung hat, fließt die ganze Ladung, die die Last in einer Periode verbraucht, in Takt 2 über D2 aus C1:

$$\Delta Q = \frac{I_L}{f}$$

C1 beginnt Takt 2 mit $U_e - U_{F0}$ und verliert diese Ladung:

$$U_{C1,\mathrm{Ende}} = U_e - U_{F0} - \frac{I_L}{f\,C_1}$$

In Schritt 4 eingesetzt:

$$U_a = U_e + \Big(U_e - U_{F0} - \frac{I_L}{f\,C_1}\Big) - U_{F0}$$

**Ergebnis:**

$$U_a = 2\,U_e - 2\,U_{F0} - \frac{I_L}{f\,C_1}$$

**Woher die Faktoren kommen:** Die 2 vor $U_e$ entsteht durch das Stapeln von C1 auf die Quelle, die 2 vor $U_{F0}$ durch die beiden Dioden; $I_L/(f\,C_1)$ ist die Spannung, um die C1 sich je Periode entladen muss, um die Ladung der Last zu liefern.

**Proben:** Ohne Last: 8,8 V. Mit 1 mA, 10 kHz und 1 µF: 0,1 V weniger, 8,7 V am Ende von Takt 2. Eine Rechnung Takt für Takt ergibt nach dem Einschwingen genau diesen Wert und dazu den Verlauf: In Takt 1 fällt der Ausgang um 0,05 V auf 8,65 V, beim Ausgleich springt er auf 8,725 V, im Rest von Takt 2 fällt er um 0,025 V zurück auf 8,70 V. Einheit: A durch Hz mal F ergibt V.

**Grenzen:** Sind die Zeitkonstanten nicht kurz gegen einen Takt, gleichen sich die Kondensatoren nicht vollständig aus, und der Ausgang sinkt weiter; mit den 10 Ω des Beispiels liegt er im Mittel bei 8,68 statt 8,69 V. Reale Dioden haben bei kleinen Strömen kleinere Durchlassspannungen als 0,6 V.
:::

:::frage
„Warum ist C2 nicht schon nach der ersten Periode voll?“
Weil sich C1 und C2 die Ladung teilen: Fließt Ladung von C1 nach C2, sinkt die Spannung an C1 und steigt die an C2, bis beide über die Diode ausgeglichen sind. Bei gleichen Kapazitäten schafft jede Periode deshalb nur die Hälfte des verbleibenden Abstands. Im allerersten Takt 1 lädt die Quelle C2 über D2 schon auf 3,8 V; am Ende der Perioden folgen 6,3 V, 7,55 V, 8,18 V und so weiter, nach zehn Perioden fehlen noch 5 mV.
:::

::::beispiel Ladungspumpe an 5 V unter Last
**Gegeben:** Eingangsspannung 5 V; 0,6 V-Modell für beide Dioden; C1 = C2 = 1 µF; Taktfrequenz 10 kHz; Last 1 mA.

**Gesucht:** Ausgangsspannung und Strom aus der Quelle.

**Rechnung:** Endwert ohne Last und Ausgang unter Last nach Formel 3:

$$U^* = 2\cdot5\ \mathrm{V} - 2\cdot0{,}6\ \mathrm{V} = 8{,}8\ \mathrm{V}, \qquad U_a = 8{,}8\ \mathrm{V} - \frac{1\ \mathrm{mA}}{10\ \mathrm{kHz}\cdot1\ \mu\mathrm{F}} = 8{,}7\ \mathrm{V}$$

Die 8,7 V gelten am Ende von Takt 2. In Takt 1 speist C2 die Last allein, seine Spannung sinkt um 0,05 V auf 8,65 V; beim Ausgleich springt sie auf 8,725 V, danach speisen C1 und C2 gemeinsam, bis sie am Ende von Takt 2 wieder bei 8,7 V liegt. Je Periode fließen 100 nC zur Last; die Quelle liefert sie zweimal, in C1 und durch C1 nach C2, also im Mittel 2 mA.

**Ergebnis:** **Ausgang zwischen 8,65 und 8,725 V, am Ende von Takt 2 8,7 V, bei 2 mA aus der Quelle.**

**Einordnung:** Die Quelle gibt 10 mW ab, am Ausgang kommen im Mittel 8,69 mW an; den Rest verbrauchen die Dioden mit 1,2 mW und das Umladen über die Widerstände mit 0,11 mW.
::::

:::fehlvorstellung
„Die Ladungspumpe gewinnt Leistung, weil sie die Spannung verdoppelt.“
Das liegt nahe, weil am Ausgang fast die doppelte Spannung anliegt. Die Quelle liefert aber auch den doppelten Strom, weil jede Ladung, die zur Last fließt, zweimal aus ihr kommt. Im Beispiel stehen 10 mW aus der Quelle 8,69 mW an der Last gegenüber.
:::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Brückenschaltung | Vier Ventile lenken beide Halbwellen in dieselbe Richtung durch die Last. |
| 1,2 V Verlust und Totzone | Jede leitende Diode kostet ihre Durchlassspannung, im Pfad liegen zwei. |
| Ladekondensator und Brumm | Der Kondensator hält die Ladung von Spitze zu Spitze; die Dioden sperren dazwischen. |
| Ladungspumpe | Ventile und Umschalter stapeln einen geladenen Kondensator auf die Quelle. |
| Energiebilanz | Stapeln verdoppelt die Spannung, nicht die Leistung. |

Eine Diode lässt Strom nur in eine Richtung: Gleichrichter lenken damit beide Halbwellen in derselben Richtung durch die Last, Kondensatoren halten die Ladung zwischen den Spitzen fest und glätten oder stapeln so die Spannung, und jede leitende Diode kostet ihre Durchlassspannung.

## Bedeutung und Ausblick

Die meisten Netzteile mit Transformator beginnen mit Brücke und Ladekondensator; Ladungspumpen erzeugen Hilfsspannungen in Schnittstellen- und Speicherchips. Der nächste Artikel, [Aufbau und Wirkungsweise des Bipolartransistors](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html), setzt zwei pn-Übergänge zu einem Verstärker zusammen.

**In der ausführlichen Fassung:** der Mittelwert gleichgerichteter Spannungen mit Herleitung, die Sperrspannung der Dioden, die Simulation der Glättung mit Stromflusswinkel und Spitzenströmen für verschiedene Kondensatoren, der Einschaltstrom, das Aufladen der Ladungspumpe Periode für Periode und die Wahl des Pumpkondensators. [Zur ausführlichen Fassung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/gleichrichtung-und-ladungspumpe-ausfuehrlich.html)

:::kern
- In der Brücke leiten je Halbwelle zwei Dioden in Reihe; der Strom durchfließt die Last immer in derselben Richtung.
- Ausgang ohne Glättung: $u_a = |u_e| - 2U_{F0}$; um jeden Nulldurchgang sperren alle Dioden.
- Ein Ladekondensator hält die Ladung von Spitze zu Spitze; dazwischen sperren die Dioden, und er speist die Last allein.
- Brummspannung: $\Delta U \approx I_L/(2fC)$ als obere Schätzung; die Dioden leiten nur kurz, mit Spitzenströmen weit über dem Laststrom.
- Ladungspumpe: Takt 1 lädt den Pumpkondensator, Takt 2 stapelt ihn auf die Eingangsspannung; der Ausgang strebt gegen $2U_e - 2U_{F0}$.
- Unter Last: $U_a = 2U_e - 2U_{F0} - I_L/(fC_1)$; die Quelle liefert den doppelten Strom, Leistung entsteht keine.
:::

:::quiz
F: Warum fließt der Strom in der Brückenschaltung in beiden Halbwellen in derselben Richtung durch die Last?
A: In der positiven Halbwelle leiten D1 und D3, in der negativen D2 und D4. Beide Paare führen den Strom zum selben Ende der Last, die Brücke kehrt die Polung der negativen Halbwelle um.
F: Warum ist die Spitze am Ausgang der Brücke 1,2 V kleiner als die Spitze am Eingang?
A: In jedem Strompfad liegen zwei leitende Dioden in Reihe, jede mit 0,6 V im Modell mit Durchlassspannung. Aus 10 V werden 8,8 V.
F: Stimmt es, dass hinter einem Brückengleichrichter ohne Kondensator eine Gleichspannung liegt?
A: Nein. Die Spannung wechselt ihr Vorzeichen nicht mehr, pulsiert aber zwischen null und 8,8 V im Takt von 100 Hz; ihr Mittelwert liegt bei 5,21 V.
F: Warum leiten die Dioden mit Ladekondensator nur kurz?
A: Weil sie nur leiten, solange der Betrag der Eingangsspannung um mehr als 1,2 V über der Kondensatorspannung liegt, und das ist nur kurz um die Spitzen der Fall. Im Beispiel gut 2 ms je Halbwelle.
F: Stimmt es, dass die Ladungspumpe Leistung gewinnt, weil sie die Spannung fast verdoppelt?
A: Nein. Die Quelle liefert jede Ladung zweimal, ihr Strom ist doppelt so groß wie der Laststrom. Im Beispiel stehen 10 mW aus der Quelle 8,69 mW am Ausgang gegenüber.
F: Wie stark sinkt die Ausgangsspannung der Ladungspumpe mit 10 kHz Taktfrequenz und 1 µF Pumpkondensator bei 1 mA Last?
A: Um den Laststrom geteilt durch Taktfrequenz mal Pumpkapazität, 1 mA durch 10 kHz mal 1 µF, also um 0,1 V: von 8,8 auf 8,7 V am Ende von Takt 2.
:::
