---
title: Von der Röhre zum integrierten Schaltkreis
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / Einführung
order: 33010100
summary: Wie aus der Elektronenröhre über den Transistor die integrierte Schaltung wurde und warum jeder Schritt nötig war, vom gesteuerten Ventil als Grundprinzip jedes Verstärkers über Rückkopplung, Überlagerungsempfänger, Silizium und Planartechnik bis zu CMOS und dem Mooreschen Gesetz. Kompakte Fassung mit hergeleiteter Verstärkung einer Röhrenstufe, Rückkopplungsformel, Mischprodukt, Umladeleistung und Verdopplungszeit; die ausführliche enthält zusätzlich Barkhausen-Formel, Spiegelfrequenz, Skalierungsregeln, Direktumsetzer und weitere Hintergründe.
tags: Elektronenröhre, Transistor, integrierte Schaltung, Mooresches Gesetz, CMOS
stil: 3
fassung: kompakt
---

## Worum es geht

Ein Funksignal kommt oft mit wenigen Mikrovolt an der Antenne an, und ein Prozessor schaltet milliardenmal je Sekunde um. Beides braucht ein Bauelement, in dem eine kleine Steuergröße einen großen Strom aus einer Versorgung steuert. Das Thema folgt aus einem Prinzip:

**Jede elektronische Schaltung beruht auf einem gesteuerten Ventil, in dem eine kleine Steuergröße einen großen Strom aus einer Versorgung steuert; die Geschichte der Schaltungstechnik ist die Geschichte, dieses Ventil kleiner, sparsamer und schneller zu machen, bis Milliarden davon gemeinsam auf einem Siliziumchip entstehen und jedes einzelne fast nichts mehr kostet.**

Vorausgesetzt werden Schulphysik und Schulmathematik (Potenzen, Logarithmus, Additionstheoreme). Halbleiter, Diode, Bipolartransistor und Operationsverstärker haben eigene Artikel, die an den passenden Stellen verlinkt sind. Auf diesem Thema bauen alle weiteren Themen der Schaltungstechnik auf.

:::grafik
Szene: st1/einfuehrung/01-drei-ventile · Vorlage: schaltbild-vergleich
**Abbildung 1:** Drei Generationen des gesteuerten Ventils über einer Zeitachse von 1906 bis 2010. Links die Triode (ab 1906/1910) mit geheizter Kathode, Gitter und Anode, in der Mitte der Bipolartransistor (ab 1947/48) mit Basis, Kollektor und Emitter, rechts der MOS-Feldeffekttransistor (ab 1959/60) mit Gate, Drain und Source. Jedes Ventil liegt mit einem Arbeitswiderstand an der Versorgungsspannung; die Steuergröße (Gitter-, Basis-Emitter- bzw. Gate-Source-Spannung) ist blau, der gesteuerte Strom orange markiert. Unter jedem Ventil die Steuerart (Feld ohne Gleichstrom, Spannung mit kleinem Basisstrom, Feld ohne Gleichstrom) und die typische Größe (Glaskolben einige Zentimeter, Gehäuse einige Millimeter, Technologieknoten 65 nm mit rund 35 nm Gatelänge im Jahr 2006). In allen drei Generationen steuert eine kleine Größe am Steueranschluss einen großen Strom aus der Versorgung; geändert haben sich Größe, Leistungsbedarf und Herstellung.
:::

## Das gesteuerte Ventil: die Elektronenröhre

*Wie kann eine kleine Spannung einen großen Strom steuern, und woher kommt die Leistung des verstärkten Signals?*

1906/07 baute Lee de Forest das Audion, eine Röhre mit einem Gitter als dritter Elektrode zwischen Kathode und Anode; unabhängig davon steuerten Robert von Lieben, Eugen Reisz und Siegmund Strauß ab 1910 ihre Röhre ebenfalls über ein Gitter. Eine solche Röhre heißt __Triode__. Zuverlässig wurde erst die gasfreie __Hochvakuumröhre__, ab 1913 entwickelt und ab 1916 bei Siemens & Halske in Serie gefertigt.

:::grafik
Szene: st1/einfuehrung/01-triode-aufbau · Vorlage: querschnitt
**Abbildung 2:** Schnitt durch eine Triode, schematisch und nicht maßstäblich. Links die vom Heizfaden auf rund 1000 K erwärmte Kathode, davor eine Wolke ausgetretener Elektronen (Raumladung, blau), dicht davor das Gitter aus dünnen Drähten, rechts die Anode. Darunter der Potentialverlauf von der Kathode zur Anode bei 250 V Anodenspannung für die Gitterspannungen −2 V und −1 V: Vor der Kathode liegt ein flaches Potentialminimum, das die Elektronenwolke selbst erzeugt und das nur Elektronen mit genügend Austrittsenergie überwinden; die weniger negative Gitterspannung hebt das Potential vor der Kathode an und lässt mehr Elektronen zur Anode. Das Gitter steuert das Potential vor der Kathode und damit den Anodenstrom; weil es negativ ist, landet praktisch kein Elektron auf ihm.
:::

Die Zahlen gelten für eines der beiden gleichen Triodensysteme der Doppeltriode ECC83 (amerikanisch 12AX7), die bis heute in Gitarrenverstärkern steckt, im __Arbeitspunkt__, dem Betriebszustand ohne Signal.

**Die Akteure:**

- __Kathode__: Metallröhrchen mit Oxidschicht, von einem Heizfaden auf rund 1000 K (gut 700 °C) erwärmt, so dass Elektronen austreten (__Glühemission__); Bezugspunkt aller Spannungen.
- __$U_g$__: Gitterspannung gegen die Kathode; in V; −2 V. Sie steuert.
- __$U_a$__: Anodenspannung; in V; 250 V. Die Anode fängt die Elektronen auf, ihre Spannungsquelle liefert die Energie.
- __$I_a$__: Anodenstrom; in mA; 1,2 mA. Er fließt in technischer Stromrichtung von der Anode zur Kathode, die Elektronen fliegen umgekehrt. Er ist der gesteuerte Strom.

**Das Zusammenspiel:**

**Schritt 1**: Die geheizte Kathode gibt laufend Elektronen ab. Sie bilden vor ihr eine negativ geladene Wolke, die nachfolgende Elektronen zurückstößt.

**Schritt 2**: Die positive Anode zieht Elektronen aus der Wolke ab. Wie viele, begrenzt die Wolke selbst, die __Raumladung__: Je höher die Elektroden das Potential vor der Kathode anheben, desto mehr Elektronen gelangen zur Anode.

