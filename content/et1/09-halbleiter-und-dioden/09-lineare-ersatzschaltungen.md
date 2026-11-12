---
title: Stufe 7: Lineare Ersatzschaltungen
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Halbleiter und Dioden
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Kapitel 9: Halbleiter und Dioden
order: 1190900
summary: Mit mehreren Dioden koppeln sich mehrere Exponentialgleichungen, und von Hand geht das nicht mehr.
tags: Ideale Diode, Diode mit Durchlassspannung, Durchlassspannung
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Mit mehreren Dioden koppeln sich mehrere Exponentialgleichungen, und von Hand geht das nicht mehr. Diese Stufe ersetzt die Diode durch lineare Teile und gibt ein Verfahren, das immer funktioniert.
:::

**Die Idee.** Über drei Stromdekaden ändert sich $U_\mathrm D$ nur um 180 mV. Die Kennlinie ist also fast ein rechter Winkel, und das Bauteil fast ein Schalter. Der Preis des Modells: Man muss den Schaltzustand jeder Diode kennen. Man nimmt ihn an und prüft ihn hinterher.

:::abbildung et1/k9ersatz 9
Oben links: reale Kennlinie (blau), ideale Diode (grün) und Modell mit $U_\mathrm F=0{,}7$ V (rot). Oben rechts: Die Ersatzschaltungen beider Modelle im leitenden und sperrenden Zustand. Unten: Beispiel mit zwei Dioden und seinem Ergebnis.
:::

:::definition Definition 7.1 (Zwei Diodenmodelle)
<span class="anker" id="satz-7-1"></span>

__Ideale Diode__: leitend ein Kurzschluss, sperrend ein Leerlauf.

<span class="anker" id="gl-7-1"></span>
$$I_\mathrm D>0\ \Rightarrow\ U_\mathrm D=0,\qquad U_\mathrm D<0\ \Rightarrow\ I_\mathrm D=0. \tag{7.1}$$

__Diode mit Durchlassspannung__: leitend eine Spannungsquelle $U_\mathrm F$, sperrend ein Leerlauf.

<span class="anker" id="gl-7-2"></span>
$$I_\mathrm D>0\ \Rightarrow\ U_\mathrm D=U_\mathrm F,\qquad U_\mathrm D<U_\mathrm F\ \Rightarrow\ I_\mathrm D=0. \tag{7.2}$$
:::

⁠**So liest man das:** $U_\mathrm F$ heißt __Durchlassspannung__, auch Flussspannung. Sie ist kein Materialwert wie $U_\mathrm{D0}$ und keine Schwelle, sondern ein Modellwert: Man wählt die Spannung beim erwarteten Strom. Üblich sind 0,6 V oder 0,7 V. Die Modelldiode hat 0,6 V bei 0,12 mA und 0,7 V bei 5,8 mA. **Gültigkeit:** Im Rechenmodell ist exakt $I=4{,}31$ mA. Die ideale Diode ergibt 5,00 mA (16 % zu viel), $U_\mathrm F=0{,}7$ V ergibt 4,30 mA ($-0{,}2$ %), $U_\mathrm F=0{,}6$ V ergibt 4,40 mA (2 % zu viel). Die ideale Diode genügt erst, wenn die Spannungen in der Schaltung groß gegen 0,7 V sind.

**Das Verfahren.**

<ol>

<li>

Wähle eine Ersatzschaltung für die Dioden.

</li>

<li>

Nimm plausibel an, welche Diode leitet und welche sperrt.

</li>

<li>

Ersetze die Dioden und berechne alle Ströme und Spannungen.

</li>

<li>

Prüfe: Leitende Dioden brauchen $I_\mathrm D>0$, sperrende $U_\mathrm D<U_\mathrm F$. Bei einem Widerspruch wähle eine neue Annahme.

</li>

</ol>

$n$ Dioden haben $2^n$ Kombinationen, also lohnt eine gute erste Annahme. Hilfreich ist ein Blick auf die Potenziale.

