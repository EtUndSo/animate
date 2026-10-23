---
title: Aufbau und Funktionsweise des MOSFET
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / MOS-Feldeffekttransistoren
order: 33030100
summary: Wie ein MOS-Feldeffekttransistor aufgebaut ist und warum eine Spannung am isolierten Gate einen leitenden Kanal zwischen Source und Drain erzeugt. Kompakte Fassung mit Aufbau, Schaltzeichen, den Zuständen des MOS-Kondensators, Herleitung von Schwellenspannung und Kanalladung, Kanalwiderstand und Abschnürung, gerechnet an einem integrierten Beispieltransistor mit 5 nm Gateoxid.
tags: MOSFET, Inversion, Kanal, Schwellenspannung, Schaltsymbol
stil: 3
fassung: kompakt
---

## Worum es geht

Verstärker und Logikgatter brauchen ein Bauelement, in dem eine Spannung an einem Anschluss den Strom zwischen zwei anderen steuert. Der MOS-Feldeffekttransistor, kurz MOSFET, steuert über eine Elektrode, die eine nur wenige Nanometer dicke Isolierschicht vom Halbleiter trennt; er braucht deshalb im Ruhezustand keinen Steuerstrom und ist das häufigste Bauelement der Elektronik geworden. Alles hängt an einem Prinzip:

**Gate, Oxid und Halbleiter bilden einen Kondensator: Die Spannung zwischen Gate und Halbleiter legt fest, wie viel Gegenladung unter dem Oxid sitzt, und oberhalb der Schwellenspannung kommt jede weitere Gegenladung als Schicht beweglicher Elektronen hinzu, die Source und Drain als Kanal verbinden; an jeder Stelle des Kanals bestimmt die örtliche Spannung zwischen Gate und Kanal, wie viel Ladung dort den Strom tragen kann.**

Vorausgesetzt werden Dotierung, Löcher, Fermi-Niveau, Bänder und Boltzmann-Verteilung aus [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html), die Raumladungszone aus [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html) und der Plattenkondensator aus [Kondensator und Kapazität](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/kondensator-und-kapazitaet.html). Auf diesem Artikel bauen die Kennlinien, das Kleinsignalmodell und alle Transistor- und CMOS-Schaltungen auf.

:::grafik
Szene: st1/mos-feldeffekttransistoren/01-querschnitt · Vorlage: querschnitt-layout
**Abbildung 1:** (a) Querschnitt eines n-Kanal-MOSFET, schematisch mit stark vergrößertem Oxid: zwei stark n-dotierte Gebiete, Source links und Drain rechts, im Abstand $L$ = 1 µm in einem p-Substrat; darüber das Gate aus n⁺-Polysilizium auf 5 nm Gateoxid; links der p⁺-Bulkkontakt. Bei $U_{GS}$ = 1 V liegt unter dem Oxid eine dünne Elektronenschicht von Source bis Drain, darunter eine rund 48 nm tiefe Zone fester, negativ geladener Akzeptorrümpfe; die Elektronen fließen von der Source zum Drain, der Strom $I_D$ in den Drain hinein. (b) Draufsicht: Der Transistor entsteht, wo der Polysilizium-Streifen das aktive n-Gebiet kreuzt, mit der Weite $W$ = 10 µm quer und der Länge $L$ = 1 µm längs zur Stromrichtung. Das Gate liegt isoliert über dem Bereich zwischen Source und Drain und steuert ihn nur über sein Feld.
:::

## Aufbau, PMOS und Bulk-Anschluss

*Aus welchen Gebieten besteht ein MOSFET, und warum liegt sein Substrat an der negativsten Spannung?*

Grundlage ist eine Scheibe aus einkristallinem, schwach p-dotiertem Silizium, der __Wafer__. __Dotieren__ heißt, gezielt Fremdatome einzubauen: Ein Boratom übernimmt für seine vierte Bindung ein Elektron aus der Nachbarschaft und bleibt als fester, negativ geladener Rumpf zurück, ein __Akzeptor__; die fehlende Bindung wandert als __Loch__ durch den Kristall, wie ein bewegliches Teilchen mit der Elementarladung $+e$. Im p-Silizium sind Löcher die __Majoritätsträger__, Elektronen die seltenen __Minoritätsträger__: Weil das Produkt beider Dichten im Gleichgewicht gleich dem Quadrat der __Eigenleitungsdichte__ $n_i$ = 10¹⁰ cm⁻³ ist, der Ladungsträgerdichte von reinem Silizium (__Massenwirkungsgesetz__), kommen unter dem Gate des Beispieltransistors auf 5,7·10¹⁷ Löcher pro Kubikzentimeter nur 176 Elektronen.

In das Substrat sind zwei sehr stark n-dotierte Gebiete eingebracht (__n⁺__, rund 10²⁰ Donatoren pro cm³, die je ein freies Elektron abgeben), __Source__ und __Drain__. Zwischen ihnen liegt an der Oberfläche das __Kanalgebiet__, darüber auf 5 nm Siliziumdioxid, dem __Gateoxid__, das __Gate__ aus gut leitendem, stark dotiertem __Polysilizium__. Das Oxid isoliert; das Gate wirkt nur über sein Feld. Der Abstand von Source und Drain ist die __Kanallänge__ $L$, die Ausdehnung quer dazu die __Kanalweite__ $W$, die man nur in der Draufsicht, dem __Layout__, sieht (Abbildung 1b). Beim Beispieltransistor ist $W$ = 10 µm und $L$ = 1 µm; Transistoren mit größerer Weite führen mehr Strom, längere weniger.

Source und Drain sind baugleich; erst die Beschaltung legt fest, welches Gebiet welches ist. Beim NMOS, dem n-Kanal-MOSFET, ist die Source das n⁺-Gebiet mit dem niedrigeren Potential. Die Elektronen fließen dann von der Source zum Drain, der Strom vom Drain zur Source.

Den vierten Anschluss, das Substrat, nennt man __Bulk__; er liegt über einen p⁺-Kontakt an der negativsten Spannung der Schaltung, meist Masse. Der Grund: Jedes n⁺-Gebiet bildet mit dem p-Substrat eine Diode mit der Anode im Substrat. Liegt das Substrat am tiefsten, sind alle diese Dioden gesperrt, und die Transistoren sind voneinander isoliert; läge es höher als eine Source oder ein Drain, flösse ab etwa 0,6 V ein Strom ins Substrat.

Der p-Kanal-MOSFET, __PMOS__, ist das Spiegelbild: p⁺-Source und -Drain in einer __n-Wanne__, einem tief eingebrachten n-Gebiet, dessen Kontakt an der höchsten Spannung $U_B$ liegt; sein Kanal besteht aus Löchern, seine Source ist das Gebiet mit dem höheren Potential, und Spannungen und Strom sind im Betrieb negativ. NMOS und PMOS zusammen auf einem Chip ergeben die __CMOS__-Technik (complementary MOS), in der fast alle integrierten Schaltungen gebaut werden.

## Schaltzeichen und Zählpfeile

*Wie stellt man NMOS und PMOS im Schaltplan dar, und wie zählt man ihre Spannungen?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/01-schaltzeichen · Vorlage: schaltsymbol-tabelle
**Abbildung 2:** Drei verbreitete Schaltzeichen, oben für den NMOS, unten für den PMOS. (a) An den Bipolartransistor angelehnt: ein Pfeil an der Source wie am Emitter, beim NMOS nach außen, beim PMOS nach innen. (b) Aus der Digitaltechnik: ohne Pfeil, der PMOS mit einem Kreis am Gate. (c) Nach DIN: unterbrochene Kanallinie für den selbstsperrenden Typ und eigener Bulkanschluss B mit Pfeil, beim NMOS zum Kanal hin, beim PMOS von ihm weg. In jedem Symbol zählt $U_{GS}$ vom Gate zur Source, $U_{DS}$ vom Drain zur Source, und $I_D$ fließt in den Drain hinein; daneben klein der selbstleitende NMOS mit durchgehender Kanallinie. Alle Schreibweisen bezeichnen dasselbe Bauteil, und beim PMOS steht die Source oben, weil sie das höhere Potential hat.
:::

Drei Schreibweisen sind verbreitet (Abbildung 2): mit einem Pfeil an der Source wie am Emitter eines Bipolartransistors, ohne Pfeil mit einem Kreis am Gate des PMOS wie in der Digitaltechnik, oder nach DIN mit eigenem Bulkanschluss, dessen Pfeil wie im Diodensymbol von p nach n zeigt. Die unterbrochene Kanallinie des DIN-Symbols kennzeichnet den __selbstsperrenden__ Typ: Ohne Gatespannung gibt es keinen Kanal. Ein __selbstleitender__ Typ hätte schon ohne Gatespannung einen; CMOS-Schaltungen brauchen ihn nicht, dieser Artikel behandelt den selbstsperrenden.

Spannungen zählen vom ersten zum zweiten Index, $U_{GS}$ also vom Gate zur Source; Ströme zählen in den Anschluss hinein. Beim NMOS sind $U_{GS}$, $U_{DS}$ und $I_D$ im Betrieb positiv, beim PMOS negativ. Bezug ist immer die Source, auch wenn sie nicht an Masse liegt: Der Transistor reagiert nur auf Spannungen zwischen seinen Anschlüssen, und an der Source treten die Elektronen in den Kanal ein. Ob es dort einen Kanal gibt, entscheidet deshalb $U_{GS}$.

## Der MOS-Kondensator

*Was macht eine Spannung zwischen Gate und Substrat mit den Ladungsträgern unter dem Oxid, solange noch kein Strom fließt?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/01-mos-zustaende · Vorlage: querschnitt-folge
**Abbildung 3:** Der MOS-Kondensator des Beispieltransistors (Gate aus n⁺-Polysilizium, 5 nm Oxid, p-Silizium mit 5,7·10¹⁷ cm⁻³, Bulk an Masse) in vier Zuständen, vollständig gerechnet (ohne Verarmungsnäherung, mit der Boltzmann-Verteilung). (a) Anreicherung bei $U_{GB}$ = −2 V: Unter dem Oxid sammeln sich Löcher, 5,94 fC/µm². (b) Flachband bei $U_{GB}$ = −1,03 V: keine Ladung, kein Feld. (c) Verarmung bei $U_{GB}$ = 0: Die Löcher sind verdrängt, zurück bleibt eine 35 nm tiefe Zone fester Akzeptorrümpfe mit 3,19 fC/µm²; die Oberfläche liegt 0,57 V über dem Inneren. (d) Inversion bei $U_{GB}$ = 1 V: Direkt unter dem Oxid liegt eine dünne Elektronenschicht mit 2,55 fC/µm² über einer 48 nm tiefen Zone mit 4,35 fC/µm²; die Oberfläche liegt 1,03 V über dem Inneren. Zur Ladung des Gates gehört immer eine gleich große Gegenladung im Silizium; mit wachsender Spannung besteht sie erst aus Löchern, dann aus festen Rümpfen, und oberhalb der Schwelle kommen bewegliche Elektronen hinzu.
:::

Um zu verstehen, was das Gate bewirkt, lässt man Source und Drain zunächst weg. Übrig bleibt der __MOS-Kondensator__ aus Gate, Oxid und Substrat.

**Die Akteure:**

