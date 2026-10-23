---
title: Aufbau und Funktionsweise des MOSFET
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / MOS-Feldeffekttransistoren
order: 33030100
summary: Wie ein MOS-Feldeffekttransistor aufgebaut ist und warum eine Spannung am isolierten Gate einen leitenden Kanal zwischen Source und Drain erzeugt. Ausführliche Fassung mit NMOS und PMOS, Schaltzeichen und Zählpfeilen, den vier Zuständen des MOS-Kondensators, Herleitung von Kontaktspannung, Verarmungszone, Inversionskriterium, Schwellenspannung, Inversionsladung und Kapazität sowie des keilförmigen Kanals, des Kanalwiderstands und der Abschnürung, durchgerechnet an einem integrierten Beispieltransistor mit 5 nm Gateoxid.
tags: MOSFET, Inversion, Kanal, Schwellenspannung, Schaltsymbol
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Verstärker und Logikgatter brauchen ein Bauelement, bei dem eine Spannung an einem Anschluss den Strom zwischen zwei anderen steuert. Der Bipolartransistor verlangt dafür einen Steuerstrom in die Basis. Der MOS-Feldeffekttransistor, kurz MOSFET, steuert über eine Elektrode, die durch eine wenige Nanometer dünne Isolierschicht vom Halbleiter getrennt ist, und nimmt deshalb im Ruhezustand keinen Steuerstrom auf. Das hat ihn zum häufigsten Bauelement der Elektronik gemacht; große Prozessoren und Speicherchips enthalten Milliarden davon. Alles hängt an einem Prinzip:

**Gate, Oxid und Halbleiter bilden einen Kondensator: Die Spannung zwischen Gate und Halbleiter legt fest, wie viel Gegenladung unter dem Oxid sitzt, und oberhalb der Schwellenspannung kommt jede weitere Gegenladung als Schicht beweglicher Elektronen hinzu, die Source und Drain als Kanal verbinden; an jeder Stelle des Kanals bestimmt die örtliche Spannung zwischen Gate und Kanal, wie viel Ladung dort den Strom tragen kann.**

Vorausgesetzt werden Dotierung, Löcher, Fermi-Niveau und Boltzmann-Verteilung aus [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell-ausfuehrlich.html), die Raumladungszone aus [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie-ausfuehrlich.html) und der Plattenkondensator aus [Kondensator und Kapazität](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/kondensator-und-kapazitaet.html). Auf diesem Artikel bauen die Kennlinien des MOSFET, sein Kleinsignalmodell, die Transistorgrundschaltungen und die digitalen CMOS-Schaltungen auf.

:::grafik
Szene: st1/mos-feldeffekttransistoren/01-querschnitt · Vorlage: querschnitt-layout
**Abbildung 1:** (a) Querschnitt eines n-Kanal-MOSFET, schematisch mit stark vergrößertem Oxid: zwei stark n-dotierte Gebiete, Source links und Drain rechts, im Abstand $L$ = 1 µm in einem p-Substrat; darüber das Gate aus n⁺-Polysilizium auf 5 nm Gateoxid; links der p⁺-Bulkkontakt. Bei $U_{GS}$ = 1 V liegt unter dem Oxid eine dünne Elektronenschicht von Source bis Drain, darunter eine rund 48 nm tiefe Zone fester, negativ geladener Akzeptorrümpfe; die Elektronen fließen von der Source zum Drain, der Strom $I_D$ in den Drain hinein. (b) Draufsicht: Der Transistor entsteht, wo der Polysilizium-Streifen das aktive n-Gebiet kreuzt, mit der Weite $W$ = 10 µm quer und der Länge $L$ = 1 µm längs zur Stromrichtung. Das Gate liegt isoliert über dem Bereich zwischen Source und Drain und steuert ihn nur über sein Feld.
:::

## Aufbau des n-Kanal-MOSFET

*Aus welchen Gebieten besteht ein MOSFET, und welche Abmessungen bestimmen sein Verhalten?*

Integrierte Schaltungen entstehen auf einer dünnen Scheibe aus einkristallinem Silizium, dem __Wafer__, der meist schwach p-dotiert ist. __Dotieren__ heißt, gezielt Fremdatome in den Kristall einzubauen. Ein Boratom hat ein Außenelektron weniger als Silizium; es übernimmt für seine vierte Bindung ein Elektron aus der Nachbarschaft und bleibt als fest eingebauter, negativ geladener Rumpf zurück, ein __Akzeptor__. Die fehlende Bindung, die es hinterlässt, wandert als __Loch__ durch den Kristall und verhält sich wie ein bewegliches Teilchen mit der Ladung $+e$, wobei $e$ die Elementarladung ist (in der Bauelementliteratur oft $q$). Im p-Silizium sind die Löcher deshalb die __Majoritätsträger__, die Ladungsträgersorte in der Überzahl, und die Elektronen die __Minoritätsträger__. Weil das Produkt beider Dichten im thermischen Gleichgewicht immer gleich dem Quadrat der __Eigenleitungsdichte__ $n_i$ = 10¹⁰ cm⁻³ ist, der Ladungsträgerdichte von reinem Silizium bei 300 K (__Massenwirkungsgesetz__), stehen unter dem Gate des Beispieltransistors dieses Artikels 5,7·10¹⁷ Löchern pro Kubikzentimeter nur 176 Elektronen gegenüber.

In dieses Substrat sind zwei Gebiete eingebracht, die mit rund 10²⁰ Donatoren pro Kubikzentimeter sehr stark n-dotiert sind; Donatoren wie Phosphor oder Arsen haben ein Außenelektron mehr als Silizium und geben es als freies Elektron ab. Solche Gebiete kennzeichnet man mit __n⁺__. Sie heißen __Source__ und __Drain__, Quelle und Abfluss der Elektronen. Zwischen ihnen liegt an der Oberfläche das __Kanalgebiet__. Darüber sitzt, durch eine Schicht Siliziumdioxid (SiO₂) von nur 5 nm getrennt, das __Gate__, eine Elektrode aus stark dotiertem, polykristallinem Silizium (__Polysilizium__); es leitet viel schlechter als ein Metall, für eine Elektrode, durch die kein Gleichstrom fließt, aber gut genug. Die Isolierschicht heißt __Gateoxid__. Sie lässt praktisch keinen Gleichstrom durch; das Gate wirkt auf den Halbleiter nur über sein elektrisches Feld.

Zwei Maße bestimmen den Transistor: die __Kanallänge__ $L$, der Abstand zwischen Source und Drain in Stromrichtung, und die __Kanalweite__ $W$ quer dazu. Im Querschnitt sieht man nur $L$; $W$ erscheint in der Draufsicht, dem __Layout__, das die Masken für die Herstellung festlegt (Abbildung 1b). Der Transistor entsteht dort, wo der Streifen aus Polysilizium das aktive n-Gebiet kreuzt. Beim Beispieltransistor ist $W$ = 10 µm und $L$ = 1 µm. Je größer die Weite, desto mehr Strom führt ein Transistor bei gleichen Spannungen, je größer die Länge, desto weniger; die kleinste herstellbare Kanallänge kennzeichnet eine Fertigungstechnologie.

:::frage
„Was bedeutet „32-nm-Technologie“? Ist der Kanal dann 32 nm lang?“
Bis in die 1990er-Jahre gab der Name einer Technologie etwa die kleinste Gatelänge an. Danach wurden die Gates kürzer als der Name: Im 65-nm-Prozess von 2006 waren sie rund 35 nm lang. Heutige Bezeichnungen wie „3 nm“ geben keine einzelne Abmessung mehr an, sondern zählen die Generationen weiter. Wie es dazu kam, zeigt [Von der Röhre zum integrierten Schaltkreis](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/einfuhrung/geschichte-der-schaltungstechnik-ausfuehrlich.html). Für die Funktion zählt allein die tatsächliche Kanallänge $L$.
:::

Source und Drain sind baugleich; vertauscht man die beiden Anschlüsse, erhält man denselben Transistor. Welches Gebiet Source heißt, entscheidet erst die Beschaltung: Beim n-Kanal-Transistor ist die Source das n⁺-Gebiet mit dem niedrigeren Potential, der Drain das mit dem höheren. Die Elektronen fließen dann von der Source zum Drain, der elektrische Strom in Gegenrichtung vom Drain zur Source.

Auch das Substrat braucht einen Anschluss, den __Bulk__ (auch Body oder Substratanschluss), über ein stark p-dotiertes Gebiet (p⁺) an der Oberfläche. Beim n-Kanal-Transistor liegt er an der negativsten Spannung der Schaltung, meist an Masse, und ein Kontakt dient vielen Transistoren gemeinsam. Mit Gate, Source, Drain und Bulk hat der MOSFET vier Anschlüsse.

Verdrahtet wird über Leitbahnen aus Aluminium oder Kupfer in mehreren Ebenen über dem Silizium. Auch Polysilizium kann kurze Verbindungen übernehmen, leitet aber viel schlechter. Man vergleicht dünne Schichten über ihren __Schichtwiderstand__, angegeben in Ω pro Quadrat (Ω/□): den Widerstand eines quadratischen Stücks der Schicht, der von der Größe des Quadrats nicht abhängt, weil ein doppelt so langes Stück auch doppelt so breit ist. Ein Streifen aus zehn Quadraten hintereinander hat den zehnfachen Wert. Polysilizium mit einer aufgebrachten Metall-Silizium-Verbindung (Silizid) hat etwa 1 bis 10 Ω/□, ohne sie 100 bis 300 Ω/□; eine 0,5 µm dicke Aluminiumbahn hat 0,05 Ω/□.

Der Name __MOSFET__ steht für Metal-Oxide-Semiconductor Field-Effect Transistor. Metall, Oxid und Halbleiter sind die drei Schichten unter dem Gate, wie sie die ersten Transistoren mit Gates aus Aluminium hatten; Feldeffekt heißt, dass das elektrische Feld des Gates den Strom steuert. Weil sein leitender Kanal aus Elektronen besteht, heißt dieser Transistor __n-Kanal-MOSFET__ oder kurz __NMOS__.

:::frage
„Warum besteht das Gate aus Polysilizium und nicht aus Metall, wie der Name sagt?“
Aluminium schmilzt bei 660 °C, die Gebiete von Source und Drain werden aber erst nach dem Gate bei rund 1000 °C ausgeheilt. Ein Gate aus Polysilizium übersteht das und dient beim Dotieren von Source und Drain selbst als Maske: Beide Gebiete enden an seinen Kanten, bis auf eine kleine seitliche Ausdehnung unter das Gate, ohne dass man eine zweite Maske ausrichten muss (selbstjustierendes Gate). Außerdem lässt sich Polysilizium n⁺ oder p⁺ dotieren, was die Schwellenspannung von NMOS und PMOS passend verschiebt (Abschnitt *Die Schwellenspannung*). Seit 2007 ersetzen die schnellsten Prozesse das Gateoxid durch Isolatoren hoher Permittivität, weil Oxide von nur noch gut einem Nanometer Dicke zu viele Elektronen durchtunneln ließen; dazu gehören wieder Metallgates, weil Polysilizium an der Grenze zu diesen Isolatoren selbst verarmt und sich schlecht mit ihnen verträgt.
:::

## PMOS, CMOS und der Bulk-Anschluss

*Wie baut man den komplementären Transistor auf demselben Substrat, und warum liegt der Bulk an der negativsten Spannung?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/01-cmos-wanne · Vorlage: querschnitt
**Abbildung 2:** Querschnitt eines CMOS-Prozesses. Links ein NMOS im p-Substrat mit n⁺-Source und -Drain, Gate aus n⁺-Polysilizium und p⁺-Bulkkontakt an Masse; rechts ein PMOS in einer n-Wanne mit p⁺-Source und -Drain, Gate aus p⁺-Polysilizium und n⁺-Wannenkontakt an $U_B$ = 2,5 V. Eingezeichnet sind die pn-Übergänge als Dioden: n⁺-Gebiete gegen das Substrat, p⁺-Gebiete gegen die Wanne und die Wanne gegen das Substrat. Weil das Substrat an der niedrigsten und die Wanne an der höchsten Spannung liegt, ist jede dieser Dioden gesperrt, und die Transistoren sind voneinander isoliert.
:::

Der p-Kanal-MOSFET, kurz __PMOS__, ist das Spiegelbild des NMOS: Source und Drain sind stark p-dotiert (p⁺), der leitende Kanal besteht aus Löchern, und das Gebiet unter dem Gate muss n-dotiert sein. Auf einem p-Substrat schafft man dafür zuerst eine __n-Wanne__, ein tief eingebrachtes n-Gebiet, in dem beliebig viele PMOS Platz finden (Abbildung 2). Ihr Anschluss, ein n⁺-Kontakt, liegt an der höchsten Spannung der Schaltung, der Versorgungsspannung $U_B$. Beim PMOS ist die Source das p⁺-Gebiet mit dem höheren Potential, und Spannungen und Strom sind im Betrieb negativ. Stehen NMOS und PMOS auf demselben Chip, spricht man von __CMOS__ (complementary MOS); fast alle digitalen und die meisten analogen integrierten Schaltungen sind so aufgebaut.

Jedes n⁺-Gebiet eines NMOS bildet mit dem p-Substrat einen pn-Übergang, also eine Diode mit der Anode im Substrat (Abbildung 2). Liegt das Substrat auf dem niedrigsten Potential der Schaltung, ist jede dieser Dioden gesperrt oder spannungslos, wie hoch Source und Drain auch liegen; es fließt nur der winzige Sperrstrom einer gesperrten Diode. Läge der Bulk dagegen höher als eine Source oder ein Drain, würde diese Diode in Durchlassrichtung gepolt, und ab etwa 0,6 V flösse ein Strom ins Substrat, der an der Funktion des Transistors vorbeigeht. Spiegelbildlich sperrt die Wanne an $U_B$ alle p⁺-Gebiete der PMOS und zugleich den Übergang zwischen Wanne und Substrat. So sind alle Transistoren eines Chips über gesperrte Übergänge gegeneinander isoliert. Zeichnet man den Bulkanschluss im Schaltplan nicht ein, gilt diese Regel stillschweigend: Bulk des NMOS an der negativsten Spannung, meist Masse, Bulk des PMOS an der positivsten, $U_B$.

