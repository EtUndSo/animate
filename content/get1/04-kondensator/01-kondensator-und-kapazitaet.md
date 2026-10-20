---
title: Der Kondensator und seine Kapazität
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Kondensator
order: 40100
summary: Wie ein Kondensator Ladung speichert, was die Kapazität genau misst, warum Fläche, Abstand und Dielektrikum sie bestimmen und wie viel Energie am Ende im Feld steckt.
tags: Kondensator, Kapazität, Farad, Plattenkondensator, Dielektrikum, Permittivität, Energie
---

:::konzept
Ein Kondensator ist ein Behälter für Ladung. Zwei Metallflächen liegen sich dicht gegenüber, ohne sich zu
berühren; lädt man die eine positiv und die andere negativ auf, bleibt die Ladung dort „gefangen", weil sich
die ungleichen Ladungen gegenseitig festhalten. Wie viel Ladung so ein Behälter bei gegebener Spannung fasst,
beschreibt eine einzige Zahl: die **Kapazität**.
:::

**Worum es geht:** Im vorigen Kapitel standen Feld und Spannung im Vordergrund. Der __Kondensator__ ist das
erste Bauelement, das beide bündelt — er speichert Ladung und damit Energie im elektrischen Feld. Wir klären,
was die __Kapazität__ misst, wovon sie abhängt und wie viel Energie am Ende gespeichert ist.

## Ladung speichern: die Kapazität

Legt man an einen Kondensator eine __Spannung__ $U$ an, sammelt sich auf der einen Fläche die Ladung $+Q$, auf
der anderen $-Q$. Je höher die Spannung, desto mehr Ladung — und zwar streng proportional. Der feste
Proportionalitätsfaktor ist die __Kapazität__:

$$C = \frac{Q}{U}.$$

Die Bestandteile:

- __$C$__: die __Kapazität__ — das „Fassungsvermögen" für Ladung pro Volt. Einheit __Farad__ (F).
- __$Q$__: die auf einer Platte gespeicherte __Ladung__, in Coulomb.
- __$U$__: die anliegende __Spannung__, in Volt.

Aus der Definition folgt die Einheit unmittelbar: $1\,\text{F} = 1\,\tfrac{\text{C}}{\text{V}} =
1\,\tfrac{\text{A}\cdot\text{s}}{\text{V}}$. Ein Farad ist riesig — reale Kondensatoren liegen meist im Bereich
von Pikofarad ($\text{pF}$) bis Mikrofarad ($\mu\text{F}$).

**Anders betrachtet.** Die Kapazität verhält sich wie die Weite eines Eimers. Dieselbe „Füllhöhe" (Spannung)
fasst in einem weiten Eimer mehr Wasser (Ladung) als in einem schmalen. Ein Kondensator mit großer Kapazität
nimmt also bei gleicher Spannung mehr Ladung auf — die Kapazität ist eine reine Bauteil-Eigenschaft und ändert
sich nicht, wenn man $U$ oder $Q$ variiert; nur ihr Verhältnis bleibt konstant.

:::grafik
Ein Plattenkondensator an einer Spannungsquelle $U$: obere Platte mit $+Q$ (Pluszeichen), untere mit $-Q$
(Minuszeichen), dazwischen das Feld. Beschriftung $C = Q/U$ und der Hinweis „gleich viel $+$ wie $-$".
:::

## Woran die Kapazität hängt: der Plattenkondensator

Beim __Plattenkondensator__ — zwei parallele Platten der Fläche $A$ im Abstand $d$ — lässt sich die Kapazität
aus der Geometrie berechnen:

$$C = \varepsilon_0 \cdot \varepsilon_\text{r} \cdot \frac{A}{d}.$$

- __$\varepsilon_0$__: die __elektrische Feldkonstante__, $\varepsilon_0 \approx 8{,}854\cdot10^{-12}\,\tfrac{\text{A}\cdot\text{s}}{\text{V}\cdot\text{m}}$.
- __$\varepsilon_\text{r}$__: die __relative Permittivität__ des Materials zwischen den Platten (im Vakuum $=1$).
- __$A$__: die __Plattenfläche__, in $\text{m}^2$.
- __$d$__: der __Plattenabstand__, in Metern.

