---
title: Parasitäre Kapazitäten des MOSFET
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / MOS-Feldeffekttransistoren
order: 33030400
summary: Welche Kapazitäten zwischen den vier Anschlüssen eines MOSFET wirken, wie groß sie in den einzelnen Betriebsbereichen sind und warum die kleine Gate-Drain-Kapazität am Eingang einer Verstärkerstufe vervielfacht erscheint. Ausführliche Fassung mit der Gatekapazität vom gesperrten Zustand bis zur Inversion, der Herleitung der Aufteilung auf Source und Drain, Überlappung, Sperrschichtkapazitäten aus Fläche und Rand, Leitungskapazität mit Randfeld, Miller-Effekt und Miller-Kompensation, durchgerechnet am Beispieltransistor.
tags: MOS-Kapazität, Gate-Kapazität, Überlappkapazität, Sperrschichtkapazität
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Ein MOSFET nimmt am Gate keinen Gleichstrom auf, und doch braucht jede Änderung seiner Spannungen Strom: Unter dem Gate, im Kanal und an den pn-Übergängen von Source und Drain sitzen Ladungen, die sich mit den Spannungen ändern und dafür durch die Anschlüsse zu- oder abfließen müssen. Für die Schaltung wirken sie wie Kondensatoren zwischen den vier Anschlüssen, beim Beispieltransistor zwischen 3 fF und 53 fF. Sie bestimmen, wie schnell ein Knoten umgeladen werden kann, und damit die Schaltzeit digitaler Schaltungen und die __Bandbreite__ analoger, also die höchste Frequenz, die eine Stufe noch verstärkt. Alles hängt an einem Prinzip:

**Eine Kapazität im MOSFET ist die Ladung, die ein Anschluss je Volt Spannungsänderung liefern muss; ihr Wert hängt davon ab, wo die Gegenladung sitzt und aus welchem Anschluss sie nachfließt, und ihre Wirkung davon, um wie viel sich die Spannung über ihr tatsächlich ändert.**

Vorausgesetzt werden der MOS-Kondensator, die Oxidkapazität und die Schwellenspannung aus [Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html), der Kanal und seine Abschnürung aus [Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien-ausfuehrlich.html), der Kondensator aus [Kondensator und Kapazität](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/kondensator-und-kapazitaet.html) und die Sperrschichtkapazität aus [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie-ausfuehrlich.html). Auf diesem Artikel bauen das Kleinsignalmodell des MOSFET, der Frequenzgang der Transistorgrundschaltungen und die Schaltzeiten digitaler CMOS-Gatter auf.

:::grafik
Szene: st1/mos-feldeffekttransistoren/04-kapazitaeten-uebersicht · Vorlage: querschnitt-beschriftet
**Abbildung 1:** (a) Querschnitt des Beispiel-NMOS, schematisch: Das Gate liegt über 5 nm Oxid und ist 1,1 µm lang, der Kanal darunter 1 µm, sodass es Source und Drain je 50 nm überlappt. Arbeitspunkt $U_{GS}$ = 1 V, $U_{DS}$ = 1 V, Source und Bulk an Masse: Der Kanal endet als Keil vor dem Drain. Kapazitätssymbole an den Orten der Ladung, jeweils mit einer Linie zu dem Anschluss, aus dem die Gegenladung kommt: zwei Überlappungskapazitäten an den Gatekanten (je 3,45 fF), vom Gate zum Kanal $C_{GS}$ (46,0 fF) und $C_{GD}$ (0), durch die Verarmungszone zum Bulk $C_{GB}$ (praktisch 0), an Boden und Rand der n⁺-Gebiete $C_{SB}$ (53,1 fF) und $C_{DB}$ (37,8 fF). (b) Schaltzeichen mit den fünf Kapazitäten zwischen den Anschlüssen: $C_{GS}$ = 49,5 fF mit Überlappung, $C_{GD}$ = 3,45 fF, $C_{GB}$ ≈ 0, $C_{SB}$ = 53,1 fF, $C_{DB}$ = 37,8 fF. Zwischen allen vier Anschlüssen liegen Kapazitäten; ihr Wert hängt davon ab, wo die Ladung sitzt, und ändert sich mit dem Betriebsbereich.
:::

## Kapazitäten zwischen den Anschlüssen

*Was bedeutet Kapazität bei einem Bauelement mit vier Anschlüssen, dessen Ladungen nicht proportional zu den Spannungen wachsen?*

Am Beispieltransistor lässt sich das an einem Versuch ablesen. Er arbeitet mit $U_{GS}$ = 1 V und $U_{DS}$ = 1 V im Abschnürbereich, Source und Bulk liegen an Masse. Hebt man das Gate um 10 mV an, während Source, Drain und Bulk fest bleiben, fließen 0,53 fC in das Gate; es verhält sich für diese kleine Änderung wie ein Kondensator von 0,53 fC je 10 mV, also 53 fF. Hält man stattdessen das Gate fest und senkt die Source um 10 mV, fließen 0,495 fC in das Gate, senkt man den Drain, nur 0,035 fC, und senkt man den Bulk, praktisch nichts. Die 53 fF des Gates verteilen sich also auf die drei anderen Anschlüsse: 49,5 fF zur Source, 3,45 fF zum Drain, nichts zum Bulk.

In Worten: Die Kapazität zwischen dem Gate und einem anderen Anschluss ist die Änderung der Gateladung je Änderung der Spannung zwischen beiden, während die Spannungen zu den übrigen Anschlüssen fest bleiben. Man definiert sie so, weil man den Transistor in einer Schaltung durch Kondensatoren zwischen seinen Anschlüssen ersetzen will, und ein Kondensator zwischen Gate und Source nimmt genau dann Ladung auf, wenn sich die Spannung zwischen diesen beiden ändert.

**Die Akteure:**

- __$Q_G$__: Ladung auf dem Gate; in fC. Beim NMOS ist sie oberhalb der Flachbandspannung positiv; ihre Gegenladung liegt im Silizium darunter oder in den n⁺-Gebieten.
- __$U_{GD}$__, __$U_{GB}$__: Spannung vom Gate zum Drain bzw. zum Bulk, neben $U_{GS}$ die beiden anderen Spannungen am Gate; $U_{GD}$ ist $U_{GS} - U_{DS}$, im Arbeitspunkt oben 0 V, $U_{GB}$ ist dort 1 V.
- __$C_{GS}$__, __$C_{GD}$__, __$C_{GB}$__: Gate-Source-, Gate-Drain- und Gate-Bulk-Kapazität; in fF; im Arbeitspunkt oben 49,5 fF, 3,45 fF und praktisch 0. In Kleinsignal-Ersatzschaltbildern schreibt man sie auch mit kleinen Indizes, $C_{gs}$.
- __$C_G$__: Kapazität des ganzen Gates, die Änderung der Gateladung, wenn sich nur das Gatepotential ändert; 53 fF im Arbeitspunkt oben.

:::formel Definition
$$C_{GS} = \frac{\partial Q_G}{\partial U_{GS}}, \qquad C_{GD} = \frac{\partial Q_G}{\partial U_{GD}}, \qquad C_{GB} = \frac{\partial Q_G}{\partial U_{GB}}$$
:::

**So liest man das:** Jede der drei Kapazitäten ist eine partielle Ableitung, die Ableitung nach einer der drei Spannungen, während die beiden anderen fest bleiben; das Zeichen ∂ statt d erinnert daran, dass $Q_G$ von mehreren Spannungen abhängt. Die Kapazitäten gelten für kleine Änderungen um einen Arbeitspunkt und hängen von ihm ab, deshalb nennt man sie auch Kleinsignalkapazitäten. Ändert sich nur das Gatepotential, ändern sich alle drei Spannungen um denselben Betrag, und die Kapazität des ganzen Gates ist die Summe:

$$C_G = C_{GS} + C_{GD} + C_{GB}$$

**Kurz gesagt:** Die Kapazität des ganzen Gates ist die Summe seiner Kapazitäten zu den drei anderen Anschlüssen.

Idee der Herleitung: Man ändert nur das Gatepotential und zählt die Beiträge der drei Spannungen zusammen.

:::herleitung
**Ausgangspunkt:** die Definition der drei Kapazitäten als partielle Ableitungen der Gateladung nach $U_{GS}$, $U_{GD}$ und $U_{GB}$.

**Annahmen:**
(i) kleine Änderungen, sodass die Gateladung auf jede der drei Spannungen linear reagiert und sich die Beiträge addieren;
(ii) die Kapazitäten sind im Arbeitspunkt ausgewertet und während der kleinen Änderung fest.

**Schritt 1**: Ändern sich alle drei Spannungen ein wenig, ändert sich die Gateladung um die Summe der drei Beiträge:

$$\mathrm dQ_G = C_{GS}\,\mathrm dU_{GS} + C_{GD}\,\mathrm dU_{GD} + C_{GB}\,\mathrm dU_{GB}$$

**Schritt 2**: Steigt nur das Gatepotential um $\mathrm dU$, während Source, Drain und Bulk fest bleiben, wächst jede der drei Spannungen um $\mathrm dU$:

$$\mathrm dU_{GS} = \mathrm dU_{GD} = \mathrm dU_{GB} = \mathrm dU$$

**Schritt 3** (entscheidender Schritt): Eingesetzt in Schritt 1:

$$\mathrm dQ_G = \big(C_{GS} + C_{GD} + C_{GB}\big)\,\mathrm dU$$

**Ergebnis:**

$$C_G = \frac{\mathrm dQ_G}{\mathrm dU} = C_{GS} + C_{GD} + C_{GB}$$

**Woher die Faktoren kommen:** Jeder Summand gehört zu einem Anschlusspaar; die Summe entsteht, weil eine Bewegung des Gates die Spannung zu allen drei Anschlüssen gleichzeitig ändert.

**Proben:** Einheit fC/V = fF. Im Arbeitspunkt oben: 49,5 fF + 3,45 fF + 0 = 52,95 fF, und 52,95 fF · 10 mV = 0,53 fC, wie im Versuch. Grenzfall: Liegen Source, Drain und Bulk auf demselben Potential, ist $C_G$ die Kapazität des MOS-Kondensators.

**Grenzen:** Bei großen Spannungssprüngen ändern sich die Kapazitäten unterwegs; dann rechnet man mit den Ladungen selbst statt mit den Kapazitäten.
:::

:::frage
„Warum spricht man von einer Kapazität, obwohl die Ladung gar nicht proportional zur Spannung wächst?“
Für kleine Änderungen um einen Arbeitspunkt ist jede glatte Kurve fast eine Gerade, und ihre Steigung ist die Kapazität. Ein Signal von wenigen Millivolt sieht deshalb einen gewöhnlichen Kondensator, dessen Wert allerdings vom Arbeitspunkt abhängt. Über größere Bereiche ändert er sich stark: Die Gatekapazität des Beispieltransistors mit verbundener Source, Drain und Bulk beträgt bei 0 V das 0,30-Fache der Oxidkapazität, bei 0,35 V das 0,26-Fache und bei 1 V das 0,92-Fache (Abschnitt *Die Gatekapazität vom gesperrten Zustand bis zur Inversion*).
:::

Für die beiden pn-Übergänge gilt dasselbe mit der Ladung in ihren Raumladungszonen: $C_{SB}$ und $C_{DB}$ sind die Änderungen dieser Ladungen je Änderung von $U_{SB}$ bzw. $U_{DB}$. Insgesamt liegen zwischen den vier Anschlüssen sieben Kapazitäten:

| Kapazität | Ladung, Gegenladung und Abhängigkeit |
|---|---|
| $C_{GS}$, $C_{GD}$ | Gate über dem Kanal gegen die Kanalelektronen aus Source und Drain; hängt vom Betriebsbereich ab |
| $C_{GB}$ | Gate über dem Kanal gegen Akzeptorrümpfe und Löcher, die der Bulk liefert; stark von $U_{GS}$ abhängig, mit Kanal fast null |
| zwei $C_\mathrm{ov}$ | Überlappung: Gatekante gegen die Elektronen von Source bzw. Drain; fast konstant |
| $C_{SB}$, $C_{DB}$ | Raumladung um Source bzw. Drain gegen Akzeptorrümpfe am Rand zum Bulk; hängt von der Sperrspannung ab |

Die beiden Überlappungskapazitäten $C_\mathrm{ov}$, an den Kanten, wo das Gate über Source und Drain reicht, liegen zwischen denselben Anschlüssen wie $C_{GS}$ und $C_{GD}$ und addieren sich zu ihnen. Eine direkte Kapazität zwischen Source und Drain gibt es auch; sie ist gegen alle anderen klein und wird vernachlässigt.

## Die Gatekapazität vom gesperrten Zustand bis zur Inversion

*Wo sitzt die Gegenladung zur Gateladung, und warum hängt die Gatekapazität so stark von der Gatespannung ab?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/04-gatekapazitaet · Vorlage: kennlinie-anteile
**Abbildung 2:** Gatekapazität des Beispieltransistors bezogen auf $C_\mathrm{ox}$ = 69,1 fF über $U_{GS}$ von −2,5 V bis 2,5 V, Drain und Bulk auf dem Potential der Source. Obere Kante: gesamte Gatekapazität, 0,96 bei −2,5 V, 0,73 bei der Flachbandspannung −1,03 V, 0,30 bei 0 V, Minimum 0,26 bei 0,35 V, 0,40 an der Schwelle 0,5 V, 0,92 bei 1 V und 0,98 bei 2,5 V. Darunter als gestapelte Flächen der Bulkanteil $C_{GB}$ (grau), bis 0 V gleich der ganzen Kapazität, an der Schwelle 0,198 und bei 1 V 0,015, und der Kanalanteil $C_{GS} + C_{GD}$ (blau, je zur Hälfte Source und Drain), an der Schwelle ebenfalls 0,198, bei 1 V 0,907 und bei 2,5 V 0,976. Gestrichelt der MOS-Kondensator ohne Source und Drain bei hoher Frequenz, 0,25 an der Schwelle und 0,23 bei 2,5 V. Unterhalb der Schwelle liegt die Gegenladung im Bulk, oberhalb liefern Source und Drain die Elektronen; im Transistor kehrt die Gatekapazität deshalb auch bei hoher Frequenz auf $C_\mathrm{ox}$ zurück, und der Bulkanteil verschwindet.
:::

Liegen Source, Drain und Bulk auf demselben Potential, ist der Transistor ein MOS-Kondensator mit zwei n⁺-Gebieten am Rand. Seine Zustände sind aus [Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html) bekannt: __Anreicherung__, wenn Löcher an der Oberfläche angereichert sind, __Verarmung__, wenn sie von dort verdrängt sind und nur die ortsfesten, negativ geladenen Akzeptorrümpfe zurückbleiben, und __Inversion__, wenn sich Elektronen an der Oberfläche sammeln. Für die Kapazität zählt in jedem Zustand nur eines: wo die Gegenladung zu- und abfließt, wenn sich die Gatespannung ein wenig ändert.

**Die Akteure:**

