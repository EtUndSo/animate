---
title: Arbeit, Potenzial und Spannung
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Elektrische Feldstärke und Potenzial
order: 30200
summary: Warum das Verschieben einer Ladung im Feld Energie kostet, wie daraus das Potenzial als „Höhe im Feld" entsteht und weshalb die Spannung immer eine Differenz zweier Potenziale ist.
tags: Arbeit, Energie, Potenzial, Spannung, Potenzialdifferenz, Volt, Äquipotentialfläche
---

:::konzept
Eine Ladung im elektrischen Feld ist wie ein Stein im Schwerefeld der Erde: Hebt man ihn an, steckt man Energie
hinein, die beim Herunterfallen wieder frei wird. Verschiebt man eine Ladung gegen das Feld, kostet das genauso
Energie — und diese Energie pro Ladung ist nichts anderes als die **Spannung**. Damit schließt sich der Kreis
von der Kraft zur Energie und zur wichtigsten Größe jeder Schaltung.
:::

**Worum es geht:** Das Feld übt Kräfte aus. Sobald sich eine Ladung in diesem Feld bewegt, wird __Arbeit__
verrichtet — es fließt Energie. Aus dieser Energiebetrachtung entstehen nacheinander das __Potenzial__ und die
__Spannung__. Das ist der Schritt von „wie stark zieht es?" zu „wie viel Energie steckt dahinter?".

## Arbeit im elektrischen Feld

Verschiebt man eine Ladung $q$ in einem __homogenen Feld__ über die Strecke $d$ in Richtung der Feldlinien,
dann verrichtet das Feld an ihr die __Arbeit__

$$W = q \cdot E \cdot d.$$

Die Bestandteile:

- __$W$__: die __Arbeit__ (oder umgesetzte __Energie__), in Joule.
- __$q$__: die verschobene __Ladung__, in Coulomb.
- __$E$__: die __Feldstärke__ des homogenen Feldes, in $\tfrac{\text{V}}{\text{m}}$.
- __$d$__: die zurückgelegte Strecke **längs** der Feldrichtung, in Metern.

Das ist im Grunde die mechanische Grundformel „Arbeit gleich Kraft mal Weg" ($W = F\cdot d$), in die man nur die
Feldkraft $F = q\cdot E$ einsetzt. Bewegt sich eine positive Ladung **mit** dem Feld, gibt das Feld Energie ab
(die Ladung wird schneller) — das Vorzeichen ist positiv im Sinne von „das Feld leistet die Arbeit". Will man
eine positive Ladung umgekehrt **gegen** das Feld schieben, muss man die Energie selbst aufbringen, genau wie
beim Anheben eines Gewichts.

**Anders betrachtet.** Nur die Strecke längs der Feldrichtung zählt. Bewegt man die Ladung quer zum Feld,
verrichtet das Feld keine Arbeit — so, wie das waagerechte Tragen eines Koffers gegen die Schwerkraft keine
Hubarbeit kostet. Entscheidend ist allein der in Feldrichtung zurückgelegte Höhenunterschied.

:::grafik
Ein homogenes Feld (parallele senkrechte Feldlinien). Eine positive Ladung wird um die Strecke $d$ in
Feldrichtung verschoben; eingezeichnet der Kraftpfeil $F = qE$ und die Beschriftung der Arbeit $W = qEd$.
Daneben derselbe Weg quer zum Feld mit der Notiz „keine Arbeit".
:::

## Das elektrische Potenzial

Wie schon bei der Feldstärke stört, dass die Arbeit von der verschobenen Ladung abhängt. Teilt man sie durch
die Ladung, bleibt eine reine Orts-Eigenschaft übrig — das __elektrische Potenzial__:

$$\varphi = \frac{W}{q}.$$

- __$\varphi$__: das __elektrische Potenzial__ an einem Punkt, in Volt.
- __$W$__: die __Arbeit__, um die Ladung von einem festgelegten __Bezugspunkt__ bis zu diesem Punkt zu bringen.
- __$q$__: die dabei bewegte __Ladung__.

