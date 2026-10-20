---
title: Kondensatorschaltungen – Reihe und Parallel
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Kondensator
order: 40200
summary: Von Grund auf – wie mehrere Kondensatoren zusammenwirken. Leitbild sind Gummimembranen in Wasserrohren, nebeneinander oder hintereinander, mit eingeschlossenem Wasser zwischen ihnen. Mit Parallel- und Reihenschaltung samt Herleitung aus dem jeweiligen Schaltungszwang, der Spannungsaufteilung, der Deutung über Plattenfläche und Plattenabstand, der Ladungserhaltung auf isolierten Knoten samt ihrer oft verschwiegenen Voraussetzung und dem Umladen zwischen zwei Kondensatoren einschließlich der Frage, wohin dabei Energie verschwindet. Mit Beispiel-Seite.
tags: Kondensator, Reihenschaltung, Parallelschaltung, Gesamtkapazität, Ladungserhaltung
---

## Anschaulich

Im vorigen Artikel war ein Kondensator eine Gummimembran in einem Wasserrohr: Man kann Wasser gegen sie drücken, aber nicht hindurch. Jetzt
kommen mehrere Membranen zusammen, und zwar auf zwei Arten.

**Das Leitbild dieses Artikels:** **Membranen nebeneinander und hintereinander**. Nebeneinander heißt: Das Rohr verzweigt sich, in jedem Zweig
sitzt eine Membran, und alle spüren denselben Druck. Jede nimmt ihre eigene Wassermenge auf, und die Mengen addieren sich. Hintereinander heißt:
Zwei Membranen sitzen im selben Rohr, und zwischen ihnen ist Wasser eingeschlossen. Wasser lässt sich nicht zusammendrücken; schiebt die erste
Membran eine bestimmte Menge in die Kammer, muss die zweite genau dieselbe Menge hinausschieben. Beide verschieben also dasselbe, und die
Druckunterschiede über ihnen addieren sich.

Elektrisch ist der Druck die Spannung und das verschobene Wasser die Ladung. Das eingeschlossene Wasser ist ein Stück Leitung zwischen zwei
Kondensatoren, von dem keine Ladung weg kann — und die Ladungserhaltung spielt dort die Rolle des unzusammendrückbaren Wassers.

:::grafik
Szene: get1/kondensator/02-membranen-parallel-reihe · Vorlage: membranen-schaltung
Links ein Rohr, das sich in zwei Zweige mit je einer Membran teilt; ein gemeinsamer Druck wölbt beide, Zähler zeigen die beiden Wassermengen und
ihre Summe. Rechts ein Rohr mit zwei Membranen hintereinander; die Kammer dazwischen ist farbig hervorgehoben. Ein Regler erhöht den Druck: Beide
Membranen wölben sich um dieselbe Menge, die Kammer behält ihr Volumen, und zwei Druckanzeigen über den Membranen addieren sich zum Gesamtdruck.
Darunter jeweils das Schaltbild mit zwei Kondensatoren parallel bzw. in Reihe. Kernaussage: Parallel ist der Druck gemeinsam und die Mengen addieren
sich, in Reihe ist die Menge gemeinsam und die Drücke addieren sich. (Blau = Wasser und Spannungen, rot = Membranen und Kondensatoren, orange =
Zähler und Kammer, grau = Rohre und Leitungen.)
:::

## Die Parallelschaltung

Bei der __Parallelschaltung__ liegen alle Kondensatoren $C_1$ bis $C_n$ zwischen denselben beiden Knoten. Daraus folgt der __Schaltungszwang__: An
jedem liegt dieselbe Spannung, die Gesamtspannung $U_G$:

$$U_i = U_G \quad\text{für } i = 1,\ \ldots,\ n.$$

Jeder trägt die Ladung $Q_i=C_i\,U_G$, und die Gesamtladung, die die Quelle geliefert hat, ist ihre Summe. Damit ist die Gesamtkapazität, die
__Ersatzkapazität__ der ganzen Anordnung:

:::formel
$$C_G = C_1+C_2+\ldots+C_n = \sum_{i=1}^{n}C_i.$$
:::

**So liest man das:** Parallel geschaltete Kapazitäten addieren sich. Die Gesamtkapazität ist größer als jede einzelne. Der Index $G$ steht wie
im Skript für „gesamt".

**Im Bild:** Membranen nebeneinander am selben Druck. Jede nimmt ihre Menge auf, zusammen nehmen sie die Summe auf.

:::herleitung
**Der Schaltungszwang.** Die oberen Anschlüsse aller Kondensatoren sind durch ideale Leitungen verbunden und liegen auf demselben Potenzial,
ebenso die unteren. Die Spannung ist die Potenzialdifferenz, also für alle gleich.

**Die Summe.** Die Quelle muss jedem Kondensator seine Ladung liefern:

$$Q_G = Q_1+\ldots+Q_n = C_1\,U_G+\ldots+C_n\,U_G = U_G\,\sum_{i=1}^{n}C_i.$$

Die Ersatzkapazität ist das Verhältnis von Gesamtladung zu Gesamtspannung, und $U_G$ kürzt sich heraus.

**Mit der Plattenfläche.** Haben alle denselben Abstand und dasselbe Dielektrikum, wirkt die Parallelschaltung wie ein Kondensator mit der
Summe der Flächen, denn die Kapazität ist proportional zur Fläche:

$$\varepsilon\,\frac{A_1}{d}+\varepsilon\,\frac{A_2}{d} = \varepsilon\,\frac{A_1+A_2}{d}.$$
:::

::::beispiel Zwei Kondensatoren parallel
$10\,\mu\text{F}$ und $22\,\mu\text{F}$ liegen parallel an $5\,\text{V}$. Die Einzelladungen, die Gesamtladung und die Ersatzkapazität:

$$Q_1 = 10\,\mu\text{F}\cdot5\,\text{V} = 50\,\mu\text{C}, \qquad Q_2 = 22\,\mu\text{F}\cdot5\,\text{V} = 110\,\mu\text{C}, \qquad Q_G = 160\,\mu\text{C}.$$

$$C_G = \frac{160\,\mu\text{C}}{5\,\text{V}} = 32\,\mu\text{F} = 10\,\mu\text{F}+22\,\mu\text{F}.$$

**Im Bild:** Die größere Membran nimmt mehr als doppelt so viel auf wie die kleinere, beide bei demselben Druck. Die Pumpe liefert die Summe.
::::

## Die Reihenschaltung

Bei der __Reihenschaltung__ sitzen die Kondensatoren hintereinander, und die Gesamtspannung teilt sich auf sie auf. Der Schaltungszwang ist jetzt
ein anderer: Sind die Kondensatoren vor dem Anlegen der Spannung ungeladen, tragen danach **alle dieselbe Ladung** $Q_G$:

$$Q_i = Q_G \quad\text{für } i = 1,\ \ldots,\ n.$$

Warum das so ist und warum die Voraussetzung nötig ist, zeigt der Abschnitt über die Ladungserhaltung. Mit dieser gemeinsamen Ladung ist jede
Teilspannung $U_i=\frac{Q_G}{C_i}$, und für die Ersatzkapazität gilt die Kehrwertregel:

:::formel
$$\frac{1}{C_G} = \frac{1}{C_1}+\frac{1}{C_2}+\ldots+\frac{1}{C_n} = \sum_{i=1}^{n}\frac{1}{C_i}.$$
:::

**So liest man das:** In Reihe addieren sich die Kehrwerte. Die Gesamtkapazität ist kleiner als die kleinste einzelne. Für zwei Kondensatoren:

$$C_G = \frac{C_1\,C_2}{C_1+C_2}.$$

**Im Bild:** Zwei Membranen hintereinander geben zusammen weniger nach als jede für sich: Jede trägt nur einen Teil des Drucks, und die
verschobene Menge ist für beide dieselbe.