:::frage
„Warum hat ein einzelner MOSFET im Gehäuse nur drei Anschlüsse?“
Bei Einzeltransistoren ist der Bulk schon im Gehäuse mit der Source verbunden. Die Diode zwischen Bulk und Drain liegt dann zwischen Source und Drain, beim NMOS mit der Anode an der Source. Diese __Inversdiode__ (body diode) sperrt im normalen Betrieb, leitet aber, sobald der Drain mehr als etwa 0,6 V unter die Source gezogen wird; in Brückenschaltungen für Motoren übernimmt sie den Strom, während beide Transistoren eines Zweigs kurz gesperrt sind. Source und Drain sind bei solchen Transistoren nicht mehr vertauschbar.
:::

## Schaltzeichen und Zählpfeile

*Wie stellt man NMOS und PMOS im Schaltplan dar, und wie zählt man ihre Spannungen und Ströme?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/01-schaltzeichen · Vorlage: schaltsymbol-tabelle
**Abbildung 3:** Drei verbreitete Schaltzeichen, oben für den NMOS, unten für den PMOS. (a) An den Bipolartransistor angelehnt: ein Pfeil an der Source wie am Emitter, beim NMOS nach außen, beim PMOS nach innen. (b) Aus der Digitaltechnik: ohne Pfeil, der PMOS mit einem Kreis am Gate. (c) Nach DIN: unterbrochene Kanallinie für den selbstsperrenden Typ und eigener Bulkanschluss B mit Pfeil, beim NMOS zum Kanal hin, beim PMOS von ihm weg. In jedem Symbol zählt $U_{GS}$ vom Gate zur Source, $U_{DS}$ vom Drain zur Source, und $I_D$ fließt in den Drain hinein; daneben klein der selbstleitende NMOS mit durchgehender Kanallinie. Alle Schreibweisen bezeichnen dasselbe Bauteil, und beim PMOS steht die Source oben, weil sie das höhere Potential hat.
:::

Für MOSFETs sind drei Schreibweisen verbreitet (Abbildung 3). Die erste lehnt sich an den Bipolartransistor an: Ein Pfeil an der Source zeigt wie der Emitterpfeil die Richtung des Stroms, beim NMOS aus der Source heraus, beim PMOS in sie hinein. Die zweite stammt aus der Digitaltechnik und ist in Simulationsprogrammen üblich; sie verzichtet auf den Pfeil und kennzeichnet den PMOS durch einen Kreis am Gate, der daran erinnert, dass er bei niedriger Gatespannung leitet. Die dritte, nach DIN, zeichnet den Kanal als senkrechte Linie und den Bulk als eigenen Anschluss mit einem Pfeil, der wie im Diodensymbol von p nach n zeigt: beim NMOS vom p-Bulk zum n-Kanal, beim PMOS vom p-Kanal zum n-Bulk.

Die unterbrochene Kanallinie des DIN-Symbols steht für den __selbstsperrenden__ Typ, auch Anreicherungstyp (enhancement): Ohne Gatespannung gibt es keinen Kanal, und der Transistor sperrt. Ein __selbstleitender__ Typ, auch Verarmungstyp (depletion), hat schon ohne Gatespannung einen Kanal, den erst eine Gatespannung entfernt; sein Symbol hat eine durchgehende Linie. Selbstleitende Transistoren dienten in der frühen MOS-Logik als Lastelemente. CMOS-Schaltungen brauchen sie nicht, und viele Technologien bieten sie nicht mehr an; dieser Artikel behandelt deshalb den selbstsperrenden Typ.

Spannungen werden vom ersten zum zweiten Index gezählt: $U_{GS}$ ist das Potential des Gates minus das der Source, $U_{DS}$ das des Drains minus das der Source, $U_{BS}$ das des Bulks minus das der Source. Ströme zählen in den Anschluss hinein positiv; $I_D$ fließt also in den Drain. Im Betrieb eines NMOS sind $U_{GS}$, $U_{DS}$ und $I_D$ positiv, beim PMOS negativ. Den NMOS zeichnet man mit dem Drain oben, den PMOS mit der Source oben, sodass das höhere Potential jeweils oben liegt.

Diese Spannungen beziehen sich immer auf die Source, nicht nur, wenn sie an Masse liegt. Der Transistor reagiert nur auf Potentialdifferenzen zwischen seinen Anschlüssen: Hebt man alle vier gemeinsam um 1 V an, ändert sich kein Feld und kein Strom. Drei Differenzen beschreiben ihn deshalb vollständig, $U_{GS}$, $U_{DS}$ und $U_{BS}$. Dass man gerade die Source als Bezug wählt, hat einen physikalischen Grund: Dort treten die Elektronen in den Kanal ein, der Kanal hat an der Source deren Potential, und ob es überhaupt einen Kanal gibt, entscheidet die Spannung zwischen Gate und Source (Abschnitt *Vom Kondensator zum Transistor*). Liegt die Source nicht an Masse, etwa in einem Source-Folger oder einer Differenzstufe, muss man $U_{GS}$ aus beiden Potentialen bilden.

## Der MOS-Kondensator

*Was macht eine Spannung zwischen Gate und Substrat mit den Ladungsträgern unter dem Oxid, solange noch kein Strom fließt?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/01-mos-zustaende · Vorlage: querschnitt-folge
**Abbildung 4:** Der MOS-Kondensator des Beispieltransistors (Gate aus n⁺-Polysilizium, 5 nm Oxid, p-Silizium mit 5,7·10¹⁷ cm⁻³, Bulk an Masse) in vier Zuständen, vollständig gerechnet (ohne Verarmungsnäherung, mit der Boltzmann-Verteilung). (a) Anreicherung bei $U_{GB}$ = −2 V: Unter dem Oxid sammeln sich Löcher, 5,94 fC/µm². (b) Flachband bei $U_{GB}$ = −1,03 V: keine Ladung, kein Feld. (c) Verarmung bei $U_{GB}$ = 0: Die Löcher sind verdrängt, zurück bleibt eine 35 nm tiefe Zone fester Akzeptorrümpfe mit 3,19 fC/µm²; die Oberfläche liegt 0,57 V über dem Inneren. (d) Inversion bei $U_{GB}$ = 1 V: Direkt unter dem Oxid liegt eine dünne Elektronenschicht mit 2,55 fC/µm² über einer 48 nm tiefen Zone mit 4,35 fC/µm²; die Oberfläche liegt 1,03 V über dem Inneren. Zur Ladung des Gates gehört immer eine gleich große Gegenladung im Silizium; mit wachsender Spannung besteht sie erst aus Löchern, dann aus festen Rümpfen, und oberhalb der Schwelle kommen bewegliche Elektronen hinzu.
:::

Gate, Oxid und Substrat bilden einen Kondensator, zwei leitende Schichten mit einem Isolator dazwischen. Um zu verstehen, was das Gate bewirkt, lässt man Source und Drain zunächst weg und betrachtet nur diese Schichtfolge zwischen Gate und Bulk, den __MOS-Kondensator__.

**Die Akteure:**

- __$U_{GB}$__: Spannung zwischen Gate und Bulk; in V; im Beispiel zwischen −2 V und 2,5 V. Sie lädt den Kondensator.
- __$t_\mathrm{ox}$__: Dicke des Gateoxids; 5 nm.
- __$\varepsilon_\mathrm{ox}$__: Permittivität des Oxids, das 3,9-Fache der elektrischen Feldkonstante; 3,45·10⁻¹³ F/cm.
- __$C'_\mathrm{ox}$__: Kapazität des Oxids pro Fläche; in fF/µm²; 6,91 fF/µm². Der Strich kennzeichnet hier und bei allen weiteren Größen den Bezug auf die Fläche.
- __$Q'_G$__: Ladung des Gates pro Fläche; in fC/µm², wobei 1 fC/µm² gleich 10⁻⁷ C/cm² ist; einige fC/µm².
- __$U_\mathrm{ox}$__: Spannung über dem Oxid; in V. Sie trägt das Feld, das die Gegenladung im Silizium bindet.
- __$\psi_s$__: __Oberflächenpotential__, das Potential der Siliziumoberfläche unter dem Oxid gegenüber dem neutralen Inneren des Substrats; in V; im Beispiel zwischen −0,1 V und 1,1 V. Es misst, wie stark das Gate die Oberfläche verändert.

**Das Zusammenspiel:** Das Oxid enthält im Idealfall keine Ladung. Nach dem Gaußschen Gesetz enden deshalb alle Feldlinien, die von der Ladung des Gates ausgehen, auf einer gleich großen Gegenladung im Silizium direkt darunter: Was das Gate pro Fläche trägt, trägt das Silizium mit umgekehrtem Vorzeichen. Die Spannung entscheidet nur, wie groß diese Ladung ist und woraus sie besteht. Im p-Silizium kommen dafür drei Sorten in Frage: bewegliche Löcher, die festen Akzeptorrümpfe und bewegliche Elektronen. Welche es jeweils sind, zeigen die vier Zustände in Abbildung 4; in der Inversion sind es Rümpfe und Elektronen zusammen. Abbildung 4 ist wie Abbildung 5 eine __vollständige Rechnung__: Feld und Potential folgen aus allen Ladungen, und die beweglichen Ladungsträger verteilen sich überall nach der Boltzmann-Verteilung. Die Formeln dieses Artikels nähern diese Rechnung; wo sie davon abweichen, steht es dabei.

Mit der Ladung hängt die Spannung über dem Oxid wie bei einem Plattenkondensator zusammen, dessen Platten das Gate und die Siliziumoberfläche sind:

:::formel Formel
$$C'_\mathrm{ox} = \frac{\varepsilon_\mathrm{ox}}{t_\mathrm{ox}}, \qquad Q'_G = C'_\mathrm{ox}\,U_\mathrm{ox}\,$$
:::

**So liest man das:** Aus Permittivität und Dicke des Oxids folgt seine Kapazität pro Fläche und mit ihr die Ladung, die eine Spannung über dem Oxid bindet. Je dünner das Oxid, desto mehr Ladung bindet dieselbe Spannung; 5 nm ergeben 6,91 fF/µm², die 10 µm² des Beispieltransistors also 69 fF. Die Oxidspannung ist nur ein Teil von $U_{GB}$: Ein weiterer Teil fällt im Silizium ab, das Oberflächenpotential $\psi_s$, und ein dritter ist die Kontaktspannung zwischen den Materialien (Abschnitt *Flachband und Kontaktspannung*).

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

::::beispiel Oxidkapazität und Oxidfeld des Beispieltransistors
**Gegeben:** Oxiddicke 5 nm; Permittivität des Oxids 3,9 · 8,854·10⁻¹⁴ F/cm = 3,453·10⁻¹³ F/cm; Kanalfläche $W L$ = 10 µm · 1 µm = 10 µm²; Durchschlagsfeldstärke von Siliziumdioxid rund 10 MV/cm.

**Gesucht:** (a) die Kapazität pro Fläche und die Gatekapazität $C_\mathrm{ox}$ des Transistors; (b) das Feld bei 1 V über dem Oxid und die Spannung, bei der das Oxid durchschlägt; (c) wie viel Ladung ein elektrostatisch aufgeladener Mensch im Vergleich dazu mitbringt.

**Rechnung:** (a) Kapazität pro Fläche und für die ganze Kanalfläche:

$$C'_\mathrm{ox} = \frac{3{,}453\cdot10^{-13}\ \mathrm{F/cm}}{5\cdot10^{-7}\ \mathrm{cm}} = 6{,}91\cdot10^{-7}\ \mathrm{F/cm^2} = 6{,}91\ \mathrm{fF/\mu m^2}$$

$$C_\mathrm{ox} = C'_\mathrm{ox}\,W L = 6{,}91\ \mathrm{fF/\mu m^2}\cdot10\ \mathrm{\mu m^2} = 69{,}1\ \mathrm{fF}$$

(b) Feld als Spannung durch Dicke, Durchschlag bei 10 MV/cm:

$$E_\mathrm{ox} = \frac{1\ \mathrm V}{5\cdot10^{-7}\ \mathrm{cm}} = 2\cdot10^{6}\ \mathrm{V/cm}$$

$$U_\mathrm{ox,max} \approx 10^{7}\ \mathrm{V/cm}\cdot5\cdot10^{-7}\ \mathrm{cm} = 5\ \mathrm V$$

(c) Prüfnormen für elektrostatische Entladung bilden einen aufgeladenen Menschen als 100 pF auf 2 kV nach; das Gate nimmt bis zum Durchschlag $C_\mathrm{ox}$ mal 5 V auf:

$$Q_\mathrm{Mensch} = 100\ \mathrm{pF}\cdot2\ \mathrm{kV} = 200\ \mathrm{nC}, \qquad Q_\mathrm{Gate} = 69{,}1\ \mathrm{fF}\cdot5\ \mathrm V = 0{,}345\ \mathrm{pC}\,$$

**Ergebnis:** **6,91 fF/µm² und 69 fF; 1 V erzeugt 2 MV/cm, bei etwa 5 V schlägt das Oxid durch, und eine Berührung bringt rund 580 000-mal mehr Ladung mit, als das Gate bis dahin aufnimmt.**

**Einordnung:** 2 MV/cm sind fast das Siebzigfache der Feldstärke, bei der Luft durchschlägt (rund 30 kV/cm). Deshalb hat jeder Eingang einer CMOS-Schaltung Schutzdioden zu den Versorgungsleitungen, die eine Entladung ableiten, bevor die Spannung am Gate gefährlich wird. Eine Versorgungsspannung von 2,5 V setzt das 5-nm-Oxid dauerhaft knapp 5 MV/cm aus; dünnere Oxide verlangen niedrigere Spannungen.
::::

