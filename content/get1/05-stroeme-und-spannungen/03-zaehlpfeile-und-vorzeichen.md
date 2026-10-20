---
title: Zählpfeile und Vorzeichen
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Ströme und Spannungen in Netzen
order: 50300
summary: Warum man in einer Schaltung zuerst Richtungen festlegt, obwohl man sie noch nicht kennt, und wie das Verbraucher- und Erzeugerpfeilsystem dafür sorgt, dass Vorzeichen und Leistung eindeutig werden.
tags: Zählpfeil, Verbraucherpfeilsystem, Erzeugerpfeilsystem, Vorzeichen, Leistung, Netzwerkanalyse
---

:::konzept
Bevor man ein Netzwerk berechnet, steht man vor einem Henne-Ei-Problem: Um Ströme und Spannungen auszurechnen,
muss man ihre Richtung kennen — aber die kennt man ja erst **nach** der Rechnung. Die Lösung ist elegant: Man
legt die Richtung einfach fest, zeichnet einen **Zählpfeil**, und rechnet damit. Kommt am Ende ein negativer
Wert heraus, bedeutet das schlicht, dass die Größe in Wirklichkeit andersherum zeigt. Der Zählpfeil ist also wie
die „positive Richtung" auf einem Zahlenstrahl.
:::

**Worum es geht:** Ohne eine saubere Vorzeichen-Vereinbarung sind Rechnungen in Netzwerken mehrdeutig. Dieser
Abschnitt klärt, was ein __Zählpfeil__ ist, wie man Strom- und Spannungspfeile einträgt und warum es zwei
sinnvolle Systeme gibt — eines für Verbraucher, eines für Quellen.

## Warum überhaupt Zählpfeile?

Ein __Zählpfeil__ zeigt **nicht** unbedingt in die tatsächliche Stromrichtung oder zum tatsächlich höheren
Potenzial. Er legt nur fest, welche Richtung als **positiv gezählt** wird. Man nimmt eine Richtung an, rechnet,
und das Vorzeichen des Ergebnisses verrät die Wahrheit:

- Ein **positiver** Wert heißt: Die Größe zeigt tatsächlich in Pfeilrichtung.
- Ein **negativer** Wert heißt: Sie zeigt in Wirklichkeit entgegengesetzt — die Rechnung bleibt trotzdem
  richtig.

Das ist der entscheidende Vorteil: Man muss die Richtungen vorher **nicht** raten. Man darf sie frei wählen,
solange man danach konsequent dabei bleibt.

:::grafik
Ein Bauteil mit einem angenommenen Strompfeil nach rechts. Daneben zwei Fälle: Ergebnis $I = +2\,\text{A}$
(tatsächlicher Strom in Pfeilrichtung) und $I = -2\,\text{A}$ (tatsächlicher Strom gegen den Pfeil), um zu
zeigen, dass das Vorzeichen die reale Richtung liefert.
:::

## Strom- und Spannungspfeile eintragen

Zwei Arten von Zählpfeilen treten auf. Der __Strompfeil__ wird längs des Leiters eingezeichnet und zeigt die
positiv gezählte Flussrichtung an. Der __Spannungspfeil__ steht zwischen zwei Punkten und zeigt (per gängiger
Vereinbarung) von Punkt zum Bezugspunkt, also in Richtung **abnehmenden** Potenzials — von Plus nach Minus.

Entscheidend ist nun, wie Strom- und Spannungspfeil an **einem Bauteil** zueinander liegen. Genau daraus
entstehen die beiden Zählpfeilsysteme.

## Verbraucher- und Erzeugerpfeilsystem

Im __Verbraucherpfeilsystem__ (VZS) zeichnet man Strom- und Spannungspfeil am Bauteil **gleichsinnig** —
der Strompfeil zeigt in dieselbe Richtung wie der Spannungspfeil, also in Richtung fallenden Potenzials. Das
passt zu einem Verbraucher wie dem Widerstand: Dort fließt der (technische) Strom vom höheren zum niedrigeren
Potenzial. In diesem System gilt das Ohmsche Gesetz ohne Vorzeichenärger als $U = R\,I$.

Im __Erzeugerpfeilsystem__ (EZS) zeichnet man die beiden Pfeile **gegensinnig** (antiparallel). Das passt zu
einer Quelle: Eine Batterie treibt den Strom im Inneren vom Minus- zum Pluspol, also **gegen** das Spannungsgefälle.

Welches System man wählt, ist Geschmackssache — üblich ist, Verbraucher im VZS und Quellen im EZS zu zeichnen,
weil dann die „erwarteten" Größen positiv herauskommen.

:::grafik
Links ein Widerstand im Verbraucherpfeilsystem: Strompfeil und Spannungspfeil zeigen gleichsinnig durch bzw.
über das Bauteil. Rechts eine Quelle im Erzeugerpfeilsystem: Strom- und Spannungspfeil gegensinnig. Beschriftung
„VZS: gleichsinnig" und „EZS: gegensinnig".
:::

## Die Leistung und ihr Vorzeichen

Der ganze Aufwand lohnt sich, weil damit auch die __Leistung__ ein eindeutiges Vorzeichen bekommt. Sie ist
immer

$$P = U \cdot I,$$

aber ihre Deutung hängt vom gewählten System ab:

- Im __Verbraucherpfeilsystem__ bedeutet $P > 0$, dass das Bauteil Energie **aufnimmt** (der Widerstand wird
  warm). $P < 0$ hieße, es gibt in Wirklichkeit Energie ab.