Die Formel bestätigt, was man anschaulich erwartet. **Größere Fläche** $A$ bietet mehr Platz für Ladung, also
steigt $C$. **Kleinerer Abstand** $d$ erhöht $C$ ebenfalls — denn bei kleinerem Abstand ist das Feld $E = U/d$
bei gleicher Spannung stärker und bindet mehr Ladung an die Platten. Fläche wirkt also im Zähler, Abstand im
Nenner.

:::grafik
Zwei Varianten nebeneinander: links ein Kondensator mit großer Fläche $A$ (viele Ladungen auf den Platten),
rechts mit kleinem Abstand $d$ (dichtere Feldlinien). Pfeile verdeutlichen „$A$ groß → $C$ groß" und „$d$ klein
→ $C$ groß".
:::

## Das Dielektrikum: mehr Kapazität durch einen Isolator

In echten Kondensatoren ist der Zwischenraum nicht leer, sondern mit einem Isolator gefüllt, dem
__Dielektrikum__ (etwa Kunststoff, Keramik oder Papier). Das hat einen bemerkenswerten Effekt: Es **erhöht** die
Kapazität um den Faktor $\varepsilon_\text{r}$, bei manchen Materialien um das Tausendfache.

Der Mechanismus dahinter ist die __Polarisation__. Im elektrischen Feld richten sich die Bausteine des
Dielektrikums als winzige __Dipole__ aus — die positiven Enden zur negativen Platte hin, die negativen zur
positiven. Diese ausgerichteten Ladungen erzeugen ein **Gegenfeld**, das das ursprüngliche Feld im Inneren
teilweise aufhebt. Dadurch sinkt die Spannung bei gleicher Ladung — oder umgekehrt: Bei gleicher Spannung passt
jetzt **mehr** Ladung auf die Platten. Genau das ist eine größere Kapazität.

**Anders betrachtet.** Das Dielektrikum „entschärft" einen Teil des Feldes von innen, sodass die Quelle
nachladen kann, bis die alte Spannung wieder erreicht ist. Es ist, als würde das Material der Spannungsquelle
einen Teil der Abstoßungsarbeit abnehmen — mehr Ladung bei gleichem „Druck".

:::grafik
Der Plattenzwischenraum mit vielen kleinen Dipolen (Pfeile), die sich alle gleich ausrichten: Minus-Enden zur
Plusplatte, Plus-Enden zur Minusplatte. Daneben zwei Feldpfeile — das starke äußere Feld und das schwächere
resultierende Feld im Material — um das Gegenfeld sichtbar zu machen.
:::

## Die gespeicherte Energie

Ein geladener Kondensator speichert __Energie__ im Feld zwischen den Platten. Man könnte naiv $W = Q\cdot U$
erwarten — doch das ist zu viel. Der Grund: Während des Aufladens steigt die Spannung erst allmählich von null
auf $U$ an. Die erste Ladung fließt noch bei fast null Volt hinüber, die letzte erst bei voller Spannung. Im
Mittel wird also nur die **halbe** Endspannung „bezahlt":

$$W = \frac{1}{2} \cdot C \cdot U^2.$$

- __$W$__: die im Feld gespeicherte __Energie__, in Joule.
- __$C$__: die __Kapazität__.
- __$U$__: die Spannung am fertig geladenen Kondensator.

Der Faktor $\tfrac{1}{2}$ ist genau die Fläche unter der $Q$-$U$-Geraden: Trägt man die geflossene Ladung über
der jeweils anliegenden Spannung auf, ergibt sich ein Dreieck mit der Fläche $\tfrac{1}{2}QU$, und mit $Q = CU$
wird daraus $\tfrac{1}{2}CU^2$. Dieselbe Energie lässt sich dank $Q = CU$ auch als $W = \tfrac{1}{2}QU =
\tfrac{Q^2}{2C}$ schreiben — je nachdem, welche Größen gegeben sind.

:::grafik
Ein $Q$-$U$-Diagramm: eine Gerade durch den Ursprung (Steigung $C$). Die Dreiecksfläche unter der Geraden bis
zur Endspannung $U$ ist schraffiert und beschriftet als „gespeicherte Energie $W = \tfrac{1}{2}QU$".
:::