### Anreicherung

Ist das Gate deutlich negativ gegenüber dem Substrat, trägt es negative Ladung, und die Gegenladung im p-Silizium besteht aus Löchern, die das Feld an die Oberfläche zieht (Abbildung 4a). Bei $U_{GB}$ = −2 V sammeln sich dort 5,9 fC/µm², und direkt an der Oberfläche ist die Löcherdichte, mit der vollständigen Fermi-Verteilung gerechnet, mit gut 3·10¹⁹ cm⁻³ fast 60-mal so hoch wie im Inneren. Diesen Zustand nennt man __Anreicherung__ oder Akkumulation. Weil die Löcherschicht nur wenige Nanometer dick ist, verhält sich die Struktur fast wie ein Plattenkondensator mit der Kapazität $C'_\mathrm{ox}$.

### Flachband und Kontaktspannung

Zur Erinnerung aus [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell-ausfuehrlich.html): Das __Banddiagramm__ trägt die Energie der Elektronen über dem Ort auf. Freie Elektronen haben Energien ab der __Leitungsbandkante__ $W_L$, Löcher sitzen an der __Valenzbandkante__ $W_V$, und das __Eigenleitungsniveau__ $W_i$ liegt nahe der Mitte dazwischen. Das __Fermi-Niveau__ $W_F$ zeigt, wie die Zustände besetzt sind: Je näher es an $W_L$ liegt, desto mehr freie Elektronen gibt es, je näher an $W_V$, desto mehr Löcher; in reinem Silizium liegt es bei $W_i$.

Zwischen Anreicherung und Verarmung liegt der Zustand, in dem weder Gate noch Silizium Ladung tragen. Das Feld ist überall null, das Oberflächenpotential ebenfalls, und im Banddiagramm verlaufen die Bänder bis an die Oberfläche waagerecht. Die Gate-Bulk-Spannung dieses Zustands heißt __Flachbandspannung__ $U_\mathrm{FB}$. Man würde sie bei 0 V erwarten; beim Beispieltransistor liegt sie aber bei −1,03 V, weil Gate und Substrat verschieden dotiert sind.

**Die Akteure:**

- __$N_A$__: Akzeptordichte im Substrat unter dem Gate; in cm⁻³; 5,68·10¹⁷.
- __$U_T$__: Temperaturspannung $k_B T/e$; 25,85 mV bei 300 K. Eine Potentialstufe von 59,5 mV ändert eine Dichte im Gleichgewicht um den Faktor 10.
- __$N_L$__: effektive Zustandsdichte des Leitungsbands, die Elektronendichte, bei der das Fermi-Niveau die Leitungsbandkante erreicht; 3,2·10¹⁹ cm⁻³.
- __$\Phi_F$__: __Fermi-Potential__, der Abstand des Fermi-Niveaus unter dem Eigenleitungsniveau im Substrat, in Volt; 0,462 V.
- __$\Phi_\mathrm{MS}$__: __Austrittsarbeitsdifferenz__ zwischen Gate und Substrat, in Volt; −1,027 V. Sie ist gleich der Flachbandspannung und verschiebt alle Zustände zu negativeren Gatespannungen.

**Das Zusammenspiel:** Verbindet man Gate und Bulk über einen Draht, gilt dasselbe wie zwischen den beiden Seiten eines pn-Übergangs: Im thermischen Gleichgewicht liegt das Fermi-Niveau überall gleich hoch, sonst flössen Elektronen vom höheren zum tieferen ([Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell-ausfuehrlich.html), Abschnitt *Der pn-Übergang*). Im n⁺-Polysilizium liegt das Fermi-Niveau an der Leitungsbandkante, mit $n_i$ = 10¹⁰ cm⁻³ gerechnet 0,566 eV über dem Eigenleitungsniveau, im p-Substrat 0,462 eV darunter. Damit beide gleich hoch liegen, müssen die Bänder des Gates um 1,027 eV tiefer liegen als die des Substrats, und eine tiefere Elektronenenergie bedeutet ein höheres Potential: Das Gate liegt 1,027 V über dem Inneren des Substrats. Diese eingebaute Spannung heißt __Kontaktspannung__.

Sie entsteht, indem beim Verbinden einige Elektronen vom Gate durch den Draht ins Substrat fließen. Das Gate lädt sich positiv auf, und die Kontaktspannung fällt über dem Oxid und an der Siliziumoberfläche ab. Schon bei $U_{GB}$ = 0 ist die Oberfläche deshalb verarmt (Abbildung 4c); erst eine Gegenspannung von −1,027 V hebt die Kontaktspannung auf, und diese Gegenspannung ist die Flachbandspannung. Man schreibt sie als __Austrittsarbeitsdifferenz__ $\Phi_\mathrm{MS}$: den Unterschied der __Austrittsarbeiten__ von Gate und Halbleiter, also der Energien, die ein Elektron vom Fermi-Niveau ins Vakuum heben, geteilt durch $e$. Die Kontaktspannung ist ihr Negatives, +1,027 V.

:::formel Formel
$$\Phi_F = U_T\,\ln\frac{N_A}{n_i}$$

$$\begin{aligned}U_\mathrm{FB} = \Phi_\mathrm{MS} &= -\Big(U_T\,\ln\frac{N_L}{n_i} + \Phi_F\Big)\\ &= -U_T\,\ln\frac{N_L\,N_A}{n_i^{2}}\end{aligned}$$
:::

**So liest man das:** Eingaben sind die Dotierung des Substrats und die Temperatur, Ausgabe ist die Gate-Bulk-Spannung, bei der der Kondensator ungeladen ist. Das Fermi-Potential wächst um 59,5 mV je Zehnerpotenz Dotierung; die Kontaktspannung ist die Summe dieser Strecke und der des Gates, 0,566 V, und die Flachbandspannung ihr Negatives, weil man das höher liegende Gate um diesen Betrag absenken muss. Bei höherer Substratdotierung wird $U_\mathrm{FB}$ noch etwas negativer. Ein Gate aus p⁺-Polysilizium, dessen Fermi-Niveau an der Valenzbandkante liegt, hätte auf demselben Substrat nur +0,09 V.

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

::::beispiel Kontakt- und Flachbandspannung des Beispieltransistors
**Gegeben:** Substrat mit $N_A$ = 5,68·10¹⁷ cm⁻³ unter dem Gate; $n_i$ = 10¹⁰ cm⁻³; $N_L$ = 3,2·10¹⁹ cm⁻³; $U_T$ = 25,85 mV; Gate aus n⁺-Polysilizium; zum Vergleich die Dotierung einer p-Wanne ohne zusätzliche Implantation, 4·10¹⁶ cm⁻³.

**Gesucht:** Fermi-Potential, Kontakt- und Flachbandspannung, auch für die schwächere Dotierung.

**Rechnung:** Die beiden Strecken zwischen Fermi-Niveau und Eigenleitungsniveau:

$$\Phi_F = 25{,}85\ \mathrm{mV}\cdot\ln(5{,}68\cdot10^{7}) = 25{,}85\ \mathrm{mV}\cdot17{,}86 = 0{,}462\ \mathrm V$$

$$U_T\,\ln\frac{N_L}{n_i} = 25{,}85\ \mathrm{mV}\cdot\ln(3{,}2\cdot10^{9}) = 25{,}85\ \mathrm{mV}\cdot21{,}89 = 0{,}566\ \mathrm V$$

Ihre Summe mit negativem Vorzeichen:

$$U_\mathrm{FB} = \Phi_\mathrm{MS} = -(0{,}566\ \mathrm V + 0{,}462\ \mathrm V) = -1{,}027\ \mathrm V$$

Mit 4·10¹⁶ cm⁻³:

$$\Phi_F = 25{,}85\ \mathrm{mV}\cdot\ln(4\cdot10^{6}) = 0{,}393\ \mathrm V, \qquad \Phi_\mathrm{MS} = -0{,}959\ \mathrm V\,$$

**Ergebnis:** **$\Phi_F$ = 0,462 V, Kontaktspannung 1,027 V und $U_\mathrm{FB}$ = −1,027 V; mit 4·10¹⁶ cm⁻³ 0,393 V, 0,959 V und −0,959 V.**

**Einordnung:** Die Kontaktspannung ist größer als die Diffusionsspannung der Beispieldiode mit je 10¹⁶ cm⁻³ (0,714 V), weil das Gate so stark dotiert ist, dass sein Fermi-Niveau bis an die Bandkante reicht. Sie hängt nur logarithmisch von der Dotierung ab: 14-mal mehr Akzeptoren ändern sie um 69 mV.
::::

:::fehlvorstellung
„Ohne Spannung am Gate sind die Bänder flach, und die Oberfläche unter dem Oxid ist neutral.“ Das liegt nahe, weil ein Kondensator ohne Spannung keine Ladung trägt. Für den MOS-Kondensator stimmt es nur, wenn Gate und Halbleiter dasselbe Fermi-Niveau hätten. Beim Gate aus n⁺-Polysilizium auf p-Silizium wirkt schon bei $U_{GB}$ = 0 die Kontaktspannung von 1,03 V: Das Gate trägt 3,19 fC/µm² positive Ladung, die Oberfläche ist 35 nm tief verarmt und liegt 0,57 V über dem Inneren (Abbildung 4c). Flach sind die Bänder erst bei $U_{GB}$ = −1,03 V.
:::

### Verarmung

Zwischen Flachbandspannung und Schwelle trägt das Gate positive Ladung. Ihr Feld drängt die beweglichen Löcher von der Oberfläche weg ins Innere des Substrats; die Löcher wandern mit dem Feld fort, und über den Bulkanschluss fließt dabei ein kurzer Ladestrom. Zurück bleiben die Akzeptorrümpfe, fest im Gitter und negativ geladen, nun ohne ihre Löcher in der Nähe. Sie bilden eine __Verarmungszone__, die so tief reicht, bis ihre Ladung die des Gates ausgleicht (Abbildung 4c); diesen Zustand nennt man __Verarmung__. Es ist dieselbe Raumladungszone wie an einem pn-Übergang ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie-ausfuehrlich.html), Abschnitt *Die Raumladungszone unter Spannung*), nur einseitig: Die Gegenladung sitzt nicht in einem n-Gebiet, sondern auf dem Gate. Weil jede Schicht nur die feste Dichte $e N_A$ an Ladung beisteuert, muss die Zone tiefer werden, wenn die Gateladung wächst.

**Die Akteure:**

- __$\varepsilon_\mathrm{Si}$__: Permittivität von Silizium, das 11,7-Fache der Feldkonstante; 1,036·10⁻¹² F/cm.
- __$y_d$__: Tiefe der Verarmungszone unter dem Oxid; in nm; 35 nm bei $U_{GB}$ = 0, 45 nm an der Schwelle.
- __$Q'_\mathrm{dep}$__: Ladung der Verarmungszone pro Fläche, negativ; ihr Betrag in der Verarmung von 0 bis rund 4,2 fC/µm² an der Schwelle, bei $U_{GB}$ = 0 rund 3,2 fC/µm².

:::formel Formel
$$y_d = \sqrt{\frac{2\,\varepsilon_\mathrm{Si}\,\psi_s}{e\,N_A}}$$

$$|Q'_\mathrm{dep}| = e\,N_A\,y_d = \sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A\,\psi_s}$$
:::

**So liest man das:** Aus dem Oberflächenpotential folgen Tiefe und Ladung der Zone; beide wachsen mit der Wurzel von $\psi_s$. Höhere Dotierung macht die Zone flacher, aber ihre Ladung größer, weil die Rümpfe dichter stehen. Nach der Formel reicht die Zone bei 0,57 V 36 nm tief, bei 0,92 V 46 nm; die vollständige Rechnung ergibt 35 und 45 nm.

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

::::beispiel Verarmungszone bei 0 V und an der Schwelle
**Gegeben:** $N_A$ = 5,68·10¹⁷ cm⁻³, $\varepsilon_\mathrm{Si}$ = 1,036·10⁻¹² F/cm, $e$ = 1,602·10⁻¹⁹ C; Oberflächenpotential 0,566 V bei $U_{GB}$ = 0 (Abbildung 4c) und 0,923 V an der Schwelle.

**Gesucht:** Tiefe und Ladung der Verarmungszone und die Zahl der freigelegten Rümpfe pro µm².

**Rechnung:** Tiefe bei 0,566 V:

$$y_d = \sqrt{\frac{2\cdot1{,}036\cdot10^{-12}\ \mathrm{F/cm}\cdot0{,}566\ \mathrm V}{1{,}602\cdot10^{-19}\ \mathrm C\cdot5{,}68\cdot10^{17}\ \mathrm{cm^{-3}}}} = 3{,}59\cdot10^{-6}\ \mathrm{cm} = 35{,}9\ \mathrm{nm}$$

Ladung und Zahl der Rümpfe pro Fläche:

$$|Q'_\mathrm{dep}| = e\,N_A\,y_d = 3{,}27\cdot10^{-7}\ \mathrm{C/cm^2} = 3{,}27\ \mathrm{fC/\mu m^2}, \qquad N_A\,y_d = 2{,}04\cdot10^{12}\ \mathrm{cm^{-2}}\,$$

An der Schwelle ist das Potential 1,63-mal so groß, Tiefe und Ladung wachsen um die Wurzel davon, den Faktor 1,28:

$$y_d = 45{,}8\ \mathrm{nm}, \qquad |Q'_\mathrm{dep}| = 4{,}17\ \mathrm{fC/\mu m^2}\,$$

**Ergebnis:** **36 nm und 3,27 fC/µm² bei 0 V, 20 400 Rümpfe pro µm²; 46 nm und 4,17 fC/µm² an der Schwelle, 26 000 Rümpfe pro µm².**

