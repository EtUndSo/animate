---
title: Parasitäre Kapazitäten des MOSFET
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / MOS-Feldeffekttransistoren
order: 33030400
summary: Welche Kapazitäten zwischen den vier Anschlüssen eines MOSFET wirken, wie groß sie in den einzelnen Betriebsbereichen sind und warum die kleine Gate-Drain-Kapazität am Eingang einer Verstärkerstufe vervielfacht erscheint. Kompakte Fassung mit Gatekapazität, Aufteilung auf Source und Drain, Überlappung, Sperrschichtkapazitäten von Source und Drain und Miller-Effekt, durchgerechnet am Beispieltransistor.
tags: MOS-Kapazität, Gate-Kapazität, Überlappkapazität, Sperrschichtkapazität
stil: 3
fassung: kompakt
---

## Worum es geht

Am Gate eines MOSFET fließt kein Gleichstrom, und trotzdem kostet jede Spannungsänderung Strom. Unter dem Gate, im Kanal und an den pn-Übergängen von Source und Drain sitzen Ladungen, die sich mit den Spannungen ändern und dafür durch die Anschlüsse zu- und abfließen müssen. Für die Schaltung sind das Kondensatoren zwischen den vier Anschlüssen, beim Beispieltransistor zwischen 3 fF und 53 fF; sie legen fest, wie schnell sich ein Knoten umladen lässt, und damit die Schaltzeit digitaler Schaltungen und die __Bandbreite__ analoger, die höchste Frequenz, die eine Stufe noch verstärkt. Alles hängt an einem Prinzip:

**Eine Kapazität im MOSFET ist die Ladung, die ein Anschluss je Volt Spannungsänderung liefern muss; ihr Wert hängt davon ab, wo die Gegenladung sitzt und aus welchem Anschluss sie nachfließt, und ihre Wirkung davon, um wie viel sich die Spannung über ihr tatsächlich ändert.**

Vorausgesetzt werden der MOS-Kondensator, die Oxidkapazität und die Schwellenspannung aus [Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise.html), der Kanal und seine Abschnürung aus [Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien.html), der Kondensator aus [Kondensator und Kapazität](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/kondensator-und-kapazitaet.html) und die Sperrschichtkapazität aus [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html). Darauf bauen das Kleinsignalmodell des MOSFET, der Frequenzgang der Transistorgrundschaltungen und die Schaltzeiten von CMOS-Gattern auf.

:::grafik
Szene: st1/mos-feldeffekttransistoren/04-kapazitaeten-uebersicht · Vorlage: querschnitt-beschriftet
**Abbildung 1:** (a) Querschnitt des Beispiel-NMOS, schematisch: Das Gate liegt über 5 nm Oxid und ist 1,1 µm lang, der Kanal darunter 1 µm, sodass es Source und Drain je 50 nm überlappt. Arbeitspunkt $U_{GS}$ = 1 V, $U_{DS}$ = 1 V, Source und Bulk an Masse: Der Kanal endet als Keil vor dem Drain. Kapazitätssymbole an den Orten der Ladung, jeweils mit einer Linie zu dem Anschluss, aus dem die Gegenladung kommt: zwei Überlappungskapazitäten an den Gatekanten (je 3,45 fF), vom Gate zum Kanal $C_{GS}$ (46,0 fF) und $C_{GD}$ (0), durch die Verarmungszone zum Bulk $C_{GB}$ (praktisch 0), an Boden und Rand der n⁺-Gebiete $C_{SB}$ (53,1 fF) und $C_{DB}$ (37,8 fF). (b) Schaltzeichen mit den fünf Kapazitäten zwischen den Anschlüssen: $C_{GS}$ = 49,5 fF mit Überlappung, $C_{GD}$ = 3,45 fF, $C_{GB}$ ≈ 0, $C_{SB}$ = 53,1 fF, $C_{DB}$ = 37,8 fF. Zwischen allen vier Anschlüssen liegen Kapazitäten; ihr Wert hängt davon ab, wo die Ladung sitzt, und ändert sich mit dem Betriebsbereich.
:::

## Von Grund auf: Kondensator, Ladungen im NMOS und Kapazität als Steigung

*Was muss man über Kondensatoren und über den Aufbau des NMOS wissen, bevor man seine Kapazitäten bestimmen kann?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/04-grundlagen · Vorlage: grundlagen-dreiteilig
**Abbildung 2:** Die drei Grundbausteine. (a) Das Gate des Beispieltransistors als Plattenkondensator: eine Platte von 10 µm mal 1 µm über 5 nm Oxid und einer leitenden Gegenplatte, bei 1 V +69,1 fC auf dem Gate und −69,1 fC auf der Gegenplatte, jede Ladung mit einem Pfeil durch ihren eigenen Anschluss; daneben die Spannung über der Zeit beim Laden mit festen 0,25 mA, eine Gerade, die nach 0,28 ns 1 V erreicht, und beim Laden über 10 kΩ, eine Kurve, die nach 0,69 ns 63 % ihres Endwerts erreicht. (b) Querschnitt des Beispiel-NMOS, schematisch: p-Bulk mit ortsfesten negativen Akzeptorrümpfen und beweglichen Löchern (rot), n⁺-Source und n⁺-Drain mit Elektronen (blau), Gate über dem Oxid, grau die Verarmungszonen unter dem Gate und um Source und Drain; oben bei $U_{GS}$ = 1,5 V und kleiner Drain-Source-Spannung mit gleichmäßigem Kanal bis zum Drain, unten bei $U_{GS}$ = $U_{DS}$ = 1 V mit einem Kanal, der als Keil vor dem Drain endet. (c) Ladung, die ins Gate fließt, wenn man es von 0 V an hebt, Source, Drain und Bulk an Masse, über $U_{GS}$ von 0 bis 1,5 V: 9,8 fC bis 0,5 V, 37,1 fC bis 1 V, 69,7 fC bis 1,5 V; orange die Tangenten bei 0 V mit der Steigung 20,7 fF und bei 1 V mit 63,7 fF, grau gestrichelt die Gerade eines Plattenkondensators mit 69,1 fF. Ladung und Gegenladung fließen durch verschiedene Anschlüsse, im Transistor sitzen sie an mehreren Orten, und seine Kapazität ist die Steigung einer gekrümmten Ladungskurve.
:::

### Der Kondensator: Ladung, Gegenladung und Umladezeit

Ein __Kondensator__ besteht aus zwei Leitern, die ein Isolator trennt: Fließt über den Anschluss des einen Ladung zu, fließt über den des anderen ebenso viel ab, und auf ihm bleibt die __Gegenladung__ zurück, gleich groß und mit umgekehrtem Vorzeichen. Die Ladung ist der Spannung proportional, und der Faktor ist die __Kapazität__ ([Der Kondensator und seine Kapazität](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/kondensator-und-kapazitaet.html)):

$$Q = C\,U$$

Das Gate des Beispieltransistors, eine Platte von 10 µm mal 1 µm über 5 nm Oxid, hätte über einer leitenden Gegenplatte 69,1 fF, die __Oxidkapazität__ $C_\mathrm{ox}$, und trüge bei 1 V 69,1 fC (Abbildung 2a). Ladung fließt nur, während sich die Spannung ändert, und das kostet Zeit: Mit 0,25 mA braucht die Oxidkapazität für 1 V 0,28 ns, und über 10 kΩ geladen ist ihre __Zeitkonstante__, Widerstand mal Kapazität, 0,69 ns ([Laden und Entladen des Kondensators](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/laden-und-entladen.html)).