:::herleitung
**Die Summe der Spannungen.** Geht man vom einen Anschluss zum anderen, durchläuft man nacheinander alle Kondensatoren. Die Spannung ist die
Potenzialdifferenz zwischen den Enden, und die Differenzen der einzelnen Stufen addieren sich wie bei der Kette von Punkten im Artikel über
Spannung:

$$U_G = U_1+\ldots+U_n = \frac{Q_G}{C_1}+\ldots+\frac{Q_G}{C_n} = Q_G\,\sum_{i=1}^{n}\frac{1}{C_i}.$$

Mit $U_G=\frac{Q_G}{C_G}$ kürzt sich $Q_G$, und es bleibt die Kehrwertregel.

**Zwei Kondensatoren.** Man bringt die beiden Kehrwerte auf den gemeinsamen Nenner und nimmt den Kehrwert:

$$\frac{1}{C_G} = \frac{C_2+C_1}{C_1\,C_2}, \qquad C_G = \frac{C_1\,C_2}{C_1+C_2}.$$

**Mit dem Plattenabstand.** Haben beide dieselbe Fläche und dasselbe Dielektrikum, addieren sich die Abstände:

$$\frac{d_1}{\varepsilon A}+\frac{d_2}{\varepsilon A} = \frac{d_1+d_2}{\varepsilon A}.$$

Eine dünne, ungeladene Metallfolie mitten im Spalt eines Kondensators ändert seine Kapazität deshalb nicht: Sie macht ihn zu zwei Kondensatoren in
Reihe, deren Abstände sich zum alten addieren.
:::

**Die Spannungsaufteilung.** Weil alle dieselbe Ladung tragen, ist die Teilspannung umgekehrt proportional zur Kapazität:

$$U_i = \frac{C_G}{C_i}\,U_G.$$

Der **kleinste** Kondensator bekommt die **größte** Spannung. Bei Reihenschaltungen muss man deshalb darauf achten, dass kein Kondensator über
seine zulässige Betriebsspannung kommt.

**Im Bild:** Die steifste Membran trägt den größten Teil des Drucks — sie gibt am wenigsten nach und muss deshalb am stärksten dagegenhalten.

:::herleitung
Die gemeinsame Ladung ist Ersatzkapazität mal Gesamtspannung; geteilt durch die einzelne Kapazität gibt das die Teilspannung:

$$U_i = \frac{Q_G}{C_i} = \frac{C_G\,U_G}{C_i}.$$
:::

::::beispiel Zwei Kondensatoren in Reihe
$1\,\mu\text{F}$ und $4\,\mu\text{F}$ liegen in Reihe an $10\,\text{V}$, beide vorher ungeladen:

$$C_G = \frac{1\cdot4}{1+4}\,\mu\text{F} = 0{,}8\,\mu\text{F}, \qquad Q_G = 0{,}8\,\mu\text{F}\cdot10\,\text{V} = 8\,\mu\text{C}.$$

Die Teilspannungen:

$$U_1 = \frac{8\,\mu\text{C}}{1\,\mu\text{F}} = 8\,\text{V}, \qquad U_2 = \frac{8\,\mu\text{C}}{4\,\mu\text{F}} = 2\,\text{V}.$$

Zusammen $10\,\text{V}$. Der kleine Kondensator trägt vier Fünftel der Spannung. Drei gleiche Kondensatoren von je $3\,\mu\text{F}$ ergeben übrigens in
Reihe $1\,\mu\text{F}$ und parallel $9\,\mu\text{F}$.

**Im Bild:** Die steife Membran von $1\,\mu\text{F}$ hält $8\,\text{V}$ Druck, die weiche von $4\,\mu\text{F}$ nur $2\,\text{V}$ — und beide haben
dieselben $8\,\mu\text{C}$ verschoben.
::::

## Die Ladungserhaltung

Die __Ladungserhaltung__ ist ein Grundprinzip der Physik: In einem abgeschlossenen System bleibt die Summe aller Ladungen konstant. In Schaltungen
mit Kondensatoren bildet ein Knoten ein solches System, wenn jeder Weg von ihm weg über einen Kondensator führt. Zu diesem __isolierten Knoten__,
einer Insel, gehören die Leitung und alle Elektroden, die an ihr hängen. Für ihn gilt