**Schritt 3**: Das Gitter sitzt dicht vor der Kathode und schirmt die weiter entfernte Anode weitgehend ab. Seine Spannung wirkt deshalb viel stärker auf das Potential vor der Kathode, bei der ECC83 hundertmal stärker als die Anodenspannung: Bei 150 V und −1 V fließen dieselben 1,2 mA wie bei 250 V und −2 V. Dieser Faktor heißt __Verstärkungsfaktor__ $\mu$, hier 100.

**Schritt 4**: Das negative Gitter stößt die Elektronen ab; sie fliegen zwischen seinen Drähten hindurch, praktisch keines landet darauf, und durch den Steueranschluss fließt kein Gleichstrom. Gitter und Kathode wirken wie ein kleiner Kondensator, dessen Ladung die Gitterspannung verschiebt. Diese Steuerung über ein Feld heißt __kapazitiv__; sie kostet fast keine Leistung.

**Schritt 5**: Die Leistung des verstärkten Signals stammt aus der Anodenspannungsquelle. Bei fester Anodenspannung ändern 0,1 V mehr am Gitter den Anodenstrom um 0,16 mA. Mit einem __Arbeitswiderstand__ von 100 kΩ zwischen Anode und Versorgung entsteht an der Anode eine Spannungsänderung von 6,15 V, das 61,5-Fache der Eingangsänderung, mit umgekehrtem Vorzeichen. Röhre und Arbeitswiderstand bilden eine __Verstärkerstufe__.

:::analogie
Eine Triode arbeitet wie ein Ventil in einer Wasserleitung unter Druck: Die Leitung liefert Wasser und Druck, das Ventil bestimmt nur, wie viel fließt. Im britischen Englisch heißt die Elektronenröhre bis heute *valve*.

| Im Vergleich | In der Triode |
|---|---|
| Druck der Leitung | Anodenspannung aus der Versorgung |
| Stellung des Ventils | Gitterspannung |
| Durchfluss | Anodenstrom |

**Wo der Vergleich nicht stimmt:** Ein Ventilgriff verlangt Kraft und Arbeit, das negative Gitter fast keine Leistung. Und der Durchfluss eines Ventils hängt stark vom Leitungsdruck ab, der Anodenstrom von der Anodenspannung hundertmal schwächer als von der Gitterspannung.
:::

:::fehlvorstellung
„Ein Verstärker vervielfacht Energie.“ Das liegt nahe, weil am Ausgang ein größeres Signal erscheint als am Eingang. Die zusätzliche Leistung stammt aber aus der Versorgung; der Verstärker formt nur ihren Fluss nach dem Muster des Eingangssignals. Die ECC83-Stufe aus Schritt 5 gibt bei 6,15 V Amplitude 0,19 mW Signalleistung ab und nimmt dafür 0,44 W aus der Anodenspannungsquelle und 0,945 W für die Heizung auf; fast alles davon wird Wärme.
:::

:::frage
„Warum muss die Kathode überhaupt geheizt werden?“
Um das Metall zu verlassen, muss ein Elektron eine Energieschwelle überwinden, die __Austrittsarbeit__, bei den Oxidkathoden von Empfängerröhren etwa 1 eV. Welcher Anteil der Elektronen genug Wärmeenergie dafür hat, gibt der __Boltzmann-Faktor__ an, die Exponentialfunktion von minus Schwelle durch thermische Energie: bei 300 K 1,6·10⁻¹⁷, bei 1000 K 9·10⁻⁶. Der austretende Strom wächst dadurch um mehr als das 10¹¹-Fache; erst bei Glühtemperatur treten genug Elektronen aus. Die Heizung kostet bei der ECC83 0,945 W je System, gut dreimal so viel wie die 0,3 W, die im Arbeitspunkt an der Anode umgesetzt werden; ein Transistor braucht sie nicht.
:::

Die 0,16 mA je 0,1 V Gitterspannung aus Schritt 5 und die viel schwächere Wirkung der Anodenspannung, 0,1 mA je 6,25 V, beschreibt man mit zwei Kenngrößen aus dem Datenblatt jeder Röhre; aus ihnen folgt die Verstärkung von 61,5.

**Die Akteure:**

- __$S$__: __Steilheit__, die Stromänderung je Volt Gitterspannung bei fester Anodenspannung; in mA/V; 1,6 mA/V. Sie misst, wie stark das Gitter steuert.
- __$R_i$__: __Innenwiderstand__, die Anodenspannungsänderung je Milliampere Strom bei fester Gitterspannung; in kΩ; 62,5 kΩ. Je größer er ist, desto weniger hängt der Strom von der Anodenspannung ab.
- __$R_a$__: Arbeitswiderstand zwischen Anode und Versorgung; 100 kΩ.
- __$u_g$__, __$u_a$__, __$i_a$__: kleine Änderungen von Gitterspannung, Anodenspannung und Anodenstrom gegenüber dem Arbeitspunkt; Kleinbuchstaben kennzeichnen Änderungen.
- __$v_u$__: Spannungsverstärkung der Stufe, das Verhältnis der Änderungen von Anoden- und Gitterspannung; dimensionslos.

Formal sind beide Kenngrößen Steigungen der __Kennlinie__, der Kurve des Anodenstroms über einer der beiden Spannungen, bei festgehaltener zweiter Spannung, also partielle Ableitungen. Mit ihnen ersetzt man die Kennlinie für kleine Änderungen durch ihre Tangente:

:::formel Definition
$$S = \left.\frac{\partial I_a}{\partial U_g}\right|_{U_a}$$

$$\frac{1}{R_i} = \left.\frac{\partial I_a}{\partial U_a}\right|_{U_g}$$
:::

Damit hat die Verstärkerstufe die Spannungsverstärkung:

:::formel Formel
$$v_u = \frac{u_a}{u_g} = -S\,\left(R_i \parallel R_a\right) = -S\,\frac{R_i\,R_a}{R_i + R_a}$$
:::

**So liest man das:** Die Steilheit setzt die Gitterspannung in einen Strom um, der an der Parallelschaltung aus Innen- und Arbeitswiderstand die Ausgangsspannung erzeugt. Das Minuszeichen heißt: Steigt die Gitterspannung, sinkt die Anodenspannung. Ein größerer Arbeitswiderstand vergrößert die Verstärkung, aber nie über $S R_i$ hinaus.

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

Versorgung, damit an der Anode 250 V liegen:

$$U_B = U_a + R_a\,I_a = 250\ \mathrm{V} + 100\ \mathrm{k\Omega}\cdot 1{,}2\ \mathrm{mA} = 370\ \mathrm{V}$$

Leistungen aus der Versorgung, im Signal und in der Heizung je System:

