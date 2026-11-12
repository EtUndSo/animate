---
title: Stufe 3: Der OPV ohne Rückführung
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Operationsverstärker
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Kapitel 11: Der Operationsverstärker
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

::::formelsammlung
**Modell des OPV**

$$U_\mathrm{D}=\varphi_+-\varphi_-,\qquad U_\mathrm{A}=\begin{cases}U_\mathrm{A,max}&\text{für }A\,U_\mathrm{D}\ge U_\mathrm{A,max},\\A\,U_\mathrm{D}&\text{dazwischen},\\U_\mathrm{A,min}&\text{für }A\,U_\mathrm{D}\le U_\mathrm{A,min}.\end{cases}$$

$A$ ist die Leerlaufverstärkung. Statisches Modell; das lineare Stück ist sehr schmal, im Rechenmodell $\pm110$ µ V. Ohne Rückführung arbeitet der OPV deshalb als Komparator.

**Grenzen des Ausgangs**

$$U_\mathrm{A,max}<U_\mathrm{B+},\qquad U_\mathrm{A,min}>U_\mathrm{B-}$$

Zwischen Ausgang und Versorgung liegen Transistoren, an denen Spannung abfällt.

**Idealer OPV**

$$r_\mathrm{e}\to\infty,\qquad A\to\infty,\qquad r_\mathrm{a}=0$$

Kein Eingangsstrom, unendliche Verstärkung bei allen Frequenzen, der Ausgangsstrom erfüllt alle Knoten- und Maschengleichungen; kein Rauschen.

**Komparatoren eines Flash-Wandlers**

$$2^n-1$$

Zahl der Komparatoren für $n$ Bit; alle vergleichen $U_\mathrm{E}$ gleichzeitig mit den Abgriffen eines Spannungsteilers.
::::