::::beispiel
Abb. [9](#abb-9) unten: 5 V und 2 V speisen über je 1 k$\Omega$ und eine Diode den Knoten X, von dort führt $R_3=2\,\mathrm{k\Omega}$ zur Masse. $U_\mathrm F=0{,}7$ V.

⁠*Annahme 1: Beide leiten.* Die Knotenregel ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) an X lautet $(4{,}3\,\mathrm{V}-\varphi_\mathrm X)/R_1+(1{,}3\,\mathrm{V}-\varphi_\mathrm X)/R_2=\varphi_\mathrm X/R_3$. Daraus folgt $\varphi_\mathrm X=2{,}24$ V, $I_\mathrm{D1}=2{,}06$ mA und $I_\mathrm{D2}=-0{,}94$ mA. Der negative Strom ist ein Widerspruch.

⁠*Annahme 2: D$_1$ leitet, D$_2$ sperrt.* Dann ist $I=(5\,\mathrm{V}-0{,}7\,\mathrm{V})/3\,\mathrm{k\Omega}=1{,}43$ mA und $\varphi_\mathrm X=2{,}87$ V. An D$_2$ liegt $U_\mathrm{D2}=2\,\mathrm{V}-2{,}87\,\mathrm{V}=-0{,}87$ V. Das ist kleiner als $U_\mathrm F$, kein Widerspruch. Die AP sind D$_1$ (0,7 V | 1,43 mA) und D$_2$ ($-0{,}87$ V | 0). Die volle Simulation liefert 2,89 V und 1,45 mA.

⁠*Potenzialblick:* D$_2$ leitet nur, wenn $\varphi_\mathrm X<2\,\mathrm{V}-0{,}7\,\mathrm{V}=1{,}3$ V ist. Schon die 5-V-Quelle allein hebt X auf 2,87 V, die Kathode von D$_2$ liegt also über der Anode. Die höhere Spannung setzt sich durch. Annahme 3 (nur D$_2$ leitet) ergäbe $U_\mathrm{D1}=4{,}13$ V, Annahme 4 (beide sperren) $U_\mathrm{D1}=5$ V, beide größer als $U_\mathrm F$ und damit Widersprüche.
::::

⁠**Grenzfall:** Bei $U_2=5$ V sind beide Zweige gleich, und jede Diode trägt die Hälfte.

:::frage Warum ist ein negativer Strom ein Widerspruch? Eine Spannungsquelle kann doch Strom aufnehmen.
Die Ersatzquelle kann das, die Diode nicht: In Sperrrichtung fließt nur $I_\mathrm S$. Das Modell gilt nur für $I_\mathrm D>0$. Ein negatives Ergebnis zeigt, dass die Rechnung die Diode außerhalb dieses Bereichs benutzt hat.
:::

:::aufgabe Aufgabe 8 ★★ Wer gewinnt?
<span class="anker" id="aufg-8"></span>

Im Beispiel wird die 2-V-Quelle zur Quelle $U_2$.

<ol class="al">

<li>

Sei $U_2=4{,}5$ V. Welche Dioden leiten? Berechne $\varphi_\mathrm X$ und alle Diodenströme.

</li>

<li>

Ab welchem $U_2$ beginnt D$_2$ zu leiten?

</li>

</ol>

:::loesung
(a) Annahme: Beide leiten. $(4{,}3\,\mathrm{V}-\varphi_\mathrm X)/R_1+(3{,}8\,\mathrm{V}-\varphi_\mathrm X)/R_2=\varphi_\mathrm X/R_3$ ergibt $\varphi_\mathrm X=3{,}24$ V, $I_\mathrm{D1}=1{,}06$ mA, $I_\mathrm{D2}=0{,}56$ mA. Beide positiv, kein Widerspruch. Kontrolle: $1{,}62\,\mathrm{mA}\cdot2\,\mathrm{k\Omega}=3{,}24$ V. (b) Solange D$_2$ sperrt, ist $\varphi_\mathrm X=2{,}87$ V. D$_2$ beginnt zu leiten, wenn $U_2-0{,}7\,\mathrm{V}=2{,}87$ V ist, also bei $U_2=3{,}57$ V.
:::
:::