$$P_B = 370\ \mathrm{V}\cdot 1{,}2\ \mathrm{mA} = 0{,}444\ \mathrm{W}$$

$$P_\mathrm{sig} = \frac{\hat u_a^2}{2\,R_a} = \frac{(6{,}15\ \mathrm{V})^2}{2\cdot 100\ \mathrm{k\Omega}} = 0{,}19\ \mathrm{mW}$$

$$P_\mathrm{H} = \frac{6{,}3\ \mathrm{V}\cdot 0{,}3\ \mathrm{A}}{2} = 0{,}945\ \mathrm{W}$$

**Ergebnis:** **$v_u$ = −61,5; 6,15 V Ausgangsamplitude; $U_B$ = 370 V; 0,19 mW Signalleistung bei 1,39 W Gesamtaufnahme.**

**Einordnung:** Das Ausgangssignal trägt etwa ein Siebentausendstel der aufgenommenen Leistung; Verstärken heißt, mit einem kleinen Signal einen großen Energiefluss zu formen. Mit unbegrenzt großem Arbeitswiderstand ginge die Verstärkung gegen −100.
::::

## Rückkopplung: der Verstärker als Sender

*Wie erzeugt ein Verstärker selbst eine Schwingung?*

Ein Funksender braucht einen __Oszillator__, eine Schaltung, die selbst eine ungedämpfte Schwingung konstanter Frequenz erzeugt. Alexander Meißner baute einen solchen 1913 bei Telefunken mit einer Liebenröhre: Er führte einen Teil der Ausgangsspannung der Röhrenstufe über eine Spule auf das Gitter zurück. Dieses Prinzip, die __Rückkopplung__, fanden um dieselbe Zeit auch andere, darunter Edwin Armstrong.

:::grafik
Szene: st1/einfuehrung/01-rueckkopplung · Vorlage: blockschaltbild-graph
**Abbildung 3:** Links das Signalflussbild: Eingangsspannung $u_1$, Summierstelle, Verstärker $v_u$, Ausgangsspannung $u_2$, Rückführung $k$ zurück zur Summierstelle. Mitte das Verhältnis $A/v_u$ der Verstärkungen mit und ohne Rückführung über der Schleifenverstärkung $k v_u$ von −2 bis 1: links der Null (Gegenkopplung) unter 1, bei $k v_u = -1$ genau 0,5; rechts (Mitkopplung) über 1, bei $k v_u = 0{,}5$ gleich 2, bei $k v_u = 0{,}9$ gleich 10, bei $k v_u = 1$ eine senkrechte Asymptote. Rechts die Meißner-Schaltung: Triode mit einem Schwingkreis aus Spule und Kondensator im Anodenkreis und einer Koppelspule, die auf das Gitter zurückwirkt. Bei $k v_u = 1$ entsteht eine Ausgangsspannung ohne Eingangsspannung: Die Anordnung schwingt.
:::

**Die Akteure:**

- __$v_u$__: Spannungsverstärkung des Verstärkers allein; bei der ECC83-Stufe −61,5.
- __$k$__: __Rückführfaktor__, der Bruchteil der Ausgangsspannung, der zum Eingang zurückgeführt wird, mit Vorzeichen; dimensionslos.
- __$k\,v_u$__: __Schleifenverstärkung__, der Faktor, mit dem ein Signal nach einem Umlauf durch Verstärker und Rückführung wieder am Verstärkereingang ankommt. Ist sie positiv, verstärkt das zurückgeführte Signal das Eingangssignal (__Mitkopplung__); ist sie negativ, schwächt es dieses (__Gegenkopplung__).
- __$u_1$__, __$u_2$__: Eingangs- und Ausgangsspannung der ganzen Anordnung.
- __$A$__: Verstärkung der ganzen Anordnung, $u_2/u_1$.

**Das Zusammenspiel:** Am Verstärkereingang liegt die Summe aus Eingangs- und zurückgeführter Spannung. Bei Mitkopplung wächst das Signal mit jedem Umlauf, und die Anordnung verstärkt mehr als der Verstärker allein:

:::formel Formel
$$A = \frac{u_2}{u_1} = \frac{v_u}{1 - k\,v_u}$$
:::

**So liest man das:** Ohne Rückführung ist $A$ gleich $v_u$. Bei Mitkopplung steigt der Betrag von $A$, auf das Doppelte bei einer Schleifenverstärkung von 0,5 und das Zehnfache bei 0,9; bei 1 wird der Nenner null, und eine Ausgangsspannung besteht auch ohne Eingangsspannung. Bei Gegenkopplung ist $|A|$ kleiner als $|v_u|$ und hängt bei stark negativer Schleifenverstärkung nur noch von der Rückführung ab.

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

Meißner legte einen __Schwingkreis__ aus Spule und Kondensator in den Anodenkreis; nur bei dessen __Resonanzfrequenz__, der Frequenz, mit der er von selbst schwingen würde, kommt die zurückgeführte Spannung genau gleichphasig am Gitter an. Ist die Schleifenverstärkung dort etwas größer als 1, wächst schon das Rauschen der Röhre von Umlauf zu Umlauf zu einer Schwingung an, bis die Krümmung der Kennlinie die Verstärkung so weit senkt, dass die Schleifenverstärkung genau 1 beträgt; dann bleibt die Amplitude konstant. Bei der ECC83-Stufe genügt dafür 1,6 % der Ausgangsspannung, mit umgekehrter Polung zurückgeführt, weil die Stufe selbst das Vorzeichen umkehrt. Das Gegenstück, die Gegenkopplung, führte Harold Black 1927 ein; auf ihr beruhen alle linearen Verstärkerschaltungen mit Operationsverstärkern ([Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html)). Dort zählt man das Vorzeichen der Rückführung an der Summierstelle mit, so dass die Schleifenverstärkung bei Gegenkopplung positiv ist.

## Überlagerung: ein Empfänger für jede Frequenz

*Warum setzt ein Empfänger jeden Sender auf eine feste Zwischenfrequenz um, und wie gelingt das?*

Ein Empfänger muss aus allen Sendern an der Antenne einen herausfiltern. Ein Filter trennt umso schärfer, je höher seine __Güte__ ist, das Verhältnis aus Mittenfrequenz und durchgelassener Bandbreite. Für einen UKW-Sender mit 200 kHz Bandbreite bräuchte ein Filter bei 100 MHz die Güte 500 und müsste für jeden Sender neu abgestimmt werden; bei 10,7 MHz genügt die Güte 53,5, einmal fest abgeglichen. Lucien Lévy (1917), Walter Schottky (1918) und Edwin Armstrong (1918/19) meldeten unabhängig voneinander den __Überlagerungsempfänger__ zum Patent an, der jeden Sender auf eine solche feste Frequenz umsetzt; ab den 1930er-Jahren wurde er zur Grundform fast aller Rundfunkempfänger.

