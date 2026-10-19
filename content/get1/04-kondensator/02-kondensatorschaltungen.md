---
title: Kondensatorschaltungen – Reihe und Parallel
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Kondensator
order: 40200
summary: Wie sich mehrere Kondensatoren zu einer Gesamtkapazität zusammenfassen lassen – und warum die Ladungserhaltung erklärt, dass in Reihe alle dieselbe Ladung tragen.
tags: Kondensator, Reihenschaltung, Parallelschaltung, Gesamtkapazität, Ladungserhaltung
---

:::konzept
Schaltet man Kondensatoren zusammen, verhält sich das Ergebnis oft genau **umgekehrt** zu dem, was man von
Widerständen kennt. Parallel geschaltete Kondensatoren wirken wie eine einzige große Platte — die Kapazität
addiert sich. In Reihe dagegen vergrößert sich der effektive Plattenabstand, und die Gesamtkapazität wird
**kleiner** als der kleinste Einzelkondensator. Der Schlüssel zum Verständnis ist, welche Größe jeweils gleich
bleibt: die Spannung oder die Ladung.
:::

**Worum es geht:** In einer realen Schaltung steht selten ein einzelner Kondensator. Wir klären, wie sich
__Parallel-__ und __Reihenschaltung__ zu einer __Gesamtkapazität__ zusammenfassen lassen und warum dahinter ein
fundamentales Prinzip steht: die __Ladungserhaltung__.

## Parallelschaltung: die Spannung ist gemeinsam

Bei der __Parallelschaltung__ liegen alle Kondensatoren an denselben zwei Knoten, also an **derselben
Spannung** $U$. Jeder speichert nach $Q = C\cdot U$ seine eigene Ladung; die gesamte gespeicherte Ladung ist
die Summe:

$$Q_\text{ges} = Q_1 + Q_2 = C_1 U + C_2 U = (C_1 + C_2)\,U.$$

Vergleicht man das mit $Q_\text{ges} = C_\text{ges}\cdot U$, liest man die __Gesamtkapazität__ direkt ab:

$$C_\text{ges} = C_1 + C_2 + \ldots$$

- __$C_\text{ges}$__: die __Gesamtkapazität__ der Parallelschaltung.
- __$C_1, C_2$__: die __Einzelkapazitäten__.

Die Kapazitäten addieren sich also schlicht. Anschaulich ist das sofort einsichtig: Parallelschaltung bedeutet,
die Plattenflächen nebeneinanderzulegen — und mehr __Plattenfläche__ heißt nach $C = \varepsilon_0\varepsilon_\text{r}A/d$
mehr Kapazität. Die Parallelschaltung ist damit das Gegenstück zur Reihenschaltung von Widerständen.

:::grafik
Zwei parallel geschaltete Kondensatoren an einer gemeinsamen Spannung $U$. Daneben die gedankliche Ersetzung:
beide Plattenpaare zu einer größeren Fläche zusammengeschoben, beschriftet mit $C_\text{ges} = C_1 + C_2$.
:::

## Reihenschaltung: die Ladung ist gemeinsam

Bei der __Reihenschaltung__ sitzen die Kondensatoren hintereinander, und die anliegende Spannung teilt sich auf
sie auf: $U = U_1 + U_2$. Der entscheidende Punkt ist, dass jetzt **alle Kondensatoren dieselbe Ladung** $Q$
tragen (warum, zeigt der nächste Abschnitt). Mit $U_i = Q/C_i$ wird daraus

$$U = U_1 + U_2 = \frac{Q}{C_1} + \frac{Q}{C_2} = Q\left(\frac{1}{C_1} + \frac{1}{C_2}\right).$$

Setzt man $U = Q/C_\text{ges}$ ein und kürzt $Q$, bleibt die Kehrwertregel:

$$\frac{1}{C_\text{ges}} = \frac{1}{C_1} + \frac{1}{C_2} + \ldots$$

Für zwei Kondensatoren lässt sich das zusammenfassen zu $C_\text{ges} = \dfrac{C_1 C_2}{C_1 + C_2}$. Weil sich
die Kehrwerte addieren, ist die Gesamtkapazität **kleiner** als jeder Einzelkondensator — anschaulich, weil die
Reihenschaltung den __Plattenabstand__ effektiv vergrößert, und größerer Abstand heißt weniger Kapazität.

