---
title: Stufe 5: Bauformen und Selbstentladung
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Kondensator
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Kapitel 3: Der Kondensator
order: 1130600
summary: 100 µF als Plattenpaar in Luft wären 3,4 Hektar groß.
tags: Elektrolyt, gepolt, Selbstheilend, Leckstrom, Isolationswiderstand
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
100 µF als Plattenpaar in Luft wären 3,4 Hektar groß. Reale Kondensatoren lösen das über $A$, $d$ und $\varepsilon$. Jede Bauform zahlt dafür einen eigenen Preis.
:::

**Die Idee.** Gleichung [(4.1)](plattenkondensator-und-dielektrikum.html#gl-4-1) hat drei Stellschrauben, alle Bauformen drehen daran (Abb. [5](#abb-5)).

<ul>

<li>

⁠**Folienkondensator:** Zwei lange Metallstreifen, getrennt durch Kunststofffolie oder Papier, sind zu einem Wickel gerollt. So liegt eine große Fläche auf kleinem Raum.

</li>

<li>

⁠**Keramikkondensator:** Eine Keramik mit großem $\varepsilon_\mathrm{r}$, oft in vielen dünnen Lagen übereinander, die parallel geschaltet sind (Stufe [7](parallel-und-reihenschaltung.html#stufe-7)). Der Preis: $\varepsilon_\mathrm{r}$ hängt von Spannung und Temperatur ab.

</li>

<li>

⁠**Elektrolytkondensator (Elko):** Die Elektrode ist aufgeraute Aluminiumfolie. Das vergrößert $A$. Das Dielektrikum ist eine Oxidschicht von nur einigen zehn Nanometern, das macht $d$ klein. Die Gegenelektrode ist eine leitende Flüssigkeit, der __Elektrolyt__, denn nur sie folgt jeder Vertiefung. Der Preis: Der Elko ist __gepolt__, das Oxid hält nur in einer Richtung. Falsch angeschlossen baut es sich ab, Strom fließt, das Bauteil erhitzt sich und kann platzen.

</li>

<li>

⁠**Supercap (auch Goldcap):** An einer porösen Kohleelektrode mit riesiger innerer Oberfläche lagern sich Ionen des Elektrolyten im Abstand von rund 1 nm an. Das ergibt Kapazitäten bis 100 F und mehr. Der Preis: nur einige Volt, darüber zersetzt sich der Elektrolyt, und vergleichsweise hoher Leckstrom.

</li>

</ul>

:::abbildung et1/k3bauform 5
Vier Wege zu großer Kapazität, schematische Schnitte, nicht maßstäblich. Rot und blau die beiden Elektroden, beim Elko orange das Oxid über dem Aluminium, hellblau der Elektrolyt. Beim Supercap sitzen die Ionen dicht an der Kohle.
:::

| Bauform | Kapazität | Spannung | Baugröße | gepolt | selbstheilend |
|---|---|---|---|---|---|
| Papier, Metallpapier | 100 pF bis 50 µF | 125 V bis 1 kV | groß | nein | nur metallisiert |
| Kunststofffolie | 2 pF bis 200 µF | 50 V bis 5 kV | mittel bis sehr klein | nein | nur metallisiert |
| Keramik | 0,5 pF bis 100 µF | 6 V bis 1 kV | klein | nein | nein |
| Elektrolyt | 0,5 µF bis 10 mF | 3 V bis 650 V | sehr klein | ja | ja |
| Supercap | 0,1 F bis über 100 F | einige Volt | sehr klein | ja | nein |

Die Tabelle fasst die üblichen Bereiche zusammen. __Selbstheilend__ heißt: Bei einem Durchschlag verdampft die dünne Metallschicht rund um die Fehlstelle, der Kurzschluss verschwindet, und nur eine winzige Fläche geht verloren. Beim Elko bildet sich das Oxid an der Fehlstelle neu.

**Selbstentladung.** Kein Isolator ist vollkommen. Das Dielektrikum enthält wenige bewegliche Ladungen, deshalb fließt ein winziger Strom von Platte zu Platte, der __Leckstrom__. Im Ersatzbild liegt parallel zum idealen Kondensator ein __Isolationswiderstand__ $R_\mathrm{I}$. Ideal ist $R_\mathrm{I}\to\infty$ und ein abgetrennter Kondensator hält seine Ladung für immer. Real gibt er sie im Takt $R_\mathrm{I}\,C$ ab (Stufe [10](entladen-und-zeitkonstante.html#stufe-10)). Mit dem spezifischen Widerstand $\rho$ des Stoffs ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) ist $R_\mathrm{I}=\rho\,d/A$, zusammen mit [(4.1)](plattenkondensator-und-dielektrikum.html#gl-4-1) folgt

<span class="anker" id="gl-5-1"></span>
$$R_\mathrm{I}\,C=\rho\,\varepsilon. \tag{5.1}$$

$A$ und $d$ kürzen sich: Die Selbstentladung hängt nur vom Stoff ab, nicht von der Baugröße.

::::beispiel
Kunststofffolie mit $\rho\approx10^{16}\,\Omega\,$m und $\varepsilon_\mathrm{r}=2{,}2$ ergibt rund zwei Tage. Bei einem 100-µF-Elko an 9 V nennen Datenblätter höchstens rund 9 µA Leckstrom, also $R_\mathrm{I}\approx1\,\mathrm{M\Omega}$. Das ist 100-mal mehr als $R$ im RC-Kreis, der Leckstrom beträgt 1 % von 0,9 mA und entfällt in den folgenden Stufen.
::::

⁠**Grenzfall:** Für $\rho\to\infty$ wächst $R_\mathrm{I}\,C$ unbegrenzt, das ist der ideale Kondensator ohne Selbstentladung.

:::frage Warum nimmt man nicht immer die Bauform mit der größten Kapazität?
Weil jede Bauform ihren Preis hat. Elkos sind gepolt und haben große Toleranzen, Supercaps halten nur wenige Volt. Wo die Spannung das Vorzeichen wechselt oder die Kapazität genau stimmen muss, nimmt man Folie oder Keramik.
:::

:::aufgabe Aufgabe 6 ★ Ein Elko nachgerechnet
<span class="anker" id="aufg-6"></span>

Ein Elko mit 100 µF und 16 V hat eine Oxidschicht mit $\varepsilon_\mathrm{r}=9$ und einer Dicke von 1,4 nm je Volt.

<ol class="al">

<li>

Wie dick ist das Oxid, und welche Fläche braucht man?

</li>

<li>

Im Becher findet ein Streifen von 3 cm mal 20 cm Platz. Um welchen Faktor muss das Aufrauen die Oberfläche vergrößern?

</li>

<li>

Warum ergäbe eine glatte Gegenelektrode aus Metall diesen Gewinn nicht?

</li>

</ol>

:::loesung
(a) $d=16\cdot1{,}4\,\mathrm{nm}=22{,}4$ nm. $A=\dfrac{C\,d}{\varepsilon_0\varepsilon_\mathrm{r}}=\dfrac{10^{-4}\,\mathrm{F}\cdot22{,}4\cdot10^{-9}\,\mathrm{m}}{9\cdot8{,}854\cdot10^{-12}\,\mathrm{F/m}}=281\,\mathrm{cm^2}$.

(b) Der Streifen hat 60 cm$^2$, also ist ein Faktor $281/60=4{,}7$ nötig.

(c) Eine feste Gegenelektrode berührte nur die Spitzen der rauen Fläche. Die Vertiefungen trügen nichts bei, und der Abstand wäre dort viel größer als das Oxid dick ist. Nur eine Flüssigkeit folgt der Oberfläche im Abstand $d$.
:::
:::
