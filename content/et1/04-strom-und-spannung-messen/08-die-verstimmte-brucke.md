---
title: Stufe 7: Die verstimmte Brücke
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom und Spannung messen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Kapitel 4: Strom und Spannung messen
order: 1140800
summary: Ändert sich ein Widerstand nur wenig oder laufend, stellt man nicht nach.
tags: Dehnungsmessstreifen
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Ändert sich ein Widerstand nur wenig oder laufend, stellt man nicht nach. Die Abweichung von null ist dann das Messsignal. Diese Stufe zeigt, warum so kleinste Änderungen sichtbar werden.
:::

**Die Idee.** Ein Instrument allein muss die ganze Spannung anzeigen, die Änderung ist davon ein winziger Teil. Die Brücke zieht die große gemeinsame Spannung ab. Übrig bleibt nur die Änderung, und die passt in einen kleinen Messbereich. Weil der Anzeigefehler am Bereichsendwert hängt, sinkt er mit dem Bereich.

:::satz Satz 7.1 (Brückenspannung)
<span class="anker" id="satz-7-1"></span>

Zwischen den Mittelpunkten liegt $U_\mathrm d=U_4-U_2$ mit den Spannungen $U_2$ an $R_2$ und $U_4$ an $R_4$:

<span class="anker" id="gl-7-1"></span>
$$U_\mathrm d=U_\mathrm q\left(\frac{R_4}{R_3+R_4}-\frac{R_2}{R_1+R_2}\right)=U_\mathrm q\,\frac{R_1R_4-R_2R_3}{(R_1+R_2)(R_3+R_4)}. \tag{7.1}$$

Für $R_1=R_2=R_3=R$ und $R_4=R+\Delta R$ gilt

<span class="anker" id="gl-7-2"></span>
$$U_\mathrm d=\frac{U_\mathrm q}{4}\cdot\frac{\Delta R/R}{1+\Delta R/(2R)}\approx\frac{U_\mathrm q}{4}\cdot\frac{\Delta R}{R}\qquad\text{für }\Delta R\ll R. \tag{7.2}$$
:::