Das Potenzial gibt also die __potentielle Energie__ pro Ladung an, die ein Körper an einem bestimmten Ort im
Feld besitzt. Genau hier greift das Bild der Höhe: Das Potenzial ist wie die **Höhe über einem Nullniveau**.
Und so, wie man „Höhe über dem Meeresspiegel" nur relativ zu einem vereinbarten Nullpunkt angibt, braucht auch
das Potenzial einen frei wählbaren __Bezugspunkt__ (oft die Erde oder der Minuspol), dem man $\varphi = 0$
zuordnet. Der absolute Zahlenwert ist deshalb nie für sich allein aussagekräftig.

:::grafik
Eine „Potenziallandschaft" als Höhenprofil: die Feldlinien laufen bergab. Zwei Punkte auf unterschiedlicher
Höhe sind markiert, dazu eine gestrichelte Nulllinie (Bezugspunkt, $\varphi = 0$) — das Bild betont, dass nur
Höhenunterschiede zählen.
:::

## Die Spannung als Potenzialdifferenz

Weil nur Unterschiede im Potenzial physikalisch wirken, definiert man die wichtigste Größe der Elektrotechnik
genau als solchen Unterschied. Die __Spannung__ zwischen zwei Punkten 1 und 2 ist die __Potenzialdifferenz__:

$$U = \varphi_1 - \varphi_2.$$

- __$U$__: die __Spannung__ zwischen den beiden Punkten, in Volt.
- __$\varphi_1, \varphi_2$__: die __Potenziale__ an den Punkten 1 und 2.

Der entscheidende Vorteil: Die Spannung ist von der Wahl des Bezugspunkts **unabhängig**, denn ein gemeinsamer
Nullpunkt fällt in der Differenz heraus. Deshalb misst man in der Praxis immer Spannungen (Differenzen) und nie
„absolute" Potenziale. Setzt man die Arbeit ein, bekommt die Spannung ihre handfeste Bedeutung:

$$U = \frac{W}{q}, \qquad 1\,\text{V} = 1\,\frac{\text{J}}{\text{C}}.$$

In Worten: Eine Spannung von einem __Volt__ liegt vor, wenn pro Coulomb verschobener Ladung ein Joule Energie
umgesetzt wird. Im homogenen Feld lässt sich das direkt mit der Feldstärke verknüpfen — aus $W = qEd$ und
$U = W/q$ folgt sofort

$$U = E \cdot d,$$

genau die Beziehung, die den Plattenkondensator so einfach macht.

**Anders betrachtet.** Die Spannung ist der „Antrieb", der Ladungen in Bewegung setzen will — das Gefälle
zwischen zwei Potenzialen. So wie Wasser nur fließt, wenn ein Höhenunterschied da ist, fließt Strom nur, wenn
eine Spannung anliegt. Die Spannung ist die Ursache, der Strom die Folge.

## Äquipotentialflächen

Punkte gleichen Potenzials bilden zusammen eine __Äquipotentialfläche__. Auf ihr kostet das Verschieben einer
Ladung **keine** Arbeit, denn es gibt ja keinen Potenzialunterschied — wie ein waagerechter Weg auf gleicher
Höhe. Daraus folgt eine wichtige geometrische Eigenschaft: Äquipotentialflächen stehen überall **senkrecht** zu
den Feldlinien. Gäbe es nämlich eine Feldkomponente längs der Fläche, würde beim Verschieben doch Arbeit
anfallen — Widerspruch.

Bei einer Punktladung sind die Äquipotentialflächen konzentrische Kugeln um die Ladung, beim Plattenkondensator
ebene Schichten parallel zu den Platten.

:::grafik
Links eine Punktladung: radiale Feldlinien, dazu konzentrische Kreise als Äquipotentiallinien (senkrecht zu den
Linien). Rechts der Plattenkondensator: parallele senkrechte Feldlinien, dazu waagerechte Äquipotentiallinien.
In beiden Fällen der 90°-Schnittwinkel hervorgehoben.
:::

