---
title: Stufe 7: Lineare Ersatzschaltungen
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Halbleiter und Dioden
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

⁠*Annahme 1: Beide leiten.* Die Knotenregel ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) an X lautet $(4{,}3\,\mathrm{V}-\varphi_\mathrm X)/R_1+(1{,}3\,\mathrm{V}-\varphi_\mathrm X)/R_2=\varphi_\mathrm X/R_3$. Daraus folgt $\varphi_\mathrm X=2{,}24$ V, $I_\mathrm{D1}=2{,}06$ mA und $I_\mathrm{D2}=-0{,}94$ mA. Der negative Strom ist ein Widerspruch.

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