$$Q_\text{Insel} = \text{konstant}.$$

**So liest man das:** Die Ladung der Insel kann sich innerhalb der Insel verschieben, von einer Elektrode zur anderen, aber nicht ändern. Das
Skript formuliert es mit der Masse: Ein Knoten, von dem jeder Pfad nach Masse über eine Kapazität führt, ist abgeschlossen.

**Im Bild:** Die Wasserkammer zwischen zwei Membranen. Ihr Inhalt bleibt derselbe, nur seine Verteilung ändert sich, wenn sich die Membranen
wölben.

:::herleitung
Ladung bewegt sich nur durch Leiter. Jeder Weg von der Insel weg führt durch das Dielektrikum eines Kondensators, und durch ein ideales
Dielektrikum fließt keine Ladung. Also kann keine Ladung die Insel verlassen oder erreichen, und nach dem Ladungserhaltungssatz aus dem Artikel
über das Feld bleibt ihre Summe dieselbe.
:::

**Warum in Reihe alle dieselbe Ladung tragen.** Zwei Kondensatoren in Reihe: Die rechte Elektrode von $C_1$ und die linke von $C_2$ bilden eine
Insel. Die beiden Elektroden eines Kondensators tragen stets entgegengesetzt gleiche Ladung; was auf die eine geschoben wird, wird von der anderen
abgezogen. Schiebt die Quelle die Ladung $Q$ auf die linke Elektrode von $C_1$, trägt seine rechte also $-Q$. War die Insel anfangs neutral,
muss ihre Summe null bleiben, und die linke Elektrode von $C_2$ trägt $+Q$ — genau dieselbe Ladung. Bei mehr Kondensatoren wiederholt sich das an
jeder Insel.

:::grafik
Szene: get1/kondensator/02-insel-in-der-reihe · Vorlage: reihenschaltung-insel
Drei Kondensatoren $C_1$, $C_2$, $C_3$ in Reihe an einer Quelle $U_G$, mit den Spannungspfeilen $U_1$, $U_2$, $U_3$ von links nach rechts und $U_G$
darunter. Die beiden Inseln zwischen den Kondensatoren sind gestrichelt umrandet. Ein Regler erhöht die Quellenspannung: Auf den Elektroden
erscheinen von links nach rechts $+Q$, $-Q$, $+Q$, $-Q$, $+Q$, $-Q$, und an jeder Insel zeigt ein Zähler die Summe $-Q+Q=0$. Ein zweiter Regler
lädt $C_1$ vorher auf; dann zeigt die erste Insel einen festen Rest, und die Ladungen der Kondensatoren werden verschieden. Kernaussage: Die
neutralen Inseln erzwingen in der Reihe überall dieselbe Ladung. (Rot = Kondensatoren und Ladungen, blau = Leitungen und Spannungspfeile, orange
= Inselzähler, gestrichelt = Inseln, grau = Quelle.)
:::

**Die Voraussetzung.** Das gilt nur, wenn die Inseln vorher neutral waren. War ein Kondensator schon geladen, bevor er in die Reihe kam, trägt
seine Insel Ladung, und die Kondensatoren tragen verschiedene Ladungen. Das Skript nennt die gleiche Ladung einfach den Schaltungszwang der
Reihenschaltung; die Bedingung dahinter ist die neutrale Insel.

**Im Bild:** Zwischen zwei Membranen ist eine Kammer eingeschlossen. War sie anfangs gerade gefüllt, wölben sich beide Membranen um dieselbe
Menge. War die erste schon vorgespannt, startet die Kammer mit einem Überschuss oder Mangel, und die beiden wölben sich verschieden weit.

::::beispiel Ein vorgeladener Kondensator in der Reihe
Zwei Kondensatoren von je $1\,\mu\text{F}$ kommen in Reihe an $10\,\text{V}$. $C_1$ ist vorher auf $2\,\text{V}$ geladen, seine linke Elektrode mit
$+2\,\mu\text{C}$, seine rechte mit $-2\,\mu\text{C}$; $C_2$ ist leer. Die Insel zwischen ihnen trägt also $-2\,\mu\text{C}$, und das bleibt so.

