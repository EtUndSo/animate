---
title: Zusammenschaltung von Widerständen
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Ströme und Spannungen in Netzen
order: 50600
summary: Wie man Reihen- und Parallelschaltungen zu einem einzigen Ersatzwiderstand zusammenfasst und mit Spannungs- und Stromteiler sofort sieht, wie sich Spannung und Strom aufteilen.
tags: Reihenschaltung, Parallelschaltung, Ersatzwiderstand, Spannungsteiler, Stromteiler
---

:::konzept
Die meisten Schaltungen bestehen aus vielen Widerständen — aber man muss sie nicht alle auf einmal betrachten.
Jede Gruppe aus Reihen- und Parallelschaltungen lässt sich Schritt für Schritt zu einem einzigen
**Ersatzwiderstand** zusammenfassen, bis nur noch ein Widerstand übrig bleibt. Dazu kommen zwei kleine Regeln,
die ohne Rechnung zeigen, wie sich Spannung und Strom aufteilen: der **Spannungsteiler** und der **Stromteiler**.
:::

**Worum es geht:** Die Kirchhoffschen Gesetze lösen jedes Netzwerk, sind aber umständlich. Für die beiden
häufigsten Strukturen — Reihe und Parallel — gibt es direkte Formeln. Wir leiten sie aus Kirchhoff her und
bekommen zwei Werkzeuge, die man ständig braucht.

## Reihenschaltung: derselbe Strom

In der __Reihenschaltung__ liegen die Widerstände hintereinander, es fließt durch alle **derselbe Strom** $I$
(die Knotenregel lässt keine Verzweigung zu). Nach der Maschenregel addieren sich die Teilspannungen zu
$U = U_1 + U_2 = R_1 I + R_2 I = (R_1 + R_2)I$. Der __Ersatzwiderstand__ ist also die Summe:

$$R_\text{ges} = R_1 + R_2 + \ldots$$

- __$R_\text{ges}$__: der __Ersatzwiderstand__ der Reihe.
- __$R_1, R_2$__: die __Einzelwiderstände__.

Mehr Widerstände in Reihe bedeuten mehr Gesamtwiderstand — anschaulich wird der „Engpass" für den Strom immer
länger. Die Spannung verteilt sich dabei **proportional** zu den Widerständen: Am größten Widerstand fällt die
größte Spannung ab.

:::grafik
Drei Widerstände in Reihe mit demselben Strompfeil $I$ hindurch, darunter der Pfeil auf einen einzelnen
Ersatzwiderstand $R_\text{ges} = R_1 + R_2 + R_3$.
:::

## Parallelschaltung: dieselbe Spannung

In der __Parallelschaltung__ liegen die Widerstände nebeneinander an **derselben Spannung** $U$. Nach der
Knotenregel teilt sich der Strom auf: $I = I_1 + I_2 = \tfrac{U}{R_1} + \tfrac{U}{R_2}$. Daraus folgt die
Kehrwertregel für den Ersatzwiderstand:

$$\frac{1}{R_\text{ges}} = \frac{1}{R_1} + \frac{1}{R_2} + \ldots$$

Mit Leitwerten geschrieben ist es noch einfacher — sie addieren sich: $G_\text{ges} = G_1 + G_2 + \ldots$ Für
zwei Widerstände ergibt das die oft gebrauchte Produkt-durch-Summe-Form:

$$R_\text{ges} = \frac{R_1 \cdot R_2}{R_1 + R_2}.$$

Der Ersatzwiderstand ist immer **kleiner** als der kleinste Einzelwiderstand — jeder zusätzliche Pfad bietet dem
Strom eine weitere Möglichkeit, also sinkt der Gesamtwiderstand. Das ist das Spiegelbild der Reihenschaltung von
Kondensatoren.

:::grafik
Drei Widerstände parallel zwischen zwei Knoten, an allen dieselbe Spannung $U$, der Gesamtstrom $I$ teilt sich
in $I_1, I_2, I_3$. Daneben der Ersatzwiderstand mit $1/R_\text{ges} = 1/R_1 + 1/R_2 + 1/R_3$.
:::

