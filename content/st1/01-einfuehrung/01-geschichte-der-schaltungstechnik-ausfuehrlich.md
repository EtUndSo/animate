---
title: Von der Röhre zum integrierten Schaltkreis
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / Einführung
order: 33010100
summary: Wie aus der Elektronenröhre über den Transistor die integrierte Schaltung wurde und warum jeder Schritt nötig war, vom gesteuerten Ventil als Grundprinzip jedes Verstärkers über Rückkopplung, Überlagerungsempfänger, Silizium und Planartechnik bis zu CMOS, dem Mooreschen Gesetz und ganzen Funksystemen auf einem Chip. Ausführliche Fassung: hergeleitet werden Verstärkung einer Röhrenstufe, Barkhausen-Formel, Rückkopplungsformel, Mischprodukte und Spiegelfrequenz, Umladeleistung, Verdopplungszeit und die Skalierungsregeln.
tags: Elektronenröhre, Transistor, integrierte Schaltung, Mooresches Gesetz, CMOS
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Ein UKW-Signal kommt oft nur mit wenigen Mikrovolt an der Antenne an, und ein Prozessor schaltet milliardenmal je Sekunde Millionen von Leitungen um. Beides verlangt ein Bauelement, in dem eine kleine Steuergröße einen großen Strom aus einer Versorgung steuert. Das Thema folgt aus einem Prinzip:

**Jede elektronische Schaltung beruht auf einem gesteuerten Ventil, in dem eine kleine Steuergröße einen großen Strom aus einer Versorgung steuert; die Geschichte der Schaltungstechnik ist die Geschichte, dieses Ventil kleiner, sparsamer und schneller zu machen, bis Milliarden davon gemeinsam auf einem Siliziumchip entstehen und jedes einzelne fast nichts mehr kostet.**

Vorausgesetzt werden Schulphysik (Strom, Spannung, Leistung, elektrisches Feld) und Schulmathematik (Potenzen, Logarithmus, Additionstheoreme). Halbleiter, Diode, Bipolartransistor und Operationsverstärker haben eigene Artikel, die an den passenden Stellen verlinkt sind; was hier davon gebraucht wird, steht im Text. Auf diesem Thema bauen alle weiteren Themen der Schaltungstechnik auf, vom Arbeitspunkt über das Kleinsignalmodell bis zu den Transistorgrundschaltungen.

:::grafik
Szene: st1/einfuehrung/01-drei-ventile · Vorlage: schaltbild-vergleich
**Abbildung 1:** Drei Generationen des gesteuerten Ventils über einer Zeitachse von 1906 bis 2010. Links die Triode (ab 1906/1910) mit geheizter Kathode, Gitter und Anode, in der Mitte der Bipolartransistor (ab 1947/48) mit Basis, Kollektor und Emitter, rechts der MOS-Feldeffekttransistor (ab 1959/60) mit Gate, Drain und Source. Jedes Ventil liegt mit einem Arbeitswiderstand an der Versorgungsspannung; die Steuergröße (Gitter-, Basis-Emitter- bzw. Gate-Source-Spannung) ist blau, der gesteuerte Strom orange markiert. Unter jedem Ventil die Steuerart (Feld ohne Gleichstrom, Spannung mit kleinem Basisstrom, Feld ohne Gleichstrom) und die typische Größe (Glaskolben einige Zentimeter, Gehäuse einige Millimeter, Technologieknoten 65 nm mit rund 35 nm Gatelänge im Jahr 2006). In allen drei Generationen steuert eine kleine Größe am Steueranschluss einen großen Strom aus der Versorgung; geändert haben sich Größe, Leistungsbedarf und Herstellung.
:::

## Das gesteuerte Ventil: die Elektronenröhre

*Wie kann eine kleine Spannung einen großen Strom steuern, und woher kommt die Leistung des verstärkten Signals?*

Um 1906 fehlte der Nachrichtentechnik ein Verstärker: Ferngespräche wurden mit jedem Kilometer Leitung leiser, und Funkempfänger konnten das Antennensignal nur gleichrichten. Robert von Lieben meldete 1906 eine Röhre zum Patent an, deren Elektronenstrahl ein Magnetfeld ablenkte; sie brauchte zu viel Steuerleistung. 1910 ersetzten er, Eugen Reisz und Siegmund Strauß das Magnetfeld durch ein Gitter zwischen Kathode und Anode. Unabhängig davon hatte Lee de Forest 1906/07 das Audion gebaut, ebenfalls mit drei Elektroden, das im Empfänger das Hochfrequenzsignal gleichrichtete und zugleich verstärkte; ab 1912 diente es auch als Niederfrequenzverstärker. Eine Röhre mit drei Elektroden heißt __Triode__.

Beide enthielten noch Gas, die Liebenröhre Quecksilberdampf, und reagierten deshalb empfindlich auf Druck und Temperatur. Stabil und in Serie herstellbar wurde erst die __Hochvakuumröhre__, in der nur Elektronen den Strom tragen; Irving Langmuir (General Electric, 1913) und Walter Schottky (damals an der Universität Jena) klärten unabhängig voneinander die Rolle der Raumladung. Bei Siemens & Halske lief 1916 die Serienfertigung von Verstärkerröhren für Fernsprechverstärker an, und Schottky meldete im selben Jahr die Schirmgitterröhre mit einem zusätzlichen Gitter an.

:::grafik
Szene: st1/einfuehrung/01-triode-aufbau · Vorlage: querschnitt
**Abbildung 2:** Schnitt durch eine Triode, schematisch und nicht maßstäblich. Links die vom Heizfaden auf rund 1000 K erwärmte Kathode, davor eine Wolke ausgetretener Elektronen (Raumladung, blau), dicht davor das Gitter aus dünnen Drähten, rechts die Anode. Darunter der Potentialverlauf von der Kathode zur Anode bei 250 V Anodenspannung für die Gitterspannungen −2 V und −1 V: Vor der Kathode liegt ein flaches Potentialminimum, das die Elektronenwolke selbst erzeugt und das nur Elektronen mit genügend Austrittsenergie überwinden; die weniger negative Gitterspannung hebt das Potential vor der Kathode an und lässt mehr Elektronen zur Anode. Das Gitter steuert das Potential vor der Kathode und damit den Anodenstrom; weil es negativ ist, landet praktisch kein Elektron auf ihm.
:::

Als Zahlenbeispiel dient ein System der Doppeltriode ECC83 (amerikanisch 12AX7), die zwei gleiche Triodensysteme in einem Kolben enthält und bis heute in Gitarrenverstärkern steckt. Alle Werte gelten im __Arbeitspunkt__, dem Betriebszustand ohne Signal, um den herum das Signal die Spannungen ändert.

**Die Akteure:**

- __Kathode__: Metallröhrchen mit Oxidschicht, von einem Heizfaden auf rund 1000 K (gut 700 °C) erwärmt, so dass Elektronen austreten (__Glühemission__); Bezugspunkt aller Spannungen.
- __$U_g$__: Gitterspannung, die Spannung des Gitters gegen die Kathode; in V; −2 V im Arbeitspunkt. Sie steuert.
- __$U_a$__: Anodenspannung, die Spannung der Anode gegen die Kathode; in V; 250 V. Die Anode fängt die Elektronen auf, ihre Spannungsquelle liefert die Energie.
- __$I_a$__: Anodenstrom; in mA; 1,2 mA. Er fließt in technischer Stromrichtung von der Anode durch die Röhre zur Kathode, die Elektronen fliegen in Gegenrichtung von der Kathode zur Anode. Er ist der gesteuerte Strom.

**Das Zusammenspiel:**

**Schritt 1**: Die geheizte Kathode gibt laufend Elektronen ab. Jedes ausgetretene Elektron trägt negative Ladung, und die Wolke vor der Kathode stößt nachfolgende Elektronen zurück; ohne Anodenspannung fallen so viele zurück, wie austreten.

**Schritt 2**: Eine positive Anode zieht Elektronen aus der Wolke ab. Die Kathode könnte weit mehr Elektronen liefern, als tatsächlich fließen; begrenzt wird der Strom durch die Wolke selbst, die __Raumladung__. Je höher die Elektroden das Potential vor der Kathode anheben, desto mehr Elektronen werden der Wolke entzogen, bevor ihre Abstoßung den Nachschub bremst. Wer das Potential vor der Kathode bestimmt, bestimmt den Strom.

**Schritt 3**: Das Gitter sitzt viel näher an der Kathode als die Anode und schirmt die Anode zum großen Teil ab. Eine Änderung der Gitterspannung wirkt deshalb auf das Potential vor der Kathode viel stärker als eine gleich große Änderung der Anodenspannung, bei der ECC83 hundertmal stärker: 100 V weniger an der Anode gleicht 1 V mehr am Gitter aus, bei 150 V und −1 V fließen dieselben 1,2 mA wie bei 250 V und −2 V. Dieser Faktor heißt __Verstärkungsfaktor__ $\mu$, hier $\mu = 100$.

**Schritt 4**: Das Gitter liegt negativ gegen die Kathode. Es stößt die Elektronen ab, sie fliegen zwischen den Drähten hindurch zur Anode, und auf dem Gitter selbst landet praktisch keines. Durch den Steueranschluss fließt deshalb kein Gleichstrom: Gitter und Kathode bilden einen kleinen Kondensator, und eine Änderung der Gitterspannung verschiebt nur dessen Ladung. Diese Steuerung über ein elektrisches Feld heißt __kapazitiv__; sie kostet fast keine Leistung.

**Schritt 5**: Die Leistung des verstärkten Signals stammt aus der Anodenspannungsquelle. Bei fester Anodenspannung ändern 0,1 V mehr am Gitter den Anodenstrom um 0,16 mA. Liegt im Anodenkreis ein __Arbeitswiderstand__ von 100 kΩ zwischen Anode und Versorgung, sinkt die Anodenspannung, sobald der Strom steigt, und bremst ihn etwas; an der Anode bleibt eine Spannungsänderung von 6,15 V, das 61,5-Fache der Eingangsänderung, mit umgekehrtem Vorzeichen. Die Anordnung aus Röhre und Arbeitswiderstand heißt __Verstärkerstufe__.

:::analogie
Eine Triode arbeitet wie ein Ventil in einer Wasserleitung unter Druck: Die Leitung liefert Wasser und Druck, das Ventil bestimmt nur, wie viel fließt. Im britischen Englisch heißt die Elektronenröhre bis heute *valve*.

| Im Vergleich | In der Triode |
|---|---|
| Druck der Leitung | Anodenspannung aus der Versorgung |
| Stellung des Ventils | Gitterspannung |
| Durchfluss | Anodenstrom |
| Kraft am Griff | Steuerleistung am Gitter |

**Wo der Vergleich nicht stimmt:** Ein Ventilgriff verlangt Kraft und Arbeit, das negative Gitter fast keine Leistung. Und der Durchfluss eines Ventils hängt stark vom Leitungsdruck ab, der Anodenstrom von der Anodenspannung hundertmal schwächer als von der Gitterspannung.
:::

:::fehlvorstellung
„Ein Verstärker vervielfacht Energie.“ Das liegt nahe, weil am Ausgang ein größeres Signal erscheint als am Eingang. Die zusätzliche Leistung stammt aber aus der Versorgung; der Verstärker formt nur ihren Fluss nach dem Muster des Eingangssignals. Die ECC83-Stufe aus Schritt 5 gibt bei 6,15 V Amplitude 0,19 mW Signalleistung ab und nimmt dafür 0,44 W aus der Anodenspannungsquelle und 0,945 W für die Heizung auf; fast alles davon wird Wärme.
:::

:::frage
„Warum muss die Kathode überhaupt geheizt werden?“
Im kalten Metall sind die Leitungselektronen gebunden: Um die Oberfläche zu verlassen, muss ein Elektron eine Energieschwelle überwinden, die __Austrittsarbeit__, bei Wolfram 4,5 eV, bei den Oxidkathoden von Empfängerröhren etwa 1 eV. Welcher Anteil der Elektronen genug Wärmeenergie für eine Schwelle von 1 eV hat, gibt der __Boltzmann-Faktor__ an, die Exponentialfunktion von minus Schwelle durch thermische Energie: bei 300 K 1,6·10⁻¹⁷, bei 1000 K 9·10⁻⁶. Der austretende Strom wächst dadurch um mehr als das 10¹¹-Fache, mit dem zusätzlichen Temperaturfaktor der Richardson-Gleichung um rund das 6·10¹²-Fache; erst bei Glühtemperatur treten genug Elektronen aus. Die Heizung kostet bei der ECC83 0,945 W je System, gut dreimal so viel wie die 0,3 W, die im Arbeitspunkt an der Anode umgesetzt werden; diesen Aufwand braucht ein Transistor nicht.
:::

### Steilheit, Innenwiderstand und Verstärkung

*Mit welchen Kenngrößen rechnet man die Verstärkung einer Röhrenstufe aus?*

:::grafik
Szene: st1/einfuehrung/01-triodenkennlinien · Vorlage: kennlinienschar
**Abbildung 3:** Anodenstrom $I_a$ in mA über der Gitterspannung $U_g$ von −4 V bis 0 V für die Anodenspannungen 150 V, 200 V und 250 V, berechnet mit dem Raumladungsgesetz, nach dem der Strom mit der Potenz 3/2 der wirksamen Spannung vor der Kathode wächst, angepasst an die Datenblattwerte der ECC83. Markiert sind der Arbeitspunkt bei 250 V, −2 V und 1,2 mA mit seiner Tangente (Steigung 1,6 mA/V) sowie der Punkt 150 V, −1 V mit demselben Strom. Jede um 50 V höhere Anodenspannung verschiebt die Kurve um 0,5 V nach links. Ein Volt am Gitter wirkt wie hundert Volt an der Anode.
:::

Abbildung 3 zeigt den Anodenstrom über der Gitterspannung, die __Kennlinie__ der Röhre, für drei Anodenspannungen. Die 0,16 mA je 0,1 V Gitterspannung aus Schritt 5 sind ihre Steigung im Arbeitspunkt, 1,6 mA/V. Die Anodenspannung wirkt viel schwächer: 6,25 V mehr erhöhen den Strom nur um 0,1 mA. Beide Wirkungen beschreibt man mit zwei Kenngrößen, die für jede Röhre im Datenblatt stehen.

**Die Akteure:**

- __$S$__: __Steilheit__, die Änderung des Anodenstroms je Volt Gitterspannung bei fester Anodenspannung; in mA/V; 1,6 mA/V. Sie misst, wie stark das Gitter steuert.
- __$R_i$__: __Innenwiderstand__, die Änderung der Anodenspannung je Milliampere Anodenstrom bei fester Gitterspannung; in kΩ; 62,5 kΩ. Je größer er ist, desto weniger hängt der Strom von der Anodenspannung ab.
- __$R_a$__: Arbeitswiderstand zwischen Anode und Versorgung; 100 kΩ.
- __$u_g$__, __$u_a$__, __$i_a$__: kleine Änderungen von Gitterspannung, Anodenspannung und Anodenstrom gegenüber dem Arbeitspunkt, in V bzw. mA; Kleinbuchstaben kennzeichnen Änderungen.
- __$v_u$__: Spannungsverstärkung der Stufe, das Verhältnis $u_a/u_g$; dimensionslos.

Formal sind Steilheit und Innenwiderstand partielle Ableitungen, Steigungen der Kennlinie, bei denen die jeweils andere Spannung festgehalten wird:

