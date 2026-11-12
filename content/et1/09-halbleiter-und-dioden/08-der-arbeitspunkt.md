---
title: Stufe 6: Der Arbeitspunkt
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Halbleiter und Dioden
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Kapitel 9: Halbleiter und Dioden
order: 1190800
summary: Bei einem Widerstand liefert U=R\,I sofort das Ergebnis.
tags: Arbeitsgerade, Arbeitspunkt, Arbeitspunktanalyse, Arbeitspunktsynthese, Leerlauf, Kurzschluss, Hysterese, Iteration
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Bei einem Widerstand liefert $U=R\,I$ sofort das Ergebnis. Die Diode folgt einer anderen Kurve. Diese Stufe findet Spannung und Strom der Diode in einer Schaltung.
:::

**Die Idee.** Zwei Bedingungen müssen zugleich gelten. Die Diode lässt nur Punkte auf ihrer Kennlinie zu. Der Rest der Schaltung, Quelle und Widerstand, lässt nur Punkte auf der __Arbeitsgerade__ zu ([Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). Die Schaltung findet den Schnittpunkt selbst: Ist $U_\mathrm D$ zu klein, liefert der Widerstand mehr Strom, als die Diode durchlässt. Ladung staut sich am Knoten zwischen beiden und hebt sein Potenzial, bis beide Ströme gleich sind.

:::abbildung et1/k9arbeitsgerade 8
Schaltung des Rechenmodells und grafische Lösung. Rot die Arbeitsgerade durch Leerlauf und Kurzschluss. Blau die Kennlinie der Diode, Schnittpunkt bei 0,69 V und 4,31 mA. Grün die Kennlinie eines Widerstands von 250 $\Omega$ anstelle der Diode, Schnittpunkt bei 1 V und 4 mA.
:::

:::definition Definition 6.1 (Arbeitspunkt)
<span class="anker" id="satz-6-1"></span>

Der __Arbeitspunkt__ (AP) ist der Punkt auf der Kennlinie, den Strom durch das Bauteil und Spannung über dem Bauteil festlegen. __Arbeitspunktanalyse__ heißt, ihn aus der gegebenen Schaltung zu ermitteln. __Arbeitspunktsynthese__ heißt, die Bauteile so zu wählen, dass ein gewünschter AP entsteht.
:::

**Der lineare Fall.** Ersetzt man die Diode durch einen Widerstand $R_1$, gelten Bauteilgleichung, Maschenregel und daraus die Arbeitsgerade:

<span class="anker" id="gl-6-1"></span>
$$I=\frac{U_{R1}}{R_1},\qquad U_0=U_R+U_{R1}=R\,I+U_{R1},\qquad I=\frac{U_0-U_{R1}}{R}. \tag{6.1}$$

Zwei lineare Gleichungen lassen sich auflösen, mit $R_1=250\,\Omega$ folgt $I=U_0/(R+R_1)=4$ mA und $U_{R1}=1$ V. Das Gleichungssystem zu lösen heißt, beide Geraden zu schneiden.

:::satz Satz 6.2 (Arbeitspunkt der Diode)
<span class="anker" id="satz-6-2"></span>

Für die Reihenschaltung gelten zugleich

<span class="anker" id="gl-6-2"></span>
$$I=\frac{U_0-U_\mathrm D}{R}\qquad\text{und}\qquad I=I_\mathrm S\bigl(\mathrm{e}^{U_\mathrm D/U_T}-1\bigr). \tag{6.2}$$

Die Kennlinie steigt überall, die Gerade fällt überall, also gibt es genau einen Schnittpunkt.
:::

⁠**So liest man das:** $U_\mathrm D$ ist die Spannung $U$ aus [(4.1)](warum-der-strom-exponentiell-wachst.html#gl-4-1). Die Arbeitsgerade zeichnet man durch zwei Punkte, ohne die Diode zu beachten: __Leerlauf__ ($I=0$, $U_\mathrm D=U_0$) und __Kurzschluss__ ($U_\mathrm D=0$, $I=U_0/R$). Die Kennlinie kommt aus der Gleichung oder einem Datenblatt. **Gültigkeit:** Bauteile, deren Kennlinie zurückläuft oder deren Zustand von der Vorgeschichte abhängt (__Hysterese__), können mehrere Schnittpunkte haben. Mehrere nichtlineare Bauteile löst man numerisch oder mit Ersatzschaltungen (Stufe [7](lineare-ersatzschaltungen.html#stufe-7)).

[(6.2)](#gl-6-2) lässt sich nicht nach $U_\mathrm D$ auflösen, weil $U_\mathrm D$ im Exponenten und außerhalb steht. Man löst grafisch oder durch __Iteration__, also durch wiederholtes Einsetzen: Schätze $U_\mathrm D$, berechne $I=(U_0-U_\mathrm D)/R$, dann $U_\mathrm D=U_T\ln(I/I_\mathrm S+1)$, und wiederhole.

::::beispiel
Start mit $U_\mathrm D=0{,}7$ V. Schritt 1: $I=4{,}300$ mA, $U_\mathrm D=0{,}69245$ V. Schritt 2: $I=4{,}3076$ mA, $U_\mathrm D=0{,}69249$ V. Damit ist der AP (0,692 V | 4,31 mA), am Widerstand liegen 4,31 V. Verdoppelt man $U_0$ auf 10 V, verdoppelt sich der Strom fast, auf 9,29 mA, und $U_\mathrm D$ steigt nur um 20 mV auf 0,712 V.
::::

⁠**Grenzfälle:** Bei $U_0=0{,}5$ V ist $I=2{,}3$ µ A, fast die ganze Quellenspannung bleibt an der Diode. Bei negativem $U_0$ ist $I=-I_\mathrm S$, die Quelle liegt ganz an der Diode.

:::frage Warum rechnet man nicht umgekehrt: $U_\mathrm D$ schätzen, $I$ aus der Exponentialfunktion, dann $U_\mathrm D=U_0-R\,I$?
Weil dieser Weg auseinanderläuft. Ein Fehler von 1 mV ändert den Diodenstrom um 3,9 %, also 0,17 mA, und das ergibt am Widerstand 167 mV Fehler. Im ersten Verfahren schrumpft der Fehler je Schritt um denselben Faktor, $r/R=0{,}006$ (Stufe [8](kleine-anderungen-um-den-arbeitspunkt.html#stufe-8)). Die flache Logarithmusfunktion dämpft, die steile Exponentialfunktion verstärkt.
:::

:::aufgabe Aufgabe 7 ★★ Arbeitspunkt finden und einstellen
<span class="anker" id="aufg-7"></span>

Die Diode des Rechenmodells liegt in Reihe mit $R=470\,\Omega$ an $U_0=3$ V.

<ol class="al">

<li>

Bestimme Leerlauf und Kurzschluss der Arbeitsgerade.

</li>

<li>

Iteriere von 0,7 V aus, bis sich drei Stellen nicht mehr ändern.

</li>

<li>

Arbeitspunktsynthese: Welches $R$ ergibt an $U_0=5$ V den Strom 2 mA? Welcher Strom fließt mit dem Normwert 2,2 k$\Omega$?

</li>

<li>

Die Diode wird umgedreht. Was misst man an Diode und Widerstand?

</li>

</ol>

:::loesung
(a) Leerlauf $U_\mathrm D=3$ V, Kurzschluss $I=3\,\mathrm{V}/470\,\Omega=6{,}38$ mA. (b) $U_\mathrm D=0{,}7$ V ergibt $I=4{,}894$ mA, das ergibt $U_\mathrm D=0{,}6958$ V, dann $I=4{,}903$ mA und wieder $U_\mathrm D=0{,}6958$ V. AP: (0,696 V | 4,90 mA). (c) Bei 2 mA ist $U_\mathrm D=0{,}673$ V, also $R=(5\,\mathrm{V}-0{,}673\,\mathrm{V})/2\,\mathrm{mA}=2{,}16\,\mathrm{k\Omega}$. Mit 2,2 k$\Omega$ fließen 1,97 mA. (d) Die Diode sperrt: $I=-10^{-14}$ A, am Widerstand 4,7 pV, an der Diode $-3$ V.
:::
:::

::::formelsammlung
**Widerstand statt Diode**

$$I=\frac{U_{R1}}{R_1},\qquad U_0=U_R+U_{R1}=R\,I+U_{R1}$$

Bauteilgleichung und Maschenregel für die Reihenschaltung aus Quelle $U_0$, Widerstand $R$ und Widerstand $R_1$; Lösung $I=U_0/(R+R_1)$. Das Gleichungssystem zu lösen heißt, beide Geraden zu schneiden.

**Arbeitspunkt der Diode**

$$I=\frac{U_0-U_\mathrm D}{R}\qquad\text{und}\qquad I=I_\mathrm S\bigl(\mathrm{e}^{U_\mathrm D/U_T}-1\bigr)$$

Links die Arbeitsgerade durch Leerlauf ($I=0$, $U_\mathrm D=U_0$) und Kurzschluss ($U_\mathrm D=0$, $I=U_0/R$), rechts die Kennlinie. Die Kennlinie steigt überall, die Gerade fällt überall, also gibt es genau einen Schnittpunkt.

**Iteration**

$$I=(U_0-U_\mathrm D)/R,\qquad U_\mathrm D=U_T\ln(I/I_\mathrm S+1)$$

$U_\mathrm D$ schätzen, $I$ berechnen, daraus das neue $U_\mathrm D$, wiederholen. In dieser Reihenfolge schrumpft der Fehler je Schritt; umgekehrt läuft das Verfahren auseinander.
::::

::::lernkarten
:::karte zusammenhang Arbeitspunkt und Arbeitsgerade
Warum liegt der Arbeitspunkt einer Diode in Reihe mit Quelle und Widerstand im Schnittpunkt ihrer Kennlinie mit der Arbeitsgerade?
---
Zwei Bedingungen müssen zugleich gelten: Die Diode lässt nur Punkte auf ihrer Kennlinie zu, Quelle und Widerstand nur Punkte auf der Arbeitsgerade. Beide erfüllt nur der Schnittpunkt.
--- falsch
Die Arbeitsgerade gibt die größte Leistung an, die der Widerstand verträgt. Der Arbeitspunkt liegt dort, wo die Diode gerade so viel Leistung umsetzt wie der Widerstand, und keinen Punkt weiter.
--- falsch
Die Arbeitsgerade ist die Tangente an die Kennlinie im Arbeitspunkt. Der Schnittpunkt ist der einzige Punkt, an dem sich die Diode wie ein ohmscher Widerstand verhält.
--- falsch
Die Diode stellt ihren Strom selbst ein, und der Widerstand folgt nur. Der Schnittpunkt ist eine Rechenhilfe; die Schaltung landet auch bei anderen Punkten der Kennlinie.
:::
:::karte zusammenhang Wie die Schaltung den Arbeitspunkt findet
Was passiert in der Reihenschaltung aus Quelle, Widerstand und Diode, wenn die Diodenspannung $U_\mathrm D$ kleiner ist als im Arbeitspunkt?
---
Dann liefert der Widerstand mehr Strom, als die Diode durchlässt. Ladung staut sich am Knoten zwischen beiden und hebt sein Potenzial, bis beide Ströme gleich sind.
--- falsch
Dann lässt die Diode mehr Strom durch, als der Widerstand liefert. Der Knoten zwischen beiden entlädt sich, und sein Potenzial sinkt weiter, bis die Diode ganz sperrt.
--- falsch
Dann fließt kein Strom, bis die Quelle von außen nachgestellt wird. Ohne Eingriff bleibt die Schaltung bei dieser Spannung stehen, weil die Diode sperrt.
--- falsch
Dann liefert der Widerstand mehr Strom, als die Diode durchlässt. Der Überschuss fließt über die Quelle zurück, und $U_\mathrm D$ bleibt bei diesem Wert stehen.
:::
:::karte begriff Arbeitspunktanalyse und Arbeitspunktsynthese
Was unterscheidet Arbeitspunktanalyse und Arbeitspunktsynthese bei einer Diodenschaltung?
---
Arbeitspunktanalyse heißt, den Arbeitspunkt aus der gegebenen Schaltung zu ermitteln. Arbeitspunktsynthese heißt, die Bauteile so zu wählen, dass ein gewünschter Arbeitspunkt entsteht.
--- falsch
Arbeitspunktanalyse heißt, die Bauteile für einen gewünschten Arbeitspunkt zu wählen. Arbeitspunktsynthese heißt, den Arbeitspunkt aus der gegebenen Schaltung zu ermitteln.
--- falsch
Arbeitspunktanalyse heißt, den Arbeitspunkt zu messen. Arbeitspunktsynthese heißt, ihn zu berechnen, weil man dabei Kennlinie und Arbeitsgerade zusammensetzt.
--- falsch
Arbeitspunktanalyse bestimmt die Spannung im Arbeitspunkt, Arbeitspunktsynthese den zugehörigen Strom. Beide Schritte zusammen ergeben erst den vollständigen Arbeitspunkt der Schaltung.
:::
:::karte formel Gleichungen des Arbeitspunkts
Welche zwei Gleichungen gelten im Arbeitspunkt einer Diode in Reihe mit $R$ an $U_0$ zugleich, und warum gibt es genau einen Schnittpunkt?
---
$I=\frac{U_0-U_\mathrm D}{R}$ und $I=I_\mathrm S\bigl(\mathrm{e}^{U_\mathrm D/U_T}-1\bigr)$. Die Kennlinie steigt überall, die Gerade fällt überall, also schneiden sie sich genau einmal.
--- falsch
$I=\frac{U_0+U_\mathrm D}{R}$ und $I=I_\mathrm S\bigl(\mathrm{e}^{U_\mathrm D/U_T}-1\bigr)$. Beide steigen überall, und weil die Kennlinie schneller steigt, holt sie die Gerade genau einmal ein.
--- falsch
$I=\frac{U_0-U_\mathrm D}{R}$ und $I=I_\mathrm S\bigl(\mathrm{e}^{U_\mathrm D/U_T}-1\bigr)$. Meist gibt es zwei Schnittpunkte, einen bei kleinem und einen bei großem Strom; die Schaltung wählt den stabileren.
--- falsch
$I=\frac{U_\mathrm D}{R}$ und $I=I_\mathrm S\,\mathrm{e}^{U_0/U_T}$. Der Widerstand legt den Strom fest, die Quelle die Höhe der Kennlinie, und beide zusammen ergeben einen Punkt.
:::
:::karte herleitung Arbeitsgerade aus der Maschenregel
Wie folgt aus der Maschenregel für die Reihenschaltung aus Quelle $U_0$, Widerstand $R$ und einem Bauteil die Gleichung der Arbeitsgerade?
---
Mit einem Widerstand $R_1$ als Bauteil ergibt die Maschenregel $U_0=U_R+U_{R1}=R\,I+U_{R1}$, weil sich die Quellenspannung auf beide aufteilt und durch beide derselbe Strom fließt.
---
Auflösen nach dem Strom ergibt $I=\frac{U_0-U_{R1}}{R}$, weil nur $R\,I$ den Strom enthält.
---
Für die Diode gilt dieselbe Gleichung mit $U_\mathrm D$, also $I=\frac{U_0-U_\mathrm D}{R}$, weil die Gerade nur von Quelle und Widerstand abhängt und nicht vom angeschlossenen Bauteil.
---
Beim Widerstand kommt $I=\frac{U_{R1}}{R_1}$ hinzu, und es folgt $I=U_0/(R+R_1)$, weil das Lösen zweier linearer Gleichungen das Schneiden zweier Geraden ist.
:::
:::karte zusammenhang Leerlauf und Kurzschluss der Arbeitsgerade
Durch welche zwei Punkte zeichnet man die Arbeitsgerade einer Diodenschaltung, und warum braucht man dafür die Diode nicht?
---
Durch den Leerlauf ($I=0$, $U_\mathrm D=U_0$) und den Kurzschluss ($U_\mathrm D=0$, $I=U_0/R$). Die Gerade beschreibt nur Quelle und Widerstand, die Diode bestimmt erst den Punkt auf ihr.
--- falsch
Durch den Leerlauf ($I=0$, $U_\mathrm D=0$) und den Kurzschluss ($U_\mathrm D=U_0$, $I=U_0/R$). Die Gerade beschreibt nur Quelle und Widerstand, die Diode bestimmt erst den Punkt.
--- falsch
Durch den Ursprung und den Punkt ($U_0$ | $U_0/R$), weil ein Widerstand immer eine Ursprungsgerade hat. Die Diode verschiebt diese Gerade um ihre Durchlassspannung.
--- falsch
Durch den Leerlauf ($I=0$, $U_\mathrm D=U_0$) und den Punkt der Diode bei 0,7 V. Ohne die Diode kennt man den zweiten Punkt nicht und kann die Gerade nicht zeichnen.
:::
:::karte begriff Iteration
Wie löst man die Gleichungen des Arbeitspunkts durch Iteration, da man sie nicht nach $U_\mathrm D$ auflösen kann?
---
Durch wiederholtes Einsetzen: $U_\mathrm D$ schätzen, $I=(U_0-U_\mathrm D)/R$ berechnen, dann $U_\mathrm D=U_T\ln(I/I_\mathrm S+1)$, und wiederholen, bis sich nichts mehr ändert.
--- falsch
Durch wiederholtes Einsetzen: $U_\mathrm D$ schätzen, den Strom aus der Exponentialfunktion berechnen, dann $U_\mathrm D=U_0-R\,I$, und wiederholen, bis sich nichts mehr ändert.
--- falsch
Durch Logarithmieren beider Gleichungen: Danach sind beide linear in $U_\mathrm D$, und man löst sie wie zwei Geraden in einem einzigen Schritt.
--- falsch
Durch Ausprobieren aller Spannungen von 0 bis $U_0$ in Schritten von 1 mV, bis die Arbeitsgerade und die Kennlinie denselben Strom liefern.
:::
:::karte zusammenhang Richtung der Iteration
Warum iteriert man über $U_\mathrm D=U_T\ln(I/I_\mathrm S+1)$ und nicht umgekehrt über die Exponentialfunktion und $U_\mathrm D=U_0-R\,I$?
---
Der umgekehrte Weg läuft auseinander: 1 mV Fehler ändert den Diodenstrom um 3,9 % und ergibt am Widerstand 167 mV Fehler. Im ersten Verfahren schrumpft der Fehler je Schritt um den Faktor 0,006.
--- falsch
Beide Wege führen gleich schnell zum Ziel. Man wählt den Logarithmus nur, weil er sich mit dem Taschenrechner leichter berechnen lässt als die Exponentialfunktion, und spart so Zeit.
--- falsch
Der umgekehrte Weg liefert einen zweiten, falschen Arbeitspunkt, weil die Exponentialfunktion auch für negative Spannungen Lösungen hat, die die Iteration dann anzieht.
--- falsch
Der umgekehrte Weg läuft auseinander, weil die Logarithmusfunktion jeden Fehler verstärkt. Im ersten Verfahren dämpft dagegen die steile Exponentialfunktion den Fehler je Schritt um den Faktor 0,006.
:::
:::karte zusammenhang Doppelte Quellenspannung
Eine Diode liegt mit $R=1\,\mathrm{k\Omega}$ an $U_0=5$ V und führt 4,31 mA. Was passiert mit Strom und Diodenspannung, wenn man $U_0$ auf 10 V verdoppelt?
---
Der Strom verdoppelt sich fast, auf 9,29 mA, und $U_\mathrm D$ steigt nur um 20 mV auf 0,712 V. Die Diodenspannung bleibt fast fest, weil der Strom je 60 mV um den Faktor 10 wächst.
--- falsch
Strom und Diodenspannung verdoppeln sich beide, auf 8,62 mA und 1,38 V, weil sich die Diode in der Reihenschaltung wie ein fester Widerstand verhält und die Quelle stets im selben Verhältnis geteilt wird.
--- falsch
Der Strom bleibt bei 4,31 mA, weil die Diode ihn begrenzt; die zusätzlichen 5 V liegen ganz an der Diode, die dann 5,69 V trägt.
--- falsch
Der Strom steigt auf das Zehnfache, rund 43 mA, weil die Diodenspannung um 60 mV steigt und jede solche Stufe den Strom verzehnfacht.
:::
:::karte begriff Hysterese
Was bedeutet Hysterese bei einem Bauteil, und warum kann sie mehrere Arbeitspunkte ergeben?
---
Der Zustand des Bauteils hängt von seiner Vorgeschichte ab. Solche Bauteile, wie auch solche mit zurücklaufender Kennlinie, können mehrere Schnittpunkte mit der Arbeitsgerade haben.
--- falsch
Das Bauteil reagiert verzögert auf eine Spannungsänderung. Dadurch verschiebt sich die Arbeitsgerade mit der Zeit, und der Schnittpunkt wandert langsam weiter, bis das Bauteil zur Ruhe kommt.
--- falsch
Die Kennlinie des Bauteils ist eine Gerade durch den Ursprung. Weil sie die Arbeitsgerade in jedem ihrer Punkte berühren kann, gibt es unendlich viele Arbeitspunkte.
--- falsch
Der Zustand des Bauteils hängt nur von seiner Temperatur ab. Weil sich die Temperatur im Betrieb ständig ändert, gibt es mehrere Arbeitspunkte, auch bei der Diode.
:::
:::karte zusammenhang Umgedrehte Diode
Was misst man an Diode und Widerstand, wenn die Diode in der Reihenschaltung mit $R=470\,\Omega$ an $U_0=3$ V umgedreht wird?
---
Die Diode sperrt: Es fließt nur $I=-10^{-14}$ A, am Widerstand liegen 4,7 pV, an der Diode die ganze Spannung, $-3$ V.
--- falsch
Die Diode leitet nun in Gegenrichtung mit denselben 0,7 V. Am Widerstand liegen 2,3 V, nur die Stromrichtung ist umgekehrt.
--- falsch
Die Diode sperrt, und es fließt kein Strom. Dann fällt auch an ihr keine Spannung ab: Diode und Widerstand zeigen beide 0 V.
--- falsch
Die Diode sperrt, aber die Quelle drückt den Sperrstrom durch den Widerstand, an dem deshalb die ganze Spannung von 3 V liegt.
:::
::::