:::frage
„Fließt beim Umladen ein Strom durch das Oxid?“
Nein, kein Elektron durchquert das Oxid. In den einen Anschluss fließt Ladung hinein, aus dem anderen gleich viel heraus, und dazwischen ändert sich nur das elektrische Feld im Isolator. Von außen sieht es trotzdem aus, als flösse der Strom hindurch, weil in jedem Augenblick beide Ströme gleich sind: Lädt man die Oxidkapazität mit 0,25 mA in 0,28 ns um 1 V, fließen 0,25 mA ins Gate, und dieselben 0,25 mA fließen über einen anderen Anschluss aus dem Silizium ab. Durch das Gate fließt deshalb nur während einer Änderung Strom, bei festen Spannungen keiner.
:::

### Der NMOS: wo im Transistor Ladung sitzt

Im __NMOS__-Transistor (Abbildung 2b) liegen in p-dotiertem Silizium, dem __Bulk__, zwei stark n-dotierte Gebiete voller beweglicher Elektronen, __Source__ und __Drain__, und zwischen ihnen auf dem Oxid das __Gate__. Im Bulk tragen bewegliche __Löcher__, Fehlstellen mit positiver Ladung, den Strom; wo sie fehlen, bleiben die ortsfesten negativen Rümpfe der Dotieratome zurück, eine __Verarmungszone__, an pn-Übergängen auch __Raumladungszone__ genannt, die für Gleichstrom isoliert: um Source und Drain und unter dem Gate, beim Beispieltransistor schon bei 0 V. Liegt das Gate mehr als die __Schwellenspannung__ $U_{th}$ = 0,5 V über der Source, sammeln sich unter dem Oxid Elektronen aus Source und Drain zum __Kanal__. Bei kleiner Drain-Source-Spannung reicht er gleichmäßig bis zum Drain, im __ohmschen Bereich__; übersteigt sie die __Übersteuerung__ $U_{GS} - U_{th}$, um die das Gate die Schwelle übersteigt, endet er vor dem Drain, im __Abschnürbereich__, zum Beispiel bei $U_{GS}$ = $U_{DS}$ = 1 V ([Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien.html)).

### Kapazität als Steigung

Im Halbleiter sitzt die Gegenladung nicht auf einer festen Fläche: Mit der Spannung wird eine Verarmungszone breiter, oder ein Kanal entsteht und füllt sich, und die Ladung wächst nicht mehr proportional. Hebt man das Gate des Beispieltransistors bei Source, Drain und Bulk an Masse von 0 auf 0,5 V, fließen nur 9,8 fC zu, von 0,5 auf 1 V dagegen 27,3 fC (Abbildung 2c). Für eine kleine Änderung um einen festen Betriebszustand, den __Arbeitspunkt__, zählt nur die Steigung der __Tangente__ dort, die __Kleinsignalkapazität__:

$$C = \frac{\mathrm dQ}{\mathrm dU}$$

Beim Beispieltransistor sind es bei 0 V 20,7 fF und bei 1 V 63,7 fF. Alle Kapazitäten dieses Artikels sind solche Steigungen in einem Arbeitspunkt.

## Kapazitäten zwischen den Anschlüssen

*Was bedeutet Kapazität bei einem Bauelement mit vier Anschlüssen?*

Ein Versuch am Beispieltransistor zeigt es. Er arbeitet mit $U_{GS}$ = 1 V und $U_{DS}$ = 1 V im Abschnürbereich, Source und Bulk an Masse. Hebt man das Gate um 10 mV an und hält die übrigen Anschlüsse fest, fließen 0,53 fC ins Gate, für diese kleine Änderung also 53 fF. Senkt man stattdessen bei festem Gate die Source um 10 mV, sind es 0,495 fC, beim Drain 0,035 fC und beim Bulk praktisch nichts. Die 53 fF verteilen sich demnach auf 49,5 fF zur Source, 3,45 fF zum Drain und nichts zum Bulk.

In Worten: Die Kapazität zwischen dem Gate und einem anderen Anschluss ist die Änderung der Gateladung je Änderung der Spannung zwischen beiden, während die Spannungen zu den übrigen Anschlüssen fest bleiben. So definiert, lässt sich der Transistor in einer Schaltung durch Kondensatoren zwischen seinen Anschlüssen ersetzen.

**Die Akteure:**

- __$Q_G$__: Ladung auf dem Gate; in fC; im Betrieb positiv.
- __$U_{GD}$__, __$U_{GB}$__: Spannung vom Gate zum Drain bzw. zum Bulk; $U_{GD}$ ist $U_{GS} - U_{DS}$, im Arbeitspunkt oben 0 V, $U_{GB}$ ist dort 1 V.
- __$C_{GS}$__, __$C_{GD}$__, __$C_{GB}$__: Gate-Source-, Gate-Drain- und Gate-Bulk-Kapazität; in fF; im Arbeitspunkt oben 49,5 fF, 3,45 fF und praktisch 0. In Kleinsignal-Ersatzschaltbildern auch $C_{gs}$ geschrieben.
- __$C_G$__: Kapazität des ganzen Gates; 53 fF im Arbeitspunkt oben.

:::formel Definition
$$C_{GS} = \frac{\partial Q_G}{\partial U_{GS}}, \qquad C_{GD} = \frac{\partial Q_G}{\partial U_{GD}}, \qquad C_{GB} = \frac{\partial Q_G}{\partial U_{GB}}$$
:::

**So liest man das:** Jede Kapazität ist eine partielle Ableitung, nach einer der drei Spannungen bei festen beiden anderen; ∂ statt d zeigt an, dass $Q_G$ von mehreren Spannungen abhängt. Wie jede Kleinsignalkapazität (Abschnitt *Von Grund auf*) gelten die Werte für kleine Änderungen um einen Arbeitspunkt und hängen von ihm ab. Bewegt sich nur das Gate, wachsen alle drei Spannungen gleich, und es gilt

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

Für die pn-Übergänge von Source und Drain gilt dasselbe mit der Ladung in ihren Raumladungszonen. Zwischen den vier Anschlüssen liegen damit sieben Kapazitäten:

| Kapazität | Ladung, Gegenladung und Abhängigkeit |
|---|---|
| $C_{GS}$, $C_{GD}$ | Gate über dem Kanal gegen die Kanalelektronen aus Source und Drain; hängt vom Betriebsbereich ab |
| $C_{GB}$ | Gate über dem Kanal gegen Akzeptorrümpfe und Löcher, die der Bulk liefert; stark von $U_{GS}$ abhängig, mit Kanal fast null |
| zwei $C_\mathrm{ov}$ | Überlappung: Gatekante gegen die Elektronen von Source bzw. Drain; fast konstant |
| $C_{SB}$, $C_{DB}$ | Raumladung um Source bzw. Drain gegen Akzeptorrümpfe am Rand zum Bulk; hängt von der Sperrspannung ab |

Die beiden Überlappungskapazitäten $C_\mathrm{ov}$ addieren sich zu $C_{GS}$ und $C_{GD}$; die direkte Kapazität zwischen Source und Drain ist klein und wird vernachlässigt.

## Die Gatekapazität vom gesperrten Zustand bis zur Inversion

