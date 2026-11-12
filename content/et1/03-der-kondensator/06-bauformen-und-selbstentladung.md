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

::::formelsammlung
**Isolationswiderstand**

$$R_\mathrm{I}=\rho\,d/A$$

$\rho$ spezifischer Widerstand des Dielektrikums. Im Ersatzbild liegt $R_\mathrm{I}$ parallel zum idealen Kondensator, durch ihn fließt der Leckstrom; ideal ist $R_\mathrm{I}\to\infty$.

**Selbstentladung**

$$R_\mathrm{I}\,C=\rho\,\varepsilon$$

Takt, in dem ein abgetrennter Kondensator seine Ladung verliert. $A$ und $d$ kürzen sich: Die Selbstentladung hängt nur vom Stoff ab, nicht von der Baugröße. Kunststofffolie mit $\rho\approx10^{16}\,\Omega\,$m und $\varepsilon_\mathrm{r}=2{,}2$ ergibt rund zwei Tage.
::::

::::lernkarten
:::karte zusammenhang Drei Stellschrauben
Woran drehen alle Bauformen, um auf kleinem Raum eine große Kapazität zu erreichen?
---
An den drei Größen aus $C=\varepsilon A/d$: große Fläche $A$ durch Wickeln oder Aufrauen, kleiner Abstand $d$ durch dünne Schichten und großes $\varepsilon$.
--- falsch
An Fläche, Abstand und Spannung: große Fläche, großer Abstand und hohe Spannung, weil mehr Spannung mehr Ladung und damit mehr Kapazität ergibt.
--- falsch
An Leitfähigkeit, Dicke und Temperatur der Platten: Je besser und dicker das Metall, desto größer die Kapazität.
--- falsch
An den drei Größen aus $C=\varepsilon A/d$: kleine Fläche $A$, großer Abstand $d$ und kleines $\varepsilon$, damit das Feld stark wird.
:::
:::karte begriff Folienkondensator
Wie erreicht ein Folienkondensator eine große Fläche auf kleinem Raum?
---
Zwei lange Metallstreifen, getrennt durch Kunststofffolie oder Papier, sind zu einem Wickel gerollt.
--- falsch
Eine einzige Metallfolie ist zu einem Wickel gerollt; die Luft zwischen den Windungen dient als Dielektrikum.
--- falsch
Viele dünne Keramiklagen liegen übereinander, und eine Metallfolie umhüllt sie als gemeinsame Elektrode.
--- falsch
Eine aufgeraute Kunststofffolie trägt auf beiden Seiten eine leitende Flüssigkeit, die jeder Vertiefung folgt.
:::
:::karte begriff Keramikkondensator
Welche Stellschraube nutzt ein Keramikkondensator, und welchen Preis zahlt er dafür?
---
Eine Keramik mit großem $\varepsilon_\mathrm{r}$, oft in vielen dünnen, parallel geschalteten Lagen. Der Preis: $\varepsilon_\mathrm{r}$ hängt von Spannung und Temperatur ab.
--- falsch
Eine Keramik mit kleinem $\varepsilon_\mathrm{r}$, die dafür sehr dick sein darf. Der Preis: Er ist gepolt und hält die Spannung nur in einer Richtung.
--- falsch
Eine Keramik mit großem $\varepsilon_\mathrm{r}$ in einer einzigen dicken Lage. Der Preis: Er hält nur einige Volt, darüber zersetzt sich die Keramik.
--- falsch
Eine poröse Keramik mit riesiger innerer Oberfläche, an der sich Ionen anlagern. Der Preis: ein hoher Leckstrom und eine Spannung von nur wenigen Volt.
:::
:::karte begriff Elektrolytkondensator und Elektrolyt
Wie erreicht ein Elektrolytkondensator (Elko) seine große Kapazität, und welche Aufgabe hat der Elektrolyt?
---
Aufgeraute Aluminiumfolie vergrößert $A$, eine Oxidschicht von nur einigen zehn Nanometern macht $d$ klein. Die Gegenelektrode ist eine leitende Flüssigkeit, der Elektrolyt, weil nur sie jeder Vertiefung folgt.
--- falsch
Aufgeraute Aluminiumfolie vergrößert $A$, eine dicke Kunststofffolie macht $\varepsilon$ groß. Der Elektrolyt ist das Dielektrikum: Er trennt die beiden Aluminiumfolien und isoliert sie zuverlässig voneinander, auch bei hoher Spannung.
--- falsch
Eine glatte Aluminiumfolie trägt eine Oxidschicht von einigen Millimetern. Der Elektrolyt kühlt das Bauteil, weil sich das dicke Oxid beim Laden stark erwärmt und sonst zerspringen würde.
--- falsch
Aufgeraute Aluminiumfolie vergrößert $A$, das Oxid macht $d$ klein. Der Elektrolyt ist eine feste Metallschicht als Gegenelektrode, die auf den Spitzen der rauen Fläche aufliegt.
:::
:::karte begriff gepolt
Was bedeutet es, dass ein Elko gepolt ist, und was geschieht, wenn man ihn falsch herum anschließt?
---
Das Oxid hält die Spannung nur in einer Richtung. Falsch angeschlossen baut es sich ab, Strom fließt, das Bauteil erhitzt sich und kann platzen.
--- falsch
Seine Anschlüsse sind farbig markiert, damit man ihn schneller einbaut. Falsch angeschlossen arbeitet er genauso, nur seine Spannung hat das andere Vorzeichen.
--- falsch
Er trägt schon ab Werk eine feste Ladung. Falsch angeschlossen entlädt er sich zuerst und lädt sich danach in der neuen Richtung ganz normal auf.
--- falsch
Das Oxid hält die Spannung nur in einer Richtung. Falsch angeschlossen sperrt es vollständig, kein Strom fließt, und das Bauteil bleibt einfach ungeladen.
:::
:::karte begriff Supercap
Wie erreicht ein Supercap Kapazitäten bis 100 F und mehr, und welchen Preis zahlt er dafür?
---
An einer porösen Kohleelektrode mit riesiger innerer Oberfläche lagern sich Ionen des Elektrolyten im Abstand von rund 1 nm an. Der Preis: nur einige Volt und ein vergleichsweise hoher Leckstrom.
--- falsch
Er besteht aus Tausenden gewickelter Kunststofffolien, die alle hintereinander liegen und sich addieren. Der Preis: Er ist sehr groß und schwer, hält dafür aber jede noch so hohe Spannung aus.
--- falsch
Eine Keramik mit einer Dielektrizitätszahl über einer Million trennt zwei glatte Metallplatten. Der Preis: Seine Kapazität hängt sehr stark von der Temperatur ab.
--- falsch
An einer porösen Kohleelektrode lagern sich Ionen im Abstand von rund 1 mm an. Der Preis: Er ist gepolt, hält dafür aber Spannungen bis zu einigen Kilovolt aus.
:::
:::karte begriff Selbstheilend
Was bedeutet es, dass ein Kondensator mit metallisierter Folie selbstheilend ist?
---
Bei einem Durchschlag verdampft die dünne Metallschicht rund um die Fehlstelle, der Kurzschluss verschwindet, und nur eine winzige Fläche geht verloren. Beim Elko bildet sich das Oxid an der Fehlstelle neu.
--- falsch
Nach einem Durchschlag wächst die Metallschicht an der Fehlstelle langsam von selbst nach, bis die volle Fläche wiederhergestellt ist; die Kapazität bleibt deshalb über die ganze Lebensdauer genau gleich.
--- falsch
Er entlädt sich nach dem Abtrennen nie, weil das Dielektrikum jeden Leckstrom an einer Fehlstelle sofort wieder verschließt; die Ladung bleibt so für immer auf den Platten erhalten.
--- falsch
Ein Durchschlag kann gar nicht auftreten, weil die Folie bei zu hoher Spannung von selbst abschaltet und den Kondensator vom Kreis trennt, bis die Spannung wieder sinkt.
:::
:::karte begriff Leckstrom und Isolationswiderstand
Was ist der Leckstrom eines Kondensators, und wie stellt man ihn im Ersatzbild dar?
---
Ein winziger Strom von Platte zu Platte, weil das Dielektrikum wenige bewegliche Ladungen enthält. Im Ersatzbild liegt parallel zum idealen Kondensator ein Isolationswiderstand $R_\mathrm{I}$; ideal ist $R_\mathrm{I}\to\infty$.
--- falsch
Der Strom, der beim Laden durch die Zuleitungen fließt, bis die Spannung stimmt. Im Ersatzbild liegt in Reihe zum idealen Kondensator ein Isolationswiderstand $R_\mathrm{I}$; ideal ist er null, wie bei einem idealen Draht.
--- falsch
Ein winziger Strom von Platte zu Platte durch das Dielektrikum. Im Ersatzbild liegt parallel zum idealen Kondensator ein Isolationswiderstand $R_\mathrm{I}$; ideal ist dieser Widerstand null.
--- falsch
Ein Strom, der über das Gehäuse in die Umgebung abfließt, weil die Anschlüsse nicht isoliert sind. Im Ersatzbild erscheint er gar nicht, man zählt ihn als Fehler der Messung.
:::
:::karte formel Selbstentladung
Wovon hängt der Takt $R_\mathrm{I}\,C$ ab, in dem ein abgetrennter Kondensator seine Ladung verliert?
---
$R_\mathrm{I}\,C=\rho\,\varepsilon$: nur vom spezifischen Widerstand $\rho$ und der Permittivität $\varepsilon$ des Dielektrikums. $A$ und $d$ kürzen sich, die Baugröße spielt keine Rolle.
--- falsch
$R_\mathrm{I}\,C=\rho\,\varepsilon\,A/d$: vom Stoff und von der Baugröße. Ein großer Kondensator hält seine Ladung deshalb länger als ein kleiner aus demselben Stoff.
--- falsch
$R_\mathrm{I}\,C=\rho/\varepsilon$: Je größer die Permittivität des Dielektrikums, desto schneller entlädt sich der Kondensator; die Baugröße kürzt sich dabei heraus.
--- falsch
$R_\mathrm{I}\,C=\rho\,\varepsilon$, aber nur bei Elkos. Bei Folienkondensatoren hängt die Selbstentladung allein von der Fläche $A$ der beiden Platten ab.
:::
:::karte herleitung Selbstentladung
Leite aus dem Isolationswiderstand $R_\mathrm{I}=\rho\,d/A$ und der Formel des Plattenkondensators her, dass $R_\mathrm{I}\,C=\rho\,\varepsilon$ gilt.
---
Der Leckstrom durchquert das Dielektrikum wie einen Leiter der Länge $d$ mit dem Querschnitt $A$; deshalb ist $R_\mathrm{I}=\rho\,d/A$, weil der Widerstand eines Leiters aus spezifischem Widerstand, Länge und Querschnitt folgt.
---
Dieselben Platten bilden einen Plattenkondensator mit $C=\varepsilon\,\frac{A}{d}$, weil das Dielektrikum den Raum zwischen ihnen füllt.
---
Im Produkt kürzen sich $A$ und $d$, und es bleibt $R_\mathrm{I}\,C=\rho\,\varepsilon$, weil $d/A$ und $A/d$ Kehrwerte voneinander sind.
:::
:::karte zusammenhang Wahl der Bauform
Warum nimmt man nicht immer die Bauform mit der größten Kapazität?
---
Weil jede Bauform ihren Preis hat: Elkos sind gepolt und haben große Toleranzen, Supercaps halten nur wenige Volt. Bei wechselndem Vorzeichen der Spannung oder genauem Wert nimmt man Folie oder Keramik.
--- falsch
Weil große Kapazitäten den Strom in einer Schaltung vollständig sperren, auch wenn sich die Spannung ändert; Kondensatoren mit kleiner Kapazität lassen ihn dagegen fast ungehindert durch, wie ein Draht.
--- falsch
Weil Bauformen mit großer Kapazität immer auch die größte Baugröße haben; auf einer Platine ist dafür meist kein Platz, deshalb weicht man auf kleinere Werte mit kleineren Gehäusen aus.
--- falsch
Weil die größte Kapazität am schnellsten durchschlägt: Je größer $C$ ist, desto kleiner ist die Höchstspannung jedes Kondensators, gleich aus welchem Stoff er besteht.
:::
::::