:::kern
Ein __Kondensator__ speichert Ladung; seine __Kapazität__ $C = Q/U$ (Einheit __Farad__, $1\,\text{F} =
1\,\text{A}\text{s}/\text{V}$) ist das Fassungsvermögen pro Volt. Beim __Plattenkondensator__ gilt $C =
\varepsilon_0\varepsilon_\text{r}\,A/d$: große Fläche und kleiner Abstand erhöhen $C$, ein __Dielektrikum__
zusätzlich um den Faktor $\varepsilon_\text{r}$ (über __Polarisation__ und ein Gegenfeld). Gespeichert ist die
__Energie__ $W = \tfrac{1}{2}CU^2$ — der Faktor $\tfrac12$ kommt vom allmählichen Spannungsanstieg beim Laden.
:::

Bisher ging es um einen einzelnen Kondensator. Als Nächstes die Frage, wie sich mehrere Kondensatoren in Reihe
und parallel verhalten — und warum dabei die __Ladungserhaltung__ den Ausschlag gibt.

:::quiz
F: Warum bleibt die Ladung auf einem geladenen Kondensator „gefangen"?
A: Die beiden Platten tragen entgegengesetzte Ladung, die sich über das Feld gegenseitig anzieht und festhält. Da zwischen ihnen ein Isolator liegt, kann die Ladung nicht abfließen und bleibt gespeichert.
F: Warum ist die Kapazität eine Bauteil-Eigenschaft, obwohl sie als $Q/U$ definiert ist?
A: Ladung und Spannung ändern sich zwar, aber stets proportional zueinander, sodass ihr Verhältnis konstant bleibt. Dieser feste Faktor hängt nur von Geometrie und Material ab, nicht vom gerade eingestellten Betriebspunkt.
F: Warum erhöht eine größere Plattenfläche die Kapazität?
A: Mehr Fläche bietet mehr Platz, auf dem sich bei gegebener Spannung Ladung verteilen kann. Da $C=Q/U$ und $Q$ mit der Fläche steigt, wächst auch die Kapazität — Fläche steht im Zähler.
F: Warum erhöht ein kleinerer Plattenabstand die Kapazität?
A: Bei kleinerem $d$ ist das Feld $E=U/d$ bei gleicher Spannung stärker und bindet mehr Ladung an die Platten. Deshalb steht der Abstand im Nenner von $C=\varepsilon_0\varepsilon_r A/d$.
F: Wie erhöht ein Dielektrikum die Kapazität?
A: Seine Bausteine richten sich im Feld als Dipole aus und erzeugen ein Gegenfeld, das das innere Feld teilweise aufhebt. Bei gleicher Spannung passt dadurch mehr Ladung auf die Platten — die Kapazität steigt um den Faktor $\varepsilon_r$.
F: Was bedeutet die Polarisation anschaulich für die Spannungsquelle?
A: Das Dielektrikum „entschärft" einen Teil des Feldes von innen, sodass die Quelle nachladen kann, bis die alte Spannung wieder erreicht ist. Es nimmt der Quelle einen Teil der Abstoßungsarbeit ab — mehr Ladung bei gleichem „Druck".
F: Warum ist die gespeicherte Energie $\tfrac12 CU^2$ und nicht $QU$?
A: Beim Laden steigt die Spannung erst allmählich von null auf $U$; die erste Ladung fließt bei fast 0 V, die letzte bei voller Spannung. Im Mittel wird nur die halbe Endspannung „bezahlt", daher der Faktor $\tfrac12$.
F: Wie sieht man den Faktor $\tfrac12$ im $Q$-$U$-Diagramm?
A: Die Ladung steigt linear mit der Spannung (Gerade durch den Ursprung mit Steigung $C$). Die Energie ist die Fläche darunter — ein Dreieck mit Fläche $\tfrac12 QU$.
F: Warum ist ein Farad eine so große Einheit?
A: $1\,$F bedeutet, dass pro Volt ein ganzes Coulomb Ladung gespeichert wird — eine enorme Ladungsmenge. Reale Bauteile schaffen meist nur pF bis µF, weshalb man fast immer mit diesen Vorsätzen rechnet.
F: Lassen sich mit $Q=CU$ die drei Energieformen ineinander umrechnen?
A: Ja: Aus $W=\tfrac12 CU^2$ wird mit $Q=CU$ sowohl $\tfrac12 QU$ als auch $\tfrac{Q^2}{2C}$. Alle drei beschreiben dieselbe Energie, man wählt je nach gegebenen Größen die passende Form.
:::