⁠**So liest man das:** Der Zähler in [(7.1)](#gl-7-1) wird im Abgleich null. $\Delta R/R$ ist die relative Änderung, ohne Einheit. **Gültigkeit:** Das Voltmeter entnimmt keinen merklichen Strom. **Grenzfälle:** $\Delta R=0$ ergibt $U_\mathrm d=0$. $\Delta R\to\infty$ ergibt $U_\mathrm d\to U_\mathrm q/2$: Der rechte Mittelpunkt liegt dann am Pluspol.

:::herleitung Kleine Änderung
Mit $U_2=U_\mathrm q/2$ und $U_4=U_\mathrm q(R+\Delta R)/(2R+\Delta R)$ ist

$$U_\mathrm d=U_\mathrm q\,\frac{2(R+\Delta R)-(2R+\Delta R)}{2(2R+\Delta R)}=\frac{U_\mathrm q\,\Delta R}{4R+2\Delta R}=\frac{U_\mathrm q}{4}\cdot\frac{\Delta R/R}{1+\Delta R/(2R)}.$$
:::

:::abbildung et1/k4dms 9
Links die Brücke mit dem veränderlichen $R_4$. Rechts dieselbe Änderung auf zwei Skalen: rote Linie die Anzeige, helles Band der Anzeigefehler. Auf der 10-V-Skala geht eine Änderung um 9 mV im Fehler unter. Auf der 100-mV-Skala ist die Abweichung selbst das Signal.
:::

::::beispiel Dehnungsmessstreifen
Ein __Dehnungsmessstreifen__ ist eine dünne Metallbahn, die auf ein Bauteil geklebt wird. Dehnt sich das Bauteil, wird die Bahn länger und dünner, und ihr Widerstand $R=\rho\,l/A$ steigt. Die relative Widerstandsänderung beträgt etwa das Doppelte der Dehnung. Bei 2 ‰ Dehnung wächst $R_4$ um 0,4 % von 350 $\Omega$ auf 351,4 $\Omega$. Dann ist $U_2=4{,}500$ V und $U_4=9\,\mathrm{V}\cdot351{,}4/701{,}4=4{,}509$ V, also $U_\mathrm d=8{,}98$ mV. Die Näherung gibt 9,00 mV, sie weicht um 0,2 % ab. Am 10-M$\Omega$-Voltmeter fließen 0,9 nA, gegen 12,9 mA in den Zweigen ein Anteil von $7\cdot10^{-8}$: vernachlässigbar.
::::

**Warum das genauer ist.** Direkt gemessen müsste das Instrument 4,509 V von 4,500 V unterscheiden, also im 10-V-Bereich drei Stellen hinter dem Komma sicher anzeigen. Sein Anzeigefehler von $\pm100$ mV ist aber das Elffache der gesuchten Änderung. An der Brücke reicht der 100-mV-Bereich mit $\pm1$ mV, ein Hundertstel davon (Abb. [9](#abb-9)). Dazu kommen zwei Vorteile. Schwankt die Quelle um 1 %, ändert sich $U_4$ um 45 mV, das Fünffache des Signals, $U_\mathrm d$ dagegen nur um 0,09 mV. Und ändern sich alle vier Widerstände um denselben Faktor, etwa durch Wärme, bleibt $U_\mathrm d$ gleich.

:::frage Könnte man nicht $U_4$ messen und im Kopf 4,5 V abziehen?
Rechnen lässt sich das, aber die $\pm100$ mV Anzeigefehler bleiben im Ergebnis. Die Brücke zieht ab, bevor das Instrument misst. Deshalb darf es einen kleinen Bereich haben.
:::

⁠**Von hier an:** Wenn nichts anderes dasteht, gelten Messgeräte in allen folgenden Teilen als ideal: Amperemeter mit $R_\mathrm i\to0$, Voltmeter mit $R_\mathrm i\to\infty$.

:::aufgabe Aufgabe 8 ★★★ Zwei Messstreifen
<span class="anker" id="aufg-8"></span>

Im rechten Zweig sitzen nun zwei Messstreifen: $R_3=R-\Delta R$ wird gestaucht, $R_4=R+\Delta R$ gedehnt, $R_1=R_2=R$. (a) Berechne $U_\mathrm d$ allgemein und für das Beispiel. (b) Warum ist das Ergebnis exakt linear in $\Delta R$? (c) Was ändert sich, wenn sich alle vier Widerstände durch Wärme um 1 % ändern?

:::loesung
(a) $R_3+R_4=2R$, also $U_4=U_\mathrm q(R+\Delta R)/(2R)$. Mit $U_2=U_\mathrm q/2$ folgt $U_\mathrm d=\frac12U_\mathrm q\,\Delta R/R=4{,}5\,\mathrm{V}\cdot0{,}004=18{,}0$ mV, doppelt so viel wie mit einem Streifen.

(b) Die Summe $R_3+R_4$ bleibt $2R$. Der Strom im rechten Zweig bleibt deshalb 12,9 mA, und $U_4$ wächst genau mit $R_4$. Bei einem Streifen wächst die Summe mit, das ergibt den Nenner in [(7.2)](#gl-7-2).

(c) Nichts: In [(7.1)](#gl-7-1) kürzt sich ein gemeinsamer Faktor aller Widerstände heraus.
:::
:::

::::formelsammlung
**Brückenspannung**

$$U_\mathrm d=U_4-U_2,\qquad U_\mathrm d=U_\mathrm q\left(\frac{R_4}{R_3+R_4}-\frac{R_2}{R_1+R_2}\right)=U_\mathrm q\,\frac{R_1R_4-R_2R_3}{(R_1+R_2)(R_3+R_4)}$$

$U_2$ Spannung an $R_2$, $U_4$ an $R_4$. Der Zähler wird im Abgleich null. Gilt, solange das Voltmeter keinen merklichen Strom entnimmt. Ändern sich alle vier Widerstände um denselben Faktor, kürzt er sich heraus.

**Kleine Änderung eines Widerstands**

$$U_\mathrm d=\frac{U_\mathrm q}{4}\cdot\frac{\Delta R/R}{1+\Delta R/(2R)}\approx\frac{U_\mathrm q}{4}\cdot\frac{\Delta R}{R}$$

$R_1=R_2=R_3=R$ und $R_4=R+\Delta R$; die Näherung gilt für $\Delta R\ll R$. $\Delta R/R$ ist die relative Änderung, ohne Einheit. Für $\Delta R\to\infty$ geht $U_\mathrm d\to U_\mathrm q/2$.

**Zwei Messstreifen im selben Zweig**

$$U_\mathrm d=\frac12U_\mathrm q\,\Delta R/R$$

$R_3=R-\Delta R$ gestaucht, $R_4=R+\Delta R$ gedehnt, $R_1=R_2=R$. Exakt linear und doppelt so groß wie mit einem Streifen, weil $R_3+R_4=2R$ und damit der Strom im Zweig gleich bleibt.

**Widerstand des Dehnungsmessstreifens**

$$R=\rho\,l/A$$

Dehnt sich das Bauteil, wird die Metallbahn länger und dünner, und $R$ steigt; die relative Widerstandsänderung beträgt etwa das Doppelte der Dehnung.
::::

::::lernkarten
:::karte zusammenhang Prinzip der verstimmten Brücke
Warum macht eine verstimmte Brücke kleinste Widerstandsänderungen sichtbar, die ein Instrument allein nicht auflösen kann?
---
Ein Instrument allein muss die ganze Spannung anzeigen, die Änderung ist davon ein winziger Teil. Die Brücke zieht die gemeinsame Spannung ab; übrig bleibt nur die Änderung, und die passt in einen kleinen Bereich mit kleinem Anzeigefehler.
--- falsch
Die Brücke verstärkt die Änderung: Vier Widerstände ergeben zusammen das Vierfache der Spannungsänderung eines einzelnen, deshalb reicht danach ein gewöhnlicher Messbereich mit seinem üblichen Anzeigefehler, und die Änderung ist gut zu sehen.
--- falsch
Die Brücke hält die Quellspannung konstant; ohne Schwankungen der Quelle lässt sich auch eine sehr kleine Änderung im großen Messbereich sicher ablesen, ohne dass der Anzeigefehler stört.
--- falsch
Die Brücke wird so lange nachgestellt, bis die Änderung ausgeglichen ist; die Stellung des Einstellwiderstands zeigt dann die Änderung mit der Genauigkeit der Widerstände an, ohne dass eine Spannung abzulesen ist.
:::
:::karte formel Brückenspannung
Wie groß ist die Spannung $U_\mathrm d$ zwischen den Mittelpunkten einer Brücke mit den Widerständen $R_1$ bis $R_4$ an der Quellspannung $U_\mathrm q$?
---
$U_\mathrm d=U_\mathrm q\,\frac{R_1R_4-R_2R_3}{(R_1+R_2)(R_3+R_4)}$ mit $U_\mathrm d=U_4-U_2$, den Spannungen an $R_4$ und $R_2$. Der Zähler wird im Abgleich null. Das gilt, solange das Voltmeter keinen merklichen Strom entnimmt.
--- falsch
$U_\mathrm d=U_\mathrm q\,\frac{R_1R_2-R_3R_4}{(R_1+R_2)(R_3+R_4)}$ mit $U_\mathrm d=U_4-U_2$, den Spannungen an $R_4$ und $R_2$. Der Zähler wird im Abgleich null, wenn beide Zweige gleich groß sind; das gilt für jedes Voltmeter.
--- falsch
$U_\mathrm d=U_\mathrm q\,\frac{R_1R_4-R_2R_3}{R_1+R_2+R_3+R_4}$ mit $U_\mathrm d=U_4-U_2$. Der Zähler wird im Abgleich null; der Nenner ist der Gesamtwiderstand der vier Brückenwiderstände, die an der Quelle liegen.
--- falsch
$U_\mathrm d=U_\mathrm q\,\frac{R_1R_4-R_2R_3}{(R_1+R_2)(R_3+R_4)}$ mit $U_\mathrm d=U_4-U_2$. Der Zähler wird im Abgleich null; das gilt für jedes Voltmeter, gleich welchen Strom es entnimmt.
:::
:::karte formel Kleine Änderung eines Widerstands
Welche Brückenspannung ergibt sich, wenn bei $R_1=R_2=R_3=R$ der vierte Widerstand $R_4=R+\Delta R$ ist, und wann ist sie linear in $\Delta R$?
---
$U_\mathrm d=\frac{U_\mathrm q}{4}\cdot\frac{\Delta R/R}{1+\Delta R/(2R)}\approx\frac{U_\mathrm q}{4}\cdot\frac{\Delta R}{R}$; die Näherung gilt für $\Delta R\ll R$. $\Delta R/R$ ist die relative Änderung, ohne Einheit.
--- falsch
$U_\mathrm d=\frac{U_\mathrm q}{2}\cdot\frac{\Delta R}{R}$, exakt für jede Änderung: Weil sich nur ein Widerstand ändert, ist die Brückenspannung immer streng linear in $\Delta R$.
--- falsch
$U_\mathrm d\approx\frac{U_\mathrm q}{4}\cdot\frac{\Delta R}{R}$, aber nur für große Änderungen $\Delta R\gg R$; bei kleinen Änderungen ist die Brückenspannung nicht linear in $\Delta R$.
--- falsch
$U_\mathrm d=U_\mathrm q\cdot\frac{\Delta R}{R}$ für $\Delta R\ll R$: Die ganze relative Änderung erscheint als Anteil der Quellspannung zwischen den beiden Mittelpunkten.
:::
:::karte herleitung Brückenspannung bei kleiner Änderung
Leite die Brückenspannung für $R_1=R_2=R_3=R$ und $R_4=R+\Delta R$ her, ausgehend von den Spannungen der beiden Teiler.
---
Links ist $U_2=U_\mathrm q/2$, weil $R_1=R_2$ die Spannung halbiert.
---
Rechts ist $U_4=U_\mathrm q(R+\Delta R)/(2R+\Delta R)$, weil der Teiler aus $R$ und $R+\Delta R$ die Spannung im Verhältnis der Widerstände aufteilt.
---
Auf den gemeinsamen Nenner gebracht ist $U_\mathrm d=U_\mathrm q\,\frac{2(R+\Delta R)-(2R+\Delta R)}{2(2R+\Delta R)}=\frac{U_\mathrm q\,\Delta R}{4R+2\Delta R}$, weil $U_\mathrm d=U_4-U_2$ ist.
---
Teilen von Zähler und Nenner durch $4R$ ergibt $\frac{U_\mathrm q}{4}\cdot\frac{\Delta R/R}{1+\Delta R/(2R)}$, weil so die relative Änderung $\Delta R/R$ sichtbar wird.
---
Für $\Delta R\ll R$ ist der Nenner praktisch 1, und es bleibt $\frac{U_\mathrm q}{4}\cdot\frac{\Delta R}{R}$, weil $\Delta R/(2R)$ gegen 1 nicht ins Gewicht fällt.
:::
:::karte begriff Dehnungsmessstreifen
Was ist ein Dehnungsmessstreifen, und warum ändert sich sein Widerstand, wenn sich das Bauteil dehnt?
---
Eine dünne Metallbahn, die auf ein Bauteil geklebt wird. Dehnt sich das Bauteil, wird die Bahn länger und dünner, und ihr Widerstand $R=\rho\,l/A$ steigt; die relative Widerstandsänderung beträgt etwa das Doppelte der Dehnung.
--- falsch
Eine dünne Metallbahn, die auf ein Bauteil geklebt wird. Dehnt sich das Bauteil, wird die Bahn länger, aber auch breiter, sodass ihr Widerstand gleich bleibt; gemessen wird stattdessen die Spannung, die beim Dehnen in ihr entsteht.
--- falsch
Ein kleiner Kondensator, der auf ein Bauteil geklebt wird. Dehnt sich das Bauteil, rücken seine Platten auseinander, und seine Kapazität sinkt etwa im selben Verhältnis wie die Dehnung.
--- falsch
Eine dünne Metallbahn, die auf ein Bauteil geklebt wird. Dehnt sich das Bauteil, wird die Bahn kürzer und dicker, und ihr Widerstand $R=\rho\,l/A$ sinkt um etwa die Hälfte der Dehnung.
:::
:::karte zusammenhang Direkt gemessen geht die Änderung unter
Warum lässt sich die Änderung an einem Dehnungsmessstreifen von 4,500 V auf 4,509 V nicht im 10-V-Bereich messen, wohl aber an der Brücke?
---
Im 10-V-Bereich beträgt der Anzeigefehler $\pm100$ mV, das Elffache der gesuchten Änderung. An der Brücke liegen nur rund 9 mV an; dafür reicht der 100-mV-Bereich mit $\pm1$ mV, ein Hundertstel davon.
--- falsch
Im 10-V-Bereich zeigt das Instrument nur zwei Stellen hinter dem Komma an; an der Brücke wird die Spannung durch die vier Widerstände um den Faktor 1000 verstärkt, sodass drei Stellen genügen.
--- falsch
Im 10-V-Bereich zieht das Voltmeter zu viel Strom aus dem Messstreifen; an der Brücke fließt durch das Voltmeter gar kein Strom, deshalb misst es dort genauer, auch im selben Bereich.
--- falsch
Im 10-V-Bereich beträgt der Anzeigefehler $\pm1$ mV und ist damit zu groß; an der Brücke sinkt er im selben Bereich auf $\pm0{,}01$ mV, weil dort die Spannung kleiner ist.
:::
:::karte zusammenhang Schwankende Quelle
Was bewirkt eine Schwankung der Quellspannung um 1 % bei der verstimmten Brücke, verglichen mit einer direkten Messung von $U_4$?
---
$U_4$ ändert sich um 45 mV, das Fünffache des Signals. $U_\mathrm d$ ist proportional zu $U_\mathrm q$, aber klein: Es ändert sich nur um 1 % seiner selbst, also um 0,09 mV.
--- falsch
Beide ändern sich gleich um 45 mV, weil die Quelle die ganze Brücke speist; die Brücke hilft nur gegen Anzeigefehler, aber nicht gegen eine schwankende Quelle.
--- falsch
$U_\mathrm d$ ändert sich doppelt so stark wie $U_4$, weil die Schwankung in beiden Zweigen auftritt und sich zwischen den Mittelpunkten addiert.
--- falsch
$U_4$ bleibt gleich, weil die Brücke die Quelle stabilisiert; $U_\mathrm d$ ändert sich dagegen um 1 % der Quellspannung, also um 90 mV, das Zehnfache des Signals.
:::
:::karte zusammenhang Gleiche Änderung aller Widerstände
Was geschieht mit $U_\mathrm d$, wenn sich alle vier Brückenwiderstände um denselben Faktor ändern, etwa durch Wärme?
---
Nichts: In der Gleichung für $U_\mathrm d$ kürzt sich ein gemeinsamer Faktor aller Widerstände heraus, denn beide Teilerverhältnisse bleiben gleich.
--- falsch
$U_\mathrm d$ ändert sich um denselben Faktor, weil die Spannung an jedem Widerstand mit seinem Wert wächst; eine Brücke muss deshalb immer bei fester Temperatur arbeiten.
--- falsch
$U_\mathrm d$ springt auf $U_\mathrm q/2$, weil sich die Brücke dabei vollständig verstimmt; erst ein neuer Abgleich bringt sie wieder in die Ausgangslage zurück.
--- falsch
Nichts, aber nur an einer Stromquelle; an einer Spannungsquelle ändert sich $U_\mathrm d$ um denselben Faktor wie die Widerstände, weil sich der Strom nicht anpasst.
:::
:::karte zusammenhang Im Kopf abziehen
Warum genügt es nicht, $U_4$ direkt zu messen und die gemeinsame Spannung von 4,5 V im Kopf abzuziehen?
---
Rechnen lässt sich das, aber die $\pm100$ mV Anzeigefehler des großen Bereichs bleiben im Ergebnis. Die Brücke zieht ab, bevor das Instrument misst; deshalb darf es einen kleinen Bereich haben.
--- falsch
Es genügt: Das Abziehen im Kopf liefert dasselbe Ergebnis wie die Brücke, nur langsamer; die Brücke ist lediglich bequemer, aber kein bisschen genauer als die Rechnung mit einem guten Gerät.
--- falsch
Weil man die gemeinsame Spannung nicht kennt: Sie hängt vom gesuchten Widerstand ab und lässt sich nur mit der Brücke bestimmen, nicht aus den Widerständen ausrechnen.
--- falsch
Weil das Instrument beim Messen von $U_4$ den Teiler belastet und $U_4$ dadurch um mehr als die Änderung sinkt; an der Brücke ist der Teiler dagegen unbelastet.
:::
:::karte formel Zwei Messstreifen im selben Zweig
Welche Brückenspannung ergibt sich mit zwei Messstreifen im rechten Zweig, $R_3=R-\Delta R$ gestaucht und $R_4=R+\Delta R$ gedehnt, bei $R_1=R_2=R$?
---
$U_\mathrm d=\frac12U_\mathrm q\,\Delta R/R$, doppelt so viel wie mit einem Streifen und exakt linear: Die Summe $R_3+R_4$ bleibt $2R$, der Strom im rechten Zweig bleibt gleich, und $U_4$ wächst genau mit $R_4$.
--- falsch
$U_\mathrm d=0$: Die Stauchung von $R_3$ hebt die Dehnung von $R_4$ genau auf, sodass der rechte Mittelpunkt bei jeder Belastung des Bauteils auf $U_\mathrm q/2$ bleibt und kein Signal entsteht.
--- falsch
$U_\mathrm d\approx\frac14U_\mathrm q\,\Delta R/R$ wie mit einem Streifen: Der zweite Streifen bringt keinen Gewinn, weil im selben Zweig nur die Summe der beiden Widerstände für den Strom zählt.
--- falsch
$U_\mathrm d=\frac12U_\mathrm q\,\Delta R/R$, aber nur näherungsweise für $\Delta R\ll R$: Wie bei einem Streifen wächst die Summe $R_3+R_4$ mit, und das ergibt einen Nenner, der die Kurve krümmt.
:::
:::karte zusammenhang Grenzfälle der Brückenspannung
Welche Brückenspannung ergibt sich mit einem veränderlichen Widerstand $R_4=R+\Delta R$ für $\Delta R=0$ und für $\Delta R\to\infty$?
---
$\Delta R=0$ ergibt $U_\mathrm d=0$, die Brücke ist abgeglichen. $\Delta R\to\infty$ ergibt $U_\mathrm d\to U_\mathrm q/2$, denn der rechte Mittelpunkt liegt dann am Pluspol.
--- falsch
$\Delta R=0$ ergibt $U_\mathrm d=U_\mathrm q/4$, die Ruhespannung der Brücke. $\Delta R\to\infty$ ergibt $U_\mathrm d\to\infty$, weil die Spannung mit dem Widerstand unbegrenzt wächst.
--- falsch
$\Delta R=0$ ergibt $U_\mathrm d=0$. $\Delta R\to\infty$ ergibt $U_\mathrm d\to U_\mathrm q$, denn dann liegt die ganze Quellspannung zwischen den beiden Mittelpunkten.
--- falsch
$\Delta R=0$ ergibt $U_\mathrm d=0$. $\Delta R\to\infty$ ergibt ebenfalls $U_\mathrm d\to0$, weil durch den unendlich großen Widerstand kein Strom mehr fließt.
:::
:::karte zusammenhang Strom des Voltmeters an der Brücke
Warum darf man an einer Brücke aus Widerständen von 350 $\Omega$ den Strom eines Voltmeters mit 10 M$\Omega$ vernachlässigen?
---
Bei rund 9 mV fließen durch das Voltmeter nur 0,9 nA, gegen 12,9 mA in den Zweigen ein Anteil von $7\cdot10^{-8}$. Damit ist die Voraussetzung erfüllt, dass das Voltmeter keinen merklichen Strom entnimmt.
--- falsch
Weil im Abgleich durch das Voltmeter grundsätzlich kein Strom fließt; an der verstimmten Brücke gilt das genauso, solange die Änderung des Widerstands unter 1 % bleibt.
--- falsch
Weil das Voltmeter seinen Strom aus der eigenen Batterie bezieht und nicht aus der Brücke; die Zweige merken deshalb nichts davon, gleich wie groß sein Innenwiderstand ist.
--- falsch
Weil der Strom des Voltmeters in beiden Zweigen gleich groß ist und sich in der Differenz $U_4-U_2$ heraushebt; deshalb stört auch ein Gerät mit kleinem Innenwiderstand die Messung nicht.
:::
::::