## Der Spannungsteiler

Aus der Reihenschaltung folgt eine der nützlichsten Regeln überhaupt. Weil durch beide Widerstände derselbe
Strom $I = U/(R_1+R_2)$ fließt, ist die Spannung an einem von ihnen

$$U_1 = R_1 \cdot I = U \cdot \frac{R_1}{R_1 + R_2}.$$

- __$U_1$__: die __Teilspannung__ an $R_1$.
- __$U$__: die __Gesamtspannung__ über beide Widerstände.
- __$\dfrac{R_1}{R_1 + R_2}$__: das __Teilerverhältnis__ — der Anteil, den $R_1$ am Gesamtwiderstand hat.

In Worten: Die Spannung teilt sich im **Verhältnis der Widerstände** auf. So stellt man mit zwei Widerständen
gezielt eine kleinere Spannung aus einer größeren her — die Grundschaltung hinter unzähligen Mess- und
Einstellschaltungen.

:::grafik
Zwei Widerstände $R_1$ und $R_2$ in Reihe an $U$; die Teilspannung $U_1$ wird über $R_1$ abgegriffen.
Beschriftung $U_1 = U\,R_1/(R_1+R_2)$.
:::

## Der Stromteiler

Das Gegenstück zur Parallelschaltung: Dort liegt an beiden Widerständen dieselbe Spannung $U = I\,R_\text{ges}$,
und der Strom durch einen Zweig ist $I_1 = U/R_1$. Setzt man $R_\text{ges} = \tfrac{R_1 R_2}{R_1+R_2}$ ein,
ergibt sich für zwei Widerstände

$$I_1 = I \cdot \frac{R_2}{R_1 + R_2}.$$

Man beachte das „Überkreuz": Der Strom durch $R_1$ hängt vom **anderen** Widerstand $R_2$ ab. Das ist logisch —
durch den **kleineren** Widerstand fließt der **größere** Strom, denn er ist der leichtere Weg. Allgemein teilt
sich der Strom im Verhältnis der __Leitwerte__ auf: $I_1 = I\,\tfrac{G_1}{G_1+G_2}$.

:::grafik
Zwei parallele Widerstände $R_1$ und $R_2$, der Gesamtstrom $I$ teilt sich in $I_1$ und $I_2$. Hervorgehoben,
dass durch den kleineren Widerstand der größere Strom fließt; Beschriftung $I_1 = I\,R_2/(R_1+R_2)$.
:::

## Schrittweise vereinfachen

Für ein gemischtes Netzwerk kombiniert man beides: Man sucht die innersten reinen Reihen- oder Parallelgruppen,
fasst sie zu einem Ersatzwiderstand zusammen und wiederholt das, bis nur noch ein einziger Widerstand übrig
ist. Mit dem Gesamtstrom arbeitet man sich dann über Spannungs- und Stromteiler wieder nach innen vor, um jede
einzelne Teilspannung und jeden Teilstrom zu bestimmen. So löst man viele Schaltungen ganz ohne großes
Gleichungssystem — nur mit diesen vier Bausteinen.

:::kern
__Reihe:__ gleicher Strom, $R_\text{ges} = R_1 + R_2 + \ldots$, Spannung teilt sich proportional zu $R$.
__Parallel:__ gleiche Spannung, $\tfrac{1}{R_\text{ges}} = \tfrac{1}{R_1} + \tfrac{1}{R_2} + \ldots$ (für zwei:
$R_1R_2/(R_1+R_2)$), kleiner als der kleinste Einzelwiderstand. Der __Spannungsteiler__ $U_1 = U\,R_1/(R_1+R_2)$
und der __Stromteiler__ $I_1 = I\,R_2/(R_1+R_2)$ geben die Aufteilung direkt an. Gemischte Netze fasst man
__schrittweise__ zu einem Ersatzwiderstand zusammen.
:::

Damit ist das Rüstzeug für Gleichstromnetze komplett. Im nächsten Kapitel geht es darum, Ströme und Spannungen
auch tatsächlich zu **messen** — und warum das Messgerät die Schaltung dabei möglichst wenig stören darf.