:::aufgabe Aufgabe 9 ★★★ Schutzdioden
<span class="anker" id="aufg-9"></span>

Der Eingang eines Chips ist der Knoten X. Eine Spannung $U_\mathrm e$ speist ihn über $R=1\,\mathrm{k\Omega}$. D$_1$ führt von X (Anode) zur Versorgung $+5$ V. D$_2$ führt von der Masse (Anode) nach X. $U_\mathrm F=0{,}7$ V.

<ol class="al">

<li>

Bestimme für $U_\mathrm e=3$ V, $12$ V und $-3$ V, welche Diode leitet, sowie $\varphi_\mathrm X$ und den Strom durch $R$.

</li>

<li>

Skizziere $\varphi_\mathrm X$ über $U_\mathrm e$.

</li>

<li>

Warum entfällt eine der vier Kombinationen ohne Rechnung?

</li>

</ol>

:::loesung
(a) $U_\mathrm e=3$ V: Keine Diode leitet, $I=0$, $\varphi_\mathrm X=3$ V. Prüfung: $U_\mathrm{D1}=-2$ V, $U_\mathrm{D2}=-3$ V. $U_\mathrm e=12$ V: D$_1$ leitet, $\varphi_\mathrm X=5{,}7$ V, $I=6{,}3$ mA fließt in die Versorgung. $U_\mathrm e=-3$ V: D$_2$ leitet, $\varphi_\mathrm X=-0{,}7$ V, $I=-2{,}3$ mA, der Strom kommt aus der Masse. (b) Eine Rampe $\varphi_\mathrm X=U_\mathrm e$ zwischen $-0{,}7$ V und 5,7 V, außerhalb waagerecht: Der Eingang bleibt geschützt. (c) Leiten beide, müsste $\varphi_\mathrm X$ zugleich 5,7 V und $-0{,}7$ V sein.
:::
:::

::::formelsammlung
**Ideale Diode**

$$I_\mathrm D>0\ \Rightarrow\ U_\mathrm D=0,\qquad U_\mathrm D<0\ \Rightarrow\ I_\mathrm D=0$$

Leitend ein Kurzschluss, sperrend ein Leerlauf. Genügt, wenn die Spannungen in der Schaltung groß gegen 0,7 V sind.

**Diode mit Durchlassspannung**

$$I_\mathrm D>0\ \Rightarrow\ U_\mathrm D=U_\mathrm F,\qquad U_\mathrm D<U_\mathrm F\ \Rightarrow\ I_\mathrm D=0$$

Leitend eine Spannungsquelle $U_\mathrm F$, sperrend ein Leerlauf. $U_\mathrm F$ (Durchlass- oder Flussspannung) ist ein Modellwert, meist 0,6 V oder 0,7 V. Prüfung nach der Rechnung: leitende Dioden $I_\mathrm D>0$, sperrende $U_\mathrm D<U_\mathrm F$.

**Zahl der Kombinationen**

$$2^n$$

Mögliche Annahmen aus Leiten und Sperren für $n$ Dioden.
::::