*Wo sitzt die Gegenladung zur Gateladung, und warum hängt die Gatekapazität so stark von der Gatespannung ab?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/04-gatekapazitaet · Vorlage: kennlinie-anteile
**Abbildung 3:** Gatekapazität des Beispieltransistors bezogen auf $C_\mathrm{ox}$ = 69,1 fF über $U_{GS}$ von −2,5 V bis 2,5 V, Drain und Bulk auf dem Potential der Source. Obere Kante: gesamte Gatekapazität, 0,96 bei −2,5 V, 0,73 bei der Flachbandspannung −1,03 V, 0,30 bei 0 V, Minimum 0,26 bei 0,35 V, 0,40 an der Schwelle 0,5 V, 0,92 bei 1 V und 0,98 bei 2,5 V. Darunter als gestapelte Flächen der Bulkanteil $C_{GB}$ (grau), bis 0 V gleich der ganzen Kapazität, an der Schwelle 0,198 und bei 1 V 0,015, und der Kanalanteil $C_{GS} + C_{GD}$ (blau, je zur Hälfte Source und Drain), an der Schwelle ebenfalls 0,198, bei 1 V 0,907 und bei 2,5 V 0,976. Gestrichelt der MOS-Kondensator ohne Source und Drain bei hoher Frequenz, 0,25 an der Schwelle und 0,23 bei 2,5 V. Unterhalb der Schwelle liegt die Gegenladung im Bulk, oberhalb liefern Source und Drain die Elektronen; im Transistor kehrt die Gatekapazität deshalb auch bei hoher Frequenz auf $C_\mathrm{ox}$ zurück, und der Bulkanteil verschwindet.
:::

Abbildung 3 trägt die Steigung der Ladungskurve aus Abbildung 2c über einem größeren Spannungsbereich auf, aufgeteilt nach dem Anschluss, aus dem die Gegenladung kommt. Mit Source, Drain und Bulk auf demselben Potential ist der Transistor ein MOS-Kondensator, und seine drei Zustände kennt man aus [Aufbau und Funktionsweise des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise.html): __Anreicherung__ mit Löchern an der Oberfläche, __Verarmung__, wenn die Löcher verdrängt sind und unter dem Gate eine Verarmungszone liegt, und __Inversion__ mit Elektronen an der Oberfläche, dem Kanal. Für die Kapazität zählt jeweils, wo die Gegenladung zu- und abfließt.

**Die Akteure:**

- __$C'_\mathrm{ox}$__, __$C_\mathrm{ox}$__: Kapazität des Oxids pro Fläche bzw. über der Kanalfläche $W L$; 6,91 fF/µm² und 69,1 fF bei 5 nm Oxid und 10 µm². Der Strich kennzeichnet einen auf die Fläche bezogenen Wert.
- __$U_\mathrm{FB}$__: __Flachbandspannung__, bei der die Siliziumoberfläche ungeladen ist; −1,03 V beim Gate aus n⁺-Polysilizium.
- __$y_d$__: Tiefe der Verarmungszone unter dem Gate; 35,9 nm bei $U_{GS}$ = 0.
- __$C_\mathrm{dep}$__: Kapazität der Verarmungszone unter dem Gate, $\varepsilon_\mathrm{Si} W L/y_d$; 28,9 fF bei $U_{GS}$ = 0.

**Das Zusammenspiel:** Unterhalb der Flachbandspannung liegt die Gegenladung als Löcherschicht direkt unter dem Oxid, nachgeliefert über den Bulk; die Kapazität ist fast die des Oxids, bei −2 V 65,4 fF. In der Verarmung kommt und geht die Ladung am unteren Rand der Verarmungszone, $y_d$ tief im Silizium. Oxid und Zone liegen dann wie zwei Kondensatoren in Reihe, und bei $U_{GS}$ = 0 bleiben nur 0,30 $C_\mathrm{ox}$, 20,7 fF:

$$C_{GB} = \frac{C_\mathrm{ox}\,C_\mathrm{dep}}{C_\mathrm{ox} + C_\mathrm{dep}}$$

**So liest man das:** Die Formel gilt in der Verarmung, zwischen Flachbandspannung und Beginn der Inversion. Die Gate-Bulk-Kapazität ist kleiner als jede der beiden Teilkapazitäten; je tiefer die Zone, desto kleiner $C_\mathrm{dep}$ und $C_{GB}$.

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

**Gesucht:** Tiefe der Verarmungszone, $C_\mathrm{dep}$ und $C_{GB}$ bei $U_{GS}$ = 0.

**Rechnung:** Tiefe der Zone und ihre Kapazität über 10 µm² = 10⁻⁷ cm²:

$$y_d = \sqrt{\frac{2\cdot1{,}036\cdot10^{-12}\ \mathrm{F/cm}\cdot0{,}566\ \mathrm V}{1{,}602\cdot10^{-19}\ \mathrm C\cdot5{,}68\cdot10^{17}\ \mathrm{cm^{-3}}}} = 35{,}9\ \mathrm{nm}$$

$$C_\mathrm{dep} = \frac{1{,}036\cdot10^{-12}\ \mathrm{F/cm}\cdot10^{-7}\ \mathrm{cm^2}}{3{,}59\cdot10^{-6}\ \mathrm{cm}} = 28{,}9\ \mathrm{fF}$$

Reihenschaltung mit dem Oxid:

$$C_{GB} = \frac{69{,}06\ \mathrm{fF}\cdot28{,}9\ \mathrm{fF}}{69{,}06\ \mathrm{fF} + 28{,}9\ \mathrm{fF}} = 20{,}4\ \mathrm{fF}$$

**Ergebnis:** **$C_{GB}$ = 20,4 fF nach der Verarmungsnäherung, 20,7 fF nach der vollständigen Rechnung, also 0,30 $C_\mathrm{ox}$.**

**Einordnung:** Ein gesperrter Transistor mit dem Gate auf 0 V belastet die treibende Stufe nur mit knapp einem Drittel seiner Oxidkapazität. Die volle Oxidkapazität erreicht er erst in der Anreicherung, bei Gatespannungen deutlich unter −1 V, die in normalen Schaltungen nicht vorkommen.
::::

An der Schwelle sammeln sich Elektronen an der Oberfläche, und hier trennen sich Transistor und MOS-Kondensator. Ohne Source und Drain können die Elektronen nur durch Wärme entstehen; beim Beispiel dauert der Aufbau der Inversionsschicht rund 90 s, ihre Zahl folgt schnellen Änderungen nicht, und die Kapazität bleibt bei 0,23 bis 0,25 $C_\mathrm{ox}$ (Abbildung 3, gestrichelt). Im Transistor grenzen die n⁺-Gebiete mit 10²⁰ Elektronen pro Kubikzentimeter unmittelbar an den Kanal und liefern nach, mit der Zeitkonstante aus Kanalwiderstand und Oxidkapazität: 1 kΩ mal 69 fF, also 69 ps bei $U_{GS}$ = 1 V. Seine Gatekapazität kehrt deshalb oberhalb der Schwelle bis zu Frequenzen im Gigahertzbereich auf $C_\mathrm{ox}$ zurück, 0,92 $C_\mathrm{ox}$ bei 1 V.