:::grafik
Szene: st1/einfuehrung/01-ueberlagerung · Vorlage: blockschaltbild-spektrum
**Abbildung 4:** Oben der Überlagerungsempfänger als Blockbild: Antenne, Vorfilter, Mischer mit dem abstimmbaren Lokaloszillator, Zwischenfrequenzfilter und -verstärker bei fester Frequenz, Demodulator, Lautsprecher. Unten das Spektrum auf einer Frequenzachse von 0 bis 220 MHz: das UKW-Band 87,5 bis 108 MHz grau hinterlegt, der gewünschte Sender bei 100 MHz, der Oszillator bei 110,7 MHz, die Mischprodukte bei 10,7 MHz (Differenz, Zwischenfrequenz) und 210,7 MHz (Summe), dazu die Spiegelfrequenz 121,4 MHz außerhalb des Bandes. Das Mischen schiebt den gewünschten Sender auf die feste Zwischenfrequenz; abgestimmt wird nur der Oszillator.
:::

**Die Akteure:**

- __$f_E$__: Frequenz des gewünschten Senders; im Beispiel 100 MHz.
- __$f_\mathrm{LO}$__: Frequenz des __Lokaloszillators__, eines Oszillators im Empfänger, den man beim Abstimmen verstellt; 110,7 MHz.
- __$f_\mathrm{ZF}$__: die feste __Zwischenfrequenz__; bei UKW-Empfängern 10,7 MHz.
- __Mischer__: eine Schaltung, deren Ausgangsspannung das Produkt der beiden Eingangsspannungen enthält; jede Kennlinie mit quadratischem Anteil, etwa die einer Diode, liefert ein solches Produkt.

**Das Zusammenspiel:** Der Mischer multipliziert das Empfangssignal mit der Oszillatorschwingung, und das Produkt zweier Kosinusschwingungen ist eine Summe von Kosinusschwingungen:

:::formel Satz
$$\cos\alpha\cdot\cos\beta = \tfrac12\cos(\alpha - \beta) + \tfrac12\cos(\alpha + \beta)$$
:::

Mit den Phasen der beiden Schwingungen,

$$\alpha = 2\pi f_\mathrm{LO}\,t, \qquad \beta = 2\pi f_E\,t,$$

entstehen Schwingungen bei der Differenz und bei der Summe der Frequenzen. Ein Filter bei der Differenz lässt nur diese durch, die Zwischenfrequenz:

:::formel Formel
$$f_\mathrm{ZF} = f_\mathrm{LO} - f_E$$
:::

**So liest man das:** Der Oszillator liegt um die Zwischenfrequenz über dem Sender. Beim Umstimmen verstellt man nur ihn, so dass die Differenz wieder 10,7 MHz beträgt; Filter und Verstärker der Zwischenfrequenz bleiben, wie sie sind. Die Summenfrequenz, beim Sender auf 100 MHz 210,7 MHz, hält das Zwischenfrequenzfilter zurück.

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

Das Mischen verschiebt das Signal samt seiner Information: Schwankt die Frequenz eines UKW-Senders im Takt der Musik um bis zu ±75 kHz, schwankt die Zwischenfrequenz um dieselben ±75 kHz.

:::frage
„Landet beim Mischen nicht auch ein zweiter Sender auf der Zwischenfrequenz?“
Ja, einer. Der Mischer liefert nur den Betrag der Differenz, und ein Signal, das um die Zwischenfrequenz über dem Oszillator liegt, ergibt dieselbe Differenz wie der Sender darunter. Diese __Spiegelfrequenz__ liegt zwei Zwischenfrequenzen über dem Sender, bei 100 MHz Empfangsfrequenz also bei 121,4 MHz, und ein Vorfilter vor dem Mischer muss sie unterdrücken. Weil das UKW-Band nur 20,5 MHz breit ist, der Spiegel aber 21,4 MHz entfernt liegt, fällt kein UKW-Sender auf den Spiegel eines anderen; deshalb arbeiten UKW-Empfänger mit 10,7 MHz.
:::

## Der Transistor und das Silizium

*Warum hat der Transistor die Röhre verdrängt, und warum setzte sich Silizium durch?*

Im Dezember 1947 brachten John Bardeen und Walter Brattain in den Bell Laboratories in den USA ein Germaniumplättchen mit zwei eng benachbarten Metallspitzen zum Verstärken, den ersten __Transistor__. Germanium ist ein __Halbleiter__: Seine Leitfähigkeit liegt zwischen der von Metallen und Isolatoren und lässt sich durch eingebaute Fremdatome, die __Dotierung__, einstellen, so dass entweder Elektronen (n-Gebiet) oder __Löcher__, fehlende Bindungselektronen, die sich wie positive Ladungen bewegen (p-Gebiet), überwiegen ([Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html)). William Shockley entwarf 1948 den __Bipolartransistor__ aus drei solchen Schichten in der bis heute gebauten Form. Auch er ist ein gesteuertes Ventil: Eine kleine Spannung zwischen Basis und Emitter steuert den Strom zwischen Kollektor und Emitter ([Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html)).

Dem Transistor fehlt die Heizung, und er ist klein, stoßfest und verschleißt nicht. Wie viel allein die Heizung ausmacht: 291 Millionen ECC83-Systeme, so viele Ventile wie Transistoren in einem Prozessor von 2006 (Intel Core 2 Duo), bräuchten 275 MW Heizleistung, das 4,2-Millionen-Fache der 65 W, für die der ganze Prozessor ausgelegt ist.

Die ersten Transistoren bestanden aus Germanium; 1954 entstanden die ersten aus Silizium. Silizium setzte sich aus zwei Gründen durch. Erstens sperrt es besser: Seine größere __Bandlücke__, die Energie, die ein Elektron zum Freiwerden braucht, 1,12 statt 0,66 eV, macht die __Eigenleitungsdichte__, die Dichte der von der Wärme erzeugten Ladungsträger, 2000-mal kleiner ([Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html)). Der ideale Sperrstrom eines __pn-Übergangs__, der Grenze zwischen einem n- und einem p-Gebiet, wächst mit ihrem Quadrat ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html)) und ist bei gleichem Aufbau 4 Millionen Mal kleiner; gemessen bleibt rund das Fünftausendfache, weil in Silizium ein zweiter Anteil überwiegt, der in der Sperrschicht selbst entsteht und nur mit der Eigenleitungsdichte wächst. Siliziumtransistoren arbeiten deshalb bis 150 °C, Germaniumtransistoren nur bis 90 bis 100 °C. Zweitens wächst auf Silizium beim Erhitzen in Sauerstoff eine feste, isolierende Schicht aus Siliziumdioxid (SiO₂), die die Oberfläche schützt und Dotierstoffe abhält; Germaniumdioxid löst sich in Wasser. Auf diesem Oxid beruhen Planartechnik und MOS-Transistor.