Schiebt die Quelle die Ladung $Q$ hinein, trägt $C_1$ dann $2\,\mu\text{C}+Q$, seine rechte Elektrode das Negative davon. Damit die Insel bei
$-2\,\mu\text{C}$ bleibt, trägt die linke Elektrode von $C_2$ genau $Q$. Die Spannungen müssen sich zu $10\,\text{V}$ addieren:

$$\frac{2\,\mu\text{C}+Q}{1\,\mu\text{F}}+\frac{Q}{1\,\mu\text{F}} = 10\,\text{V}, \qquad Q = 4\,\mu\text{C}.$$

$C_1$ trägt $6\,\mu\text{C}$ bei $6\,\text{V}$, $C_2$ trägt $4\,\mu\text{C}$ bei $4\,\text{V}$ — verschiedene Ladungen. Ohne Vorladung wären es zweimal
$5\,\mu\text{C}$ bei $5\,\text{V}$.

**Im Bild:** Die vorgespannte erste Membran startet mit einem Vorsprung. Die Kammer dazwischen behält ihren Inhalt, und die beiden Membranen
wölben sich verschieden weit.
::::

## Umladen zwischen zwei Kondensatoren

Mit der Ladungserhaltung lässt sich auch berechnen, was beim Umschalten geschieht. Das Skript zeigt dazu eine Schaltung, die einen Kondensator
$C_1$ zuerst an einer Quelle mit der Spannung $U_q$ lädt, während ein zweiter, $C_2$, leer ist. Dann trennen zwei Schalter $C_1$ von der Quelle und
verbinden ihn parallel mit $C_2$. Danach bilden die verbundenen Elektroden einen isolierten Knoten: Die Ladung $C_1U_q$ bleibt erhalten und
verteilt sich, bis beide Kondensatoren dieselbe Spannung $U$ haben:

:::formel
$$U = U_q\,\frac{C_1}{C_1+C_2}.$$
:::

**So liest man das:** Die Spannung sinkt im Verhältnis der alten zur gesamten Kapazität. Ein großer leerer Kondensator zieht die Spannung weit
herunter, ein kleiner kaum. Wie im Skript zählt hier nur der Zustand vor und nach dem Umschalten; den Ausgleichsvorgang dazwischen behandelt
der nächste Artikel.

**Im Bild:** Eine gespannte Membran wird mit einer schlaffen verbunden. Das Wasser verteilt sich, bis über beiden derselbe Druck herrscht, und
die Wassermenge bleibt dieselbe.

:::herleitung
Vor dem Umschalten trägt die spätere Insel die Ladung von $C_1$, nachher die Ladungen beider Kondensatoren bei der gemeinsamen Spannung $U$.
Die Ladung bleibt erhalten:

$$C_1\,U+C_2\,U = C_1\,U_q.$$

Nach $U$ aufgelöst steht die Formel da.
:::

**Wohin geht die Energie?** Vor dem Umschalten steckt in $C_1$ die Energie $\frac12C_1U_q^2$, danach in beiden zusammen nur
$\frac12(C_1+C_2)\,U^2$. Das Verhältnis ist

$$\frac{W_\text{nach}}{W_\text{vor}} = \frac{C_1}{C_1+C_2}.$$

Der Anteil $\frac{C_2}{C_1+C_2}$ geht beim Ausgleichsstrom verloren, er wird in den Leitungen zu Wärme oder bei sehr kleinem Widerstand teils
abgestrahlt. Bemerkenswert: Wie viel verloren geht, hängt nicht davon ab, wie groß der Widerstand der Verbindung ist.

**Im Bild:** Verbindet man die beiden Rohre, schwappt das Wasser hinüber und herüber, bis es zur Ruhe kommt. Die Wucht dieses Schwappens geht als
Reibung verloren, gleichgültig, wie eng die Verbindung ist — eine enge macht es langsamer, nicht verlustfreier.