:::formel Definition
$$S = \left.\frac{\partial I_a}{\partial U_g}\right|_{U_a}$$

$$\frac{1}{R_i} = \left.\frac{\partial I_a}{\partial U_a}\right|_{U_g}$$
:::

Man definiert sie so, weil sich für kleine Änderungen jede glatte Kennlinie durch ihre Tangente ersetzen lässt; dann genügen diese zwei Zahlen, um den Strom zu berechnen. Die Verstärkerstufe hat damit die Spannungsverstärkung:

:::formel Formel
$$v_u = \frac{u_a}{u_g} = -S\,\left(R_i \parallel R_a\right) = -S\,\frac{R_i\,R_a}{R_i + R_a}$$
:::

**So liest man das:** Die Steilheit setzt die Gitterspannung in einen Strom um, und dieser Strom erzeugt an der Parallelschaltung aus Innenwiderstand und Arbeitswiderstand die Ausgangsspannung. Das Minuszeichen bedeutet, dass die Anodenspannung sinkt, wenn die Gitterspannung steigt. Je größer der Arbeitswiderstand, desto größer der Betrag der Verstärkung, aber nie größer als $S R_i$.

**Kurz gesagt:** Die Verstärkung ist Steilheit mal wirksamer Widerstand am Ausgang; ihr Höchstwert, bei unbegrenzt großem Arbeitswiderstand, ist Steilheit mal Innenwiderstand.

Idee der Herleitung: Man ersetzt die Kennlinie durch ihre Tangentenebene im Arbeitspunkt und verknüpft sie mit dem Spannungsabfall am Arbeitswiderstand.

:::herleitung
**Ausgangspunkt:** der Anodenstrom als Funktion beider Spannungen, $I_a(U_g, U_a)$, und die Definitionen von Steilheit und Innenwiderstand.

**Annahmen:** (i) Die Änderungen sind so klein, dass die Kennlinie im Arbeitspunkt durch ihre Tangente ersetzt werden darf; bei der ECC83 weicht der Strom bei 0,1 V Gitteränderung nur um etwa 2 % von der Tangente ab. (ii) Die Versorgungsspannung $U_B$ ist konstant. (iii) Es fließt kein Gitterstrom, und der Ausgang ist nicht belastet.

**Schritt 1**: Totales Differential des Anodenstroms; die Änderung setzt sich aus den Beiträgen beider Spannungen zusammen:

$$i_a = S\,u_g + \frac{u_a}{R_i}$$

**Schritt 2**: Der Arbeitswiderstand liegt zwischen Versorgung und Anode, also gilt für die Anodenspannung:

$$U_a = U_B - R_a\,I_a$$

Weil $U_B$ konstant ist, folgt für die Änderungen:

$$u_a = -R_a\,i_a$$

**Schritt 3** (entscheidender Schritt): Schritt 2 in Schritt 1 eingesetzt; die Rückwirkung der Anodenspannung auf den Strom erscheint als zweiter Term:

$$-\frac{u_a}{R_a} = S\,u_g + \frac{u_a}{R_i}$$

**Schritt 4**: Nach $u_a$ aufgelöst:

$$u_a\left(\frac{1}{R_a} + \frac{1}{R_i}\right) = -S\,u_g$$

**Ergebnis:**

$$v_u = \frac{u_a}{u_g} = -S\,\frac{R_i\,R_a}{R_i + R_a}$$

**Woher die Faktoren kommen:** $S$ stammt aus der Steuerwirkung des Gitters (Schritt 1); die Parallelschaltung entsteht, weil der Signalstrom sich auf zwei Wege verteilt, den Arbeitswiderstand und den Innenwiderstand, durch den die Röhre auf ihre eigene Anodenspannung reagiert (Schritt 3). Das Minuszeichen kommt aus Schritt 2.

**Proben:** Einheit: mA/V mal kΩ ist dimensionslos. Grenzfall $R_a \to \infty$: $v_u \to -S R_i$, bei der ECC83 −100. Grenzfall $R_a \to 0$: keine Spannungsänderung, $v_u = 0$. Zahlenwert: −1,6 mA/V · 38,46 kΩ = −61,5.

**Grenzen:** Bei großen Signalen gilt die Tangente nicht mehr; die Röhre arbeitet dann im gekrümmten Teil der Kennlinie und verzerrt. Bei hohen Frequenzen kommen die Kapazitäten zwischen den Elektroden hinzu.
:::

::::beispiel Verstärkung und Leistungsbilanz einer ECC83-Stufe
**Gegeben:** ein System der ECC83 im Arbeitspunkt $U_a$ = 250 V, $U_g$ = −2 V, $I_a$ = 1,2 mA mit $S$ = 1,6 mA/V und $R_i$ = 62,5 kΩ (Datenblatt); Arbeitswiderstand $R_a$ = 100 kΩ; Heizung 6,3 V und 0,3 A für beide Systeme; Eingangssignal mit 0,1 V Amplitude.

**Gesucht:** Spannungsverstärkung, Ausgangsamplitude, nötige Versorgungsspannung und die Leistungsbilanz.

**Rechnung:** Parallelschaltung und Verstärkung:

$$R_i \parallel R_a = \frac{62{,}5\ \mathrm{k\Omega}\cdot 100\ \mathrm{k\Omega}}{162{,}5\ \mathrm{k\Omega}} = 38{,}46\ \mathrm{k\Omega}$$

$$v_u = -1{,}6\ \mathrm{mA/V}\cdot 38{,}46\ \mathrm{k\Omega} = -61{,}5$$

Ausgangsamplitude:

$$\hat u_a = 61{,}5\cdot 0{,}1\ \mathrm{V} = 6{,}15\ \mathrm{V}$$

Damit an der Anode 250 V liegen, muss die Versorgung den Spannungsabfall am Arbeitswiderstand mitliefern:

$$U_B = U_a + R_a\,I_a = 250\ \mathrm{V} + 100\ \mathrm{k\Omega}\cdot 1{,}2\ \mathrm{mA} = 370\ \mathrm{V}$$

Leistungen: aus der Versorgung, Signalleistung am Arbeitswiderstand und Heizung je System:

$$P_B = U_B\,I_a = 370\ \mathrm{V}\cdot 1{,}2\ \mathrm{mA} = 0{,}444\ \mathrm{W}$$

$$P_\mathrm{sig} = \frac{\hat u_a^2}{2\,R_a} = \frac{(6{,}15\ \mathrm{V})^2}{2\cdot 100\ \mathrm{k\Omega}} = 0{,}19\ \mathrm{mW}$$

$$P_\mathrm{H} = \frac{6{,}3\ \mathrm{V}\cdot 0{,}3\ \mathrm{A}}{2} = 0{,}945\ \mathrm{W}$$

**Ergebnis:** **$v_u$ = −61,5; 6,15 V Ausgangsamplitude; $U_B$ = 370 V; 0,19 mW Signalleistung bei 1,39 W Gesamtaufnahme.**

**Einordnung:** Das Signal am Ausgang trägt etwa ein Siebentausendstel der aufgenommenen Leistung; der Rest wird in Röhre, Arbeitswiderstand und Heizfaden zu Wärme. Spannungsverstärkung heißt nicht, dass Energie entsteht, sondern dass ein kleines Signal einen großen Energiefluss formt. Mit unbegrenzt großem Arbeitswiderstand ginge die Verstärkung gegen −100.
::::

### Steuerspannung, Durchgriff und Barkhausen-Formel

*Warum ist die Kennlinienschar in Abbildung 3 nur eine verschobene Kopie derselben Kurve, und warum hängen Steilheit, Innenwiderstand und Verstärkungsfaktor zusammen?*

Die Kurven in Abbildung 3 haben alle dieselbe Form; eine höhere Anodenspannung schiebt sie nur nach links, um 0,5 V je 50 V. Der Strom hängt also nicht von beiden Spannungen getrennt ab, sondern nur von einer Kombination aus ihnen.

**Die Akteure:**

- __$D$__: __Durchgriff__, der Bruchteil, mit dem die Anodenspannung durch die Maschen des Gitters hindurch auf das Potential vor der Kathode wirkt, gemessen an der Wirkung der Gitterspannung; dimensionslos; 0,01 bei der ECC83. Der Verstärkungsfaktor ist sein Kehrwert, $\mu = 1/D = 100$.
- __$U_\mathrm{st}$__: __Steuerspannung__, die Kombination aus Gitter- und Anodenspannung, von der allein der Strom abhängt; in V; 0,5 V im Arbeitspunkt.

:::formel Gesetz
$$I_a = h\left(U_\mathrm{st}\right)$$

$$U_\mathrm{st} = U_g + D\,U_a$$
:::

**So liest man das:** Die Anodenspannung zählt nur mit dem Gewicht $D$. Jede Änderung der Anodenspannung lässt sich deshalb durch eine $D$-mal so große, entgegengesetzte Änderung der Gitterspannung ausgleichen, und die Kennlinien für verschiedene Anodenspannungen sind verschobene Kopien. Die Funktion $h$ beschreibt die Kurvenform; sie wird null, wenn die Steuerspannung so negativ ist, dass die Elektronen nicht mehr aus der Wolke herauskommen, bei der ECC83 und 250 V ab etwa −3,1 V Gitterspannung.

Idee der Herleitung: Ohne Raumladung ist das Potential in der Gitterebene eine gewichtete Summe der Elektrodenspannungen, und der Strom hängt nur von diesem Potential ab.

:::herleitung
**Ausgangspunkt:** die Überlagerung in der Elektrostatik: Die Gleichungen für das Potential sind linear; ohne Raumladung ist das Potential an jedem Ort deshalb eine Summe von Beiträgen der einzelnen Elektroden, jeder proportional zu ihrer Spannung gegen die Kathode.

**Annahmen:** (i) Das Gitter ist so fein, dass man über die Drahtabstände mitteln und es als Fläche mit einem mittleren Potential behandeln darf. (ii) Der Strom hängt nur von diesem mittleren Potential in der Gitterebene ab, wie bei einer Diode, deren Anode in der Gitterebene läge (Ersatzdiode). (iii) Das Gitter ist negativ und führt keinen Strom.

**Schritt 1**: Mittleres Potential der Gitterebene, berechnet ohne Raumladung, mit zwei positiven Geometriefaktoren $c_g$ und $c_a$, die nur von der Anordnung der Elektroden abhängen:

$$\varphi_G = c_g\,U_g + c_a\,U_a$$

**Schritt 2**: $c_g$ ausgeklammert; das Verhältnis der Geometriefaktoren ist der Durchgriff:

$$\varphi_G = c_g\left(U_g + \frac{c_a}{c_g}\,U_a\right) = c_g\left(U_g + D\,U_a\right)$$

**Schritt 3** (entscheidender Schritt): Nach Annahme (ii) hängt der Strom nur von $\varphi_G$ ab; weil $c_g$ eine feste Zahl ist, hängt er damit nur von der Klammer ab. Diese Abhängigkeit heißt $h$:

$$I_a = h\left(U_g + D\,U_a\right)$$

**Ergebnis:**

$$I_a = h\left(U_\mathrm{st}\right)$$

$$U_\mathrm{st} = U_g + D\,U_a$$

**Woher die Faktoren kommen:** $D$ ist das Verhältnis der Geometriefaktoren aus Schritt 2. Die Anode wirkt nur durch die Lücken zwischen den Gitterdrähten und aus größerer Entfernung, deshalb ist $c_a$ klein gegen $c_g$; ein dichtes Gitter nahe an der Kathode macht den Durchgriff klein und den Verstärkungsfaktor groß.

**Proben:** Einheit: $U_g + D U_a$ ist eine Spannung. Grenzfall $D \to 0$: Die Anode hat keinen Einfluss mehr, die Kennlinien fallen zusammen. Zahlenwert: In Abbildung 3 verschieben 50 V die Kurve um 0,5 V, also $D$ = 0,5 V/50 V = 0,01.

**Grenzen:** Die Geometriefaktoren hängen etwas von den Spannungen ab, weil die Raumladung das Feld verformt; die Steuerspannung ist deshalb eine sehr gute, aber keine exakte Beschreibung. Das Kennlinienmodell der Abbildung braucht zusätzlich eine Verschiebung um 0,625 V, die Kontaktspannungen und die Austrittsgeschwindigkeit der Elektronen zusammenfasst.
:::

Aus dieser Form folgt eine Beziehung, die Heinrich Barkhausen 1919 angegeben hat und die die drei Kenngrößen jeder Triode verknüpft:

:::formel Satz
$$S\cdot D\cdot R_i = 1$$

$$\mu = \frac{1}{D} = S\,R_i$$
:::

**So liest man das:** Steilheit, Durchgriff und Innenwiderstand sind nicht unabhängig; kennt man zwei, folgt die dritte. Eine steile Röhre mit großem Durchgriff hat einen kleinen Innenwiderstand. Die größtmögliche Verstärkung einer Stufe, $S R_i$, ist genau der Verstärkungsfaktor $\mu$, um den das Gitter stärker wirkt als die Anode; bei der ECC83 ergibt 1,6 mA/V mal 62,5 kΩ den Wert 100.

**Kurz gesagt:** Die größtmögliche Spannungsverstärkung einer Triode ist der Faktor, um den ihr Gitter stärker auf den Strom wirkt als ihre Anode.

Idee der Herleitung: Man leitet das Gesetz der Steuerspannung einmal nach $U_g$ und einmal nach $U_a$ ab; beide Ableitungen enthalten dieselbe Steigung von $h$.

:::herleitung
**Ausgangspunkt:** das Gesetz der Steuerspannung (vorige Formel) und die Definitionen von $S$ und $R_i$.

**Annahmen:** (i) $h$ ist differenzierbar, und der Durchgriff $D$ ist konstant.

**Schritt 1**: Ableitung nach $U_g$ bei festem $U_a$ mit der Kettenregel; die innere Ableitung ist 1:

$$S = \frac{dh}{dU_\mathrm{st}}$$

**Schritt 2**: Ableitung nach $U_a$ bei festem $U_g$; die innere Ableitung ist $D$:

$$\frac{1}{R_i} = D\,\frac{dh}{dU_\mathrm{st}}$$

**Schritt 3** (entscheidender Schritt): Schritt 1 in Schritt 2 eingesetzt, die unbekannte Steigung von $h$ fällt heraus:

$$\frac{1}{R_i} = D\,S$$

**Ergebnis:**

$$S\cdot D\cdot R_i = 1$$

**Woher die Faktoren kommen:** Steilheit und Innenwiderstand sind dieselbe Steigung von $h$, einmal direkt und einmal durch den Durchgriff gesehen; deshalb ist ihr Produkt mit $D$ immer 1.

**Proben:** Einheit: mA/V mal kΩ ist dimensionslos. Zahlenwert: 1,6 mA/V · 0,01 · 62,5 kΩ = 1,000. Folge: Bei kleinerem Strom wird die Steigung von $h$ kleiner, $S$ sinkt und $R_i$ steigt im selben Verhältnis, das Produkt bleibt gleich.

**Grenzen:** Gilt, solange die Steuerspannung die Röhre beschreibt (vorige Herleitung).
:::

::::beispiel Durchgriff aus der Kennlinienschar und Probe der Barkhausen-Formel
**Gegeben:** die Kennlinien der Abbildung 3: Bei $U_a$ = 250 V und $U_g$ = −2 V fließen 1,2 mA, bei $U_a$ = 150 V und $U_g$ = −1 V ebenfalls; Steilheit 1,6 mA/V und Innenwiderstand 62,5 kΩ aus dem Datenblatt.