## Die integrierte Schaltung

*Warum wird ein Transistor billiger, wenn man viele davon gemeinsam auf einem Chip herstellt?*

Aus Einzelteilen gebaute Schaltungen haben ein Grundproblem: Jede Verbindung ist eine Lötstelle, der Röhrenrechner ENIAC von 1946 hatte rund 5 Millionen davon, und mit der Zahl der Teile wachsen Kosten und Ausfälle. Schon 1926 vereinte die Röhre Loewe 3NF drei Triodensysteme mit Widerständen und Kondensatoren in einem Glaskolben, weil für Rundfunkempfänger Abgaben je Röhrenfassung fällig wurden. 1958 zeigte Jack Kilby bei Texas Instruments eine Schaltung, deren Bauelemente aus einem einzigen Germaniumplättchen geformt, aber noch mit Golddrähten verbunden waren. 1959 meldete Robert Noyce bei Fairchild Semiconductor die Lösung des Verbindungsproblems zum Patent an: Bauelemente in einem Siliziumplättchen unter Oxid, Verbindungen als aufgedampfte Aluminiumbahnen auf dem Oxid, hergestellt in der __Planartechnik__ seines Kollegen Jean Hoerni. Eine solche Schaltung aus einem Stück heißt __integrierte Schaltung__ (IC), das Siliziumplättchen __Chip__.

:::grafik
Szene: st1/einfuehrung/01-planartechnik · Vorlage: querschnitt-prozess
**Abbildung 5:** Oben fünf Schritte der Planartechnik als kleine Querschnitte: (a) Siliziumscheibe mit gewachsener Oxidschicht, (b) Fotolack, durch eine Maske belichtet, (c) Fenster ins Oxid geätzt, (d) Dotierstoff dringt nur durch das Fenster ein, (e) Aluminium aufgedampft und zu Leiterbahnen geätzt. Unten der fertige Querschnitt mit einem npn-Transistor (Kollektor-, Basis- und Emittergebiet) und einem Widerstand nebeneinander, beide unter dem Oxid, verbunden durch eine Aluminiumbahn auf dem Oxid; dotierte Gebiete farbig, Oxid grau, Metall dunkel. Alle Bauelemente und ihre Verbindungen entstehen in denselben Schritten.
:::

Die Planartechnik wiederholt wenige Schritte (Abbildung 5). Die Siliziumscheibe, der __Wafer__, wird oxidiert. Ein lichtempfindlicher Lack, durch eine Maske mit dem Muster einer ganzen Ebene belichtet, legt fest, wo man Fenster ins Oxid ätzt; dieses Übertragen eines Musters mit Licht heißt __Fotolithografie__. Durch die Fenster dringen bei hoher Temperatur __Dotierstoffe__ ein, Fremdatome wie Bor für p- oder Phosphor für n-Gebiete; überall sonst hält das Oxid sie ab. Zuletzt verbinden Aluminiumbahnen auf dem Oxid die Fenster.

Jeder Schritt bearbeitet alle Strukturen der Scheibe zugleich, gleich ob ein Chip zehn oder zehn Millionen Transistoren enthält. Die Kosten eines Chips hängen deshalb an seiner Fläche, kaum an der Zahl seiner Transistoren, und Verbindungen kosten keine Lötstelle mehr. Auf dem Chip sitzen also keine eingesetzten Einzelteile; Transistoren, Widerstände und Leiterbahnen sind dotierte Gebiete und Schichten desselben Siliziumstücks. Gleich gezeichnete Nachbarn durchlaufen jeden Schritt gemeinsam und gleichen sich auf etwa 0,1 %, obwohl ihre Absolutwerte um 10 bis 20 % schwanken; darauf bauen viele integrierte Schaltungen.

## MOSFET und CMOS: Steuern ohne Strom

*Wie steuert ein Feldeffekttransistor, und warum braucht eine CMOS-Schaltung im Ruhezustand praktisch keine Leistung?*

Die Idee des __Feldeffekttransistors__ (FET), den Strom wie in der Röhre über ein elektrisches Feld zu steuern, ist älter als der Bipolartransistor; Julius Lilienfeld meldete sie 1925 zum Patent an. Mit isolierter Steuerelektrode, wie Lilienfeld ihn gedacht hatte, ließ er sich erst bauen, als Mohamed Atalla und Dawon Kahng 1959/60 in den Bell Laboratories zeigten, dass eine durch Erhitzen in Sauerstoff gewachsene SiO₂-Schicht die Elektronenzustände an der Siliziumoberfläche, die bis dahin das Feld abgeschirmt hatten, so stark verringert, dass das Feld in den Halbleiter eindringt.

Im __MOSFET__ (Metall, Oxid, Halbleiter) liegt die Steuerelektrode, das __Gate__, durch eine dünne Oxidschicht isoliert über dem Silizium zwischen den Anschlüssen __Source__ und __Drain__. Eine positive Gatespannung zieht wie die Platte eines Kondensators Elektronen an die Oberfläche darunter; sie bilden einen leitenden __Kanal__, dessen Ladung und damit Strom mit der Gatespannung wächst. Durch das Oxid fließt kein Gleichstrom: Der MOSFET wird wie die Triode kapazitiv gesteuert. Der Bipolartransistor braucht dagegen einen Basisstrom, beim BC547C etwa ein Fünfhundertstel des Kollektorstroms, auch wenn physikalisch die Basis-Emitter-Spannung steuert. Die Schaltungstechnik behandelt beide als __spannungsgesteuerte Stromquellen__, deren Ausgangsstrom die Steuerspannung festlegt.

1963 zeigten Chih-Tang Sah und Frank Wanlass bei Fairchild eine Logikschaltung aus einem n-Kanal-MOSFET (__NMOS__), der bei hoher Gatespannung leitet, und einem p-Kanal-MOSFET (__PMOS__) mit einem Kanal aus Löchern, der bei niedriger Gatespannung leitet. Diese Technik heißt __CMOS__, von complementary MOS; ihre Grundschaltung ist der __Inverter__, der eine logische 1 (hohe Spannung) in eine 0 (Spannung null) umkehrt und umgekehrt.

