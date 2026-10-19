---
title: Der Bipolartransistor – Aufbau und Wirkungsweise
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Bipolartransistoren
order: 110100
summary: Wie aus drei dotierten Schichten ein steuerbares Bauelement wird, das mit einem winzigen Basisstrom einen großen Kollektorstrom lenkt – der Transistoreffekt, die Stromverstärkung und die drei Betriebsbereiche.
tags: Bipolartransistor, npn, pnp, Transistoreffekt, Stromverstärkung, aktiver Bereich, Sättigung
---

:::konzept
Der Transistor ist das wichtigste aktive Bauelement der Elektronik — er kann **verstärken** und **schalten**.
Das Prinzip: Ein sehr kleiner Steuerstrom lenkt einen viel größeren Strom, so wie ein leichter Druck auf einen
Wasserhahn einen kräftigen Strahl freigibt. Gebaut ist er aus drei dotierten Halbleiterschichten, und der ganze
Zauber beruht darauf, dass die mittlere Schicht — die **Basis** — extrem dünn ist.
:::

**Worum es geht:** Nach der Diode kommt das Bauelement, das die moderne Elektronik überhaupt möglich macht. Wir
klären den __Aufbau__ des __Bipolartransistors__, den __Transistoreffekt__, der die Verstärkung erzeugt, die
__Stromverstärkung__ als Kennzahl und die drei __Betriebsbereiche__.

## Aufbau: drei Schichten, zwei Übergänge

Ein __Bipolartransistor__ besteht aus drei dotierten Zonen in der Folge **npn** (oder pnp). Beim npn-Typ liegt
eine dünne p-Schicht zwischen zwei n-Schichten. Die drei Anschlüsse heißen:

- __Emitter__ (E): stark n-dotiert — er „emittiert" (sendet) die Ladungsträger aus.
- __Basis__ (B): die mittlere, **sehr dünne** und **schwach dotierte** p-Schicht — die Steuerelektrode.
- __Kollektor__ (C): n-dotiert — er „kollektiert" (sammelt) die Ladungsträger ein.

Damit enthält der Transistor **zwei pn-Übergänge**: den __Basis-Emitter-Übergang__ (BE) und den
__Basis-Kollektor-Übergang__ (BC). Entscheidend sind zwei bauliche Besonderheiten der Basis: Sie ist einerseits
**hauchdünn** und andererseits nur **schwach dotiert**. Genau das macht den Transistoreffekt erst möglich.

:::grafik
Links der Schichtaufbau npn: n-Emitter | dünne p-Basis | n-Kollektor, mit den zwei pn-Übergängen BE und BC und
den drei Anschlüssen. Rechts das Schaltsymbol des npn-Transistors (Pfeil am Emitter nach außen) mit den
beschrifteten Anschlüssen E, B, C.
:::

## Der Transistoreffekt

Jetzt die Wirkungsweise im Normalbetrieb (aktiver Bereich): Der __Basis-Emitter-Übergang__ wird in
**Durchlassrichtung** gepolt (Basis positiv gegenüber Emitter), der __Basis-Kollektor-Übergang__ in
**Sperrrichtung** (Kollektor noch positiver).

Weil der BE-Übergang leitet, „schießt" der stark dotierte Emitter eine große Zahl Elektronen in die Basis. Jetzt
kommt die dünne Basis ins Spiel: Eigentlich müssten diese Elektronen als Basisstrom abfließen. Doch die Basis
ist so **dünn** und so **schwach dotiert**, dass die allermeisten Elektronen gar nicht genug Löcher zum
Rekombinieren finden — sie durchqueren die Basis einfach und geraten in den Einzugsbereich des gesperrten
BC-Übergangs. Dessen elektrisches Feld zieht sie sofort zum Kollektor hinüber.

Das Ergebnis: Nur ein **winziger Bruchteil** der Elektronen fließt tatsächlich als Basisstrom ab, der große Rest
landet als Kollektorstrom. Ein kleiner __Basisstrom__ $I_\text{B}$ ist also von einem viel größeren
__Kollektorstrom__ $I_\text{C}$ begleitet — und weil $I_\text{B}$ das Ganze steuert, **steuert ein kleiner Strom
einen großen**. Das ist der __Transistoreffekt__.

:::grafik
Der npn-Transistor im Betrieb: vom Emitter strömen viele Elektronen in die dünne Basis; ein dicker Pfeil zeigt,
wie fast alle zum Kollektor durchlaufen, nur ein dünner Pfeil zweigt als Basisstrom ab (wenige Rekombinationen
in der Basis). Spannungen: BE in Durchlass, BC in Sperrrichtung.
:::