**Gesucht:** Durchgriff, Verstärkungsfaktor und die Probe von $S\,D\,R_i = 1$.

**Rechnung:** Gleicher Strom heißt gleiche Steuerspannung:

$$-2\ \mathrm{V} + D\cdot 250\ \mathrm{V} = -1\ \mathrm{V} + D\cdot 150\ \mathrm{V}$$

$$D = \frac{1\ \mathrm{V}}{100\ \mathrm{V}} = 0{,}01, \qquad \mu = \frac{1}{D} = 100$$

Probe:

$$S\,D\,R_i = 1{,}6\ \mathrm{mA/V}\cdot 0{,}01\cdot 62{,}5\ \mathrm{k\Omega} = 1{,}00$$

**Ergebnis:** **$D$ = 0,01, $\mu$ = 100; die Barkhausen-Formel ist erfüllt.**

**Einordnung:** Die Steuerspannung im Arbeitspunkt beträgt nur 0,5 V: Die durch den Durchgriff auf 2,5 V abgeschwächte Wirkung der Anode und die −2 V des Gitters heben sich vor der Kathode fast auf, und kleine Gitteränderungen bewegen genau diesen kleinen Rest. Für den Feldeffekttransistor heißen dieselben Größen Steilheit $g_m$ und Ausgangswiderstand $r_{DS}$; ihr Produkt, die Eigenverstärkung, spielt dort dieselbe Rolle wie $\mu$.
::::

## Rückkopplung: der Verstärker als Sender

*Wie erzeugt ein Verstärker selbst eine Schwingung, und wie hängt das mit seiner Verstärkung zusammen?*

Ein Funksender braucht einen __Oszillator__, eine Schaltung, die selbst eine ungedämpfte Schwingung konstanter Frequenz erzeugt; die Funkensender der Zeit lieferten nur abklingende Wellenzüge. Alexander Meißner baute 1913 bei Telefunken mit einer Liebenröhre einen der ersten Röhrensender: Er führte einen Teil der Ausgangsspannung der Röhrenstufe über eine Spule auf das Gitter zurück. Dieses Prinzip, die __Rückkopplung__, fanden um dieselbe Zeit auch andere, darunter Edwin Armstrong in den USA.

:::grafik
Szene: st1/einfuehrung/01-rueckkopplung · Vorlage: blockschaltbild-graph
**Abbildung 4:** Links das Signalflussbild: Eingangsspannung $u_1$, Summierstelle, Verstärker $v_u$, Ausgangsspannung $u_2$, Rückführung $k$ zurück zur Summierstelle. Mitte das Verhältnis $A/v_u$ der Verstärkungen mit und ohne Rückführung über der Schleifenverstärkung $k v_u$ von −2 bis 1: links der Null (Gegenkopplung) unter 1, bei $k v_u = -1$ genau 0,5; rechts (Mitkopplung) über 1, bei $k v_u = 0{,}5$ gleich 2, bei $k v_u = 0{,}9$ gleich 10, bei $k v_u = 1$ eine senkrechte Asymptote. Rechts die Meißner-Schaltung: Triode mit einem Schwingkreis aus Spule und Kondensator im Anodenkreis und einer Koppelspule, die auf das Gitter zurückwirkt. Bei $k v_u = 1$ entsteht eine Ausgangsspannung ohne Eingangsspannung: Die Anordnung schwingt.
:::

**Die Akteure:**

- __$v_u$__: Spannungsverstärkung des Verstärkers allein, das Verhältnis aus Ausgangsspannung und Spannung an seinem Eingang; dimensionslos; bei der ECC83-Stufe −61,5.
- __$k$__: __Rückführfaktor__, der Bruchteil der Ausgangsspannung, der zum Eingang zurückgeführt wird, mit Vorzeichen; dimensionslos.
- __$k\,v_u$__: __Schleifenverstärkung__, der Faktor, mit dem ein Signal nach einem Umlauf durch Verstärker und Rückführung wieder am Verstärkereingang ankommt. Ist sie positiv, verstärkt das zurückgeführte Signal das Eingangssignal (__Mitkopplung__); ist sie negativ, schwächt es dieses (__Gegenkopplung__).
- __$u_1$__, __$u_2$__: Eingangs- und Ausgangsspannung der ganzen Anordnung.
- __$A$__: Verstärkung der ganzen Anordnung, $u_2/u_1$.

**Das Zusammenspiel:** Am Verstärkereingang liegt die Summe aus Eingangsspannung und zurückgeführter Spannung. Bei Mitkopplung vergrößert jeder Umlauf das Signal, und die Anordnung verstärkt mehr als der Verstärker allein:

:::formel Formel
$$A = \frac{u_2}{u_1} = \frac{v_u}{1 - k\,v_u}$$
:::

**So liest man das:** Ohne Rückführung ist $A$ gleich $v_u$. Bei Mitkopplung wächst der Betrag von $A$ mit der Schleifenverstärkung, auf das Doppelte bei einer Schleifenverstärkung von 0,5 und das Zehnfache bei 0,9; bei 1 wird der Nenner null, und eine Ausgangsspannung besteht auch ohne Eingangsspannung. Bei Gegenkopplung ist der Nenner größer als 1 und $|A|$ kleiner als $|v_u|$; bei stark negativer Schleifenverstärkung geht $A$ gegen $-1/k$ und hängt nur noch von der Rückführung ab.

**Kurz gesagt:** Mitkopplung vergrößert die Verstärkung bis zur Selbsterregung, Gegenkopplung verkleinert sie und macht sie unempfindlich gegen Schwankungen des Verstärkers.

Idee der Herleitung: Man schreibt die Spannung am Verstärkereingang als Summe von Eingang und Rückführung, setzt sie in die Verstärkergleichung ein und löst nach der Ausgangsspannung auf.

:::herleitung
**Ausgangspunkt:** die Verstärkung $v_u$ als Verhältnis aus Ausgangsspannung und Spannung am Verstärkereingang, und die Summierstelle im Signalflussbild.

**Annahmen:** (i) $v_u$ und $k$ sind bei der betrachteten Frequenz reelle Zahlen, ändern also die Phase nur durch ihr Vorzeichen. (ii) Die Rückführung belastet den Verstärker nicht. (iii) Alle Spannungen bleiben im linearen Bereich.

**Schritt 1**: Spannung am Verstärkereingang, Summe aus Eingang und Rückführung:

$$u_v = u_1 + k\,u_2$$

**Schritt 2**: Der Verstärker vervielfacht sie:

$$u_2 = v_u\,u_v = v_u\,u_1 + k\,v_u\,u_2$$

**Schritt 3** (entscheidender Schritt): Die Ausgangsspannung steht auf beiden Seiten; alle Terme mit $u_2$ nach links:

$$u_2\left(1 - k\,v_u\right) = v_u\,u_1$$

**Ergebnis:**

$$A = \frac{u_2}{u_1} = \frac{v_u}{1 - k\,v_u}$$

**Woher die Faktoren kommen:** Die 1 im Nenner ist der direkte Weg vom Eingang zum Ausgang, $-k v_u$ der Beitrag des Umlaufs; im Zähler steht der Verstärker allein.

**Proben:** Einheit: dimensionslos. Ohne Rückführung bleibt $A$ gleich $v_u$. ECC83-Stufe mit der Schleifenverstärkung 0,5: −61,5/0,5 = −123. Bei der Schleifenverstärkung 1 erfüllt jedes $u_2$ die Gleichung aus Schritt 3 auch ohne Eingangsspannung: eine Ausgangsspannung ohne Eingang.

**Grenzen:** Reale Verstärker und Rückführungen hängen von der Frequenz ab und verschieben die Phase; Annahme (i) gilt dann nur bei einzelnen Frequenzen. Bei $k v_u > 1$ wächst das Signal, bis die Kennlinie der Röhre gekrümmt wird; die lineare Formel gilt dann nicht mehr.
:::

::::beispiel Mit- und Gegenkopplung an der ECC83-Stufe
**Gegeben:** die ECC83-Stufe mit $v_u$ = −61,5 (Vorzeichenumkehr wie in Schritt 5 der Röhre).

**Gesucht:** (a) die Verstärkung bei Mitkopplung mit $k v_u$ = 0,5 und 0,9 und der Rückführfaktor für Selbsterregung; (b) die Verstärkung bei Gegenkopplung mit $k$ = 0,1 und ihre Änderung, wenn $v_u$ um 20 % sinkt.

**Rechnung:** (a) Mitkopplung:

$$A = \frac{-61{,}5}{1 - 0{,}5} = -123, \qquad A = \frac{-61{,}5}{1 - 0{,}9} = -615$$

Selbsterregung bei $k v_u = 1$:

$$k = \frac{1}{v_u} = \frac{1}{-61{,}5} = -0{,}0163$$

(b) Gegenkopplung mit dem Rückführfaktor 0,1, also der Schleifenverstärkung −6,15:

$$A = \frac{-61{,}5}{1 + 6{,}15} = -8{,}60$$

Mit $v_u$ = −49,2 (20 % weniger):

$$A = \frac{-49{,}2}{1 + 4{,}92} = -8{,}31$$

**Ergebnis:** **(a) −123 und −615; Selbsterregung ab $k$ = −0,0163, also 1,6 % der Ausgangsspannung mit umgekehrter Polung. (b) −8,60; bei 20 % weniger Röhrenverstärkung nur 3,4 % weniger Gesamtverstärkung.**

**Einordnung:** Weil die Stufe das Vorzeichen umkehrt, muss die Rückführung es für Mitkopplung noch einmal umkehren; Meißner erreichte das durch die Wicklungsrichtung der Koppelspule. Für (b) gilt umgekehrt: Die Stufe kehrt das Vorzeichen selbst um, eine Rückführung ohne Umkehr wirkt gegenkoppelnd. Der Grenzwert $-1/k$ = −10 wird bei $k v_u$ = −6,15 erst zu 86 % erreicht.
::::

Damit aus der Mitkopplung eine Schwingung **einer** Frequenz wird, liegt im Anodenkreis der Meißner-Schaltung ein __Schwingkreis__ aus Spule und Kondensator. Er hat nur bei seiner __Resonanzfrequenz__, der Frequenz, mit der er von selbst schwingen würde, einen großen Widerstand ohne Phasenverschiebung; dort ist die Verstärkung der Stufe am größten, und die zurückgeführte Spannung kommt genau gleichphasig am Gitter an. Ist die Schleifenverstärkung bei dieser Frequenz etwas größer als 1, wächst jede kleine Störung, etwa das Rauschen der Röhre, von Umlauf zu Umlauf. Das Wachstum endet, wenn die Röhre in den gekrümmten Teil ihrer Kennlinie gerät und ihre mittlere Verstärkung so weit sinkt, dass die Schleifenverstärkung genau 1 beträgt; dann bleibt die Amplitude konstant. Diese Bedingung, Schleifenverstärkung 1 bei Phase null, gilt für jeden Oszillator.

Die Gegenkopplung wurde zum zweiten Grundprinzip: Harold Black führte 1927 einen Teil des Ausgangssignals mit umgekehrtem Vorzeichen zurück und erhielt Verstärker, deren Verstärkung fast nur von der Rückführung abhängt. Auf diesem Prinzip beruhen alle linearen Verstärkerschaltungen mit Operationsverstärkern ([Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html)); dort schreibt man das Minuszeichen an die Summierstelle, und mit der Leerlaufverstärkung $v_D$ des Operationsverstärkers steht im Nenner $1 + k\,v_D$; die Schleifenverstärkung $k\,v_D$ ist dort bei Gegenkopplung deshalb positiv.

## Überlagerung: ein Empfänger für jede Frequenz

*Warum setzt ein Empfänger jeden Sender auf eine feste Zwischenfrequenz um, und wie gelingt das?*

An der Antenne kommen alle Sender gleichzeitig an, und der Empfänger muss einen herausfiltern. Ein Filter trennt Frequenzen umso schärfer, je höher seine __Güte__ ist, das Verhältnis aus Mittenfrequenz und durchgelassener Bandbreite. Ein UKW-Sender belegt rund 200 kHz. Ein Filter, das ihn bei 100 MHz allein durchlässt, braucht die Güte 500 und müsste sich für jeden Sender neu abstimmen lassen, mit mehreren Schwingkreisen im Gleichlauf. Bei 10,7 MHz genügt für dieselbe Bandbreite die Güte 53,5, und ein Filter für eine feste Frequenz lässt sich einmal genau abgleichen.

Lucien Lévy in Frankreich (1917), Walter Schottky bei Siemens & Halske (1918) und Edwin Armstrong (1918/19) meldeten unabhängig voneinander ein Verfahren zum Patent an, das jeden Sender auf eine solche feste Frequenz umsetzt: den __Überlagerungsempfänger__, englisch superheterodyne receiver. In Deutschland verzögerte die wirtschaftliche Lage nach dem Ersten Weltkrieg die Verwertung; ab den 1930er-Jahren wurde der Überlagerungsempfänger zur Grundform fast aller Rundfunkempfänger.

:::grafik
Szene: st1/einfuehrung/01-ueberlagerung · Vorlage: blockschaltbild-spektrum
**Abbildung 5:** Oben der Überlagerungsempfänger als Blockbild: Antenne, Vorfilter, Mischer mit dem abstimmbaren Lokaloszillator, Zwischenfrequenzfilter und -verstärker bei fester Frequenz, Demodulator, Lautsprecher. Unten das Spektrum auf einer Frequenzachse von 0 bis 220 MHz: das UKW-Band 87,5 bis 108 MHz grau hinterlegt, der gewünschte Sender bei 100 MHz, der Oszillator bei 110,7 MHz, die Mischprodukte bei 10,7 MHz (Differenz, Zwischenfrequenz) und 210,7 MHz (Summe), dazu die Spiegelfrequenz 121,4 MHz außerhalb des Bandes. Das Mischen schiebt den gewünschten Sender auf die feste Zwischenfrequenz; abgestimmt wird nur der Oszillator.
:::

**Die Akteure:**

- __$f_E$__: Frequenz des gewünschten Senders; im Beispiel 100 MHz.
- __$f_\mathrm{LO}$__: Frequenz des __Lokaloszillators__, eines Oszillators im Empfänger, den man beim Abstimmen verstellt; 110,7 MHz.
- __$f_\mathrm{ZF}$__: die feste __Zwischenfrequenz__; bei UKW-Empfängern 10,7 MHz.
- __Mischer__: eine Schaltung, deren Ausgangsspannung das Produkt der beiden Eingangsspannungen enthält. Jede Kennlinie mit quadratischem Anteil liefert ein solches Produkt, etwa die einer Diode oder einer Triode: Ist ein Strom proportional zum Quadrat der Summe zweier Spannungen, enthält er das doppelte Produkt beider.

**Das Zusammenspiel:** Der Mischer multipliziert das Empfangssignal mit der Oszillatorschwingung. Das Produkt zweier Kosinusschwingungen ist wieder eine Summe von Kosinusschwingungen:

:::formel Satz
$$\cos\alpha\cdot\cos\beta = \tfrac12\cos(\alpha - \beta) + \tfrac12\cos(\alpha + \beta)$$
:::

Setzt man für $\alpha$ und $\beta$ die Phasen der beiden Schwingungen ein,