:::herleitung
**Das Verhältnis.** Man setzt die gemeinsame Spannung ein:

$$W_\text{nach} = \frac12\,(C_1+C_2)\,U_q^2\,\frac{C_1^2}{(C_1+C_2)^2} = \frac12\,C_1\,U_q^2\cdot\frac{C_1}{C_1+C_2} = W_\text{vor}\cdot\frac{C_1}{C_1+C_2}.$$

**Unabhängig vom Widerstand.** Der Endzustand folgt allein aus der Ladungserhaltung, ohne dass der Widerstand der Verbindung darin vorkommt. Also
ist auch die Energie vor und nach dem Umschalten unabhängig davon — und damit ihre Differenz, der Verlust. Ein kleiner Widerstand lässt einen
kurzen, starken Ausgleichsstrom fließen, ein großer einen langen, schwachen; die umgesetzte Energie ist dieselbe.
:::

::::beispiel Umladen in Zahlen
Ein Kondensator von $10\,\mu\text{F}$ ist auf $9\,\text{V}$ geladen und wird mit einem leeren von $20\,\mu\text{F}$ verbunden:

$$U = 9\,\text{V}\cdot\frac{10\,\mu\text{F}}{10\,\mu\text{F}+20\,\mu\text{F}} = 3\,\text{V}.$$

Probe mit der Ladung: vorher $10\,\mu\text{F}$ mal $9\,\text{V}$, also $90\,\mu\text{C}$; nachher $30\,\mu\text{F}$ mal $3\,\text{V}$, ebenfalls
$90\,\mu\text{C}$. Die Energie:

$$W_\text{vor} = \frac12\cdot10\,\mu\text{F}\cdot(9\,\text{V})^2 = 405\,\mu\text{J}, \qquad W_\text{nach} = \frac12\cdot30\,\mu\text{F}\cdot(3\,\text{V})^2 = 135\,\mu\text{J}.$$

Verloren sind $270\,\mu\text{J}$, zwei Drittel — genau der Anteil $\frac{20}{30}$ aus der Formel.

**Im Bild:** Die Ladung verteilt sich auf dreimal so viel Kapazität, die Spannung fällt auf ein Drittel. Weil die Energie mit dem Quadrat der
Spannung geht, bleibt nur ein Drittel der Energie übrig.
::::

:::grafik
Szene: get1/kondensator/02-umladen · Vorlage: schalter-kondensatoren
Ein Schaltbild: links eine Quelle $U_q$, daneben $C_1$, rechts $C_2$; zwei Umschalter mit den Stellungen 1 und 2, unten eine gemeinsame Masse. In
Stellung 1 liegt $C_1$ an der Quelle und $C_2$ ist kurzgeschlossen; ein Regler legt beide Schalter in Stellung 2, und $C_1$ und $C_2$ sind parallel
verbunden, die Quelle abgetrennt. Ein Ladungszähler am isolierten Knoten bleibt konstant, zwei Spannungsanzeigen laufen auf denselben Wert zu, ein
Energiebalken schrumpft auf $\frac{C_1}{C_1+C_2}$ seiner Länge. Kernaussage: Beim Umladen bleibt die Ladung erhalten, nicht die Energie. (Rot =
Kondensatoren, blau = Leitungen und Spannungen, orange = Zähler und Energiebalken, gestrichelt = isolierter Knoten, grau = Quelle und Masse.)
:::

## Bedeutung und Ausblick

Parallel schaltet man Kondensatoren, um eine größere Kapazität zu erhalten, etwa zum Puffern einer Versorgungsspannung. In Reihe schaltet man sie,
um eine höhere Spannung zu vertragen: Zwei Doppelschichtkondensatoren von $2{,}7\,\text{V}$ in Reihe halten $5{,}4\,\text{V}$ aus, bei halber
Kapazität. Weil sich die Spannung umgekehrt zur Kapazität verteilt und reale Kapazitäten streuen, braucht man dann oft Ausgleichswiderstände, damit
keiner überlastet wird. Kapazitive Spannungsteiler messen hohe Wechselspannungen, und geschaltete Kondensatoren arbeiten in Abtast-Halte-Gliedern,
Analog-Digital-Wandlern und Ladungspumpen, die Kapitel 10 behandelt.