- __$U_{GB}$__: Spannung zwischen Gate und Bulk; in V; im Beispiel von −2 V bis 2,5 V.
- __$t_\mathrm{ox}$__, __$\varepsilon_\mathrm{ox}$__: Dicke und Permittivität des Oxids; 5 nm und das 3,9-Fache der Feldkonstante, 3,45·10⁻¹³ F/cm.
- __$C'_\mathrm{ox}$__: Kapazität des Oxids pro Fläche; 6,91 fF/µm². Der Strich kennzeichnet hier und im Folgenden Größen pro Fläche.
- __$Q'_G$__: Ladung des Gates pro Fläche; einige fC/µm², wobei 1 fC/µm² gleich 10⁻⁷ C/cm² ist.
- __$U_\mathrm{ox}$__: Spannung über dem Oxid; in V.
- __$\psi_s$__: __Oberflächenpotential__, das Potential der Siliziumoberfläche gegenüber dem neutralen Inneren des Substrats; im Beispiel von −0,1 V bis 1,1 V.

**Das Zusammenspiel:** Weil das Oxid keine Ladung enthält, enden nach dem Gaußschen Gesetz alle Feldlinien der Gateladung auf einer gleich großen Gegenladung im Silizium. Die Spannung bestimmt nur, wie groß diese ist und woraus sie besteht: aus Löchern, aus festen Akzeptorrümpfen und oberhalb der Schwelle zusätzlich aus Elektronen (Abbildung 3). Die Abbildungen 3 und 4 sind eine __vollständige Rechnung__, in der Feld und Potential aus allen Ladungen folgen und sich die beweglichen Ladungsträger nach der Boltzmann-Verteilung verteilen; die Formeln dieses Artikels nähern sie.

Ein Teil der Spannung liegt über dem Oxid, das wie ein Plattenkondensator wirkt:

:::formel Formel
$$C'_\mathrm{ox} = \frac{\varepsilon_\mathrm{ox}}{t_\mathrm{ox}}, \qquad Q'_G = C'_\mathrm{ox}\,U_\mathrm{ox}\,$$
:::

**So liest man das:** Je dünner das Oxid, desto mehr Ladung bindet dieselbe Spannung über ihm; 5 nm ergeben 6,91 fF/µm², die 10 µm² des Beispieltransistors 69 fF. Der Rest von $U_{GB}$ fällt im Silizium ab ($\psi_s$) oder ist Kontaktspannung zwischen den Materialien (Abschnitt *Flachband und Kontaktspannung*).

**Kurz gesagt:** Halbe Oxiddicke, doppelte Kapazität pro Fläche.

Idee der Herleitung: Das Gaußsche Gesetz liefert das Feld im Oxid, die Spannung ist Feld mal Dicke.

:::herleitung
**Ausgangspunkt:** das Gaußsche Gesetz aus dem Artikel [Kondensator und Kapazität](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/kondensator-und-kapazitaet.html): Der Fluss der Verschiebungsdichte $\varepsilon E$ durch eine geschlossene Fläche ist gleich der eingeschlossenen Ladung.

**Annahmen:**
(i) Die Gatefläche ist groß gegen die Oxiddicke; das Feld im Oxid ist homogen und steht senkrecht auf den Schichten, Randfelder werden vernachlässigt.
(ii) Das Oxid enthält keine Ladung.
(iii) Im Gate ist das Feld null, weil es ein guter Leiter ist.

**Schritt 1**: Eine flache Schachtel mit der Deckfläche $A$ umschließt die Gateladung $Q'_G A$. Ihre obere Deckfläche liegt im feldfreien Gate, die untere im Oxid; nur die untere trägt Fluss:

$$\varepsilon_\mathrm{ox}\,E_\mathrm{ox}\,A = Q'_G\,A$$

Durch $A$ geteilt, ergibt sich das Feld im Oxid:

$$E_\mathrm{ox} = \frac{Q'_G}{\varepsilon_\mathrm{ox}}$$

**Schritt 2**: Nach (i) und (ii) ist das Feld im ganzen Oxid gleich groß; die Spannung über dem Oxid ist deshalb Feld mal Dicke:

$$U_\mathrm{ox} = E_\mathrm{ox}\,t_\mathrm{ox} = \frac{t_\mathrm{ox}}{\varepsilon_\mathrm{ox}}\,Q'_G$$

**Schritt 3**: Nach $Q'_G$ aufgelöst; der Faktor vor $U_\mathrm{ox}$ ist die Kapazität pro Fläche:

$$Q'_G = \frac{\varepsilon_\mathrm{ox}}{t_\mathrm{ox}}\,U_\mathrm{ox}$$

**Ergebnis:**

$$C'_\mathrm{ox} = \frac{\varepsilon_\mathrm{ox}}{t_\mathrm{ox}}, \qquad Q'_G = C'_\mathrm{ox}\,U_\mathrm{ox}\,$$

**Woher die Faktoren kommen:** $\varepsilon_\mathrm{ox}$ stammt aus dem Gaußschen Gesetz, $t_\mathrm{ox}$ aus dem Schritt von Feld zu Spannung. Mit der Fläche $W L$ multipliziert ergibt sich die Formel $C = \varepsilon A/d$ des Plattenkondensators.

**Proben:** Einheit: F/cm geteilt durch cm ergibt F/cm². Zahlenwert: 3,453·10⁻¹³ F/cm geteilt durch 5·10⁻⁷ cm ergibt 6,906·10⁻⁷ F/cm², also 6,906 fF/µm².

**Grenzen:** In sehr dünnen Oxiden zählt, dass die Ladung im Silizium nicht genau an der Grenzfläche sitzt, sondern bis etwa einen Nanometer darunter; das wirkt wie ein etwas dickeres Oxid und senkt die wirksame Kapazität um einige Prozent.
:::

### Anreicherung

Bei deutlich negativer Gatespannung zieht das Feld Löcher an die Oberfläche (Abbildung 3a): bei −2 V 5,9 fC/µm², an der Oberfläche fast 60-mal so dicht wie im Inneren. Die Struktur verhält sich dann fast wie ein Plattenkondensator mit $C'_\mathrm{ox}$.

### Flachband und Kontaktspannung

Zur Erinnerung aus [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html): Das __Banddiagramm__ trägt die Energie der Elektronen über dem Ort auf. Freie Elektronen haben Energien ab der __Leitungsbandkante__ $W_L$, Löcher sitzen an der __Valenzbandkante__ $W_V$, und das __Eigenleitungsniveau__ $W_i$ liegt nahe der Mitte. Das __Fermi-Niveau__ $W_F$ zeigt die Besetzung: Je näher es an $W_L$ liegt, desto mehr freie Elektronen gibt es, je näher an $W_V$, desto mehr Löcher.

Ladungsfrei und feldfrei ist der Kondensator bei der __Flachbandspannung__ $U_\mathrm{FB}$; dann verlaufen die Bänder bis an die Oberfläche waagerecht. Beim Beispieltransistor liegt sie bei −1,03 V.

**Die Akteure:**

- __$N_A$__: Akzeptordichte unter dem Gate; 5,68·10¹⁷ cm⁻³.
- __$U_T$__: Temperaturspannung $k_B T/e$; 25,85 mV, je 59,5 mV ändert sich eine Dichte im Gleichgewicht um den Faktor 10.
- __$N_L$__: effektive Zustandsdichte des Leitungsbands, die Elektronendichte, bei der das Fermi-Niveau die Leitungsbandkante erreicht; 3,2·10¹⁹ cm⁻³.
- __$\Phi_F$__: __Fermi-Potential__, der Abstand des Fermi-Niveaus unter dem Eigenleitungsniveau im Substrat, in Volt; 0,462 V.
- __$\Phi_\mathrm{MS}$__: __Austrittsarbeitsdifferenz__ zwischen Gate und Substrat in Volt, gleich der Flachbandspannung; −1,027 V.

**Das Zusammenspiel:** Sind Gate und Bulk verbunden, liegt im Gleichgewicht das Fermi-Niveau überall gleich hoch, wie an einem pn-Übergang. Im n⁺-Polysilizium liegt es an der Leitungsbandkante, mit $n_i$ = 10¹⁰ cm⁻³ gerechnet 0,566 eV über dem Eigenleitungsniveau, im Substrat 0,462 eV darunter. Damit beide gleich hoch liegen, muss das Gate elektrisch 1,027 V über dem Substrat liegen, die eingebaute __Kontaktspannung__; dazu fließen beim Verbinden einige Elektronen vom Gate ins Substrat. Schon bei $U_{GB}$ = 0 ist das Gate deshalb positiv geladen und die Oberfläche verarmt (Abbildung 3c); erst −1,027 V heben die Kontaktspannung auf. Diese Gegenspannung ist die Flachbandspannung; man schreibt sie als __Austrittsarbeitsdifferenz__ $\Phi_\mathrm{MS}$, den Unterschied der Energien, die ein Elektron in Gate und Halbleiter vom Fermi-Niveau ins Vakuum heben, geteilt durch $e$.

:::formel Formel
$$\Phi_F = U_T\,\ln\frac{N_A}{n_i}$$

$$\begin{aligned}U_\mathrm{FB} = \Phi_\mathrm{MS} &= -\Big(U_T\,\ln\frac{N_L}{n_i} + \Phi_F\Big)\\ &= -U_T\,\ln\frac{N_L\,N_A}{n_i^{2}}\end{aligned}$$
:::

**So liest man das:** Aus der Dotierung des Substrats folgt die Spannung, bei der der Kondensator ungeladen ist. Das Fermi-Potential wächst um 59,5 mV je Zehnerpotenz Dotierung; die Kontaktspannung ist die Summe dieser Strecke und der 0,566 V im Gate, die Flachbandspannung ihr Negatives, weil man das zu hoch liegende Gate absenken muss.

**Kurz gesagt:** Beim n⁺-Gate auf p-Substrat ist die Kontaktspannung die Summe der beiden Strecken, um die die Dotierungen von Gate und Substrat das Fermi-Niveau aus dem Eigenleitungsniveau schieben; die Flachbandspannung ist ihr Negatives.

Idee der Herleitung: Man legt die Fermi-Niveaus von Gate und Substrat auf gleiche Höhe und liest ab, wie weit die Bänder dafür gegeneinander verschoben sein müssen.

:::herleitung
**Ausgangspunkt:** die Lage des Fermi-Niveaus und die Gleichheit der Fermi-Niveaus im Gleichgewicht, beide aus dem Artikel [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell-ausfuehrlich.html); dort folgt auf demselben Weg die Diffusionsspannung des pn-Übergangs. Die Lage des Fermi-Niveaus bei der Elektronendichte $n$ ist

$$W_F - W_i = k_B T\,\ln\frac{n}{n_i}$$

**Annahmen:**
(i) thermisches Gleichgewicht; Gate und Bulk sind außen verbunden ($U_{GB}$ = 0).
(ii) Das n⁺-Polysilizium ist so stark dotiert, dass sein Fermi-Niveau an der Leitungsbandkante liegt; seine Elektronendichte entspricht $N_L$.
(iii) Im Substrat gilt die Boltzmann-Näherung, und alle Akzeptoren sind ionisiert, also $n = n_i^2/N_A$.
(iv) Oxid und Grenzfläche sind frei von Ladungen.

**Schritt 1**: Im Substrat ist $n = n_i^2/N_A$; die Formel für die Lage des Fermi-Niveaus ergibt einen Abstand unter dem Eigenleitungsniveau von

$$W_i - W_F = k_B T\,\ln\frac{N_A}{n_i} = e\,\Phi_F$$

**Schritt 2**: Im Gate ist nach (ii) $n = N_L$; das Fermi-Niveau liegt über dem Eigenleitungsniveau um

$$W_F - W_i = k_B T\,\ln\frac{N_L}{n_i}$$

**Schritt 3** (entscheidender Schritt): Bei gleichem Fermi-Niveau liegt das Eigenleitungsniveau des Gates um die Summe beider Strecken tiefer als das des Substrats. Die Energie eines Elektrons ist $-e\varphi$; eine um $\Delta W$ tiefere Energie bedeutet ein um $\Delta W/e$ höheres Potential. Bei $U_{GB}$ = 0 liegt das Gate deshalb um

$$\varphi_\mathrm{Gate} - \varphi_\mathrm{Substrat} = U_T\,\ln\frac{N_L}{n_i} + \Phi_F$$

über dem Inneren des Substrats.

**Schritt 4**: Eine äußere Spannung $U_{GB}$ kommt zu diesem Unterschied hinzu. Flach sind die Bänder, wenn über Oxid und Silizium zusammen keine Spannung liegt, wenn also $U_{GB}$ den Unterschied aus Schritt 3 gerade aufhebt. Das ergibt $U_\mathrm{FB}$; die Summe der Logarithmen ist der Logarithmus des Produkts.

**Ergebnis:**

$$\Phi_F = U_T\,\ln\frac{N_A}{n_i}$$

$$\begin{aligned}U_\mathrm{FB} = \Phi_\mathrm{MS} &= -\Big(U_T\,\ln\frac{N_L}{n_i} + \Phi_F\Big)\\ &= -U_T\,\ln\frac{N_L\,N_A}{n_i^{2}}\end{aligned}$$

**Woher die Faktoren kommen:** Jeder Logarithmus ist eine der beiden Strecken zwischen Fermi-Niveau und Eigenleitungsniveau; das Minuszeichen rührt daher, dass das Gate um diese Spannung zu hoch liegt. Der Ausdruck hat dieselbe Gestalt wie die Diffusionsspannung $U_T\ln(N_A N_D/n_i^2)$ eines pn-Übergangs, mit $N_L$ anstelle von $N_D$.

**Proben:** Einheit V. Zahlenwert: 25,85 mV · ln(3,2·10⁹) = 0,566 V und 25,85 mV · ln(5,68·10⁷) = 0,462 V, zusammen −1,027 V. Grenzfall: Bestünde das Gate aus demselben p-Silizium wie das Substrat, wären beide Strecken gleich und entgegengesetzt, und $\Phi_\mathrm{MS}$ wäre null.

**Grenzen:** In sehr stark dotiertem Polysilizium liegt das Fermi-Niveau sogar etwas über der Leitungsbandkante. Positive Ladungen im Oxid und an der Grenzfläche verschieben $U_\mathrm{FB}$ zusätzlich zu negativeren Werten.
:::

:::fehlvorstellung
„Ohne Spannung am Gate sind die Bänder flach, und die Oberfläche unter dem Oxid ist neutral.“ Das liegt nahe, weil ein Kondensator ohne Spannung keine Ladung trägt. Beim MOS-Kondensator stimmt das nur, wenn Gate und Halbleiter dasselbe Fermi-Niveau hätten. Mit einem Gate aus n⁺-Polysilizium auf p-Silizium wirkt schon bei $U_{GB}$ = 0 die Kontaktspannung von 1,03 V: Das Gate trägt 3,19 fC/µm², die Oberfläche ist 35 nm tief verarmt und liegt 0,57 V über dem Inneren (Abbildung 3c). Flach sind die Bänder erst bei −1,03 V.
:::

### Verarmung

Oberhalb der Flachbandspannung trägt das Gate positive Ladung, und ihr Feld schiebt die Löcher von der Oberfläche in die Tiefe. Rekombinieren können sie dort nicht, dafür gibt es unter dem Gate kaum Elektronen; sie wandern mit dem Feld fort. Zurück bleiben die festen, negativ geladenen Akzeptorrümpfe als __Verarmungszone__, dieselbe Raumladungszone wie am pn-Übergang, nur einseitig. Weil jede Schicht nur die Ladungsdichte $e N_A$ beiträgt, wird die Zone mit wachsender Gateladung tiefer. Sie wirkt dabei wie ein zweiter Kondensator in Reihe mit dem Oxid; die zwischen Gate und Bulk gemessene Kapazität sinkt in der Verarmung bis auf ein Viertel von $C'_\mathrm{ox}$.

**Die Akteure:**

- __$\varepsilon_\mathrm{Si}$__: Permittivität von Silizium, das 11,7-Fache der Feldkonstante; 1,036·10⁻¹² F/cm.
- __$y_d$__: Tiefe der Verarmungszone; 35 nm bei $U_{GB}$ = 0, 45 nm an der Schwelle.
- __$Q'_\mathrm{dep}$__: Ladung der Verarmungszone pro Fläche, negativ; ihr Betrag in der Verarmung von 0 bis rund 4,2 fC/µm² an der Schwelle, bei $U_{GB}$ = 0 rund 3,2 fC/µm².

:::formel Formel
$$y_d = \sqrt{\frac{2\,\varepsilon_\mathrm{Si}\,\psi_s}{e\,N_A}}$$

$$|Q'_\mathrm{dep}| = e\,N_A\,y_d = \sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A\,\psi_s}$$
:::

**So liest man das:** Tiefe und Ladung der Zone wachsen mit der Wurzel des Oberflächenpotentials; höhere Dotierung macht die Zone flacher und ihre Ladung größer. Nach der Formel reicht sie bei 0,57 V 36 nm tief, bei 0,92 V 46 nm; die vollständige Rechnung ergibt 35 und 45 nm.

**Kurz gesagt:** Vierfaches Oberflächenpotential, doppelte Tiefe und doppelte Ladung der Verarmungszone.

Idee der Herleitung: Das Feld wächst linear durch die Schicht der Rümpfe, und das Oberflächenpotential ist die Fläche unter dem Felddreieck.

:::herleitung
**Ausgangspunkt:** das Gaußsche Gesetz in der Form, die der Artikel [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie-ausfuehrlich.html) für die Raumladungszone benutzt: Über eine Schicht der Dicke $\mathrm dy$ mit der Ladungsdichte $\rho$ ändert sich das Feld um

$$\mathrm dE = \frac{\rho}{\varepsilon_\mathrm{Si}}\,\mathrm dy$$

**Annahmen:**
(i) Verarmungsnäherung: Zwischen der Oberfläche ($y$ = 0) und der Tiefe $y_d$ gibt es keine beweglichen Ladungsträger, die Ladungsdichte ist $-e N_A$; darunter ist das Silizium neutral und feldfrei.
(ii) Die Dotierung ist gleichmäßig.
(iii) Die Struktur ist eben und groß gegen $y_d$.

**Schritt 1**: Vom feldfreien Rand bei $y_d$ zur Oberfläche hin wächst der Betrag des Feldes linear und erreicht an der Oberfläche

$$E_s = \frac{e\,N_A\,y_d}{\varepsilon_\mathrm{Si}}$$

**Schritt 2** (entscheidender Schritt): Das Oberflächenpotential ist das Integral des Feldes über die Zone, also die Fläche des Dreiecks:

$$\psi_s = \frac{1}{2}\,E_s\,y_d = \frac{e\,N_A\,y_d^{2}}{2\,\varepsilon_\mathrm{Si}}$$

**Schritt 3**: Nach $y_d$ aufgelöst:

$$y_d = \sqrt{\frac{2\,\varepsilon_\mathrm{Si}\,\psi_s}{e\,N_A}}$$

**Schritt 4**: Die Ladung pro Fläche ist Ladungsdichte mal Tiefe; mit Schritt 3:

$$|Q'_\mathrm{dep}| = e\,N_A\,y_d = \sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A\,\psi_s}$$

**Ergebnis:**

$$y_d = \sqrt{\frac{2\,\varepsilon_\mathrm{Si}\,\psi_s}{e\,N_A}}, \qquad |Q'_\mathrm{dep}| = \sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A\,\psi_s}\,$$

**Woher die Faktoren kommen:** Die 2 stammt aus der Dreiecksfläche, $\varepsilon_\mathrm{Si}$ aus dem Gaußschen Gesetz. Es ist der Grenzfall der Formel für den pn-Übergang, wenn eine Seite unendlich stark dotiert ist: Der Bruch $(N_A + N_D)/(N_A N_D)$ geht dann gegen $1/N_A$.

**Proben:** Einheit: F/cm mal V geteilt durch C mal cm⁻³ ergibt cm², unter der Wurzel also cm. Bei 0,923 V ergeben sich 45,8 nm und 4,17 fC/µm². Die vollständige Rechnung liefert bei $U_{GB}$ = 0 mit 3,19 fC/µm² um 2 % weniger als die Formel, weil der Rand der Zone über einige Nanometer verschmiert ist.

**Grenzen:** Die Formel beschreibt nur die Ladung der Rümpfe. Sobald sich Elektronen an der Oberfläche sammeln (Abschnitt *Inversion*), kommt deren Ladung hinzu.
:::

## Inversion: wie die Oberfläche n-leitend wird

*Warum entsteht bei genügend positiver Gatespannung eine Schicht aus Elektronen, und warum wächst danach fast nur noch sie?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/01-oberflaechenpotential · Vorlage: gestapelte-kennlinien
**Abbildung 4:** Der MOS-Kondensator des Beispieltransistors über der Gate-Bulk-Spannung von −2 V bis 1,5 V, vollständig gerechnet; Marken bei $U_\mathrm{FB}$ = −1,03 V und $U_{th0}$ = 0,50 V. (a) Oberflächenpotential: 0,57 V bei 0 V, 0,92 V (das Doppelte des Fermi-Potentials) an der Schwelle, danach fast waagerecht, 1,03 V bei 1 V. (b) Elektronendichte (blau) und Löcherdichte (rot) an der Oberfläche, logarithmisch: Sie kreuzen sich bei 10¹⁰ cm⁻³ und −0,15 V; die Elektronendichte erreicht an der Schwelle die Dotierung, 5,7·10¹⁷ cm⁻³, und bei 1 V 3,3·10¹⁹ cm⁻³, mit der vollständigen Fermi-Verteilung statt ihrer Boltzmann-Näherung 2,8·10¹⁹ cm⁻³. (c) Beträge der Flächenladungen: Die Verarmungsladung (grau) steigt bis 4,11 fC/µm² an der Schwelle und bleibt danach fast konstant, die Elektronenladung (blau) wächst fast linear, 2,55 fC/µm² bei 1 V; gestrichelt das Ladungsmodell $C'_\mathrm{ox}(U_{GB} - U_{th0})$. Bis zur Schwelle wächst das Oberflächenpotential mit der Gatespannung; danach steigt die Elektronendichte so steil, dass das Potential fast stehen bleibt und jede weitere Gateladung als Elektronenschicht erscheint.
:::

**Die Akteure:**

- __$n_s$__, __$p_s$__: Elektronen- und Löcherdichte direkt an der Oberfläche; $n_s$ von 176 cm⁻³ im Flachband bis über 10¹⁹ cm⁻³.
- __$n_{p0}$__: Elektronendichte im Inneren, $n_i^2/N_A$ = 176 cm⁻³.

**Das Zusammenspiel:**

**Schritt 1**: Ein positives Oberflächenpotential senkt die Energie der Elektronen an der Oberfläche um $e\psi_s$. Nach der Boltzmann-Verteilung steigt ihre Dichte dort deshalb um den Faktor $\exp(\psi_s/U_T)$, je 59,5 mV um das Zehnfache, während die Löcherdichte ebenso sinkt (Abbildung 4b).

**Schritt 2**: Ab $\psi_s = \Phi_F$ = 0,46 V, bei $U_{GB}$ = −0,15 V, überwiegen an der Oberfläche die Elektronen; bei $U_{GB}$ = 0 sind es 5,6·10¹¹ pro cm³, aber noch eine Million Mal weniger als Rümpfe, und zur Ladung tragen sie nichts bei.

**Schritt 3**: Bei $\psi_s = 2\Phi_F$ = 0,92 V erreicht die Elektronendichte die Dotierung, 5,7·10¹⁷ cm⁻³: Die Oberfläche ist so stark n-leitend wie das Innere p-leitend. Hier beginnt die __starke Inversion__; die Gatespannung dazu ist die __Schwellenspannung__, beim Beispieltransistor 0,50 V.

**Schritt 4** (entscheidender Schritt): Weil die Elektronendichte je 60 mV um das Zehnfache steigt, vervielfacht schon eine kleine Zunahme von $\psi_s$ die Elektronenladung. Von 0,5 V auf 1 V Gatespannung steigt $\psi_s$ nur noch um 0,105 V, die Elektronendichte an der Oberfläche aber auf das Fünfzig- bis Sechzigfache (Abbildung 4a und b).

**Schritt 5**: Die Verarmungszone bleibt deshalb fast gleich tief, 45 nm an der Schwelle und 48 nm bei 1 V; jede weitere Gateladung erscheint als Elektronenschicht, bei 1 V schon 16 000 Elektronen pro µm² (Abbildung 4c). Diese wenige Nanometer dünne Schicht ist die __Inversionsschicht__, im Transistor der __Kanal__.

:::formel Gesetz
$$n_s = n_{p0}\,\exp\Big(\frac{\psi_s}{U_T}\Big) = \frac{n_i^{2}}{N_A}\,\exp\Big(\frac{\psi_s}{U_T}\Big)\,$$
:::

**So liest man das:** Aus dem Oberflächenpotential folgt die Elektronendichte an der Oberfläche. Ohne Bandverbiegung ist sie die Minoritätsdichte des Inneren, beim Oberflächenpotential $\Phi_F$ gleich $n_i$, beim doppelten Wert gleich $N_A$; dazwischen liegen 15 Zehnerpotenzen.

**Kurz gesagt:** Solange die Boltzmann-Verteilung gilt, verzehnfachen je 59,5 mV mehr Oberflächenpotential die Elektronendichte an der Oberfläche.

Idee der Herleitung: Die Elektronen an der Oberfläche und im Inneren gehören zu einem Gleichgewicht; ihr Dichteverhältnis ist der Boltzmann-Faktor des Potentialunterschieds.

:::herleitung
**Ausgangspunkt:** die Boltzmann-Verteilung aus dem Artikel [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell-ausfuehrlich.html): Im thermischen Gleichgewicht ist die Dichte von Teilchen an einem Ort, an dem ihre Energie um $\Delta W$ höher liegt, um den Faktor $\exp(-\Delta W/(k_B T))$ kleiner.

**Annahmen:**
(i) thermisches Gleichgewicht senkrecht zur Oberfläche: Das Oxid lässt keinen Strom durch, und die Elektronen an der Oberfläche tauschen sich mit dem Inneren aus;
(ii) Boltzmann-Näherung, gültig bis etwa 10¹⁹ cm⁻³;
(iii) ein Elektron trägt die Ladung $-e$; wo das Potential um $\psi_s$ höher ist, ist seine Energie um $e\psi_s$ niedriger;
(iv) im Inneren ist $n = n_{p0} = n_i^2/N_A$ (Massenwirkungsgesetz, volle Ionisation).

**Schritt 1**: Nach (iii) ist die Energie der Elektronen an der Oberfläche um $e\psi_s$ niedriger als im Inneren; im Sinn des Ausgangspunkts ist $\Delta W$ hier negativ.

**Schritt 2** (entscheidender Schritt): Nach dem Ausgangspunkt ist die Dichte dort um $\exp(e\psi_s/(k_B T))$ größer; mit $U_T = k_B T/e$:

$$n_s = n_{p0}\,\exp\Big(\frac{\psi_s}{U_T}\Big)$$

**Schritt 3**: Mit (iv):

$$n_s = \frac{n_i^{2}}{N_A}\,\exp\Big(\frac{\psi_s}{U_T}\Big)$$

**Ergebnis:**

$$n_s = n_{p0}\,\exp\Big(\frac{\psi_s}{U_T}\Big) = \frac{n_i^{2}}{N_A}\,\exp\Big(\frac{\psi_s}{U_T}\Big)\,$$

**Woher die Faktoren kommen:** $U_T$ stammt aus der Boltzmann-Verteilung, $n_i^2/N_A$ aus dem Massenwirkungsgesetz. Für die Löcher gilt dasselbe mit umgekehrtem Vorzeichen im Exponenten:

$$p_s = N_A\,\exp\Big(-\frac{\psi_s}{U_T}\Big)$$

**Proben:** An der Schwelle ist das Oberflächenpotential $2\Phi_F$, der Boltzmann-Faktor also das Quadrat von $N_A/n_i$:

$$n_s = \frac{n_i^{2}}{N_A}\cdot\Big(\frac{N_A}{n_i}\Big)^{2} = N_A$$

Zahlenwert: 176 cm⁻³ · exp(0,923 V/25,85 mV) = 176 cm⁻³ · 3,23·10¹⁵ = 5,68·10¹⁷ cm⁻³. Beim Oberflächenpotential $\Phi_F$ ist der Faktor $N_A/n_i$, und Elektronen- und Löcherdichte sind beide gleich $n_i$.

**Grenzen:** Über etwa 10¹⁹ cm⁻³, beim Beispieltransistor ab rund 0,75 V Gatespannung, ist die Oberfläche so dicht besetzt, dass die Boltzmann-Näherung ungenau wird; zudem verteilen sich die Elektronen der wenige Nanometer dünnen Schicht nach den Regeln der Quantenmechanik etwas anders.
:::

::::beispiel Elektronendichte an der Oberfläche zwischen Flachband und Schwelle
**Gegeben:** $n_{p0}$ = 176 cm⁻³, $U_T$ = 25,85 mV; Oberflächenpotentiale 0,5655 V bei $U_{GB}$ = 0, 0,9232 V an der Schwelle ($2\Phi_F$) und 1,0285 V bei $U_{GB}$ = 1 V aus Abbildung 4a.

**Gesucht:** die Elektronendichte an der Oberfläche.

**Rechnung:** Jeweils $n_{p0}$ mal Boltzmann-Faktor:

$$n_s(0{,}5655\ \mathrm V) = 176\ \mathrm{cm^{-3}}\cdot\exp(21{,}87) = 5{,}6\cdot10^{11}\ \mathrm{cm^{-3}}$$

$$n_s(0{,}9232\ \mathrm V) = 176\ \mathrm{cm^{-3}}\cdot\exp(35{,}71) = 5{,}7\cdot10^{17}\ \mathrm{cm^{-3}}$$

$$n_s(1{,}0285\ \mathrm V) = 176\ \mathrm{cm^{-3}}\cdot\exp(39{,}78) = 3{,}3\cdot10^{19}\ \mathrm{cm^{-3}}$$

**Ergebnis:** **5,6·10¹¹ cm⁻³ bei 0 V, 5,7·10¹⁷ cm⁻³ an der Schwelle, 3,3·10¹⁹ cm⁻³ bei 1 V.**

**Einordnung:** Von 0 V bis zur Schwelle wächst die Elektronendichte um sechs Zehnerpotenzen, während das Oberflächenpotential um 0,36 V steigt. Die nächsten 0,105 V bis 1 V Gatespannung bringen noch einmal den Faktor 59; deshalb nimmt das Oberflächenpotential oberhalb der Schwelle kaum noch zu. Der Wert bei 1 V liegt schon an der Grenze der Boltzmann-Näherung: Mit der vollständigen Fermi-Verteilung sind es 2,8·10¹⁹ cm⁻³, das Fünfzigfache der Dotierung.
::::

Diese Beobachtung macht man zur Definition der Schwelle:

:::formel Definition
$$\psi_s = 2\,\Phi_F$$
:::

Man wählt diesen Wert, weil an ihm die Elektronendichte an der Oberfläche die Dotierung erreicht; ab hier wächst die Elektronenladung schneller als die der Rümpfe. Im Banddiagramm heißt das: Das Eigenleitungsniveau ist an der Oberfläche so weit unter das Fermi-Niveau getaucht, wie es im Inneren darüber liegt.

## Die Schwellenspannung

*Welche Gatespannung braucht man bis zur starken Inversion, und wodurch wird sie eingestellt?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/01-schwellenspannung · Vorlage: bilanz-und-kennlinie
**Abbildung 5:** (a) Spannungsbilanz an der Schwelle als Treppe: Die Flachbandspannung $U_\mathrm{FB} = \Phi_\mathrm{MS}$ = −1,027 V, die die Kontaktspannung aufhebt, führt nach unten, das Oberflächenpotential $2\Phi_F$ = 0,923 V und die Spannung über dem Oxid $|Q'_\mathrm{dep,max}|/C'_\mathrm{ox}$ = 0,604 V führen nach oben, zusammen auf $U_{th0}$ = 0,500 V. (b) Schwellenspannung über der Dotierung unter dem Gate, logarithmisch von 10¹⁶ bis 10¹⁸ cm⁻³: −0,14 V bei 10¹⁶, −0,025 V bei 4·10¹⁶, 0,09 V bei 10¹⁷, 0,31 V bei 3·10¹⁷, 0,50 V bei 5,7·10¹⁷ und 0,72 V bei 10¹⁸ cm⁻³; unterhalb der Nulllinie ist der Transistor selbstleitend. Dünn daneben die Kurven für 4,5 nm und 5,5 nm Oxid, beim Beispielwert 0,44 V und 0,56 V. Die Schwellenspannung ist eine Spannungsbilanz aus Flachbandspannung, Oberflächenpotential und Oxidspannung; über die Dotierung unter dem Gate lässt sie sich um mehr als 0,8 V verschieben.
:::

**Die Akteure:**

- __$U_{th0}$__: Schwellenspannung, wenn Bulk und Source auf demselben Potential liegen, wie überall in diesem Artikel; deshalb ist hier $U_{th} = U_{th0}$, beim Beispiel-NMOS 0,50 V.
- __$|Q'_\mathrm{dep,max}|$__: Betrag der Verarmungsladung an der Schwelle; 4,17 fC/µm².

**Das Zusammenspiel:** An der Schwelle verteilt sich die Gate-Bulk-Spannung auf drei Stellen (Abbildung 5a): −1,027 V heben die Kontaktspannung auf, 0,923 V biegen die Oberfläche bis zur starken Inversion, und 0,604 V liegen über dem Oxid, wo sie das Feld zur Verarmungsladung tragen. Die ersten beiden heben sich fast auf; die Schwelle ist im Wesentlichen die Oxidspannung der Verarmungsladung.

:::formel Gesetz
$$U_{th0} = U_\mathrm{FB} + 2\,\Phi_F + \frac{|Q'_\mathrm{dep,max}|}{C'_\mathrm{ox}}, \qquad |Q'_\mathrm{dep,max}| = \sqrt{4\,e\,\varepsilon_\mathrm{Si}\,N_A\,\Phi_F}\,$$
:::

**So liest man das:** Gatematerial, Dotierung unter dem Gate und Oxiddicke legen die Schwelle fest. Mehr Dotierung hebt sie vor allem über den dritten Term, dünneres Oxid senkt ihn. Beim NMOS ist die Schwelle positiv, beim PMOS negativ, typisch einige hundert Millivolt. Liegt der Bulk unter dem Potential der Source, wächst die Verarmungsladung und mit ihr die Schwelle (__Substrateffekt__).

**Kurz gesagt:** An der Schwelle ist die Gatespannung die Summe aus Flachbandspannung, Oberflächenpotential und Oxidspannung; beim Beispieltransistor ist 0,500 V = −1,027 V + 0,923 V + 0,604 V.

Idee der Herleitung: Man teilt die Gate-Bulk-Spannung auf Oxid und Silizium auf, setzt für die Oxidspannung die Verarmungsladung ein und verlangt $\psi_s = 2\Phi_F$.

:::herleitung
**Ausgangspunkt:** die Oxidkapazität, die Flachbandspannung und die Verarmungsladung aus dem Abschnitt *Der MOS-Kondensator*, dazu die Definition der Schwelle über das Oberflächenpotential $2\Phi_F$ (Abschnitt *Inversion*).

**Annahmen:**
(i) Bulk und Source liegen auf gleichem Potential, also ist $U_{GB} = U_{GS}$.
(ii) Oxid und Grenzfläche sind frei von Ladungen.
(iii) Verarmungsnäherung bei gleichmäßiger Dotierung.
(iv) An der Schwelle ist die Elektronenladung klein gegen die Verarmungsladung, 370 gegen 25 700 Elementarladungen pro µm².

**Schritt 1**: Bei $U_{GB} = U_\mathrm{FB}$ liegt über Oxid und Silizium keine Spannung. Was $U_{GB}$ darüber hinausgeht, verteilt sich auf die beiden hintereinanderliegenden Schichten:

$$U_{GB} - U_\mathrm{FB} = U_\mathrm{ox} + \psi_s$$

**Schritt 2**: Nach (ii) und (iv) ist die Gateladung gleich dem Betrag der Verarmungsladung; die Oxidspannung ist also

$$U_\mathrm{ox} = \frac{|Q'_\mathrm{dep}|}{C'_\mathrm{ox}} = \frac{\sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A\,\psi_s}}{C'_\mathrm{ox}}$$

**Schritt 3**: Eingesetzt ergibt sich die Gate-Bulk-Spannung zu jedem Oberflächenpotential in der Verarmung:

$$U_{GB} = U_\mathrm{FB} + \psi_s + \frac{\sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A\,\psi_s}}{C'_\mathrm{ox}}$$

**Schritt 4** (entscheidender Schritt): An der Schwelle ist $\psi_s = 2\Phi_F$, und die Verarmungsladung wird

$$|Q'_\mathrm{dep,max}| = \sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A\cdot2\,\Phi_F} = \sqrt{4\,e\,\varepsilon_\mathrm{Si}\,N_A\,\Phi_F}$$

**Ergebnis:**

$$U_{th0} = U_\mathrm{FB} + 2\,\Phi_F + \frac{|Q'_\mathrm{dep,max}|}{C'_\mathrm{ox}}, \qquad |Q'_\mathrm{dep,max}| = \sqrt{4\,e\,\varepsilon_\mathrm{Si}\,N_A\,\Phi_F}\,$$

**Woher die Faktoren kommen:** $U_\mathrm{FB}$ stammt aus der Kontaktspannung der Materialien, $2\Phi_F$ aus der Definition der starken Inversion, der dritte Term aus dem Gaußschen Gesetz am Oxid; die 4 unter der Wurzel ist die 2 der Dreiecksfläche mal der 2 in $2\Phi_F$.

**Proben:** Einheit: C/cm² geteilt durch F/cm² ergibt V. Zahlenwert: −1,027 V + 0,923 V + 0,604 V = 0,500 V. Die vollständige Rechnung erreicht $\psi_s = 2\Phi_F$ ebenfalls bei 0,500 V; die kleine Elektronenladung und die etwas kleinere Ladung der am Rand verschmierten Zone gleichen sich an dieser Stelle aus. Schritt 3 ergibt bei $U_{GB}$ = 0 ein Oberflächenpotential von 0,558 V, nahe an 0,566 V aus der vollständigen Rechnung.

**Grenzen:** Liegt der Bulk unter der Source, braucht die starke Inversion ein höheres Oberflächenpotential, und die Schwelle steigt. Ladungen im Oxid verschieben $U_\mathrm{FB}$. Sehr kurze Kanäle haben eine niedrigere Schwelle, weil Source und Drain einen Teil der Verarmungsladung selbst binden.
:::

::::beispiel Schwellenspannung des Beispieltransistors und Wirkung der Dotierung
**Gegeben:** $N_A$ = 5,68·10¹⁷ cm⁻³, $C'_\mathrm{ox}$ = 6,906·10⁻⁷ F/cm², $\varepsilon_\mathrm{Si}$ = 1,036·10⁻¹² F/cm, $e$ = 1,602·10⁻¹⁹ C, $n_i$ = 10¹⁰ cm⁻³, $N_L$ = 3,2·10¹⁹ cm⁻³, $U_T$ = 25,85 mV; zum Vergleich die Dotierung einer p-Wanne ohne zusätzliche Implantation, 4·10¹⁶ cm⁻³.

**Gesucht:** die Schwellenspannung, auch mit der schwächeren Dotierung.

**Rechnung:** Fermi-Potential und Flachbandspannung:

$$\Phi_F = 25{,}85\ \mathrm{mV}\cdot\ln(5{,}68\cdot10^{7}) = 0{,}462\ \mathrm V$$

$$U_T\,\ln\frac{N_L}{n_i} = 25{,}85\ \mathrm{mV}\cdot\ln(3{,}2\cdot10^{9}) = 0{,}566\ \mathrm V$$

$$U_\mathrm{FB} = -(0{,}566\ \mathrm V + 0{,}462\ \mathrm V) = -1{,}027\ \mathrm V$$

Verarmungsladung an der Schwelle und ihre Oxidspannung:

$$|Q'_\mathrm{dep,max}| = \sqrt{1{,}74\cdot10^{-13}\ \mathrm{C^2/cm^4}} = 4{,}17\cdot10^{-7}\ \mathrm{C/cm^2}$$

$$\frac{|Q'_\mathrm{dep,max}|}{C'_\mathrm{ox}} = \frac{4{,}17\cdot10^{-7}\ \mathrm{C/cm^2}}{6{,}906\cdot10^{-7}\ \mathrm{F/cm^2}} = 0{,}604\ \mathrm V$$

Die Bilanz:

$$U_{th0} = -1{,}027\ \mathrm V + 0{,}923\ \mathrm V + 0{,}604\ \mathrm V = 0{,}500\ \mathrm V$$

Mit 4·10¹⁶ cm⁻³ ($\Phi_F$ = 0,393 V, $U_\mathrm{FB}$ = −0,959 V, Verarmungsladung 1,02·10⁻⁷ C/cm²):

$$U_{th0} = -0{,}959\ \mathrm V + 0{,}786\ \mathrm V + 0{,}148\ \mathrm V = -0{,}025\ \mathrm V$$

**Ergebnis:** **$U_{th0}$ = 0,500 V; mit 4·10¹⁶ cm⁻³ allein −0,025 V.**

**Einordnung:** Mit dieser Dotierung wäre der Transistor schon bei $U_{GS}$ = 0 leitend. Die Schwelle von 0,5 V entsteht erst, wenn man die Dotierung unter dem Gate durch __Ionenimplantation__, das Einschießen beschleunigter Bor-Ionen, auf 5,7·10¹⁷ cm⁻³ erhöht. 10 % mehr Dotierung heben sie um 34 mV, 0,5 nm mehr Oxid um 60 mV.
::::

Beim PMOS ist alles gespiegelt: Gate aus p⁺-Polysilizium, n-Wanne mit 5,4·10¹⁷ cm⁻³ unter dem Gate, Löcher statt Elektronen. Dieselbe Bilanz mit umgekehrten Vorzeichen, +1,011 V − 0,921 V − 0,590 V, ergibt −0,500 V: Das Gate muss 0,5 V unter der Source liegen, damit ein Löcherkanal entsteht.

## Die Inversionsladung oberhalb der Schwelle

*Wie viel bewegliche Ladung enthält die Inversionsschicht über der Schwelle?*

**Die Akteure:**

- __$Q'_n$__: Ladung der Elektronen in der Inversionsschicht pro Fläche, negativ; 3,45 fC/µm² bei $U_{GB}$ = 1 V im Modell.
- __$U_{GB} - U_{th}$__: die __Gate-Übersteuerung__; 0,5 V bei 1 V.

**Das Zusammenspiel:** Über der Schwelle bleiben Oberflächenpotential und Verarmungsladung fast fest. Jede weitere Gatespannung liegt deshalb über dem Oxid, und die zusätzliche Gateladung, $C'_\mathrm{ox}$ mal dieser Spannung, findet ihre Gegenladung in den Elektronen.

:::formel Formel
$$Q'_n = -C'_\mathrm{ox}\,\big(U_{GB} - U_{th}\big), \qquad U_{GB} > U_{th}\,$$
:::

**So liest man das:** Die Elektronenladung wächst proportional zur Gate-Übersteuerung; das Minuszeichen steht für die negative Ladung der Elektronen. Bei 1 V Gatespannung sind es 3,45 fC/µm², 21 600 Elektronen pro µm² und 216 000 im ganzen Kanal des Beispieltransistors.

Idee der Herleitung: Man zieht von der Gateladung die festgehaltene Verarmungsladung ab.

:::herleitung
**Ausgangspunkt:** die Aufteilung der Gate-Bulk-Spannung auf Oxid und Silizium aus Schritt 1 der Herleitung der Schwellenspannung, die Oxidkapazität und die Gleichheit von Gateladung und Gegenladung im Silizium.

**Annahmen:**
(i) Oberhalb der Schwelle bleibt das Oberflächenpotential bei $\psi_s = 2\Phi_F$.
(ii) Die Verarmungsladung bleibt deshalb bei $|Q'_\mathrm{dep,max}|$.
(iii) Bulk und Source auf gleichem Potential; Oxid ohne Ladung.

**Schritt 1**: Mit (i) ist die Oxidspannung

$$U_\mathrm{ox} = U_{GB} - U_\mathrm{FB} - 2\,\Phi_F$$

**Schritt 2**: Die Gateladung $C'_\mathrm{ox} U_\mathrm{ox}$ teilt sich im Silizium auf Rümpfe und Elektronen auf:

$$C'_\mathrm{ox}\,\big(U_{GB} - U_\mathrm{FB} - 2\,\Phi_F\big) = |Q'_\mathrm{dep,max}| + |Q'_n|$$

**Schritt 3**: Nach der Elektronenladung aufgelöst:

$$|Q'_n| = C'_\mathrm{ox}\,\big(U_{GB} - U_\mathrm{FB} - 2\,\Phi_F\big) - |Q'_\mathrm{dep,max}|$$

**Schritt 4** (entscheidender Schritt): $C'_\mathrm{ox}$ ausgeklammert; die drei abgezogenen Spannungen $U_\mathrm{FB}$, $2\Phi_F$ und $|Q'_\mathrm{dep,max}|/C'_\mathrm{ox}$ sind zusammen genau die Schwellenspannung:

$$|Q'_n| = C'_\mathrm{ox}\,\big(U_{GB} - U_{th}\big)$$

**Ergebnis:** Mit dem negativen Vorzeichen der Elektronenladung:

$$Q'_n = -C'_\mathrm{ox}\,\big(U_{GB} - U_{th}\big), \qquad U_{GB} > U_{th}\,$$

**Woher die Faktoren kommen:** $C'_\mathrm{ox}$ stammt aus dem Oxid; in $U_{th}$ ist alles gesammelt, was schon vor der ersten Elektronenschicht aufgebracht werden muss.

**Proben:** Einheit: F/cm² mal V ergibt C/cm². Bei $U_{GB} = U_{th}$ ist die Elektronenladung null. Zahlenwert bei 1 V: 6,906 fF/µm² · 0,5 V = 3,45 fC/µm².

**Grenzen:** Annahme (i) gilt nur näherungsweise. Die vollständige Rechnung zeigt, dass $\psi_s$ bis 1 V noch um 0,105 V steigt und die Verarmungsladung um 6 % wächst; die Elektronenladung ist dort mit 2,55 fC/µm² um 26 % kleiner als im Modell. Weiter oberhalb wächst sie mit 93 % der Steigung $C'_\mathrm{ox}$, als begänne sie bei 0,60 V statt bei 0,50 V. Wer Transistoren nach diesem Modell berechnet, setzt deshalb eine aus Messungen gewonnene Schwellenspannung ein, die solche Abweichungen aufnimmt.
:::

:::frage
„Woher kommen die Elektronen des Kanals? Im p-Substrat gibt es doch nur 176 pro Kubikzentimeter.“
Im Transistor aus Source und Drain: Die n⁺-Gebiete enthalten 10²⁰ Elektronen pro cm³, und sobald die Oberfläche invertiert ist, trennt sie keine Barriere mehr vom Kanal. Die 216 000 Elektronen bei 1 V stecken in 0,002 µm³ des Source-Gebiets und fließen in Bruchteilen einer Nanosekunde nach. Ein MOS-Kondensator ohne Source müsste sie durch Wärme erzeugen lassen; das dauert beim Beispiel etwa 90 s.
:::

## Vom Kondensator zum Transistor: Sperrbereich und Kanal

*Was ändert sich, wenn neben dem Gate Source und Drain liegen und zwischen ihnen eine Spannung anliegt?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/01-betriebsbereiche · Vorlage: querschnitt-folge
**Abbildung 6:** Oben drei Querschnitte des Beispieltransistors, Source und Bulk an Masse. (a) Sperrbereich bei $U_{GS}$ = 0,3 V und $U_{DS}$ = 1 V: kein Kanal, nur Verarmungszonen um Source und Drain und unter dem Gate. (b) Ohmscher Bereich bei $U_{GS}$ = 1 V und $U_{DS}$ = 0,3 V: Der Kanal reicht von der Source bis zum Drain und wird zum Drain hin keilförmig dünner, am Drain-Ende auf 40 %. (c) Abschnürung bei $U_{GS}$ = 1 V und $U_{DS}$ = 2 V: Der Kanal endet kurz vor dem Drain, dahinter liegt eine 58 nm kurze verarmte Zone, durch die Elektronen zum Drain laufen. Unten die Ladung des Kanals längs des Weges von der Source zum Drain, bezogen auf ihren Wert an der Source, bei $U_{GS}$ = 1 V: Am Drain-Ende sind es 80 % bei $U_{DS}$ = 0,1 V, 40 % bei 0,3 V und null bei 0,5 V. Die Drainspannung hebt das Kanalpotential zum Drain hin an und verdünnt dort den Kanal; bei $U_{DS} = U_{GS} - U_{th}$ verschwindet er am Drain-Ende.
:::

Liegen Source und Bulk an Masse, ist $U_{GB} = U_{GS}$, und an der Source gilt alles über den MOS-Kondensator Gesagte. Unterhalb der Schwelle gibt es keinen Kanal (Abbildung 6a): Jeder Weg eines Elektrons von der Source zum Drain führt über die Barriere des pn-Übergangs zwischen Source und Substrat, der ohne Durchlassspannung sperrt. Dieser __Sperrbereich__ ist der Ruhezustand eines selbstsperrenden Transistors bei $U_{GS}$ = 0.

:::frage
„Fließt unterhalb der Schwelle wirklich gar kein Strom?“
Ein sehr kleiner Strom fließt, denn die Elektronendichte an der Oberfläche fällt unterhalb der Schwelle zwar steil, aber stetig: um den Faktor 10 je 60 mV Oberflächenpotential. Beim Beispieltransistor liegt sie bei $U_{GS}$ = 0,25 V tausendmal und bei 0 V eine Million Mal unter dem Wert an der Schwelle. Für die meisten Schaltungen ist dieser Strom vernachlässigbar; in Chips mit Milliarden Transistoren summiert er sich aber zu einem merklichen Ruhestrom.
:::

Oberhalb der Schwelle verbindet die Inversionsschicht Source und Drain, und der Kanal hat an der Source deren Potential, am Drain das des Drains.

**Die Akteure:**

- __$x$__: Ort längs des Kanals, von 0 an der Source bis $L$ am Drain.
- __$U(x)$__: __Kanalpotential__ gegenüber der Source; 0 an der Source, $U_{DS}$ am Drain.
- __$Q'_n(x)$__: Elektronenladung pro Fläche an der Stelle $x$.

**Das Zusammenspiel:** Das Gate wirkt senkrecht zur Oberfläche, die Drainspannung längs des Kanals; beide treffen sich im Kanalpotential. Die Drainspannung hebt $U(x)$ zum Drain hin an, und um genau diesen Betrag sinkt dort die Spannung zwischen Gate und Kanal, die die Elektronen bindet. Jedes kurze Stück des Kanals ist ein MOS-Kondensator mit seiner eigenen Gate-Kanal-Spannung, und der Kanal wird zum Drain hin keilförmig dünner (Abbildung 6b und unten).

:::formel Formel
$$Q'_n(x) = -C'_\mathrm{ox}\,\big(U_{GS} - U_{th} - U(x)\big)$$
:::

**So liest man das:** An der Source ist die Ladung die des MOS-Kondensators; zum Drain hin sinkt sie bis auf $C'_\mathrm{ox}(U_{GS} - U_{th} - U_{DS})$. Bei $U_{GS}$ = 1 V und $U_{DS}$ = 0,3 V bleiben am Drain-Ende 40 % der Ladung an der Source.

Idee der Herleitung: Man wendet die Inversionsladung des MOS-Kondensators auf jedes kurze Stück des Kanals mit seiner örtlichen Gate-Kanal-Spannung an.

:::herleitung
**Ausgangspunkt:** die Inversionsladung des MOS-Kondensators aus dem Abschnitt *Die Inversionsladung oberhalb der Schwelle*:

$$Q'_n = -C'_\mathrm{ox}\,\big(U_{GB} - U_{th}\big)$$

**Annahmen:**
(i) __Allmählicher Kanal__: Das Kanalpotential ändert sich längs des Kanals langsam, das Feld längs des Kanals ist klein gegen das senkrecht zur Oberfläche. Jedes kurze Stück verhält sich dann wie ein MOS-Kondensator.
(ii) Die Elektronen eines Stücks haben das Potential $U(x)$; für ihre Ladung zählt deshalb die Spannung zwischen Gate und Kanal, wie im Kondensator die zwischen Gate und Bulk.
(iii) Die Schwellenspannung ist längs des Kanals dieselbe wie an der Source.

**Schritt 1**: An der Stelle $x$ liegt zwischen Gate und Kanal die örtliche Spannung, beide gegen die Source gemessen:

$$U_{GC}(x) = U_{GS} - U(x)$$

**Schritt 2** (entscheidender Schritt): Nach (i) und (ii) tritt sie im Ausgangspunkt an die Stelle von $U_{GB}$:

$$Q'_n(x) = -C'_\mathrm{ox}\,\big(U_{GC}(x) - U_{th}\big) = -C'_\mathrm{ox}\,\big(U_{GS} - U_{th} - U(x)\big)$$

**Ergebnis:**

$$Q'_n(x) = -C'_\mathrm{ox}\,\big(U_{GS} - U_{th} - U(x)\big)$$

**Woher die Faktoren kommen:** $C'_\mathrm{ox}$ und $U_{th}$ stammen aus dem MOS-Kondensator, $U(x)$ aus der Drainspannung, die den Kanal zum Drain hin anhebt.

**Proben:** Bei $x$ = 0 ergibt sich die Ladung des Kondensators; bei $U_{DS}$ = 0 ist sie überall gleich. Zahlenwert am Drain-Ende bei $U_{GS}$ = 1 V und $U_{DS}$ = 0,3 V: 6,906 fF/µm² · 0,2 V = 1,38 fC/µm², 40 % des Werts an der Source.

**Grenzen:** Annahme (iii) gilt nur näherungsweise: Wo der Kanal höher liegt als das Substrat, braucht die Inversion etwas mehr Gatespannung, nach demselben Mechanismus wie beim Substrateffekt, und die Ladung zum Drain hin ist etwas kleiner. Annahme (i) versagt nahe dem Ende des Kanals (Abschnitt *Abschnürung*).
:::

## Der ohmsche Bereich

*Wie verhält sich der Transistor, solange die Drain-Source-Spannung klein ist?*

**Die Akteure:**

- __$\mu_n$__: Beweglichkeit der Elektronen im Kanal, ihre Driftgeschwindigkeit pro Feldstärke; 290 cm²/(V s).
- __$K'_n$__, __$K_n$__: Prozessparameter und Steilheitskoeffizient, wie unten definiert; 200 µA/V² und 2 mA/V².
- __$R_\mathrm{on}$__: Widerstand des Kanals bei kleiner Drain-Source-Spannung; 1 kΩ bei $U_{GS}$ = 1 V.

**Das Zusammenspiel:** Ist $U_{DS}$ klein gegen die Gate-Übersteuerung, ist der Kanal überall fast so dick wie an der Source: eine dünne leitende Schicht, durch die die Elektronen im Feld $U_{DS}/L$ driften. Solche Schichten beschreibt man mit ihrem __Schichtwiderstand__ in Ω pro Quadrat, dem Widerstand eines quadratischen Stücks, der von der Größe des Quadrats nicht abhängt; ein Streifen aus $L/W$ Quadraten hintereinander hat das $L/W$-Fache. Der Schichtwiderstand des Kanals sinkt, je mehr Elektronen das Gate bindet. Der Transistor ist also ein Widerstand, dessen Wert die Gatespannung einstellt, und sein Strom wächst proportional zu $U_{DS}$. Den ganzen Bereich mit durchgehendem Kanal, $0 < U_{DS} < U_{GS} - U_{th}$, nennt man deshalb __ohmschen Bereich__, auch Triodenbereich.

:::formel Definition
$$K_n = K'_n\,\frac{W}{L}, \qquad K'_n = \mu_n\,C'_\mathrm{ox}\,$$
:::

Der __Prozessparameter__ $K'_n$ kommt aus der Fertigung, $W/L$ aus dem Schaltungsentwurf; das Produkt, der __Steilheitskoeffizient__ $K_n$, kennzeichnet einen bestimmten Transistor, beim Beispiel-NMOS 2 mA/V².

:::formel Formel
$$R_\mathrm{on} = \frac{L}{W\,\mu_n\,|Q'_n|} = \frac{1}{K_n\,\big(U_{GS} - U_{th}\big)}\,$$
:::

**So liest man das:** Gültig für $U_{DS}$ klein gegen $U_{GS} - U_{th}$: 1 kΩ bei 1 V Gatespannung, halb so viel bei doppelter Übersteuerung, unbegrenzt viel an der Schwelle.

**Kurz gesagt:** Doppelte Gate-Übersteuerung, halber Kanalwiderstand.

Idee der Herleitung: Die Elektronen driften in einer dünnen Schicht, deren Ladung pro Fläche das Gate festlegt.

:::herleitung
**Ausgangspunkt:** die Driftstromdichte der Elektronen mit ihrer Leitfähigkeit aus dem Artikel [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell-ausfuehrlich.html):

$$J = \sigma\,E, \qquad \sigma = e\,n\,\mu_n\,$$

**Annahmen:**
(i) $U_{DS}$ ist klein gegen $U_{GS} - U_{th}$; die Elektronenladung ist überall gleich $Q'_n(0)$.
(ii) Der Strom fließt nur durch Drift, im Feld $U_{DS}/L$, das längs des Kanals überall gleich ist.
(iii) Die Beweglichkeit ist überall gleich.

**Schritt 1**: Eine Schicht der Dicke $d$ mit $n$ Elektronen pro Volumen trägt pro Fläche die Ladung $|Q'_n| = e\,n\,d$. Durch ihren Querschnitt $W d$ fließt im Feld $E$ der Strom

$$I_D = J\,W\,d = e\,n\,\mu_n\,E\,W\,d = \mu_n\,|Q'_n|\,W\,E$$

Dicke und Dichte treten nur als Produkt auf; die Ladung pro Fläche genügt.

**Schritt 2**: Mit dem Feld $E = U_{DS}/L$:

$$I_D = \frac{W\,\mu_n\,|Q'_n|}{L}\,U_{DS}$$

**Schritt 3** (entscheidender Schritt): Der Faktor vor $U_{DS}$ ist der Leitwert. Für $|Q'_n|$ setzt man die Inversionsladung an der Source ein, $C'_\mathrm{ox}$ mal Gate-Übersteuerung, und fasst mit der Definition von $K_n$ zusammen:

$$\frac{1}{R_\mathrm{on}} = \frac{W\,\mu_n\,C'_\mathrm{ox}}{L}\,\big(U_{GS} - U_{th}\big) = K_n\,\big(U_{GS} - U_{th}\big)$$

**Ergebnis:**

$$R_\mathrm{on} = \frac{L}{W\,\mu_n\,|Q'_n|} = \frac{1}{K_n\,\big(U_{GS} - U_{th}\big)}\,$$

**Woher die Faktoren kommen:** $1/(\mu_n |Q'_n|)$ ist der Schichtwiderstand des Kanals, $L/W$ die Zahl der Quadrate hintereinander; $K_n$ fasst Beweglichkeit, Oxidkapazität und Abmessungen zusammen.

**Proben:** Einheit: cm geteilt durch cm · cm²/(V s) · C/cm² ergibt V s/C, also Ω. Zahlenwert bei 1 V: 1/(2 mA/V² · 0,5 V) = 1 kΩ. Grenzfall: Geht $U_{GS}$ gegen $U_{th}$, wächst $R_\mathrm{on}$ über alle Grenzen.

**Grenzen:** Bei größerem $U_{DS}$ wird der Kanal zum Drain hin dünner (Abschnitt *Vom Kondensator zum Transistor*), und der Strom wächst langsamer als proportional zu $U_{DS}$.
:::

::::beispiel Der Beispieltransistor als einstellbarer Widerstand
**Gegeben:** $\mu_n$ = 290 cm²/(V s), $W$ = 10 µm, $L$ = 1 µm, $K_n$ = 2 mA/V², $U_{th}$ = 0,5 V; Gate-Source-Spannungen 1 V, 1,5 V und 2,5 V.

**Gesucht:** Schichtwiderstand und Widerstand des Kanals.

**Rechnung:** Bei 1 V ist die Elektronenladung 3,45·10⁻⁷ C/cm², der Schichtwiderstand

$$R_\square = \frac{1}{290\ \mathrm{cm^2/(V\,s)}\cdot3{,}45\cdot10^{-7}\ \mathrm{C/cm^2}} = 10{,}0\ \mathrm{k\Omega}$$

und mit $L/W$ = 0,1 Quadraten der Kanalwiderstand 1,00 kΩ. Für die übrigen Spannungen:

$$R_\mathrm{on} = \frac{1}{2\ \mathrm{mA/V^2}\cdot\big(U_{GS} - 0{,}5\ \mathrm V\big)} = 1000;\ 500;\ 250\ \Omega$$

**Ergebnis:** **10 kΩ/□ und 1 kΩ bei 1 V, 500 Ω bei 1,5 V, 250 Ω bei 2,5 V.**

**Einordnung:** Als Schalter in einer Schaltung mit 2,5 V hat der Transistor 250 Ω; mit einer Last von 1 pF ergibt das 250 ps als Größenordnung der Umladezeit. Tatsächlich dauert das Umladen länger, weil der Transistor anfangs, solange die Drainspannung über der Abschnürgrenze liegt, nur einen begrenzten Strom liefert (Abschnitt *Abschnürung*). Unterhalb der Schwelle sperrt er.
::::

## Abschnürung

*Was geschieht am Drain-Ende, wenn die Drain-Source-Spannung die Gate-Übersteuerung erreicht, und warum fließt der Strom weiter?*

**Die Akteure:**

- __$U_{GD}$__: Spannung zwischen Gate und Drain, nach der Maschenregel $U_{GS} - U_{DS}$.
- __$U_{DS,\mathrm{ab}}$__: __Abschnürspannung__, die Drain-Source-Spannung, bei der der Kanal am Drain verschwindet; 0,5 V bei $U_{GS}$ = 1 V, auch $U_{DS,\mathrm{sat}}$ genannt.

**Das Zusammenspiel:**

**Schritt 1**: Am Drain-Ende hat der Kanal das Potential $U_{DS}$; zwischen Gate und Kanal liegt dort $U_{GD}$.

**Schritt 2**: Solange $U_{GD}$ über der Schwelle liegt, reicht der Kanal bis zum Drain, nur dünner: bei $U_{GS}$ = 1 V und $U_{DS}$ = 0,3 V mit 40 % der Ladung an der Source (Abbildung 6b).

**Schritt 3**: Bei $U_{DS}$ = $U_{GS} - U_{th}$, beim Beispiel 0,5 V, sinkt $U_{GD}$ auf die Schwelle, und am Drain-Ende ist keine Ladung mehr: Der Kanal ist __abgeschnürt__ (pinch-off).

**Schritt 4** (entscheidender Schritt): Steigt $U_{DS}$ weiter, endet der Kanal ein kleines Stück vor dem Drain. An diesem Abschnürpunkt ist die Ladung null, das Kanalpotential also genau $U_{GS} - U_{th}$. Der Kanal von der Source bis dorthin sieht deshalb unabhängig von $U_{DS}$ dieselbe Spannung wie an der Grenze und führt in erster Näherung denselben Strom.

**Schritt 5**: Der Rest der Spannung fällt über einer kurzen verarmten Zone vor dem Drain ab, bei $U_{DS}$ = 2 V 1,5 V über rund 58 nm (Abbildung 6c). Ihr starkes Feld zieht jedes Elektron, das das Kanalende erreicht, zum Drain, so wie ein Minoritätsträger am Rand einer gesperrten Raumladungszone hinübergezogen wird.

**Schritt 6**: Weil die Zone mit $U_{DS}$ wächst, wird der Kanal etwas kürzer, bei 2 V um 5,8 %, und der Strom steigt leicht an (__Kanallängenmodulation__).

Weil der Strom oberhalb der Grenze kaum von $U_{DS}$ abhängt, wirkt der Transistor dort als Stromquelle, die die Gatespannung steuert; diesen __Abschnürbereich__ nennt man auch Sättigungsbereich. Mit der Sättigung des Bipolartransistors hat das nichts zu tun: Dort leiten beide pn-Übergänge, was dem ohmschen Bereich des MOSFET entspricht; dem Abschnürbereich entspricht beim Bipolartransistor der aktive Bereich.

:::formel Formel
$$U_{DS,\mathrm{ab}} = U_{GS} - U_{th}$$
:::

**So liest man das:** Die Grenze zwischen ohmschem Bereich und Abschnürbereich wächst Volt für Volt mit der Gatespannung: 0,5 V bei 1 V, 2 V bei 2,5 V; an der Schwelle ist sie null.

**Kurz gesagt:** Der Kanal schnürt am Drain ab, sobald die Spannung zwischen Gate und Drain auf die Schwellenspannung gesunken ist.

Idee der Herleitung: Man setzt die örtliche Kanalladung am Drain-Ende null.

:::herleitung
**Ausgangspunkt:** die örtliche Kanalladung aus dem Abschnitt *Vom Kondensator zum Transistor*.

**Annahmen:**
(i) dieselben wie für die örtliche Kanalladung;
(ii) am Drain-Ende ist das Kanalpotential gleich dem Drainpotential, $U(L) = U_{DS}$.

**Schritt 1**: Ladung am Drain-Ende:

$$Q'_n(L) = -C'_\mathrm{ox}\,\big(U_{GS} - U_{th} - U_{DS}\big)$$

**Schritt 2** (entscheidender Schritt): Sie verschwindet, wenn die Klammer null wird:

$$U_{DS,\mathrm{ab}} = U_{GS} - U_{th}$$

**Schritt 3**: Mit der Maschenregel $U_{GD} = U_{GS} - U_{DS}$ lautet dieselbe Bedingung

$$U_{GD} = U_{th}$$

**Ergebnis:**

$$U_{DS,\mathrm{ab}} = U_{GS} - U_{th}$$

**Woher die Faktoren kommen:** Es ist die Schwellenbedingung, angewandt auf das Drain-Ende statt auf die Source.

**Proben:** Einheit V. Zahlenwert: 1 V − 0,5 V = 0,5 V. Grenzfall: Bei $U_{GS} = U_{th}$ gibt es keinen Kanal, und die Grenze liegt bei null.

**Grenzen:** Nahe dem Kanalende ist das Feld längs des Kanals nicht mehr klein; dort versagt die Annahme des allmählichen Kanals, und die Zone zwischen Kanalende und Drain lässt sich nur abschätzen. In sehr kurzen Kanälen begrenzt schon vorher die Höchstgeschwindigkeit der Elektronen den Strom.
:::

::::beispiel Kanal des Beispieltransistors bei 1 V Gatespannung
**Gegeben:** $C'_\mathrm{ox}$ = 6,906 fF/µm², $U_{th}$ = 0,5 V, $U_{GS}$ = 1 V; Drain-Source-Spannungen 0,1 V, 0,3 V, 0,5 V und 2 V; $N_A$ = 5,68·10¹⁷ cm⁻³, also $e N_A$ = 9,10·10⁻² C/cm³, $\varepsilon_\mathrm{Si}$ = 1,036·10⁻¹² F/cm.

**Gesucht:** (a) die Ladung an Source und Drain-Ende; (b) die Abschnürspannung; (c) Länge und Feld der abgeschnürten Zone bei 2 V.

**Rechnung:** (a) An der Source und am Drain-Ende:

$$|Q'_n(0)| = 6{,}906\ \mathrm{fF/\mu m^2}\cdot0{,}5\ \mathrm V = 3{,}45\ \mathrm{fC/\mu m^2}$$

$$|Q'_n(L)| = 6{,}906\ \mathrm{fF/\mu m^2}\cdot\big(0{,}5\ \mathrm V - U_{DS}\big) = 2{,}76;\ 1{,}38;\ 0\ \mathrm{fC/\mu m^2}$$

(b) Abschnürspannung:

$$U_{DS,\mathrm{ab}} = 1\ \mathrm V - 0{,}5\ \mathrm V = 0{,}5\ \mathrm V$$

(c) Über der Zone liegen 2 V − 0,5 V = 1,5 V. Ihre Länge schätzt man mit der Formel für die Tiefe einer einseitigen Verarmungszone (Abschnitt *Verarmung*), angewandt auf die Strecke vor dem Drain:

$$\Delta L^2 \approx \frac{2\cdot1{,}036\cdot10^{-12}\ \mathrm{F/cm}\cdot1{,}5\ \mathrm V}{9{,}10\cdot10^{-2}\ \mathrm{C/cm^3}} = 3{,}41\cdot10^{-11}\ \mathrm{cm^2}$$

$$\Delta L \approx 58{,}4\ \mathrm{nm}, \qquad E \approx \frac{1{,}5\ \mathrm V}{5{,}84\cdot10^{-6}\ \mathrm{cm}} = 2{,}6\cdot10^{5}\ \mathrm{V/cm}\,$$

**Ergebnis:** **Am Drain-Ende 80 %, 40 % und 0 % der Ladung an der Source; Abschnürung bei 0,5 V; bei 2 V liegen 1,5 V über rund 58 nm, im Mittel 2,6·10⁵ V/cm.**

**Einordnung:** Jedes Zehntel Volt Drainspannung nimmt dem Drain-Ende ein Fünftel der Ladung an der Source. Jenseits der Grenze ist die Zone vor dem Drain kein Hindernis, sondern eine kurze Strecke mit starkem Feld, die die Elektronen mit ihrer Höchstgeschwindigkeit von rund 10⁷ cm/s in 0,6 ps durchqueren; der Kanal wird dadurch 5,8 % kürzer.
::::

| Bereich | Bedingung, Kanal und Verhalten |
|---|---|
| Sperrbereich | $U_{GS} < U_{th}$: kein Kanal, nur ein sehr kleiner Strom |
| ohmscher Bereich (Triodenbereich) | $U_{GS} > U_{th}$ und $U_{DS} < U_{GS} - U_{th}$: durchgehender Kanal, zum Drain hin dünner; bei kleinem $U_{DS}$ ein Widerstand $R_\mathrm{on}$ |
| Abschnürbereich (Sättigungsbereich) | $U_{GS} > U_{th}$ und $U_{DS} > U_{GS} - U_{th}$: Kanal vor dem Drain abgeschnürt; Strom fast unabhängig von $U_{DS}$, der Transistor wirkt als Stromquelle |

:::fehlvorstellung
„Ist der Kanal abgeschnürt, fließt kein Strom mehr; er ist doch unterbrochen.“ Das liegt nahe, weil Abschnüren nach dem Zudrücken eines Schlauchs klingt. Der Strom fließt aber weiter, etwa so groß wie an der Abschnürgrenze. Nur das kurze Stück vor dem Drain enthält keine Inversionsschicht, und dort zieht ein starkes Feld jedes ankommende Elektron weiter: Bei 1 V Gatespannung und 2 V am Drain liegen 1,5 V über 58 nm (Abschnitt *Abschnürung*). Wenige schnelle Elektronen tragen dort denselben Strom wie viele langsame im Kanal.
:::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Anreicherung, Verarmung, Inversion | woraus die Gegenladung im Silizium gerade besteht |
| Flachband- und Schwellenspannung | wann der Kondensator ungeladen ist und ab wann zusätzliche Gegenladung aus beweglichen Elektronen besteht |
| Inversionsladung, Kanalwiderstand | wie viel Ladung die Spannung über der Schwelle bindet und wie gut sie leitet |
| keilförmiger Kanal und Abschnürung | jedes Stück des Kanals ist ein Kondensator mit eigener Gate-Kanal-Spannung; am Drain sinkt sie auf die Schwelle |
| Bulk-Anschluss, PMOS | die untere Platte bleibt gegen Source und Drain isoliert; beim PMOS sind alle Vorzeichen gespiegelt |

Gate, Oxid und Halbleiter bilden einen Kondensator: Die Spannung zwischen Gate und Halbleiter legt fest, wie viel Gegenladung unter dem Oxid sitzt, und oberhalb der Schwellenspannung kommt jede weitere Gegenladung als Schicht beweglicher Elektronen hinzu, die Source und Drain als Kanal verbinden; an jeder Stelle des Kanals bestimmt die örtliche Spannung zwischen Gate und Kanal, wie viel Ladung dort den Strom tragen kann.

## Bedeutung und Ausblick

In CMOS-Logik wechseln die Transistoren zwischen Sperrbereich und ohmschem Bereich, aus und ein wie ein Schalter; Verstärker und Stromquellen nutzen den Abschnürbereich, in dem der Strom kaum von der Drainspannung abhängt. Wie groß der Strom in beiden Bereichen ist, leitet der nächste Artikel her, „Kennlinien des NMOS-Transistors“. Die MOS-Diode im Artikel über [Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung.html) ist dieser Beispieltransistor mit verbundenem Gate und Drain.

**In der ausführlichen Fassung:** Verdrahtung, Technologieknoten und Polysilizium-Gate, der CMOS-Querschnitt, die Inversdiode einzelner MOSFETs, Oxidfeld und Schutz gegen elektrostatische Entladung, weitere Beispiele, die Frage, warum die Schwelle bei $2\Phi_F$ liegt, das Banddiagramm als zweite Sichtweise, Datenblatt-Schwellen, Oxidladungen, die Kapazitätskurve und eigene Abbildungen zu Kanalwiderstand und abgeschnürter Zone. [Zur ausführlichen Fassung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/aufbau-und-funktionsweise-ausfuehrlich.html)

:::kern
- Ein NMOS besteht aus n⁺-Source und n⁺-Drain im p-Substrat und einem Gate über wenigen Nanometern Oxid; die Source ist das Gebiet mit dem niedrigeren Potential, der Bulk liegt an der negativsten Spannung.
- Gate, Oxid und Silizium bilden einen Kondensator mit $C'_\mathrm{ox} = \varepsilon_\mathrm{ox}/t_\mathrm{ox}$; die Gegenladung besteht aus Löchern, dann aus festen Akzeptorrümpfen, zu denen oberhalb der Schwelle Elektronen hinzukommen.
- Wegen der Kontaktspannung liegt das Flachband nicht bei 0 V, sondern bei $U_\mathrm{FB} = \Phi_\mathrm{MS}$, beim n⁺-Poly-Gate etwa −1 V.
- Starke Inversion beginnt bei $\psi_s = 2\Phi_F$, wenn die Elektronendichte an der Oberfläche die Dotierung erreicht; darüber bleibt $\psi_s$ fast fest.
- $U_{th0} = U_\mathrm{FB} + 2\Phi_F + |Q'_\mathrm{dep,max}|/C'_\mathrm{ox}$; eingestellt über die Dotierung unter dem Gate und die Oxiddicke.
- Die Kanalladung ist örtlich $Q'_n(x) = -C'_\mathrm{ox}(U_{GS} - U_{th} - U(x))$; für kleine $U_{DS}$ ist der Kanal ein Widerstand $1/(K_n(U_{GS} - U_{th}))$.
- Bei $U_{DS} = U_{GS} - U_{th}$, also $U_{GD} = U_{th}$, schnürt der Kanal am Drain ab; der Strom fließt weiter und hängt danach kaum noch von $U_{DS}$ ab.
- Der PMOS ist das Spiegelbild in einer n-Wanne: Löcherkanal, negative Schwelle, Bulk an der positivsten Spannung.
:::

:::quiz
F: Warum ändert sich das Oberflächenpotential oberhalb der Schwelle kaum noch, obwohl die Gatespannung weiter steigt?
A: Die Elektronendichte an der Oberfläche wächst je 60 mV Oberflächenpotential um das Zehnfache; schon eine kleine Zunahme bringt so viele Elektronen, dass sie die ganze zusätzliche Gateladung aufnehmen. Von 0,5 V auf 1 V Gatespannung steigt das Oberflächenpotential nur um 0,105 V, die Verarmungszone bleibt fast gleich tief.
F: Warum schnürt der Kanal bei $U_{DS} = U_{GS} - U_{th}$ am Drain ab?
A: Am Drain-Ende hat der Kanal das Potential $U_{DS}$, zwischen Gate und Kanal liegt dort also nur $U_{GD} = U_{GS} - U_{DS}$. Sinkt diese Spannung auf die Schwelle, bindet sie keine Elektronen mehr, und die Ladung am Drain-Ende wird null.
F: Stimmt es, dass beim MOS-Kondensator ohne Gatespannung die Bänder flach sind?
A: Nein. Gate aus n⁺-Polysilizium und p-Substrat haben eine Kontaktspannung von 1,03 V; schon bei $U_{GB}$ = 0 ist die Oberfläche 35 nm tief verarmt und liegt 0,57 V über dem Inneren. Flach sind die Bänder erst bei −1,03 V.
F: Stimmt es, dass bei abgeschnürtem Kanal kein Strom mehr fließt?
A: Nein. Der Kanal sieht bis zum Abschnürpunkt weiter die Spannung $U_{GS} - U_{th}$ und führt etwa denselben Strom; die kurze Zone vor dem Drain hat ein starkes Feld, das jedes ankommende Elektron zum Drain zieht, bei 2 V am Drain 1,5 V über 58 nm.
F: Wie setzt sich die Schwellenspannung des Beispieltransistors zusammen?
A: Aus −1,027 V Flachbandspannung, die die Kontaktspannung des Gates aufhebt, +0,923 V Oberflächenpotential bis zur starken Inversion und +0,604 V Oxidspannung für die Verarmungsladung von 4,17 fC/µm², zusammen 0,500 V.
F: Warum muss der Bulk eines NMOS an der negativsten Spannung der Schaltung liegen?
A: Source und Drain bilden mit dem p-Substrat Dioden mit der Anode im Substrat. Nur wenn das Substrat am tiefsten liegt, bleiben alle gesperrt und die Transistoren voneinander isoliert; sonst flösse ab etwa 0,6 V ein Strom ins Substrat.
:::