:::grafik
Szene: st1/einfuehrung/01-cmos-inverter · Vorlage: schaltbild-zeitverlauf
**Abbildung 6:** Links der CMOS-Inverter: PMOS zwischen Versorgung $U$ und Ausgang, NMOS zwischen Ausgang und Masse, beide Gates am Eingang, am Ausgang die Kapazität $C$ der angeschlossenen Gates und Leitungen. Daneben die beiden Ruhezustände: Eingang 0 V, PMOS leitet, NMOS sperrt, Ausgang auf $U$; Eingang $U$, NMOS leitet, PMOS sperrt, Ausgang auf 0 V; in beiden ist der Weg von der Versorgung zur Masse unterbrochen. Rechts über einer gemeinsamen Zeitachse die Eingangsspannung (Rechteck), die Ausgangsspannung (umgekehrt, mit kurzen Flanken) und der Strom aus der Versorgung: schmale Spitzen nur beim Laden des Ausgangs, sonst null. Strom fließt nur beim Umschalten.
:::

**Die Akteure:**

- __$U$__: Versorgungsspannung, zugleich der Spannungshub am Ausgang; in V; 1 V als Beispielwert heutiger Logik.
- __$C$__: Kapazität des Ausgangsknotens aus den Gates der nachfolgenden Transistoren und der Leitung dorthin; in F; 1 fF, also 10⁻¹⁵ F.
- __$f$__: wie oft je Sekunde der Knoten geladen und wieder entladen wird; in Hz; höchstens die __Taktfrequenz__, der Takt, in dem ein Prozessor seine Schritte ausführt, heute einige GHz, im Beispiel 3 GHz.
- __$P$__: mittlere Leistung, die der Knoten aus der Versorgung aufnimmt; in W.

**Das Zusammenspiel:**

**Schritt 1**: Jeder Ausgang eines __Logikgatters__, einer Schaltung, die aus den logischen Werten 0 und 1 ihrer Eingänge einen Ausgangswert bildet, treibt eine Kapazität. Eine logische 1 heißt: Sie ist auf die Versorgungsspannung geladen; eine 0 heißt: Sie ist entladen.

**Schritt 2**: Im Inverter leitet je nach Eingangsspannung genau einer der beiden Transistoren. In beiden Ruhezuständen ist der Weg von der Versorgung zur Masse unterbrochen, und es fließt kein Strom (Abbildung 6).

**Schritt 3**: Beim Wechsel von 0 auf 1 lädt der PMOS die Kapazität; die Versorgung liefert die Ladung $C U$ bei der Spannung $U$, also die Energie $C U^2$. Die Hälfte davon steckt danach in der Kapazität, die andere wird im PMOS zu Wärme, gleich wie groß sein Widerstand ist.

**Schritt 4**: Beim Wechsel zurück auf 0 entlädt der NMOS die Kapazität, und die gespeicherte Hälfte wird in ihm zu Wärme. Ein Zyklus aus Laden und Entladen kostet $C U^2$.

**Schritt 5**: Die Leistung wächst mit der Zahl der Zyklen je Sekunde: 1 fF, 1 V und 3 GHz ergeben 3 µW. Ein Chip mit 10⁸ Knoten, von denen in jedem Takt jeder zehnte geladen wird, nimmt 30 W auf. Zöge jedes Gatter dauernd nur 1 µA Ruhestrom, kämen 100 W hinzu.

:::formel Formel
$$P = C\,U^2 f$$
:::

**So liest man das:** Die Leistung wächst linear mit Kapazität und Frequenz, quadratisch mit der Spannung, und im Ruhezustand ist sie null. Am stärksten wirkt die Versorgungsspannung: Von 5 V, dem Standard bis Anfang der 1990er-Jahre, auf etwa 1 V gesenkt, kostet jeder Umladevorgang 25-mal weniger Energie.

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

**Gesucht:** Energie je Lade-Entlade-Zyklus, Leistung eines Knotens, Leistung des Chips und die Leistung des Ruhestroms.

**Rechnung:** Energie je Zyklus und Leistung eines Knotens, der in jedem Takt umgeladen wird:

$$C\,U^2 = 10^{-15}\ \mathrm{F}\cdot(1\ \mathrm{V})^2 = 1\ \mathrm{fJ}$$

$$P = 1\ \mathrm{fJ}\cdot 3\cdot 10^9\ \mathrm{s^{-1}} = 3\ \mu\mathrm{W}$$

Chip mit 10 % geladenen Knoten je Takt und Ruhestrom zum Vergleich:

$$P_\mathrm{Chip} = 0{,}1\cdot 10^8\cdot 3\ \mu\mathrm{W} = 30\ \mathrm{W}$$

$$P_\mathrm{Ruhe} = 10^8\cdot 1\ \mu\mathrm{A}\cdot 1\ \mathrm{V} = 100\ \mathrm{W}$$

**Ergebnis:** **1 fJ je Zyklus, 3 µW je Knoten, 30 W für den Chip; schon 1 µA Ruhestrom je Gatter brächte 100 W dazu.**

**Einordnung:** 30 W liegen in der Größenordnung realer Prozessoren; der Core 2 Duo von 2006 ist für 65 W Verlustleistung ausgelegt, Leckströme eingeschlossen. Bei 5 V statt 1 V stiege die Umladeleistung auf das 25-Fache, 750 W.
::::

Die ersten __Mikroprozessoren__, Rechenkerne auf einem Chip wie der 8008 von 1972 mit 3500 Transistoren und 10 µm kleinsten Strukturen, waren noch in PMOS- und NMOS-Technik gebaut, deren Gatter in einem Zustand dauernd Strom ziehen; mit wachsender Transistorzahl wurde das untragbar, und seit den 1980er-Jahren ist CMOS die beherrschende Technik.

## Das Mooresche Gesetz

*Wie schnell wächst die Zahl der Transistoren auf einem Chip, und warum gerade exponentiell?*

1965 trug Gordon Moore, damals Forschungsleiter bei Fairchild und später Mitgründer von Intel, die Zahl der Bauelemente auf den kostengünstigsten Chips über den Jahren ein: Von 1959 bis 1965 hatte sie sich jedes Jahr verdoppelt, auf etwa 64 = 2⁶, und er sagte für 1975 rund 65 000 voraus, 2¹⁶ = 65 536. 1975 sagte er voraus, dass sich das Wachstum ab etwa 1980 auf eine Verdopplung alle zwei Jahre verlangsamen werde. Diese Erfahrungsregel heißt __Mooresches Gesetz__.

