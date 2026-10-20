---
title: Der Operationsverstärker – idealer OPV und Rückkopplung
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Operationsverstärker
order: 120100
summary: Warum der Operationsverstärker ein fast perfekter Verstärkerbaustein ist, was ihn ideal macht und warum erst die Gegenkopplung aus seiner gigantischen Verstärkung eine präzise, berechenbare Schaltung formt.
tags: Operationsverstärker, OPV, idealer OPV, Differenzverstärker, virtueller Kurzschluss, Gegenkopplung
---

:::konzept
Der **Operationsverstärker** (OPV) ist ein fertiger Verstärkerbaustein mit einer schier unglaublichen
Verstärkung — hunderttausendfach und mehr. Allein genutzt wäre diese Verstärkung unbrauchbar, weil schon
Mikrovolt den Ausgang an den Anschlag treiben. Der ganze Trick ist die **Gegenkopplung**: Man führt einen Teil
des Ausgangs auf den Eingang zurück und zähmt den OPV damit so, dass nicht mehr der Chip, sondern ein paar
**äußere Widerstände** das genaue Verhalten bestimmen. Das macht ihn zum vielleicht flexibelsten analogen
Bauteil überhaupt.
:::

**Worum es geht:** Der Transistor verstärkte kräftig, aber ungenau. Der __Operationsverstärker__ bündelt viele
Transistoren zu einem Baustein mit nahezu idealen Eigenschaften. Wir klären, was ein OPV ist, was ihn __ideal__
macht und warum die __Gegenkopplung__ der Schlüssel zu allem Weiteren ist.

## Was ist ein Operationsverstärker?

Ein OPV ist im Kern ein __Differenzverstärker__: Er hat zwei Eingänge — den __invertierenden__ Eingang ($-$) und
den __nichtinvertierenden__ Eingang ($+$) — und einen Ausgang. Er verstärkt nicht eine einzelne Spannung,
sondern die **Differenz** der beiden Eingangsspannungen, und zwar mit der riesigen __Leerlaufverstärkung__
$V_0$:

$$U_\text{a} = V_0 \cdot (U_+ - U_-).$$

- __$U_\text{a}$__: die __Ausgangsspannung__.
- __$U_+, U_-$__: die Spannungen am nichtinvertierenden und invertierenden Eingang.
- __$V_0$__: die __Leerlaufverstärkung__ (Open-Loop-Gain), typisch $10^5$ bis $10^6$.

Diese Verstärkung ist so groß, dass der Ausgang schon bei winzigen Eingangsdifferenzen in die Begrenzung läuft
(an die Versorgungsspannung, die __Sättigung__). Ohne weitere Maßnahme ist der OPV deshalb nur als Komparator
(Vergleicher) brauchbar — für lineare Verstärkung braucht es die Gegenkopplung.

:::grafik
Das OPV-Schaltsymbol (Dreieck) mit nichtinvertierendem Eingang ($+$) oben, invertierendem ($-$) unten und dem
Ausgang an der Spitze, dazu die Versorgungsanschlüsse. Daneben die Übertragungskennlinie: eine extrem steile
Gerade durch den Ursprung, die sofort in die Sättigung $\pm U_\text{sat}$ läuft.
:::

## Der ideale Operationsverstärker

Für das Verständnis rechnet man zunächst mit dem __idealen OPV__ — einer Idealisierung, der reale Bauteile sehr
nahekommen. Er hat vier Eigenschaften:

| Eigenschaft | idealer Wert | Bedeutung |
|---|---|---|
| Leerlaufverstärkung $V_0$ | $\to \infty$ | verstärkt die Differenz unendlich stark |
| Eingangswiderstand $R_\text{ein}$ | $\to \infty$ | in die Eingänge fließt **kein** Strom |
| Ausgangswiderstand $R_\text{aus}$ | $0$ | der Ausgang ist eine ideale Spannungsquelle |
| Bandbreite | $\to \infty$ | verstärkt alle Frequenzen gleich |