$$\alpha = 2\pi f_\mathrm{LO}\,t, \qquad \beta = 2\pi f_E\,t,$$

entstehen Schwingungen bei der Differenz und bei der Summe beider Frequenzen. Ein Filter bei der Differenz lässt nur sie durch; sie ist die Zwischenfrequenz:

:::formel Formel
$$f_\mathrm{ZF} = f_\mathrm{LO} - f_E$$
:::

**So liest man das:** Der Oszillator liegt um die Zwischenfrequenz über dem gewünschten Sender. Stimmt man auf einen anderen Sender um, verstellt man nur den Oszillator, so dass die Differenz wieder 10,7 MHz beträgt; Filter und Verstärker der Zwischenfrequenz bleiben unverändert. Die Summenfrequenz, beim Sender auf 100 MHz 210,7 MHz, hält das Zwischenfrequenzfilter zurück.

**Kurz gesagt:** Das Produkt zweier Kosinusschwingungen ist die halbe Summe zweier Kosinusschwingungen, eine mit der Differenz und eine mit der Summe der beiden Frequenzen.

Idee der Herleitung: Man addiert die Additionstheoreme für $\cos(\alpha - \beta)$ und $\cos(\alpha + \beta)$; die Sinusprodukte heben sich auf.

:::herleitung
**Ausgangspunkt:** die Additionstheoreme des Kosinus (ausführlicher in [Schwebung und das Produkt zweier Sinussignale](/wissen/elektrotechnik/1-semester/mathematische-methoden-der-elektrotechnik/spektrum-und-fourier-reihe/schwebung-und-produkt.html)).

**Annahmen:** (i) Der Mischer bildet das Produkt der beiden Spannungen mit einem konstanten Faktor; weitere Mischprodukte bei Vielfachen der Frequenzen liegen weit neben der Zwischenfrequenz und werden ausgefiltert. (ii) Der Oszillator liegt oberhalb des Senders.

**Schritt 1**: Die beiden Additionstheoreme:

$$\cos(\alpha - \beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta$$

$$\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$$

**Schritt 2** (entscheidender Schritt): Addiert, die Sinusprodukte heben sich auf:

$$\cos(\alpha - \beta) + \cos(\alpha + \beta) = 2\cos\alpha\cos\beta$$

**Schritt 3**: Mit den Phasen beider Schwingungen haben die Summanden die Differenz- bzw. die Summenfrequenz:

$$\alpha - \beta = 2\pi\,(f_\mathrm{LO} - f_E)\,t, \qquad \alpha + \beta = 2\pi\,(f_\mathrm{LO} + f_E)\,t$$

**Ergebnis:**

$$\cos\alpha\cdot\cos\beta = \tfrac12\cos(\alpha - \beta) + \tfrac12\cos(\alpha + \beta)$$

$$f_\mathrm{ZF} = f_\mathrm{LO} - f_E$$

**Woher die Faktoren kommen:** Der Faktor ½ entsteht, weil in Schritt 2 das Produkt doppelt erscheint; Differenz- und Summenfrequenz stammen aus den Phasen $\alpha \mp \beta$.

**Proben:** $\alpha = \beta = 0$: links 1, rechts ½ + ½ = 1. Zahlenwert bei $t$ = 1,234 ns mit 110,7 MHz und 100 MHz: beide Seiten 0,466873. Die Frequenzen haben dieselbe Einheit wie $f_\mathrm{LO}$ und $f_E$.

**Grenzen:** Ein realer Mischer liefert zusätzlich Produkte bei Vielfachen der Frequenzen; bei UKW liegen sie weit von 10,7 MHz entfernt. Gegen ein zweites Signal, das ebenso weit über dem Oszillator liegt wie der Sender darunter, hilft das Zwischenfrequenzfilter nicht; davor schützt nur das Vorfilter.
:::

Das Mischen verschiebt das Signal mitsamt seiner Information. Schwankt die Frequenz eines UKW-Senders im Takt der Musik um bis zu ±75 kHz, schwankt die Zwischenfrequenz um dieselben ±75 kHz, wegen des oberhalb liegenden Oszillators in umgekehrter Richtung, und der __Demodulator__, der aus der Frequenzschwankung das Tonsignal zurückgewinnt, arbeitet bei 10,7 MHz.

Die Differenzbildung hat eine Kehrseite: Der Mischer unterscheidet nicht, ob ein Signal um die Zwischenfrequenz unter oder über dem Oszillator liegt. Ein Signal bei der __Spiegelfrequenz__ landet ebenfalls auf der Zwischenfrequenz:

:::formel Formel
$$f_\mathrm{Sp} = f_\mathrm{LO} + f_\mathrm{ZF} = f_E + 2\,f_\mathrm{ZF}$$
:::

**So liest man das:** Die Spiegelfrequenz liegt spiegelbildlich zum gewünschten Sender auf der anderen Seite des Oszillators, zwei Zwischenfrequenzen vom Sender entfernt. Ein Vorfilter vor dem Mischer muss sie unterdrücken; je höher die Zwischenfrequenz, desto weiter liegt sie weg und desto leichter gelingt das.

Idee der Herleitung: Man sucht alle Frequenzen, deren Abstand vom Oszillator gleich der Zwischenfrequenz ist.

:::herleitung
**Ausgangspunkt:** das Mischprodukt bei der Differenzfrequenz aus der vorigen Herleitung. Weil der Kosinus gerade ist, zählt nur der Betrag der Differenz.

**Annahmen:** (i) Der Oszillator liegt oberhalb des gewünschten Senders. (ii) Das Zwischenfrequenzfilter lässt nur $f_\mathrm{ZF}$ durch.

**Schritt 1**: Ein Signal bei einer beliebigen Frequenz $f$ erzeugt die Differenzschwingung

$$\cos\big(2\pi\,(f_\mathrm{LO} - f)\,t\big) = \cos\big(2\pi\,|f_\mathrm{LO} - f|\,t\big)$$

**Schritt 2** (entscheidender Schritt): Sie passiert das Filter, wenn ihr Betrag die Zwischenfrequenz ist; das trifft auf zwei Frequenzen zu:

$$f = f_\mathrm{LO} - f_\mathrm{ZF} = f_E$$

oder

$$f = f_\mathrm{LO} + f_\mathrm{ZF}$$

**Schritt 3**: Die zweite Lösung mit $f_\mathrm{LO} = f_E + f_\mathrm{ZF}$ ausgedrückt:

$$f_\mathrm{Sp} = f_E + f_\mathrm{ZF} + f_\mathrm{ZF} = f_E + 2\,f_\mathrm{ZF}$$

**Ergebnis:**

$$f_\mathrm{Sp} = f_\mathrm{LO} + f_\mathrm{ZF} = f_E + 2\,f_\mathrm{ZF}$$

**Woher die Faktoren kommen:** Die 2 steht für den doppelten Abstand, einmal vom Sender zum Oszillator und einmal vom Oszillator zum Spiegel.

**Proben:** 100 MHz + 2 · 10,7 MHz = 121,4 MHz; Gegenprobe: 121,4 MHz − 110,7 MHz = 10,7 MHz. Grenzfall: Bei der Zwischenfrequenz null fällt der Spiegel auf den Sender selbst.

**Grenzen:** Liegt der Oszillator unterhalb des Senders, liegt der Spiegel ebenso weit darunter, bei $f_E - 2 f_\mathrm{ZF}$.
:::

::::beispiel Ein UKW-Empfänger mit 10,7 MHz Zwischenfrequenz
**Gegeben:** Sender bei $f_E$ = 100 MHz; Zwischenfrequenz $f_\mathrm{ZF}$ = 10,7 MHz, Oszillator oberhalb; Bandbreite eines Senders 200 kHz; UKW-Band 87,5 bis 108 MHz; Frequenzhub ±75 kHz. Die Güte $Q$ eines Filters ist Mittenfrequenz durch Bandbreite.

**Gesucht:** Oszillatorfrequenz, Mischprodukte, Spiegelfrequenz, nötige Filtergüte mit und ohne Umsetzung, Lage der Spiegel aller UKW-Sender.

**Rechnung:** Oszillator und Mischprodukte:

$$f_\mathrm{LO} = f_E + f_\mathrm{ZF} = 110{,}7\ \mathrm{MHz}$$

$$f_\mathrm{LO} - f_E = 10{,}7\ \mathrm{MHz}, \qquad f_\mathrm{LO} + f_E = 210{,}7\ \mathrm{MHz}$$

Spiegelfrequenz:

$$f_\mathrm{Sp} = 100\ \mathrm{MHz} + 2\cdot 10{,}7\ \mathrm{MHz} = 121{,}4\ \mathrm{MHz}$$

Güte für 200 kHz Bandbreite:

$$Q_E = \frac{100\ \mathrm{MHz}}{200\ \mathrm{kHz}} = 500, \qquad Q_\mathrm{ZF} = \frac{10{,}7\ \mathrm{MHz}}{200\ \mathrm{kHz}} = 53{,}5$$

Spiegel des untersten und des obersten Senders:

$$87{,}5\ \mathrm{MHz} + 21{,}4\ \mathrm{MHz} = 108{,}9\ \mathrm{MHz}, \qquad 108\ \mathrm{MHz} + 21{,}4\ \mathrm{MHz} = 129{,}4\ \mathrm{MHz}$$

**Ergebnis:** **Oszillator 110,7 MHz; Mischprodukte 10,7 MHz und 210,7 MHz; Spiegel 121,4 MHz; Filtergüte 53,5 statt 500; alle Spiegel zwischen 108,9 und 129,4 MHz, oberhalb des Bandes.**

**Einordnung:** Das Band ist 20,5 MHz breit, der Spiegelabstand 21,4 MHz; deshalb fällt kein UKW-Sender auf den Spiegel eines anderen, und das Vorfilter muss nur Signale außerhalb des Bandes dämpfen. Das erklärt die Wahl von 10,7 MHz. Der Hub von ±75 kHz erscheint auf der Zwischenfrequenz als Schwankung zwischen 10,625 und 10,775 MHz.
::::

## Der Transistor: ein Ventil ohne Heizung

*Warum hat der Transistor die Röhre verdrängt, und warum musste er aus Silizium sein?*

Im Dezember 1947 brachten John Bardeen und Walter Brattain in den Bell Laboratories in den USA ein Germaniumplättchen mit zwei eng benachbarten Metallspitzen zum Verstärken, den ersten __Transistor__ (Spitzentransistor). Germanium ist ein __Halbleiter__, ein Stoff, dessen Leitfähigkeit zwischen der von Metallen und Isolatoren liegt und sich durch eingebaute Fremdatome, die __Dotierung__, gezielt einstellen lässt: Je nach Fremdatom überwiegen als bewegliche Ladungsträger Elektronen (n-Gebiet) oder __Löcher__, fehlende Bindungselektronen, die sich wie positive Ladungen bewegen (p-Gebiet) ([Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html)). William Shockley, der Leiter der Gruppe, entwarf im Januar 1948 den __Flächentransistor__ aus drei solchen Schichten mit zwei Grenzen zwischen n- und p-Gebiet, den __pn-Übergängen__: den __Bipolartransistor__ in der bis heute gebauten Form; ab 1950/51 ließ er sich herstellen. 1956 erhielten die drei den Nobelpreis für Physik. Auch der Bipolartransistor ist ein gesteuertes Ventil: Eine kleine Spannung zwischen Basis und Emitter steuert den großen Strom zwischen Kollektor und Emitter ([Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html)).

Gegenüber der Röhre fehlt dem Transistor die Heizung, und er ist klein, stoßfest und verschleißt nicht. Wie viel allein die Heizung ausmacht, zeigt eine Überschlagsrechnung: Ein Triodensystem der ECC83 braucht 0,945 W Heizleistung. 291 Millionen davon, so viele Ventile wie Transistoren in einem Prozessor des Jahres 2006 (Intel Core 2 Duo), bräuchten 275 MW nur zum Heizen, das 4,2-Millionen-Fache der 65 W, für die der ganze Prozessor ausgelegt ist (seine thermische Auslegungsleistung). Wie unzuverlässig viele Röhren zusammen sind, zeigte der Rechner ENIAC von 1946 mit 17 468 Röhren und rund 150 kW: Anfangs fielen fast täglich Röhren aus, erst im Dauerbetrieb ohne Aufheizen und Abkühlen nur noch etwa eine alle zwei Tage. In den 1950er-Jahren beherrschte die Röhre noch die meisten Geräte, doch wo Größe, Leistungsbedarf und Zuverlässigkeit zählten, setzte sich der Transistor durch.

Die ersten Transistoren bestanden aus Germanium. 1954 gelangen die ersten Siliziumtransistoren, im Januar Morris Tanenbaum in den Bell Laboratories, im April Gordon Teal bei Texas Instruments, der sie als Erster in Serie fertigte. Silizium setzte sich aus zwei Gründen durch, die die Gegenüberstellung zeigt:

| | Germanium | Silizium |
|---|---|---|
| Bandlücke bei 300 K | 0,66 eV | 1,12 eV |
| Eigen­leitungs­dichte bei 300 K | 2·10¹³ cm⁻³ | 10¹⁰ cm⁻³ |
| idealer Sperrstrom der Beispieldiode | 5,8·10⁻⁸ A | 1,5·10⁻¹⁴ A |
| Sperrstrom bei 1 V, mit Generation | rund 10⁻⁷ A | 2·10⁻¹¹ A |
| höchste Sperr­schicht­tempe­ratur | 90 bis 100 °C (AC128) | 150 °C (BC547) |
| Oxid | wasser­löslich, nicht beständig | fest, isolie­rend, dicht |

Der erste Grund ist der Sperrstrom. Die __Eigenleitungsdichte__ ist die Dichte der Elektronen und Löcher, die die Wärmebewegung in einem undotierten Kristall erzeugt; je größer die __Bandlücke__, die Energie, die ein Elektron zum Freiwerden braucht, desto kleiner ist sie ([Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html)). Silizium hat 2000-mal weniger solcher Ladungsträger als Germanium. Der Sperrstrom eines pn-Übergangs hat zwei Anteile ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html)): Der ideale, der __Sättigungssperrstrom__, wächst mit dem Quadrat der Eigenleitungsdichte, ein zweiter, der in der Sperrschicht selbst durch Erzeugung von Elektron-Loch-Paaren entsteht (__Generationsstrom__), mit ihrer ersten Potenz. Für eine Beispieldiode mit 0,1 mm² Fläche, beiderseits mit 10¹⁶ Fremdatomen je cm³ dotiert, ist der ideale Sperrstrom bei sonst gleichen Materialwerten aus Silizium 4 Millionen Mal kleiner als aus Germanium; gemessen bei 1 V Sperrspannung überwiegt beim Silizium der Generationsstrom, und es bleibt rund das Fünftausendfache. Siliziumtransistoren wie der BC547 sind deshalb bis 150 °C __Sperrschichttemperatur__, der Temperatur an ihren pn-Übergängen, zugelassen, Germaniumtransistoren wie der AC128 nur bis 90 bis 100 °C.

Der zweite Grund ist das Oxid. Erhitzt man Silizium in Sauerstoff, wächst auf ihm eine feste, chemisch stabile Schicht aus Siliziumdioxid (SiO₂). Sie isoliert sehr gut, schützt die empfindliche Oberfläche vor Verunreinigungen (__Passivierung__) und hält Dotierstoffe ab, so dass sie beim Dotieren als Maske dient. Germaniumdioxid dagegen löst sich in Wasser und ist bei den Temperaturen der Fertigung nicht beständig. Ohne das Siliziumoxid gäbe es weder die Planartechnik noch den MOS-Transistor.