:::kern
Verschiebt man eine Ladung im Feld, wird __Arbeit__ verrichtet; im homogenen Feld ist $W = q\,E\,d$. Das
__Potenzial__ $\varphi = W/q$ ist die Energie pro Ladung an einem Ort — eine „Höhe", die nur relativ zu einem
frei gewählten __Bezugspunkt__ gilt. Die __Spannung__ ist die bezugspunkt-unabhängige __Potenzialdifferenz__
$U = \varphi_1 - \varphi_2 = W/q$, mit $1\,\text{V} = 1\,\text{J}/\text{C}$; im homogenen Feld gilt $U = E\,d$.
__Äquipotentialflächen__ stehen senkrecht auf den Feldlinien, und längs ihnen kostet Verschieben keine Arbeit.
:::

Mit Feld, Potenzial und Spannung ist die Elektrostatik beisammen. Das erste Bauelement, das sie alle vereint und
Ladung gezielt speichert, ist der __Kondensator__ — das Thema des nächsten Kapitels.

:::quiz
F: Warum ist die Arbeit im Feld im Grunde nur „Kraft mal Weg"?
A: Das Feld übt auf die Ladung die Kraft $F=qE$ aus; verschiebt man sie längs dieser Kraft über die Strecke $d$, ergibt $W=F\cdot d=qEd$. Es ist dieselbe mechanische Grundformel, nur mit der elektrischen Feldkraft eingesetzt.
F: Warum zählt nur die Strecke längs der Feldrichtung zur Arbeit?
A: Arbeit entsteht nur, wenn die Kraft eine Komponente in Bewegungsrichtung hat. Quer zum Feld steht die Kraft senkrecht zum Weg und leistet nichts — wie das waagerechte Tragen eines Koffers keine Hubarbeit kostet.
F: Warum gibt das Feld einer mitlaufenden positiven Ladung Energie, während man gegen das Feld Energie aufbringen muss?
A: Das Feld beschleunigt eine positive Ladung in Feldrichtung, gibt also Energie ab. Schiebt man sie umgekehrt gegen das Feld, muss man gegen die Kraft arbeiten — wie beim Anheben eines Gewichts gegen die Schwerkraft.
F: Warum teilt man die Arbeit durch die Ladung, um das Potenzial zu definieren?
A: Die Arbeit hängt von der verschobenen Ladung ab; der Quotient $W/q$ kürzt diese Abhängigkeit heraus. Übrig bleibt eine reine Orts-Eigenschaft des Feldes — die potentielle Energie pro Ladung.
F: Warum braucht das Potenzial einen frei wählbaren Bezugspunkt?
A: Das Potenzial ist wie eine Höhe, und Höhe hat nur relativ zu einem Nullniveau einen Sinn. Man ordnet einem beliebigen Punkt (oft Erde oder Minuspol) $\varphi=0$ zu; der absolute Zahlenwert allein ist daher nicht aussagekräftig.
F: Warum ist die Spannung unabhängig von der Wahl des Bezugspunkts?
A: Sie ist die Differenz $U=\varphi_1-\varphi_2$, und ein gemeinsam addierter Nullpunkt fällt beim Subtrahieren heraus. Deshalb misst man in der Praxis stets Spannungen (Differenzen) statt absoluter Potenziale.
F: Was bedeutet „eine Spannung von 1 Volt" energetisch?
A: Wegen $U=W/q$ und $1\,$V$=1\,$J/C liegt 1 Volt vor, wenn pro Coulomb verschobener Ladung ein Joule Energie umgesetzt wird. Die Spannung ist also Energie pro Ladung.
F: Warum ist die Spannung die Ursache und der Strom die Folge?
A: Die Spannung ist das Potenzialgefälle, das Ladungen in Bewegung treiben will — wie ein Höhenunterschied das Wasser. Ohne Gefälle kein Antrieb: Strom fließt erst, wenn eine Spannung anliegt.
F: Warum kostet das Verschieben einer Ladung auf einer Äquipotentialfläche keine Arbeit?
A: Auf ihr ist das Potenzial überall gleich, es gibt also keine Potenzialdifferenz und damit kein $W=qU$. Wie auf einem waagerechten Weg gleicher Höhe wird keine Energie umgesetzt.
F: Warum stehen Äquipotentialflächen immer senkrecht auf den Feldlinien?
A: Gäbe es eine Feldkomponente längs der Fläche, würde Verschieben dort Arbeit kosten — im Widerspruch zur Gleichheit des Potenzials. Also darf das Feld nur senkrecht zur Fläche stehen.
:::