**Einordnung:** Die Zone ist viel flacher als die Raumladungszone der Beispieldiode mit 10¹⁶ cm⁻³ (0,43 µm), weil die Rümpfe 57-mal dichter stehen. Die vollständige Rechnung ergibt bei 0 V 3,19 statt 3,27 fC/µm² und 35 statt 36 nm; die Näherung ist auf 2 bis 3 % genau.
::::

:::fehlvorstellung
„Die Verarmungszone entsteht, weil Löcher und Elektronen an der Oberfläche miteinander rekombinieren.“ Das liegt nahe, weil sich am pn-Übergang tatsächlich Elektronen und Löcher treffen und rekombinieren. Unter dem Gate gibt es aber kaum Elektronen, mit denen die Löcher rekombinieren könnten, nur 176 pro Kubikzentimeter gegenüber 5,7·10¹⁷ Löchern. Die Löcher verschwinden nicht, sie werden vom Feld des positiv geladenen Gates in die Tiefe geschoben. Bei $U_{GB}$ = 0 sind so rund 20 000 Löcher pro Quadratmikrometer aus einer 35 nm tiefen Schicht verdrängt (Abschnitt *Verarmung*).
:::

## Inversion: wie die Oberfläche n-leitend wird

*Warum entsteht bei genügend positiver Gatespannung unter dem Oxid eine Schicht aus Elektronen, und warum wächst danach fast nur noch sie?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/01-oberflaechenpotential · Vorlage: gestapelte-kennlinien
**Abbildung 5:** Der MOS-Kondensator des Beispieltransistors über der Gate-Bulk-Spannung von −2 V bis 1,5 V, vollständig gerechnet; Marken bei $U_\mathrm{FB}$ = −1,03 V und $U_{th0}$ = 0,50 V. (a) Oberflächenpotential: 0,57 V bei 0 V, 0,92 V (das Doppelte des Fermi-Potentials) an der Schwelle, danach fast waagerecht, 1,03 V bei 1 V. (b) Elektronendichte (blau) und Löcherdichte (rot) an der Oberfläche, logarithmisch: Sie kreuzen sich bei 10¹⁰ cm⁻³ und −0,15 V; die Elektronendichte erreicht an der Schwelle die Dotierung, 5,7·10¹⁷ cm⁻³, und bei 1 V 3,3·10¹⁹ cm⁻³, mit der vollständigen Fermi-Verteilung statt ihrer Boltzmann-Näherung 2,8·10¹⁹ cm⁻³. (c) Beträge der Flächenladungen: Die Verarmungsladung (grau) steigt bis 4,11 fC/µm² an der Schwelle und bleibt danach fast konstant, die Elektronenladung (blau) wächst fast linear, 2,55 fC/µm² bei 1 V; gestrichelt das Ladungsmodell $C'_\mathrm{ox}(U_{GB} - U_{th0})$. Bis zur Schwelle wächst das Oberflächenpotential mit der Gatespannung; danach steigt die Elektronendichte so steil, dass das Potential fast stehen bleibt und jede weitere Gateladung als Elektronenschicht erscheint.
:::

**Die Akteure:**

- __$n_s$__, __$p_s$__: Elektronen- und Löcherdichte direkt an der Oberfläche; in cm⁻³; $n_s$ von 176 cm⁻³ im Flachband bis über 10¹⁹ cm⁻³.
- __$n_{p0}$__: Elektronendichte im neutralen Inneren des Substrats, nach dem Massenwirkungsgesetz $n_i^2/N_A$; 176 cm⁻³.

**Das Zusammenspiel:**

**Schritt 1**: Ein positives Oberflächenpotential senkt die Energie der Elektronen an der Oberfläche um $e\psi_s$ gegenüber dem Inneren. Nach der Boltzmann-Verteilung ist ihre Dichte dort deshalb um den Faktor $\exp(\psi_s/U_T)$ größer, je 59,5 mV um das Zehnfache; die Löcherdichte sinkt um denselben Faktor (Abbildung 5b).

**Schritt 2**: Bei $\psi_s = \Phi_F$ = 0,46 V, beim Beispieltransistor bei $U_{GB}$ = −0,15 V, sind beide Dichten gleich $n_i$ = 10¹⁰ cm⁻³: Die Oberfläche ist eigenleitend. Darüber überwiegen an der Oberfläche die Elektronen; sie ist im wörtlichen Sinn invertiert. Bei $U_{GB}$ = 0 kommen dort 5,6·10¹¹ Elektronen pro cm³ auf 1,8·10⁸ Löcher. Zur Ladung tragen sie trotzdem nichts bei, denn sie sind noch eine Million Mal seltener als die Rümpfe.

**Schritt 3**: Bei $\psi_s = 2\Phi_F$ = 0,92 V erreicht die Elektronendichte an der Oberfläche die Dotierung, 5,7·10¹⁷ cm⁻³: Die Oberfläche ist so stark n-leitend wie das Innere p-leitend. Von hier an spricht man von __starker Inversion__, und die Gatespannung, bei der das eintritt, ist die __Schwellenspannung__, beim Beispieltransistor 0,50 V.

**Schritt 4** (entscheidender Schritt): Weil die Elektronendichte je 60 mV um das Zehnfache steigt, genügt nun eine kleine Zunahme des Oberflächenpotentials, um die Elektronenladung zu vervielfachen. Von 0,5 V auf 1 V Gatespannung steigt $\psi_s$ nur noch um 0,105 V, vier Temperaturspannungen, die Elektronendichte an der Oberfläche aber auf das Fünfzig- bis Sechzigfache, rund 3·10¹⁹ cm⁻³ (Abbildung 5a und b).

**Schritt 5**: Die Verarmungszone, deren Ladung nur mit der Wurzel von $\psi_s$ wächst, bleibt deshalb fast gleich tief: 45 nm an der Schwelle, 48 nm bei 1 V, 49 nm bei 2,5 V. Jede weitere Gateladung erscheint als Elektronenschicht. Pro Quadratmikrometer sind es 370 Elektronen an der Schwelle, 16 000 bei 1 V und 77 000 bei 2,5 V, während die Zahl der Rümpfe nur von 25 700 auf 27 900 steigt; Abbildung 5c zeigt den Verlauf bis 1,5 V. Diese wenige Nanometer dicke Elektronenschicht direkt unter dem Oxid ist die __Inversionsschicht__; im Transistor bildet sie den __Kanal__.

:::formel Gesetz
$$n_s = n_{p0}\,\exp\Big(\frac{\psi_s}{U_T}\Big) = \frac{n_i^{2}}{N_A}\,\exp\Big(\frac{\psi_s}{U_T}\Big)\,$$
:::

**So liest man das:** Eingabe ist das Oberflächenpotential, Ausgabe die Elektronendichte an der Oberfläche. Ohne Bandverbiegung ist sie die winzige Minoritätsdichte des Inneren, 176 cm⁻³; beim Oberflächenpotential $\Phi_F$ ist sie gleich $n_i$, beim doppelten Wert gleich $N_A$. Zwischen Flachband und Schwelle wächst sie um 15 Zehnerpotenzen.

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
**Gegeben:** $n_{p0}$ = 176 cm⁻³, $U_T$ = 25,85 mV; Oberflächenpotentiale 0 (Flachband), 0,4616 V ($\Phi_F$), 0,5655 V ($U_{GB}$ = 0), 0,9232 V ($2\Phi_F$) und 1,0285 V ($U_{GB}$ = 1 V) aus Abbildung 5a.

**Gesucht:** die Elektronendichte an der Oberfläche in allen fünf Fällen.

**Rechnung:** Jeweils $n_{p0}$ mal Boltzmann-Faktor:

$$n_s(0{,}4616\ \mathrm V) = 176\ \mathrm{cm^{-3}}\cdot\exp(17{,}86) = 1{,}0\cdot10^{10}\ \mathrm{cm^{-3}}$$

$$n_s(0{,}5655\ \mathrm V) = 176\ \mathrm{cm^{-3}}\cdot\exp(21{,}87) = 5{,}6\cdot10^{11}\ \mathrm{cm^{-3}}$$

$$n_s(0{,}9232\ \mathrm V) = 176\ \mathrm{cm^{-3}}\cdot\exp(35{,}71) = 5{,}7\cdot10^{17}\ \mathrm{cm^{-3}}$$

$$n_s(1{,}0285\ \mathrm V) = 176\ \mathrm{cm^{-3}}\cdot\exp(39{,}78) = 3{,}3\cdot10^{19}\ \mathrm{cm^{-3}}$$

**Ergebnis:** **176 cm⁻³ im Flachband, 10¹⁰ cm⁻³ bei $\Phi_F$, 5,6·10¹¹ cm⁻³ bei 0 V, 5,7·10¹⁷ cm⁻³ an der Schwelle und 3,3·10¹⁹ cm⁻³ bei 1 V.**

**Einordnung:** Zwischen Flachband und Schwelle wächst die Elektronendichte um 15 Zehnerpotenzen, während sich das Oberflächenpotential um 0,92 V ändert. Die letzten 0,105 V bis 1 V Gatespannung bringen noch einmal den Faktor 59; deshalb nimmt das Oberflächenpotential oberhalb der Schwelle kaum noch zu. Der Wert bei 1 V liegt schon an der Grenze der Boltzmann-Näherung: Mit der vollständigen Fermi-Verteilung sind es 2,8·10¹⁹ cm⁻³, das Fünfzigfache der Dotierung.
::::

Diese Beobachtung macht man zur Definition der Schwelle:

:::formel Definition
$$\psi_s = 2\,\Phi_F$$
:::

Man wählt gerade diesen Wert, weil an ihm die Elektronendichte an der Oberfläche die Dotierung erreicht: Ab hier wächst die Elektronenladung schneller als die der Rümpfe, und zusätzliche Gateladung erscheint fast nur noch als Elektronenschicht.

:::frage
„Die Oberfläche ist doch schon bei $\psi_s = \Phi_F$ n-leitend. Warum legt man die Schwelle erst bei $2\Phi_F$ fest?“
Zwischen $\Phi_F$ und $2\Phi_F$ überwiegen an der Oberfläche zwar die Elektronen, aber in so geringer Zahl, dass sie zur Ladung und zur Leitfähigkeit kaum beitragen; man spricht von __schwacher Inversion__. Beim Beispieltransistor liegen bei $U_{GB}$ = 0 an der Oberfläche 5,6·10¹¹ Elektronen pro cm³, eine Million Mal weniger als Rümpfe. Erst mit $n_s = N_A$ beginnt der Zustand, in dem die Elektronenschicht die zusätzliche Ladung trägt. Die Grenze ist eine Vereinbarung, der Übergang ist fließend; auch in schwacher Inversion fließt bereits ein kleiner Strom.
:::

Dasselbe zeigt das Banddiagramm (Abbildung 6), in dem die Energie der Elektronen nach oben aufgetragen ist. Ein positives Oberflächenpotential senkt diese Energie an der Oberfläche; die Bänder biegen sich nach unten, während das Fermi-Niveau im Gleichgewicht waagerecht bleibt. Taucht das Eigenleitungsniveau an der Oberfläche unter das Fermi-Niveau, überwiegen dort die Elektronen. Die Schwelle ist erreicht, wenn es dort so weit darunter liegt, wie es im Inneren darüber liegt, um $e\Phi_F$ = 0,46 eV, also nach einer Biegung um 0,92 eV. Beide Bilder führen zur selben Zahl. Primär ist die Rechnung mit Potential und Ladung, denn aus ihr folgen die Spannungen; das Banddiagramm zeigt anschaulich, warum die Dichten exponentiell vom Abstand zwischen Bandkante und Fermi-Niveau abhängen.

:::grafik
Szene: st1/mos-feldeffekttransistoren/01-baender · Vorlage: banddiagramm-folge
**Abbildung 6:** Banddiagramme unter dem Oxid über der Tiefe von 0 bis 100 nm, mit Leitungsbandkante $W_L$, Valenzbandkante $W_V$, Eigenleitungsniveau $W_i$ (gepunktet) und dem waagerechten Fermi-Niveau $W_F$ (gestrichelt). (a) Verarmung bei $U_{GB}$ = 0: Die Bänder sind an der Oberfläche um 0,57 eV nach unten gebogen, über 35 nm; $W_i$ liegt dort schon 0,10 eV unter $W_F$. (b) Schwelle bei 0,50 V: Biegung um 0,92 eV über 45 nm; im Inneren liegt $W_i$ 0,46 eV über $W_F$, an der Oberfläche 0,46 eV darunter. (c) Starke Inversion bei 1 V: Biegung um 1,03 eV, die Leitungsbandkante nähert sich an der Oberfläche dem Fermi-Niveau, und im Knick sammelt sich die Elektronenschicht. Inversion heißt im Banddiagramm, dass das Eigenleitungsniveau an der Oberfläche unter das Fermi-Niveau taucht; die Schwelle ist erreicht, wenn es dort so weit darunter liegt wie im Inneren darüber.
:::

## Die Schwellenspannung

*Welche Gatespannung braucht man, bis die Oberfläche stark invertiert ist, und wodurch wird sie eingestellt?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/01-schwellenspannung · Vorlage: bilanz-und-kennlinie
**Abbildung 7:** (a) Spannungsbilanz an der Schwelle als Treppe: Die Flachbandspannung $U_\mathrm{FB} = \Phi_\mathrm{MS}$ = −1,027 V, die die Kontaktspannung aufhebt, führt nach unten, das Oberflächenpotential $2\Phi_F$ = 0,923 V und die Spannung über dem Oxid $|Q'_\mathrm{dep,max}|/C'_\mathrm{ox}$ = 0,604 V führen nach oben, zusammen auf $U_{th0}$ = 0,500 V. (b) Schwellenspannung über der Dotierung unter dem Gate, logarithmisch von 10¹⁶ bis 10¹⁸ cm⁻³: −0,14 V bei 10¹⁶, −0,025 V bei 4·10¹⁶, 0,09 V bei 10¹⁷, 0,31 V bei 3·10¹⁷, 0,50 V bei 5,7·10¹⁷ und 0,72 V bei 10¹⁸ cm⁻³; unterhalb der Nulllinie ist der Transistor selbstleitend. Dünn daneben die Kurven für 4,5 nm und 5,5 nm Oxid, beim Beispielwert 0,44 V und 0,56 V. Die Schwellenspannung ist eine Spannungsbilanz aus Flachbandspannung, Oberflächenpotential und Oxidspannung; über die Dotierung unter dem Gate lässt sie sich um mehr als 0,8 V verschieben.
:::