Dabei wechselt der Ort der Gegenladung. Genau an der Schwelle teilt sich eine zusätzliche Gateladung je zur Hälfte auf Verarmungszone und Kanalelektronen auf. Darüber bleibt die Oberfläche an ihr Potential gebunden, von 0,5 V auf 1 V Gatespannung steigt es nur um 105 mV; bei 1 V kommen 98,3 % jeder zusätzlichen Gateladung aus Source und Drain. Der Kanal schirmt den Bulk ab, $C_{GB}$ fällt praktisch auf null, und die Gatekapazität gehört nun zu Source und Drain.

## Überlappung des Gates

*Welche Kapazität bilden die Ränder des Gates über Source und Drain?*

Das Gate ist etwas länger als der Kanal darunter und reicht auf beiden Seiten über Source und Drain, beim Beispieltransistor je 50 nm: 1,1 µm Gate über 1 µm Kanal. Über diesen Streifen bildet es mit dem leitenden n⁺-Gebiet einen Plattenkondensator, dessen Gegenladung aus Source bzw. Drain kommt, gleichgültig, ob darunter ein Kanal besteht und ob er abgeschnürt ist.

:::frage
„Warum überlappt das Gate Source und Drain überhaupt, wenn das nur Kapazität kostet?“
Source und Drain werden erst eingebracht, wenn das Gate schon steht: Man schießt die Dotierstoffe mit dem Gate als Maske ein, sodass die n⁺-Gebiete von selbst genau an den Gatekanten beginnen; ein solches Gate heißt __selbstjustiert__. Beim anschließenden Ausheilen bei rund 1000 °C wandern die Dotierstoffe ein Stück zur Seite und damit unter das Gate. Ohne diese Überlappung bliebe zwischen Kanal und n⁺-Gebiet ein Streifen, über dem kein Gate liegt; er würde nicht invertiert und trennte den Kanal vom Drain. Man hält die Überlappung deshalb klein, aber nicht null.
:::

**Die Akteure:**

- __$L_\mathrm{ov}$__: Länge, um die das Gate über Source bzw. Drain reicht (ov für englisch overlap); 50 nm je Seite.
- __$C_\mathrm{ov}$__: __Überlappungskapazität__ je Seite; 3,45 fF, 5 % von $C_\mathrm{ox}$. Sie addiert sich zu $C_{GS}$ bzw. $C_{GD}$.

:::formel Formel
$$C_\mathrm{ov} = C'_\mathrm{ox}\,W\,L_\mathrm{ov}$$
:::

**So liest man das:** Die Überlappungskapazität ist die Oxidkapazität der Fläche $W L_\mathrm{ov}$; gemessen an der Oxidkapazität über dem Kanal ist sie $L_\mathrm{ov}/L$. Weil das n⁺-Gebiet immer leitet, hängt sie kaum von den Spannungen ab. Das Randfeld von der Flanke des Gates zu Source und Drain kommt hinzu; Schaltungssimulatoren führen beides zusammen als Wert pro Weite, beim Beispiel 0,345 fF/µm.

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
- __$U(x)$__: Kanalpotential an der Stelle $x$ gegenüber der Source; die Elektronenladung pro Fläche ist dort $C'_\mathrm{ox}$ mal der örtlichen __Übersteuerung__ $U_{GS} - U_{th} - U(x)$, um die das Gate die Schwelle gegenüber dem Kanal an dieser Stelle übersteigt ([Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien.html)).
- __$U_{GD} - U_{th}$__: Übersteuerung am Drain-Ende; positiv, solange der Kanal den Drain erreicht, bei 1 V/1 V −0,5 V, der Kanal ist dort abgeschnürt.

**Das Zusammenspiel:**

**Schritt 1**: Oberhalb der Schwelle kommt die Gegenladung fast ganz aus Kanalelektronen, und jedes davon stammt aus Source oder Drain; wie viele aus welchem Anschluss kommen, legt $C_{GS}$ und $C_{GD}$ fest.

**Schritt 2**: Eine Anschlussspannung ändert die Ladung nur dort, wo sich mit ihr das Kanalpotential und damit die örtliche Übersteuerung ändert.

**Schritt 3**: Im ohmschen Bereich bei kleiner Drain-Source-Spannung ist der Kanal gleichmäßig (Abbildung 4a). Hebt man die Source um 10 mV, sinkt die Übersteuerung an der Source um 10 mV und am Drain gar nicht, dazwischen linear; im Mittel ändert sich die Ladung um die Hälfte. $C_{GS}$ und ebenso $C_{GD}$ sind je die halbe Oxidkapazität, 34,5 fF.

**Schritt 4** (entscheidender Schritt): Im Abschnürbereich endet der Kanal vor dem Drain am Abschnürpunkt, dessen Potential $U_{GS} - U_{th}$ über der Source liegt; den Rest der Drain-Source-Spannung nimmt die kurze verarmte Zone davor auf. Hebt man den Drain an, ändert sich im Kanal nichts, und $C_{GD}$ ist null.

**Schritt 5**: Die Ladung fällt jetzt wie die Wurzel aus $1 - x/L$ von 3,45 fC/µm² auf null (Abbildung 4b). Hebt man die Source um 10 mV, schrumpft das ganze Profil im selben Verhältnis, und sein Mittelwert ist zwei Drittel des Werts an der Source: $C_{GS}$ ist $\tfrac23 C_\mathrm{ox}$, 46,0 fF. Bei 10 mV fließen 0,46 fC, 2874 Elektronen, in die Source zurück.

:::formel Formel
Ohmscher Bereich, kleine $U_{DS}$:

$$C_{GS} = C_{GD} = \frac{1}{2}\,C_\mathrm{ox}$$

Abschnürbereich:

$$C_{GS} = \frac{2}{3}\,C_\mathrm{ox}, \qquad C_{GD} = 0$$
:::

**So liest man das:** Die Formel nennt den Anteil der Oxidkapazität, der zur Source bzw. zum Drain gehört; die Überlappung aus dem vorigen Abschnitt kommt jeweils hinzu. Im ohmschen Bereich teilen sich Source und Drain den symmetrischen Kanal. Im Abschnürbereich hängt die Kanalladung nur noch von $U_{GS}$ ab, und die Gatekapazität ist ein Drittel kleiner. Zum Bulk gehört in beiden Bereichen nichts, weil der Kanal ihn abschirmt.

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

**Gesucht:** $C_{GS}$ und $C_{GD}$ mit Überlappung; in (a) außerdem die Kanalladung und die Zahl der Elektronen, die in die Source zurückfließen, wenn sie um 10 mV angehoben wird.

**Rechnung:** (a) $U_{DS}$ = 1 V liegt über $U_{GS} - U_{th}$ = 0,5 V, also Abschnürbereich:

$$C_{GS} = \frac{2}{3}\cdot69{,}06\ \mathrm{fF} + 3{,}45\ \mathrm{fF} = 49{,}5\ \mathrm{fF}, \qquad C_{GD} = 0 + 3{,}45\ \mathrm{fF} = 3{,}45\ \mathrm{fF}$$

$$Q_K = 46{,}0\ \mathrm{fF}\cdot0{,}5\ \mathrm V = 23{,}0\ \mathrm{fC}, \qquad \frac{46{,}0\ \mathrm{fF}\cdot10\ \mathrm{mV}}{1{,}602\cdot10^{-19}\ \mathrm C} = 2874$$

(b) Ohmscher Bereich bei kleiner $U_{DS}$:

$$C_{GS} = C_{GD} = \frac{1}{2}\cdot69{,}06\ \mathrm{fF} + 3{,}45\ \mathrm{fF} = 38{,}0\ \mathrm{fF}$$