:::grafik
Szene: st1/einfuehrung/01-moore · Vorlage: kennlinie-semilog
**Abbildung 7:** Transistorzahl je Chip, logarithmisch von 1 bis 10¹¹, über den Jahren 1959 bis 2010. Punkte für zwölf Intel-Prozessoren: 4004 (1971, 2300), 8008 (1972, 3500), 8080 (1974, 4500), 8086 (1978, 29 000), 80286 (1982, 134 000), 80386 (1985, 275 000), 80486 (1989, 1,18 Mio.), Pentium (1993, 3,1 Mio.), Pentium II (1997, 7,5 Mio.), Pentium 4 (2000, 42 Mio.), Core 2 Duo (2006, 291 Mio.), Xeon 7500 mit acht Kernen (2010, 2,3 Mrd.). Dazu die Ausgleichsgerade mit 2,04 Jahren Verdopplungszeit, gestrichelt Moores Gerade von 1965 (Verdopplung jedes Jahr, von 1 im Jahr 1959 über 64 im Jahr 1965 bis 65 536 im Jahr 1975) und gepunktet eine Verdopplung alle 18 Monate ab dem 8008, die 2006 bei 2,3·10¹⁰ endet. Auf der logarithmischen Achse wird exponentielles Wachstum zur Geraden.
:::

**Die Akteure:**

- __$N(t)$__: Zahl der Transistoren auf einem Chip im Jahr $t$; dimensionslos; 3500 im Jahr 1972 bis 2,3·10⁹ im Jahr 2010.
- __$t_0$__, __$N_0$__: ein Bezugsjahr und die Transistorzahl in diesem Jahr; etwa 1972 und 3500.
- __$T_2$__: __Verdopplungszeit__, die Zeit, in der sich die Transistorzahl verdoppelt; in Jahren; etwa 2.

**Das Zusammenspiel:**

**Schritt 1**: Die Kosten eines Chips hängen an seiner Fläche, kaum an der Zahl seiner Transistoren (Abschnitt *Die integrierte Schaltung*).

**Schritt 2**: Eine neue Fertigungsgeneration, ein neuer __Technologieknoten__, verkleinert alle Längen um etwa den Faktor 0,7, etwa von 180 über 130, 90 und 65 auf 45 nm. Die Fläche je Transistor sinkt auf 0,7 · 0,7 = 0,49, rund die Hälfte.

**Schritt 3**: Auf derselben Fläche finden doppelt so viele Transistoren Platz, zu fast denselben Kosten; zugleich lohnen sich größere Chips.

**Schritt 4**: Ein neuer Knoten kam etwa alle zwei bis drei Jahre. Zusammen mit den wachsenden Chipflächen verdoppelte sich die Transistorzahl je Chip etwa alle zwei Jahre.

**Schritt 5**: Gleiche Faktoren in gleichen Zeitabständen ergeben eine Exponentialfunktion. Vom 8008 (1972, 3500 Transistoren) zum Core 2 Duo (2006, 291 Millionen) wuchs die Zahl um den Faktor 83 143, das sind 16,3 Verdopplungen in 34 Jahren, eine alle 2,08 Jahre.

:::formel Formel
$$N(t) = N_0\cdot 2^{(t - t_0)/T_2}$$
:::

**So liest man das:** Der Exponent zählt die seit dem Bezugsjahr vergangenen Verdopplungszeiten; jede bringt einen Faktor 2. Auf einer logarithmischen Achse ist das eine Gerade (Abbildung 7). Bei zwei Jahren Verdopplungszeit wächst die Zahl um 41 % je Jahr.

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

**So liest man das:** Der Logarithmus des Wachstumsfaktors, geteilt durch $\ln 2$, zählt die Verdopplungen zwischen den beiden Chips; die verstrichene Zeit geteilt durch diese Zahl ist die Verdopplungszeit.

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

$$\frac{2{,}3\cdot 10^9}{3500} = 657\,143, \qquad T_2 = \frac{38\ \mathrm{Jahre}}{19{,}33} = 1{,}97\ \mathrm{Jahre}$$

**Ergebnis:** **2,08 Jahre bzw. 1,97 Jahre, also rund zwei Jahre.**

**Einordnung:** Die Ausgleichsgerade durch alle zwölf Prozessoren der Abbildung 7 ergibt 2,04 Jahre; Moores Schätzung von 1975 stimmte 35 Jahre lang.
::::

:::fehlvorstellung
„Nach dem Mooreschen Gesetz verdoppelt sich die Zahl der Transistoren alle 18 Monate.“ Die Zahl ist weit verbreitet; sie geht auf den Intel-Manager David House zurück, der damit die Rechenleistung meinte, die durch mehr und zugleich schnellere Transistoren wächst. Moore selbst nannte für die Transistorzahl 1965 ein Jahr und 1975 zwei Jahre. Mit 18 Monaten müsste ein Prozessor des Jahres 2006, ausgehend von den 3500 Transistoren des 8008, rund 2,3·10¹⁰ Transistoren haben; der Core 2 Duo hatte 2,9·10⁸, achtzigmal weniger.
:::

Das Mooresche Gesetz ist eine Erfahrungsregel über Technik und Wirtschaft, kein Naturgesetz; es erfüllte sich auch deshalb, weil die Industrie ihre Entwicklungspläne jahrzehntelang danach ausrichtete, und es endet spätestens an den Atomen des Siliziumgitters, die nur 0,235 nm voneinander entfernt liegen. Kleinere Transistoren sind zudem schneller: Verkleinert man alle Längen und Spannungen um denselben Faktor und erhöht die Dotierung entsprechend, bleiben Feldstärken und Geschwindigkeit der Ladungsträger gleich, ihr Weg wird aber kürzer und die umzuladende Ladung kleiner. Im Idealfall schalten sie so je Technologieknoten 1,41-mal schneller mit halber Leistung, und die Leistung je Fläche bleibt gleich; die Spannung wurde allerdings erst ab Anfang der 1990er-Jahre mitverkleinert, davor stieg die Leistung je Fläche.

:::frage
„Warum sind die Taktfrequenzen von Prozessoren seit Mitte der 2000er-Jahre kaum noch gestiegen?“
Weil sich die Spannung nicht mehr mitverkleinern ließ. Ein MOSFET sperrt nie vollständig: Unterhalb seiner __Schwellspannung__, der Gatespannung, ab der sein Kanal leitet, sinkt sein Strom bei Raumtemperatur je 60 mV weniger Gatespannung höchstens um den Faktor 10. Damit ein gesperrter Transistor viele Zehnerpotenzen weniger Strom führt als ein leitender, braucht er eine Schwellspannung von einigen hundert Millivolt und eine Versorgungsspannung deutlich darüber; deshalb blieb diese bei etwa 1 V stehen, und ohne kleinere Spannung steigt nach der Umladeleistung die Leistung je Fläche mit dem Takt. Der Core 2 Duo war 2006 bei 2,4 GHz für 65 W auf 143 mm² ausgelegt, 45 W/cm², fast sechsmal so viel wie eine Kochplatte mit 2 kW auf 18 cm Durchmesser. Von 1990 bis 2004 stieg der Takt von rund 33 MHz auf 3,8 GHz, danach in zwanzig Jahren nur noch auf etwa 6 GHz im Spitzentakt; seither wächst die Rechenleistung über mehrere Rechenkerne je Chip.
:::