::::lernkarten
:::karte begriff Operationsverstärker
Was ist ein Operationsverstärker, und welche Anschlüsse hat er?
---
Ein integrierter Verstärker aus einigen Dutzend Transistoren, der die Spannung zwischen seinen zwei Eingängen verstärkt. Er hat zwei Eingänge, einen Ausgang und zwei Versorgungsanschlüsse, aber keinen Masseanschluss.
--- falsch
Ein integrierter Verstärker, der die Spannung an einem Eingang gegen Masse verstärkt. Er hat einen Eingang, einen Ausgang und einen Masseanschluss; die Versorgung kommt über den Eingang, der dabei zugleich als Masse dient.
--- falsch
Ein einzelner Transistor mit eingebauter Rechenfunktion. Er hat zwei Eingänge und einen Ausgang; eine Versorgung braucht er nicht, die Energie kommt aus dem Signal.
--- falsch
Ein integrierter Verstärker mit zwei Eingängen und einem Ausgang, dazu einem Masseanschluss, auf den sich alle Spannungen beziehen. Die Versorgung sitzt im Gehäuse.
:::
:::karte begriff Leerlaufverstärkung
Was gibt die Leerlaufverstärkung eines Operationsverstärkers an, und wie genau ist ihr Wert?
---
Den Faktor $A$, mit dem der OPV die Spannung zwischen seinen Eingängen verstärkt, rund 100000. Er schwankt von Exemplar zu Exemplar um den Faktor vier und ändert sich mit der Temperatur.
--- falsch
Die Verstärkung, die der OPV mit einer Rückführung über zwei Widerstände erreicht, etwa 5. Ihr Wert ist sehr genau, weil ihn nur die beiden Widerstände festlegen.
--- falsch
Den Faktor $A$, mit dem der OPV die Spannung zwischen seinen Eingängen verstärkt, rund 100000. Er wird beim Hersteller für jedes Exemplar auf 0,01 % genau abgeglichen und hängt nicht von der Temperatur ab.
--- falsch
Die Verstärkung des OPV, solange am Ausgang keine Last hängt, rund 100000. Mit einer Last fällt sie auf den Wert, den die Widerstände der Rückführung vorgeben.
:::
:::karte formel Modell des OPV
Wie hängt die Ausgangsspannung eines OPV ohne Rückführung von der Differenz seiner Eingangspotenziale ab?
---
$U_\mathrm{D}=\varphi_+-\varphi_-$ und $U_\mathrm{A}=A\,U_\mathrm{D}$, aber nur zwischen $U_\mathrm{A,min}$ und $U_\mathrm{A,max}$. Mit $\pm11$ V und $A=100000$ ist das lineare Stück nur $\pm110$ µ V breit.
--- falsch
$U_\mathrm{D}=\varphi_--\varphi_+$ und $U_\mathrm{A}=A\,U_\mathrm{D}$ zwischen den Grenzen. Mit $\pm11$ V und $A=100000$ ist das lineare Stück der Kennlinie $\pm110$ mV breit.
--- falsch
$U_\mathrm{A}=A\,U_\mathrm{D}$ für jede Differenz: Der Ausgang erreicht beliebig hohe Spannungen, weil im Modell des OPV keine Grenzen vorkommen und der Ausgang jeder Rechnung folgt.
--- falsch
$U_\mathrm{A}=A\,\varphi_+$; der Minus-Eingang dient nur als Bezug für die Versorgung, und der Ausgang folgt dem Plus-Eingang bis $\pm11$ V.
:::
:::karte zusammenhang Sättigung
Was passiert mit dem Ausgang eines OPV ohne Rückführung, wenn die Eingangsdifferenz größer als etwa 110 µ V wird?
---
Er gerät in die Sättigung: Er steht am Anschlag $U_\mathrm{A,max}$ oder $U_\mathrm{A,min}$, hier $\pm11$ V, und folgt $A\,U_\mathrm{D}$ nicht mehr. Bei 300 µ V wären rechnerisch 30 V nötig.
--- falsch
Er steigt weiter mit $A\,U_\mathrm{D}$; bei 300 µ V liefert er die 30 V, die die Rechnung verlangt, weil sein Ausgangsstrom nicht begrenzt ist.
--- falsch
Der OPV schaltet sich zum Schutz ab, und der Ausgang geht auf 0 V zurück, bis die Differenz wieder kleiner als 110 µ V ist.
--- falsch
Er steht am Anschlag, und zwar genau auf der Versorgungsspannung von 12 V, weil zwischen Ausgang und Versorgung keine Spannung abfällt und der Ausgang sie voll erreicht.
:::
:::karte zusammenhang Grenzen des Ausgangs
Warum erreicht der Ausgang eines OPV mit der Versorgung $\pm12$ V nur $\pm11$ V?
---
Zwischen Ausgang und Versorgung liegen Transistoren, an denen Spannung abfällt, hier je 1 V. Deshalb gilt $U_\mathrm{A,max}<U_\mathrm{B+}$ und $U_\mathrm{A,min}>U_\mathrm{B-}$.
--- falsch
Der Eingangswiderstand von 1 M$\Omega$ verbraucht 1 V der Versorgung; mit einem idealen Eingang erreichte der Ausgang die vollen $\pm12$ V.
--- falsch
Der OPV hält 1 V als Reserve für die Gegenkopplung zurück; ohne Rückführung erreicht der Ausgang deshalb die vollen $\pm12$ V.
--- falsch
Am Ausgangswiderstand von 75 $\Omega$ fällt bei jedem Strom genau 1 V ab, auch dann, wenn am Ausgang gar keine Last hängt.
:::
:::karte zusammenhang Kein Masseanschluss
Warum erfüllen die drei Anschlüsse, die ein Schaltbild vom OPV meist zeigt, die Knotenregel nicht?
---
Jeder Ausgangsstrom kommt aus den Versorgungsanschlüssen $U_\mathrm{B+}$ und $U_\mathrm{B-}$, die man in Schaltbildern meist weglässt. Einen Masseanschluss hat der OPV nicht.
--- falsch
Der OPV speichert Ladung in seiner inneren Kapazität; den Ausgangsstrom nimmt er aus diesem Speicher und ersetzt ihn später über die Eingänge.
--- falsch
Die Knotenregel gilt nur für Widerstände und Quellen, nicht für aktive Bauteile; bei einem Verstärker ist sie grundsätzlich verletzt.
--- falsch
Der Ausgangsstrom fließt über den Masseanschluss ab, den man im Schaltbild meist weglässt; die Versorgung liefert keinen Strom an den Ausgang, sondern nur an die Eingänge.
:::
:::karte begriff ideale OPV
Welche Eigenschaften hat der ideale OPV, mit dem man Schaltungen in erster Näherung rechnet?
---
Er hat $r_\mathrm{e}\to\infty$, $A\to\infty$ bei allen Frequenzen, $r_\mathrm{a}=0$ und kein Rauschen. Sein Ausgangsstrom stellt sich so ein, dass alle Knoten- und Maschengleichungen erfüllt sind.
--- falsch
Er hat $r_\mathrm{e}=0$, damit jeder Eingangsstrom ungehindert hineinfließt, $A\to\infty$ und einen unendlichen Ausgangswiderstand, damit die Last ihn nicht belastet und die Spannung voll ankommt.
--- falsch
Er hat $r_\mathrm{e}\to\infty$, $A=1$ und $r_\mathrm{a}=0$; er verstärkt also nicht, sondern gibt die Differenz der Eingänge unverändert und belastbar weiter.
--- falsch
Er hat $r_\mathrm{e}\to\infty$, $A\to\infty$ und $r_\mathrm{a}=0$, aber nur bei Gleichspannung; bei jeder Frequenz über null fällt seine Verstärkung auf 1.
:::
:::karte zusammenhang Komparator
Warum arbeitet ein OPV ohne Rückführung als Komparator?
---
Fast jede Differenz ist größer als das Fenster von $\pm110$ µ V. Er meldet dann nur, welcher Eingang höher liegt: $U_\mathrm{A,max}$ für $\varphi_+>\varphi_-$, $U_\mathrm{A,min}$ für $\varphi_+<\varphi_-$.
--- falsch
Er hat eine eingebaute Schwelle bei 0,6 V: Liegt der Plus-Eingang darüber, schaltet der Ausgang nach oben, sonst nach unten, unabhängig vom Minus-Eingang, der nur als Bezug dient.
--- falsch
Das lineare Fenster ist nur $\pm110$ µ V breit; er meldet $U_\mathrm{A,max}$ für $\varphi_+<\varphi_-$ und $U_\mathrm{A,min}$ für $\varphi_+>\varphi_-$, weil sein Ausgang invertiert.
--- falsch
Ohne Rückführung ist $A$ gleich 1, der Ausgang zeigt die Differenz unverstärkt an; ein angeschlossenes Messgerät mit Skala liest daran ab, welcher der beiden Eingänge höher liegt.
:::
:::karte begriff Flash-Wandler
Was ist ein Flash-Wandler, und woher hat er seinen Namen?
---
Ein Analog-Digital-Wandler, in dem je ein Komparator $U_\mathrm{E}$ mit einem Abgriff eines Spannungsteilers vergleicht. Alle Komparatoren arbeiten gleichzeitig, daher der Name (flash, Blitz).
--- falsch
Ein Analog-Digital-Wandler, der $U_\mathrm{E}$ nacheinander mit immer feineren Schwellen vergleicht; den Namen hat er von einem Lichtblitz, der jeden Vergleich anzeigt.
--- falsch
Ein Digital-Analog-Wandler, der eine Zahl über einen Spannungsteiler in eine Spannung umsetzt; den Namen hat er von den schnellen Sprüngen am Ausgang.
--- falsch
Ein Speicher, der eine Spannung blitzschnell festhält und sie dann mit einem einzigen Komparator gegen eine langsam steigende Rampe vergleicht.
:::
:::karte formel Zahl der Komparatoren
Wie viele Komparatoren braucht ein Flash-Wandler für $n$ Bit, und warum?
---
$2^n-1$: $n$ Bit unterscheiden $2^n$ Bereiche, und zwischen ihnen liegen $2^n-1$ Schwellen. 8 Bit brauchen also 255 Komparatoren.
--- falsch
$n$: Jeder Komparator liefert genau ein Bit der Zahl; 8 Bit brauchen also 8 Komparatoren, die alle gleichzeitig arbeiten und je ein Bit melden.
--- falsch
$2^n$: Jeder der $2^n$ Bereiche braucht seinen eigenen Komparator, auch der unterste; 8 Bit brauchen also 256 Komparatoren.
--- falsch
$2\,n-1$: Jedes Bit braucht zwei Schwellen, von denen sich benachbarte Bits eine teilen; 8 Bit brauchen also 15 Komparatoren.
:::
::::