::::lernkarten
:::karte begriff Ideale Diode
Wie verhält sich die ideale Diode als Ersatzschaltung im leitenden und im sperrenden Zustand?
---
Leitend ist sie ein Kurzschluss, sperrend ein Leerlauf: $I_\mathrm D>0\ \Rightarrow\ U_\mathrm D=0$ und $U_\mathrm D<0\ \Rightarrow\ I_\mathrm D=0$. Die Spannung an der leitenden Diode wird vernachlässigt.
--- falsch
Leitend ist sie ein Widerstand von 0,7 $\Omega$, sperrend ein Widerstand von 1 M$\Omega$, sodass sie in beiden Zuständen eine kleine Spannung trägt.
--- falsch
Leitend ist sie eine Spannungsquelle mit 0,7 V, sperrend ein Leerlauf: Bei $I_\mathrm D>0$ liegt an ihr $U_\mathrm D=0{,}7$ V, sonst ist $I_\mathrm D=0$, wie bei jeder realen Siliziumdiode.
--- falsch
Leitend ist sie ein Kurzschluss, sperrend eine Stromquelle, die den Sperrstrom in den Kreis treibt: Bei $U_\mathrm D<0$ fließt $I_\mathrm D=-I_\mathrm S$.
:::
:::karte begriff Diode mit Durchlassspannung
Wie verhält sich das Modell der Diode mit Durchlassspannung im leitenden und im sperrenden Zustand?
---
Leitend ist sie eine Spannungsquelle $U_\mathrm F$, sperrend ein Leerlauf: $I_\mathrm D>0\ \Rightarrow\ U_\mathrm D=U_\mathrm F$ und $U_\mathrm D<U_\mathrm F\ \Rightarrow\ I_\mathrm D=0$.
--- falsch
Leitend ist sie ein Widerstand mit dem Wert $U_\mathrm F/I_\mathrm D$, sperrend ein Leerlauf. Ihr Strom steigt deshalb im leitenden Zustand linear mit der angelegten Spannung.
--- falsch
Leitend ist sie eine Spannungsquelle $U_\mathrm F$, sperrend ebenfalls, nur umgepolt: Bei $U_\mathrm D<U_\mathrm F$ liegt an ihr $-U_\mathrm F$, und es fließt kein Strom.
--- falsch
Leitend ist sie ein Kurzschluss, sperrend eine Spannungsquelle $U_\mathrm F$, die verhindert, dass Strom fließt, solange die Quelle kleiner als $U_\mathrm F$ ist.
:::
:::karte begriff Durchlassspannung
Was ist die Durchlassspannung $U_\mathrm F$ im Diodenmodell, und wie wählt man ihren Wert?
---
Ein Modellwert, kein Materialwert wie $U_\mathrm{D0}$ und keine Schwelle: Man wählt die Spannung beim erwarteten Strom, üblich sind 0,6 V oder 0,7 V. Sie heißt auch Flussspannung.
--- falsch
Ein Materialwert wie $U_\mathrm{D0}$: die Spannung, ab der die Barriere verschwindet und die Diode zu leiten beginnt. Bei Silizium ist sie immer genau 0,7 V.
--- falsch
Die größte Spannung, die eine Diode in Sperrrichtung aushält, bevor der Durchbruch einsetzt. Man wählt sie aus dem Datenblatt, üblich sind je nach Bauform 50 V bis 1000 V.
--- falsch
Ein Modellwert, den man so wählt, dass der Sperrstrom im Modell richtig herauskommt. Üblich sind 25,85 mV, die Temperaturspannung bei 300 K.
:::
:::karte zusammenhang Diode als Schalter
Warum darf man eine Diode für Handrechnungen durch einen Schalter mit fester Durchlassspannung ersetzen, und was kostet das?
---
Über drei Stromdekaden ändert sich $U_\mathrm D$ nur um 180 mV, die Kennlinie ist fast ein rechter Winkel. Der Preis: Man muss den Schaltzustand jeder Diode annehmen und hinterher prüfen.
--- falsch
Weil die Diode unterhalb von 0,7 V wirklich keinen Strom führt und oberhalb jeden; die Kennlinie hat dort eine echte Schwelle. Das Modell kostet deshalb keine Genauigkeit.
--- falsch
Weil die Diode in Durchlassrichtung ein ohmscher Widerstand mit fester Steigung ist. Der Schalter ersetzt nur den Sperrbereich; der Preis ist ein Fehler von rund 16 %.
--- falsch
Über drei Stromdekaden ändert sich $U_\mathrm D$ nur um 180 mV. Deshalb muss man den Schaltzustand nicht prüfen, denn das Modell stellt ihn von selbst richtig ein.
:::
:::karte zusammenhang Genauigkeit der Diodenmodelle
Wie genau treffen die ideale Diode und das Modell mit $U_\mathrm F=0{,}7$ V den exakten Strom von 4,31 mA einer Diode in Reihe mit 1 k$\Omega$ an 5 V?
---
Die ideale Diode ergibt 5,00 mA, 16 % zu viel, das Modell mit 0,7 V ergibt 4,30 mA. Die ideale Diode genügt erst, wenn die Spannungen in der Schaltung groß gegen 0,7 V sind.
--- falsch
Beide treffen ihn auf 1 % genau, weil an der Diode nur 0,7 V von 5 V abfallen. Die Wahl des Modells spielt bei dieser Schaltung deshalb keine Rolle, erst bei viel größeren Spannungen.
--- falsch
Die ideale Diode ergibt 4,30 mA, das Modell mit 0,7 V ergibt 5,00 mA, 16 % zu viel. Die Durchlassspannung lohnt sich erst bei Spannungen groß gegen 0,7 V.
--- falsch
Die ideale Diode ergibt 5,00 mA, 16 % zu viel, das Modell mit 0,7 V 3,60 mA, weil es die Spannung doppelt abzieht. Beide Modelle sind deshalb gleich ungenau.
:::
:::karte zusammenhang Annehmen, rechnen, prüfen
In welchen Schritten berechnet man eine Schaltung mit mehreren Dioden über lineare Ersatzschaltungen?
---
Ersatzschaltung wählen, plausibel annehmen, welche Diode leitet und welche sperrt, ersetzen und rechnen, dann prüfen: Leitende Dioden brauchen $I_\mathrm D>0$, sperrende $U_\mathrm D<U_\mathrm F$. Bei Widerspruch neu annehmen.
--- falsch
Alle Dioden als leitend ansetzen, alles berechnen und die Dioden mit negativem Strom danach einfach weglassen. Eine zweite Rechnung ist nicht nötig, weil sich die übrigen Ströme dadurch nicht mehr ändern.
--- falsch
Ersatzschaltung wählen, annehmen, welche Diode leitet und welche sperrt, ersetzen und alles berechnen. Eine Prüfung ist nicht nötig, weil jede Annahme zu einer gültigen Lösung führt.
--- falsch
Ersatzschaltung wählen, annehmen, welche Diode leitet, ersetzen und rechnen, dann prüfen: Leitende Dioden brauchen $U_\mathrm D<U_\mathrm F$, sperrende $I_\mathrm D>0$. Bei einem Widerspruch neue Annahme.
:::
:::karte zusammenhang Gute erste Annahme
Warum lohnt sich bei $n$ Dioden eine gute erste Annahme, und was hilft dabei?
---
$n$ Dioden haben $2^n$ Kombinationen aus Leiten und Sperren. Hilfreich ist ein Blick auf die Potenziale: Eine Diode kann nur leiten, wenn ihre Anode um $U_\mathrm F$ über ihrer Kathode liegen kann.
--- falsch
$n$ Dioden haben $n^2$ Kombinationen, und jede muss vollständig durchgerechnet werden. Eine gute Annahme spart deshalb keine Arbeit, sie ändert nur die Reihenfolge.
--- falsch
$n$ Dioden haben $2n$ Kombinationen. Hilfreich ist, zuerst alle Dioden als sperrend anzunehmen, weil diese Annahme immer richtig ist, solange kein Strom fließt.
--- falsch
$n$ Dioden haben $2^n$ Kombinationen. Hilfreich ist, die Diode mit dem kleinsten Vorwiderstand als leitend anzunehmen, weil der Strom immer den Weg des geringsten Widerstands nimmt.
:::
:::karte zusammenhang Negativer Diodenstrom
Warum ist ein negativer Diodenstrom in einer Rechnung mit Ersatzspannungsquelle ein Widerspruch, obwohl eine Spannungsquelle Strom aufnehmen kann?
---
Die Ersatzquelle kann das, die Diode nicht: In Sperrrichtung fließt nur $I_\mathrm S$. Das Modell gilt nur für $I_\mathrm D>0$; ein negatives Ergebnis zeigt, dass die Rechnung die Diode außerhalb dieses Bereichs benutzt hat.
--- falsch
Ein negativer Strom bedeutet, dass die Diode Energie erzeugt, und das verbietet der Energiesatz für jedes Bauteil. Die Spannungsquelle im Modell darf deshalb nie Strom aufnehmen, auch in anderen Schaltungen nicht.
--- falsch
Ein negativer Strom ist gar kein Widerspruch; er zeigt nur, dass der Zählpfeil falsch herum gewählt war. Man dreht den Pfeil um und rechnet mit dem Betrag des Stroms weiter.
--- falsch
Die Ersatzquelle kann das, die Diode nicht, weil sie bei negativem Strom sofort in den Durchbruch gerät. Ein negatives Ergebnis zeigt also, dass die Diode in dieser Schaltung zerstört würde.
:::
:::karte zusammenhang Die höhere Spannung setzt sich durch
Zwei Quellen mit 5 V und 2 V speisen über je 1 k$\Omega$ und eine Diode einen Knoten X, von dem $R_3=2\,\mathrm{k\Omega}$ zur Masse führt. Warum leitet nur die Diode der 5-V-Quelle?
---
Schon die 5-V-Quelle allein hebt X auf 2,87 V. Die Diode der 2-V-Quelle leitet nur für $\varphi_\mathrm X<2\,\mathrm{V}-0{,}7\,\mathrm{V}=1{,}3$ V; ihre Kathode liegt also über der Anode, mit $-0{,}87$ V an der Diode.
--- falsch
Bei zwei parallelen Dioden leitet immer nur eine. Welche es ist, entscheidet der kleinere Vorwiderstand; hier sind beide gleich, und deshalb gewinnt die Diode, die zuerst an der Spannung liegt.
--- falsch
Beide leiten: X liegt bei 2,24 V, und die 2-V-Quelle nimmt dabei 0,94 mA auf. Dass ihr Diodenstrom negativ ist, stört nicht, weil eine Spannungsquelle Strom aufnehmen kann.
--- falsch
Die 5-V-Quelle hebt X auf 4,3 V, weil an ihrer Diode nur 0,7 V abfallen. Damit liegt die Kathode der anderen Diode 2,3 V über ihrer Anode, und diese Diode sperrt.
:::
:::karte zusammenhang Schutzdioden am Chipeingang
Ein Eingang X liegt über D$_1$ (Anode an X) an $+5$ V und über D$_2$ (Anode an Masse) an Masse, mit $U_\mathrm F=0{,}7$ V. Warum können beide Dioden nicht zugleich leiten?
---
Leitet D$_1$, ist $\varphi_\mathrm X=5{,}7$ V; leitet D$_2$, ist $\varphi_\mathrm X=-0{,}7$ V. Beide zugleich verlangten zwei verschiedene Potenziale am selben Knoten, also entfällt diese Kombination ohne Rechnung.
--- falsch
Die beiden Dioden liegen dann in Reihe zwischen Versorgung und Masse. Leiten beide, schließen sie die 5-V-Versorgung kurz, und eine Sicherung im Chip trennt den Eingang ab.
--- falsch
Sie können es doch: Bei einer Eingangsspannung von 12 V leiten beide und teilen sich den Strom von 6,3 mA, sodass X bei 2,5 V liegt.
--- falsch
Eine Diode leitet nur, wenn ihre Anode an einer Quelle hängt. D$_2$ hat ihre Anode an der Masse und leitet deshalb nie, gleich welche Eingangsspannung anliegt.
:::
::::
