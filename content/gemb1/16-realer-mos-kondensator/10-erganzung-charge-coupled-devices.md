---
title: Stufe 8: Ergänzung: Charge-Coupled Devices
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der reale MOS-Kondensator
order: 4261000
summary: Ein Kondensator in Tiefenverarmung ist ein leerer Topf für Elektronen.
tags: CCD, Belichtungsphase, Auslesephase, Dunkelrauschen
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Ein Kondensator in Tiefenverarmung ist ein leerer Topf für Elektronen. Diese Stufe zeigt, wie aus vielen solchen Töpfen ein Bildsensor wird.
:::

**Die Idee.** Ladungsgekoppelte Bauelemente (kurz __CCD__) sind große Felder von MOS-Kondensatoren. Sie dienen als Bildsensoren, zum Beispiel in Digitalkameras. Eine Zelle hat eine dünne lichtdurchlässige Elektrode, ein lichtdurchlässiges Oxid und einen dotierten Halbleiter. Auf einem p-Substrat liegt positive Spannung am Gate, die Bänder biegen nach unten, und für Elektronen entsteht an der Grenzfläche ein Potentialtopf. Er ist leer, die Struktur steht in Tiefenverarmung. In der __Belichtungsphase__ erzeugt Licht mit $h\nu>E_\mathrm g$ in der Zone Elektron-Loch-Paare. Das Feld treibt die Elektronen zum Isolator, der sie aufhält, und die Löcher ins Substrat. Der Topf füllt sich, die Zahl der Elektronen misst die Lichtmenge. In der __Auslesephase__ wird die Ladung getaktet seitlich von Kondensator zu Kondensator weitergegeben, bis sie die Ausleseelektronik am Rand des Feldes erreicht.

:::abbildung gemb1/k16ccd 8
Drei-Phasen-CCD mit zwei Zellen, schematisch. Die Linien zeigen die Energie eines Elektrons an der Grenzfläche, tiefer bedeutet höhere Gatespannung. Takt a: Ladung unter den Elektroden 1. Takt b: $V_2$ steigt über $V_1$, die Elektronen rutschen nach rechts. Takt c: $V_1$ sinkt, die Ladung liegt unter den Elektroden 2.
:::

:::definition Definition 8.1 (Drei-Phasen-CCD)
<span class="anker" id="satz-8-1"></span>

Jede Speicherzelle besteht aus drei MOS-Kondensatoren. Alle Kondensatoren 1 hängen an der Spannung $V_1$, alle Kondensatoren 2 an $V_2$, alle Kondensatoren 3 an $V_3$. Ein Schritt hat drei Takte (Abb. [8](#abb-8)):

<ol class="al">

<li>

$V_1>V_2=V_3$: Nur unter den Kondensatoren 1 herrscht Inversion, dort liegt die Ladung.

</li>

<li>

$V_2>V_1>V_3$: Die Kondensatoren 2 sind stärker in Richtung Inversion vorgespannt, die Ladung fließt zu ihnen. $V_3$ bleibt unverändert und sperrt den Rückweg, deshalb kann Kondensator 3 nicht entfallen.

</li>

<li>

$V_2>V_1=V_3$: Kondensator 1 hat keine Inversion mehr, Kondensator 2 hat schwächere Inversion als im Takt b. Die Ladung ist übertragen.

</li>

</ol>
:::

⁠**So liest man das:** Der Ablauf a bis c muss noch zweimal folgen, bis wieder der Ausgangszustand erreicht ist, dann ist die Ladung genau eine Zelle weiter. **Gültigkeit:** Die Elektroden stehen so eng, dass sich die Töpfe benachbarter Kondensatoren berühren.

Thermisch erzeugte Elektronen füllen den Topf auch im Dunkeln. Sie sind das __Dunkelrauschen__ des Sensors. Dagegen hilft eine hohe p-Dotierung: Sie senkt $n=n_\mathrm i^2/p$ und macht die Zone schmaler, in der $j_\mathrm{gen}$ entsteht. Kühlung senkt $n_\mathrm i$ und damit den Effekt weiter.

::::beispiel
Ein Bildpunkt des Rechenmodells mit 5 µ m Kantenlänge hat 43,2 fF. Bei $V_\mathrm G=5$ V reicht die Zone des leeren Topfs 451 nm tief, $\varphi_\mathrm s=4{,}7$ V. Der volle Topf entspricht dem Gleichgewicht, also $|Q'_\mathrm{inv}|\approx C'_\mathrm{IS}(V_\mathrm G-V_\mathrm{th})=807\,\mathrm{nC/cm^2}$ oder $1{,}3\cdot10^{6}$ Elektronen. Jedes Elektron ändert die Spannung um 3,7 µ V. Thermisch entstehen je Sekunde $j_\mathrm{gen}A/e=5\cdot10^{4}$ Elektronen, der Topf wäre nach 25 s voll. Bei 250 K sinkt $n_\mathrm i$ um den Faktor 100, bei 200 K um $9\cdot10^{4}$.
::::

⁠**Grenzfall:** Geht je Schritt ein Bruchteil verloren, addiert sich das. Mit der Übertragungsgüte 0,99999 je Takt bleiben nach 1000 Zellen zu je drei Takten 97 % der Ladung, mit 0,9999 nur 74 %.

:::frage Warum läuft der Topf nicht sofort voll, wenn doch jeder Kondensator ins Gleichgewicht will?
Er läuft voll, aber langsam. Die Belichtung und das Auslesen sind viel kürzer als die Sekunden, die die thermische Erzeugung braucht. Der Sensor lebt davon, dass die Tiefenverarmung lange genug hält.
:::

:::aufgabe Aufgabe 11 ★★ Ein Bildpunkt
<span class="anker" id="aufg-11"></span>

Ein Bildpunkt von 8 µ m $\times$ 8 µ m hat 50 nm $\mathrm{SiO_2}$, es gilt $V_\mathrm G-V_\mathrm{th}=4$ V.

<ol class="al">

<li>

Berechne Kapazität, Ladung und Elektronenzahl des vollen Topfs.

</li>

<li>

Es treffen $2\cdot10^{12}$ Photonen je s und cm$^2$ auf, 60 % davon erzeugen ein gesammeltes Elektron. Wie viele Elektronen sammelt der Bildpunkt in 50 ms, wie voll ist er?

</li>

<li>

Ein Bild hat 2048 Zellen in einer Reihe mit je drei Takten. Welcher Anteil der Ladung aus der entferntesten Zelle kommt bei der Übertragungsgüte 0,9999 und bei 0,99999 an?

</li>

</ol>

:::loesung
(a) $C'_\mathrm{IS}=69{,}1\,\mathrm{nF/cm^2}$, $C=44{,}2$ fF, $Q=C\cdot4\,\mathrm{V}=177$ fC, das sind $1{,}1\cdot10^{6}$ Elektronen. (b) $2\cdot10^{12}\cdot0{,}6\cdot0{,}05\cdot6{,}4\cdot10^{-5}=38\,400$ Elektronen, 3,5 % voll. (c) 6144 Takte: $0{,}9999^{6144}=54\,\%$, $0{,}99999^{6144}=94\,\%$.
:::
:::
