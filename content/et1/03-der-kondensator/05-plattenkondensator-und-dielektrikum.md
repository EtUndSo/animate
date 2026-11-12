---
title: Stufe 4: Plattenkondensator und Dielektrikum
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Kondensator
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Kapitel 3: Der Kondensator
order: 1130500
summary: Woher kommt der Wert von C ?
tags: Polarisation, gebundene Ladung, Permittivität, Dielektrizitätszahl, Durchschlag, Verschiebungsstrom
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Woher kommt der Wert von $C$? Bei zwei ebenen Platten folgt er aus Fläche, Abstand und dem Stoff dazwischen. Diese Stufe leitet die Formel her und erklärt, was der Isolator bewirkt.
:::

**Die Idee.** Bei fester Spannung $U$ und festem Abstand $d$ liegt das Feld $E=U/d$ fest ([Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Das Feld sagt, wie dicht die Feldlinien stehen, und jede Linie beginnt auf einer Ladung. Fest liegt also die Ladung je Fläche. Doppelte Fläche heißt deshalb doppelte Ladung. Halber Abstand heißt doppeltes Feld und damit doppelte Ladung je Fläche.

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

⁠**So liest man das:** $C$ steigt mit größerer Fläche $A$ (in m$^2$, das kursive $A$ ist nicht die Platte A aus Stufe [1](warum-strom-in-einen-isolator-fliet.html#stufe-1)), kleinerem Abstand $d$ (in m) und größerem $\varepsilon$. $\varepsilon_0$ ist die elektrische Feldkonstante aus [Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html). $\varepsilon$ heißt __Permittivität__, die reine Zahl $\varepsilon_\mathrm{r}$ heißt __Dielektrizitätszahl__ und gibt an, um welchen Faktor der Stoff die Kapazität gegenüber Vakuum erhöht. Luft zählt mit dem Wert 1, der Fehler beträgt 0,06 %. **Gültigkeit:** $d$ muss klein gegen die Plattenbreite sein. Sonst zählt das Streufeld am Rand ([Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)), im Plattenpaar mit 3 mm Abstand und 10 cm Breite erhöht es $C$ um rund 10 %. Für Überschläge reicht [(4.1)](#gl-4-1).

| Stoff | Luft | Papier | Glimmer | Porzellan | Wasser | Kondensatorkeramik |
|---|---|---|---|---|---|---|
| $\varepsilon_\mathrm{r}$ | 1 | $\approx2$ | $\approx5$ | $\approx6$ | $\approx81$ | 60 bis 3000 |

:::herleitung Vom Feldlinienbild zur Formel
Eine Punktladung erzeugt das Feld $E=\frac{Q}{4\pi\varepsilon_0r^2}=\frac{Q}{\varepsilon_0\cdot4\pi r^2}$. Im Nenner steht die Kugelfläche, durch die alle ihre Feldlinien laufen. Also gilt nach [Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html): Die Feldstärke ist die Ladung, geteilt durch $\varepsilon_0$ und durch die Fläche, die ihre Linien gleichmäßig durchlaufen. Im Plattenpaar laufen alle Linien der Ladung $Q$ parallel durch die Fläche $A$:

$$E=\frac{Q}{\varepsilon_0\,A},\qquad U=E\,d=\frac{Q\,d}{\varepsilon_0\,A}\quad\Longrightarrow\quad C=\frac QU=\varepsilon_0\,\frac Ad.$$

Mit Dielektrikum enden Linien auf der gebundenen Ladung $Q_\mathrm{g}$, durch den Raum läuft nur noch der Anteil $Q-Q_\mathrm{g}$. In den meisten Isolatoren ist dieser Anteil ein fester Bruchteil von $Q$. Man schreibt $Q-Q_\mathrm{g}=Q/\varepsilon_\mathrm{r}$, das ergibt $E=Q/(\varepsilon_\mathrm{r}\varepsilon_0A)$ und damit [(4.1)](#gl-4-1).
:::

::::beispiel
Das Plattenpaar hat $C=8{,}854\cdot10^{-12}\,\mathrm{F/m}\cdot0{,}01\,\mathrm{m^2}/0{,}003\,\mathrm{m}=29{,}5$ pF. Mit Keramik der Zahl $\varepsilon_\mathrm{r}=1000$ wären es 29,5 nF. Für 100 µF bräuchte man bei 3 mm Luft die Fläche $A=C\,d/\varepsilon_0=33\,900\,\mathrm{m^2}$, das sind 3,4 Hektar. Deshalb arbeiten reale Kondensatoren mit dünnen Schichten (Stufe [5](bauformen-und-selbstentladung.html#stufe-5)).
::::

⁠**Kontrolle:** Die Einheit stimmt: $\frac{\mathrm{A\,s}}{\mathrm{V\,m}}\cdot\frac{\mathrm{m^2}}{\mathrm{m}}=\frac{\mathrm{A\,s}}{\mathrm V}=\mathrm F$. **Grenzfall:** Für $d\to0$ wüchse $C$ unbegrenzt. Das verhindert der __Durchschlag__: Bei $E_\mathrm{max}$ wird das Dielektrikum leitend, in Luft bei 3 MV/m ([Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Dünne Schichten brauchen deshalb einen festen Stoff, und jeder Kondensator hat eine Höchstspannung $U_\mathrm{max}=E_\mathrm{max}\,d$.

:::zusatz Der Verschiebungsstrom
Mit $u=E\,d$ und [(4.1)](#gl-4-1) wird [(3.1)](strom-und-spannung-am-kondensator.html#gl-3-1) zu $i=\varepsilon A\,\mathrm{d} E/\mathrm{d} t$. In der Lücke fließt keine Ladung, aber dort ändert sich das Feld, und diese Änderung hat genau die Größe des Stroms in den Drähten. Maxwell nannte sie __Verschiebungsstrom__. Sie erzeugt in der Lücke dasselbe Magnetfeld wie der Strom im Draht (Durchflutungsgesetz, [Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Für das Magnetfeld ist der Kreis also geschlossen.
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

::::formelsammlung
**Plattenkondensator**

$$C=\varepsilon\,\frac{A}{d},\qquad\varepsilon=\varepsilon_0\,\varepsilon_\mathrm{r},\qquad\varepsilon_0=8{,}854\cdot10^{-12}\,\frac{\mathrm{A\,s}}{\mathrm{V\,m}}$$

$A$ Fläche einer Platte, $d$ Abstand, das Dielektrikum füllt den Raum. $\varepsilon$ Permittivität, $\varepsilon_\mathrm{r}$ Dielektrizitätszahl: Luft 1, Papier $\approx2$, Glimmer $\approx5$, Porzellan $\approx6$, Wasser $\approx81$, Kondensatorkeramik 60 bis 3000. Gilt für $d$ klein gegen die Plattenbreite, sonst erhöht das Streufeld am Rand $C$.

**Feld und Spannung im Plattenpaar in Luft**

$$E=\frac{Q}{\varepsilon_0\,A},\qquad U=E\,d=\frac{Q\,d}{\varepsilon_0\,A}$$

Alle Feldlinien der Ladung $Q$ laufen parallel durch die Fläche $A$; daraus folgt $C=\frac QU=\varepsilon_0\,\frac Ad$.

**Gebundene Ladung**

$$Q-Q_\mathrm{g}=Q/\varepsilon_\mathrm{r},\qquad E=Q/(\varepsilon_\mathrm{r}\varepsilon_0A)$$

Durch die Polarisation bleibt an den Oberflächen des Dielektrikums die gebundene Ladung $Q_\mathrm{g}$, gegenüber der Plusplatte negativ; auf ihr enden Feldlinien. Hält die Quelle die Spannung fest, schiebt sie Ladung nach, bis das Feld wieder stimmt.

**Höchstspannung**

$$U_\mathrm{max}=E_\mathrm{max}\,d$$

Bei der Feldstärke $E_\mathrm{max}$ wird das Dielektrikum leitend (Durchschlag), in Luft bei 3 MV/m. Kleiner Abstand ergibt große Kapazität, aber kleine Höchstspannung; dünne Schichten brauchen deshalb einen festen Stoff.

**Verschiebungsstrom**

$$i=\varepsilon A\,\mathrm{d} E/\mathrm{d} t$$

Aus $i=C\,\mathrm{d} u/\mathrm{d} t$ mit $u=E\,d$: Die Änderung des Felds in der Lücke hat genau die Größe des Stroms in den Drähten und erzeugt dasselbe Magnetfeld, obwohl dort keine Ladung fließt.
::::

::::lernkarten
:::karte formel Plattenkondensator
Wie hängt die Kapazität eines Plattenkondensators von Fläche, Abstand und Stoff ab, und wann gilt die Formel?
---
$C=\varepsilon\,\frac{A}{d}$ mit $\varepsilon=\varepsilon_0\,\varepsilon_\mathrm{r}$; $A$ Fläche einer Platte, $d$ Abstand, das Dielektrikum füllt den Raum. Gilt, wenn $d$ klein gegen die Plattenbreite ist, sonst zählt das Streufeld am Rand.
--- falsch
$C=\varepsilon\,\frac{d}{A}$ mit $\varepsilon=\varepsilon_0\,\varepsilon_\mathrm{r}$: Ein größerer Abstand ergibt mehr Kapazität, weil mehr Feld zwischen die Platten passt. Gilt für jeden Abstand der Platten, auch wenn er größer ist als ihre Breite.
--- falsch
$C=\varepsilon\,A\,d$ mit $\varepsilon=\varepsilon_0\,\varepsilon_\mathrm{r}$: Die Kapazität wächst mit dem Volumen zwischen den Platten. Gilt, wenn das Dielektrikum diesen Raum ganz ausfüllt.
--- falsch
$C=\varepsilon\,\frac{A}{d}$ mit $\varepsilon=\varepsilon_0\,\varepsilon_\mathrm{r}$; $A$ Fläche, $d$ Abstand. Gilt auch für weit auseinanderliegende Platten, denn das Streufeld am Rand zählt nie.
:::
:::karte begriff Permittivität und Dielektrizitätszahl
Was geben die Permittivität $\varepsilon$ und die Dielektrizitätszahl $\varepsilon_\mathrm{r}$ des Stoffs zwischen den Platten an?
---
$\varepsilon=\varepsilon_0\,\varepsilon_\mathrm{r}$ heißt Permittivität, $\varepsilon_0$ ist die elektrische Feldkonstante. Die reine Zahl $\varepsilon_\mathrm{r}$ gibt an, um welchen Faktor der Stoff die Kapazität gegenüber Vakuum erhöht; Luft zählt mit 1.
--- falsch
$\varepsilon=\varepsilon_0/\varepsilon_\mathrm{r}$ heißt Permittivität. Die reine Zahl $\varepsilon_\mathrm{r}$ gibt an, um welchen Faktor der Stoff die Kapazität gegenüber Vakuum verkleinert; Luft zählt mit 1, jeder feste Stoff mit weniger.
--- falsch
$\varepsilon=\varepsilon_0\,\varepsilon_\mathrm{r}$ heißt Permittivität. Die Zahl $\varepsilon_\mathrm{r}$ gibt an, wie gut der Stoff Strom leitet; je größer sie ist, desto schneller entlädt sich der Kondensator von selbst.
--- falsch
$\varepsilon=\varepsilon_0\,\varepsilon_\mathrm{r}$ heißt Permittivität. Die Zahl $\varepsilon_\mathrm{r}$ gibt die Feldstärke in MV/m an, bei der der Stoff durchschlägt; Luft zählt deshalb mit 3.
:::
:::karte begriff Polarisation und gebundene Ladung
Was versteht man unter der Polarisation eines Dielektrikums und unter der gebundenen Ladung, die dabei an seinen Oberflächen entsteht?
---
Das Feld verschiebt in jedem Atom oder Molekül die positive gegen die negative Ladung ein kleines Stück; die Elektronen bleiben bei ihren Atomen. Innen heben sich benachbarte Enden auf, an den Oberflächen bleibt gebundene Ladung, gegenüber der Plusplatte negativ.
--- falsch
Das Feld reißt Elektronen aus den Atomen und treibt sie durch den Stoff zur Oberfläche an der Plusplatte. Dort sammeln sie sich als gebundene Ladung, die frei durch den Stoff wandern kann, sobald man die Spannung abschaltet.
--- falsch
Das Feld verschiebt in jedem Molekül die positive gegen die negative Ladung ein kleines Stück. Innen heben sich die Enden auf, an den Oberflächen bleibt gebundene Ladung, gegenüber der Plusplatte positiv; sie verstärkt das Feld zwischen den Platten zusätzlich.
--- falsch
Die Ladung der Platten dringt beim Laden ein Stück in den Isolator ein und bleibt dort gebunden. Sie verteilt sich gleichmäßig im ganzen Inneren des Stoffs, an seinen Oberflächen bleibt dagegen keine Ladung zurück.
:::
:::karte zusammenhang Wie das Dielektrikum die Kapazität erhöht
Warum sitzt bei gleicher Spannung mehr Ladung auf den Platten, wenn ein Dielektrikum den Raum zwischen ihnen füllt?
---
Auf der gebundenen Ladung endet ein Teil der Feldlinien, das Feld zwischen den Platten würde schwächer. Die Batterie hält aber $U$ und damit $E$ fest und schiebt Ladung nach, bis das Feld wieder stimmt.
--- falsch
Weil das Dielektrikum selbst Ladung leitet und sie zusätzlich auf die Platten bringt; ein Isolator ganz ohne bewegliche Ladung würde die Kapazität deshalb überhaupt nicht erhöhen.
--- falsch
Weil das Dielektrikum das Feld zwischen den Platten verstärkt, indem sich seine Moleküle ausrichten; das stärkere Feld zieht bei gleicher Spannung mehr Ladung aus der Batterie auf die Platten.
--- falsch
Weil das Dielektrikum die Platten ein Stück zueinander zieht und so ihren Abstand verkleinert; bei kleinerem $d$ steigt die Kapazität bei gleicher Spannung.
:::
:::karte herleitung Vom Feldlinienbild zur Formel
Leite aus dem Feld einer Punktladung her, dass ein Plattenkondensator in Luft die Kapazität $C=\varepsilon_0\,\frac Ad$ und mit Dielektrikum $C=\varepsilon\,\frac{A}{d}$ hat.
---
Eine Punktladung erzeugt $E=\frac{Q}{\varepsilon_0\cdot4\pi r^2}$, weil im Nenner die Kugelfläche steht, durch die alle ihre Feldlinien laufen: Die Feldstärke ist die Ladung, geteilt durch $\varepsilon_0$ und durch diese Fläche.
---
Im Plattenpaar ist $E=\frac{Q}{\varepsilon_0\,A}$, weil alle Linien der Ladung $Q$ parallel und gleichmäßig durch die Plattenfläche $A$ laufen.
---
Damit ist $U=E\,d=\frac{Q\,d}{\varepsilon_0\,A}$ und $C=\frac QU=\varepsilon_0\,\frac Ad$, weil das Feld zwischen den Platten überall gleich ist und die Kapazität das Verhältnis von Ladung und Spannung ist.
---
Mit Dielektrikum läuft durch den Raum nur noch $Q-Q_\mathrm{g}=Q/\varepsilon_\mathrm{r}$, weil ein Teil der Linien auf der gebundenen Ladung $Q_\mathrm{g}$ endet und dieser Anteil in den meisten Isolatoren ein fester Bruchteil von $Q$ ist.
---
Das ergibt $E=Q/(\varepsilon_\mathrm{r}\varepsilon_0A)$ und damit $C=\varepsilon\,\frac{A}{d}$, weil sich gegenüber Luft nur $\varepsilon_0$ durch $\varepsilon=\varepsilon_0\,\varepsilon_\mathrm{r}$ ersetzt.
:::
:::karte zusammenhang Fläche und Abstand
Warum verdoppelt sich die Kapazität, wenn man die Plattenfläche verdoppelt oder den Abstand halbiert?
---
Bei fester Spannung und festem Abstand liegt $E=U/d$ fest und damit die Ladung je Fläche: Doppelte Fläche trägt doppelte Ladung. Halber Abstand heißt doppeltes Feld und damit doppelte Ladung je Fläche.
--- falsch
Halber Abstand halbiert bei gleicher Spannung das Feld, weil die Feldlinien kürzer werden; in das schwächere Feld passt doppelt so viel Ladung. Doppelte Fläche wirkt genauso, weil sich das Feld dort verdünnt.
--- falsch
Doppelte Fläche bietet doppelt so vielen Elektronen Platz und trägt deshalb die doppelte Ladung. Der Abstand wirkt dagegen nur über das Dielektrikum und ändert die Kapazität in Luft gar nicht.
--- falsch
Weil Fläche und Abstand die Spannung der Batterie verändern: Doppelte Fläche oder halber Abstand halbieren sie, und bei halber Spannung sitzt auf den Platten die doppelte Ladung je Volt.
:::
:::karte begriff Durchschlag
Was ist ein Durchschlag, und warum begrenzt er die Kapazität, die man durch kleinen Plattenabstand erreichen kann?
---
Bei der Feldstärke $E_\mathrm{max}$ wird das Dielektrikum leitend, in Luft bei 3 MV/m. Jeder Kondensator hat deshalb eine Höchstspannung $U_\mathrm{max}=E_\mathrm{max}\,d$, und dünne Schichten brauchen einen festen Stoff.
--- falsch
Bei der Feldstärke $E_\mathrm{max}$ wird das Dielektrikum leitend. Die Höchstspannung ist $U_\mathrm{max}=E_\mathrm{max}/d$; sie wächst also, wenn man den Abstand der Platten verkleinert.
--- falsch
Bei einer bestimmten Spannung schmelzen die Platten, unabhängig von ihrem Abstand. Ein kleiner Abstand ist deshalb unbedenklich, solange diese Spannung nicht erreicht wird.
--- falsch
Bei großer Ladung reißt das Feld Elektronen aus den Platten in den leeren Raum. Das geschieht nur in Vakuum und Luft; ein fester Stoff zwischen den Platten verhindert es ganz, gleich wie dünn er ist.
:::
:::karte begriff Verschiebungsstrom
Was versteht man unter dem Verschiebungsstrom in der Lücke eines Kondensators?
---
Die Änderung des Felds in der Lücke, $i=\varepsilon A\,\mathrm{d} E/\mathrm{d} t$. Dort fließt keine Ladung, aber diese Änderung hat genau die Größe des Stroms in den Drähten und erzeugt dasselbe Magnetfeld wie er.
--- falsch
Den Strom der Elektronen, die durch die Lücke von Platte zu Platte springen, $i=\varepsilon A\,\mathrm{d} E/\mathrm{d} t$; er ist genau so groß wie der Strom in den Drähten und schließt den Kreis.
--- falsch
Die Änderung des Felds in der Lücke. Sie ist viel kleiner als der Strom in den Drähten und erzeugt deshalb kein messbares Magnetfeld; der Kreis bleibt auch für das Magnetfeld unterbrochen.
--- falsch
Den Strom, der beim Verschieben der Platten gegeneinander in den Drähten fließt. Er tritt nur auf, wenn sich der Abstand der Platten ändert, sonst ist er null.
:::
:::karte zusammenhang Wasser als Dielektrikum
Warum baut niemand Kondensatoren mit Wasser als Dielektrikum, obwohl Wasser $\varepsilon_\mathrm{r}=81$ hat?
---
Weil Wasser in der Praxis leitet: Gelöste Ionen tragen Strom zwischen den Platten, der Kondensator entlädt sich sofort selbst. Ein Dielektrikum muss sich polarisieren und isolieren.
--- falsch
Weil ein großes $\varepsilon_\mathrm{r}$ das Feld zwischen den Platten schwächt und damit die Ladung auf den Platten verkleinert; Wasser würde die Kapazität deshalb sogar unter den Wert in Luft senken.
--- falsch
Weil Wasser beim Laden verdampft: Die Feldenergie heizt es so stark auf, dass sich zwischen den Platten schon nach kurzer Zeit Dampf bildet.
--- falsch
Weil sich Wassermoleküle im Feld nicht ausrichten können, da sie keine getrennten Ladungsschwerpunkte haben; der hohe Wert von $\varepsilon_\mathrm{r}$ gilt nur für Eis.
:::
::::