:::frage
„Wenn Silizium so viel besser ist, warum waren die ersten Transistoren aus Germanium?“
Weil sich Germanium leichter verarbeiten ließ. Es schmilzt bei 938 °C, Silizium erst bei 1414 °C, und flüssiges Silizium greift fast jedes Tiegelmaterial an; reine Einkristalle aus Germanium ließen sich deshalb früher ziehen und reinigen. Außerdem bewegen sich Ladungsträger in Germanium schneller, Elektronen 2,8-mal, Löcher 4,2-mal so schnell wie in Silizium (Beweglichkeit 3900 bzw. 1900 gegen 1400 bzw. 450 cm²/(V s)), was für die ersten Hochfrequenztransistoren zählte. Erst Verfahren für sehr reine Siliziumkristalle machten 1954 den Wechsel möglich; den Ausschlag gaben dann Sperrstrom, Temperatur und vor allem das Oxid.
:::

## Die integrierte Schaltung

*Warum wird ein Transistor billiger, wenn man viele davon gemeinsam auf einem Chip herstellt?*

Mit Transistoren wurden die Schaltungen größer, und ein neues Problem trat hervor: Jeder Transistor, jeder Widerstand und jeder Kondensator war ein eigenes Bauteil, jede Verbindung eine Lötstelle. Der ENIAC hatte rund 5 Millionen von Hand gelötete Verbindungen, fast 300 je Röhre; jede konnte ausfallen und kostete Arbeitszeit. Mit der Zahl der Bauteile wuchsen Kosten und Ausfallwahrscheinlichkeit.

Den Gedanken, mehrere Ventile in einem Bauteil zu vereinen, gab es schon in der Röhrenzeit. Die Firma Loewe brachte 1926 die 3NF heraus, drei Triodensysteme, vier Widerstände und zwei Kondensatoren in einem Glaskolben; Widerstände und Kondensatoren steckten in eigenen, zugeschmolzenen Glasröhrchen, damit sie das Vakuum nicht verunreinigten. Der Anlass war wirtschaftlich: In Deutschland wurden für Rundfunkempfänger Abgaben je Röhrenfassung fällig, und ein Empfänger mit einer einzigen Fassung war entsprechend billiger. Die Kehrseite zeigte der Heizfaden: Brannte er durch, waren alle drei Systeme verloren. Am Empfänger OE333, der mit der 3NF arbeitete, wirkte der junge Manfred von Ardenne mit, der 1931 ein vollelektronisches Fernsehsystem vorstellte.

Die Lösung für den Festkörper kam 1958 und 1959. Jack Kilby bei Texas Instruments zeigte im September 1958 eine Schaltung, in der Transistor, Widerstände und Kondensator aus einem einzigen Germaniumplättchen geformt waren; verbunden waren sie noch durch feine Golddrähte. Robert Noyce bei Fairchild Semiconductor meldete im Juli 1959 den entscheidenden zweiten Teil zum Patent an: Die Bauelemente entstehen in einem Siliziumplättchen unter einer Oxidschicht, und die Verbindungen werden als dünne Aluminiumbahnen auf das Oxid aufgedampft. Grundlage war die __Planartechnik__, die sein Kollege Jean Hoerni 1959 entwickelt hatte. Eine solche Schaltung aus einem Stück heißt __integrierte Schaltung__ (englisch integrated circuit, IC), das Siliziumplättchen __Chip__.

:::grafik
Szene: st1/einfuehrung/01-planartechnik · Vorlage: querschnitt-prozess
**Abbildung 6:** Oben fünf Schritte der Planartechnik als kleine Querschnitte: (a) Siliziumscheibe mit gewachsener Oxidschicht, (b) Fotolack, durch eine Maske belichtet, (c) Fenster ins Oxid geätzt, (d) Dotierstoff dringt nur durch das Fenster ein, (e) Aluminium aufgedampft und zu Leiterbahnen geätzt. Unten der fertige Querschnitt mit einem npn-Transistor (Kollektor-, Basis- und Emittergebiet) und einem Widerstand nebeneinander, beide unter dem Oxid, verbunden durch eine Aluminiumbahn auf dem Oxid; dotierte Gebiete farbig, Oxid grau, Metall dunkel. Alle Bauelemente und ihre Verbindungen entstehen in denselben Schritten.
:::

Die Planartechnik besteht aus wenigen, oft wiederholten Schritten:

1. Die Siliziumscheibe, der __Wafer__ (in den 1960er-Jahren 2,5 cm, heute 30 cm Durchmesser), wird bei rund 1000 °C in Sauerstoff oxidiert.
2. Ein lichtempfindlicher Lack wird durch eine Maske belichtet, die das Muster einer ganzen Ebene trägt; nach dem Entwickeln ätzt man an den freigelegten Stellen Fenster ins Oxid. Dieses Übertragen eines Musters mit Licht heißt __Fotolithografie__.
3. Bei hoher Temperatur dringen __Dotierstoffe__ durch die Fenster ins Silizium ein, Fremdatome wie Bor, das p-Gebiete erzeugt, oder Phosphor für n-Gebiete; überall sonst hält das Oxid sie ab.
4. Neues Oxid, neue Maske, neue Fenster, bis Kollektor, Basis, Emitter und Widerstände entstanden sind.
5. Eine aufgedampfte Aluminiumschicht wird so geätzt, dass Leiterbahnen auf dem Oxid die Fenster miteinander verbinden.

Jeder Schritt bearbeitet alle Strukturen der Scheibe zugleich, gleich ob ein Chip zehn oder zehn Millionen Transistoren enthält. Die Kosten eines Chips hängen deshalb von seiner Fläche und von der Zahl der Schritte ab, kaum von der Zahl der Transistoren auf ihm, und Verbindungen kosten keine Lötstelle mehr. Darin liegt der Grund für alles Weitere: Wer die Strukturen verkleinert, bekommt mehr Transistoren zum selben Preis.

:::fehlvorstellung
„Ein Chip ist eine winzige Platine, auf der einzelne Bauteile sitzen.“ Das liegt nahe, weil Schaltbilder einzelne Bauteile zeigen. Auf dem Chip gibt es aber nichts einzusetzen: Transistoren, Widerstände und Kondensatoren sind dotierte Gebiete sowie Oxid- und Metallschichten desselben Siliziumstücks, entstanden in denselben Belichtungs- und Dotierschritten wie ihre Verbindungen. Deshalb kostet ein zusätzlicher Transistor fast nichts, solange er Platz findet; im Core 2 Duo kommen auf jeden Quadratmillimeter gut 2 Millionen Transistoren.
:::

Die ersten käuflichen integrierten Schaltungen (1961) waren bipolare Logikbausteine, zuerst eingesetzt in Raumfahrt und Militär, etwa im Navigationsrechner der Apollo-Raumschiffe. Ab Mitte der 1960er-Jahre folgten analoge Schaltungen wie die Operationsverstärker µA709 (1965) und µA741 (1968), der bis heute gefertigt wird ([Der reale Operationsverstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/realer-operationsverstaerker.html)). Eine Eigenart integrierter Bauelemente prägt seither die Schaltungstechnik: Ihre Absolutwerte schwanken von Scheibe zu Scheibe stark, bei Widerständen um 10 bis 20 %, doch zwei benachbarte, gleich gezeichnete Bauelemente durchlaufen jeden Schritt zur selben Zeit am selben Ort und gleichen sich auf etwa 0,1 %. Integrierte Schaltungen entwirft man deshalb so, dass es auf Verhältnisse gleicher Bauelemente ankommt, nicht auf Absolutwerte; Stromspiegel und Differenzverstärker beruhen darauf.

## MOSFET und CMOS: Steuern ohne Strom

*Wie steuert ein Feldeffekttransistor, und warum braucht eine CMOS-Schaltung im Ruhezustand praktisch keine Leistung?*

Die Idee, den Strom in einem Festkörper wie in der Röhre über ein elektrisches Feld zu steuern, ist älter als der Bipolartransistor: Julius Lilienfeld meldete 1925 einen solchen __Feldeffekttransistor__ (FET) zum Patent an, Oskar Heil 1934. In dieselbe Zeit fällt Walter Schottkys Theorie der Sperrschicht (1938), die erklärt, warum ein Kontakt zwischen Metall und Halbleiter gleichrichtet; nach ihm heißt die Schottky-Diode. Auch die Gruppe in den Bell Laboratories wollte ab 1945 eigentlich einen Feldeffekttransistor bauen; die Frage, warum das Feld nicht in den Halbleiter eindrang, führte Bardeen auf Elektronenzustände an der Halbleiteroberfläche, die __Oberflächenzustände__, die die vom Feld angezogenen Ladungsträger einfangen und das Feld abschirmen, und 1947 zum Spitzentransistor. Einen Feldeffekttransistor, dessen Feld ein gesperrter pn-Übergang statt einer Isolierschicht einkoppelt (__Sperrschicht-FET__), bauten George Dacey und Ian Ross 1953 in den Bell Laboratories. Die isolierte Steuerelektrode der ursprünglichen Idee machten Mohamed Atalla und Dawon Kahng 1959/60 ebendort möglich: Eine durch Erhitzen in Sauerstoff gewachsene SiO₂-Schicht verringert die Oberflächenzustände so stark, dass das Feld in den Halbleiter eindringt. Der Feldeffekttransistor ist also die ältere Idee; als MOSFET gebaut wurde er zwölf Jahre nach dem ersten Transistor.

Im __MOS-Feldeffekttransistor__ (MOSFET; MOS steht für Metall, Oxid, Halbleiter) liegt die Steuerelektrode, das __Gate__, durch eine dünne Oxidschicht isoliert über dem Silizium zwischen zwei dotierten Anschlussgebieten, __Source__ und __Drain__. Gate, Oxid und Silizium bilden einen Kondensator. Eine positive Gatespannung zieht Elektronen an die Siliziumoberfläche unter dem Gate; sie bilden einen leitenden __Kanal__ zwischen Source und Drain, und je höher die Gatespannung, desto mehr Ladung trägt der Kanal und desto größer ist der Strom. Durch das Oxid fließt kein Gleichstrom. Der MOSFET wird also wie die Triode kapazitiv gesteuert, ohne Heizung und ohne Vakuum.

Der Bipolartransistor wird anders gesteuert. Seine Basis-Emitter-Spannung senkt eine Potentialbarriere, und der Kollektorstrom wächst exponentiell mit ihr; dabei fließt zwangsläufig ein Basisstrom, beim Kleinsignaltransistor BC547C etwa ein Fünfhundertstel des Kollektorstroms. Man kann den Bipolartransistor deshalb auch als stromgesteuert beschreiben, mit einem Kollektorstrom vom 500-Fachen des Basisstroms. Beide Beschreibungen führen auf dieselben Zahlen; physikalisch primär ist die Spannung, die die Barriere einstellt ([Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html)). Die Schaltungstechnik behandelt beide Transistorarten gemeinsam als __spannungsgesteuerte Stromquellen__: Eine Steuerspannung legt den Ausgangsstrom fest, und dieser hängt nur wenig von der Spannung am Ausgang ab, so wie der Anodenstrom der Triode wegen ihres großen Innenwiderstands kaum von der Anodenspannung.

1963 zeigten Chih-Tang Sah und Frank Wanlass bei Fairchild eine Logikschaltung aus zwei einander ergänzenden MOSFETs: einem n-Kanal-Transistor (__NMOS__), dessen Kanal aus Elektronen besteht und der bei hoher Gatespannung leitet, und einem p-Kanal-Transistor (__PMOS__), dessen Kanal aus Löchern besteht und der bei niedriger Gatespannung leitet. Die Technik heißt __CMOS__, von complementary MOS. Ihre Grundschaltung ist der __Inverter__, der eine logische 1 (hohe Spannung) in eine 0 (Spannung null) umkehrt und umgekehrt.

:::grafik
Szene: st1/einfuehrung/01-cmos-inverter · Vorlage: schaltbild-zeitverlauf
**Abbildung 7:** Links der CMOS-Inverter: PMOS zwischen Versorgung $U$ und Ausgang, NMOS zwischen Ausgang und Masse, beide Gates am Eingang, am Ausgang die Kapazität $C$ der angeschlossenen Gates und Leitungen. Daneben die beiden Ruhezustände: Eingang 0 V, PMOS leitet, NMOS sperrt, Ausgang auf $U$; Eingang $U$, NMOS leitet, PMOS sperrt, Ausgang auf 0 V; in beiden ist der Weg von der Versorgung zur Masse unterbrochen. Rechts über einer gemeinsamen Zeitachse die Eingangsspannung (Rechteck), die Ausgangsspannung (umgekehrt, mit kurzen Flanken) und der Strom aus der Versorgung: schmale Spitzen nur beim Laden des Ausgangs, sonst null. Strom fließt nur beim Umschalten.
:::

**Die Akteure:**

- __$U$__: Versorgungsspannung, zugleich der Spannungshub am Ausgang; in V; 1 V als Beispielwert heutiger Logik.
- __$C$__: Kapazität des Ausgangsknotens, gebildet aus den Gates der nachfolgenden Transistoren und der Leitung dorthin; in F; 1 fF, also 10⁻¹⁵ F.
- __$f$__: wie oft je Sekunde der Knoten geladen und wieder entladen wird; in Hz; höchstens die __Taktfrequenz__, der Takt, in dem ein Prozessor seine Schritte ausführt, heute einige GHz, im Beispiel 3 GHz.
- __$P$__: mittlere Leistung, die der Knoten aus der Versorgung aufnimmt; in W.

**Das Zusammenspiel:**

**Schritt 1**: Jeder Ausgang eines __Logikgatters__, einer Schaltung, die aus den logischen Werten 0 und 1 ihrer Eingänge einen Ausgangswert bildet, treibt eine Kapazität, die Gates der folgenden Transistoren und die Leitung dorthin. Eine logische 1 heißt: Diese Kapazität ist auf die Versorgungsspannung geladen; eine 0 heißt: Sie ist entladen.

**Schritt 2**: Im CMOS-Inverter leitet je nach Eingangsspannung genau einer der beiden Transistoren, der andere sperrt. In beiden Ruhezuständen gibt es deshalb keinen leitenden Weg von der Versorgung zur Masse, und es fließt kein Strom (Abbildung 7).

**Schritt 3**: Schaltet der Ausgang von 0 auf 1, lädt der PMOS die Kapazität. Die Versorgung liefert dabei die Ladung $C U$ bei der Spannung $U$, also die Energie $C U^2$. Die Hälfte davon steckt danach in der Kapazität, die andere Hälfte wird im PMOS zu Wärme, gleich wie groß sein Widerstand ist.

**Schritt 4**: Schaltet der Ausgang zurück auf 0, entlädt der NMOS die Kapazität, und die gespeicherte Hälfte wird in ihm zu Wärme. Ein vollständiger Zyklus aus Laden und Entladen kostet also die Energie $C U^2$.

**Schritt 5**: Je öfter der Knoten umgeladen wird, desto mehr Leistung nimmt er auf: 1 fF, 1 V und 3 GHz ergeben 3 µW. Ein Chip mit 10⁸ solchen Knoten, von denen in jedem Takt jeder zehnte geladen wird, nimmt 30 W auf. Zöge jedes Gatter dagegen dauernd nur 1 µA Ruhestrom, kämen 100 W hinzu.