- Im __Erzeugerpfeilsystem__ bedeutet $P > 0$, dass das Bauteil Energie **abgibt** (die Quelle speist das Netz).

Anschaulich: Wo Strom- und Spannungspfeil **gleich** gerichtet sind (VZS), wird bei positivem Produkt Energie im
Bauteil umgesetzt; wo sie **entgegengesetzt** sind (EZS), wird dem Kreis Energie zugeführt. Ein Vorzeichen in
der berechneten Leistung sagt also direkt, ob ein Bauteil Verbraucher oder Quelle ist — unabhängig davon, wie
man es anfangs angenommen hat.

:::grafik
Eine kleine Übersicht: oben VZS (Pfeile gleichsinnig) mit „$P>0 \Rightarrow$ nimmt auf", unten EZS (Pfeile
gegensinnig) mit „$P>0 \Rightarrow$ gibt ab". Jeweils ein Widerstand bzw. eine Batterie als Beispiel daneben.
:::

:::kern
Ein __Zählpfeil__ legt nur die positiv gezählte Richtung fest, nicht die tatsächliche — ein negatives Ergebnis
heißt „in Wirklichkeit andersherum". Am Bauteil unterscheidet man das __Verbraucherpfeilsystem__ (Strom- und
Spannungspfeil **gleichsinnig**, Ohmsches Gesetz $U = RI$, $P>0$ = Aufnahme) und das __Erzeugerpfeilsystem__
(Pfeile **gegensinnig**, $P>0$ = Abgabe). Die __Leistung__ $P = U\,I$ bekommt so ein eindeutiges Vorzeichen, das
Verbraucher von Quelle unterscheidet. Richtungen darf man frei wählen — nur konsequent muss man bleiben.
:::

Mit festgelegten Zählrichtungen lässt sich jede Schaltung eindeutig beschreiben. Als Nächstes die Sprache, in
der man über die Struktur eines Netzwerks spricht: __Knoten__, __Zweige__ und __Maschen__.

:::quiz
F: Warum legt man Zählpfeile fest, obwohl man die wahren Richtungen noch nicht kennt?
A: Um ein Netzwerk zu berechnen, braucht man vorab eine Vorzeichenkonvention — die kennt man aber erst nach der Rechnung. Der Zählpfeil löst dieses Henne-Ei-Problem: Man nimmt eine Richtung an und das Ergebnisvorzeichen liefert die Wahrheit nach.
F: Was bedeutet ein negatives Ergebnis bei einer Zählpfeilrechnung?
A: Die Größe zeigt in Wirklichkeit entgegengesetzt zum angenommenen Pfeil. Die Rechnung bleibt dabei völlig korrekt — das Minuszeichen ist nur die Auskunft über die tatsächliche Richtung.
F: Warum darf man die Pfeilrichtungen frei wählen?
A: Weil der Pfeil nur die positiv gezählte Richtung definiert, wie die positive Seite eines Zahlenstrahls. Jede Wahl führt zum richtigen physikalischen Ergebnis, solange man konsequent dabei bleibt.
F: Was unterscheidet Verbraucher- und Erzeugerpfeilsystem?
A: Im Verbraucherpfeilsystem zeigen Strom- und Spannungspfeil gleichsinnig, im Erzeugerpfeilsystem gegensinnig. Die Pfeilanordnung legt fest, wie Vorzeichen von Spannung, Strom und Leistung zu deuten sind.
F: Warum passt das Verbraucherpfeilsystem zum Widerstand?
A: Der technische Strom fließt durch einen Verbraucher vom höheren zum niedrigeren Potenzial, also in Spannungsrichtung — das ist genau gleichsinnig. Deshalb gilt dort das Ohmsche Gesetz ohne Vorzeichenärger als $U=RI$.
F: Warum passt das Erzeugerpfeilsystem zur Quelle?
A: Eine Batterie treibt den Strom in ihrem Inneren vom Minus- zum Pluspol, also gegen das Spannungsgefälle. Strom- und Spannungspfeil liegen dann gegensinnig, was das Erzeugerpfeilsystem kennzeichnet.
F: Warum wählt man üblicherweise Verbraucher im VZS und Quellen im EZS?
A: Dann kommen die „erwarteten" Größen mit positivem Vorzeichen heraus — der Verbraucher nimmt Leistung auf ($P>0$), die Quelle gibt sie ab ($P>0$). Das macht die Ergebnisse intuitiv lesbar.
F: Was bedeutet ein positives $P$ im VZS gegenüber dem EZS?
A: Im Verbraucherpfeilsystem heißt $P>0$, das Bauteil nimmt Energie auf (z. B. der Widerstand erwärmt sich); im Erzeugerpfeilsystem heißt $P>0$, es gibt Energie ab. Dasselbe Produkt $UI$, nur je nach System anders gedeutet.
F: Wie erkennt man an der berechneten Leistung, ob ein Bauteil Verbraucher oder Quelle ist?
A: Das Vorzeichen von $P=UI$ im gewählten System verrät es direkt — unabhängig davon, wie man das Bauteil anfangs angenommen hat. Ein unerwartetes Vorzeichen zeigt, dass es tatsächlich die andere Rolle spielt.
F: Was passiert, wenn man Strom- und Spannungspfeil inkonsistent einträgt?
A: Dann stimmen die Vorzeichenregeln für Ohmsches Gesetz und Leistung nicht mehr, und man kann aus dem Ergebnis nicht mehr ablesen, ob aufgenommen oder abgegeben wird. Entscheidend ist nicht die Wahl des Systems, sondern dass man innerhalb einer Rechnung konsequent bleibt.
:::