Bei Widerständen ist es übrigens genau umgekehrt: In Reihe addieren sich die Widerstände, parallel ihre Kehrwerte — das zeigt Kapitel 5. Der
nächste Artikel verfolgt den Ausgleichsvorgang selbst: Wie schnell lädt sich ein Kondensator über einen Widerstand auf, und wie entlädt er sich?

:::kern
- __Parallel__: An allen liegt dieselbe Spannung; Ladungen und Kapazitäten addieren sich, $C_G=\sum C_i$.
- __In Reihe__ tragen anfangs ungeladene Kondensatoren dieselbe Ladung; Spannungen und Kehrwerte addieren sich, $\frac{1}{C_G}=\sum\frac{1}{C_i}$.
- Für zwei in Reihe ist $C_G=\frac{C_1C_2}{C_1+C_2}$, kleiner als jede einzelne Kapazität.
- In Reihe bekommt der kleinste Kondensator die größte Spannung: $U_i=\frac{C_G}{C_i}U_G$.
- Anschaulich addieren sich parallel die Plattenflächen, in Reihe die Plattenabstände.
- __Ladungserhaltung__: Die Ladung eines isolierten Knotens, von dem jeder Weg über einen Kondensator führt, bleibt konstant.
- Sie erzwingt die gleiche Ladung in Reihe — aber nur, wenn die Inseln anfangs neutral sind.
- Beim Umladen verteilt sich die Ladung: Die gemeinsame Spannung ist $U_q\frac{C_1}{C_1+C_2}$.
- Dabei geht der Energieanteil $\frac{C_2}{C_1+C_2}$ verloren, unabhängig vom Widerstand der Verbindung.
:::