:::formel Formel
$$P = C\,U^2 f$$
:::

**So liest man das:** Die Leistung wächst mit der Kapazität und mit der Frequenz linear, mit der Spannung quadratisch, und im Ruhezustand ist sie null. Am stärksten wirkt deshalb die Versorgungsspannung: Von 5 V, dem Standard bis Anfang der 1990er-Jahre, auf etwa 1 V gesenkt, kostet jeder Umladevorgang 25-mal weniger Energie.

**Kurz gesagt:** Doppelte Spannung, vierfache Leistung; doppelte Frequenz oder doppelte Kapazität, doppelte Leistung.

Idee der Herleitung: Die Versorgung liefert beim Laden die Energie $C U^2$; die Hälfte bleibt in der Kapazität, die andere wird im PMOS zu Wärme, und beim Entladen wird auch die gespeicherte Hälfte im NMOS zu Wärme.

:::herleitung
**Ausgangspunkt:** die Kapazität als Verhältnis von Ladung und Spannung ([Der Kondensator und seine Kapazität](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/kondensator-und-kapazitaet.html)) und die Arbeit einer Spannungsquelle: Liefert sie die Ladung $dq$ bei der Spannung $U$, gibt sie die Energie $U\,dq$ ab.

**Annahmen:** (i) Der Ausgang wird in jeder Periode einmal vollständig von 0 auf $U$ geladen und wieder entladen. (ii) Beim Umschalten leiten nie beide Transistoren zugleich, und ein gesperrter Transistor lässt keinen Leckstrom durch. (iii) $C$ hängt nicht von der Spannung ab.

**Schritt 1**: Energie aus der Versorgung beim Laden; sie liefert die Ladung $C U$ bei der konstanten Spannung $U$:

$$\int_0^{CU} U\,dq = C\,U^2$$

**Schritt 2**: Energie in der Kapazität; ihre Spannung steigt beim Laden mit der Ladung, $u = q/C$:

$$\int_0^{CU} \frac{q}{C}\,dq = \tfrac12\,C\,U^2$$

**Schritt 3** (entscheidender Schritt): Die Differenz wird im PMOS zu Wärme; sein Widerstand kommt darin nicht vor:

$$C\,U^2 - \tfrac12\,C\,U^2 = \tfrac12\,C\,U^2$$

**Schritt 4**: Beim Entladen liefert die Versorgung nichts, die gespeicherte Energie wird im NMOS zu Wärme:

$$\tfrac12\,C\,U^2$$

**Schritt 5**: Je Periode wird $C U^2$ zu Wärme, und je Sekunde laufen $f$ Perioden ab:

$$P = \left(\tfrac12\,C\,U^2 + \tfrac12\,C\,U^2\right) f = C\,U^2 f$$

**Ergebnis:**

$$P = C\,U^2 f$$

**Woher die Faktoren kommen:** $U^2$ entsteht aus der Ladung, die mit $U$ wächst, mal der Spannung, bei der die Versorgung sie liefert (Schritt 1); $f$ zählt die Umladungen. Die beiden Hälften aus Schritt 3 und 4 ergänzen sich, deshalb bleibt kein Faktor ½.

**Proben:** Einheit: F · V² · s⁻¹ = (C/V) · V² · s⁻¹ = A · V = W. Grenzfall $f = 0$: keine Leistung, der Ruhezustand. Zahlenwert: 10⁻¹⁵ F · (1 V)² · 3·10⁹ s⁻¹ = 3 µW.

**Grenzen:** Bei langsamen Flanken leiten kurzzeitig beide Transistoren, und ein Querstrom kommt hinzu. Sehr kleine Transistoren lassen auch gesperrt einen Leckstrom durch; seit den 2000er-Jahren macht er einen merklichen Teil der Verlustleistung aus.
:::

::::beispiel Umladeleistung eines Gatterausgangs und eines Chips
**Gegeben:** Knotenkapazität $C$ = 1 fF, Versorgungsspannung $U$ = 1 V, Taktfrequenz 3 GHz (Annahmen in der Größenordnung heutiger Logik); ein Chip mit 10⁸ Knoten, von denen in jedem Takt 10 % geladen werden; zum Vergleich ein angenommener Ruhestrom von 1 µA je Gatter.

**Gesucht:** Energie je Lade-Entlade-Zyklus, Leistung eines Knotens, Leistung des Chips und die Leistung, die ein solcher Ruhestrom verursachen würde.

**Rechnung:** Energie je Zyklus und Leistung eines Knotens, der in jedem Takt umgeladen wird:

$$C\,U^2 = 10^{-15}\ \mathrm{F}\cdot(1\ \mathrm{V})^2 = 1\ \mathrm{fJ}$$

$$P = 1\ \mathrm{fJ}\cdot 3\cdot 10^9\ \mathrm{s^{-1}} = 3\ \mu\mathrm{W}$$

Chip mit 10 % geladenen Knoten je Takt:

$$P_\mathrm{Chip} = 0{,}1\cdot 10^8\cdot 3\ \mu\mathrm{W} = 30\ \mathrm{W}$$

Ruhestrom von 1 µA je Gatter bei 1 V:

$$P_\mathrm{Ruhe} = 10^8\cdot 1\ \mu\mathrm{A}\cdot 1\ \mathrm{V} = 100\ \mathrm{W}$$

**Ergebnis:** **1 fJ je Zyklus, 3 µW je Knoten, 30 W für den Chip; ein Ruhestrom von nur 1 µA je Gatter brächte 100 W dazu.**

**Einordnung:** 30 W liegen in der Größenordnung realer Prozessoren; der Core 2 Duo von 2006 ist für 65 W Verlustleistung ausgelegt, Leckströme eingeschlossen. Logikfamilien, deren Gatter in einem Zustand dauernd Strom ziehen, scheitern bei solchen Transistorzahlen an der Ruheleistung. Variation: Bei 5 V statt 1 V stiege die Umladeleistung auf das 25-Fache, 750 W.
::::

CMOS setzte sich zuerst dort durch, wo jede Ruheleistung die Batterie leert, in Digitaluhren und tragbaren Geräten. Die ersten __Mikroprozessoren__, der Rechenkern eines Computers auf einem Chip, waren der 4004 (1971) und der 8008 (1972, 3500 Transistoren, kleinste Strukturen 10 µm) in PMOS-Technik; ihre Nachfolger bauten auf NMOS-Technik, deren Gatter in einem der beiden Zustände dauernd Strom ziehen. Mit wachsender Transistorzahl wurde diese Ruheleistung untragbar, und in den 1980er-Jahren wurde CMOS zur beherrschenden Technik; heute sind fast alle digitalen Chips CMOS-Schaltungen. In den 1970er-Jahren verdrängten zudem __Halbleiterspeicher__ (RAM) die Magnetkernspeicher der Rechner.

## Das Mooresche Gesetz

*Wie schnell wächst die Zahl der Transistoren auf einem Chip, und warum gerade exponentiell?*

1965, sechs Jahre nach den ersten integrierten Schaltungen, trug Gordon Moore, damals Forschungsleiter bei Fairchild und später Mitgründer von Intel, die Zahl der Bauelemente auf den kostengünstigsten Chips über den Jahren ein, mit logarithmischer Achse. Von 1959 bis 1965 hatte sie sich jedes Jahr verdoppelt, auf etwa 64 = 2⁶; aus diesen wenigen Punkten verlängerte er die Gerade um zehn Jahre und sagte für 1975 rund 65 000 Bauelemente voraus, 2¹⁶ = 65 536. 1975 sagte er voraus, dass sich das Wachstum ab etwa 1980 auf eine Verdopplung alle zwei Jahre verlangsamen werde. Diese Erfahrungsregel heißt __Mooresches Gesetz__.

:::grafik
Szene: st1/einfuehrung/01-moore · Vorlage: kennlinie-semilog
**Abbildung 8:** Transistorzahl je Chip, logarithmisch von 1 bis 10¹¹, über den Jahren 1959 bis 2010. Punkte für zwölf Intel-Prozessoren: 4004 (1971, 2300), 8008 (1972, 3500), 8080 (1974, 4500), 8086 (1978, 29 000), 80286 (1982, 134 000), 80386 (1985, 275 000), 80486 (1989, 1,18 Mio.), Pentium (1993, 3,1 Mio.), Pentium II (1997, 7,5 Mio.), Pentium 4 (2000, 42 Mio.), Core 2 Duo (2006, 291 Mio.), Xeon 7500 mit acht Kernen (2010, 2,3 Mrd.). Dazu die Ausgleichsgerade mit 2,04 Jahren Verdopplungszeit, gestrichelt Moores Gerade von 1965 (Verdopplung jedes Jahr, von 1 im Jahr 1959 über 64 im Jahr 1965 bis 65 536 im Jahr 1975) und gepunktet eine Verdopplung alle 18 Monate ab dem 8008, die 2006 bei 2,3·10¹⁰ endet. Auf der logarithmischen Achse wird exponentielles Wachstum zur Geraden.
:::

**Die Akteure:**

- __$N(t)$__: Zahl der Transistoren auf einem Chip zur Zeit $t$, hier in Jahren gemessen; dimensionslos; 3500 im Jahr 1972 bis 2,3·10⁹ im Jahr 2010.
- __$t_0$__, __$N_0$__: ein Bezugsjahr und die Transistorzahl in diesem Jahr; etwa 1972 und 3500.
- __$T_2$__: __Verdopplungszeit__, die Zeit, in der sich die Transistorzahl verdoppelt; in Jahren; etwa 2.

**Das Zusammenspiel:**

**Schritt 1**: Die Kosten eines Chips hängen von seiner Fläche ab, kaum von der Zahl seiner Transistoren (Abschnitt *Die integrierte Schaltung*).

**Schritt 2**: Eine neue Fertigungsgeneration, ein neuer __Technologieknoten__, verkleinert alle Längen um etwa den Faktor 0,7, etwa von 180 über 130, 90 und 65 auf 45 nm. Die Fläche je Transistor sinkt dabei auf 0,7 · 0,7 = 0,49, rund die Hälfte.

**Schritt 3**: Auf derselben Fläche finden doppelt so viele Transistoren Platz, zu fast denselben Kosten; der einzelne Transistor wird halb so teuer. Zugleich lohnen sich größere Chips.

**Schritt 4**: Ein neuer Knoten kam etwa alle zwei bis drei Jahre; von 10 µm im Jahr 1972 bis 65 nm im Jahr 2006 sind es rechnerisch 14 Generationen zu je 0,7 in 34 Jahren, eine alle 2,4 Jahre. Zusammen mit den wachsenden Chipflächen verdoppelte sich die Transistorzahl je Chip etwa alle zwei Jahre.

**Schritt 5**: Gleiche Faktoren in gleichen Zeitabständen ergeben eine Exponentialfunktion. Vom 8008 (1972, 3500 Transistoren) zum Core 2 Duo (2006, 291 Millionen) wuchs die Zahl um den Faktor 83 143, das sind 16,3 Verdopplungen in 34 Jahren, eine alle 2,08 Jahre.

:::formel Formel
$$N(t) = N_0\cdot 2^{(t - t_0)/T_2}$$
:::

**So liest man das:** Der Exponent zählt, wie viele Verdopplungszeiten seit dem Bezugsjahr vergangen sind; jede bringt einen Faktor 2. Auf einer logarithmischen Achse ist das eine Gerade (Abbildung 8). Bei zwei Jahren Verdopplungszeit wächst die Zahl um 41 % je Jahr.

**Kurz gesagt:** In gleich langen Zeitspannen wächst die Zahl um denselben Faktor: alle zwei Jahre um 2, in zehn Jahren um 32, in zwanzig um 1024.

Idee der Herleitung: Aus demselben Faktor 2 in jeder Verdopplungszeit wird eine Potenz von 2, deren Exponent die Zahl der verstrichenen Verdopplungszeiten ist.

:::herleitung
**Ausgangspunkt:** die Beobachtung aus den Schritten 2 bis 4, dass sich die Transistorzahl in jeder Zeitspanne $T_2$ verdoppelt.

**Annahmen:** (i) Der Faktor 2 je Zeitspanne $T_2$ ist in jedem Jahr derselbe. (ii) Zwischen den Produktgenerationen darf man stetig interpolieren, auch für Bruchteile einer Verdopplungszeit.

**Schritt 1**: Nach $n$ ganzen Verdopplungszeiten:

$$N(t_0 + n\,T_2) = N_0\cdot 2^n$$

**Schritt 2** (entscheidender Schritt): $n$ ist die Zahl der verstrichenen Verdopplungszeiten; für ein beliebiges Jahr $t$ gilt nach Annahme (ii)

$$n = \frac{t - t_0}{T_2}$$

**Ergebnis:**

$$N(t) = N_0\cdot 2^{(t - t_0)/T_2}$$

**Woher die Faktoren kommen:** Die Basis 2 ist der Faktor je Zeitspanne, der Exponent die Zahl der Zeitspannen; $N_0$ legt fest, wo die Gerade im Diagramm liegt.

**Proben:** Im Bezugsjahr ergibt die Formel $N_0$, eine Verdopplungszeit später $2 N_0$. Der Exponent ist dimensionslos, Jahre durch Jahre. Zahlenwert: 3500 · 2^(34/2,08) = 291 Millionen.

**Grenzen:** Chips kommen in Stufen, und ein großer Serverchip hat mehr Transistoren als ein Desktopchip desselben Jahres; die Formel beschreibt den Trend, nicht jeden einzelnen Chip.
:::

Aus zwei Chips lässt sich die Verdopplungszeit bestimmen:

:::formel Formel
$$T_2 = \frac{(t_2 - t_1)\,\ln 2}{\ln\left(N_2/N_1\right)}$$
:::

**So liest man das:** Im Nenner steht der natürliche Logarithmus des Wachstumsfaktors; geteilt durch $\ln 2$ ergibt er den Zweierlogarithmus, die Zahl der Verdopplungen zwischen den beiden Chips. Die verstrichene Zeit geteilt durch diese Zahl ist die Verdopplungszeit.

**Kurz gesagt:** Die Verdopplungszeit ist die Zeitspanne geteilt durch die Anzahl der Verdopplungen, und diese ist der Zweierlogarithmus des Wachstumsfaktors.

Idee der Herleitung: Man bildet das Verhältnis der Transistorzahlen zweier Jahre, logarithmiert und löst nach $T_2$ auf.

:::herleitung
**Ausgangspunkt:** das Mooresche Gesetz (vorige Formel), ausgewertet in zwei Jahren $t_1$ und $t_2$ mit den Transistorzahlen $N_1$ und $N_2$.

**Annahmen:** (i) Beide Chips liegen auf derselben Trendgeraden.

**Schritt 1**: Verhältnis; $N_0$ und $t_0$ fallen heraus:

$$\frac{N_2}{N_1} = 2^{(t_2 - t_1)/T_2}$$

**Schritt 2** (entscheidender Schritt): Natürlicher Logarithmus beider Seiten; der Exponent wird zum Faktor:

$$\ln\frac{N_2}{N_1} = \frac{t_2 - t_1}{T_2}\,\ln 2$$

**Schritt 3**: Nach $T_2$ aufgelöst:

$$T_2 = \frac{(t_2 - t_1)\,\ln 2}{\ln\left(N_2/N_1\right)}$$

**Ergebnis:**