## Die Ströme und die Stromverstärkung

Nach der Knotenregel teilt sich der Emitterstrom in Basis- und Kollektorstrom auf:

$$I_\text{E} = I_\text{C} + I_\text{B}.$$

Das Verhältnis von Kollektor- zu Basisstrom ist die __Stromverstärkung__ $\beta$ (auch $B$ genannt):

$$I_\text{C} = \beta \cdot I_\text{B}.$$

- __$I_\text{C}$__: der __Kollektorstrom__ (der große, gesteuerte Strom).
- __$I_\text{B}$__: der __Basisstrom__ (der kleine Steuerstrom).
- __$\beta$__: die __Stromverstärkung__, typisch $100$ bis $300$ (bei manchen Typen bis über $1000$).

Ein Basisstrom von nur $10\,\mu\text{A}$ erzeugt bei $\beta = 200$ also einen Kollektorstrom von $2\,\text{mA}$ —
das Zweihundertfache. Gelegentlich nutzt man auch die __Gleichstromverstärkung__ $\alpha = I_\text{C}/I_\text{E}$
(knapp unter 1, etwa $0{,}99$); beide hängen über $\beta = \dfrac{\alpha}{1-\alpha}$ zusammen.

## Die drei Betriebsbereiche

Je nachdem, wie die beiden Übergänge gepolt sind, arbeitet der Transistor in einem von drei Bereichen:

| Bereich | BE-Übergang | BC-Übergang | Verhalten |
|---|---|---|---|
| Sperrbereich | gesperrt | gesperrt | Transistor aus (kein $I_\text{C}$) |
| aktiver Bereich | leitend | gesperrt | linearer Verstärker ($I_\text{C} = \beta I_\text{B}$) |
| Sättigung | leitend | leitend | voll durchgeschaltet (Schalter „ein") |

Im __aktiven Bereich__ gilt die Verstärkungsbeziehung — hier arbeitet der Transistor als **Verstärker**. Im
__Sperrbereich__ (aus) und in der __Sättigung__ (voll ein) nutzt man ihn als **Schalter**, der zwischen diesen
beiden Zuständen umspringt — die Grundlage jeder Digitalelektronik.

:::grafik
Das Ausgangskennlinienfeld $I_\text{C}$ über $U_\text{CE}$ mit mehreren Kurven für verschiedene $I_\text{B}$:
links der steile Anstieg (Sättigung), rechts die nahezu waagerechten Äste (aktiver Bereich), unten die Nulllinie
(Sperrbereich). Die drei Bereiche farbig abgegrenzt und beschriftet.
:::

## Der pnp-Transistor

Der __pnp-Transistor__ ist das komplementäre Gegenstück: Die Schichtfolge und damit alle Dotierungen sind
vertauscht (p-n-p), und entsprechend kehren sich **alle Spannungspolaritäten und Stromrichtungen um**. Hier
steuert der Emitter Löcher statt Elektronen, und die Versorgungsspannung ist umgekehrt gepolt. Funktionsweise und
Formeln bleiben identisch — man muss nur konsequent alle Vorzeichen spiegeln. In der Praxis ergänzen sich npn-
und pnp-Transistoren zu komplementären Schaltungen.

:::grafik
Die beiden Schaltsymbole nebeneinander: npn (Emitterpfeil nach außen) und pnp (Emitterpfeil nach innen), jeweils
mit der Polung der Versorgungsspannung — bei npn Kollektor positiv, bei pnp Kollektor negativ.
:::

:::kern
Der __Bipolartransistor__ (npn/pnp) besteht aus drei Schichten mit zwei pn-Übergängen; die __Basis__ dazwischen
ist **dünn und schwach dotiert**. Im aktiven Betrieb (BE leitend, BC gesperrt) durchqueren fast alle vom Emitter
injizierten Träger die Basis zum Kollektor — der __Transistoreffekt__: ein kleiner __Basisstrom__ steuert einen
großen __Kollektorstrom__, $I_\text{C} = \beta I_\text{B}$ (mit $I_\text{E} = I_\text{C} + I_\text{B}$, $\beta
\approx 100\ldots300$). Drei __Betriebsbereiche__: Sperrbereich (aus), aktiver Bereich (Verstärker), Sättigung
(Schalter ein). Der __pnp-Transistor__ arbeitet spiegelbildlich mit umgekehrten Polaritäten.
:::

Damit der Transistor sauber als Verstärker arbeitet, muss man ihn in den aktiven Bereich bringen und dort
stabil halten — das ist die __Arbeitspunkteinstellung__, das Thema des nächsten Abschnitts.