Dazu kommt: Die __Gleichtaktverstärkung__ ist null (nur die Differenz zählt, nicht das gemeinsame Niveau beider
Eingänge), und es gibt keine Offset-Fehler. Mit diesen Annahmen werden OPV-Schaltungen erstaunlich einfach
berechenbar.

## Gegenkopplung und die goldenen Regeln

Die __Gegenkopplung__ (negative Rückkopplung) führt einen Teil der Ausgangsspannung auf den **invertierenden**
Eingang zurück. Das wirkt wie eine selbsttätige Regelung: Der OPV stellt seinen Ausgang gerade so ein, dass die
Differenz an seinen Eingängen verschwindet. Daraus folgen zwei Regeln, die das Rechnen mit idealen OPV auf
wenige Zeilen verkürzen — die __goldenen Regeln__:

**Regel 1 — kein Eingangsstrom.** Wegen des unendlichen Eingangswiderstands fließt in beide Eingänge **kein
Strom**: $I_+ = I_- = 0$. Diese Regel gilt immer, unabhängig von der Beschaltung.

**Regel 2 — virtueller Kurzschluss.** Bei Gegenkopplung regelt der OPV so, dass beide Eingänge auf **gleichem
Potenzial** liegen: $U_+ = U_-$. Man nennt das den __virtuellen Kurzschluss__ (und, wenn der $+$-Eingang auf
Masse liegt, die __virtuelle Masse__). Der Grund: Für einen endlichen Ausgang $U_\text{a}$ muss bei $V_0 \to
\infty$ die Differenz $U_+ - U_- = U_\text{a}/V_0$ gegen null gehen. **Wichtig:** Diese Regel gilt nur bei
**negativer** Rückkopplung — bei Mitkopplung (positiver Rückkopplung) entstehen stattdessen Kipp- und
Schwingschaltungen.

**Anders betrachtet.** Der virtuelle Kurzschluss ist „virtuell", weil die beiden Eingänge zwar auf gleicher
Spannung liegen, aber nicht wirklich leitend verbunden sind — es fließt ja (Regel 1) kein Strom zwischen ihnen.
Der OPV *macht* die Differenz null, indem er seinen Ausgang nachführt, nicht indem er die Eingänge kurzschließt.

:::grafik
Ein gegengekoppelter OPV (ein Rückführwiderstand vom Ausgang zum $-$-Eingang). Hervorgehoben die zwei goldenen
Regeln: an beiden Eingängen „$I = 0$" (durchgestrichener Strompfeil) und zwischen den Eingängen „$U_+ = U_-$"
(virtueller Kurzschluss, gestrichelte Verbindung).
:::

## Warum Gegenkopplung?

Der Gewinn der Gegenkopplung ist derselbe wie beim Emitterwiderstand des Transistors: Man **tauscht überschüssige
Verstärkung gegen Präzision**. Die gigantische, aber ungenaue und temperaturabhängige Leerlaufverstärkung $V_0$
wird durch die Rückkopplung auf einen kleineren, dafür **exakt durch äußere Widerstände festgelegten** Wert
gebracht. Zusätzlich wird die Schaltung linearer, stabiler und breitbandiger. Deshalb werden praktisch alle
linearen OPV-Schaltungen gegengekoppelt — und genau deshalb lässt sich ihr Verhalten allein aus den beiden
goldenen Regeln und ein paar Widerständen berechnen.

:::kern
Der __Operationsverstärker__ ist ein __Differenzverstärker__ mit riesiger __Leerlaufverstärkung__
$U_\text{a} = V_0(U_+ - U_-)$, $V_0 \sim 10^5\ldots10^6$. Der __ideale OPV__ hat $V_0 \to \infty$,
$R_\text{ein} \to \infty$ (kein Eingangsstrom), $R_\text{aus} = 0$ und unendliche Bandbreite. Mit
__Gegenkopplung__ gelten die __goldenen Regeln__: (1) $I_+ = I_- = 0$ (immer), (2) $U_+ = U_-$ (__virtueller
Kurzschluss__, nur bei negativer Rückkopplung). Die Gegenkopplung tauscht überschüssige Verstärkung gegen
Präzision — äußere Widerstände legen das Verhalten fest.
:::