$$T_2 = \frac{(t_2 - t_1)\,\ln 2}{\ln\left(N_2/N_1\right)}$$

**Woher die Faktoren kommen:** $\ln 2$ stammt aus der Basis 2 des Gesetzes; mit Zehnerlogarithmen stünde dort $\log_{10} 2$, das Ergebnis bliebe gleich.

**Proben:** Einheit: Jahre. Verdopplung in genau einem Jahr: $\ln 2/\ln 2$ = 1 Jahr. Zahlenwert: 34 Jahre · 0,693/11,33 = 2,08 Jahre.

**Grenzen:** Liegt einer der beiden Chips weit neben dem Trend, verfälscht er das Ergebnis; besser ist eine Ausgleichsgerade durch viele Punkte.
:::

::::beispiel Verdopplungszeit aus Intel-Prozessoren
**Gegeben:** Intel 8008 (1972) mit 3500 Transistoren, Core 2 Duo (2006) mit 291 Millionen, Xeon 7500 (2010) mit 2,3 Milliarden (Herstellerangaben).

**Gesucht:** die Verdopplungszeit vom 8008 zum Core 2 Duo und zum Xeon.

**Rechnung:** Wachstumsfaktor und Zahl der Verdopplungen bis 2006:

$$\frac{N_2}{N_1} = \frac{291\cdot 10^6}{3500} = 83\,143, \qquad \log_2 83\,143 = 16{,}34$$

$$T_2 = \frac{34\ \mathrm{Jahre}}{16{,}34} = 2{,}08\ \mathrm{Jahre}$$

Bis 2010:

$$\frac{2{,}3\cdot 10^9}{3500} = 657\,143, \qquad T_2 = \frac{38\ \mathrm{Jahre}}{\log_2 657\,143} = \frac{38\ \mathrm{Jahre}}{19{,}33} = 1{,}97\ \mathrm{Jahre}$$

**Ergebnis:** **2,08 Jahre bzw. 1,97 Jahre, also rund zwei Jahre.**

**Einordnung:** Die Ausgleichsgerade durch alle zwölf Prozessoren der Abbildung 8 ergibt 2,04 Jahre. Genauere Daten, April 1972 bis Juli 2006, ändern das erste Ergebnis nur auf 2,10 Jahre. Moores zweite Schätzung von 1975 hat damit 35 Jahre lang gestimmt.
::::

:::fehlvorstellung
„Nach dem Mooreschen Gesetz verdoppelt sich die Zahl der Transistoren alle 18 Monate.“ Die Zahl ist weit verbreitet; sie geht auf den Intel-Manager David House zurück, der damit die Rechenleistung meinte, die durch mehr und zugleich schnellere Transistoren wächst. Moore selbst nannte für die Transistorzahl 1965 ein Jahr und 1975 zwei Jahre. Mit 18 Monaten müsste ein Prozessor des Jahres 2006, ausgehend von den 3500 Transistoren des 8008, rund 2,3·10¹⁰ Transistoren haben; der Core 2 Duo hatte 2,9·10⁸, achtzigmal weniger.
:::

Das Mooresche Gesetz ist eine Erfahrungsregel über Technik und Wirtschaft, kein Naturgesetz. Es beschreibt, wie schnell die Industrie verkleinern und daran verdienen konnte, und weil sie ihre Entwicklungspläne jahrzehntelang danach ausrichtete, zuletzt in der International Technology Roadmap for Semiconductors bis 2016, erfüllte es sich auch deshalb, weil man es erfüllen wollte. Moore selbst sagte 2005, es könne nicht ewig weitergehen: Die Atome des Siliziumgitters liegen nur 0,235 nm voneinander entfernt, und kein Transistor kann kleiner werden als einige von ihnen.

:::frage
„Was bedeutet ‚65-nm-Technologie‘? Ist dort etwas 65 nm groß?“
Ein Technologieknoten ist eine Fertigungsgeneration, benannt nach einer kennzeichnenden kleinsten Abmessung. Bis in die 1990er-Jahre entsprach der Name etwa der kürzesten Gatelänge; danach wurden die Gates kürzer als der Name, und Bezeichnungen wie „3 nm“ heutiger Fertigungen geben keine einzelne Abmessung mehr an, sondern zählen die Generationen weiter. Von Knoten zu Knoten schrumpfen die Längen um etwa 0,7, die Fläche je Transistor auf rund die Hälfte. Im Core 2 Duo (65 nm, 143 mm²) kommen auf 1 mm² gut 2 Millionen Transistoren, rechnerisch 0,49 µm² je Transistor einschließlich Verdrahtung und Speicher, ein Quadrat von 0,7 µm Kantenlänge.
:::

### Warum kleinere Transistoren schneller und sparsamer sind

*Was ändert sich an einem Transistor, wenn man ihn verkleinert, außer seinem Preis?*

Robert Dennard und seine Kollegen zeigten 1974, wie man einen MOSFET verkleinern muss, damit er sich verhält wie vorher, nur in kleinerem Maßstab: Alle Längen und alle Spannungen werden durch denselben Faktor geteilt, und die Dotierung wird um ihn erhöht, damit auch die Sperrschichten mitschrumpfen. Dann bleiben die elektrischen Feldstärken gleich, und mit ihnen die Geschwindigkeit der Ladungsträger und die Ladung je Fläche im Kanal.

:::grafik
Szene: st1/einfuehrung/01-skalierung · Vorlage: schema-tabelle
**Abbildung 9:** Links der Querschnitt eines MOSFET mit Kanallänge $L$, Oxiddicke $t_\mathrm{ox}$ und Gatespannung $U$, rechts derselbe Transistor um den Faktor $\kappa$ verkleinert, mit $L/\kappa$, $t_\mathrm{ox}/\kappa$ und $U/\kappa$; die Feldpfeile im Oxid und im Kanal sind in beiden gleich lang. Darunter die Tabelle der Faktoren für $\kappa = \sqrt2$, einen Technologieknoten: Längen, Spannung, Kapazität, Strom und Schaltzeit ×0,71, Dotierung und Frequenz ×1,41, Leistung je Transistor ×0,5, Transistoren je Fläche ×2, Leistung je Fläche ×1. Bei gleicher Feldstärke wird der kleinere Transistor schneller und sparsamer, und die Leistung je Fläche bleibt gleich.
:::

**Die Akteure:**

- __$\kappa$__: Skalierungsfaktor, größer als 1, durch den alle Längen und Spannungen geteilt werden; je Technologieknoten etwa $\sqrt2 \approx 1{,}41$, der Kehrwert von 0,7.
- __$L$__, __$W$__, __$t_\mathrm{ox}$__: Kanallänge, Kanalweite und Oxiddicke; in nm.
- __$\varepsilon$__: Permittivität des Gateoxids; sie ändert sich nicht.
- __$E$__, __$E_\mathrm{ox}$__: Feldstärke längs des Kanals und im Gateoxid; sie bleiben gleich.
- __$I$__: Strom eines eingeschalteten Transistors.
- __$\tau$__: __Schaltzeit__, die Zeit, in der ein Transistor mit dem Strom $I$ eine Kapazität $C$ um die Spannung $U$ umlädt.
- Gestrichene Größen ($\tau'$, $P'$, $W'$, $L'$) gelten nach der Verkleinerung; die Chipfläche je Transistor ist proportional zu $W L$.

:::formel Formel
$$\tau' = \frac{\tau}{\kappa}, \qquad P' = \frac{P}{\kappa^2}, \qquad \frac{P'}{W'L'} = \frac{P}{W L}$$
:::

**So liest man das:** Der verkleinerte Transistor schaltet $\kappa$-mal schneller, nimmt bei entsprechend höherer Frequenz nur ein $\kappa^2$-tel der Leistung auf, und weil auf derselben Fläche $\kappa^2$-mal so viele Transistoren Platz finden, bleibt die Leistung je Fläche gleich. Ein Chip gleicher Größe hat also doppelt so viele, 1,41-mal schnellere Transistoren bei gleicher Gesamtleistung.

**Kurz gesagt:** Verkleinert man alle Längen und Spannungen um denselben Faktor und erhöht die Dotierung um ihn, bleiben Feldstärken und Leistung je Fläche gleich, und jeder Transistor schaltet um diesen Faktor schneller.

Idee der Herleitung: Gleiche Feldstärken bedeuten gleiche Geschwindigkeit der Ladungsträger und gleiche Ladung je Fläche; daraus folgen Strom, Kapazität, Schaltzeit und mit der Umladeleistung die Leistung.

:::herleitung
**Ausgangspunkt:** die Schaltzeit aus Ladung gleich Strom mal Zeit; die Kapazität des Plattenkondensators aus Gate und Kanal; der Strom als Ladung je Fläche $\sigma$ im Kanal mal Weite mal Geschwindigkeit $v$ der Ladungsträger; die Ladung je Fläche einer Kondensatorplatte bei der Feldstärke $E_\mathrm{ox}$ im Oxid:

$$C\,U = I\,\tau$$

$$C = \frac{\varepsilon\,W L}{t_\mathrm{ox}}$$

$$I = \sigma\,W v$$

$$\sigma = \varepsilon\,E_\mathrm{ox}$$

Dazu die Umladeleistung aus dem Abschnitt *MOSFET und CMOS*.

**Annahmen:** (i) Alle Längen ($L$, $W$, $t_\mathrm{ox}$) und alle Spannungen werden durch $\kappa$ geteilt. (ii) Die Werkstoffe bleiben gleich, nur die Dotierung steigt um den Faktor $\kappa$, so dass die Sperrschichten mitschrumpfen. (iii) Die Geschwindigkeit der Ladungsträger hängt nur von der Feldstärke ab. (iv) Die Taktfrequenz steigt so, wie die Schaltzeit sinkt.

**Schritt 1**: Feldstärken, Spannung durch Länge, bleiben gleich:

$$E' = \frac{U/\kappa}{L/\kappa} = E$$

$$E_\mathrm{ox}' = \frac{U/\kappa}{t_\mathrm{ox}/\kappa} = E_\mathrm{ox}$$

**Schritt 2**: Damit bleiben $\sigma$ und $v$ gleich, und der Strom sinkt mit der Weite:

$$I' = \sigma\,\frac{W}{\kappa}\,v = \frac{I}{\kappa}$$

**Schritt 3**: Die Kapazität sinkt mit der Fläche und steigt mit dem dünneren Oxid:

$$C' = \frac{\varepsilon\,(W/\kappa)(L/\kappa)}{t_\mathrm{ox}/\kappa} = \frac{C}{\kappa}$$

**Schritt 4** (entscheidender Schritt): Schaltzeit; die umzuladende Ladung sinkt zweifach, über $C$ und über $U$, der Strom nur einfach:

$$\tau' = \frac{C'\,U'}{I'} = \frac{(C/\kappa)(U/\kappa)}{I/\kappa} = \frac{\tau}{\kappa}$$

**Schritt 5**: Leistung je Transistor bei $\kappa$-facher Frequenz:

$$P' = C'\,U'^2 f' = \frac{C}{\kappa}\cdot\frac{U^2}{\kappa^2}\cdot\kappa f = \frac{P}{\kappa^2}$$

**Schritt 6**: Fläche je Transistor und Leistung je Fläche:

$$W'L' = \frac{W}{\kappa}\cdot\frac{L}{\kappa} = \frac{W L}{\kappa^2}, \qquad \frac{P'}{W'L'} = \frac{P/\kappa^2}{W L/\kappa^2} = \frac{P}{W L}$$

**Ergebnis:**

$$\tau' = \frac{\tau}{\kappa}, \qquad P' = \frac{P}{\kappa^2}, \qquad \frac{P'}{W'L'} = \frac{P}{W L}$$

**Woher die Faktoren kommen:** Der Gewinn an Geschwindigkeit stammt aus Schritt 4: Die umzuladende Ladung $C U$ sinkt mit $\kappa^2$, der Strom nur mit $\kappa$. Die Leistung je Transistor sinkt mit $\kappa^2$, weil die Energie je Umladung $C U^2$ mit $\kappa^3$ sinkt und die Frequenz mit $\kappa$ steigt.

**Proben:** Mit dem Faktor 1 bleibt alles unverändert. Mit $\sqrt2$: Schaltzeit ×0,707, Leistung je Transistor ×0,5, Transistoren je Fläche ×2, Leistung je Fläche ×1. Einheiten: Alle Gleichungen sind Verhältnisse gleichartiger Größen.

**Grenzen:** Für die Spannung galt Annahme (i) nur etwa von Anfang der 1990er- bis Mitte der 2000er-Jahre: Davor blieb sie bei 5 V, danach hätte eine weitere Absenkung die Leckströme stark erhöht. Außerdem lassen Oxide von wenigen Atomlagen Elektronen durchtunneln. Ohne Spannungsskalierung steigt die Leistung je Fläche, wenn man den Takt erhöht.
:::

::::beispiel Ein Technologieknoten nach den Skalierungsregeln
**Gegeben:** ein Logikgatter mit $C$ = 2 fF, $U$ = 1,4 V und 1 GHz; Verkleinerung um einen Knoten, $\kappa = \sqrt2$.

**Gesucht:** Kapazität, Spannung, Frequenz und Leistung nach der Verkleinerung sowie die Leistung je Fläche.

**Rechnung:** Kapazität und Spannung durch $\kappa$, Frequenz mal $\kappa$:

$$C' = \frac{2\ \mathrm{fF}}{1{,}414} = 1{,}41\ \mathrm{fF}, \qquad U' = \frac{1{,}4\ \mathrm{V}}{1{,}414} = 0{,}99\ \mathrm{V}, \qquad f' = 1{,}41\ \mathrm{GHz}$$

Leistung vorher und nachher:

$$P = 2\ \mathrm{fF}\cdot(1{,}4\ \mathrm{V})^2\cdot 1\ \mathrm{GHz} = 3{,}92\ \mu\mathrm{W}$$

$$P' = 1{,}41\ \mathrm{fF}\cdot(0{,}99\ \mathrm{V})^2\cdot 1{,}41\ \mathrm{GHz} = 1{,}96\ \mu\mathrm{W}$$

**Ergebnis:** **Das Gatter schaltet mit 1,41 GHz statt 1 GHz und braucht 1,96 µW statt 3,92 µW; auf derselben Fläche sitzen doppelt so viele Gatter, die zusammen genauso viel Leistung aufnehmen wie vorher.**

**Einordnung:** So sieht die ideale Verkleinerung aus. Tatsächlich blieb die Versorgungsspannung bis Anfang der 1990er-Jahre bei 5 V, und die Leistung je Fläche stieg; die Leistung von Prozessoren wuchs von wenigen Watt bis Mitte der 2000er-Jahre auf rund 100 W, und die Kühlung musste mitwachsen.
::::

:::frage
„Warum sind die Taktfrequenzen von Prozessoren seit Mitte der 2000er-Jahre kaum noch gestiegen?“
Weil sich die Spannung nicht mehr mitverkleinern ließ. Ein MOSFET sperrt nie vollständig: Unterhalb seiner __Schwellspannung__, der Gatespannung, ab der sein Kanal leitet, sinkt sein Strom bei Raumtemperatur je 60 mV weniger Gatespannung höchstens um den Faktor 10, denn die Ladungsträger überwinden die Barriere im Kanal nach derselben Boltzmann-Statistik wie in einer Diode ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html)). Damit ein gesperrter Transistor viele Zehnerpotenzen weniger Strom führt als ein leitender, braucht er deshalb eine Schwellspannung von einigen hundert Millivolt und eine Versorgungsspannung deutlich darüber; jede weitere Absenkung hätte die Leckströme um Zehnerpotenzen erhöht, und die Versorgungsspannung blieb bei etwa 1 V stehen. Ohne kleinere Spannung steigt nach der Umladeleistung die Leistung je Fläche mit dem Takt, und die Kühlung setzt die Grenze: Der Core 2 Duo war 2006 bei 2,4 GHz für 65 W auf 143 mm² ausgelegt, 45 W/cm², fast sechsmal so viel wie eine Kochplatte mit 2 kW auf 18 cm Durchmesser. Von 1990 bis 2004 stieg der Takt von Desktop-Prozessoren von rund 33 MHz auf 3,8 GHz, auf mehr als das Hundertfache, in den zwanzig Jahren danach nur noch auf etwa 6 GHz im kurzzeitigen Spitzentakt. Seither wächst die Rechenleistung über mehrere Rechenkerne je Chip; der Core 2 Duo hatte zwei, der Xeon 7500 acht.
:::