**Ergebnis:** **(a) $C_{GS}$ = 49,5 fF, $C_{GD}$ = 3,45 fF, $Q_K$ = 23,0 fC, 2874 Elektronen; (b) je 38,0 fF.**

**Einordnung:** Im ohmschen Bereich hängt das Gate zu gleichen Teilen an Source und Drain, zusammen 76,0 fF; im Abschnürbereich sind es 53,0 fF, und zum Drain gehört nur noch die Überlappung, 7 % dessen, was zur Source gehört. Gerade diese kleine Gate-Drain-Kapazität verbindet in einer Verstärkerstufe den Ausgang mit dem Eingang.
::::

:::grafik
Szene: st1/mos-feldeffekttransistoren/04-cgs-cgd-uds · Vorlage: kennlinie
**Abbildung 5:** $C_{GS}$ und $C_{GD}$ des Beispieltransistors über $U_{DS}$ von 0 bis 2 V bei $U_{GS}$ = 1,5 V, ohne Überlappung. $C_{GS}$ steigt von 34,5 fF über 40,9 fF bei 0,5 V auf 46,0 fF an der Abschnürgrenze bei 1 V, $C_{GD}$ fällt von 34,5 fF über 25,6 fF auf null; die Summe sinkt von 69,1 fF auf 46,0 fF und bleibt danach konstant. Gestrichelt dieselben Kurven mit je 3,45 fF Überlappung. Darüber kleine Bilder des Kanals bei 0, 0,5 V und 1 V. Mit wachsender Drain-Source-Spannung wandert die Gatekapazität vom Drain zur Source; ab der Abschnürgrenze gehört zum Drain nur noch die Überlappung.
:::

Zwischen beiden Grenzfällen geht die Aufteilung stetig über (Abbildung 5): Mit wachsender Drain-Source-Spannung wird der Kanal zum Drain hin dünner, und der Drain erreicht weniger Ladung. Bei $U_{GS}$ = 1,5 V und $U_{DS}$ = 0,5 V gehören 40,9 fF zur Source und 25,6 fF zum Drain; die allgemeine Formel dafür, das Meyer-Modell, leitet die ausführliche Fassung her.

Zusammengefasst für den Beispieltransistor mit Source und Bulk an Masse: gesperrt bei $U_{GS}$ = 0, im Abschnürbereich bei $U_{GS}$ = $U_{DS}$ = 1 V, im ohmschen Bereich bei kleiner $U_{DS}$; alle Werte in fF und mit den Überlappungen. Gesperrt bilden die Überlappungen alles, was zu Source und Drain gehört, und $C_{GB}$ ist die Reihenschaltung aus Oxid und Verarmungszone; oberhalb der Schwelle kommen $\tfrac23 C_\mathrm{ox}$ bzw. je $\tfrac12 C_\mathrm{ox}$ hinzu.

| in fF | gesperrt | abge­schnürt | ohmsch |
|---|---|---|---|
| $C_{GS}$ | 3,45 | 49,5 | 38,0 |
| $C_{GD}$ | 3,45 | 3,45 | 38,0 |
| $C_{GB}$ | 20,7 | ≈ 0 | ≈ 0 |
| $C_G$ | 27,6 | 53,0 | 76,0 |

Vom gesperrten Zustand bis in den ohmschen Bereich wächst die Gatekapazität auf fast das Dreifache, und ihre Gegenladung wechselt dabei vom Bulk zur Source und schließlich zu Source und Drain je zur Hälfte.

:::fehlvorstellung
„Die Gatekapazität eines MOSFET ist die Oxidkapazität, Permittivität mal Gatefläche durch Oxiddicke.“ Das liegt nahe, weil Gate, Oxid und Kanal wie ein Plattenkondensator aussehen. Das ist sie aber nur, wenn die Gegenladung unmittelbar unter dem Oxid sitzt und von beiden Kanalenden nachfließen kann. Beim Beispieltransistor sind es gesperrt bei 0 V 20,7 fF statt 69,1 fF, weil die Verarmungszone in Reihe liegt, und im Abschnürbereich 46,0 fF, weil der Kanal vor dem Drain endet; erst im ohmschen Bereich wird die volle Oxidkapazität erreicht.
:::

## Sperrschichtkapazitäten von Source und Drain

*Welche Kapazität haben Source und Drain gegen den Bulk, und warum zählt neben der Fläche auch der Rand?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/04-sperrschicht-geometrie · Vorlage: querschnitt-und-aufsicht
**Abbildung 6:** (a) Aufsicht auf das Draingebiet des Beispieltransistors: 10 µm entlang der Gatekante, 2 µm vom Gate bis zum Ende des Gebiets; Fläche 20 µm² schraffiert, Umfang 24 µm als dicke Randlinie. (b) Querschnitt quer zur Gatekante: n⁺-Gebiet 0,2 µm tief, umgeben von der Raumladungszone, ohne Spannung 48,4 nm und bei 1 V 67,9 nm breit; Kondensatorsymbole am Boden, 2,14 fF/µm², und an den Seitenwänden, 0,428 fF pro µm Rand. An der Gatekante grenzt die Wand an das p-Gebiet unter dem nur wenige Nanometer dicken Kanal. Ohne Spannung entfallen 42,9 fF auf den Boden und 10,3 fF auf den Rand. Die Kapazität eines Source- oder Draingebiets besteht aus Boden und Rand; der Boden zählt mit seiner Fläche, der Rand mit seiner Länge.
:::

Source und Drain bilden mit dem p-Gebiet je einen pn-Übergang, der im Betrieb gesperrt ist, weil der Bulk an der niedrigsten Spannung liegt. Die Raumladungszone dazwischen ist beim Beispieltransistor ohne Spannung 48,4 nm breit und liegt fast ganz im schwächer dotierten p-Gebiet. Wächst die Spannung zwischen Drain und Bulk, wird sie breiter: Am Rand werden weitere Akzeptorrümpfe frei, deren Löcher über den Bulk abfließen, und ebenso viele Elektronen verlassen das n⁺-Gebiet über den Drain. Diese Ladung je Spannungsänderung ist die __Sperrschichtkapazität__, die eines Plattenkondensators, dessen Plattenabstand mit der Spannung wächst. Für Gleichstrom isoliert der gesperrte Übergang, für Änderungen nicht: Die Drainkapazität des Beispieltransistors erreicht drei Viertel von $C_{GS}$.

**Die Akteure:**

- __$U_j$__: Spannung am Übergang, in Durchlassrichtung vom p- zum n-Gebiet gezählt (j für englisch junction); beim Drain $-U_{DB}$, im Betrieb negativ.
- __$U_\mathrm{Diff}$__: Diffusionsspannung des Übergangs, die Spannung, die ohne äußere Spannung über der Zone liegt; 1,03 V beim Beispieltransistor. Über der Zone liegt die Spannung $U_\mathrm{Diff} - U_j$.
- __$w$__: Breite der Raumladungszone; 48,4 nm ohne Spannung, 67,9 nm bei $U_{DB}$ = 1 V.
- __$C_j$__, __$C_{j0}$__: Sperrschichtkapazität bei der Spannung $U_j$ bzw. ohne Spannung; beim Draingebiet 37,8 fF bei 1 V und 53,1 fF ohne Spannung.
- __$m_j$__: Exponent, der vom Verlauf der Dotierung abhängt; 1/2 bei einem abrupten Übergang, an dem die Dotierung sprunghaft wechselt, 1/3 bei einem linear verlaufenden.

