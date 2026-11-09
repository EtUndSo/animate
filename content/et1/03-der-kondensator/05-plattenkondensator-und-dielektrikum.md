---
title: Stufe 4: Plattenkondensator und Dielektrikum
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Kondensator
order: 1130500
summary: Woher kommt der Wert von C ?
tags: Polarisation, gebundene Ladung, Permittivität, Dielektrizitätszahl, Durchschlag, Verschiebungsstrom
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Woher kommt der Wert von $C$? Bei zwei ebenen Platten folgt er aus Fläche, Abstand und dem Stoff dazwischen. Diese Stufe leitet die Formel her und erklärt, was der Isolator bewirkt.
:::

**Die Idee.** Bei fester Spannung $U$ und festem Abstand $d$ liegt das Feld $E=U/d$ fest ([Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Das Feld sagt, wie dicht die Feldlinien stehen, und jede Linie beginnt auf einer Ladung. Fest liegt also die Ladung je Fläche. Doppelte Fläche heißt deshalb doppelte Ladung. Halber Abstand heißt doppeltes Feld und damit doppelte Ladung je Fläche.

Der Isolator erhöht die Kapazität zusätzlich. Seine Elektronen bleiben zwar bei ihren Atomen, aber das Feld verschiebt in jedem Atom oder Molekül die positive gegen die negative Ladung ein kleines Stück. Diese Verschiebung heißt __Polarisation__. Im Inneren heben sich benachbarte Enden auf, an den Oberflächen bleibt eine __gebundene Ladung__ stehen, gegenüber der Plusplatte negativ (Abb. [4](#abb-4) rechts). Auf ihr endet ein Teil der Feldlinien, das Feld zwischen den Platten würde schwächer. Die Batterie hält aber $U$ und damit $E$ fest, also schiebt sie Ladung nach, bis das Feld wieder stimmt. Bei gleicher Spannung sitzt mehr Ladung auf den Platten.

:::abbildung et1/k3platte 4
Gleiche Spannung, gleicher Abstand, gleiches Feld. Links Luft: Jede Feldlinie läuft von Platte zu Platte, $A$ ist die Fläche einer Platte. Rechts ein Dielektrikum mit $\varepsilon_\mathrm{r}=2$: Die Moleküle sind ausgerichtet, innen heben sich die Enden auf, am Rand bleibt gebundene Ladung. Die Hälfte der Linien endet dort. Deshalb trägt die Platte die doppelte Ladung.
:::

:::satz Satz 4.1 (Plattenkondensator)
<span class="anker" id="satz-4-1"></span>

Für zwei ebene Platten der Fläche $A$ im Abstand $d$ mit einem Dielektrikum, das den Raum füllt, gilt

<span class="anker" id="gl-4-1"></span>
$$C=\varepsilon\,\frac{A}{d},\qquad\varepsilon=\varepsilon_0\,\varepsilon_\mathrm{r},\qquad\varepsilon_0=8{,}854\cdot10^{-12}\,\frac{\mathrm{A\,s}}{\mathrm{V\,m}}. \tag{4.1}$$
:::

⁠**So liest man das:** $C$ steigt mit größerer Fläche $A$ (in m$^2$, das kursive $A$ ist nicht die Platte A aus Stufe [1](warum-strom-in-einen-isolator-fliet.html#stufe-1)), kleinerem Abstand $d$ (in m) und größerem $\varepsilon$. $\varepsilon_0$ ist die elektrische Feldkonstante aus [Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html). $\varepsilon$ heißt __Permittivität__, die reine Zahl $\varepsilon_\mathrm{r}$ heißt __Dielektrizitätszahl__ und gibt an, um welchen Faktor der Stoff die Kapazität gegenüber Vakuum erhöht. Luft zählt mit dem Wert 1, der Fehler beträgt 0,06 %. **Gültigkeit:** $d$ muss klein gegen die Plattenbreite sein. Sonst zählt das Streufeld am Rand ([Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)), im Plattenpaar mit 3 mm Abstand und 10 cm Breite erhöht es $C$ um rund 10 %. Für Überschläge reicht [(4.1)](#gl-4-1).

| Stoff | Luft | Papier | Glimmer | Porzellan | Wasser | Kondensatorkeramik |
|---|---|---|---|---|---|---|
| $\varepsilon_\mathrm{r}$ | 1 | $\approx2$ | $\approx5$ | $\approx6$ | $\approx81$ | 60 bis 3000 |

:::herleitung Vom Feldlinienbild zur Formel
Eine Punktladung erzeugt das Feld $E=\frac{Q}{4\pi\varepsilon_0r^2}=\frac{Q}{\varepsilon_0\cdot4\pi r^2}$. Im Nenner steht die Kugelfläche, durch die alle ihre Feldlinien laufen. Also gilt nach [Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html): Die Feldstärke ist die Ladung, geteilt durch $\varepsilon_0$ und durch die Fläche, die ihre Linien gleichmäßig durchlaufen. Im Plattenpaar laufen alle Linien der Ladung $Q$ parallel durch die Fläche $A$:

$$E=\frac{Q}{\varepsilon_0\,A},\qquad U=E\,d=\frac{Q\,d}{\varepsilon_0\,A}\quad\Longrightarrow\quad C=\frac QU=\varepsilon_0\,\frac Ad.$$

Mit Dielektrikum enden Linien auf der gebundenen Ladung $Q_\mathrm{g}$, durch den Raum läuft nur noch der Anteil $Q-Q_\mathrm{g}$. In den meisten Isolatoren ist dieser Anteil ein fester Bruchteil von $Q$. Man schreibt $Q-Q_\mathrm{g}=Q/\varepsilon_\mathrm{r}$, das ergibt $E=Q/(\varepsilon_\mathrm{r}\varepsilon_0A)$ und damit [(4.1)](#gl-4-1).
:::

::::beispiel
Das Plattenpaar hat $C=8{,}854\cdot10^{-12}\,\mathrm{F/m}\cdot0{,}01\,\mathrm{m^2}/0{,}003\,\mathrm{m}=29{,}5$ pF. Mit Keramik der Zahl $\varepsilon_\mathrm{r}=1000$ wären es 29,5 nF. Für 100 µF bräuchte man bei 3 mm Luft die Fläche $A=C\,d/\varepsilon_0=33\,900\,\mathrm{m^2}$, das sind 3,4 Hektar. Deshalb arbeiten reale Kondensatoren mit dünnen Schichten (Stufe [5](bauformen-und-selbstentladung.html#stufe-5)).
::::

⁠**Kontrolle:** Die Einheit stimmt: $\frac{\mathrm{A\,s}}{\mathrm{V\,m}}\cdot\frac{\mathrm{m^2}}{\mathrm{m}}=\frac{\mathrm{A\,s}}{\mathrm V}=\mathrm F$. **Grenzfall:** Für $d\to0$ wüchse $C$ unbegrenzt. Das verhindert der __Durchschlag__: Bei $E_\mathrm{max}$ wird das Dielektrikum leitend, in Luft bei 3 MV/m ([Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Dünne Schichten brauchen deshalb einen festen Stoff, und jeder Kondensator hat eine Höchstspannung $U_\mathrm{max}=E_\mathrm{max}\,d$.

:::zusatz Der Verschiebungsstrom
Mit $u=E\,d$ und [(4.1)](#gl-4-1) wird [(3.1)](strom-und-spannung-am-kondensator.html#gl-3-1) zu $i=\varepsilon A\,\mathrm{d} E/\mathrm{d} t$. In der Lücke fließt keine Ladung, aber dort ändert sich das Feld, und diese Änderung hat genau die Größe des Stroms in den Drähten. Maxwell nannte sie __Verschiebungsstrom__. Sie erzeugt in der Lücke dasselbe Magnetfeld wie der Strom im Draht (Durchflutungsgesetz, [Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Für das Magnetfeld ist der Kreis also geschlossen.
:::

:::frage Wasser hat $\varepsilon_\mathrm{r}=81$. Warum baut niemand Wasserkondensatoren?
Weil Wasser in der Praxis leitet: Gelöste Ionen tragen Strom zwischen den Platten, der Kondensator entlädt sich sofort selbst. Ein Dielektrikum muss zwei Dinge können, sich polarisieren und isolieren. Das hohe $\varepsilon_\mathrm{r}$ kommt von den Wassermolekülen, die von sich aus getrennte Ladungsschwerpunkte haben und sich im Feld ausrichten.
:::

:::aufgabe Aufgabe 4 ★★ Fläche und Höchstspannung
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Wie groß muss $A$ für 100 µF sein, wenn statt 3 mm Luft eine 10 µm dicke Folie mit $\varepsilon_\mathrm{r}=3$ die Platten trennt?

</li>

<li>

Wie lang wäre ein 5 cm breiter Streifen dieser Fläche?

</li>

<li>

Bis zu welcher Spannung hält das Plattenpaar in Luft?

</li>

</ol>

:::loesung
(a) $A=\dfrac{C\,d}{\varepsilon_0\varepsilon_\mathrm{r}}=\dfrac{10^{-4}\,\mathrm{F}\cdot10^{-5}\,\mathrm{m}}{3\cdot8{,}854\cdot10^{-12}\,\mathrm{F/m}}=37{,}6\,\mathrm{m^2}$.

(b) $37{,}6\,\mathrm{m^2}/0{,}05\,\mathrm{m}=753$ m. Reale Wickel sind kürzer, weil sie dünnere Folie und beide Seiten jeder Elektrode nutzen.

(c) $U_\mathrm{max}=E_\mathrm{max}\,d=3\,\mathrm{MV/m}\cdot3\,\mathrm{mm}=9$ kV.
:::
:::

:::aufgabe Aufgabe 5 ★★ Dielektrikum einschieben
<span class="anker" id="aufg-5"></span>

Das Plattenpaar liegt an 9 V. Nun wird der Raum mit einem Stoff der Zahl $\varepsilon_\mathrm{r}=4$ gefüllt. Sage zuerst vorher, was gleich bleibt, und rechne dann.

<ol class="al">

<li>

Die Batterie bleibt angeschlossen. Wie groß sind $C$, $U$, $Q$ und $E$?

</li>

<li>

Die Batterie wurde vorher abgetrennt. Wie groß sind nun $C$, $U$, $Q$ und $E$?

</li>

<li>

Warum unterscheiden sich die beiden Fälle, obwohl $C$ gleich ist?

</li>

</ol>

:::loesung
In beiden Fällen ist $C=4\cdot29{,}5\,\mathrm{pF}=118$ pF.

(a) Die Batterie hält $U=9$ V fest. Dann bleibt $E=U/d=3$ kV/m, und $Q=C\,U=1{,}06$ nC. Die Batterie schiebt die zusätzliche Ladung nach.

(b) Ohne Batterie kann keine Ladung nachfließen, $Q=266$ pC bleibt. Dann ist $U=Q/C=2{,}25$ V und $E=U/d=750$ V/m.

(c) Festgehalten wird jeweils etwas anderes: mit Batterie die Spannung, ohne Batterie die Ladung. Das Dielektrikum ändert $C$, die andere Größe stellt sich nach $Q=CU$ ein.
:::
:::