:::grafik
Zwei Kondensatoren in Reihe an der Spannung $U$. Die Spannungsaufteilung $U = U_1 + U_2$ ist eingezeichnet, und
gestrichelt die Ersatzvorstellung eines einzelnen Kondensators mit vergrößertem Abstand, beschriftet
$1/C_\text{ges} = 1/C_1 + 1/C_2$.
:::

## Warum tragen in Reihe alle dieselbe Ladung? Die Ladungserhaltung

Das ist der physikalisch spannendste Punkt. Betrachtet man die Reihenschaltung zweier Kondensatoren, dann sind
die beiden **inneren** Platten (die untere des ersten und die obere des zweiten) nur miteinander verbunden — und
sonst mit nichts. Dieser Mittelbereich ist elektrisch __isoliert__: Von außen kann keine Ladung zu- oder
abfließen.

Genau hier greift die __Ladungserhaltung__. Vor dem Anlegen der Spannung war dieser isolierte Inselbereich
neutral, trug also die Gesamtladung null. Dieser Wert kann sich nicht ändern, weil keine Ladung die Insel
verlassen oder betreten kann. Lädt die Quelle nun die äußere Platte des ersten Kondensators mit $+Q$ auf, so
zieht dieses Feld auf der gegenüberliegenden inneren Platte die Ladung $-Q$ an. Da die Insel aber insgesamt
neutral bleiben muss, bleibt für die innere Platte des zweiten Kondensators zwangsläufig $+Q$ übrig — und die
treibt auf dessen äußerer Platte $-Q$. So trägt **jeder** Kondensator dieselbe Ladung $Q$.

**Anders betrachtet.** Die mittlere Insel verschiebt nur ihre eigene Ladung, sie bekommt keine neue. Was an
einem Ende der Insel an negativer Ladung angesammelt wird, fehlt am anderen Ende genau als positive Ladung —
die Summe bleibt null. Diese erzwungene Buchführung ist der Grund, warum die Reihenladung überall gleich ist.

:::grafik
Reihenschaltung zweier Kondensatoren mit hervorgehobenem isoliertem Mittelbereich (gestrichelt umrandet). An den
vier Platten die Ladungen $+Q, -Q, +Q, -Q$; am Mittelbereich die Bilanz „$-Q + Q = 0$" als Beleg der
Ladungserhaltung.
:::

## Merkhilfe: das Spiegelbild der Widerstände

Wer die Widerstandsregeln schon kennt, muss für Kondensatoren nur spiegeln:

| | Widerstände | Kondensatoren |
|---|---|---|
| Reihe | $R_\text{ges} = R_1 + R_2$ | $\dfrac{1}{C_\text{ges}} = \dfrac{1}{C_1} + \dfrac{1}{C_2}$ |
| Parallel | $\dfrac{1}{R_\text{ges}} = \dfrac{1}{R_1} + \dfrac{1}{R_2}$ | $C_\text{ges} = C_1 + C_2$ |

Der Grund für die Vertauschung: Beim Widerstand steht $R$ im Zusammenhang $U = R\,I$ „oben", bei der Kapazität
dagegen taucht $C$ in $U = Q/C$ im Nenner auf. Diese eine Kehrwert-Verschiebung dreht Reihe und Parallel
gegeneinander um.

:::kern
__Parallel__ liegt an allen Kondensatoren dieselbe __Spannung__, die Ladungen addieren sich, und die
Kapazitäten addieren sich: $C_\text{ges} = C_1 + C_2 + \ldots$ (anschaulich mehr Fläche). __In Reihe__ tragen
alle dieselbe __Ladung__ — erzwungen durch die __Ladungserhaltung__ auf dem isolierten Mittelbereich —, die
Spannungen addieren sich, und es gilt $\tfrac{1}{C_\text{ges}} = \tfrac{1}{C_1} + \tfrac{1}{C_2} + \ldots$
(anschaulich größerer Abstand, kleinere Gesamtkapazität). Das ist genau das Spiegelbild der Widerstandsregeln.
:::

Damit ist das statische Verhalten des Kondensators geklärt. Interessant wird es zeitlich: Wie *schnell* lädt
sich ein Kondensator auf, wenn ein Widerstand im Spiel ist? Das führt zum __Auf- und Entladevorgang__.