:::formel Gesetz
$$C_j = C_{j0}\,\Big(1 - \frac{U_j}{U_\mathrm{Diff}}\Big)^{-m_j}$$
:::

**So liest man das:** In Sperrrichtung ist $U_j$ negativ, die Klammer größer als 1 und die Kapazität kleiner als $C_{j0}$; je größer die Sperrspannung, desto breiter die Zone und desto kleiner die Kapazität. Für den Drain des NMOS, mit $U_j$ = $-U_{DB}$:

$$C_{DB} = C_{DB0}\,\Big(1 + \frac{U_{DB}}{U_\mathrm{Diff}}\Big)^{-m_j}$$

Bei 1 V und $m_j$ = 1/2 sinkt sie auf das 0,712-Fache, bei 2,5 V auf das 0,540-Fache.

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

Die Zone umgibt das n⁺-Gebiet am Boden und an allen vier Seitenwänden (Abbildung 6). Weil die Tiefe der Gebiete im Herstellungsprozess fest ist, genügen zwei Technologiewerte: einer pro Fläche für den Boden, einer pro Länge für den Rand.

**Die Akteure:**

- __$C'_{jF}$__: Sperrschichtkapazität des Bodens pro Fläche; 2,14 fF/µm² ohne Spannung.
- __$C'_{jS}$__: Sperrschichtkapazität der Seitenwände pro Länge des Randes; 0,428 fF/µm ohne Spannung. Der Strich bedeutet hier den Bezug auf die Länge.
- __$x_j$__: Tiefe der n⁺-Gebiete; 0,2 µm.
- __$b$__: Länge des Draingebiets von der Gatekante bis zu seinem Ende; 2 µm.
- __$A_D$__, __$P_D$__: Fläche und Umfang des Draingebiets in der Aufsicht; 20 µm² und 24 µm.

:::formel Formel
$$C_{DB} = C'_{jF}\,A_D + C'_{jS}\,P_D, \qquad A_D = W\,b, \qquad P_D = 2\,\big(W + b\big)$$
:::

**So liest man das:** Der Boden zählt mit seiner Fläche, der Rand mit seiner Länge; beide Beläge folgen bei derselben Spannung dem Gesetz oben. Beim Beispiel sind es ohne Spannung 42,9 fF Boden und 10,3 fF Rand, zusammen 53,1 fF. Die Wand an der Gatekante zählt mit, weil der Kanal davor nur wenige Nanometer dick ist. Schaltungssimulatoren erwarten deshalb für jeden Transistor Fläche und Umfang von Source und Drain.

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

::::beispiel Sperrschichtkapazität des Draingebiets
**Gegeben:** p-Gebiet mit $N_A$ = 5,68·10¹⁷ cm⁻³, n⁺-Gebiete so stark dotiert, dass nur $N_A$ zählt; $U_\mathrm{Diff}$ = 1,027 V, $\varepsilon_\mathrm{Si}$ = 1,036·10⁻¹² F/cm, $e$ = 1,602·10⁻¹⁹ C, Tiefe $x_j$ = 0,2 µm, $m_j$ = 1/2. Draingebiet $W$ = 10 µm, $b$ = 2 µm; $U_{DB}$ = 1 V. (b) Alle Abmessungen des Gebiets geviertelt.

**Gesucht:** die Beläge, $C_{DB}$ ohne Spannung und bei 1 V, der Randanteil; für (b) die Anteile ohne Spannung.

**Rechnung:** Breite der Zone ohne Spannung; der Bruch mit $N_A$ und $N_D$ wird zu $1/N_A$:

$$w_0 = \sqrt{\frac{2\cdot1{,}036\cdot10^{-12}\ \mathrm{F/cm}\cdot1{,}027\ \mathrm V}{1{,}602\cdot10^{-19}\ \mathrm C\cdot5{,}68\cdot10^{17}\ \mathrm{cm^{-3}}}} = 48{,}4\ \mathrm{nm}$$

Beläge:

$$C'_{jF} = \frac{1{,}036\cdot10^{-12}\ \mathrm{F/cm}}{4{,}84\cdot10^{-6}\ \mathrm{cm}} = 2{,}14\ \mathrm{fF/\mu m^2}, \qquad C'_{jS} = 2{,}14\ \mathrm{fF/\mu m^2}\cdot0{,}2\ \mathrm{\mu m} = 0{,}428\ \mathrm{fF/\mu m}$$

Ohne Spannung und bei 1 V:

$$\begin{aligned} C_{DB0} &= 2{,}14\ \mathrm{fF/\mu m^2}\cdot20\ \mathrm{\mu m^2} + 0{,}428\ \mathrm{fF/\mu m}\cdot24\ \mathrm{\mu m} \\ &= 42{,}9\ \mathrm{fF} + 10{,}3\ \mathrm{fF} = 53{,}1\ \mathrm{fF} \end{aligned}$$

$$C_{DB} = 53{,}1\ \mathrm{fF}\cdot\Big(1 + \frac{1\ \mathrm V}{1{,}027\ \mathrm V}\Big)^{-1/2} = 37{,}8\ \mathrm{fF}$$

(b) Geviertelt, 2,5 µm mal 0,5 µm, also 1,25 µm² und 6 µm Umfang:

$$2{,}14\ \mathrm{fF/\mu m^2}\cdot1{,}25\ \mathrm{\mu m^2} = 2{,}68\ \mathrm{fF}, \qquad 0{,}428\ \mathrm{fF/\mu m}\cdot6\ \mathrm{\mu m} = 2{,}57\ \mathrm{fF}$$

**Ergebnis:** **$C_{DB}$ = 53,1 fF ohne Spannung und 37,8 fF bei 1 V, davon 19 % aus dem Rand; geviertelt 5,25 fF mit 49 % Randanteil.**

**Einordnung:** Die Drainkapazität ist drei Viertel so groß wie $C_{GS}$ und elfmal so groß wie $C_{GD}$; am Ausgang einer Verstärkerstufe ist sie meist die größte Kapazität. Beim Verkleinern schrumpft der Boden um den Faktor 16, der Rand nur um 4, deshalb gibt man in feinen Prozessen beide Beläge getrennt an.
::::

Dazu kommen die Leitungen zwischen den Transistoren. Eine Metallbahn über 1 µm Oxid ist ein Kondensator gegen das Substrat; eine 2 µm breite und 1 mm lange Bahn hat als Plattenkondensator 69,1 fF, so viel wie das Gate des Beispieltransistors. Das __Randfeld__, das von den Flanken und der Oberseite der Bahn zum Substrat biegt, hebt das bei dieser Breite auf 162 fF, bei 1 µm Breite auf das 3,55-Fache, bei 4 µm auf das 1,75-Fache des Plattenwerts.

## Umladen und Miller-Effekt

*Was bewirken die Kapazitäten in einer Schaltung, und warum wiegt gerade die kleine Gate-Drain-Kapazität am schwersten?*

Wie im Abschnitt *Von Grund auf* gezeigt, kostet Umladen Zeit: Das Gate des Beispieltransistors im Abschnürbereich, 53 fF, braucht mit 0,25 mA für 1 V 0,21 ns, und über 10 kΩ geladen ist seine Zeitkonstante 0,53 ns. In einer Verstärkerstufe kann eine Kapazität aber weit größer wirken, als sie ist.