- __$C'_\mathrm{ox}$__, __$C_\mathrm{ox}$__: Kapazität des Oxids pro Fläche bzw. über der ganzen Kanalfläche $W L$; 6,91 fF/µm² und 69,1 fF bei 5 nm Oxid und 10 µm². Der Strich kennzeichnet wie in den vorigen Artikeln einen auf die Fläche bezogenen Wert.
- __$U_\mathrm{FB}$__: __Flachbandspannung__, die Gatespannung, bei der die Siliziumoberfläche ungeladen ist; −1,03 V beim Gate aus n⁺-Polysilizium.
- __$y_d$__: Tiefe der Verarmungszone unter dem Gate; 35,9 nm bei $U_{GS}$ = 0 und 45,8 nm an der Schwelle nach der Verarmungsnäherung, die die Zone als scharf begrenzt und frei von Löchern annimmt.
- __$C_\mathrm{dep}$__: Kapazität der Verarmungszone unter dem Gate, $\varepsilon_\mathrm{Si} W L/y_d$; 28,9 fF bei $U_{GS}$ = 0.

**Das Zusammenspiel:** Unterhalb der Flachbandspannung sitzt die Gegenladung als Löcherschicht direkt unter dem Oxid, und die Löcher kommen über den Bulkanschluss. Die Kapazität ist dann fast die des Oxids, bei −2 V das 0,95-Fache, 65,4 fF; sie gehört ganz zu $C_{GB}$ (Abbildung 2, links).

In der Verarmung ändert eine kleine Gatespannung die Breite der Verarmungszone: Ladung kommt und geht an ihrem unteren Rand, $y_d$ tief im Silizium, wo der Bulk Löcher zuführt oder abzieht. Zwischen Gate und dieser Stelle liegen hintereinander das Oxid und die Zone, zwei Kondensatoren in Reihe, und die Kapazität sinkt. Bei $U_{GS}$ = 0 sind es nur noch 0,30 $C_\mathrm{ox}$, 20,7 fF. Ein gesperrter Transistor, dessen Gate auf 0 V liegt, belastet die treibende Stufe also mit knapp einem Drittel seiner Oxidkapazität.

$$C_{GB} = \frac{C_\mathrm{ox}\,C_\mathrm{dep}}{C_\mathrm{ox} + C_\mathrm{dep}}$$

**So liest man das:** Die Formel gilt in der Verarmung, zwischen der Flachbandspannung und dem Beginn der Inversion. Die Gate-Bulk-Kapazität ist kleiner als jede der beiden Teilkapazitäten; je tiefer die Zone, desto kleiner $C_\mathrm{dep}$ und damit $C_{GB}$.

**Kurz gesagt:** In der Verarmung addieren sich die Kehrwerte von Oxid- und Verarmungskapazität zum Kehrwert der Gate-Bulk-Kapazität.

Idee der Herleitung: Eine kleine Spannungsänderung teilt sich auf Oxid und Verarmungszone auf, und beide tragen dieselbe Ladungsänderung.

:::herleitung
**Ausgangspunkt:** die Spannungsbilanz des MOS-Kondensators aus [Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html): Die Gate-Bulk-Spannung ist die Flachbandspannung plus die Spannung über dem Oxid plus das Oberflächenpotential $\psi_s$, um das die Oberfläche höher liegt als das neutrale Innere; dazu die Verarmungsladung $W L\sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A\,\psi_s}$ mit der Dotierung $N_A$ unter dem Gate.

**Annahmen:**
(i) Verarmung: Die Gegenladung besteht nur aus Akzeptorrümpfen; Elektronen und Löcher an der Oberfläche sind vernachlässigbar;
(ii) Verarmungsnäherung: Die Zone ist scharf begrenzt;
(iii) kleine Änderungen.

**Schritt 1**: Eine kleine Änderung der Gatespannung teilt sich auf Oxid und Silizium auf; die Flachbandspannung ist fest:

$$\mathrm dU_{GB} = \mathrm dU_\mathrm{ox} + \mathrm d\psi_s$$

**Schritt 2**: Die Gateladung ändert sich um so viel wie die Ladung im Silizium; dieselbe Ladungsänderung $\mathrm dQ_G$ liegt über beiden Schichten:

$$\mathrm dU_\mathrm{ox} = \frac{\mathrm dQ_G}{C_\mathrm{ox}}, \qquad \mathrm d\psi_s = \frac{\mathrm dQ_G}{C_\mathrm{dep}}$$

**Schritt 3**: $C_\mathrm{dep}$ ist die Ableitung der Verarmungsladung nach dem Oberflächenpotential. Mit der Tiefe der Zone

$$y_d = \sqrt{\frac{2\,\varepsilon_\mathrm{Si}\,\psi_s}{e\,N_A}}$$

wird daraus ein Plattenkondensator:

$$\begin{aligned} C_\mathrm{dep} &= W L\,\frac{\mathrm d}{\mathrm d\psi_s}\sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A\,\psi_s} \\ &= W L\,\sqrt{\frac{e\,\varepsilon_\mathrm{Si}\,N_A}{2\,\psi_s}} = \frac{\varepsilon_\mathrm{Si}\,W L}{y_d} \end{aligned}$$

**Schritt 4** (entscheidender Schritt): Schritt 2 in Schritt 1 eingesetzt und durch $\mathrm dQ_G$ geteilt:

$$\frac{1}{C_{GB}} = \frac{\mathrm dU_{GB}}{\mathrm dQ_G} = \frac{1}{C_\mathrm{ox}} + \frac{1}{C_\mathrm{dep}}$$

**Ergebnis:**

$$C_{GB} = \frac{C_\mathrm{ox}\,C_\mathrm{dep}}{C_\mathrm{ox} + C_\mathrm{dep}}$$

**Woher die Faktoren kommen:** Die Reihenschaltung entsteht, weil beide Schichten dieselbe Ladungsänderung tragen; $C_\mathrm{dep}$ ist ein Plattenkondensator mit dem Abstand zwischen Oberfläche und Rand der Zone.

**Proben:** Einheit F. Bei $U_{GS}$ = 0 ergeben 69,06 fF und 28,9 fF in Reihe 20,4 fF, das 0,295-Fache von $C_\mathrm{ox}$; die vollständige Rechnung ohne Verarmungsnäherung ergibt 20,7 fF. Grenzfall: Geht $y_d$ gegen null, geht $C_{GB}$ gegen $C_\mathrm{ox}$.

**Grenzen:** Nahe der Flachbandspannung ist die Zone nicht scharf begrenzt, dort misst man 0,73 $C_\mathrm{ox}$ statt $C_\mathrm{ox}$; nahe der Schwelle tragen bereits Elektronen bei, und ein Teil der Kapazität gehört zu Source und Drain.
:::

::::beispiel Gatekapazität des gesperrten Beispieltransistors
**Gegeben:** Beispiel-NMOS mit $C_\mathrm{ox}$ = 69,06 fF, $W L$ = 10 µm², Dotierung unter dem Gate $N_A$ = 5,68·10¹⁷ cm⁻³, $\varepsilon_\mathrm{Si}$ = 1,036·10⁻¹² F/cm, $e$ = 1,602·10⁻¹⁹ C; bei $U_{GS}$ = 0 liegt die Oberfläche $\psi_s$ = 0,566 V über dem Inneren. Source, Drain und Bulk an Masse.

**Gesucht:** Tiefe der Verarmungszone, $C_\mathrm{dep}$ und $C_{GB}$ bei $U_{GS}$ = 0; Vergleich mit der Anreicherung.

**Rechnung:** Tiefe der Zone:

$$y_d = \sqrt{\frac{2\cdot1{,}036\cdot10^{-12}\ \mathrm{F/cm}\cdot0{,}566\ \mathrm V}{1{,}602\cdot10^{-19}\ \mathrm C\cdot5{,}68\cdot10^{17}\ \mathrm{cm^{-3}}}} = 3{,}59\cdot10^{-6}\ \mathrm{cm} = 35{,}9\ \mathrm{nm}$$

Kapazität der Zone über 10 µm² = 10⁻⁷ cm²:

$$C_\mathrm{dep} = \frac{1{,}036\cdot10^{-12}\ \mathrm{F/cm}\cdot10^{-7}\ \mathrm{cm^2}}{3{,}59\cdot10^{-6}\ \mathrm{cm}} = 28{,}9\ \mathrm{fF}$$

Reihenschaltung mit dem Oxid:

$$C_{GB} = \frac{69{,}06\ \mathrm{fF}\cdot28{,}9\ \mathrm{fF}}{69{,}06\ \mathrm{fF} + 28{,}9\ \mathrm{fF}} = 20{,}4\ \mathrm{fF}$$

**Ergebnis:** **$C_{GB}$ = 20,4 fF nach der Verarmungsnäherung, 20,7 fF nach der vollständigen Rechnung, also 0,30 $C_\mathrm{ox}$; in der Anreicherung bei −2 V dagegen 65,4 fF.**

**Einordnung:** Die Verarmungszone ist mit 36 nm siebenmal so dick wie das Oxid, hat aber die dreifache Permittivität; deshalb ist ihre Kapazität nur 2,4-mal kleiner als die des Oxids, und die Reihenschaltung landet bei knapp einem Drittel. Die volle Oxidkapazität erreicht ein gesperrter NMOS mit n⁺-Gate erst bei Gatespannungen deutlich unter −1 V, die in normalen Schaltungen nicht vorkommen.
::::

An der Schwelle beginnen sich Elektronen an der Oberfläche zu sammeln, und hier unterscheidet sich der Transistor vom MOS-Kondensator ohne Source und Drain. Beim Kondensator können die Elektronen nur durch Wärme entstehen, als Elektron-Loch-Paare in der Verarmungszone; beim Beispiel dauert der Aufbau der Inversionsschicht rund 90 s. Schon bei langsamen Messsignalen folgt ihre Zahl der Spannung nicht mehr, die Ladung pendelt weiter am Rand der Verarmungszone, und die Kapazität bleibt bei 0,23 bis 0,25 $C_\mathrm{ox}$ (Abbildung 2, gestrichelt). Im Transistor grenzen die n⁺-Gebiete von Source und Drain, die 10²⁰ Elektronen pro Kubikzentimeter enthalten, unmittelbar an den Kanal. Sie liefern die Elektronen über den Kanal nach, mit der Zeitkonstante aus Kanalwiderstand und Oxidkapazität: Bei $U_{GS}$ = 1 V hat der Kanal 1 kΩ, und 1 kΩ mal 69 fF ergibt 69 ps. Die Kapazität des Transistors kehrt deshalb oberhalb der Schwelle auf $C_\mathrm{ox}$ zurück, 0,92 $C_\mathrm{ox}$ bei 1 V und 0,98 $C_\mathrm{ox}$ bei 2,5 V, und das bis zu Frequenzen im Gigahertzbereich.

Zugleich wechselt der Ort der Gegenladung. Genau an der Schwelle teilt sich eine zusätzliche Gateladung je zur Hälfte auf die Verarmungszone und die Kanalelektronen auf, je 0,198 $C_\mathrm{ox}$. Darüber ist die Oberfläche an ihr Potential gebunden: Von 0,5 V auf 1 V Gatespannung steigt es nur um 105 mV, die Verarmungsladung wächst um 0,23 fC/µm², die Elektronenladung um 2,49 fC/µm². Bei 1 V kommen 98,3 % jeder zusätzlichen Gateladung aus Source und Drain, bei 1,5 V 99,4 %. Der Kanal schirmt den Bulk ab: $C_{GB}$ fällt praktisch auf null, und die Kapazität des Gates gehört nun zu Source und Drain.

## Überlappung und Randfeld des Gates

*Welche Kapazität bilden die Ränder des Gates über Source und Drain, und warum hängt sie nicht vom Kanal ab?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/04-ueberlappung · Vorlage: querschnitt-detail
**Abbildung 3:** Ausschnitt um die drainseitige Gatekante, in der Höhe gestreckt. Das n⁺-Draingebiet reicht 50 nm unter das Gate; dort laufen die Feldlinien dicht und parallel vom Gate durch das 5 nm dicke Oxid ins n⁺-Gebiet, ein Plattenkondensator von 3,45 fF bei 10 µm Weite. Dazu gebogene Feldlinien von der Flanke des Gates zur Oberfläche des Drains, das Randfeld. Links davon endet der Kanal abgeschnürt vor dem Drain. Die Überlappung ist ein kleiner Plattenkondensator zwischen Gate und Drain, den keine Abschnürung abschaltet.
:::

Das Gate ist etwas länger als der Kanal darunter und reicht auf beiden Seiten ein kleines Stück über Source und Drain, beim Beispieltransistor je 50 nm: 1,1 µm Gate über 1 µm Kanal. Über diesen Streifen liegt das Gate dem leitenden n⁺-Gebiet gegenüber, getrennt durch das Gateoxid, und bildet mit ihm einen Plattenkondensator. Seine Gegenladung sitzt an der Oberfläche des n⁺-Gebiets und kommt aus Source bzw. Drain, gleichgültig, ob unter dem Gate ein Kanal besteht und ob er abgeschnürt ist (Abbildung 3).

:::frage
„Warum überlappt das Gate Source und Drain überhaupt, wenn das nur Kapazität kostet?“
Source und Drain werden erst eingebracht, wenn das Gate schon steht: Man schießt die Dotierstoffe mit dem Gate als Maske ein, sodass die n⁺-Gebiete von selbst genau an den Gatekanten beginnen; ein solches Gate heißt __selbstjustiert__. Beim anschließenden Ausheilen bei rund 1000 °C wandern die Dotierstoffe ein Stück zur Seite und damit unter das Gate. Ohne diese Überlappung bliebe zwischen Kanal und n⁺-Gebiet ein Streifen, über dem kein Gate liegt; er würde nicht invertiert und trennte den Kanal vom Drain. Man hält die Überlappung deshalb klein, aber nicht null.
:::

**Die Akteure:**

- __$L_\mathrm{ov}$__: Länge, um die das Gate über Source bzw. Drain reicht (ov für englisch overlap); 50 nm je Seite.
- __$C_\mathrm{ov}$__: __Überlappungskapazität__ je Seite; 3,45 fF beim Beispieltransistor, 5 % von $C_\mathrm{ox}$. Sie liegt zwischen denselben Anschlüssen wie $C_{GS}$ bzw. $C_{GD}$ und addiert sich zu ihnen.

:::formel Formel
$$C_\mathrm{ov} = C'_\mathrm{ox}\,W\,L_\mathrm{ov}$$
:::

**So liest man das:** Die Überlappungskapazität ist die Oxidkapazität der Fläche $W L_\mathrm{ov}$. Sie wächst mit der Weite des Transistors, nicht mit seiner Länge; gemessen an der Oxidkapazität über dem Kanal ist sie $L_\mathrm{ov}/L$, beim Beispieltransistor 5 %. Weil das n⁺-Gebiet immer leitet, hängt sie kaum von den Spannungen ab. Hinzu kommt das Randfeld von der Flanke des Gates zur Oberfläche von Source und Drain; in Schaltungssimulatoren steht für beides zusammen ein Wert pro Weite, beim Beispiel 0,345 fF/µm (Parameter CGSO und CGDO).

Idee der Herleitung: Die Überlappung ist ein Plattenkondensator mit dem Gateoxid als Dielektrikum.

:::herleitung
**Ausgangspunkt:** die Kapazität des Plattenkondensators, Permittivität mal Fläche durch Plattenabstand, aus [Kondensator und Kapazität](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/kondensator-und-kapazitaet.html), und die Oxidkapazität pro Fläche $C'_\mathrm{ox}$ als Permittivität des Oxids durch seine Dicke.

