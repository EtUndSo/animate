---
title: Stufe 3: Der OPV ohne Rückführung
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Operationsverstärker
order: 1210500
summary: Aus den Verstärkerstufen wird ein Bauteil mit wenigen Anschlüssen.
tags: Sättigung, ideale OPV, Flash-Wandler
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Aus den Verstärkerstufen wird ein Bauteil mit wenigen Anschlüssen. Diese Stufe legt sein Modell fest und zeigt, was es ohne äußere Beschaltung tut: Es vergleicht.
:::

**Die Idee.** Der OPV hat zwei Eingänge, einen Ausgang und zwei Anschlüsse für die Versorgung $U_\mathrm{B+}$ und $U_\mathrm{B-}$ (Abb. [3](#abb-3)). Einen Masseanschluss hat er nicht: Der Ausgang bezieht sich auf die Mitte der Versorgung. Jeder Ausgangsstrom kommt aus den Versorgungsanschlüssen, die in Schaltbildern meist weggelassen sind. Deshalb erfüllen die sichtbaren drei Anschlüsse die Knotenregel nicht.

Der Ausgang liefert $A$ mal $U_\mathrm{D}$, aber nur bis zu seinen Grenzen. Mit $\pm11$ V und $A=100000$ endet das lineare Stück schon bei $\pm110$ µ V. Jede größere Differenz treibt den Ausgang an einen Anschlag, die __Sättigung__.

:::definition Definition 3.1 (Modell des OPV)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$U_\mathrm{D}=\varphi_+-\varphi_-,\qquad U_\mathrm{A}=\begin{cases}U_\mathrm{A,max}&\text{für }A\,U_\mathrm{D}\ge U_\mathrm{A,max},\\A\,U_\mathrm{D}&\text{dazwischen},\\U_\mathrm{A,min}&\text{für }A\,U_\mathrm{D}\le U_\mathrm{A,min}.\end{cases} \tag{3.1}$$

Der __ideale OPV__ hat $r_\mathrm{e}\to\infty$ (kein Eingangsstrom), $A\to\infty$ bei allen Frequenzen, $r_\mathrm{a}=0$ (der Ausgangsstrom stellt sich so ein, dass alle Knoten- und Maschengleichungen erfüllt sind) und kein Rauschen.
:::

⁠**So liest man das:** $U_\mathrm{A,max}<U_\mathrm{B+}$ und $U_\mathrm{A,min}>U_\mathrm{B-}$, denn zwischen Ausgang und Versorgung liegen Transistoren, an denen Spannung abfällt, hier je 1 V. **Gültigkeit:** Das Modell ist statisch, die Trägheit des Ausgangs folgt in Stufe [4](gegenkopplung.html#stufe-4).

:::abbildung et1/k11opv 3
Links das Schaltzeichen mit Versorgungsanschlüssen. Rechts die Kennlinie im Rechenmodell. Die Steigung ist $A$, das lineare Stück ist nur $\pm110$ µ V breit. Beachte die Achse: Bei einer Skala in Volt wäre es eine senkrechte Stufe.
:::

**Der Komparator.** Ohne Rückführung ist $|U_\mathrm{D}|$ fast immer größer als das Fenster. Der OPV meldet dann nur, welcher Eingang höher liegt: $U_\mathrm{A,max}$ für $\varphi_+>\varphi_-$, $U_\mathrm{A,min}$ für $\varphi_+<\varphi_-$. Das ist der Komparator. Ein Anwendungsfall ist der __Flash-Wandler__, ein Analog-Digital-Wandler (Abb. [4](#abb-4)). Ein Spannungsteiler erzeugt Vergleichsspannungen, jeder Komparator vergleicht $U_\mathrm{E}$ mit einer davon. Alle arbeiten gleichzeitig, daher der Name (flash, Blitz). $n$ Bit brauchen $2^n-1$ Komparatoren, 8 Bit also 255.

:::abbildung et1/k11flash 4
2-Bit-Flash-Wandler mit $U_\mathrm{Ref}=6$ V und gleichen Widerständen. Die Eingänge ziehen keinen Strom, die Widerstände liegen in Reihe, die Abgriffe liegen bei 6, 4 und 2 V. Bei $U_\mathrm{E}=3{,}2$ V schaltet nur K3 nach oben.
:::

::::beispiel
Bei $U_\mathrm{E}=3{,}2$ V ist $U_\mathrm{D}=-2{,}8$ V an K1, $-0{,}8$ V an K2 und $+1{,}2$ V an K3. K1 und K2 stehen auf $-11$ V, K3 auf $+11$ V. Die drei Ausgänge unterscheiden vier Bereiche: unter 2 V, 2 bis 4 V, 4 bis 6 V, über 6 V.
::::

⁠**Grenzfall:** Für $A\to\infty$ wird das Fenster zum Punkt, die Kennlinie zur Stufe bei $U_\mathrm{D}=0$.

:::aufgabe Aufgabe 3 ★ Komparatoren
<span class="anker" id="aufg-3"></span>

(a) Ein Flash-Wandler wie in Abb. [4](#abb-4) hat $U_\mathrm{Ref}=9$ V. Wo liegen die Abgriffe? Welche Komparatoren stehen bei $U_\mathrm{E}=4$ V oben? (b) Wie viele Komparatoren braucht man für 3 Bit? (c) Am OPV V liegen $U_\mathrm{D}=50$ µ V, dann 300 µ V. Wie groß ist jeweils $U_\mathrm{A}$?

:::loesung
(a) 9, 6 und 3 V. Bei 4 V ist nur an K3 $U_\mathrm{D}>0$ ($+1$ V), K1 und K2 haben $-5$ V und $-2$ V. (b) $2^3-1=7$. (c) 5 V im Fenster. Bei 300 µ V wären es 30 V, der Ausgang steht auf 11 V.
:::
:::