## Die Funktechnik auf dem Chip

*Warum mussten Funkschaltungen auf einen Chip, und was machte das möglich?*

Wie zu Beginn der Röhrenzeit trieb die Nachrichtentechnik auch in den 1990er- und 2000er-Jahren die Schaltungstechnik an. Ein Mobiltelefon für viele Millionen Menschen musste billig werden, und billig wird Elektronik durch Integration, im Empfänger wie im Sender. Zu Beginn der 1990er-Jahre waren dafür unter den Siliziumtechniken nur integrierte Bipolartransistoren schnell genug, für Frequenzen bis etwa 2 GHz. Daraus entstand die __BiCMOS__-Technik, die Bipolartransistoren und CMOS auf einem Chip vereint, und mit __Silizium-Germanium__ (SiGe) eine noch schnellere Variante: Germanium in der Basis des Bipolartransistors verkleinert dort die Bandlücke zum Kollektor hin, und das entstehende Feld treibt die Elektronen schneller durch die Basis.

:::grafik
Szene: st1/einfuehrung/01-direktumsetzer · Vorlage: blockschaltbild
**Abbildung 10:** Oben ein Überlagerungsempfänger mit dem Chip als Rahmen: Spiegelfrequenzfilter und Zwischenfrequenzfilter (keramisch oder Oberflächenwellenfilter) liegen außerhalb des Rahmens als eigene Bauteile. Unten ein Direktumsetzer: Antenne, rauscharmer Verstärker, zwei Mischer, gespeist vom Oszillator bei der Empfangsfrequenz, einmal direkt und einmal um 90° verschoben (I- und Q-Zweig), danach je ein integrierter Tiefpass, ein Analog-Digital-Umsetzer und die digitale Verarbeitung im Basisband, alles innerhalb des Rahmens; außerhalb bleiben nur Antenne, Bandfilter und Quarz. Der Direktumsetzer kommt ohne Zwischenfrequenzfilter aus und passt bis auf diese Teile auf den Chip.
:::

Der Überlagerungsempfänger braucht für die Zwischenfrequenz ein sehr steiles Filter, meist ein keramisches oder ein Oberflächenwellenfilter, und ein Vorfilter gegen die Spiegelfrequenz; solche Filter lassen sich nicht auf einem Siliziumchip herstellen. Der __Direktumsetzer__ wählt die Oszillatorfrequenz gleich der Empfangsfrequenz. Die Zwischenfrequenz ist dann null, das Signal liegt nach dem Mischer direkt im Bereich niedriger Frequenzen, dem __Basisband__, und den Kanal wählt ein Tiefpass aus Widerständen, Kondensatoren und Verstärkern, der sich integrieren lässt. Weil beim Mischen auf null die Anteile oberhalb und unterhalb der Trägerfrequenz übereinanderfallen, mischt man zweimal, mit zwei um eine Viertelperiode (90°) gegeneinander verschobenen Oszillatorsignalen, und trennt die Anteile danach rechnerisch. Das gelingt nur, wenn die beiden Zweige sich in Verstärkung und Phase sehr genau gleichen; zwei gleich gezeichnete Zweige auf demselben Chip gleichen sich ohne Abgleich auf etwa 1 % in der Verstärkung und 1° in der Phase, aus demselben Grund wie die Bauelementpaare im Abschnitt *Die integrierte Schaltung*, und das genügt hier. Die gut beherrschten Fertigungsschwankungen integrierter Technik machten den Direktumsetzer damit erst brauchbar.

Den letzten Schritt brachte die Verkleinerung des MOSFET. Ein Transistor verstärkt nur bis zu einer Grenze: Die __Transitfrequenz__ ist die Frequenz, bei der seine Stromverstärkung auf 1 gefallen ist, und sie steigt, je kürzer die Strecke ist, die die Ladungsträger zurücklegen müssen. Bei hohen Feldstärken erreichen Elektronen in Silizium eine Höchstgeschwindigkeit von rund 10⁷ cm/s und durchqueren einen 180 nm langen Kanal in 1,8 ps. NMOS-Transistoren des 180-nm-Knotens (Ende der 1990er-Jahre), deren Kanal höchstens so lang ist, erreichen Transitfrequenzen von 50 bis 70 GHz, das 25- bis 35-Fache der Mobilfunkfrequenzen um 2 GHz. Damit wurden Hochfrequenzschaltungen in reiner CMOS-Technik wirtschaftlich.

Nun ließen sich ganze Funksysteme auf einem Chip unterbringen, der Hochfrequenzteil, der Analogteil mit Filtern, Oszillatoren und Analog-Digital-Umsetzern und die digitale Verarbeitung im Basisband (Demodulation, Fehlerkorrektur, Ablauf des Funkprotokolls). Ein solcher Chip heißt __System-on-Chip__ (SoC). Um 2000/2001 kamen die ersten Bluetooth-Chips dieser Art in CMOS-Technik auf den Markt, etwa der BlueCore von CSR, danach Chips für den amerikanischen Mobilfunkstandard CDMA2000 und Mitte der 2000er-Jahre Ein-Chip-Lösungen für GSM-Telefone.

:::frage
„Wozu braucht ein Prozessor aus Logikgattern Schaltungstechnik auf Transistorebene?“
Weil an seinen Rändern analoge Aufgaben liegen. Den Takt von einigen Gigahertz erzeugt eine __Phasenregelschleife__ (englisch phase-locked loop, PLL): ein Oszillator, dessen Frequenz sich mit einer Spannung verstellen lässt und den eine Regelung über Rückkopplung an die vervielfachte Frequenz eines Quarzoszillators bindet. Bei 3 GHz dauert eine Periode 333 ps; wie genau die Flanken kommen, bestimmen Rauschen und Gleichlauf einzelner Transistoren. Ebenso müssen Bustreiber Signale mit Milliarden Bit je Sekunde über Leitungen von einigen Zentimetern Länge treiben, auf denen sich Signale als Wellen ausbreiten; Pegel, Flankensteilheit und Leitungsabschluss sind dort analoge Größen. Solche Blöcke entwirft man Transistor für Transistor.
:::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Triode | ein Feld steuert den Elektronenstrom aus der Kathode, das Gitter liefert fast keine Leistung |
| Rückkopplung und Überlagerung | was man aus gesteuerten Ventilen baut: Oszillator, Mischer, Empfänger mit fester Zwischenfrequenz |
| Transistor und Silizium | dasselbe Ventil ohne Heizung, im Festkörper, mit kleinem Sperrstrom und stabilem Oxid |
| Planartechnik und IC | Ventile und Verbindungen entstehen in denselben Schritten, die Kosten hängen an der Fläche |
| MOSFET und CMOS | Steuerung über ein Feld wie bei der Röhre; Ventilpaare ohne Ruhestrom |
| Mooresches Gesetz | gemeinsames Herstellen und Verkleinern: doppelt so viele Ventile je Chip etwa alle zwei Jahre |
| Skalierung | kleinere Ventile schalten schneller und brauchen weniger Energie je Schaltvorgang |
| Funk-SoC | gleich gezeichnete Ventile auf einem Chip gleichen sich genau, ganze Funksysteme passen auf einen Chip |

Jede elektronische Schaltung beruht auf einem gesteuerten Ventil, in dem eine kleine Steuergröße einen großen Strom aus einer Versorgung steuert; die Geschichte der Schaltungstechnik ist die Geschichte, dieses Ventil kleiner, sparsamer und schneller zu machen, bis Milliarden davon gemeinsam auf einem Siliziumchip entstehen und jedes einzelne fast nichts mehr kostet.

## Bedeutung und Ausblick

Wer heute eine Schaltung entwirft, beschreibt integrierte MOS- und Bipolartransistoren als spannungsgesteuerte Stromquellen mit Steilheit und Ausgangswiderstand, mit denselben Begriffen, mit denen Barkhausen die Triode beschrieb. Bei mehr als zwei Transistoren werden geschlossene Formeln so lang, dass sie kaum noch etwas aussagen; die Schaltungstechnik lebt deshalb von Näherungen und zerlegt große Schaltpläne in Grundschaltungen, deren Verhalten man kennt. Die Röhre ist nicht verschwunden: Wanderfeldröhren verstärken in Nachrichtensatelliten, Magnetrons erzeugen die Mikrowellen im Haushaltsgerät.

Das Bild des gesteuerten Ventils sagt, was ein Transistor tut, aber nicht, wie schnell er reagiert; das bestimmen seine Kapazitäten. Und seine Kennlinie ist gekrümmt: Das nächste Thema beginnt deshalb bei nichtlinearen Bauelementen, ihrem Arbeitspunkt und der Linearisierung um ihn herum.

:::kern
- Ein aktives Bauelement ist ein gesteuertes Ventil: Eine kleine Steuergröße steuert einen großen Strom, die Energie liefert die Versorgung.
- Triode und MOSFET werden kapazitiv über ein Feld gesteuert, ohne Gleichstrom am Steueranschluss; der Bipolartransistor braucht einen kleinen Basisstrom. Die Schaltungstechnik behandelt alle als spannungsgesteuerte Stromquellen.
- Rückkopplung: $A = v_u/(1 - k v_u)$; bei $k v_u = 1$ schwingt die Anordnung, Gegenkopplung macht die Verstärkung klein und stabil.
- Überlagerung: Das Produkt zweier Schwingungen enthält Differenz- und Summenfrequenz; die Zwischenfrequenz ist $f_\mathrm{LO} - f_E$.
- Silizium siegte durch sein stabiles Oxid und den kleinen Sperrstrom; die Planartechnik fertigt alle Bauelemente und Verbindungen eines Chips gemeinsam, die Kosten hängen an der Fläche.
- CMOS braucht im Ruhezustand fast keine Leistung, beim Umschalten $P = C U^2 f$.
- Mooresches Gesetz: Die Transistorzahl je Chip verdoppelt sich etwa alle zwei Jahre (1965 geschätzt: jedes Jahr); eine Erfahrungsregel, kein Naturgesetz.
- Kleinere Transistoren schalten schneller und sparsamer; seit Mitte der 2000er-Jahre begrenzt die Leistung je Fläche den Takt.
:::

:::quiz
F: Warum kostet die Steuerung einer Triode fast keine Leistung, obwohl sie einen Strom von Milliampere steuert?
A: Das Gitter ist negativ gegen die Kathode; die Elektronen werden abgestoßen, fliegen zwischen den Drähten hindurch, und kein Gleichstrom fließt zum Gitter. Es verändert nur das Feld vor der Kathode wie die Elektrode eines Kondensators; die Leistung des Ausgangssignals liefert die Anodenspannungsquelle.
F: Warum wirkt eine Änderung der Gitterspannung bei der ECC83 hundertmal stärker als eine gleich große Änderung der Anodenspannung?
A: Das Gitter sitzt dicht vor der Kathode und schirmt die Anode weitgehend ab; die Anode wirkt nur mit dem Durchgriff D = 0,01 durch die Maschen. 1 V mehr am Gitter gleicht 100 V weniger an der Anode aus.
F: Wie groß ist die Spannungsverstärkung einer ECC83-Stufe mit S = 1,6 mA/V, R_i = 62,5 kΩ und 100 kΩ Arbeitswiderstand?
A: v_u = −S (R_i ∥ R_a) = −1,6 mA/V · 38,46 kΩ = −61,5; 0,1 V Eingangsamplitude ergeben 6,15 V am Ausgang.
F: Warum schwingt ein mitgekoppelter Verstärker bei der Schleifenverstärkung $k v_u = 1$, obwohl kein Eingangssignal anliegt?
A: Nach $A = v_u/(1 - k v_u)$ wird der Nenner null; eine Ausgangsspannung erhält sich selbst. Ist die Schleifenverstärkung etwas größer als 1, wächst das Rauschen von Umlauf zu Umlauf an, bis die Krümmung der Kennlinie sie auf genau 1 senkt; der Schwingkreis legt die Frequenz fest.
F: Warum arbeiten UKW-Empfänger mit 10,7 MHz Zwischenfrequenz?
A: Auf einer festen Zwischenfrequenz genügt ein einmal abgeglichenes Filter mit der Güte 53,5 statt 500 bei 100 MHz; und der Spiegel liegt 21,4 MHz neben dem Sender, mehr als das UKW-Band breit ist (20,5 MHz), so dass kein UKW-Sender auf den Spiegel eines anderen fällt.
F: Warum setzte sich Silizium gegen Germanium durch?
A: Sein Oxid SiO₂ ist fest, isoliert und maskiert beim Dotieren; darauf beruhen Planartechnik und MOSFET. Außerdem ist seine Eigenleitungsdichte 2000-mal kleiner, der ideale Sperrstrom deshalb 4 Millionen Mal und der gemessene rund 5000-mal kleiner, und Siliziumtransistoren arbeiten bis 150 °C statt 90 bis 100 °C.
F: Warum sinken die Kosten je Transistor, wenn man die Strukturen verkleinert?
A: Die Planartechnik bearbeitet alle Strukturen einer Scheibe gleichzeitig; die Kosten hängen an der Fläche. Ein Knoten mit 0,7-fachen Längen halbiert die Fläche je Transistor, auf derselben Fläche sitzen doppelt so viele Transistoren zu fast denselben Kosten.
F: Stimmt es, dass eine CMOS-Schaltung keine Leistung braucht, weil immer ein Transistor sperrt?
A: Nein. Im Ruhezustand fließt fast kein Strom, aber jeder Lade-Entlade-Zyklus kostet C U², also P = C U² f: 1 fF, 1 V und 3 GHz ergeben 3 µW je Knoten, 10⁸ Knoten mit 10 % Umladung je Takt 30 W.
F: Stimmt es, dass Moore eine Verdopplung der Transistorzahl alle 18 Monate vorhergesagt hat?
A: Nein. Moore nannte 1965 ein Jahr und 1975 zwei Jahre; die 18 Monate gehen auf David House zurück, der die Rechenleistung meinte. Mit 18 Monaten hätte ein Prozessor 2006 rund 2,3·10¹⁰ Transistoren, achtzigmal mehr als der Core 2 Duo.
F: Der 8008 von 1972 hatte 3500 Transistoren, der Core 2 Duo von 2006 291 Millionen. Welche Verdopplungszeit folgt daraus?
A: Faktor 83 143, log₂ 83 143 = 16,34 Verdopplungen; 34 Jahre / 16,34 = 2,08 Jahre.
:::