**Annahmen:**
(i) Das n⁺-Gebiet unter der Gatekante ist leitend; seine Gegenladung sitzt an der Oberfläche, unmittelbar unter dem Oxid;
(ii) das Feld ist homogen, das Randfeld wird nicht mitgezählt.

**Schritt 1**: Die Platten sind das Gate und die Oberfläche des n⁺-Gebiets; ihre gemeinsame Fläche ist ein Streifen der Breite $W$ und der Länge $L_\mathrm{ov}$, ihr Abstand die Oxiddicke $t_\mathrm{ox}$.

**Schritt 2** (entscheidender Schritt): In die Formel des Plattenkondensators eingesetzt:

$$C_\mathrm{ov} = \frac{\varepsilon_\mathrm{ox}\,W\,L_\mathrm{ov}}{t_\mathrm{ox}} = C'_\mathrm{ox}\,W\,L_\mathrm{ov}$$

**Ergebnis:**

$$C_\mathrm{ov} = C'_\mathrm{ox}\,W\,L_\mathrm{ov}$$

**Woher die Faktoren kommen:** $C'_\mathrm{ox}$ ist dasselbe Oxid wie über dem Kanal; $W L_\mathrm{ov}$ ist die Fläche des Streifens.

**Proben:** Einheit fF/µm² · µm · µm = fF. Zahlenwert: 6,906 fF/µm² · 10 µm · 0,05 µm = 3,45 fF. Verhältnis zur Oxidkapazität des Kanals: 50 nm / 1 µm = 5 %.

**Grenzen:** Das Randfeld kommt hinzu und ist bei kurzen Überlappungen von ähnlicher Größe. Ist das Gebiet unter der Gatekante schwächer dotiert, kann es bei großer Spannung verarmen, und die Kapazität sinkt etwas.
:::

## Aufteilung der Kanalladung auf Source und Drain

*Welcher Teil der Gatekapazität gehört zur Source und welcher zum Drain, und warum hängt das vom Betriebsbereich ab?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/04-kanalladung-aufteilung · Vorlage: profil-folge
**Abbildung 4:** Elektronenladung pro Fläche im Kanal über dem Ort $x/L$ von der Source (0) zum Drain (1). (a) Ohmscher Bereich bei $U_{GS}$ = 1,5 V und kleiner Drain-Source-Spannung: gleichmäßig 6,91 fC/µm². Wird die Source um 10 mV angehoben, während Gate, Drain und Bulk fest bleiben, sinkt die Ladung an der Source um 0,069 fC/µm² und am Drain gar nicht, dazwischen linear; die Änderung beträgt im Mittel die Hälfte. Wird der Drain angehoben, gilt dasselbe gespiegelt. (b) Abschnürbereich bei $U_{GS}$ = 1 V und $U_{DS}$ = 1 V: Die Ladung fällt wie die Wurzel aus $1 - x/L$, 3,45 fC/µm² an der Source, 2,44 fC/µm² auf halber Länge und null am Ende des Kanals. Wird die Source um 10 mV angehoben, schrumpft das ganze Profil im selben Verhältnis, im Mittel um zwei Drittel des Werts an der Source; wird der Drain angehoben, ändert sich nichts. Eine Anschlussspannung ändert die Kanalladung nur dort, wo das Kanalpotential ihr folgt.
:::

**Die Akteure:**

- __$Q_K$__: Betrag der gesamten Elektronenladung im Kanal; in fC; bei $U_{GS}$ = 1 V 34,5 fC bei kleiner Drain-Source-Spannung und 23,0 fC im Abschnürbereich.
- __$U(x)$__: Kanalpotential an der Stelle $x$ gegenüber der Source, 0 an der Source; die Elektronenladung pro Fläche ist dort $C'_\mathrm{ox}$ mal der örtlichen __Übersteuerung__ $U_{GS} - U_{th} - U(x)$, um die das Gate die Schwelle gegenüber dem Kanal an dieser Stelle übersteigt ([Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien-ausfuehrlich.html)).
- __$U_{GD} - U_{th}$__: Übersteuerung am Drain-Ende; positiv, solange der Kanal den Drain erreicht, bei 1 V/1 V −0,5 V, der Kanal ist dort abgeschnürt.

**Das Zusammenspiel:**

**Schritt 1**: Oberhalb der Schwelle findet fast jede zusätzliche Gateladung ihre Gegenladung in den Kanalelektronen (Abschnitt *Die Gatekapazität vom gesperrten Zustand bis zur Inversion*). Jedes dieser Elektronen kommt aus der Source oder aus dem Drain, und wie viele aus welchem Anschluss kommen, legt $C_{GS}$ und $C_{GD}$ fest.

**Schritt 2**: Die Ladung an der Stelle $x$ folgt der örtlichen Übersteuerung. Eine Spannung an der Source oder am Drain ändert sie deshalb nur dort, wo sich das Kanalpotential mit dieser Spannung ändert.

**Schritt 3**: Im ohmschen Bereich bei kleiner Drain-Source-Spannung ist der Kanal überall gleich dick (Abbildung 4a). Hebt man die Source um 10 mV an, sinkt die Übersteuerung an der Source um 10 mV, am Drain gar nicht, und dazwischen geht die Änderung gleichmäßig auf null zurück. Im Mittel ändert sich die Ladung um die Hälfte: $C_{GS}$ ist die halbe Oxidkapazität, 34,5 fF. Vom Drain aus gesehen gilt dasselbe, und $C_{GD}$ ist ebenfalls 34,5 fF.

**Schritt 4** (entscheidender Schritt): Im Abschnürbereich endet der Kanal vor dem Drain am Abschnürpunkt, dessen Potential $U_{GS} - U_{th}$ über der Source liegt; den Rest der Drain-Source-Spannung nimmt die kurze verarmte Zone zwischen Abschnürpunkt und Drain auf ([Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien-ausfuehrlich.html)). Hebt man den Drain an, wächst nur die Spannung über dieser Zone; im Kanal ändert sich nichts. $C_{GD}$ ist null.

**Schritt 5**: Die Ladung fällt jetzt wie die Wurzel aus $1 - x/L$ von 3,45 fC/µm² an der Source auf null (Abbildung 4b). Hebt man die Source um 10 mV an, sinkt die Übersteuerung um 10 mV, und das ganze Profil schrumpft im selben Verhältnis. Der Mittelwert der Wurzel über den Kanal ist zwei Drittel: $C_{GS}$ ist $\tfrac23 C_\mathrm{ox}$, 46,0 fF. Bei 10 mV verlassen 0,46 fC den Kanal, 2874 Elektronen, die in die Source zurückfließen.

:::formel Formel
Ohmscher Bereich, kleine $U_{DS}$:

$$C_{GS} = C_{GD} = \frac{1}{2}\,C_\mathrm{ox}$$

Abschnürbereich:

$$C_{GS} = \frac{2}{3}\,C_\mathrm{ox}, \qquad C_{GD} = 0$$
:::

**So liest man das:** Eingabe ist der Betriebsbereich, Ausgabe der Anteil der Oxidkapazität, der zur Source bzw. zum Drain gehört; die Überlappung aus dem vorigen Abschnitt kommt jeweils hinzu. Im ohmschen Bereich ist der Kanal symmetrisch, und Source und Drain teilen sich seine Ladung. Im Abschnürbereich hängt die Kanalladung nur noch von $U_{GS}$ ab; sie beträgt zwei Drittel von $C_\mathrm{ox}(U_{GS} - U_{th})$, und die Gatekapazität ist ein Drittel kleiner als im ohmschen Bereich. Zum Bulk gehört in beiden Bereichen nichts, weil der Kanal ihn abschirmt.

**Kurz gesagt:** Ohne Kanallängenmodulation gibt es über den Kanal eine Kapazität zwischen Gate und Drain nur, solange der Kanal den Drain erreicht.

Idee der Herleitung: Man rechnet die gesamte Kanalladung aus, indem man statt über den Ort über das Kanalpotential integriert, und leitet sie nach den Spannungen an beiden Enden ab.

:::herleitung
**Ausgangspunkt:** die Stromgleichung des Kanals aus der Herleitung der Triodengleichung in [Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien-ausfuehrlich.html): Auf dem Stück $\mathrm dx$ steigt das Kanalpotential um $\mathrm dU$, und weil durch jeden Querschnitt derselbe Strom fließt, gilt

$$I_D\,\mathrm dx = \mu_n\,W\,C'_\mathrm{ox}\,\big(U_{GS} - U_{th} - U\big)\,\mathrm dU$$

**Annahmen:**
(i) das Modell der Kennlinien: Langkanal, Elektronenladung pro Fläche $C'_\mathrm{ox}$ mal örtliche Übersteuerung, konstante Beweglichkeit;
(ii) die Verarmungsladung unter dem Kanal ist fest; die Gateladung ändert sich dann genau um die Kanalladung, und zum Bulk gehört nichts;
(iii) quasistatisch: Die Kanalladung folgt den Spannungen ohne Verzögerung, also bei Änderungen, die langsam gegen die Laufzeit durch den Kanal sind, beim Beispieltransistor 92 ps;
(iv) zur Abkürzung die Übersteuerungen an Source und Drain-Ende; im Abschnürbereich endet der Kanal am Abschnürpunkt, dort ist die Übersteuerung null, gleichgültig, wo der Drain liegt:

$$U_{\text{ü}S} = U_{GS} - U_{th}, \qquad U_{\text{ü}D} = U_{GD} - U_{th}\ \ \text{bzw.}\ \ 0$$

**Schritt 1**: Nach Annahme (ii) sind die Kapazitäten die Ableitungen der Kanalladung:

$$C_{GS} = \frac{\partial Q_K}{\partial U_{GS}}, \qquad C_{GD} = \frac{\partial Q_K}{\partial U_{GD}}$$

**Schritt 2**: Die Kanalladung ist die Summe der Ladung über den Kanal:

$$Q_K = W \int_0^L C'_\mathrm{ox}\,\big(U_{GS} - U_{th} - U(x)\big)\,\mathrm dx$$

**Schritt 3**: Mit der Stromgleichung wird aus dem Integral über den Ort eines über das Kanalpotential; es läuft von 0 bis zum Potential am Ende des Kanals, $U_{GS} - U_{th} - U_{\text{ü}D}$:

$$Q_K = \frac{\mu_n\,W^2\,C'^2_\mathrm{ox}}{I_D}\int \big(U_{GS} - U_{th} - U\big)^2\,\mathrm dU$$

**Schritt 4**: Über den ganzen Kanal integriert, liefert die Stromgleichung auch den Strom:

$$I_D\,L = \mu_n\,W\,C'_\mathrm{ox}\int \big(U_{GS} - U_{th} - U\big)\,\mathrm dU$$

Teilt man Schritt 3 durch diesen Ausdruck, bleibt nur ein Verhältnis zweier Integrale:

$$Q_K = W L\,C'_\mathrm{ox}\,\frac{\int \big(U_{GS} - U_{th} - U\big)^2\,\mathrm dU}{\int \big(U_{GS} - U_{th} - U\big)\,\mathrm dU}$$

**Schritt 5**: Beide Integrale ausgerechnet; der Integrand fällt von $U_{\text{ü}S}$ an der Source auf $U_{\text{ü}D}$ am Ende des Kanals. Gekürzt wird mit

$$a^3 - b^3 = (a - b)\,\big(a^2 + ab + b^2\big), \qquad a^2 - b^2 = (a - b)\,(a + b)$$

und es bleibt:

$$\begin{aligned} Q_K &= W L\,C'_\mathrm{ox}\,\frac{\big(U_{\text{ü}S}^3 - U_{\text{ü}D}^3\big)/3}{\big(U_{\text{ü}S}^2 - U_{\text{ü}D}^2\big)/2} \\ &= \frac{2}{3}\,C_\mathrm{ox}\,\frac{U_{\text{ü}S}^2 + U_{\text{ü}S}\,U_{\text{ü}D} + U_{\text{ü}D}^2}{U_{\text{ü}S} + U_{\text{ü}D}} \end{aligned}$$

**Schritt 6** (entscheidender Schritt): Im Abschnürbereich ist $U_{\text{ü}D}$ null und hängt nicht von $U_{GD}$ ab. Es bleibt

$$Q_K = \frac{2}{3}\,C_\mathrm{ox}\,\big(U_{GS} - U_{th}\big) \quad\Rightarrow\quad C_{GS} = \frac{2}{3}\,C_\mathrm{ox}, \qquad C_{GD} = 0$$

**Schritt 7**: Im ohmschen Bereich lässt sich Schritt 5 in den Mittelwert der beiden Übersteuerungen und einen Rest zerlegen, der mit dem Quadrat ihrer Differenz $U_{DS}$ wächst:

$$Q_K = C_\mathrm{ox}\,\frac{U_{\text{ü}S} + U_{\text{ü}D}}{2} + C_\mathrm{ox}\,\frac{U_{DS}^2}{6\,\big(U_{\text{ü}S} + U_{\text{ü}D}\big)}$$

Bei kleinem $U_{DS}$ verschwindet der Rest samt seinen Ableitungen, und nach Schritt 1 ist

$$C_{GS} = C_{GD} = \frac{1}{2}\,C_\mathrm{ox}$$

**Ergebnis:** im ohmschen Bereich bei kleiner $U_{DS}$ je die halbe Oxidkapazität, im Abschnürbereich zwei Drittel zur Source und nichts zum Drain.

**Woher die Faktoren kommen:** Die 1/2 ist der Mittelwert einer Ladungsänderung, die von der Source zum Drain linear auf null fällt, die 2/3 der Mittelwert der Wurzel aus $1 - x/L$, des Ladungsprofils an der Abschnürgrenze; die Null entsteht, weil der Abschnürpunkt die Spannung des Drains vom Kanal fernhält.

**Proben:** Einheit fF. Bei $U_{GS}$ = 1 V im Abschnürbereich: $Q_K$ = 2/3 · 69,06 fF · 0,5 V = 23,0 fC, rund 144 000 Elektronen; bei kleiner $U_{DS}$ 34,5 fC. Grenzfall $U_{DS}$ = 0: $Q_K$ = $C_\mathrm{ox}(U_{GS} - U_{th})$, ein gleichmäßiger Kanal. An der Abschnürgrenze ist $U_{\text{ü}D}$ null, und beide Bereiche schließen stetig aneinander an.

**Grenzen:** Wächst die Verarmungsladung zum Drain hin, wie es der Substrateffekt verlangt, bleibt im Abschnürbereich ein kleiner Anteil beim Bulk, beim Beispieltransistor rund 8 % von $C_\mathrm{ox}$; dicht über der Schwelle sind alle Werte etwas kleiner, weil die Ladung dort langsamer als $C'_\mathrm{ox}$ mal Übersteuerung wächst.
:::

::::beispiel Kapazitäten des Beispieltransistors im Abschnürbereich und im ohmschen Bereich
**Gegeben:** Beispiel-NMOS mit $C_\mathrm{ox}$ = 69,06 fF, $U_{th}$ = 0,5 V, Überlappungskapazität $C_\mathrm{ov}$ = 3,45 fF je Seite, $e$ = 1,602·10⁻¹⁹ C; (a) $U_{GS}$ = 1 V, $U_{DS}$ = 1 V; (b) $U_{GS}$ = 1,5 V, $U_{DS}$ nahe 0.

**Gesucht:** $C_{GS}$ und $C_{GD}$ ohne und mit Überlappung; in (a) außerdem die Kanalladung und die Zahl der Elektronen, die in die Source zurückfließen, wenn sie um 10 mV angehoben wird.

**Rechnung:** (a) $U_{DS}$ = 1 V liegt über $U_{GS} - U_{th}$ = 0,5 V, der Transistor ist im Abschnürbereich:

$$C_{GS} = \frac{2}{3}\cdot69{,}06\ \mathrm{fF} = 46{,}0\ \mathrm{fF}, \qquad C_{GD} = 0$$

Mit den Überlappungen:

$$C_{GS} = 46{,}0\ \mathrm{fF} + 3{,}45\ \mathrm{fF} = 49{,}5\ \mathrm{fF}, \qquad C_{GD} = 3{,}45\ \mathrm{fF}$$

Kanalladung und Elektronen bei 10 mV:

$$Q_K = 46{,}0\ \mathrm{fF}\cdot0{,}5\ \mathrm V = 23{,}0\ \mathrm{fC}, \qquad \frac{46{,}0\ \mathrm{fF}\cdot10\ \mathrm{mV}}{1{,}602\cdot10^{-19}\ \mathrm C} = 2874$$

(b) Ohmscher Bereich bei kleiner $U_{DS}$:

$$C_{GS} = C_{GD} = \frac{1}{2}\cdot69{,}06\ \mathrm{fF} + 3{,}45\ \mathrm{fF} = 38{,}0\ \mathrm{fF}$$

**Ergebnis:** **(a) $C_{GS}$ = 49,5 fF, $C_{GD}$ = 3,45 fF, $Q_K$ = 23,0 fC, 2874 Elektronen; (b) je 38,0 fF.**

**Einordnung:** Im ohmschen Bereich hängt das Gate zu gleichen Teilen an Source und Drain, zusammen 76,0 fF. Im Abschnürbereich sinkt die Summe auf 53,0 fF, und zum Drain gehört nur noch die Überlappung, 7 % dessen, was zur Source gehört. Gerade diese kleine Gate-Drain-Kapazität verbindet in einer Verstärkerstufe den Ausgang mit dem Eingang.
::::

### Der Übergang zwischen ohmschem Bereich und Abschnürbereich

*Wie wandert die Kapazität vom Drain zur Source, wenn die Drain-Source-Spannung wächst?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/04-cgs-cgd-uds · Vorlage: kennlinie
**Abbildung 5:** $C_{GS}$ und $C_{GD}$ des Beispieltransistors über $U_{DS}$ von 0 bis 2 V bei $U_{GS}$ = 1,5 V, ohne Überlappung. $C_{GS}$ steigt von 34,5 fF über 40,9 fF bei 0,5 V auf 46,0 fF an der Abschnürgrenze bei 1 V, $C_{GD}$ fällt von 34,5 fF über 25,6 fF auf null; die Summe sinkt von 69,1 fF auf 46,0 fF und bleibt danach konstant. Gestrichelt dieselben Kurven mit je 3,45 fF Überlappung. Darüber kleine Bilder des Kanals bei 0, 0,5 V und 1 V. Mit wachsender Drain-Source-Spannung wandert die Gatekapazität vom Drain zur Source; ab der Abschnürgrenze gehört zum Drain nur noch die Überlappung.
:::

Zwischen beiden Grenzfällen geht die Aufteilung stetig über (Abbildung 5). Mit wachsender Drain-Source-Spannung wird der Kanal zum Drain hin dünner, der Drain erreicht weniger Ladung, und eine Änderung an der Source verschiebt mehr. Bei $U_{GS}$ = 1,5 V und $U_{DS}$ = 0,5 V gehören 40,9 fF zur Source und 25,6 fF zum Drain, an der Abschnürgrenze bei 1 V 46,0 fF und null. Die Ableitung der Kanalladung aus Schritt 5 der vorigen Herleitung ergibt den ganzen Verlauf; nach seinem Urheber heißt er __Meyer-Modell__:

$$\begin{aligned} C_{GS} &= \frac{2}{3}\,C_\mathrm{ox}\,\Big[1 - \Big(\frac{U_{GD} - U_{th}}{U_{GS} + U_{GD} - 2\,U_{th}}\Big)^2\Big] \\ C_{GD} &= \frac{2}{3}\,C_\mathrm{ox}\,\Big[1 - \Big(\frac{U_{GS} - U_{th}}{U_{GS} + U_{GD} - 2\,U_{th}}\Big)^2\Big] \end{aligned}$$

**So liest man das:** Die Formeln gelten im ohmschen Bereich, solange $U_{GD}$ über der Schwelle liegt; im Abschnürbereich gelten 2/3 und 0. Bei $U_{DS}$ = 0 ist $U_{GD}$ gleich $U_{GS}$, beide Klammern ergeben 3/4, und beide Kapazitäten sind $C_\mathrm{ox}/2$. An der Abschnürgrenze ist $U_{GD}$ gleich $U_{th}$, und es folgen $\tfrac23 C_\mathrm{ox}$ und null. Die Summe sinkt dazwischen stetig von $C_\mathrm{ox}$ auf $\tfrac23 C_\mathrm{ox}$.

Idee der Herleitung: Man leitet die Kanalladung aus Schritt 5 nach der Übersteuerung an der Source bzw. am Drain-Ende ab.

:::herleitung
**Ausgangspunkt:** Schritt 5 der vorigen Herleitung, die Kanalladung als Funktion der beiden Übersteuerungen:

$$Q_K = \frac{2}{3}\,C_\mathrm{ox}\,\frac{U_{\text{ü}S}^2 + U_{\text{ü}S}\,U_{\text{ü}D} + U_{\text{ü}D}^2}{U_{\text{ü}S} + U_{\text{ü}D}}$$

**Annahmen:** dieselben wie dort; ohmscher Bereich, also $U_{\text{ü}D}$ positiv.

**Schritt 1**: $U_{\text{ü}S}$ ändert sich nur mit $U_{GS}$, $U_{\text{ü}D}$ nur mit $U_{GD}$, jeweils Volt für Volt:

$$C_{GS} = \frac{\partial Q_K}{\partial U_{\text{ü}S}}, \qquad C_{GD} = \frac{\partial Q_K}{\partial U_{\text{ü}D}}$$

**Schritt 2**: Quotientenregel, $U_{\text{ü}D}$ fest, mit dem Zähler $Z$:

$$\frac{\partial Q_K}{\partial U_{\text{ü}S}} = \frac{2}{3}\,C_\mathrm{ox}\,\frac{Z}{\big(U_{\text{ü}S} + U_{\text{ü}D}\big)^2}$$

$$\begin{aligned} Z &= \big(2U_{\text{ü}S} + U_{\text{ü}D}\big)\big(U_{\text{ü}S} + U_{\text{ü}D}\big) \\ &\quad - \big(U_{\text{ü}S}^2 + U_{\text{ü}S}U_{\text{ü}D} + U_{\text{ü}D}^2\big) \end{aligned}$$

**Schritt 3** (entscheidender Schritt): Ausmultipliziert ist $Z$ gleich $U_{\text{ü}S}^2 + 2U_{\text{ü}S}U_{\text{ü}D}$, also das Quadrat der Summe weniger $U_{\text{ü}D}^2$:

$$C_{GS} = \frac{2}{3}\,C_\mathrm{ox}\,\Big[1 - \Big(\frac{U_{\text{ü}D}}{U_{\text{ü}S} + U_{\text{ü}D}}\Big)^2\Big]$$

**Schritt 4**: $Q_K$ ändert sich nicht, wenn man beide Übersteuerungen vertauscht; deshalb folgt $C_{GD}$ durch Vertauschen:

$$C_{GD} = \frac{2}{3}\,C_\mathrm{ox}\,\Big[1 - \Big(\frac{U_{\text{ü}S}}{U_{\text{ü}S} + U_{\text{ü}D}}\Big)^2\Big]$$

**Ergebnis:** die Formeln oben, nachdem man für die beiden Übersteuerungen wieder $U_{GS} - U_{th}$ und $U_{GD} - U_{th}$ einsetzt.

**Woher die Faktoren kommen:** Die 2/3 stammen aus dem Mittelwert über das Ladungsprofil; die Klammer misst, wie viel der Kanalladung das jeweils andere Ende festhält.

**Proben:** Einheit fF. $U_{GS}$ = 1,5 V, $U_{DS}$ = 0,5 V: $U_{\text{ü}S}$ = 1 V, $U_{\text{ü}D}$ = 0,5 V, also $C_{GS}$ = 2/3 · 8/9 · $C_\mathrm{ox}$ = 0,593 $C_\mathrm{ox}$ = 40,9 fF und $C_{GD}$ = 2/3 · 5/9 · $C_\mathrm{ox}$ = 0,370 $C_\mathrm{ox}$ = 25,6 fF. Gleiche Übersteuerungen ergeben je 1/2, $U_{\text{ü}D}$ = 0 ergibt 2/3 und 0.

**Grenzen:** dieselben wie in der vorigen Herleitung.
:::

::::beispiel Kapazitäten zwischen den Grenzfällen
**Gegeben:** Beispiel-NMOS mit $C_\mathrm{ox}$ = 69,06 fF und $U_{th}$ = 0,5 V; $U_{GS}$ = 1,5 V, (a) $U_{DS}$ = 0,5 V, (b) $U_{DS}$ = 0,75 V.

**Gesucht:** $C_{GS}$ und $C_{GD}$ ohne Überlappung.

**Rechnung:** (a) $U_{GD} - U_{th}$ = 1 V − 0,5 V = 0,5 V, Summe der Übersteuerungen 1,5 V:

$$C_{GS} = \frac{2}{3}\Big[1 - \Big(\frac{0{,}5}{1{,}5}\Big)^2\Big]\cdot69{,}06\ \mathrm{fF} = 40{,}9\ \mathrm{fF}, \qquad C_{GD} = \frac{2}{3}\Big[1 - \Big(\frac{1}{1{,}5}\Big)^2\Big]\cdot69{,}06\ \mathrm{fF} = 25{,}6\ \mathrm{fF}$$

(b) $U_{GD} - U_{th}$ = 0,25 V, Summe 1,25 V:

$$C_{GS} = \frac{2}{3}\,\big(1 - 0{,}04\big)\cdot69{,}06\ \mathrm{fF} = 44{,}2\ \mathrm{fF}, \qquad C_{GD} = \frac{2}{3}\,\big(1 - 0{,}64\big)\cdot69{,}06\ \mathrm{fF} = 16{,}6\ \mathrm{fF}$$

**Ergebnis:** **(a) 40,9 fF und 25,6 fF, zusammen 66,5 fF; (b) 44,2 fF und 16,6 fF, zusammen 60,8 fF.**

**Einordnung:** Auf halbem Weg zur Abschnürgrenze ist $C_{GD}$ um ein Viertel kleiner als bei $U_{DS}$ = 0, bei drei Vierteln des Wegs auf knapp die Hälfte gesunken; $C_{GS}$ wächst nicht im selben Maß, deshalb sinkt die Summe.
::::

:::frage
„Bleibt unter dem Kanal keine Kapazität zum Bulk?“
Doch. Zwischen Kanal und Bulk liegt die Verarmungszone, an der Schwelle 45,8 nm tief, mit 2,26 fF/µm², über der ganzen Kanalfläche 22,6 fF. Weil der Kanal an Source und Drain hängt, liegt diese Kapazität zwischen ihnen und dem Bulk und addiert sich zu den Sperrschichtkapazitäten $C_{SB}$ und $C_{DB}$. Sie teilt sich nach demselben Muster auf wie die Gatekapazität: im ohmschen Bereich je rund 11 fF, im Abschnürbereich rund 15 fF zur Source und nichts zum Drain.
:::

:::vertiefung
**Was die einfache Aufteilung vernachlässigt.** Die Werte 1/2 und 2/3 beruhen auf dem Modell der Kennlinien, in dem die Elektronenladung genau $C'_\mathrm{ox}$ mal Übersteuerung beträgt und die Verarmungsladung längs des Kanals fest bleibt. Eine vollständige Rechnung des Langkanaltransistors, mit der Elektronendichte nach der Boltzmann-Verteilung und einer zum Drain hin wachsenden Verarmungsladung, ergibt für den Beispieltransistor bei $U_{GS}$ = 1 V im Abschnürbereich $C_{GS}$ = 0,60 $C_\mathrm{ox}$ statt 0,67 und $C_{GB}$ = 0,08 $C_\mathrm{ox}$ statt null; die Summe, 0,69 $C_\mathrm{ox}$, weicht kaum vom einfachen Wert ab. Bei 1,5 V sind es 0,64 und 0,07. Der Bulkanteil entsteht, weil mit der Gatespannung auch das Potential am Ende des Kanals steigt; im drainseitigen Teil wird die Verarmungszone dadurch tiefer, und die zusätzliche Ladung kommt aus dem Bulk. Die Kanallängenmodulation koppelt außerdem den Drain schwach an die Kanalladung, weil sich der Abschnürpunkt mit der Drainspannung verschiebt. Schließlich gelten alle Werte nur, solange die Kanalladung den Spannungen folgen kann. Die Elektronen brauchen bei 1 V für den Weg durch den Kanal 92 ps; ändern sich die Spannungen in vergleichbarer Zeit, bei sinusförmigen Signalen etwa ab 1,7 GHz, hinkt die Kanalladung nach, und das Bild fester Kondensatoren reicht nicht mehr aus.
:::

### Die Kapazitäten in den drei Bereichen

*Wie groß sind die Kapazitäten des Gates im gesperrten Zustand, im Abschnürbereich und im ohmschen Bereich?*

Zusammengefasst für den Beispieltransistor mit Source und Bulk an Masse: gesperrt bei $U_{GS}$ = 0, im Abschnürbereich bei $U_{GS}$ = $U_{DS}$ = 1 V, im ohmschen Bereich bei kleiner $U_{DS}$; alle Werte in fF und mit den Überlappungen. Gesperrt bilden die Überlappungen alles, was zu Source und Drain gehört, und $C_{GB}$ ist die Reihenschaltung aus Oxid und Verarmungszone; oberhalb der Schwelle kommen $\tfrac23 C_\mathrm{ox}$ bzw. je $\tfrac12 C_\mathrm{ox}$ hinzu.

| in fF | gesperrt | abge­schnürt | ohmsch |
|---|---|---|---|
| $C_{GS}$ | 3,45 | 49,5 | 38,0 |
| $C_{GD}$ | 3,45 | 3,45 | 38,0 |
| $C_{GB}$ | 20,7 | ≈ 0 | ≈ 0 |
| $C_G$ | 27,6 | 53,0 | 76,0 |

Vom gesperrten Zustand bis in den ohmschen Bereich wächst die Gatekapazität auf fast das Dreifache, und ihre Gegenladung wechselt dabei den Anschluss: erst der Bulk, dann vor allem die Source, schließlich Source und Drain zu gleichen Teilen.

:::fehlvorstellung
„Die Gatekapazität eines MOSFET ist die Oxidkapazität, Permittivität mal Gatefläche durch Oxiddicke.“ Das liegt nahe, weil Gate, Oxid und Kanal wie ein Plattenkondensator aussehen. Das ist sie aber nur, wenn die Gegenladung unmittelbar unter dem Oxid sitzt und von beiden Kanalenden nachfließen kann: in der Anreicherung und im ohmschen Bereich. Beim Beispieltransistor sind es gesperrt bei 0 V 20,7 fF statt 69,1 fF, weil die Verarmungszone in Reihe liegt, und im Abschnürbereich 46,0 fF, weil der Kanal vor dem Drain endet. Erst im ohmschen Bereich wird die volle Oxidkapazität erreicht, mit den Überlappungen 76,0 fF.
:::

## Sperrschichtkapazitäten von Source und Drain

*Welche Kapazität haben Source und Drain gegen den Bulk, und warum zählt neben der Fläche auch der Rand?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/04-sperrschicht-geometrie · Vorlage: querschnitt-und-aufsicht
**Abbildung 6:** (a) Aufsicht auf das Draingebiet des Beispieltransistors: 10 µm entlang der Gatekante, 2 µm vom Gate bis zum Ende des Gebiets; Fläche 20 µm² schraffiert, Umfang 24 µm als dicke Randlinie. (b) Querschnitt quer zur Gatekante: n⁺-Gebiet 0,2 µm tief, umgeben von der Raumladungszone, ohne Spannung 48,4 nm und bei 1 V 67,9 nm breit; Kondensatorsymbole am Boden, 2,14 fF/µm², und an den Seitenwänden, 0,428 fF pro µm Rand. An der Gatekante grenzt die Wand an das p-Gebiet unter dem nur wenige Nanometer dicken Kanal. Ohne Spannung entfallen 42,9 fF auf den Boden und 10,3 fF auf den Rand. Die Kapazität eines Source- oder Draingebiets besteht aus Boden und Rand; der Boden zählt mit seiner Fläche, der Rand mit seiner Länge.
:::

Source und Drain bilden mit dem p-Gebiet je einen pn-Übergang. Im Betrieb sind beide gesperrt, weil der Bulk an der niedrigsten Spannung der Schaltung liegt, und zwischen n⁺-Gebiet und p-Gebiet liegt eine Raumladungszone, beim Beispieltransistor ohne Spannung 48,4 nm breit. Weil das n⁺-Gebiet mit 10²⁰ cm⁻³ rund 180-mal so stark dotiert ist wie das p-Gebiet, liegt die Zone zu 99,4 % im p-Gebiet. Wächst die Spannung zwischen Drain und Bulk, wird die Zone breiter: An ihrem Rand im p-Gebiet verlieren weitere Akzeptorrümpfe ihre Löcher, die über den Bulk abfließen, und auf der n⁺-Seite fließen ebenso viele Elektronen über den Drain ab. Diese Ladung je Spannungsänderung ist die __Sperrschichtkapazität__. Die Zone wirkt wie ein Plattenkondensator mit Silizium als Dielektrikum, dessen Plattenabstand mit der Spannung wächst; deshalb sinkt die Kapazität mit steigender Sperrspannung. Source und Drain heißen nach ihrer Herstellung auch Diffusionsgebiete; mit der Diffusionskapazität einer Diode in Durchlassrichtung, die von gespeicherten Minoritätsträgern herrührt, hat ihre Sperrschichtkapazität nichts zu tun.

**Die Akteure:**

- __$U_j$__: Spannung am Übergang, in Durchlassrichtung vom p- zum n-Gebiet gezählt (j für englisch junction); beim Drain $-U_{DB}$, im Betrieb also negativ.
- __$U_\mathrm{Diff}$__: Diffusionsspannung des Übergangs, die Spannung, die ohne äußere Spannung über der Zone liegt; 1,03 V beim Beispieltransistor. Sie ist so groß wie die Kontaktspannung des n⁺-Gates aus [Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html), denn auch dort steht ein n⁺-Gebiet mit dem Fermi-Niveau an der Leitungsbandkante demselben p-Gebiet gegenüber. Über der Zone liegt die Spannung $U_\mathrm{Diff} - U_j$.
- __$w$__: Breite der Raumladungszone; 48,4 nm ohne Spannung, 67,9 nm bei $U_{DB}$ = 1 V.
- __$C_j$__, __$C_{j0}$__: Sperrschichtkapazität bei der Spannung $U_j$ bzw. ohne Spannung; für das Draingebiet 37,8 fF bei 1 V und 53,1 fF ohne Spannung.
- __$m_j$__: Exponent, der vom Verlauf der Dotierung am Übergang abhängt; 1/2 bei einem abrupten Übergang, an dem die Dotierung sprunghaft wechselt, 1/3 bei einem linear verlaufenden. Gemessene Werte liegen meist dazwischen.

:::formel Gesetz
$$C_j = C_{j0}\,\Big(1 - \frac{U_j}{U_\mathrm{Diff}}\Big)^{-m_j}$$
:::

**So liest man das:** Eingabe ist die Spannung am Übergang, Ausgabe die Kapazität. In Sperrrichtung ist $U_j$ negativ, die Klammer größer als 1 und die Kapazität kleiner als $C_{j0}$; je größer die Sperrspannung, desto breiter die Zone und desto kleiner die Kapazität, aber mit abnehmender Steigung. Für den Drain des NMOS, mit $U_j$ = $-U_{DB}$:

$$C_{DB} = C_{DB0}\,\Big(1 + \frac{U_{DB}}{U_\mathrm{Diff}}\Big)^{-m_j}$$

Bei $U_{DB}$ = 1 V und $m_j$ = 1/2 sinkt sie auf das 0,712-Fache, bei 2,5 V auf das 0,540-Fache.

**Kurz gesagt:** Beim abrupten Übergang halbiert die vierfache Spannung über der Zone die Kapazität.

Idee der Herleitung: Die Zone ist ein Plattenkondensator, dessen Plattenabstand mit der Spannung über ihr wächst; wie schnell er wächst, hängt vom Verlauf der Dotierung ab.

:::herleitung
**Ausgangspunkt:** die Breite der Raumladungszone eines abrupten pn-Übergangs aus [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie-ausfuehrlich.html), dort aus der Poisson-Gleichung hergeleitet, mit den Dotierungen $N_A$ und $N_D$ beiderseits:

$$w = \sqrt{\frac{2\,\varepsilon_\mathrm{Si}\,\big(U_\mathrm{Diff} - U_j\big)}{e}\cdot\frac{N_A + N_D}{N_A\,N_D}}$$

**Annahmen:**
(i) Verarmungsnäherung: Die Zone ist scharf begrenzt und frei von beweglichen Ladungsträgern;
(ii) kleine Änderungen;
(iii) entweder ein abrupter Übergang mit festen Dotierungen beiderseits oder ein linear verlaufender mit festem Gradienten der Dotierung.

**Schritt 1**: Ändert sich die Spannung ein wenig, kommt und geht Ladung nur an den beiden Rändern der Zone; dazwischen gibt es keine beweglichen Ladungen. Die Zone wirkt deshalb wie ein Plattenkondensator mit dem Abstand $w$ und der Fläche $A$ des Übergangs:

$$C_j = \frac{\varepsilon_\mathrm{Si}\,A}{w}$$

**Schritt 2**: Beim abrupten Übergang wächst $w$ mit der Wurzel der Spannung über der Zone. Mit der Breite $w_0$ ohne Spannung:

$$w = w_0\,\sqrt{1 - \frac{U_j}{U_\mathrm{Diff}}}$$

**Schritt 3** (entscheidender Schritt): In Schritt 1 eingesetzt; ohne Spannung ist die Kapazität

$$C_{j0} = \frac{\varepsilon_\mathrm{Si}\,A}{w_0}$$

und damit

$$C_j = C_{j0}\,\Big(1 - \frac{U_j}{U_\mathrm{Diff}}\Big)^{-1/2}$$

**Schritt 4**: Beim linear verlaufenden Übergang ist die Netto-Dotierung $N_D - N_A$ gleich $a\,x$, mit dem Gradienten $a$ in cm⁻⁴ und dem Übergang bei $x$ = 0. In der Zone von $-w/2$ bis $w/2$ ist die Raumladung $e\,a\,x$; die Poisson-Gleichung, mit verschwindendem Feld an beiden Rändern integriert, ergibt

$$\frac{\mathrm dE}{\mathrm dx} = \frac{e\,a\,x}{\varepsilon_\mathrm{Si}} \quad\Rightarrow\quad E(x) = \frac{e\,a}{2\,\varepsilon_\mathrm{Si}}\,\Big(x^2 - \frac{w^2}{4}\Big)$$

**Schritt 5**: Die Spannung über der Zone ist das negative Integral des Feldes über die Zone:

$$U_\mathrm{Diff} - U_j = -\int_{-w/2}^{w/2} E\,\mathrm dx = \frac{e\,a\,w^3}{12\,\varepsilon_\mathrm{Si}}$$

**Schritt 6**: Die Breite wächst also mit der dritten Wurzel der Spannung, und mit Schritt 1 folgt

$$C_j = C_{j0}\,\Big(1 - \frac{U_j}{U_\mathrm{Diff}}\Big)^{-1/3}$$

**Ergebnis:**

$$C_j = C_{j0}\,\Big(1 - \frac{U_j}{U_\mathrm{Diff}}\Big)^{-m_j}, \qquad m_j = \tfrac12\ \text{(abrupt)}, \qquad m_j = \tfrac13\ \text{(linear)}$$

**Woher die Faktoren kommen:** Der Exponent misst, wie schnell die Zone mit der Spannung wächst. Beim abrupten Übergang braucht die doppelte Breite die vierfache Spannung, beim linearen die achtfache, weil die Ladungsdichte zum Rand der Zone hin zunimmt.

**Proben:** Einheit F. Draingebiet: $w_0$ = 48,4 nm, bei $U_{DB}$ = 1 V 48,4 nm · √1,973 = 67,9 nm; die Kapazität sinkt im selben Verhältnis auf das 0,712-Fache. Linearer Übergang mit $a$ = 10²² cm⁻⁴ und angenommener Diffusionsspannung 0,9 V: 191 nm ohne und 282 nm bei 2 V Sperrspannung; das Verhältnis der Kapazitäten, 0,677, ist die dritte Wurzel aus 0,9/2,9. Grenzfall $U_j$ = 0: $C_j$ = $C_{j0}$.

**Grenzen:** In Durchlassrichtung wird die Zone schmal, die Verarmungsnäherung ungenau, und die Ladung der Minoritätsträger überwiegt; Source und Drain bleiben im Betrieb aber gesperrt.
:::

Die Zone umgibt das n⁺-Gebiet am Boden und an allen vier Seitenwänden (Abbildung 6). Weil die Tiefe der Gebiete in einem Herstellungsprozess fest ist, lässt sich die Kapazität jedes Gebiets aus zwei Technologiewerten berechnen, einem pro Fläche für den Boden und einem pro Länge für den Rand.

**Die Akteure:**

- __$C'_{jF}$__: Sperrschichtkapazität des Bodens pro Fläche; 2,14 fF/µm² ohne Spannung, ein knappes Drittel von $C'_\mathrm{ox}$.
- __$C'_{jS}$__: Sperrschichtkapazität der Seitenwände pro Länge des Randes; 0,428 fF/µm ohne Spannung. Der Strich bedeutet hier den Bezug auf die Länge.
- __$x_j$__: Tiefe der n⁺-Gebiete; 0,2 µm.
- __$b$__: Länge des Draingebiets von der Gatekante bis zu seinem Ende; 2 µm, genug für die Kontakte.
- __$A_D$__, __$P_D$__: Fläche und Umfang des Draingebiets in der Aufsicht; 20 µm² und 24 µm. Für die Source gilt dasselbe mit $A_S$ und $P_S$.

:::formel Formel
$$C_{DB} = C'_{jF}\,A_D + C'_{jS}\,P_D, \qquad A_D = W\,b, \qquad P_D = 2\,\big(W + b\big)$$
:::

**So liest man das:** Der Boden zählt mit seiner Fläche, der Rand mit seiner Länge; beide Beläge gelten bei derselben Spannung und folgen dem Gesetz oben, im Allgemeinen mit eigenem Exponenten. Beim Beispiel entfallen ohne Spannung 42,9 fF auf den Boden und 10,3 fF auf den Rand, zusammen 53,1 fF, der Rand trägt 19 % bei. An der Gatekante grenzt die Seitenwand an das p-Gebiet unter dem Kanal; weil der Kanal nur wenige Nanometer dick ist, zählt man sie voll mit. Wie viele der übrigen Seiten tatsächlich an p-Silizium grenzen, hängt davon ab, wie die Transistoren voneinander isoliert sind; die Formel zählt alle vier. In Schaltungssimulatoren gibt man deshalb für jeden Transistor Fläche und Umfang von Source und Drain an (Parameter AS, PS, AD, PD).

**Kurz gesagt:** Verkleinert man ein Gebiet in beiden Richtungen um denselben Faktor, sinkt der Bodenanteil mit dem Quadrat des Faktors, der Randanteil nur mit dem Faktor selbst.

Idee der Herleitung: Man zerlegt die Zone in ebene Stücke, den Boden und vier Seitenwände, und zählt ihre Plattenkondensatoren zusammen.

:::herleitung
**Ausgangspunkt:** Schritt 1 der vorigen Herleitung: Jedes ebene Stück der Zone ist ein Plattenkondensator $\varepsilon_\mathrm{Si} A/w$.

**Annahmen:**
(i) Boden und Seitenwände grenzen an p-Silizium derselben Dotierung und haben deshalb dieselbe Zonenbreite;
(ii) Ecken und Krümmung werden vernachlässigt, weil die Zone, 48 nm, dünn gegen die Tiefe, 200 nm, ist;
(iii) der Kanal an der Gatekante wird vernachlässigt.

**Schritt 1**: Der Boden hat die Fläche $W b$ und damit die Kapazität $C'_{jF} W b$.

**Schritt 2**: Die vier Seitenwände sind Rechtecke der Höhe $x_j$ und der Längen $W$, $b$, $W$ und $b$; ihre Fläche ist $x_j$ mal Umfang, und bei gleicher Dotierung haben sie dieselbe Kapazität pro Fläche:

$$C_\mathrm{Rand} = C'_{jF}\,x_j\cdot2\,\big(W + b\big)$$

**Schritt 3** (entscheidender Schritt): Das Produkt $C'_{jF} x_j$ hängt nur vom Prozess ab, nicht von den Abmessungen; man fasst es zu einem Wert pro Länge zusammen:

$$C'_{jS} = C'_{jF}\,x_j$$

**Ergebnis:**

$$C_{DB} = C'_{jF}\,A_D + C'_{jS}\,P_D, \qquad A_D = W\,b, \qquad P_D = 2\,\big(W + b\big)$$

**Woher die Faktoren kommen:** Die 2 im Umfang steht, weil das Rechteck je zwei Seiten der Längen $W$ und $b$ hat; $x_j$ steckt im Randbelag.

**Proben:** Einheit fF/µm² · µm² + fF/µm · µm = fF. Zahlenwert: 2,142 · 0,2 = 0,428 fF/µm; 2,142 · 20 + 0,428 · 24 = 42,85 + 10,28 = 53,13 fF.

**Grenzen:** Die Seitenwände grenzen in realen Prozessen oft an höher dotierte Gebiete oder an Isolationsoxid; dann misst man $C'_{jS}$ eigens, mit eigenem, meist kleinerem Exponenten.
:::

:::grafik
Szene: st1/mos-feldeffekttransistoren/04-sperrschicht-spannung · Vorlage: kennlinie-anteile
**Abbildung 7:** Oben $C_{DB}$ des Beispieltransistors in fF über $U_{DB}$ von 0 bis 2,5 V, als gestapelte Flächen aus Boden und Rand: zusammen 53,1 fF ohne Spannung, 43,6 fF bei 0,5 V, 37,8 fF bei 1 V, 33,9 fF bei 1,5 V, 31,0 fF bei 2 V und 28,7 fF bei 2,5 V; der Boden fällt von 42,9 auf 23,1 fF, der Rand von 10,3 auf 5,5 fF. Gestrichelt der Verlauf mit $m_j$ = 1/3 bei gleichem Wert ohne Spannung, das 0,797-Fache statt 0,712 bei 1 V. Unten die Breite der Zone über derselben Achse, von 48,4 nm auf 89,6 nm. Mit der Sperrspannung wird die Zone breiter und die Kapazität kleiner, beim abrupten Übergang mit der Wurzel der Spannung über der Zone.
:::

Abbildung 7 zeigt beide Anteile über der Sperrspannung: Sie sinken im selben Verhältnis, weil im Beispiel Boden und Rand an dieselbe Dotierung grenzen. Zwischen 0 und 2,5 V halbiert sich die Kapazität fast, von 53,1 fF auf 28,7 fF.

::::beispiel Sperrschichtkapazität des Draingebiets
**Gegeben:** p-Gebiet mit $N_A$ = 5,68·10¹⁷ cm⁻³, n⁺-Gebiete so stark dotiert, dass nur $N_A$ zählt; $U_\mathrm{Diff}$ = 1,027 V, $\varepsilon_\mathrm{Si}$ = 1,036·10⁻¹² F/cm, $e$ = 1,602·10⁻¹⁹ C, Tiefe $x_j$ = 0,2 µm, $m_j$ = 1/2. Draingebiet $W$ = 10 µm, $b$ = 2 µm; $U_{DB}$ = 1 V. (b) Alle Abmessungen des Gebiets geviertelt. (c) Derselbe Transistor mit zwei Fingern.

**Gesucht:** die Beläge, $C_{DB}$ ohne Spannung und bei 1 V, der Randanteil; dasselbe für (b) ohne Spannung und für (c) bei 1 V.

**Rechnung:** Breite der Zone ohne Spannung; der Bruch mit $N_A$ und $N_D$ wird zu $1/N_A$:

$$w_0 = \sqrt{\frac{2\cdot1{,}036\cdot10^{-12}\ \mathrm{F/cm}\cdot1{,}027\ \mathrm V}{1{,}602\cdot10^{-19}\ \mathrm C\cdot5{,}68\cdot10^{17}\ \mathrm{cm^{-3}}}} = 4{,}84\cdot10^{-6}\ \mathrm{cm} = 48{,}4\ \mathrm{nm}$$

Beläge:

$$C'_{jF} = \frac{1{,}036\cdot10^{-12}\ \mathrm{F/cm}}{4{,}84\cdot10^{-6}\ \mathrm{cm}} = 2{,}14\ \mathrm{fF/\mu m^2}, \qquad C'_{jS} = 2{,}14\ \mathrm{fF/\mu m^2}\cdot0{,}2\ \mathrm{\mu m} = 0{,}428\ \mathrm{fF/\mu m}$$

Ohne Spannung und bei 1 V:

$$\begin{aligned} C_{DB0} &= 2{,}14\ \mathrm{fF/\mu m^2}\cdot20\ \mathrm{\mu m^2} + 0{,}428\ \mathrm{fF/\mu m}\cdot24\ \mathrm{\mu m} \\ &= 42{,}9\ \mathrm{fF} + 10{,}3\ \mathrm{fF} = 53{,}1\ \mathrm{fF} \end{aligned}$$

$$C_{DB} = 53{,}1\ \mathrm{fF}\cdot\Big(1 + \frac{1\ \mathrm V}{1{,}027\ \mathrm V}\Big)^{-1/2} = 53{,}1\ \mathrm{fF}\cdot0{,}712 = 37{,}8\ \mathrm{fF}$$

(b) Geviertelt, 2,5 µm mal 0,5 µm: Fläche 1,25 µm², Umfang 6 µm:

$$2{,}14\ \mathrm{fF/\mu m^2}\cdot1{,}25\ \mathrm{\mu m^2} = 2{,}68\ \mathrm{fF}, \qquad 0{,}428\ \mathrm{fF/\mu m}\cdot6\ \mathrm{\mu m} = 2{,}57\ \mathrm{fF}$$

(c) Teilt man das Gate in zwei Finger von je 5 µm Weite, die sich einen Drain in der Mitte teilen, hat dieser 5 µm mal 2 µm, also 10 µm² Fläche und 14 µm Umfang:

:::grafik
Szene: st1/mos-feldeffekttransistoren/04-finger-layout · Vorlage: layout-aufsicht
**Abbildung 8:** Zwei Layouts mit derselben Gesamtweite von 10 µm. (a) Ein Finger: Source 10 µm mal 2 µm, Gate 10 µm breit, Drain 10 µm mal 2 µm. (b) Zwei Finger zu je 5 µm in der Folge Source, Gate, Drain, Gate, Source: Der Drain in der Mitte, 5 µm mal 2 µm, gehört zu beiden Gates, die beiden äußeren Sources sind verbunden. Bei $U_{DB}$ = 1 V hat der Drain in (a) 37,8 fF, in (b) 19,5 fF. Teilen sich zwei Gates einen Drain, halbiert sich fast die Drainkapazität bei unverändertem Strom.
:::

$$C_{DB} = \big(2{,}14\cdot10 + 0{,}428\cdot14\big)\ \mathrm{fF}\cdot0{,}712 = 27{,}4\ \mathrm{fF}\cdot0{,}712 = 19{,}5\ \mathrm{fF}$$

**Ergebnis:** **$C_{DB}$ = 53,1 fF ohne Spannung und 37,8 fF bei 1 V, davon 19 % aus dem Rand; geviertelt 5,25 fF mit 49 % Randanteil; mit zwei Fingern 19,5 fF bei 1 V.**

**Einordnung:** Die Drainkapazität ist mit 37,8 fF drei Viertel so groß wie $C_{GS}$ und elfmal so groß wie $C_{GD}$; am Ausgang einer Verstärkerstufe ist sie meist die größte Kapazität. Beim Verkleinern um den Faktor 4 schrumpft der Boden um den Faktor 16, der Rand nur um 4; in feinen Prozessen gibt man deshalb beide Beläge getrennt an. Das Falten in Finger halbiert fast die Drainkapazität bei gleicher Weite und gleichem Strom; die beiden Sources werden dafür größer, doch eine Source an Masse wird nicht umgeladen.
::::

:::fehlvorstellung
„Ein gesperrter pn-Übergang isoliert; seine Kapazität ist klein gegen die des Gates.“ Das liegt nahe, weil durch einen gesperrten Übergang kaum Strom fließt. Für Gleichstrom isoliert er tatsächlich, für Änderungen aber ist seine Zone eine dünne Isolierschicht zwischen zwei leitenden Gebieten. 48 nm Silizium haben pro Fläche 2,14 fF/µm², ein knappes Drittel des 5 nm dicken Oxids, und das Draingebiet ist mit 20 µm² doppelt so groß wie die Kanalfläche. Beim Beispieltransistor erreicht $C_{DB}$ bei 1 V mit 37,8 fF drei Viertel von $C_{GS}$.
:::

## Kapazität der Leitungen

*Wie viel Kapazität bringt eine Leiterbahn mit, und warum mehr, als der Plattenkondensator angibt?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/04-leitung-randfeld · Vorlage: feldbild-querschnitt
**Abbildung 9:** Querschnitt einer Metallbahn, 2 µm breit und 0,5 µm dick, 1 µm über dem Substrat, das als leitende Ebene gezeichnet ist; dazwischen Oxid. Unter der Bahn laufen die Feldlinien senkrecht und gleichmäßig, von den Flanken und der Oberseite in Bögen zum Substrat. Je Millimeter Länge ergibt der Plattenkondensator 69,1 fF, mit dem Randfeld 162 fF, das 2,35-Fache; daneben eine kleine Tabelle mit dem Faktor 3,55 bei 1 µm, 2,35 bei 2 µm und 1,75 bei 4 µm Breite. Je schmaler eine Bahn im Verhältnis zu ihrem Abstand vom Substrat, desto mehr trägt das Randfeld zu ihrer Kapazität bei.
:::

Die Transistoren sind über Bahnen aus Metall oder Polysilizium verbunden, die ein dickes Oxid vom Substrat trennt. Das leitende Substrat liegt auf dem Potential des Bulk und bildet die Gegenelektrode; jede Bahn ist deshalb ein Kondensator gegen Masse. Als Plattenkondensator gerechnet hat 1 µm Oxid 0,0345 fF/µm², zweihundertmal weniger als das 5 nm dicke Gateoxid. Bahnen sind aber lang: Eine 2 µm breite und 1 mm lange Bahn bedeckt 2000 µm² und hat so 69,1 fF, genau so viel wie das Gate des Beispieltransistors.

Dazu kommt das __Randfeld__: Die Feldlinien verlassen nicht nur die Unterseite der Bahn, sondern auch ihre Flanken und ihre Oberseite und biegen zum Substrat (Abbildung 9). Bei Bahnen, die nicht viel breiter sind als ihr Abstand zum Substrat, trägt es einen großen Teil der Kapazität. Für eine Bahn über einer leitenden Ebene ist folgende Näherung aus numerischen Feldrechnungen verbreitet.

**Die Akteure:**

- __$b_M$__, __$t_M$__, __$\ell$__: Breite, Dicke und Länge der Bahn; 2 µm, 0,5 µm und 1 mm.
- __$h$__: Abstand der Bahn vom Substrat, die Dicke des Oxids darunter; 1 µm.
- __$\varepsilon_\mathrm{ox}$__: Permittivität des Oxids, 3,9-mal die des Vakuums; 3,45·10⁻¹³ F/cm, also 0,0345 fF/µm.
- __$C_\mathrm{Bahn}$__: Kapazität der Bahn gegen das Substrat; 162 fF für die Beispielbahn.

$$C_\mathrm{Bahn} = \varepsilon_\mathrm{ox}\,\ell\,\Big[1{,}15\,\frac{b_M}{h} + 2{,}80\,\Big(\frac{t_M}{h}\Big)^{0{,}222}\Big]$$

**So liest man das:** Der erste Summand wächst wie der Plattenkondensator mit der Breite der Bahn; der zweite beschreibt das Randfeld an Flanken und Oberseite, er hängt nicht von der Breite ab und wächst schwach mit der Dicke. Je schmaler die Bahn, desto mehr zählt er: Bei 4 µm, 2 µm und 1 µm Breite ist die Kapazität das 1,75-, 2,35- bzw. 3,55-Fache des Plattenwerts. Die Formel stammt von Sakurai und Tamaru (1983) und weicht im Bereich von 0,3 bis 30 für $b_M/h$ und $t_M/h$ um weniger als 6 % von der genauen Feldrechnung ab.

Idee der Herleitung: Man löst die Feldgleichung im Oxid numerisch für viele Formen der Bahn und passt eine Formel an die Ergebnisse an.

:::herleitung
**Ausgangspunkt:** Im Oxid gibt es keine Raumladung; das Potential erfüllt deshalb die Laplace-Gleichung, die Poisson-Gleichung ohne Ladung, mit der Spannung $U$ auf der Bahn und null auf dem Substrat. Die Kapazität ist die Ladung auf der Bahn durch $U$.

**Annahmen:**
(i) Die Bahn ist lang gegen ihren Querschnitt, sodass ein Querschnitt genügt;
(ii) das Substrat ist eine ideal leitende Ebene;
(iii) das Oxid ist überall gleich, und keine anderen Leiter sind in der Nähe.

**Schritt 1**: Für eine unendlich breite Bahn ist das Feld darunter homogen, und es bleibt der Plattenkondensator:

$$\frac{C_\mathrm{Bahn}}{\ell} = \varepsilon_\mathrm{ox}\,\frac{b_M}{h}$$

**Schritt 2**: Bei endlicher Breite laufen Feldlinien auch von Flanken und Oberseite zum Substrat. Für ein Rechteck über einer Ebene hat die Laplace-Gleichung keine geschlossene Lösung; man löst sie numerisch für viele Werte von $b_M/h$ und $t_M/h$ und berechnet jedes Mal die Ladung auf der Bahn.

**Schritt 3** (entscheidender Schritt): An die numerischen Ergebnisse wird eine Formel mit einem Anteil proportional zur Breite und einem von der Breite unabhängigen Randanteil angepasst; sie trifft im genannten Bereich alle Ergebnisse auf 6 %:

$$C_\mathrm{Bahn} = \varepsilon_\mathrm{ox}\,\ell\,\Big[1{,}15\,\frac{b_M}{h} + 2{,}80\,\Big(\frac{t_M}{h}\Big)^{0{,}222}\Big]$$

**Ergebnis:** die Formel oben. Hinweis: Die Feldrechnung selbst geht über den Rahmen dieses Artikels hinaus; die Formel ist eine Anpassung an ihre Ergebnisse, keine geschlossene Herleitung.

**Woher die Faktoren kommen:** 1,15 und 2,80 sowie der Exponent 0,222 sind Anpassungswerte; die Aufteilung in Breitenanteil und Randanteil ist die Struktur des Feldes.

**Proben:** Einheit F/cm · cm = F. Beispielbahn: 0,0345 fF/µm · 1000 µm · (2,30 + 2,80 · 0,857) = 34,5 fF · 4,70 = 162 fF, gegen 69,1 fF als Plattenkondensator. Für sehr breite Bahnen ginge das Verhältnis zum Plattenwert gegen 1,15 statt gegen 1; das zeigt, dass die Formel nur in ihrem Bereich gilt.

**Grenzen:** Liegen andere Bahnen nahe daneben, enden Feldlinien auf ihnen statt auf dem Substrat; ein Teil der Kapazität wird dann zur Kapazität zwischen den Bahnen.
:::

::::beispiel Kapazität einer 1 mm langen Leiterbahn
**Gegeben:** Metallbahn $b_M$ = 2 µm breit, $t_M$ = 0,5 µm dick, $\ell$ = 1 mm lang, $h$ = 1 µm über dem Substrat; $\varepsilon_\mathrm{ox}$ = 3,453·10⁻¹³ F/cm = 0,03453 fF/µm.

**Gesucht:** die Kapazität als Plattenkondensator und mit Randfeld; Vergleich mit dem Gate des Beispieltransistors.

**Rechnung:** Plattenkondensator:

$$C_\mathrm{Platte} = \frac{0{,}03453\ \mathrm{fF/\mu m}\cdot2\ \mathrm{\mu m}\cdot1000\ \mathrm{\mu m}}{1\ \mathrm{\mu m}} = 69{,}1\ \mathrm{fF}$$

Mit Randfeld:

$$\begin{aligned} C_\mathrm{Bahn} &= 0{,}03453\ \mathrm{fF/\mu m}\cdot1000\ \mathrm{\mu m}\cdot\big(1{,}15\cdot2 + 2{,}80\cdot0{,}5^{0{,}222}\big) \\ &= 34{,}53\ \mathrm{fF}\cdot4{,}70 = 162\ \mathrm{fF} \end{aligned}$$

**Ergebnis:** **69,1 fF als Plattenkondensator, 162 fF mit Randfeld, das 2,35-Fache.**

**Einordnung:** Ein Millimeter dieser Bahn belastet einen Knoten so stark wie drei Gates des Beispieltransistors im Abschnürbereich mit je 53 fF. Lange Leitungen bekommen deshalb eigene, kräftige Treiberstufen. Liegt eine zweite Bahn 1 µm daneben, bilden schon die einander zugewandten Flanken auf 1 mm Länge einen Plattenkondensator von 17,3 fF; über diese __Koppelkapazität__ wirkt ein Signal auf der einen Bahn auf die andere, man spricht von Übersprechen.
::::

## Umladen und Miller-Effekt

*Was bewirken die Kapazitäten in einer Schaltung, und warum wiegt gerade die kleine Gate-Drain-Kapazität am schwersten?*

Jede Kapazität an einem Knoten muss Ladung aufnehmen oder abgeben, wenn sich seine Spannung ändert, und das braucht Zeit. Ein Knoten mit 53 fF, so viel wie das Gate des Beispieltransistors im Abschnürbereich, ändert sich mit einem Strom von 0,25 mA in 0,21 ns um 1 V; lädt man ihn über einen Widerstand von 10 kΩ, ist die Zeitkonstante Widerstand mal Kapazität, 0,53 ns ([Laden und Entladen des Kondensators](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/laden-und-entladen.html)). In einer Verstärkerstufe kommt eine Wirkung hinzu, die eine einzelne Kapazität weit über ihren Wert hinaus wachsen lässt.

Betrachtet wird die __Source-Schaltung__: Source und Bulk liegen an Masse, das Signal kommt ans Gate, und der Drain hängt über den Widerstand $R_D$ an der Versorgung und ist der Ausgang. Im Arbeitspunkt $U_{GS}$ = 1 V, $I_D$ = 0,25 mA und $U_{DS}$ = 1 V hat der Beispieltransistor die __Steilheit__ $g_m$ = 1 mS, die Änderung des Drainstroms je Volt Gate-Source-Spannung, und den __Ausgangsleitwert__ $g_o$ = 25 µS, die Änderung je Volt Drain-Source-Spannung. Mit $R_D$ = 10 kΩ verstärkt die Stufe kleine Änderungen achtfach und invertiert sie.

:::grafik
Szene: st1/mos-feldeffekttransistoren/04-miller · Vorlage: schaltung-mit-ersatz
**Abbildung 10:** (a) Source-Schaltung mit dem Beispiel-NMOS, Source und Bulk an Masse, $R_D$ = 10 kΩ zur Versorgung, am Gate eine Signalquelle mit 10 kΩ Innenwiderstand; eingezeichnet $C_{GS}$ = 49,5 fF vom Gate nach Masse, $C_{GD}$ = 3,45 fF vom Gate zum Drain und $C_{DB}$ = 37,8 fF vom Drain nach Masse; $g_m$ = 1 mS, $g_o$ = 25 µS, Verstärkung −8. Spannungsbalken: Gate +10 mV, Drain −80 mV, über $C_{GD}$ 90 mV. (b) Ersatz: $C_{GD}$ aufgeteilt in 31,1 fF vom Gate nach Masse und 3,88 fF vom Drain nach Masse; am Eingang zusammen 80,6 fF statt 52,9 fF, am Ausgang 41,7 fF. (c) Eingangskapazität für die Verstärkungen 0, −8 und −40: 52,9 fF, 80,6 fF und 191,1 fF, davon aus $C_{GD}$ 3,45 fF, 31,1 fF und 141,6 fF. Weil sich die Spannung über $C_{GD}$ neunmal so stark ändert wie am Gate, wirkt sie am Eingang neunmal so groß.
:::

**Die Akteure:**

- __$A_V$__: Spannungsverstärkung der Stufe vom Gate zum Drain für kleine Änderungen, $-g_m/(G_D + g_o)$ mit dem Leitwert $G_D$ des Drainwiderstands ([Vierpole: Parameterformen und Zusammenschaltung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/vierpole-ausfuehrlich.html)); −8 mit $G_D$ = 0,1 mS. Sie ist negativ, weil der Drain sinkt, wenn das Gate steigt.
- __$C_\mathrm{ein}$__: Kapazität, die eine Signalquelle am Gate gegen Masse sieht; 80,6 fF.
- __$C_\mathrm{aus}$__: Kapazität am Drain gegen Masse; 41,7 fF.

**Das Zusammenspiel:**

**Schritt 1**: In der Source-Schaltung liegt $C_{GS}$ zwischen Gate und Masse und $C_{DB}$ zwischen Drain und Masse; nur $C_{GD}$ verbindet den Eingang mit dem Ausgang (Abbildung 10a). Im Abschnürbereich ist sie allein die Überlappung, 3,45 fF.

**Schritt 2**: Steigt das Gate um 10 mV, sinkt der Drain um 80 mV.

**Schritt 3**: Die Spannung über $C_{GD}$ ändert sich deshalb um 90 mV, neunmal so viel wie am Eingang.

**Schritt 4** (entscheidender Schritt): Die Ladung, die dafür durch $C_{GD}$ fließt, 0,311 fC, muss die Signalquelle liefern. So viel Ladung nähme bei 10 mV ein Kondensator von 31,1 fF gegen Masse auf: Für die Quelle wirkt $C_{GD}$ neunmal so groß.

**Schritt 5**: Am Eingang liegen damit 80,6 fF statt 52,9 fF, 49,5 fF aus $C_{GS}$ und 31,1 fF aus $C_{GD}$ (Abbildung 10b). Am Ausgang ändert sich die Spannung über $C_{GD}$ um 90 mV, wenn sich der Drain um 80 mV ändert; dort wirkt sie nur 9/8-mal so groß, 3,88 fF zu den 37,8 fF von $C_{DB}$.

**Schritt 6**: Je größer die Verstärkung, desto stärker die Wirkung. Mit einer idealen Stromquelle statt $R_D$ verstärkt die Stufe 40-fach, und die 3,45 fF der Überlappung wirken am Eingang wie 141,6 fF, fast dreimal so viel wie $C_{GS}$ (Abbildung 10c).

Diese Vervielfachung heißt __Miller-Effekt__, nach John M. Miller, der sie 1920 an der Elektronenröhre beschrieb.

:::formel Satz
$$C_\mathrm{ein} = C_{GS} + C_{GD}\,\big(1 - A_V\big), \qquad C_\mathrm{aus} = C_{DB} + C_{GD}\,\frac{A_V - 1}{A_V}$$
:::

**So liest man das:** Eingaben sind die Kapazitäten und die Verstärkung, Ausgabe die Kapazitäten gegen Masse, die Signalquelle und Last sehen. Allgemein wirkt jede Kapazität zwischen Ein- und Ausgang eines Verstärkers am Eingang mit dem Faktor $1 - A_V$ und am Ausgang mit $(A_V - 1)/A_V$. Bei einer invertierenden Stufe ist $1 - A_V$ gleich $1 + |A_V|$: Am Eingang wird die Kapazität vervielfacht, am Ausgang nur wenig vergrößert, bei $A_V$ = −8 um den Faktor 9/8. Bei $A_V$ = 0, einem festgehaltenen Drain, wirkt $C_{GD}$ mit ihrem eigenen Wert; nähert sich $A_V$ dem Wert 1, verschwindet ihre Wirkung, weil sich beide Enden gleich bewegen.

**Kurz gesagt:** Am Eingang zählt eine Kapazität so oft, wie sich die Spannung über ihr je Volt Eingangsspannung ändert.

Idee der Herleitung: Man berechnet den Strom durch $C_{GD}$ aus den Spannungsänderungen an ihren beiden Enden und sucht die Kapazität gegen Masse, die denselben Strom zöge.

:::herleitung
**Ausgangspunkt:** die Kondensatorgleichung aus [Laden und Entladen des Kondensators](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/laden-und-entladen.html): Der Strom in einen Kondensator ist seine Kapazität mal der zeitlichen Änderung der Spannung über ihm.

**Annahmen:**
(i) kleine Signale um den Arbeitspunkt, die Kapazitäten sind fest;
(ii) die Spannung am Drain folgt der am Gate ohne Verzögerung mit dem festen Faktor $A_V$, der Verstärkung für langsame Änderungen; das ist die __Miller-Näherung__.

**Schritt 1**: Mit den Kleinsignalspannungen $u_G$ am Gate und $u_D$ am Drain, beide gegen Masse:

$$u_D = A_V\,u_G$$

**Schritt 2**: Der Strom vom Gate in $C_{GD}$:

$$i_\mathrm{ein} = C_{GD}\,\frac{\mathrm d\big(u_G - u_D\big)}{\mathrm dt} = C_{GD}\,\big(1 - A_V\big)\,\frac{\mathrm du_G}{\mathrm dt}$$

**Schritt 3** (entscheidender Schritt): Das ist der Strom eines Kondensators der Kapazität $C_{GD}(1 - A_V)$ vom Gate nach Masse. $C_{GS}$ liegt parallel dazu, weil die Source an Masse liegt, und parallele Kapazitäten addieren sich:

$$C_\mathrm{ein} = C_{GS} + C_{GD}\,\big(1 - A_V\big)$$

**Schritt 4**: Der Strom vom Drain in $C_{GD}$, mit $u_G$ = $u_D/A_V$:

$$i_\mathrm{aus} = C_{GD}\,\frac{\mathrm d\big(u_D - u_G\big)}{\mathrm dt} = C_{GD}\,\frac{A_V - 1}{A_V}\,\frac{\mathrm du_D}{\mathrm dt}$$

**Schritt 5**: $C_{DB}$ liegt am Drain parallel dazu, weil der Bulk an Masse liegt:

$$C_\mathrm{aus} = C_{DB} + C_{GD}\,\frac{A_V - 1}{A_V}$$

**Ergebnis:**

$$C_\mathrm{ein} = C_{GS} + C_{GD}\,\big(1 - A_V\big), \qquad C_\mathrm{aus} = C_{DB} + C_{GD}\,\frac{A_V - 1}{A_V}$$

**Woher die Faktoren kommen:** $1 - A_V$ ist die Spannungsänderung über $C_{GD}$ je Volt am Gate, $(A_V - 1)/A_V$ die je Volt am Drain.

**Proben:** Einheit F. Bei $A_V$ = −8: 3,453 fF · 9 = 31,1 fF, $C_\mathrm{ein}$ = 49,49 fF + 31,08 fF = 80,6 fF und $C_\mathrm{aus}$ = 37,82 fF + 3,885 fF = 41,7 fF. Grenzfall $A_V$ = 1: Durch $C_{GD}$ fließt kein Strom, weil sich beide Enden gleich bewegen. Vorzeichen: Bei einer invertierenden Stufe sind beide Faktoren positiv, die Ersatzkapazitäten also gewöhnliche Kapazitäten.

**Grenzen:** Annahme (ii) verlangt, dass der Drain schnell gegen die betrachteten Änderungen folgt. Mit 10 kΩ an der Quelle und $A_V$ = −8 lädt sich das Gate mit der Zeitkonstante 0,81 ns, der Drain über 8 kΩ und 41,7 fF mit 0,33 ns; die Näherung ist brauchbar. Bei $A_V$ = −40 ist der Drain mit 1,65 ns, aus 40 kΩ und 41,4 fF, fast so langsam wie das Gate mit 1,91 ns, und der Miller-Wert ist nur noch eine Abschätzung; genauer rechnet man dann mit dem Frequenzgang der ganzen Stufe.
:::

:::analogie
Eine Feder verbindet einen Wagen, den man von Hand verschiebt, mit einem zweiten, den ein Motor bei jeder Bewegung des ersten um das Achtfache in die Gegenrichtung schiebt. Verschiebt man den ersten um 1 cm, wird die Feder um 9 cm gestaucht, und man spürt die neunfache Federkraft, als hinge der Wagen an einer neunmal so steifen Feder vor einer festen Wand. Beide Fälle folgen derselben linearen Beziehung: Die Kraft ist Steifigkeit mal Längenänderung, die Ladung Kapazität mal Spannungsänderung.

| Im Vergleich | In der Schaltung |
|---|---|
| Verschiebung des ersten Wagens | Spannungsänderung am Gate |
| Motor, der den zweiten Wagen gegenläufig bewegt | invertierende Verstärkerstufe |
| Steifigkeit der Feder | Gate-Drain-Kapazität |
| Federkraft | Ladung auf der Kapazität |
| neunmal so steife Feder vor fester Wand | vervielfachte Kapazität gegen Masse |

**Wo der Vergleich nicht stimmt:** In der Schaltung zählt nicht eine Kraft im Gleichgewicht, sondern die Ladung, die in der verfügbaren Zeit fließen muss, also ein Strom; und die Energie für die Gegenbewegung liefert kein Motor, sondern die Versorgung über den Transistor.
:::

:::fehlvorstellung
„Im Abschnürbereich ist $C_{GD}$ null, also kann man die Gate-Drain-Kapazität vergessen.“ Das liegt nahe, weil der abgeschnürte Kanal den Drain nicht erreicht und die Überlappung mit 3,45 fF nur 5 % der Oxidkapazität ausmacht. Die Überlappung bleibt aber, und gerade sie verbindet den Eingang mit dem invertierten Ausgang. Bei $A_V$ = −8 wirkt sie am Eingang wie 31,1 fF, bei −40 wie 141,6 fF, fast dreimal so viel wie $C_{GS}$; in Verstärkerstufen mit hoher Verstärkung bestimmt sie die Eingangskapazität.
:::

::::beispiel Eingangskapazität und Zeitkonstanten der Source-Schaltung
**Gegeben:** Beispiel-NMOS im Abschnürbereich mit $C_{GS}$ = 49,5 fF, $C_{GD}$ = 3,45 fF, $C_{DB}$ = 37,8 fF bei $U_{DB}$ = 1 V, $g_m$ = 1 mS, $g_o$ = 25 µS; Signalquelle mit $R_\mathrm{sig}$ = 10 kΩ; (a) $R_D$ = 10 kΩ, (b) eine ideale Stromquelle statt $R_D$.

**Gesucht:** Verstärkung, $C_\mathrm{ein}$, $C_\mathrm{aus}$ und die Zeitkonstanten an Gate und Drain.

**Rechnung:** (a) Verstärkung mit $G_D$ = 0,1 mS:

$$A_V = -\frac{1\ \mathrm{mS}}{0{,}1\ \mathrm{mS} + 0{,}025\ \mathrm{mS}} = -8$$

Kapazitäten:

$$C_\mathrm{ein} = 49{,}5\ \mathrm{fF} + 3{,}45\ \mathrm{fF}\cdot9 = 80{,}6\ \mathrm{fF}, \qquad C_\mathrm{aus} = 37{,}8\ \mathrm{fF} + 3{,}45\ \mathrm{fF}\cdot\frac{9}{8} = 41{,}7\ \mathrm{fF}$$

Zeitkonstanten, am Drain mit dem Ausgangswiderstand $1/(G_D + g_o)$ = 8 kΩ:

$$\tau_\mathrm{ein} = 10\ \mathrm{k\Omega}\cdot80{,}6\ \mathrm{fF} = 0{,}81\ \mathrm{ns}, \qquad \tau_\mathrm{aus} = 8\ \mathrm{k\Omega}\cdot41{,}7\ \mathrm{fF} = 0{,}33\ \mathrm{ns}$$

(b) Ohne $R_D$ bleibt am Drain nur $g_o$:

$$A_V = -\frac{1\ \mathrm{mS}}{0{,}025\ \mathrm{mS}} = -40, \qquad C_\mathrm{ein} = 49{,}5\ \mathrm{fF} + 3{,}45\ \mathrm{fF}\cdot41 = 191{,}1\ \mathrm{fF}$$

$$\tau_\mathrm{ein} = 10\ \mathrm{k\Omega}\cdot191{,}1\ \mathrm{fF} = 1{,}91\ \mathrm{ns}, \qquad \tau_\mathrm{aus} = 40\ \mathrm{k\Omega}\cdot41{,}4\ \mathrm{fF} = 1{,}65\ \mathrm{ns}$$

**Ergebnis:** **(a) $A_V$ = −8, $C_\mathrm{ein}$ = 80,6 fF, $\tau_\mathrm{ein}$ = 0,81 ns; (b) $A_V$ = −40, $C_\mathrm{ein}$ = 191,1 fF, $\tau_\mathrm{ein}$ = 1,91 ns.**

**Einordnung:** Ohne den Miller-Effekt läge die Zeitkonstante am Gate bei 0,53 ns, 10 kΩ mal 52,9 fF; die 3,45 fF der Überlappung verlängern sie in (a) um die Hälfte und machen in (b) 74 % der Eingangskapazität aus. In (b) ist der Drain fast so langsam wie das Gate; dort ist die Miller-Rechnung nur eine Abschätzung, und man rechnet mit dem Frequenzgang der ganzen Stufe.
::::

:::frage
„Gilt die Rechnung auch beim Sourcefolger?“
Ja, mit der Kapazität, die dort zwischen Eingang und Ausgang liegt. Beim Sourcefolger ist das Gate der Eingang und die Source der Ausgang; sie folgt dem Gate mit dem Faktor 0,80 ([PMOS-Transistor, Substrateffekt und Latch-Up](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/pmos-substrateffekt-latch-up-ausfuehrlich.html)). $C_{GS}$ wirkt am Eingang deshalb nur mit $1 - 0{,}80$, also 9,9 fF statt 49,5 fF, und zusammen mit $C_{GD}$ gegen den festen Drain sind es 13,4 fF statt 52,9 fF. Deshalb puffert man empfindliche Knoten gern mit einem Folger.
:::

## Miller-Kompensation

*Warum schaltet man in Verstärkern absichtlich eine Kapazität zwischen Ein- und Ausgang einer Stufe?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/04-miller-kompensation · Vorlage: schaltung
**Abbildung 11:** Zweistufiger Verstärker als Blockbild: erste Stufe mit 1 MΩ Ausgangswiderstand, zweite Stufe invertierend mit der Verstärkung −50 und einer Kapazität $C_M$ = 1 pF zwischen ihrem Eingang und ihrem Ausgang. Darunter der Ersatz: 51 pF vom Ausgang der ersten Stufe nach Masse. Rechts maßstäblich zwei Quadrate für die Kondensatorfläche bei 1 fF/µm², 32 µm Kantenlänge für 1 pF und 226 µm für 51 pF. Über den Miller-Effekt wirkt ein kleiner Kondensator wie ein 51-mal größerer; das spart Chipfläche.
:::

Ein Operationsverstärker braucht für den Betrieb mit Gegenkopplung einen Knoten, der viel langsamer ist als alle anderen; sonst kommt die Korrektur der Gegenkopplung zu spät, und die Schaltung kann schwingen ([Idealer Operationsverstärker und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung-ausfuehrlich.html)). Man erzeugt ihn mit einer Kapazität $C_M$ zwischen Ein- und Ausgang einer invertierenden Stufe, meist der zweiten; sie verbindet dann den Ausgang der ersten Stufe mit dem Ausgang der letzten. Nach dem Miller-Effekt wirkt sie am Ausgang der ersten Stufe mit dem Faktor $1 - A_2$, bei der Verstärkung $A_2$ = −50 der zweiten Stufe 51-fach (Abbildung 11).

Der Gewinn ist Fläche. Kondensatoren zwischen zwei Metallebenen eines Chips haben rund 1 fF/µm²; 51 pF bräuchten 51 000 µm², ein Quadrat von 226 µm Kantenlänge. Mit dem Miller-Effekt genügen 1 pF auf 1000 µm². Im Operationsverstärker 741 sitzt auf diese Weise ein Kondensator von 30 pF über der zweiten Stufe.

::::beispiel Miller-Kompensation eines zweistufigen Verstärkers
**Gegeben:** zweite Stufe mit $A_2$ = −50, $C_M$ = 1 pF zwischen ihrem Ein- und Ausgang; Ausgangswiderstand der ersten Stufe 1 MΩ; Kondensatorbelag 1 fF/µm² (angenommen).

**Gesucht:** die wirksame Kapazität am Ausgang der ersten Stufe, die Zeitkonstante dort und die eingesparte Fläche.

**Rechnung:** Miller-Faktor und Zeitkonstante:

$$C_\mathrm{wirk} = 1\ \mathrm{pF}\cdot\big(1 + 50\big) = 51\ \mathrm{pF}, \qquad \tau = 1\ \mathrm{M\Omega}\cdot51\ \mathrm{pF} = 51\ \mathrm{\mu s}$$

Flächen:

$$\frac{1\ \mathrm{pF}}{1\ \mathrm{fF/\mu m^2}} = 1000\ \mathrm{\mu m^2}, \qquad \frac{51\ \mathrm{pF}}{1\ \mathrm{fF/\mu m^2}} = 51\,000\ \mathrm{\mu m^2}$$

**Ergebnis:** **51 pF wirksam, Zeitkonstante 51 µs; 1000 µm² statt 51 000 µm².**

**Einordnung:** Die Zeitkonstante von 51 µs ist um Größenordnungen länger als die Nanosekunden an den übrigen Knoten eines solchen Verstärkers; dieser eine Knoten bestimmt dann allein, wie schnell der Verstärker reagiert, und die Gegenkopplung kommt ohne Schwingen zur Ruhe. Mit dem Gateoxid als Dielektrikum, 6,91 fF/µm², wären es 145 µm² statt 7385 µm².
::::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| gesperrt nur 0,30 $C_\mathrm{ox}$ | die Gegenladung sitzt am Rand der Verarmungszone, tief unter dem Oxid |
| Rückkehr auf $C_\mathrm{ox}$ im Transistor | Source und Drain liefern die Kanalelektronen schnell nach |
| $C_{GB}$ fast null in der Inversion | der Bulk liefert nichts mehr, die Gegenladung kommt aus dem Kanal |
| je die Hälfte im ohmschen Bereich | beide Enden des Kanals liefern gleich viel |
| zwei Drittel und null im Abschnürbereich | der abgeschnürte Drain erreicht die Kanalladung nicht mehr |
| Überlappung | Gegenladung im n⁺-Gebiet unter der Gatekante, unabhängig vom Kanal |
| Sperrschichtkapazität sinkt mit der Spannung, der Rand zählt mit | die Gegenladung sitzt am Rand einer Zone, die mit der Spannung breiter wird, an Boden und Seitenwänden |
| Miller-Effekt | die Spannung über $C_{GD}$ ändert sich $(1 - A_V)$-mal so stark wie am Eingang |

Eine Kapazität im MOSFET ist die Ladung, die ein Anschluss je Volt Spannungsänderung liefern muss; ihr Wert hängt davon ab, wo die Gegenladung sitzt und aus welchem Anschluss sie nachfließt, und ihre Wirkung davon, um wie viel sich die Spannung über ihr tatsächlich ändert.

## Bedeutung und Ausblick

In digitalen CMOS-Schaltungen bilden diese Kapazitäten die Last jedes Gatters: das Gate der folgenden Stufe, die Drainkapazitäten der eigenen Transistoren und die Leitung dazwischen. Ihre Summe, geteilt durch den Strom, den die Transistoren liefern, bestimmt die Schaltzeit. In analogen Verstärkern begrenzt vor allem der Miller-Effekt die Bandbreite; Schaltungen wie die Kaskode sind gerade so gebaut, dass sich die Spannung am Drain des Eingangstransistors kaum ändert. Im Layout senkt man die Kapazitäten mit gefalteten Transistoren, kleinen Draingebieten und kurzen Leitungen, und Schaltungssimulatoren rechnen sie aus den Angaben zu Fläche und Umfang von Source und Drain und aus der Überlappung pro Weite. Gemessen werden die Beläge an Teststrukturen, deren Kapazität man über der Spannung aufnimmt.

Die Werte gelten, solange die Kanalladung den Spannungen folgen kann, beim Beispieltransistor bis in den Gigahertzbereich; bei sehr kurzen Kanälen kommen weitere Effekte hinzu. Der nächste Artikel, das Kleinsignalmodell des MOSFET, setzt die Kapazitäten mit Steilheit, Ausgangsleitwert und Substratsteilheit zu einem Ersatzschaltbild für kleine Signale zusammen, auf dem der Frequenzgang aller Transistorgrundschaltungen beruht.

:::kern
- Eine Kapazität zwischen zwei Anschlüssen ist die Ladungsänderung am einen je Spannungsänderung zwischen beiden, bei festen übrigen Spannungen; für das Gate gilt $C_G = C_{GS} + C_{GD} + C_{GB}$.
- Im gesperrten Zustand gehört die Gatekapazität zum Bulk und ist kleiner als $C_\mathrm{ox}$, weil die Verarmungszone in Reihe liegt; die volle Oxidkapazität gibt es dort nur in der Anreicherung.
- Oberhalb der Schwelle liefern Source und Drain die Gegenladung; der Kanal schirmt den Bulk ab, und $C_{GB}$ ist fast null.
- Im ohmschen Bereich gehört je die Hälfte von $C_\mathrm{ox}$ zu Source und Drain; im Abschnürbereich ist $C_{GS} = \tfrac23 C_\mathrm{ox}$, und zum Drain gehört über den Kanal nichts.
- Die Überlappung $C_\mathrm{ov} = C'_\mathrm{ox} W L_\mathrm{ov}$ liegt immer parallel zu $C_{GS}$ und $C_{GD}$; im Abschnürbereich ist sie die ganze Gate-Drain-Kapazität.
- Source und Drain haben Sperrschichtkapazitäten aus Boden und Rand, $C_j = C_{j0}(1 - U_j/U_\mathrm{Diff})^{-m_j}$ mit $m_j$ zwischen 1/3 und 1/2.
- Leitungen sind Plattenkondensatoren mit Randfeld; Bahnen von 4 bis 1 µm Breite über 1 µm Oxid haben das 1,75- bis 3,55-Fache des Plattenwerts.
- Miller-Effekt: $C_\mathrm{ein} = C_{GS} + C_{GD}(1 - A_V)$; bei invertierender Verstärkung wird die kleine Gate-Drain-Kapazität am Eingang vervielfacht.
:::

:::quiz
F: Warum ist die Gatekapazität eines gesperrten NMOS bei 0 V Gatespannung kleiner als die Oxidkapazität?
A: Die Gegenladung kommt und geht am unteren Rand der Verarmungszone, beim Beispiel 36 nm tief; Oxid und Zone liegen wie zwei Kondensatoren in Reihe. Beim Beispieltransistor sind es 20,7 fF statt 69,1 fF.
F: Warum fällt die Gatekapazität des Transistors in der Inversion nicht ab wie die eines MOS-Kondensators bei hoher Frequenz?
A: Beim Kondensator ohne Source und Drain entstehen die Elektronen nur durch Wärme, beim Beispiel in rund 90 s; im Transistor liefern Source und Drain sie über den Kanal mit einer Zeitkonstante von rund 69 ps. Deshalb kehrt die Kapazität auf $C_\mathrm{ox}$ zurück, bei 1 V auf 0,92 $C_\mathrm{ox}$ statt 0,24.
F: Warum ist $C_{GS}$ im Abschnürbereich zwei Drittel der Oxidkapazität?
A: Die Kanalladung fällt von der Source zum Abschnürpunkt wie die Wurzel aus $1 - x/L$. Eine Änderung der Gate-Source-Spannung ändert dieses ganze Profil im selben Verhältnis, und sein Mittelwert ist zwei Drittel des Werts an der Source.
F: Warum verschwindet $C_{GD}$ im Abschnürbereich bis auf die Überlappung?
A: Der Kanal endet am Abschnürpunkt, dessen Potential nur von $U_{GS}$ abhängt. Eine höhere Drainspannung fällt über der verarmten Zone zwischen Abschnürpunkt und Drain ab und ändert die Kanalladung nicht.
F: Warum wirkt $C_{GD}$ am Eingang einer Source-Schaltung vervielfacht?
A: Steigt das Gate, fällt der Drain um das $|A_V|$-Fache. Die Spannung über $C_{GD}$ ändert sich deshalb $(1 - A_V)$-mal so stark wie am Gate, und die entsprechende Ladung muss die Signalquelle liefern; bei $A_V$ = −8 wirken 3,45 fF wie 31,1 fF.
F: Stimmt es, dass die Gatekapazität eines MOSFET immer die Oxidkapazität ist?
A: Nein. Beim Beispieltransistor sind es ohne Überlappung gesperrt bei 0 V 20,7 fF, im Abschnürbereich 46,0 fF und erst im ohmschen Bereich die vollen 69,1 fF.
F: Stimmt es, dass man $C_{GD}$ im Abschnürbereich vernachlässigen kann, weil sie dort null ist?
A: Nein. Die Überlappung von 3,45 fF bleibt, und der Miller-Effekt vervielfacht sie: bei $A_V$ = −8 auf 31,1 fF, bei −40 auf 141,6 fF, fast das Dreifache von $C_{GS}$.
F: Stimmt es, dass gesperrte pn-Übergänge wegen des kleinen Sperrstroms keine nennenswerte Kapazität haben?
A: Nein. Ihre 48 nm dünne Zone hat 2,14 fF/µm²; das Draingebiet des Beispieltransistors kommt bei 1 V auf 37,8 fF, drei Viertel von $C_{GS}$.
F: Wie groß ist die Eingangskapazität einer Source-Schaltung mit $C_{GS}$ = 49,5 fF, $C_{GD}$ = 3,45 fF und $A_V$ = −8?
A: $49{,}5\ \mathrm{fF} + 3{,}45\ \mathrm{fF}\cdot(1 + 8)$ = 80,6 fF, statt 52,9 fF ohne Miller-Effekt.
F: Warum wächst bei kleinen Source- und Draingebieten der Anteil der Seitenwände an der Sperrschichtkapazität?
A: Der Boden zählt mit der Fläche, der Rand mit dem Umfang. Verkleinert man beide Richtungen um den Faktor 4, sinkt der Bodenanteil um den Faktor 16, der Randanteil nur um 4; beim Beispiel steigt der Randanteil von 19 % auf 49 %.
:::