In der __Source-Schaltung__ liegen Source und Bulk an Masse, das Signal kommt ans Gate, und der Drain ist über $R_D$ mit der Versorgung verbunden und bildet den Ausgang. Im Arbeitspunkt $U_{GS}$ = 1 V, $I_D$ = 0,25 mA und $U_{DS}$ = 1 V hat der Beispieltransistor die __Steilheit__ $g_m$ = 1 mS, die Änderung des Drainstroms je Volt Gate-Source-Spannung, und den __Ausgangsleitwert__ $g_o$ = 25 µS, die Änderung je Volt Drain-Source-Spannung. Mit $R_D$ = 10 kΩ verstärkt die Stufe kleine Änderungen achtfach und invertiert sie.

:::grafik
Szene: st1/mos-feldeffekttransistoren/04-miller · Vorlage: schaltung-mit-ersatz
**Abbildung 7:** (a) Source-Schaltung mit dem Beispiel-NMOS, Source und Bulk an Masse, $R_D$ = 10 kΩ zur Versorgung, am Gate eine Signalquelle mit 10 kΩ Innenwiderstand; eingezeichnet $C_{GS}$ = 49,5 fF vom Gate nach Masse, $C_{GD}$ = 3,45 fF vom Gate zum Drain und $C_{DB}$ = 37,8 fF vom Drain nach Masse; $g_m$ = 1 mS, $g_o$ = 25 µS, Verstärkung −8. Spannungsbalken: Gate +10 mV, Drain −80 mV, über $C_{GD}$ 90 mV. (b) Ersatz: $C_{GD}$ aufgeteilt in 31,1 fF vom Gate nach Masse und 3,88 fF vom Drain nach Masse; am Eingang zusammen 80,6 fF statt 52,9 fF, am Ausgang 41,7 fF. (c) Eingangskapazität für die Verstärkungen 0, −8 und −40: 52,9 fF, 80,6 fF und 191,1 fF, davon aus $C_{GD}$ 3,45 fF, 31,1 fF und 141,6 fF. Weil sich die Spannung über $C_{GD}$ neunmal so stark ändert wie am Gate, wirkt sie am Eingang neunmal so groß.
:::

**Die Akteure:**

- __$A_V$__: Spannungsverstärkung der Stufe vom Gate zum Drain für kleine Änderungen, $-g_m/(G_D + g_o)$ mit dem Leitwert $G_D$ des Drainwiderstands ([Vierpole: Parameterformen und Zusammenschaltung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/vierpole.html)); −8 mit $G_D$ = 0,1 mS, negativ, weil der Drain sinkt, wenn das Gate steigt.
- __$C_\mathrm{ein}$__, __$C_\mathrm{aus}$__: Kapazität gegen Masse, die eine Signalquelle am Gate bzw. eine Last am Drain sieht; 80,6 fF und 41,7 fF.

**Das Zusammenspiel:**

**Schritt 1**: $C_{GS}$ liegt zwischen Gate und Masse, $C_{DB}$ zwischen Drain und Masse; nur $C_{GD}$ verbindet Eingang und Ausgang (Abbildung 7a), im Abschnürbereich allein die Überlappung mit 3,45 fF.

**Schritt 2**: Steigt das Gate um 10 mV, sinkt der Drain um 80 mV, und die Spannung über $C_{GD}$ ändert sich um 90 mV, neunmal so viel wie am Eingang.

**Schritt 3** (entscheidender Schritt): Die Ladung dafür, 0,311 fC, muss die Signalquelle liefern. Bei 10 mV nähme so viel ein Kondensator von 31,1 fF gegen Masse auf: Für die Quelle wirkt $C_{GD}$ neunmal so groß.

**Schritt 4**: Am Eingang liegen damit 80,6 fF statt 52,9 fF (Abbildung 7b); am Ausgang wirkt $C_{GD}$ nur 9/8-mal so groß, 3,88 fF zu den 37,8 fF von $C_{DB}$. Mit einer idealen Stromquelle statt $R_D$ verstärkt die Stufe 40-fach, und die 3,45 fF wirken am Eingang wie 141,6 fF, fast dreimal so viel wie $C_{GS}$ (Abbildung 7c).

Diese Vervielfachung heißt __Miller-Effekt__, nach John M. Miller, der sie 1920 an der Elektronenröhre beschrieb.

:::formel Satz
$$C_\mathrm{ein} = C_{GS} + C_{GD}\,\big(1 - A_V\big), \qquad C_\mathrm{aus} = C_{DB} + C_{GD}\,\frac{A_V - 1}{A_V}$$
:::

**So liest man das:** Jede Kapazität zwischen Ein- und Ausgang eines Verstärkers wirkt am Eingang mit dem Faktor $1 - A_V$ und am Ausgang mit $(A_V - 1)/A_V$. Bei einer invertierenden Stufe ist $1 - A_V$ gleich $1 + |A_V|$: Am Eingang wird die Kapazität vervielfacht, am Ausgang kaum vergrößert. Nähert sich $A_V$ dem Wert 1, verschwindet ihre Wirkung, weil sich beide Enden gleich bewegen.

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

:::fehlvorstellung
„Im Abschnürbereich ist $C_{GD}$ null, also kann man die Gate-Drain-Kapazität vergessen.“ Das liegt nahe, weil der abgeschnürte Kanal den Drain nicht erreicht und die Überlappung nur 5 % der Oxidkapazität ausmacht. Die Überlappung bleibt aber und verbindet den Eingang mit dem invertierten Ausgang: Bei $A_V$ = −8 wirkt sie am Eingang wie 31,1 fF, bei −40 wie 141,6 fF, fast dreimal so viel wie $C_{GS}$.
:::

::::beispiel Eingangskapazität und Zeitkonstanten der Source-Schaltung
**Gegeben:** Beispiel-NMOS im Abschnürbereich mit $C_{GS}$ = 49,5 fF, $C_{GD}$ = 3,45 fF, $C_{DB}$ = 37,8 fF bei $U_{DB}$ = 1 V, $g_m$ = 1 mS, $g_o$ = 25 µS; Signalquelle mit $R_\mathrm{sig}$ = 10 kΩ; (a) $R_D$ = 10 kΩ, (b) eine ideale Stromquelle statt $R_D$.

**Gesucht:** Verstärkung, $C_\mathrm{ein}$, $C_\mathrm{aus}$ und die Zeitkonstanten an Gate und Drain.

**Rechnung:** (a) Verstärkung mit $G_D$ = 0,1 mS und Kapazitäten:

$$A_V = -\frac{1\ \mathrm{mS}}{0{,}1\ \mathrm{mS} + 0{,}025\ \mathrm{mS}} = -8$$

$$C_\mathrm{ein} = 49{,}5\ \mathrm{fF} + 3{,}45\ \mathrm{fF}\cdot9 = 80{,}6\ \mathrm{fF}, \qquad C_\mathrm{aus} = 37{,}8\ \mathrm{fF} + 3{,}45\ \mathrm{fF}\cdot\frac{9}{8} = 41{,}7\ \mathrm{fF}$$

Zeitkonstanten, am Drain mit dem Ausgangswiderstand $1/(G_D + g_o)$ = 8 kΩ:

$$\tau_\mathrm{ein} = 10\ \mathrm{k\Omega}\cdot80{,}6\ \mathrm{fF} = 0{,}81\ \mathrm{ns}, \qquad \tau_\mathrm{aus} = 8\ \mathrm{k\Omega}\cdot41{,}7\ \mathrm{fF} = 0{,}33\ \mathrm{ns}$$

(b) Ohne $R_D$ bleibt am Drain nur $g_o$:

$$A_V = -\frac{1\ \mathrm{mS}}{0{,}025\ \mathrm{mS}} = -40, \qquad C_\mathrm{ein} = 49{,}5\ \mathrm{fF} + 3{,}45\ \mathrm{fF}\cdot41 = 191{,}1\ \mathrm{fF}$$

$$\tau_\mathrm{ein} = 10\ \mathrm{k\Omega}\cdot191{,}1\ \mathrm{fF} = 1{,}91\ \mathrm{ns}, \qquad \tau_\mathrm{aus} = 40\ \mathrm{k\Omega}\cdot41{,}4\ \mathrm{fF} = 1{,}65\ \mathrm{ns}$$

**Ergebnis:** **(a) $A_V$ = −8, $C_\mathrm{ein}$ = 80,6 fF, $\tau_\mathrm{ein}$ = 0,81 ns; (b) $A_V$ = −40, $C_\mathrm{ein}$ = 191,1 fF, $\tau_\mathrm{ein}$ = 1,91 ns.**

**Einordnung:** Ohne den Miller-Effekt läge die Zeitkonstante am Gate bei 0,53 ns; die 3,45 fF der Überlappung verlängern sie in (a) um die Hälfte und machen in (b) 74 % der Eingangskapazität aus. In (b) ist der Drain fast so langsam wie das Gate; dort ist die Miller-Rechnung nur eine Abschätzung, und man rechnet mit dem Frequenzgang der ganzen Stufe.
::::

:::frage
„Warum baut man in Verstärker manchmal absichtlich eine Kapazität zwischen Ein- und Ausgang einer Stufe?“
Ein Operationsverstärker braucht für den Betrieb mit Gegenkopplung einen Knoten, der viel langsamer ist als alle anderen, sonst kann er schwingen. Eine Kapazität über einer invertierenden Stufe mit der Verstärkung −50 wirkt nach dem Miller-Effekt 51-fach: 1 pF ersetzt 51 pF und braucht bei rund 1 fF/µm² nur 1000 µm² statt 51 000 µm² Chipfläche. Man nennt das __Miller-Kompensation__; im Operationsverstärker 741 sitzen auf diese Weise 30 pF über der zweiten Stufe.
:::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| gesperrt nur 0,30 $C_\mathrm{ox}$, mit Kanal wieder $C_\mathrm{ox}$ | die Gegenladung sitzt erst am Rand der Verarmungszone, dann kommt sie schnell aus Source und Drain |
| je die Hälfte im ohmschen Bereich, zwei Drittel und null im Abschnürbereich | jedes Kanalende liefert so viel, wie seine Spannung das Kanalpotential bewegt |
| Überlappung | Gegenladung im n⁺-Gebiet unter der Gatekante, unabhängig vom Kanal |
| Sperrschichtkapazität aus Boden und Rand | die Gegenladung sitzt am Rand einer Zone, die mit der Spannung breiter wird |
| Miller-Effekt | die Spannung über $C_{GD}$ ändert sich $(1 - A_V)$-mal so stark wie am Eingang |

Eine Kapazität im MOSFET ist die Ladung, die ein Anschluss je Volt Spannungsänderung liefern muss; ihr Wert hängt davon ab, wo die Gegenladung sitzt und aus welchem Anschluss sie nachfließt, und ihre Wirkung davon, um wie viel sich die Spannung über ihr tatsächlich ändert.

## Bedeutung und Ausblick

In digitalen Schaltungen bilden Gate der folgenden Stufe, Drainkapazitäten und Leitungen die Last jedes Gatters und bestimmen mit dem verfügbaren Strom die Schaltzeit; in Verstärkern begrenzt vor allem der Miller-Effekt die Bandbreite. Der nächste Artikel, das Kleinsignalmodell des MOSFET, setzt die Kapazitäten mit Steilheit und Ausgangsleitwert zu einem Ersatzschaltbild für kleine Signale zusammen.

**In der ausführlichen Fassung:** die allgemeine Formel für die Aufteilung zwischen ohmschem Bereich und Abschnürbereich (Meyer-Modell) mit Herleitung, die Kapazität zwischen Kanal und Bulk, was die einfache Aufteilung vernachlässigt und bis zu welcher Frequenz sie gilt, Querschnitt und Randfeld der Überlappung, der Verlauf der Sperrschichtkapazität über der Spannung, gefaltete Transistoren mit gemeinsamem Drain, Leitungskapazität mit Randfeld und Koppelkapazität samt Näherungsformel, ein mechanisches Bild des Miller-Effekts, der Sourcefolger und die Miller-Kompensation mit Beispiel ([Parasitäre Kapazitäten des MOSFET, ausführlich](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/parasitaere-kapazitaeten-ausfuehrlich.html)).

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
F: Warum ist $C_{GS}$ im Abschnürbereich zwei Drittel der Oxidkapazität?
A: Die Kanalladung fällt von der Source zum Abschnürpunkt wie die Wurzel aus $1 - x/L$. Eine Änderung der Gate-Source-Spannung ändert das ganze Profil im selben Verhältnis, und sein Mittelwert ist zwei Drittel des Werts an der Source.
F: Warum wirkt $C_{GD}$ am Eingang einer Source-Schaltung vervielfacht?
A: Steigt das Gate, fällt der Drain um das $|A_V|$-Fache; die Spannung über $C_{GD}$ ändert sich $(1 - A_V)$-mal so stark wie am Gate, und die Ladung dafür muss die Signalquelle liefern. Bei $A_V$ = −8 wirken 3,45 fF wie 31,1 fF.
F: Warum fällt die Gatekapazität des Transistors in der Inversion nicht ab wie die eines MOS-Kondensators bei hoher Frequenz?
A: Beim Kondensator ohne Source und Drain entstehen die Elektronen nur durch Wärme, beim Beispiel in rund 90 s; im Transistor liefern Source und Drain sie über den Kanal mit einer Zeitkonstante von rund 69 ps. Bei 1 V misst man deshalb 0,92 $C_\mathrm{ox}$ statt 0,24.
F: Stimmt es, dass die Gatekapazität eines MOSFET immer die Oxidkapazität ist?
A: Nein. Beim Beispieltransistor sind es ohne Überlappung gesperrt bei 0 V 20,7 fF, im Abschnürbereich 46,0 fF und erst im ohmschen Bereich die vollen 69,1 fF.
F: Stimmt es, dass man $C_{GD}$ im Abschnürbereich vernachlässigen kann, weil sie dort null ist?
A: Nein. Die Überlappung von 3,45 fF bleibt, und der Miller-Effekt vervielfacht sie: bei $A_V$ = −8 auf 31,1 fF, bei −40 auf 141,6 fF, fast das Dreifache von $C_{GS}$.
F: Wie groß ist die Eingangskapazität einer Source-Schaltung mit $C_{GS}$ = 49,5 fF, $C_{GD}$ = 3,45 fF und $A_V$ = −8?
A: $49{,}5\ \mathrm{fF} + 3{,}45\ \mathrm{fF}\cdot(1 + 8)$ = 80,6 fF, statt 52,9 fF ohne Miller-Effekt.
:::
