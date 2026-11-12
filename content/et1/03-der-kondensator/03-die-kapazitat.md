---
title: Stufe 2: Die Kapazität
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Kondensator
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Kapitel 3: Der Kondensator
order: 1130300
summary: Wie viel Ladung hält eine bestimmte Spannung auf den Platten?
tags: 
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Wie viel Ladung hält eine bestimmte Spannung auf den Platten? Die Antwort ist eine einzige Zahl je Bauteil.
:::

**Die Idee.** Verdoppelt man die Ladung auf beiden Platten, trägt jede Ladung ihr Feld doppelt bei. Nach der Überlagerung aus [Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html) verdoppelt sich das Feld an jedem Ort, seine Form bleibt gleich (Abb. [2](#abb-2) links). Die Spannung ist das Integral des Felds von Platte zu Platte, also verdoppelt sie sich auch. $Q$ und $U$ sind deshalb proportional. Ihr Verhältnis hängt nicht davon ab, wie viel Ladung gerade da ist, sondern nur von Form, Abstand und Stoff.

:::definition Definition 2.1 (Kapazität)
<span class="anker" id="satz-2-1"></span>

Die Kapazität eines Kondensators ist das Verhältnis von Ladung und Spannung:

<span class="anker" id="gl-2-1"></span>
$$C=\frac{Q}{U},\qquad Q=C\,U,\qquad[C]=\frac{\mathrm{A\,s}}{\mathrm V}=\mathrm F\ \text{(Farad)}. \tag{2.1}$$
:::

⁠**So liest man das:** $Q$ ist die Ladung der positiven Platte in C (Coulomb), $U$ die Spannung zwischen den Platten in V, $C$ die Kapazität in F. Bei 1 F hält ein Volt ein Coulomb. Das ist sehr viel. Übliche Werte liegen bei fF, pF, nF und µF, Elektrolytkondensatoren reichen bis in den mF-Bereich. Die Formelzeichen nicht verwechseln: Kursiv ist $C$ die Kapazität, aufrecht ist C das Coulomb. **Gültigkeit:** [(2.1)](#gl-2-1) setzt voraus, dass der Stoff zwischen den Platten sich mit dem Feld nicht ändert. Keramik mit sehr großem $\varepsilon_\mathrm{r}$ (Stufe [4](plattenkondensator-und-dielektrikum.html#stufe-4)) verliert bei hoher Spannung merklich an Kapazität.

:::abbildung et1/k3qu 2
Links: Doppelte Ladung ergibt doppelt so dichte Feldlinien und damit die doppelte Spannung. Rechts: Die Ladung wächst proportional zur Spannung, die Steigung der Geraden ist die Kapazität. Die Punkte gehören zu 9 V.
:::

::::beispiel
Das Plattenpaar hat $C=29{,}5$ pF (Stufe [4](plattenkondensator-und-dielektrikum.html#stufe-4)). Bei 9 V trägt es $Q=29{,}5\,\mathrm{pF}\cdot9\,\mathrm{V}=266$ pC, das sind $1{,}66\cdot10^{9}$ Elektronen. Eine 1 mm dicke Kupferplatte dieser Fläche enthält $8{,}5\cdot10^{23}$ freie Elektronen. Es wandert also nur eines von $5\cdot10^{14}$, und diese sitzen auf der Innenseite der Platte. Das Metall bleibt praktisch unverändert. Der Kondensator des RC-Kreises trägt bei 9 V $Q=900\,\mu\text{C}$, 3,4 Millionen Mal mehr.
::::

⁠**Grenzfall:** Für $U=0$ ist $Q=0$: Ohne Spannung ist nichts getrennt. Bei gleicher Ladung zeigt der kleinere Kondensator die größere Spannung.

:::frage Kapazität klingt nach Fassungsvermögen. Ist ein Kondensator irgendwann voll?
Nicht im Sinn eines Eimers. Mehr Spannung bringt immer mehr Ladung, $C$ bleibt dabei gleich. Die Grenze setzt das Dielektrikum: Über einer bestimmten Feldstärke schlägt es durch. Voll heißt in diesem Kapitel nur: Die Spannung hat die der Quelle erreicht.
:::

:::aufgabe Aufgabe 2 ★ Ladung und Spannung
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Ein Kondensator mit 470 nF liegt an 12 V. Wie groß ist seine Ladung?

</li>

<li>

Bei welcher Spannung trägt er 1 µC?

</li>

<li>

Die Spannung wird halbiert. Was geschieht mit $Q$ und mit $C$?

</li>

<li>

Zwei Kondensatoren mit 10 µF und 1 µF tragen je 50 µC. Welche Spannungen liegen an ihnen?

</li>

</ol>

:::loesung
(a) $Q=470\,\mathrm{nF}\cdot12\,\mathrm{V}=5{,}64\,\mu\text{C}$.

(b) $U=Q/C=1\,\mu\text{C}/470\,\mathrm{nF}=2{,}13$ V.

(c) $Q$ halbiert sich auf 2,82 µC. $C$ bleibt gleich, denn es hängt nur vom Bauteil ab.

(d) $U=Q/C$: 5 V am 10-µF-Kondensator, 50 V am 1-µF-Kondensator. Dieselbe Ladung erzeugt am kleineren die größere Spannung.
:::
:::

::::formelsammlung
**Kapazität**

$$C=\frac{Q}{U},\qquad Q=C\,U$$

$Q$ Ladung der positiven Platte, $U$ Spannung zwischen den Platten. $C$ hängt nur von Form, Abstand und Stoff ab, nicht von $Q$ oder $U$; bei gleicher Ladung zeigt der kleinere Kondensator die größere Spannung. Gilt, wenn sich der Stoff zwischen den Platten mit dem Feld nicht ändert.

**Einheit Farad**

$$[C]=\frac{\mathrm{A\,s}}{\mathrm V}=\mathrm F$$

Bei 1 F hält ein Volt ein Coulomb, das ist sehr viel. Übliche Werte: fF, pF, nF und µF, Elektrolytkondensatoren bis in den mF-Bereich. Kursiv ist $C$ die Kapazität, aufrecht ist C das Coulomb.
::::

::::lernkarten
:::karte begriff Kapazität
Was gibt die Kapazität $C$ eines Kondensators an, und in welcher Einheit misst man sie?
---
Das Verhältnis von Ladung und Spannung, $C=\frac{Q}{U}$: wie viel Ladung je Volt auf den Platten sitzt. Einheit $[C]=\frac{\mathrm{A\,s}}{\mathrm V}=\mathrm F$ (Farad).
--- falsch
Das Produkt aus Ladung und Spannung, $C=Q\,U$: die Energie, die auf den Platten sitzt. Einheit $\mathrm{A\,s\,V}=\mathrm F$ (Farad).
--- falsch
Das Verhältnis von Spannung und Ladung, $C=U/Q$: wie viel Spannung je Coulomb an den Platten liegt. Einheit $\mathrm V/(\mathrm{A\,s})=\mathrm F$ (Farad).
--- falsch
Die größte Ladung, die der Kondensator aufnehmen kann, bevor er voll ist. Einheit Coulomb; mehr Spannung bringt danach keine weitere Ladung.
:::
:::karte begriff Farad
Wie groß ist eine Kapazität von 1 F, und welche Werte haben übliche Kondensatoren?
---
Bei 1 F hält ein Volt ein Coulomb, das ist sehr viel. Übliche Werte liegen bei fF, pF, nF und µF, Elektrolytkondensatoren reichen bis in den mF-Bereich.
--- falsch
Bei 1 F hält ein Volt ein einziges Elektron, das ist sehr wenig. Übliche Werte liegen deshalb bei kF und MF, Elektrolytkondensatoren reichen bis in den GF-Bereich.
--- falsch
Bei 1 F hält ein Volt ein Ampere, das ist ein mittlerer Wert. Übliche Kondensatoren liegen zwischen 0,1 F und 10 F, kleinere Werte kommen nur selten vor.
--- falsch
Bei 1 F hält ein Volt ein Mikrocoulomb, das ist wenig. Übliche Werte liegen bei einigen Farad, Elektrolytkondensatoren reichen bis zu einigen tausend Farad.
:::
:::karte formel Ladung und Spannung
Wie hängen Ladung und Spannung an einem Kondensator zusammen, und was setzt dieser Zusammenhang voraus?
---
$Q=C\,U$: Die Ladung ist proportional zur Spannung, $C$ ist der feste Faktor des Bauteils. Vorausgesetzt ist, dass sich der Stoff zwischen den Platten mit dem Feld nicht ändert.
--- falsch
$Q=C\,U$: Die Ladung ist proportional zur Spannung. Das gilt für jeden Stoff zwischen den Platten und bei jeder noch so hohen Spannung, auch wenn sich der Stoff im Feld merklich verändert.
--- falsch
$Q=U/C$: Die Ladung ist proportional zur Spannung; ein Kondensator mit größerem $C$ trägt bei gleicher Spannung deshalb weniger Ladung auf seinen Platten.
--- falsch
$Q=C\,U$, wobei $C$ mit der Ladung wächst: Je mehr Ladung schon auf den Platten sitzt, desto leichter kommt bei gleicher Spannung weitere Ladung hinzu.
:::
:::karte zusammenhang Warum Ladung und Spannung proportional sind
Warum ist die Ladung eines Kondensators proportional zu seiner Spannung?
---
Doppelte Ladung trägt ihr Feld doppelt bei: Nach der Überlagerung verdoppelt sich das Feld an jedem Ort, seine Form bleibt. Die Spannung ist das Integral des Felds von Platte zu Platte, also verdoppelt sie sich auch.
--- falsch
Weil die Batterie bei doppelter Spannung doppelt so lange Strom liefert und so doppelt so viel Ladung auf die Platten bringt; Form und Stärke des Felds zwischen den Platten spielen für die Spannung dabei gar keine Rolle.
--- falsch
Weil die Platten bei doppelter Ladung doppelt so weit auseinanderrücken, denn ihre Ladungen drücken stärker; bei gleichem Feld verdoppelt der größere Abstand die Spannung zwischen ihnen.
--- falsch
Weil doppelte Ladung das Feld nur in der Mitte zwischen den Platten verdoppelt und am Rand gleich lässt; im Mittel über die ganze Fläche ergibt das ungefähr die doppelte Spannung.
:::
:::karte zusammenhang Wovon die Kapazität abhängt
Wovon hängt die Kapazität eines Kondensators ab, und wovon hängt sie nicht ab?
---
Nur von Form, Abstand und Stoff zwischen den Platten. Sie hängt nicht davon ab, wie viel Ladung gerade auf den Platten sitzt oder welche Spannung anliegt.
--- falsch
Von der angelegten Spannung: Je höher die Spannung, desto größer die Kapazität, weil dann mehr Ladung auf den Platten sitzt. Form und Abstand legen nur die Höchstspannung fest.
--- falsch
Von der gespeicherten Ladung: Ein leerer Kondensator hat die Kapazität null, ein voll geladener hat seine größte Kapazität; dazwischen wächst sie mit jeder Ladung.
--- falsch
Nur vom Metall der Platten: Ein Metall mit mehr freien Elektronen ergibt eine größere Kapazität, Form, Abstand und Stoff dazwischen spielen dagegen keine Rolle.
:::
:::karte zusammenhang Gleiche Ladung, verschiedene Kapazität
Zwei Kondensatoren tragen dieselbe Ladung. Welcher zeigt die größere Spannung, und warum?
---
Der mit der kleineren Kapazität: Nach $U=Q/C$ ergibt dieselbe Ladung bei kleinerem $C$ die größere Spannung.
--- falsch
Der mit der größeren Kapazität: Nach $U=C\,Q$ ergibt dieselbe Ladung bei größerem $C$ die größere Spannung.
--- falsch
Keiner: Gleiche Ladung erzeugt zwischen den Platten immer dasselbe Feld und dieselbe Spannung, gleich welches Bauteil.
--- falsch
Der mit der größeren Kapazität, weil er die Ladung dichter auf seinen Platten zusammendrängt und sie dort stärker drückt.
:::
:::karte zusammenhang Wann ein Kondensator voll ist
Kapazität klingt nach Fassungsvermögen: Was begrenzt die Ladung, die ein Kondensator aufnehmen kann?
---
Nicht $C$: Mehr Spannung bringt immer mehr Ladung, $C$ bleibt dabei gleich. Die Grenze setzt das Dielektrikum, das über einer bestimmten Feldstärke durchschlägt.
--- falsch
Die Kapazität selbst: Sie ist die größte Ladung, die er fasst. Ist sie erreicht, bringt weitere Spannung keine weitere Ladung mehr auf die Platten.
--- falsch
Die Zahl der freien Elektronen in den Platten: Sind sie alle von der einen Platte auf die andere gewandert, ist der Kondensator voll und nimmt nichts mehr auf.
--- falsch
Die Batterie: Ein Kondensator nimmt höchstens so viel Ladung auf, wie in der Batterie gespeichert ist; danach ist er voll, auch wenn die Spannung steigt.
:::
:::karte zusammenhang Metall der Platten
Warum bleibt das Metall der Platten beim Laden praktisch unverändert?
---
Weil nur ein winziger Bruchteil seiner freien Elektronen wandert, beim Plattenpaar mit 9 V nur eines von $5\cdot10^{14}$. Diese sitzen auf der Innenseite der Platte.
--- falsch
Weil jedes Elektron, das die Platte verlässt, sofort aus dem Draht ersetzt wird; jede Platte behält deshalb genau so viele freie Elektronen wie vor dem Laden.
--- falsch
Weil sich die Ladung im Inneren des Metalls gleichmäßig verteilt und dort von den positiven Ionen des Gitters sofort neutralisiert wird.
--- falsch
Weil beim Laden gar keine Elektronen wandern; es baut sich nur das Feld zwischen den Platten auf, die Ladung im Metall bleibt gleich.
:::
::::