## Die Funktechnik auf dem Chip

*Warum mussten Funkschaltungen auf einen Chip, und was machte das möglich?*

Seit den 1990er-Jahren trieb der Mobilfunk die Integration voran, denn billig wird Elektronik nur, wenn sie auf wenige Chips passt. Zunächst waren unter den Siliziumtechniken nur integrierte Bipolartransistoren schnell genug für Frequenzen bis 2 GHz, in einer Technik, die sie mit CMOS auf einem Chip vereint (__BiCMOS__), später mit Germanium in der Basis (Silizium-Germanium). Statt auf eine Zwischenfrequenz setzen moderne Empfänger das Signal direkt in den Bereich niedriger Frequenzen um, das __Basisband__ (__Direktumsetzer__). Das spart die Zwischenfrequenzfilter, die sich nicht auf Silizium herstellen lassen, verlangt aber zwei Mischungen mit um 90° versetzten Oszillatorsignalen, weil die Anteile oberhalb und unterhalb der Trägerfrequenz beim Umsetzen auf null übereinanderfallen; die beiden Signalwege müssen sich so genau gleichen, wie es nur gleich gezeichnete Strukturen auf einem Chip tun. Mit kürzeren Kanälen stieg zudem die __Transitfrequenz__ der MOSFETs, die Frequenz, bis zu der ein Transistor Strom noch verstärkt: Im 180-nm-Knoten Ende der 1990er-Jahre erreichte sie 50 bis 70 GHz, genug für Funkschaltungen um 2 GHz in reiner CMOS-Technik. Um 2000/2001 kamen Bluetooth-Chips und Mitte der 2000er-Jahre GSM-Chips auf den Markt, die Hochfrequenzteil und digitale Verarbeitung auf einem CMOS-Chip vereinen, ein __System-on-Chip__ (SoC).

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Triode und MOSFET | ein Feld steuert den Strom aus der Versorgung, der Steueranschluss braucht fast keine Leistung |
| Rückkopplung und Überlagerung | was man aus gesteuerten Ventilen baut: Oszillatoren und Empfänger mit fester Zwischenfrequenz |
| Transistor und Silizium | das Ventil ohne Heizung, mit kleinem Sperrstrom und stabilem Oxid |
| Planartechnik und Mooresches Gesetz | Ventile entstehen gemeinsam, die Kosten hängen an der Fläche; Verkleinern verdoppelt ihre Zahl etwa alle zwei Jahre |
| CMOS | Ventilpaare ohne Ruhestrom, Leistung nur beim Umladen |

Jede elektronische Schaltung beruht auf einem gesteuerten Ventil, in dem eine kleine Steuergröße einen großen Strom aus einer Versorgung steuert; die Geschichte der Schaltungstechnik ist die Geschichte, dieses Ventil kleiner, sparsamer und schneller zu machen, bis Milliarden davon gemeinsam auf einem Siliziumchip entstehen und jedes einzelne fast nichts mehr kostet.

## Bedeutung und Ausblick

Integrierte Transistoren beschreibt man heute als spannungsgesteuerte Stromquellen mit Steilheit und Ausgangswiderstand, mit denselben Begriffen wie die Triode. Schaltungen aus vielen Transistoren berechnet man mit Näherungen, indem man sie in bekannte Grundschaltungen zerlegt; das nächste Thema beginnt bei nichtlinearen Bauelementen, ihrem Arbeitspunkt und der Linearisierung um ihn herum.

**In der ausführlichen Fassung:** die Kennlinienschar der Triode mit Steuerspannung, Durchgriff und Barkhausen-Formel, Mit- und Gegenkopplung im Zahlenbeispiel, die Spiegelfrequenz mit Herleitung und UKW-Beispiel, Germanium und Silizium im Vergleich, die Loewe 3NF, die Skalierungsregeln mit Herleitung, der Direktumsetzer im Einzelnen, die Transitfrequenz und weshalb ein Prozessor analoge Schaltungstechnik braucht. [Zur ausführlichen Fassung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/einfuhrung/geschichte-der-schaltungstechnik-ausfuehrlich.html)

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
F: Stimmt es, dass ein Verstärker die zusätzliche Leistung am Ausgang selbst erzeugt?
A: Nein. Sie stammt aus der Versorgung; der Verstärker formt nur ihren Fluss. Die ECC83-Stufe gibt 0,19 mW Signalleistung ab und nimmt dafür 0,44 W aus der Anodenspannungsquelle und 0,945 W Heizleistung auf.
F: Warum wird ein Transistor billiger, wenn man die Strukturen verkleinert?
A: Die Planartechnik bearbeitet alle Strukturen einer Scheibe gleichzeitig, die Kosten hängen an der Fläche. Ein Knoten mit 0,7-fachen Längen halbiert die Fläche je Transistor; auf derselben Fläche sitzen doppelt so viele Transistoren zu fast denselben Kosten.
F: Stimmt es, dass eine CMOS-Schaltung keine Leistung braucht, weil immer ein Transistor sperrt?
A: Nein. Im Ruhezustand fließt fast kein Strom, aber jeder Lade-Entlade-Zyklus kostet $C U^2$, also $P = C U^2 f$: 1 fF, 1 V und 3 GHz ergeben 3 µW je Knoten, 10⁸ Knoten mit 10 % Umladung je Takt 30 W.
F: Stimmt es, dass Moore eine Verdopplung der Transistorzahl alle 18 Monate vorhergesagt hat?
A: Nein. Moore nannte 1965 ein Jahr und 1975 zwei Jahre; die 18 Monate gehen auf David House zurück, der die Rechenleistung meinte. Mit 18 Monaten hätte ein Prozessor 2006 rund 2,3·10¹⁰ Transistoren, achtzigmal mehr als der Core 2 Duo.
F: Der 8008 von 1972 hatte 3500 Transistoren, der Core 2 Duo von 2006 291 Millionen. Welche Verdopplungszeit folgt daraus?
A: Faktor 83 143, log₂ 83 143 = 16,34 Verdopplungen; 34 Jahre / 16,34 = 2,08 Jahre.
:::