Mit diesen beiden Regeln als Werkzeug lassen sich die wichtigsten __Grundschaltungen__ des Operationsverstärkers
in jeweils wenigen Zeilen herleiten — invertierender und nichtinvertierender Verstärker, Spannungsfolger,
Addierer und mehr.

:::quiz
F: Was verstärkt ein Operationsverstärker genau?
A: Nicht eine einzelne Spannung, sondern die Differenz seiner beiden Eingänge: $U_a=V_0(U_+-U_-)$. Er ist im Kern ein Differenzverstärker mit sehr großer Leerlaufverstärkung.
F: Warum ist der OPV ohne Beschaltung nur als Komparator brauchbar?
A: Seine Leerlaufverstärkung ist so riesig ($10^5$–$10^6$), dass schon Mikrovolt Eingangsdifferenz den Ausgang in die Sättigung treiben. Er kann dann nur „größer/kleiner" melden, nicht linear verstärken.
F: Was bedeutet der unendliche Eingangswiderstand des idealen OPV praktisch?
A: In die Eingänge fließt kein Strom ($I_+=I_-=0$). Die Quelle am Eingang wird also nicht belastet, was das Rechnen stark vereinfacht.
F: Was bedeutet der Ausgangswiderstand null?
A: Der Ausgang verhält sich wie eine ideale Spannungsquelle und hält seine Spannung unabhängig von der Last. Nachfolgende Stufen können ihn belasten, ohne dass die Ausgangsspannung einbricht.
F: Warum verschwindet beim idealen OPV die Gleichtaktverstärkung?
A: Er verstärkt nur die *Differenz* der Eingänge, nicht ihr gemeinsames Niveau. Hebt man beide Eingänge gleich an, ändert sich der Ausgang idealerweise nicht.
F: Was besagt die erste goldene Regel und wann gilt sie?
A: In beide Eingänge fließt kein Strom ($I_+=I_-=0$), weil der Eingangswiderstand unendlich ist. Diese Regel gilt immer, unabhängig von der Beschaltung.
F: Woher kommt der virtuelle Kurzschluss ($U_+=U_-$)?
A: Für einen endlichen Ausgang muss bei $V_0\to\infty$ die Eingangsdifferenz $U_+-U_-=U_a/V_0$ gegen null gehen. Der gegengekoppelte OPV regelt seinen Ausgang gerade so, dass beide Eingänge auf gleichem Potenzial liegen.
F: Warum heißt der virtuelle Kurzschluss „virtuell"?
A: Die Eingänge liegen zwar auf gleicher Spannung, sind aber nicht leitend verbunden — zwischen ihnen fließt kein Strom (Regel 1). Der OPV *erzeugt* die Gleichheit durch Nachführen des Ausgangs, nicht durch eine echte Verbindung.
F: Warum gilt die zweite goldene Regel nur bei negativer Rückkopplung?
A: Nur die Gegenkopplung regelt die Differenz selbsttätig auf null. Bei Mitkopplung (positiver Rückkopplung) verstärkt sich jede Abweichung, und es entstehen Kipp- und Schwingschaltungen statt eines virtuellen Kurzschlusses.
F: Was ist der eigentliche Gewinn der Gegenkopplung?
A: Sie tauscht überschüssige, aber ungenaue Verstärkung gegen Präzision: Das Verhalten wird durch exakte äußere Widerstände festgelegt statt durch den streuenden Chip. Zusätzlich wird die Schaltung linearer, stabiler und breitbandiger.
:::