:::quiz
F: Warum addieren sich parallel geschaltete Kapazitäten, und was ergeben $10\,\mu\text{F}$ und $22\,\mu\text{F}$ parallel an $5\,\text{V}$?
A: Alle Kondensatoren liegen zwischen denselben Knoten, also an derselben Spannung; jeder trägt $C_iU_G$, und die Quelle liefert die Summe. Gesamtladung durch Spannung gibt $C_G=\sum C_i$. Im Beispiel tragen sie $50$ und $110\,\mu\text{C}$, zusammen $160\,\mu\text{C}$ bei $5\,\text{V}$, also $32\,\mu\text{F}$.
F: Wie folgt die Kehrwertregel der Reihenschaltung, und warum ist die Gesamtkapazität kleiner als die kleinste einzelne?
A: Bei gleicher Ladung $Q_G$ ist jede Teilspannung $\frac{Q_G}{C_i}$, und die Teilspannungen addieren sich zur Gesamtspannung. Teilt man durch $Q_G$, addieren sich die Kehrwerte zu $\frac{1}{C_G}$. Weil jeder Summand positiv ist, ist $\frac{1}{C_G}$ größer als jeder einzelne Kehrwert, also $C_G$ kleiner als jede einzelne Kapazität.
F: Wie teilt sich in Reihe die Spannung auf, und was ergeben $1\,\mu\text{F}$ und $4\,\mu\text{F}$ an $10\,\text{V}$?
A: Wegen der gleichen Ladung ist $U_i=\frac{C_G}{C_i}U_G$: Der kleinste Kondensator bekommt die größte Spannung. Im Beispiel ist $C_G=0{,}8\,\mu\text{F}$ und $Q_G=8\,\mu\text{C}$; der Kondensator von $1\,\mu\text{F}$ trägt $8\,\text{V}$, der von $4\,\mu\text{F}$ nur $2\,\text{V}$.
F: Was bedeuten Parallel- und Reihenschaltung für Plattenfläche und Plattenabstand, und warum ändert eine ungeladene Metallfolie im Spalt nichts?
A: Bei gleichem Abstand und Dielektrikum addieren sich parallel die Flächen, denn die Kapazität ist proportional zur Fläche; bei gleicher Fläche addieren sich in Reihe die Abstände, denn der Kehrwert der Kapazität ist proportional zum Abstand. Eine dünne ungeladene Folie im Spalt macht aus einem Kondensator zwei in Reihe, deren Abstände sich zum alten addieren — die Kapazität bleibt dieselbe.
F: Was ist ein isolierter Knoten, und warum bleibt seine Ladung erhalten?
A: Ein Knoten, von dem jeder Weg über einen Kondensator führt, samt der Elektroden an ihm. Ladung bewegt sich nur durch Leiter, und durch ein ideales Dielektrikum fließt keine; also kann keine Ladung die Insel verlassen, und nach dem Ladungserhaltungssatz bleibt ihre Summe konstant. Verschieben kann sie sich innerhalb der Insel.
F: Warum tragen in Reihe alle Kondensatoren dieselbe Ladung, und welche Voraussetzung ist dafür nötig?
A: Die beiden Elektroden eines Kondensators tragen entgegengesetzt gleiche Ladung. Schiebt die Quelle $Q$ auf die erste Elektrode, trägt die Inselseite von $C_1$ $-Q$; damit die anfangs neutrale Insel neutral bleibt, trägt die Inselseite von $C_2$ $+Q$. Voraussetzung ist, dass alle Inseln anfangs neutral waren, die Kondensatoren also ungeladen.
F: Was passiert, wenn in einer Reihe ein Kondensator vorgeladen ist?
A: Seine Insel trägt dann von Anfang an Ladung, und die Kondensatoren tragen verschiedene Ladungen. Bei zwei Kondensatoren von $1\,\mu\text{F}$ an $10\,\text{V}$, der erste vorher auf $2\,\text{V}$, bleibt die Insel bei $-2\,\mu\text{C}$; der erste trägt dann $6\,\mu\text{C}$ bei $6\,\text{V}$, der zweite $4\,\mu\text{C}$ bei $4\,\text{V}$ statt zweimal $5\,\text{V}$.
F: Welche Spannung stellt sich ein, wenn ein geladener Kondensator mit einem leeren verbunden wird?
A: Die verbundenen Elektroden bilden eine Insel, und die Ladung $C_1U_q$ bleibt erhalten. Sie verteilt sich auf $C_1+C_2$ bei gemeinsamer Spannung, also $U=U_q\frac{C_1}{C_1+C_2}$. Für $10\,\mu\text{F}$ auf $9\,\text{V}$ und einen leeren von $20\,\mu\text{F}$ sind das $3\,\text{V}$, die Ladung bleibt $90\,\mu\text{C}$.
F: Wohin verschwindet beim Umladen Energie, und warum hängt der Verlust nicht vom Leitungswiderstand ab?
A: Nachher ist nur noch der Anteil $\frac{C_1}{C_1+C_2}$ der Energie gespeichert, im Beispiel $135$ von $405\,\mu\text{J}$; der Rest wird beim Ausgleichsstrom zu Wärme oder abgestrahlt. Der Endzustand folgt allein aus der Ladungserhaltung, ohne den Widerstand; also sind Anfangs- und Endenergie und damit der Verlust unabhängig von ihm. Ein kleiner Widerstand gibt einen kurzen, starken Strom, ein großer einen langen, schwachen.
F: Wozu schaltet man Kondensatoren parallel oder in Reihe, und worauf muss man bei Reihen achten?
A: Parallel für mehr Kapazität, etwa zum Puffern; in Reihe für eine höhere zulässige Spannung, zwei Doppelschichtkondensatoren von $2{,}7\,\text{V}$ etwa für $5{,}4\,\text{V}$ bei halber Kapazität. Weil sich die Spannung umgekehrt zur Kapazität verteilt und reale Kapazitäten streuen, kann ein Kondensator überlastet werden; Ausgleichswiderstände verhindern das.
:::