**Die Akteure:**

- __$U_{th0}$__: Schwellenspannung, wenn Bulk und Source auf demselben Potential liegen; in V; 0,50 V beim Beispiel-NMOS. Weil in diesem Artikel der Bulk immer auf Source-Potential liegt, ist die Schwellenspannung $U_{th}$ hier gleich $U_{th0}$. Verbreitet ist auch der Name Einsatzspannung; Simulatoren nennen sie VTO.
- __$|Q'_\mathrm{dep,max}|$__: Betrag der Verarmungsladung an der Schwelle, also bei $\psi_s = 2\Phi_F$; 4,17 fC/µm².

**Das Zusammenspiel:** An der Schwelle verteilt sich die Gate-Bulk-Spannung auf drei Stellen (Abbildung 7a). Ein Teil hebt die Kontaktspannung auf, −1,027 V; ein Teil biegt die Oberfläche um $2\Phi_F$ = 0,923 V; der dritte liegt über dem Oxid und trägt dort das Feld, das zur Verarmungsladung gehört, 0,604 V. Flachbandspannung und Oberflächenpotential heben sich fast auf, sodass die Schwelle von 0,50 V im Wesentlichen die Oxidspannung für die Verarmungsladung ist.

:::formel Gesetz
$$U_{th0} = U_\mathrm{FB} + 2\,\Phi_F + \frac{|Q'_\mathrm{dep,max}|}{C'_\mathrm{ox}}, \qquad |Q'_\mathrm{dep,max}| = \sqrt{4\,e\,\varepsilon_\mathrm{Si}\,N_A\,\Phi_F}\,$$
:::

**So liest man das:** Eingaben sind Gatematerial und Dotierung unter dem Gate, die über $U_\mathrm{FB}$, $\Phi_F$ und die Verarmungsladung eingehen, sowie die Oxiddicke über $C'_\mathrm{ox}$; Ausgabe ist die Gatespannung, ab der ein Kanal besteht. Mehr Dotierung hebt die Schwelle vor allem über den dritten Term, weil mehr Rümpfe mehr Gateladung verlangen; ein dünneres Oxid senkt sie, weil dieselbe Ladung dann weniger Oxidspannung braucht. Beim NMOS ist sie positiv, beim PMOS negativ, und übliche Werte liegen bei einigen hundert Millivolt. Liegt der Bulk unter dem Potential der Source, wächst die Verarmungsladung und mit ihr die Schwelle; das ist der __Substrateffekt__.

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
**Gegeben:** $N_A$ = 5,68·10¹⁷ cm⁻³, $C'_\mathrm{ox}$ = 6,906·10⁻⁷ F/cm², $\varepsilon_\mathrm{Si}$ = 1,036·10⁻¹² F/cm, $e$ = 1,602·10⁻¹⁹ C; $\Phi_F$ = 0,462 V und $U_\mathrm{FB}$ = −1,027 V aus dem Abschnitt *Flachband und Kontaktspannung*. Zum Vergleich die Dotierung einer p-Wanne ohne zusätzliche Implantation, 4·10¹⁶ cm⁻³ mit $\Phi_F$ = 0,393 V und $U_\mathrm{FB}$ = −0,959 V, und Oxiddicken von 4,5 und 5,5 nm.

**Gesucht:** die Schwellenspannung, mit der schwächeren Dotierung und bei geänderter Oxiddicke.

**Rechnung:** Das Produkt unter der Wurzel und die Verarmungsladung an der Schwelle:

$$4\,e\,\varepsilon_\mathrm{Si}\,N_A\,\Phi_F = 1{,}74\cdot10^{-13}\ \mathrm{C^2/cm^4}$$

$$|Q'_\mathrm{dep,max}| = \sqrt{1{,}74\cdot10^{-13}\ \mathrm{C^2/cm^4}} = 4{,}17\cdot10^{-7}\ \mathrm{C/cm^2}$$

Die Oxidspannung dazu und die Bilanz:

$$\frac{|Q'_\mathrm{dep,max}|}{C'_\mathrm{ox}} = \frac{4{,}17\cdot10^{-7}\ \mathrm{C/cm^2}}{6{,}906\cdot10^{-7}\ \mathrm{F/cm^2}} = 0{,}604\ \mathrm V$$

$$U_{th0} = -1{,}027\ \mathrm V + 0{,}923\ \mathrm V + 0{,}604\ \mathrm V = 0{,}500\ \mathrm V$$

Mit 4·10¹⁶ cm⁻³ ist die Verarmungsladung 1,02·10⁻⁷ C/cm², die Oxidspannung 0,148 V:

$$U_{th0} = -0{,}959\ \mathrm V + 0{,}786\ \mathrm V + 0{,}148\ \mathrm V = -0{,}025\ \mathrm V$$

Mit 4,5 nm Oxid ist $C'_\mathrm{ox}$ um den Faktor 5/4,5 größer und die Oxidspannung entsprechend kleiner, mit 5,5 nm umgekehrt; die Schwelle wird 0,440 V bzw. 0,560 V.

**Ergebnis:** **$U_{th0}$ = 0,500 V; mit 4·10¹⁶ cm⁻³ −0,025 V; mit 4,5 nm und 5,5 nm Oxid 0,44 V und 0,56 V.**

**Einordnung:** Mit dieser Dotierung allein wäre der Transistor schon bei $U_{GS}$ = 0 leitend. Die gewünschte Schwelle entsteht erst, wenn man die Dotierung unter dem Gate durch __Ionenimplantation__, das Einschießen beschleunigter Bor-Ionen in die Oberfläche, gezielt auf 5,7·10¹⁷ cm⁻³ erhöht. Ein Zehntel Nanometer Oxid verschiebt die Schwelle um 12 mV; daher die engen Toleranzen der Fertigung.
::::

Beim PMOS ist alles gespiegelt. Sein Gate aus p⁺-Polysilizium hat das Fermi-Niveau an der Valenzbandkante, die n-Wanne ist unter dem Gate mit 5,4·10¹⁷ cm⁻³ dotiert, und die Bänder müssen sich an der Oberfläche nach oben biegen, bis sich dort Löcher sammeln. Mit umgekehrten Vorzeichen ergibt dieselbe Bilanz +1,011 V − 0,921 V − 0,590 V = −0,500 V: Das Gate muss 0,5 V unter der Source liegen, damit ein Kanal aus Löchern entsteht. Die Dotierungen des Beispiel-Transistorpaars sind so gewählt, dass beide Schwellen den Betrag 0,50 V haben.

:::frage
„Im Datenblatt eines Einzeltransistors steht als Schwellenspannung 0,8 bis 3,0 V. Ist das dieselbe Größe?“
Dieselbe Idee, aber anders gemessen. Datenblätter definieren die Schwelle über einen Strom, beim 2N7000 als die Gate-Source-Spannung, bei der mit verbundenem Gate und Drain 1 mA fließt. Der Wert hängt deshalb von der Größe des Transistors ab: Bei kleinen Transistoren muss für 1 mA schon ein Kanal bestehen, und er liegt über der Schwelle dieses Artikels; bei sehr weiten kann der Prüfstrom schon unterhalb von ihr fließen. Die weite Spanne zeigt, wie empfindlich die Schwelle auf die Fertigung reagiert: Schon beim Beispieltransistor verschieben 10 % mehr Dotierung unter dem Gate sie um 34 mV und 0,5 nm mehr Oxid um 60 mV. In Simulationsmodellen ist die Schwellenspannung deshalb ein Parameter, den man aus Messungen bestimmt.
:::

:::vertiefung
**Wie Ladungen im Oxid die Schwelle verschieben.** Ein reales Gateoxid enthält nahe der Grenzfläche feste positive Ladungen, typisch 10¹⁰ bis 10¹¹ Elementarladungen pro cm². Ihr Feld übernimmt einen Teil der Aufgabe der Gateladung, sodass sich alle Zustände zu kleineren Gatespannungen verschieben. Sitzt die Ladung pro Fläche $Q'_\mathrm{ox}$ an der Grenzfläche, so muss das Gate im Flachband die Gegenladung $-Q'_\mathrm{ox}$ tragen, und dafür liegt über dem Oxid die Spannung $-Q'_\mathrm{ox}/C'_\mathrm{ox}$:

$$U_\mathrm{FB} = \Phi_\mathrm{MS} - \frac{Q'_\mathrm{ox}}{C'_\mathrm{ox}}$$

Beim Beispieltransistor senken 5·10¹⁰ Elementarladungen pro cm² die Schwelle um 11,6 mV. Dazu kommen Zustände an der Grenzfläche, die je nach Oberflächenpotential Elektronen aufnehmen oder abgeben. Dass die Grenzfläche zwischen Silizium und seinem eigenen Oxid besonders wenige solcher Zustände hat, ist ein Hauptgrund dafür, dass Silizium die Mikroelektronik beherrscht.
:::

## Die Inversionsladung oberhalb der Schwelle

*Wie viel bewegliche Ladung enthält die Inversionsschicht, wenn die Gatespannung über der Schwelle liegt?*

**Die Akteure:**

- __$Q'_n$__: Ladung der Elektronen in der Inversionsschicht pro Fläche, negativ; ihr Betrag 3,45 fC/µm² bei $U_{GB}$ = 1 V im Modell.
- __$U_{GB} - U_{th}$__: die __Gate-Übersteuerung__, um wie viel die Gatespannung über der Schwelle liegt; 0,5 V bei $U_{GB}$ = 1 V.

**Das Zusammenspiel:** Oberhalb der Schwelle bleibt das Oberflächenpotential fast bei $2\Phi_F$ und die Verarmungsladung fast bei ihrem Wert an der Schwelle (Abschnitt *Inversion*). Jede weitere Gatespannung liegt deshalb über dem Oxid, und die zusätzliche Gateladung, $C'_\mathrm{ox}$ mal diese Spannung, findet ihre Gegenladung in den Elektronen der Inversionsschicht (Abbildung 5c).

:::formel Formel
$$Q'_n = -C'_\mathrm{ox}\,\big(U_{GB} - U_{th}\big), \qquad U_{GB} > U_{th}\,$$
:::

**So liest man das:** Eingabe ist die Gate-Übersteuerung, Ausgabe die Elektronenladung pro Fläche; sie wächst proportional mit der Übersteuerung, und das Minuszeichen steht für die negative Ladung der Elektronen. Bei 1 V Gatespannung sind es 3,45 fC/µm², also 21 600 Elektronen pro µm². Unterhalb der Schwelle ist die Elektronenladung in diesem Modell null.

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

::::beispiel Elektronen im Kanal des Beispieltransistors
**Gegeben:** $C'_\mathrm{ox}$ = 6,906 fF/µm², $U_{th}$ = 0,50 V; Source und Bulk an Masse, also $U_{GB} = U_{GS}$, mit 1 V und 1,5 V; Kanalfläche 10 µm²; $e$ = 1,602·10⁻¹⁹ C.

**Gesucht:** Elektronenladung pro Fläche, Zahl der Elektronen pro µm² und im ganzen Kanal.

**Rechnung:** Bei 1 V ist die Übersteuerung 0,5 V:

$$|Q'_n| = 6{,}906\ \mathrm{fF/\mu m^2}\cdot0{,}5\ \mathrm V = 3{,}45\ \mathrm{fC/\mu m^2}$$

Durch die Elementarladung geteilt:

$$\frac{|Q'_n|}{e} = \frac{3{,}45\cdot10^{-15}\ \mathrm{C/\mu m^2}}{1{,}602\cdot10^{-19}\ \mathrm C} = 21\,600\ \mathrm{\mu m^{-2}}$$

Mal 10 µm² ergibt 216 000 Elektronen im Kanal. Bei 1,5 V ist die Übersteuerung doppelt so groß, und alle Werte verdoppeln sich.

**Ergebnis:** **3,45 fC/µm², 21 600 Elektronen pro µm² und 216 000 im Kanal; bei 1,5 V doppelt so viele.**

**Einordnung:** Unter jedem Quadratmikrometer liegen 26 000 Rümpfe der Verarmungszone; bei 1 V kommen im Modell 21 600 bewegliche Elektronen dazu, nach der vollständigen Lösung 16 000. Diese wenigen hunderttausend Elektronen machen aus dem Kanal einen Leiter von 1 kΩ (Abschnitt *Der ohmsche Bereich*).
::::

:::frage
„Woher kommen die Elektronen des Kanals überhaupt? Im p-Substrat gibt es doch nur 176 pro Kubikzentimeter.“
Im Transistor kommen sie aus Source und Drain. Die n⁺-Gebiete enthalten 10²⁰ Elektronen pro cm³, und sobald die Oberfläche invertiert ist, trennt sie keine Barriere mehr vom Kanal: Die 216 000 Elektronen bei 1 V stecken in 0,002 µm³ des Source-Gebiets und fließen beim Einschalten in Bruchteilen einer Nanosekunde nach. Ein MOS-Kondensator ohne Source und Drain muss sie dagegen durch Wärme erzeugen lassen, wie beim Sperrstrom einer Diode. Seine Verarmungszone liefert bei einer Lebensdauer der Ladungsträger von 1 µs rund 3,7·10⁻⁹ A/cm², und bis 3,45 fC/µm² beisammen sind, vergehen etwa 90 s. Diese Trägheit bestimmt seine Kapazität bei hoher Frequenz (Abschnitt *Die Kapazität des MOS-Kondensators*).
:::

## Die Kapazität des MOS-Kondensators

*Welche Kapazität misst man zwischen Gate und Bulk, und warum hängt sie in der Inversion von der Messfrequenz ab?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/01-cv-kurve · Vorlage: kennlinie
**Abbildung 8:** Kapazität des MOS-Kondensators, bezogen auf $C'_\mathrm{ox}$ = 6,91 fF/µm², über der Gate-Bulk-Spannung von −2,5 V bis 2,5 V; durchgezogen bei niedriger, gestrichelt bei hoher Messfrequenz. 0,96 bei −2,5 V, 0,73 im Flachband bei −1,03 V und 0,30 bei 0 V. Bei niedriger Frequenz erreicht die Kurve schon bei 0,35 V, in der schwachen Inversion, ihr Minimum von 0,26 und steigt dann wieder an, 0,40 bei 0,5 V, 0,92 bei 1 V und 0,98 bei 2,5 V; bei hoher Frequenz sinkt sie weiter, auf 0,25 an der Schwelle und 0,23 bei 2,5 V. Hilfslinien bei 1 und bei 0,247, dem Wert der Reihenschaltung aus Oxid und Verarmungszone an der Schwelle nach der Verarmungsnäherung; darüber kleine Ersatzschaltbilder der Zustände. In der Verarmung liegt die Kapazität der Zone in Reihe mit dem Oxid; in der Inversion kehrt die Kapazität nur dann auf $C'_\mathrm{ox}$ zurück, wenn die Elektronen der Messspannung folgen können.
:::

**Die Akteure:**

- __$C'$__: Kapazität pro Fläche, wie sie eine Messung mit kleiner Wechselspannung ergibt, also die Änderung der Gateladung pro Änderung der Gatespannung; in fF/µm².
- __$C'_\mathrm{dep}$__: Kapazität der Verarmungszone pro Fläche; 2,26 fF/µm² an der Schwelle, bei 45,8 nm Tiefe nach der Verarmungsnäherung.

**Das Zusammenspiel:** Liegt über $U_{GB}$ eine kleine Wechselspannung, pendelt die Gateladung, und im Silizium pendelt die Gegenladung mit; entscheidend ist, wo. In der Anreicherung pendeln die Löcher direkt an der Oberfläche, und man misst fast $C'_\mathrm{ox}$, bei −2,5 V das 0,96-Fache (Abbildung 8). In der Verarmung kommt und geht die Ladung am unteren Rand der Zone, $y_d$ tief im Silizium. Die Zone wirkt dann wie ein zweiter Kondensator in Reihe mit dem Oxid, und die Kapazität sinkt, bei 0 V auf 0,30 $C'_\mathrm{ox}$.

In der Inversion kommt es darauf an, ob die Elektronen dem Signal folgen können. Bei niedriger Frequenz tun sie es, und zwar schon in der schwachen Inversion: Ab 0,35 V steigt die Kapazität wieder und kehrt auf $C'_\mathrm{ox}$ zurück, 0,92 $C'_\mathrm{ox}$ bei 1 V. Bei hoher Frequenz bleibt ihre Zahl fest, denn ohne Source entstehen sie nur durch Wärme, in rund 90 s. Dann pendelt die Ladung am Rand der Verarmungszone, die oberhalb der Schwelle kaum noch wächst, und die Kapazität bleibt bei 0,23 bis 0,25 $C'_\mathrm{ox}$.

:::formel Formel
$$\frac{1}{C'} = \frac{1}{C'_\mathrm{ox}} + \frac{1}{C'_\mathrm{dep}}, \qquad C'_\mathrm{dep} = \frac{\varepsilon_\mathrm{Si}}{y_d}\,$$
:::

**So liest man das:** Die Formel gilt in der Verarmung und in der Inversion bei hoher Frequenz. Die Gesamtkapazität ist kleiner als jede der beiden; je tiefer die Zone, desto kleiner $C'_\mathrm{dep}$ und damit $C'$. An der Schwelle, nach der Verarmungsnäherung 45,8 nm tief, sind es 2,26 fF/µm² für die Zone und 1,70 fF/µm² insgesamt, das 0,247-Fache von $C'_\mathrm{ox}$.

**Kurz gesagt:** In der Verarmung addieren sich die Kehrwerte von Oxid- und Verarmungskapazität zum Kehrwert der Gesamtkapazität.

Idee der Herleitung: Eine kleine Spannungsänderung teilt sich auf Oxid und Silizium auf, und beide tragen dieselbe Ladungsänderung.

:::herleitung
**Ausgangspunkt:** die Aufteilung der Gate-Bulk-Spannung auf Oxid und Silizium (Herleitung der Schwellenspannung, Schritt 1), die Oxidkapazität und die Verarmungsladung aus dem Abschnitt *Verarmung*.

**Annahmen:**
(i) Verarmung, oder Inversion bei so hoher Frequenz, dass die Zahl der Elektronen fest bleibt;
(ii) Verarmungsnäherung;
(iii) kleine Änderungen, sodass man linear rechnen darf.

**Schritt 1**: Eine kleine Änderung der Gatespannung teilt sich auf beide Schichten auf:

$$\mathrm dU_{GB} = \mathrm dU_\mathrm{ox} + \mathrm d\psi_s$$

**Schritt 2**: Beide Schichten tragen dieselbe Ladungsänderung $\mathrm dQ'$, denn die Gateladung ändert sich um so viel wie die Ladung im Silizium:

$$\mathrm dU_\mathrm{ox} = \frac{\mathrm dQ'}{C'_\mathrm{ox}}, \qquad \mathrm d\psi_s = \frac{\mathrm dQ'}{C'_\mathrm{dep}}\,$$

Dabei ist $C'_\mathrm{dep}$ die Ableitung der Verarmungsladung nach dem Oberflächenpotential.

**Schritt 3**: Diese Ableitung, mit der Formel für $y_d$ umgeformt:

$$C'_\mathrm{dep} = \frac{\mathrm d}{\mathrm d\psi_s}\sqrt{2\,e\,\varepsilon_\mathrm{Si}\,N_A\,\psi_s} = \sqrt{\frac{e\,\varepsilon_\mathrm{Si}\,N_A}{2\,\psi_s}} = \frac{\varepsilon_\mathrm{Si}}{y_d}$$

**Schritt 4** (entscheidender Schritt): Schritt 2 in Schritt 1 eingesetzt und durch $\mathrm dQ'$ geteilt:

$$\frac{1}{C'} = \frac{\mathrm dU_{GB}}{\mathrm dQ'} = \frac{1}{C'_\mathrm{ox}} + \frac{1}{C'_\mathrm{dep}}$$

**Ergebnis:**

$$\frac{1}{C'} = \frac{1}{C'_\mathrm{ox}} + \frac{1}{C'_\mathrm{dep}}, \qquad C'_\mathrm{dep} = \frac{\varepsilon_\mathrm{Si}}{y_d}\,$$

**Woher die Faktoren kommen:** Die Reihenschaltung entsteht, weil beide Schichten dieselbe Ladungsänderung tragen; $\varepsilon_\mathrm{Si}/y_d$ ist ein Plattenkondensator mit dem Abstand zwischen Oberfläche und Rand der Zone.

**Proben:** Einheit F/cm². An der Schwelle ist $1/(1/6{,}906 + 1/2{,}26)$ fF/µm² = 1,70 fF/µm², also 0,247 $C'_\mathrm{ox}$; die vollständige Rechnung ergibt dort 0,249 und bei 2,5 V 0,234, weil die Zone oberhalb der Schwelle noch etwas tiefer wird. Grenzfall: Geht $y_d$ gegen null, geht $C'$ gegen $C'_\mathrm{ox}$.

**Grenzen:** Nahe dem Flachband ist die Zone nicht scharf begrenzt, weil die Löcher über einige Nanometer auf die Spannung reagieren; dort misst man 0,73 $C'_\mathrm{ox}$ statt $C'_\mathrm{ox}$.
:::

::::beispiel Kapazität des Beispieltransistors bei hoher Frequenz
**Gegeben:** $C'_\mathrm{ox}$ = 6,906 fF/µm², $\varepsilon_\mathrm{Si}$ = 1,036·10⁻¹² F/cm, Tiefe der Verarmungszone an der Schwelle nach der Verarmungsnäherung 45,8 nm, Gatefläche 10 µm².

**Gesucht:** die Kapazität bei hoher Frequenz an der Schwelle, pro Fläche und für den ganzen Transistor.

**Rechnung:** Kapazität der Zone:

$$C'_\mathrm{dep} = \frac{1{,}036\cdot10^{-12}\ \mathrm{F/cm}}{4{,}58\cdot10^{-6}\ \mathrm{cm}} = 2{,}26\cdot10^{-7}\ \mathrm{F/cm^2} = 2{,}26\ \mathrm{fF/\mu m^2}$$

Reihenschaltung mit dem Oxid und Fläche:

$$C' = \Big(\frac{1}{6{,}906} + \frac{1}{2{,}26}\Big)^{-1}\ \mathrm{fF/\mu m^2} = 1{,}70\ \mathrm{fF/\mu m^2}$$

$$C = 1{,}70\ \mathrm{fF/\mu m^2}\cdot10\ \mathrm{\mu m^2} = 17\ \mathrm{fF}$$

**Ergebnis:** **1,70 fF/µm², das 0,247-Fache von $C'_\mathrm{ox}$; 17 fF statt 69 fF für den ganzen Transistor.**

**Einordnung:** Die vollständige Rechnung ergibt an der Schwelle 0,249 und bis 2,5 V 0,234, weil die Zone noch um einige Nanometer wächst. Aus dem Höchstwert einer gemessenen Kurve folgt die Oxiddicke, aus dem Tiefstwert die Dotierung; deshalb überwachen Halbleiterhersteller ihre Prozesse mit solchen Messungen. Im Transistor liefern Source und Drain die Elektronen schnell genug, sodass die Gatekapazität in der Inversion auch bei hohen Frequenzen auf $C_\mathrm{ox}$ zurückkehrt.
::::

## Vom Kondensator zum Transistor: Sperrbereich und Kanal

*Was ändert sich, wenn neben dem Gate Source und Drain liegen und zwischen ihnen eine Spannung anliegt?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/01-betriebsbereiche · Vorlage: querschnitt-folge
**Abbildung 9:** Oben drei Querschnitte des Beispieltransistors, Source und Bulk an Masse. (a) Sperrbereich bei $U_{GS}$ = 0,3 V und $U_{DS}$ = 1 V: kein Kanal, nur Verarmungszonen um Source und Drain und unter dem Gate. (b) Ohmscher Bereich bei $U_{GS}$ = 1 V und $U_{DS}$ = 0,3 V: Der Kanal reicht von der Source bis zum Drain und wird zum Drain hin keilförmig dünner, am Drain-Ende auf 40 %. (c) Abschnürung bei $U_{GS}$ = 1 V und $U_{DS}$ = 2 V: Der Kanal endet kurz vor dem Drain, dahinter liegt eine 58 nm kurze verarmte Zone, durch die Elektronen zum Drain laufen. Unten die Ladung des Kanals längs des Weges von der Source zum Drain, bezogen auf ihren Wert an der Source, bei $U_{GS}$ = 1 V: Am Drain-Ende sind es 80 % bei $U_{DS}$ = 0,1 V, 40 % bei 0,3 V und null bei 0,5 V. Die Drainspannung hebt das Kanalpotential zum Drain hin an und verdünnt dort den Kanal; bei $U_{DS} = U_{GS} - U_{th}$ verschwindet er am Drain-Ende.
:::

Im Transistor liegen Source und Bulk zunächst beide an Masse. Dann ist $U_{GB} = U_{GS}$, und an der Source gilt alles, was der MOS-Kondensator gezeigt hat. Neu sind zwei Dinge: Die n⁺-Gebiete liefern die Elektronen für den Kanal, und eine Drain-Source-Spannung macht das Potential im Kanal ortsabhängig.

Ist $U_{GS}$ kleiner als die Schwelle, gibt es keinen Kanal (Abbildung 9a). Zwischen Source und Drain liegt p-Silizium, und jeder Weg eines Elektrons von der Source zum Drain führt über die Barriere des pn-Übergangs zwischen Source und Substrat, der wie eine Diode ohne Durchlassspannung sperrt. Es fließt nur ein sehr kleiner Strom: Bei $U_{GS}$ = 0 liegen an der Oberfläche 5,6·10¹¹ Elektronen pro cm³, eine Million Mal weniger als an der Schwelle, bei 0,25 V noch tausendmal weniger. Das ist der __Sperrbereich__; ein selbstsperrender Transistor ist bei $U_{GS}$ = 0 in diesem Zustand.

Ist $U_{GS}$ größer als die Schwelle, verbindet die Inversionsschicht Source und Drain. An der Oberfläche liegt nun durchgehend n-leitendes Silizium, die Barriere zur Source ist verschwunden, und der Kanal hat an der Source deren Potential und am Drain das des Drains.

**Die Akteure:**

- __$x$__: Ort längs des Kanals, von 0 an der Source bis $L$ am Drain.
- __$U(x)$__: __Kanalpotential__, das Potential des Kanals an der Stelle $x$ gegenüber der Source; 0 an der Source, $U_{DS}$ am Drain.
- __$Q'_n(x)$__: Elektronenladung pro Fläche an der Stelle $x$; an der Source 3,45 fC/µm² bei $U_{GS}$ = 1 V.

**Das Zusammenspiel:** Das Gate wirkt senkrecht zur Oberfläche, die Drainspannung längs des Kanals. Beide treffen sich im Kanalpotential: Die Drainspannung hebt $U(x)$ zum Drain hin an, und um genau diesen Betrag sinkt dort die Spannung zwischen Gate und Kanal, die die Elektronen bindet. Jedes kurze Stück des Kanals verhält sich wie ein MOS-Kondensator mit seiner eigenen Gate-Kanal-Spannung und führt umso weniger Elektronen, je näher es am Drain liegt. Der Kanal wird zum Drain hin dünner, er ist keilförmig (Abbildung 9b und 9 unten).

:::formel Formel
$$Q'_n(x) = -C'_\mathrm{ox}\,\big(U_{GS} - U_{th} - U(x)\big)$$
:::

**So liest man das:** Eingaben sind die Gate-Source-Spannung und das Kanalpotential an der Stelle $x$, Ausgabe ist die Elektronenladung dort. An der Source ist $U$ = 0, und die Ladung ist die des MOS-Kondensators; zum Drain hin nimmt sie ab, bis auf $C'_\mathrm{ox}(U_{GS} - U_{th} - U_{DS})$ am Drain-Ende. Ohne Drainspannung ist der Kanal überall gleich dick.

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

::::beispiel Ladung längs des Kanals bei 1 V Gatespannung
**Gegeben:** $C'_\mathrm{ox}$ = 6,906 fF/µm², $U_{th}$ = 0,5 V, $U_{GS}$ = 1 V; Drain-Source-Spannungen 0,1 V, 0,3 V und 0,5 V.

**Gesucht:** die Elektronenladung an Source und Drain-Ende.

**Rechnung:** An der Source ist $U$ = 0:

$$|Q'_n(0)| = 6{,}906\ \mathrm{fF/\mu m^2}\cdot0{,}5\ \mathrm V = 3{,}45\ \mathrm{fC/\mu m^2}$$

Am Drain-Ende ist $U = U_{DS}$:

$$|Q'_n(L)| = 6{,}906\ \mathrm{fF/\mu m^2}\cdot\big(0{,}5\ \mathrm V - U_{DS}\big) = 2{,}76;\ 1{,}38;\ 0\ \mathrm{fC/\mu m^2}$$

**Ergebnis:** **Am Drain-Ende bleiben 80 %, 40 % und 0 % der Ladung an der Source.**

**Einordnung:** Mit jedem Zehntel Volt Drainspannung verliert das Drain-Ende ein Fünftel der Ladung, die die Übersteuerung von 0,5 V an der Source bindet. Bei 0,5 V ist dort nichts mehr übrig. Den Verlauf dazwischen zeigt Abbildung 9 unten; er folgt aus der Bedingung, dass durch jeden Querschnitt des Kanals derselbe Strom fließt.
::::

## Der ohmsche Bereich

*Wie verhält sich der Transistor, solange die Drain-Source-Spannung klein ist?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/01-kanalwiderstand · Vorlage: kennlinie
**Abbildung 10:** (a) Drainstrom über der Drain-Source-Spannung von 0 bis 20 mV für $U_{GS}$ = 0,75 V, 1 V, 1,5 V und 2,5 V: nahezu Geraden durch den Ursprung mit den Steigungen 0,5 mS, 1 mS, 2 mS und 4 mS, bei 20 mV also 10 µA, 20 µA, 40 µA und 80 µA; bei $U_{GS}$ unter 0,5 V die Nulllinie. (b) Kanalwiderstand über $U_{GS}$ von 0,6 V bis 2,5 V, eine Hyperbel mit 2 kΩ bei 0,75 V, 1 kΩ bei 1 V, 500 Ω bei 1,5 V und 250 Ω bei 2,5 V. Für kleine Drain-Source-Spannungen ist der Kanal ein Widerstand, dessen Leitwert proportional zur Gate-Übersteuerung wächst.
:::

**Die Akteure:**

- __$\mu_n$__: Beweglichkeit der Elektronen im Kanal, ihre Driftgeschwindigkeit pro Feldstärke; 290 cm²/(V s).
- __$K'_n$__, __$K_n$__: Prozessparameter und Steilheitskoeffizient, wie unten definiert; 200 µA/V² und 2 mA/V².
- __$R_\mathrm{on}$__: Widerstand des Kanals zwischen Source und Drain bei kleiner Drain-Source-Spannung; 1 kΩ bei $U_{GS}$ = 1 V.

**Das Zusammenspiel:** Ist $U_{DS}$ klein gegen die Gate-Übersteuerung, ändert sich das Kanalpotential kaum, und der Kanal ist überall fast so dick wie an der Source. Er ist dann eine dünne leitende Schicht, durch die die Elektronen im Feld $U_{DS}/L$ driften: ein Widerstand. Ihre Beweglichkeit ist dort mit 290 cm²/(V s) kleiner als die 1400 cm²/(V s) in reinem Silizium, weil sie an den Dotieratomen und an der Grenzfläche zum Oxid gestreut werden. Der Leitwert der Schicht ist proportional zur Elektronenladung pro Fläche und damit zur Gate-Übersteuerung; der Transistor ist ein Widerstand, dessen Wert die Gatespannung einstellt (Abbildung 10). Weil der Strom dabei proportional zu $U_{DS}$ wächst, heißt der ganze Bereich mit durchgehendem Kanal, $0 < U_{DS} < U_{GS} - U_{th}$, __ohmscher Bereich__, auch linearer Bereich oder Triodenbereich.

Alle Größen, die Fertigung und Entwurf beitragen, fasst man zusammen:

:::formel Definition
$$K_n = K'_n\,\frac{W}{L}, \qquad K'_n = \mu_n\,C'_\mathrm{ox}\,$$
:::

Der __Prozessparameter__ $K'_n$ ist durch die Fertigung festgelegt, das Verhältnis $W/L$ wählt der Schaltungsentwurf; ihr Produkt, der __Steilheitskoeffizient__ $K_n$, kennzeichnet einen bestimmten Transistor. Beim Beispiel-NMOS sind es 200 µA/V² und, mit $W/L$ = 10, 2 mA/V².

:::formel Formel
$$R_\mathrm{on} = \frac{L}{W\,\mu_n\,|Q'_n|} = \frac{1}{K_n\,\big(U_{GS} - U_{th}\big)}\,$$
:::

**So liest man das:** Die Formel gilt für $U_{DS}$ klein gegen $U_{GS} - U_{th}$. Bei 1 V Gatespannung hat der Beispieltransistor 1 kΩ; der Widerstand halbiert sich, wenn sich die Übersteuerung verdoppelt, und wächst unbegrenzt, wenn sich $U_{GS}$ der Schwelle nähert. Der erste Ausdruck zeigt die Bauform: Schichtwiderstand des Kanals, $1/(\mu_n |Q'_n|)$, mal der Zahl $L/W$ der Quadrate hintereinander.

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
**Gegeben:** $\mu_n$ = 290 cm²/(V s), $C'_\mathrm{ox}$ = 6,906·10⁻⁷ F/cm², $W$ = 10 µm, $L$ = 1 µm, also $K_n$ = 2 mA/V², $U_{th}$ = 0,5 V; Gate-Source-Spannungen 0,75 V, 1 V, 1,5 V und 2,5 V.

**Gesucht:** Schichtwiderstand des Kanals und Kanalwiderstand.

**Rechnung:** Bei 1 V ist die Ladung 3,45·10⁻⁷ C/cm², der Schichtwiderstand

$$R_\square = \frac{1}{\mu_n\,|Q'_n|} = \frac{1}{290\ \mathrm{cm^2/(V\,s)}\cdot3{,}45\cdot10^{-7}\ \mathrm{C/cm^2}} = 10{,}0\ \mathrm{k\Omega}$$

Der Kanal ist 0,1 Quadrate lang ($L/W$):

$$R_\mathrm{on} = 10{,}0\ \mathrm{k\Omega}\cdot0{,}1 = 1{,}00\ \mathrm{k\Omega}$$

Mit der zweiten Form für die übrigen Spannungen:

$$R_\mathrm{on} = \frac{1}{2\ \mathrm{mA/V^2}\cdot\big(U_{GS} - 0{,}5\ \mathrm V\big)} = 2000;\ 1000;\ 500;\ 250\ \Omega$$

**Ergebnis:** **Schichtwiderstand 10 kΩ/□ bei 1 V; Kanalwiderstand 2 kΩ, 1 kΩ, 500 Ω und 250 Ω.**

**Einordnung:** Der Kanal hat bei 1 V einen Schichtwiderstand von 10 kΩ/□, rund fünfzigmal so viel wie Polysilizium ohne Silizid; erst die Weite von zehn Mikrometern auf einem Mikrometer Länge macht daraus 1 kΩ. Als Schalter in einer Schaltung mit 2,5 V hat der Transistor 250 Ω; mit einer Last von 1 pF ergibt das 250 ps als Größenordnung der Umladezeit. Tatsächlich dauert das Umladen länger, weil der Transistor anfangs, solange die Drainspannung über der Abschnürgrenze liegt, nur einen begrenzten Strom liefert (Abschnitt *Abschnürung*). Unterhalb der Schwelle sperrt er.
::::

## Abschnürung

*Was geschieht am Drain-Ende, wenn die Drain-Source-Spannung die Gate-Übersteuerung erreicht, und warum fließt der Strom trotzdem weiter?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/01-abschnuerung · Vorlage: querschnitt-detail
**Abbildung 11:** Das Drain-Ende des Beispieltransistors bei $U_{GS}$ = 1 V und $U_{DS}$ = 2 V. (a) Vergrößerter Querschnitt: Die Elektronenschicht wird zum Abschnürpunkt hin dünn und endet 58 nm vor dem Drain; dazwischen liegt eine verarmte Zone mit einem Feld vom Drain zum Kanalende, durch das die Elektronen zum Drain laufen. (b) Potential längs des Weges von der Source zum Drain: im Kanal von 0 auf 0,5 V am Abschnürpunkt, dann auf 58 nm steil auf 2 V; gestrichelt der Verlauf an der Abschnürgrenze, $U_{DS}$ = 0,5 V. Was über $U_{GS} - U_{th}$ hinausgeht, fällt über der kurzen Zone ab; der Kanal selbst sieht weiter nur 0,5 V, und das starke Feld der Zone zieht jedes ankommende Elektron zum Drain.
:::

**Die Akteure:**

- __$U_{GD}$__: Spannung zwischen Gate und Drain, nach der Maschenregel $U_{GS} - U_{DS}$; 0,5 V an der Abschnürgrenze bei $U_{GS}$ = 1 V.
- __$U_{DS,\mathrm{ab}}$__: __Abschnürspannung__, die Drain-Source-Spannung, bei der der Kanal am Drain-Ende verschwindet; 0,5 V bei $U_{GS}$ = 1 V. Üblich ist auch die Bezeichnung $U_{DS,\mathrm{sat}}$.

**Das Zusammenspiel:**

**Schritt 1**: Am Drain-Ende ist das Kanalpotential $U_{DS}$; die Spannung zwischen Gate und Kanal ist dort $U_{GS} - U_{DS}$, also $U_{GD}$.

**Schritt 2**: Solange $U_{GD}$ über der Schwelle liegt, gibt es auch am Drain Elektronen; der Kanal reicht durchgehend von der Source zum Drain und wird nur zum Drain hin dünner. Bei $U_{GS}$ = 1 V und $U_{DS}$ = 0,3 V liegen dort noch 40 % der Ladung an der Source (Abbildung 9b).

**Schritt 3**: Erreicht $U_{DS}$ die Gate-Übersteuerung, beim Beispiel 0,5 V, sinkt $U_{GD}$ auf die Schwelle, und die Ladung am Drain-Ende wird null. Der Kanal ist dort __abgeschnürt__ (englisch pinch-off).

**Schritt 4** (entscheidender Schritt): Steigt $U_{DS}$ weiter, rückt das Kanalende ein kleines Stück zur Source. Am Kanalende, dem Abschnürpunkt, ist die örtliche Ladung null; dort hat der Kanal also genau das Potential $U_{GS} - U_{th}$. Der Kanal von der Source bis dorthin sieht deshalb unabhängig von $U_{DS}$ dieselbe Spannung und hat dieselbe Ladungsverteilung wie an der Abschnürgrenze, und er führt in erster Näherung denselben Strom (Abbildung 11b).

**Schritt 5**: Was $U_{DS}$ über $U_{GS} - U_{th}$ hinausgeht, fällt über der kurzen verarmten Zone zwischen Kanalende und Drain ab: bei $U_{DS}$ = 2 V sind es 1,5 V über rund 58 nm, im Mittel 2,6·10⁵ V/cm (Abbildung 11a). Jedes Elektron, das das Kanalende erreicht, zieht dieses Feld zum Drain, so wie ein Minoritätsträger, der den Rand einer gesperrten Raumladungszone erreicht, hinübergezogen wird ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie-ausfuehrlich.html)).

**Schritt 6**: Weil die Zone mit $U_{DS}$ wächst, wird der wirksame Kanal etwas kürzer, bei 2 V um 5,8 %, und der Strom steigt leicht an. Diese __Kanallängenmodulation__ ist der Grund, warum der Strom oberhalb der Abschnürgrenze nicht ganz konstant bleibt.

Weil der Strom oberhalb der Grenze kaum noch von $U_{DS}$ abhängt, wirkt der Transistor dort als Stromquelle, die die Gatespannung steuert. Den Bereich nennt man __Abschnürbereich__, nach dem Ausbleiben eines weiteren Stromanstiegs auch Sättigungsbereich.

:::formel Formel
$$U_{DS,\mathrm{ab}} = U_{GS} - U_{th}$$
:::

**So liest man das:** Eingabe ist die Gate-Source-Spannung, Ausgabe die Drain-Source-Spannung an der Grenze zwischen ohmschem Bereich und Abschnürbereich. Sie wächst Volt für Volt mit $U_{GS}$: 0,25 V, 0,5 V, 1 V und 2 V bei 0,75 V, 1 V, 1,5 V und 2,5 V Gatespannung. An der Schwelle selbst ist sie null.

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

::::beispiel Abschnürgrenzen des Beispieltransistors
**Gegeben:** $U_{th}$ = 0,5 V; Gate-Source-Spannungen 0,75 V, 1 V, 1,5 V und 2,5 V.

**Gesucht:** die Abschnürspannung und die Gate-Drain-Spannung an der Grenze.

**Rechnung:** Abschnürspannung als Gate-Übersteuerung:

$$U_{DS,\mathrm{ab}} = U_{GS} - 0{,}5\ \mathrm V = 0{,}25;\ 0{,}5;\ 1{,}0;\ 2{,}0\ \mathrm V$$

Gate-Drain-Spannung an der Grenze:

$$U_{GD} = U_{GS} - U_{DS,\mathrm{ab}} = 0{,}5\ \mathrm V$$

**Ergebnis:** **0,25 V, 0,5 V, 1,0 V und 2,0 V; an der Grenze liegt zwischen Gate und Drain immer die Schwellenspannung, 0,5 V.**

**Einordnung:** Wer den Transistor als Stromquelle oder Verstärker nutzt, muss $U_{DS}$ über dieser Grenze halten: Bei 1 V Gatespannung genügen 0,5 V, bei 2,5 V sind 2 V nötig. Als Schalter dagegen betreibt man ihn weit darunter, mit großer Gatespannung und kleiner Drain-Source-Spannung.
::::

| Bereich | Bedingung, Kanal und Verhalten |
|---|---|
| Sperrbereich | $U_{GS} < U_{th}$: kein Kanal, nur ein sehr kleiner Strom |
| ohmscher Bereich (Triodenbereich) | $U_{GS} > U_{th}$ und $U_{DS} < U_{GS} - U_{th}$: durchgehender Kanal, zum Drain hin dünner; bei kleinem $U_{DS}$ ein Widerstand $R_\mathrm{on}$ |
| Abschnürbereich (Sättigungsbereich) | $U_{GS} > U_{th}$ und $U_{DS} > U_{GS} - U_{th}$: Kanal vor dem Drain abgeschnürt; Strom fast unabhängig von $U_{DS}$, der Transistor wirkt als Stromquelle |

:::fehlvorstellung
„Ist der Kanal abgeschnürt, fließt kein Strom mehr; er ist doch unterbrochen.“ Das liegt nahe, weil Abschnüren nach dem Zudrücken eines Schlauchs klingt. Tatsächlich fließt der Strom weiter und bleibt etwa so groß wie an der Abschnürgrenze. Nur der letzte, kurze Abschnitt vor dem Drain enthält keine Inversionsschicht, und dort sorgt ein starkes Feld dafür, dass jedes ankommende Elektron weiterkommt: Bei $U_{GS}$ = 1 V und $U_{DS}$ = 2 V liegen 1,5 V über 58 nm, und die Elektronen durchqueren die Zone in 0,6 ps (Abschnitt *Abschnürung*). Wenige, schnelle Elektronen tragen dort denselben Strom wie viele langsame im Kanal.
:::

::::beispiel Die abgeschnürte Zone bei 2 V Drain-Source-Spannung
**Gegeben:** $U_{GS}$ = 1 V, $U_{th}$ = 0,5 V, $U_{DS}$ = 2 V; $N_A$ = 5,68·10¹⁷ cm⁻³, also $e N_A$ = 9,10·10⁻² C/cm³; $\varepsilon_\mathrm{Si}$ = 1,036·10⁻¹² F/cm; Höchstgeschwindigkeit der Elektronen in Silizium rund 10⁷ cm/s.

**Gesucht:** Spannung über der Zone, ihre Länge als Abschätzung, mittleres Feld, Laufzeit der Elektronen und Verkürzung des Kanals.

**Rechnung:** Über der Zone liegt der Überschuss über die Abschnürspannung:

$$\Delta U = U_{DS} - (U_{GS} - U_{th}) = 2\ \mathrm V - 0{,}5\ \mathrm V = 1{,}5\ \mathrm V$$

Die Länge schätzt man mit der Formel für eine einseitige Verarmungszone (Abschnitt *Verarmung*), angewandt auf die Strecke vor dem Drain:

$$\Delta L^2 \approx \frac{2\,\varepsilon_\mathrm{Si}\,\Delta U}{e\,N_A} = \frac{2\cdot1{,}036\cdot10^{-12}\ \mathrm{F/cm}\cdot1{,}5\ \mathrm V}{9{,}10\cdot10^{-2}\ \mathrm{C/cm^3}} = 3{,}41\cdot10^{-11}\ \mathrm{cm^2}$$

Daraus Länge, Feld und Laufzeit:

$$\Delta L \approx 5{,}84\cdot10^{-6}\ \mathrm{cm} = 58{,}4\ \mathrm{nm}$$

$$E \approx \frac{1{,}5\ \mathrm V}{5{,}84\cdot10^{-6}\ \mathrm{cm}} = 2{,}6\cdot10^{5}\ \mathrm{V/cm}, \qquad t \approx \frac{5{,}84\cdot10^{-6}\ \mathrm{cm}}{10^{7}\ \mathrm{cm/s}} = 0{,}58\ \mathrm{ps}\,$$

**Ergebnis:** **1,5 V über rund 58 nm, im Mittel 2,6·10⁵ V/cm; die Elektronen brauchen 0,6 ps hindurch, und der Kanal wird um 5,8 % kürzer.**

**Einordnung:** Die Abschätzung behandelt die Zone eindimensional; das wirkliche Feld verteilt sich zweidimensional zwischen Drain, Gate und Substrat. Die Größenordnung genügt aber: Die Zone ist kein Hindernis, sondern eine Strecke mit starkem Feld. Bei 2,5 V wächst sie auf 68 nm, 6,7 % der Kanallänge; um so viel kürzer wird der leitende Kanal, und entsprechend steigt der Strom leicht mit $U_{DS}$.
::::

:::fehlvorstellung
„Der Abschnürbereich ist dasselbe wie die Sättigung des Bipolartransistors.“ Das liegt nahe, weil der Abschnürbereich oft Sättigungsbereich heißt. Beim MOSFET meint das Wort aber, dass der Strom nicht weiter mit $U_{DS}$ wächst: Der Transistor wirkt als Stromquelle. Beim [Bipolartransistor](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise-ausfuehrlich.html) heißt Sättigung der Zustand, in dem beide pn-Übergänge leiten und die Kollektor-Emitter-Spannung nur noch etwa 0,1 bis 0,2 V beträgt; das entspricht dem ohmschen Bereich des MOSFET. Dem Abschnürbereich entspricht beim Bipolartransistor der aktive Bereich, in dem er als Verstärker arbeitet.
:::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Gate, Oxid und Substrat | die Platten und der Isolator des Kondensators |
| Anreicherung, Verarmung, Inversion | woraus die Gegenladung im Silizium gerade besteht |
| Flachbandspannung | die Spannung, bei der der Kondensator ungeladen ist; die Kontaktspannung der Materialien verschiebt sie |
| Schwellenspannung | die Spannung, ab der zusätzliche Gegenladung aus beweglichen Elektronen besteht |
| Inversionsladung | die Ladung, die die Spannung über der Schwelle pro Fläche bindet |
| keilförmiger Kanal und Abschnürung | jedes Stück des Kanals ist ein Kondensator mit seiner eigenen Gate-Kanal-Spannung; am Drain sinkt sie auf die Schwelle |
| Bulk-Anschluss, PMOS | die untere Platte muss gegen Source und Drain isoliert bleiben; beim PMOS sind alle Vorzeichen gespiegelt |

Gate, Oxid und Halbleiter bilden einen Kondensator: Die Spannung zwischen Gate und Halbleiter legt fest, wie viel Gegenladung unter dem Oxid sitzt, und oberhalb der Schwellenspannung kommt jede weitere Gegenladung als Schicht beweglicher Elektronen hinzu, die Source und Drain als Kanal verbinden; an jeder Stelle des Kanals bestimmt die örtliche Spannung zwischen Gate und Kanal, wie viel Ladung dort den Strom tragen kann.

## Bedeutung und Ausblick

In einem CMOS-Logikgatter wechseln die Transistoren zwischen Sperrbereich und ohmschem Bereich: Aus ist der Transistor ein offener Schalter, ein ist er ein Widerstand von einigen hundert Ohm, und im Ruhezustand fließt kein Strom. Verstärker und Stromquellen betreiben ihn im Abschnürbereich, wo der Strom kaum von der Drainspannung abhängt. Gemessen werden die Größen dieses Artikels an Teststrukturen auf jedem Wafer: Oxiddicke und Dotierung aus der Kapazitätskurve, die Schwellenspannung aus dem Strom bei kleiner Drain-Source-Spannung.

Wie groß der Drainstrom im ohmschen und im Abschnürbereich ist und wie stark die Kanallängenmodulation ihn mit $U_{DS}$ ansteigen lässt, leitet der nächste Artikel her, „Kennlinien des NMOS-Transistors“. Die MOS-Diode im Artikel über [Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung-ausfuehrlich.html) ist genau dieser Beispieltransistor mit verbundenem Gate und Drain. Weitere Artikel behandeln den PMOS mit seinen Gleichungen, den Einfluss einer Spannung zwischen Bulk und Source, die Kapazitäten des Transistors und sein Kleinsignalmodell. Aus Sicht der Bauelementphysik behandeln [Die MOS-Kapazität](/wissen/elektrotechnik/4-semester/grundlagen-elektronischer-materialien-und-bauelemente/bauelemente/mos-kapazitaet.html) und [Der MOSFET](/wissen/elektrotechnik/4-semester/grundlagen-elektronischer-materialien-und-bauelemente/bauelemente/mosfet.html) dasselbe Bauelement.

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
A: Die Elektronendichte an der Oberfläche wächst je 60 mV Oberflächenpotential um das Zehnfache; schon eine kleine Zunahme bringt so viele Elektronen, dass sie die ganze zusätzliche Gateladung aufnehmen. Von 0,5 V auf 1 V Gatespannung steigt das Oberflächenpotential nur um 0,105 V, die Verarmungszone wächst von 45 auf 48 nm.
F: Warum legt man die Schwelle bei einem Oberflächenpotential von $2\Phi_F$ fest?
A: Dort erreicht die Elektronendichte an der Oberfläche die Dotierung, die Oberfläche ist so stark n-leitend wie das Innere p-leitend. Ab hier wächst die Elektronenladung schneller als die der Rümpfe, und zusätzliche Gateladung erscheint fast nur noch als Kanal; zwischen $\Phi_F$ und $2\Phi_F$ sind die Elektronen zu selten, um zu zählen.
F: Warum wird der Kanal bei anliegender Drain-Source-Spannung zum Drain hin dünner?
A: Die Drainspannung hebt das Kanalpotential zum Drain hin an. Die Spannung zwischen Gate und Kanal, die die Elektronen bindet, ist $U_{GS} - U(x)$ und sinkt deshalb zum Drain hin; mit ihr sinkt die örtliche Elektronenladung.
F: Warum fließt der Strom nach der Abschnürung weiter und bleibt etwa gleich groß?
A: Am Kanalende hat der Kanal immer das Potential $U_{GS} - U_{th}$; der leitende Teil sieht deshalb dieselbe Spannung wie an der Abschnürgrenze und führt denselben Strom. Der Rest der Drainspannung fällt über einer kurzen Zone ab, deren starkes Feld jedes ankommende Elektron zum Drain zieht.
F: Stimmt es, dass beim MOS-Kondensator ohne Gatespannung die Bänder flach sind?
A: Nein. Gate aus n⁺-Polysilizium und p-Substrat haben eine Kontaktspannung von 1,03 V; schon bei $U_{GB}$ = 0 ist die Oberfläche 35 nm tief verarmt und liegt 0,57 V über dem Inneren. Flach sind die Bänder erst bei −1,03 V.
F: Stimmt es, dass die Verarmungszone unter dem Gate durch Rekombination von Löchern und Elektronen entsteht?
A: Nein. Unter dem Gate gibt es kaum Elektronen; das Feld des positiv geladenen Gates schiebt die Löcher in die Tiefe, und zurück bleiben die festen, negativ geladenen Akzeptorrümpfe.
F: Stimmt es, dass der Abschnürbereich des MOSFET der Sättigung des Bipolartransistors entspricht?
A: Nein. Im Abschnürbereich wirkt der MOSFET als Stromquelle; das entspricht dem aktiven Bereich des Bipolartransistors. Dessen Sättigung, beide Übergänge leitend und kleine Kollektor-Emitter-Spannung, entspricht dem ohmschen Bereich.
F: Wie groß ist die Schwellenspannung des Beispieltransistors, und woraus setzt sie sich zusammen?
A: 0,500 V: −1,027 V Flachbandspannung, die die Kontaktspannung des Gates aufhebt, +0,923 V Oberflächenpotential bis zur starken Inversion und +0,604 V Oxidspannung für die Verarmungsladung von 4,17 fC/µm².
F: Welchen Kanalwiderstand hat der Beispieltransistor bei $U_{GS}$ = 1,5 V und kleiner Drain-Source-Spannung?
A: $1/(K_n(U_{GS} - U_{th})) = 1/(2\ \mathrm{mA/V^2}\cdot1\ \mathrm V)$ = 500 Ω, halb so viel wie bei 1 V, weil sich die Gate-Übersteuerung verdoppelt.
F: Warum muss der Bulk eines NMOS an der negativsten Spannung der Schaltung liegen?
A: Source und Drain bilden mit dem p-Substrat Dioden mit der Anode im Substrat. Nur wenn das Substrat am tiefsten liegt, bleiben alle diese Dioden gesperrt und die Transistoren voneinander isoliert; sonst flösse ab etwa 0,6 V ein Strom ins Substrat.
:::
