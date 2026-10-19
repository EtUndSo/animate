---
title: Die Kirchhoffschen Gesetze
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Ströme und Spannungen in Netzen
order: 50500
summary: Die beiden Grundregeln, aus denen sich jede Schaltung berechnen lässt – die Knotenregel aus der Ladungserhaltung, die Maschenregel aus der Energieerhaltung – mit Vorzeichen und einem durchgerechneten Beispiel.
tags: Kirchhoff, Knotenregel, Maschenregel, Netzwerkanalyse, Ladungserhaltung, Energieerhaltung
---

:::konzept
Zwei einfache Buchhaltungsregeln genügen, um jedes Gleichstromnetz zu berechnen. Die erste betrifft die Ströme:
An einer Kreuzung staut sich nichts an — was hineinfließt, muss auch wieder heraus. Die zweite betrifft die
Spannungen: Geht man eine geschlossene Runde und kommt zum Startpunkt zurück, heben sich alle Spannungs-Anstiege
und -Abfälle genau auf. Das sind die **Kirchhoffschen Gesetze**, und dahinter stehen zwei der tiefsten Prinzipien
der Physik: Ladungserhaltung und Energieerhaltung.
:::

**Worum es geht:** Mit den topologischen Begriffen (Knoten, Zweig, Masche) im Rücken formulieren wir jetzt die
beiden Gesetze, die jede Netzwerkberechnung tragen — die __Knotenregel__ und die __Maschenregel__ — und rechnen
ein kleines Netzwerk damit durch.

## Die Knotenregel: Ströme an einem Knoten

Die __Knotenregel__ (1. Kirchhoffsches Gesetz) sagt: An jedem Knoten ist die Summe der zufließenden Ströme
gleich der Summe der abfließenden. Zählt man zufließende positiv und abfließende negativ, lautet sie kompakt

$$\sum_k I_k = 0.$$

- __$I_k$__: die einzelnen __Zweigströme__ am Knoten, mit Vorzeichen nach ihrer Zählrichtung (hinein $+$, hinaus $-$).

Der Grund ist die __Ladungserhaltung__: An einem Knoten kann sich keine Ladung ansammeln oder verschwinden — er
hat kein „Lager". Was in einer Sekunde an Ladung hineinströmt, muss in derselben Sekunde wieder herausströmen,
sonst würde sich dort unbegrenzt Ladung aufstauen. Genau das ist bereits beim Kondensator in Reihe aufgetaucht
(die isolierte Insel blieb neutral) — hier ist es dieselbe Idee für einen durchströmten Knoten.

:::grafik
Ein Knoten mit drei zufließenden Strömen ($I_1, I_2$ hinein) und zwei abfließenden ($I_3, I_4$ heraus). Daneben
die Bilanz $I_1 + I_2 = I_3 + I_4$ bzw. $\sum I_k = 0$, mit farblich getrennten Hinein-/Hinaus-Pfeilen.
:::

## Die Maschenregel: Spannungen in einer Runde

Die __Maschenregel__ (2. Kirchhoffsches Gesetz) sagt: In jeder geschlossenen __Masche__ ist die Summe aller
Spannungen null:

$$\sum_k U_k = 0.$$

- __$U_k$__: die __Teilspannungen__ längs der Masche, mit Vorzeichen nach der gewählten Umlaufrichtung.

**Die Vorzeichenregel:** Man legt eine Umlaufrichtung fest (etwa im Uhrzeigersinn) und zählt jede Spannung
positiv, deren Zählpfeil in Umlaufrichtung zeigt, und negativ, wenn er dagegen zeigt. Dann müssen sich alle
Beiträge zu null addieren.

Dahinter steckt die __Energieerhaltung__: Das __Potenzial__ ist an jedem Punkt ein eindeutiger Wert. Geht man
eine geschlossene Runde, ist man am Ende wieder am Ausgangspunkt — also auf demselben Potenzial. Die Summe aller
Höhenunterschiede längs des Weges muss deshalb null sein, genau wie bei einer Wanderung, die am Startpunkt endet:
So viel wie man bergauf gestiegen ist, ist man in Summe auch wieder hinabgestiegen.

:::grafik
Eine Masche mit einer Quelle $U_0$ und zwei Widerständen; ein kreisförmiger Umlaufpfeil (im Uhrzeigersinn) legt
die Richtung fest. Jede Spannung mit $+$ oder $-$ markiert, je nachdem, ob ihr Pfeil mit dem Umlauf läuft.
Bilanz: $U_0 - U_1 - U_2 = 0$.
:::

## Beide zusammen: ein Netzwerk lösen

Der Nutzen zeigt sich erst im Zusammenspiel. Nimm eine Quelle $U_0 = 12\,\text{V}$ mit zwei Widerständen
$R_1 = 2\,\Omega$ und $R_2 = 4\,\Omega$ in Reihe. Gesucht ist der Strom $I$.

**Schritt 1** — Maschenregel für den einzigen Umlauf aufstellen. Die Quellenspannung treibt, an den Widerständen
fällt Spannung ab: $U_0 - U_1 - U_2 = 0$, also $U_0 = U_1 + U_2$.

**Schritt 2** — das Ohmsche Gesetz einsetzen. Mit $U_1 = R_1 I$ und $U_2 = R_2 I$ (gleicher Strom, weil
Reihenschaltung — die Knotenregel garantiert das) wird daraus

$$U_0 = R_1 I + R_2 I = (R_1 + R_2)\,I.$$

**Schritt 3** — nach dem Strom auflösen und einsetzen:

$$I = \frac{U_0}{R_1 + R_2} = \frac{12\,\text{V}}{2\,\Omega + 4\,\Omega} = 2\,\text{A}.$$

Die Teilspannungen sind dann $U_1 = R_1 I = 4\,\text{V}$ und $U_2 = R_2 I = 8\,\text{V}$ — und ihre Summe ergibt
wieder die $12\,\text{V}$ der Quelle, wie es die Maschenregel verlangt. Genau nach diesem Muster — Knotengleichungen
plus Maschengleichungen plus Ohmsches Gesetz — löst man beliebig große Netzwerke; man braucht nur die $k-1$ und
$m = z-(k-1)$ unabhängigen Gleichungen aus dem vorigen Abschnitt.

:::grafik
Das durchgerechnete Beispiel als Schaltbild: Quelle $12\,\text{V}$, $R_1 = 2\,\Omega$ und $R_2 = 4\,\Omega$ in
Reihe, Strom $I = 2\,\text{A}$ eingezeichnet, dazu die Teilspannungen $4\,\text{V}$ und $8\,\text{V}$.
:::

:::kern
Die __Knotenregel__ $\sum I_k = 0$ (zu/ab mit Vorzeichen) folgt aus der __Ladungserhaltung__ — an einem Knoten
sammelt sich nichts an. Die __Maschenregel__ $\sum U_k = 0$ (Vorzeichen nach Umlaufrichtung) folgt aus der
__Energieerhaltung__ — eine geschlossene Runde endet auf demselben Potenzial. Zusammen mit dem Ohmschen Gesetz
und den $k-1$ bzw. $m = z-(k-1)$ unabhängigen Gleichungen lässt sich damit jedes Gleichstromnetz lösen.
:::

Diese Gesetze von Hand auf jedes Netzwerk anzuwenden ist möglich, aber mühsam. Für oft gebrauchte Strukturen gibt
es Abkürzungen — die __Zusammenschaltung von Widerständen__ zu Reihen, Parallelschaltungen und Spannungsteilern.
