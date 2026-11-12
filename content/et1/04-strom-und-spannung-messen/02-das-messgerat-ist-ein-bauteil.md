---
title: Stufe 1: Das Messgerät ist ein Bauteil
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom und Spannung messen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Kapitel 4: Strom und Spannung messen
order: 1140200
summary: Bevor sich ein Fehler berechnen lässt, muss klar sein, was ein Messgerät elektrisch ist: ein Bauteil mit zwei Anschlüssen und einem Widerstand dazwischen.
tags: Bereichsendwert
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Bevor sich ein Fehler berechnen lässt, muss klar sein, was ein Messgerät elektrisch ist: ein Bauteil mit zwei Anschlüssen und einem Widerstand dazwischen.
:::

**Die Idee.** Im Zeigerinstrument sitzt eine drehbare Spule aus dünnem Draht zwischen den Polen eines Dauermagneten (Abb. [1](#abb-1)). Fließt Strom, übt das Magnetfeld auf die bewegten Elektronen im Draht eine Kraft aus, und die Spule dreht sich gegen eine Spiralfeder. Die Drehkraft wächst mit dem Strom, die Gegenkraft der Feder mit dem Winkel. Deshalb ist der Ausschlag dem Strom proportional. Zwei Dinge lassen sich nicht vermeiden: Ohne Strom gibt es keinen Ausschlag, und mit Strom fällt am Draht Spannung ab. Ein Digitalmultimeter (Gerät mit Zahlenanzeige) wandelt die Spannung an einem internen Widerstand in eine Zahl um. Auch dort fließt Strom durch einen Widerstand.

:::abbildung et1/k4messwerk 1
Links das Messwerk: Die Spule dreht sich im Magnetfeld gegen eine Feder (nicht gezeichnet). Rechts die Ersatzbilder: ideales Instrument plus Innenwiderstand, in Reihe oder parallel.
:::

:::definition Definition 1.1 (Messbereich und Innenwiderstand)
<span class="anker" id="satz-1-1"></span>

Der Messbereich reicht bis zum __Bereichsendwert__, dem größten anzeigbaren Wert (beim Zeiger der Vollausschlag). Der Innenwiderstand $R_\mathrm i$ ist der Widerstand zwischen den Anschlüssen.

<ul>

<li>

Ein Amperemeter wird in Reihe geschaltet. Ideal ist $R_\mathrm i=0$, real etwa $R_\mathrm i\approx1\,\Omega$.

</li>

<li>

Ein Voltmeter wird parallel geschaltet. Ideal ist $R_\mathrm i\to\infty$, real etwa $R_\mathrm i\approx10\,\mathrm{M\Omega}$.

</li>

</ul>
:::

⁠**So liest man das:** Strom ist Ladung, die durch einen Querschnitt läuft. Deshalb trennt man den Stromkreis auf und schickt den ganzen Strom durch das Amperemeter. An ihm soll keine Spannung abfallen, also soll $R_\mathrm i$ klein sein. Spannung ist die Differenz zwischen zwei Punkten. Deshalb legt man das Voltmeter an beide Punkte, ohne den Kreis zu öffnen. Durch es soll kein Strom fließen, also soll $R_\mathrm i$ groß sein. Die Zahlenwerte sind typisch für Digitalmultimeter. **Gültigkeit:** $R_\mathrm i$ gilt für einen Messbereich und ändert sich beim Umschalten (Stufe [2](den-messbereich-erweitern.html#stufe-2)).

::::beispiel
Das Messwerk des Rechenmodells ist schon beides. Bei Vollausschlag fließen 50 µ A durch 2 k$\Omega$, also liegen $U_\mathrm M=R_\mathrm MI_\mathrm M=100$ mV an. Die Skala ließe sich mit 50 µ A oder mit 100 mV beschriften: zwei Namen für denselben Ausschlag.
::::

⁠**Grenzfall:** Für $R_\mathrm i=0$ wirkt das Amperemeter wie ein Stück Draht, für $R_\mathrm i\to\infty$ das Voltmeter wie eine offene Stelle. Ideale Instrumente sind für die Schaltung nicht vorhanden.

:::frage Wenn durch ein ideales Voltmeter kein Strom fließt, wie kann es dann etwas anzeigen?
Ein Zeiger könnte es nicht, denn ohne Strom gibt es keinen Ausschlag. Der ideale Fall ist eine Grenze, kein Gerät. Ein großer Innenwiderstand macht den Strom klein, nicht null. Digitale Geräte kommen mit sehr wenig Strom aus, weil die Energie für die Anzeige aus ihrer eigenen Batterie stammt, nicht aus der gemessenen Schaltung.
:::

:::aufgabe Aufgabe 1 ★ Falsch angeschlossen
<span class="anker" id="aufg-1"></span>

Sage zuerst vorher, welches Gerät in Gefahr ist. (a) Das Amperemeter des Rechenmodells liegt versehentlich direkt an der 9-V-Quelle. Welcher Strom fließt? (b) Das Voltmeter liegt versehentlich in Reihe mit $R$ an der Quelle. Was zeigt es an, welcher Strom fließt?

:::loesung
(a) In Gefahr ist das Amperemeter, denn sein kleiner Widerstand begrenzt den Strom kaum: $I=9\,\mathrm{V}/10\,\Omega=0{,}9$ A, das Neunzigfache des Bereichs. Durch das Messwerk fließen 4,5 mA statt 50 µ A, im Shunt werden 8,06 W frei.

(b) $I=9\,\mathrm{V}/201{,}8\,\mathrm{k\Omega}=44{,}6$ µ A. Das Voltmeter zeigt $44{,}6\,\mu\text{A}\cdot200\,\mathrm{k\Omega}=8{,}92$ V, an $R$ bleiben 80 mV. Nichts geht kaputt, aber die Schaltung arbeitet nicht mehr.
:::
:::

::::formelsammlung
**Amperemeter: in Reihe, kleiner Innenwiderstand**

$$R_\mathrm i=0\quad\text{(ideal)},\qquad R_\mathrm i\approx1\,\Omega\quad\text{(real)}$$

$R_\mathrm i$ ist der Widerstand zwischen den Anschlüssen. Der ganze Strom läuft durch das Gerät, an ihm soll keine Spannung abfallen. Für $R_\mathrm i=0$ wirkt es wie ein Stück Draht. Der reale Wert ist typisch für Digitalmultimeter; $R_\mathrm i$ gilt für einen Messbereich und ändert sich beim Umschalten.

**Voltmeter: parallel, großer Innenwiderstand**

$$R_\mathrm i\to\infty\quad\text{(ideal)},\qquad R_\mathrm i\approx10\,\mathrm{M\Omega}\quad\text{(real)}$$

Das Gerät liegt an beiden Punkten, ohne den Kreis zu öffnen; durch es soll kein Strom fließen. Für $R_\mathrm i\to\infty$ wirkt es wie eine offene Stelle. Ein großer Innenwiderstand macht den Strom klein, nicht null.

**Vollausschlag als Strom oder Spannung**

$$U_\mathrm M=R_\mathrm MI_\mathrm M$$

$I_\mathrm M$ Strom bei Vollausschlag, $R_\mathrm M$ Eigenwiderstand des Messwerks, $U_\mathrm M$ Spannung am Messwerk; mit 50 µ A und 2 k$\Omega$ sind es 100 mV. Die Skala ließe sich in beiden Größen beschriften: zwei Namen für denselben Ausschlag.
::::

::::lernkarten
:::karte begriff Innenwiderstand
Was versteht man unter dem Innenwiderstand $R_\mathrm i$ eines Messgeräts, und wofür gilt ein bestimmter Wert?
---
Den Widerstand zwischen den Anschlüssen des Geräts. Er entsteht, weil das Gerät zum Anzeigen Strom braucht, der durch einen Draht oder Widerstand fließt. Ein Wert gilt nur für einen Messbereich.
--- falsch
Den Widerstand des Bauteils, an dem gemessen wird: Das Gerät rechnet ihn aus Strom und Spannung heraus. Ein Wert gilt für die ganze Messung, gleich in welchem Messbereich man misst.
--- falsch
Den Widerstand gegen Ablesefehler, also ein Maß für die Genauigkeit der Anzeige in Prozent. Ein Wert gilt für das ganze Gerät und bleibt beim Umschalten des Bereichs gleich.
--- falsch
Den Widerstand zwischen den Anschlüssen, den nur Zeigerinstrumente haben. Digitalmultimeter haben keinen, weil sie aus ihrer eigenen Batterie versorgt werden und der gemessenen Schaltung deshalb keinen Strom entnehmen.
:::
:::karte begriff Messwerk
Was ist das Messwerk eines Zeigerinstruments, und wie ist es aufgebaut?
---
Der Teil des Geräts, der Strom in einen Zeigerausschlag umsetzt: eine drehbare Spule aus dünnem Draht zwischen den Polen eines Dauermagneten, die sich gegen eine Spiralfeder dreht.
--- falsch
Der Teil des Geräts, der Spannung ganz ohne Strom in einen Ausschlag umsetzt: zwei geladene Platten, zwischen denen sich ein leichter Zeiger im elektrischen Feld gegen eine Spiralfeder dreht.
--- falsch
Der Teil des Geräts, der den Messbereich umschaltet: ein Stufenschalter mit mehreren Widerständen, der je nach Stellung einen anderen Zeiger vor die Skala schiebt.
--- falsch
Der Teil des Geräts, der Strom in Wärme umsetzt: ein dünner Draht, der sich mit dem Strom erwärmt, dabei ausdehnt und so den Zeiger über die Skala schiebt.
:::
:::karte zusammenhang Ausschlag und Strom
Warum ist der Ausschlag eines Zeigerinstruments dem Strom durch seine Spule proportional?
---
Das Magnetfeld übt auf die bewegten Elektronen im Draht eine Kraft aus. Die Drehkraft wächst mit dem Strom, die Gegenkraft der Feder mit dem Winkel; die Spule bleibt dort stehen, wo beide gleich groß sind.
--- falsch
Die Spule erwärmt sich mit dem Strom und dehnt sich aus. Die Ausdehnung wächst mit dem Strom und schiebt den Zeiger weiter; die Feder holt ihn erst nach dem Abschalten zurück.
--- falsch
Die Drehkraft ist für jeden Strom gleich groß, nur die Zeit, in der sie wirkt, wächst mit dem Strom. Je länger sie wirkt, desto weiter dreht sich die Spule gegen die Feder, bis man den Strom abschaltet.
--- falsch
Der Strom verstärkt das Feld des Dauermagneten, und das stärkere Feld zieht den Zeiger mit wachsendem Strom immer stärker an. Die Feder ist nur dazu da, den Zeiger ohne Strom in der Nullstellung zu halten.
:::
:::karte zusammenhang Digitalmultimeter
Warum hat auch ein Digitalmultimeter (Gerät mit Zahlenanzeige) einen Innenwiderstand, obwohl es kein Messwerk mit Spule enthält?
---
Es wandelt die Spannung an einem internen Widerstand in eine Zahl um. Auch dort fließt Strom durch einen Widerstand, also ist es ebenfalls ein Bauteil mit einem Widerstand zwischen seinen Anschlüssen.
--- falsch
Es hat keinen: Ohne Spule fließt durch das Gerät kein Strom, es liest die Spannung nur ab. Der angegebene Widerstand ist allein der Widerstand seiner beiden Messleitungen.
--- falsch
Weil seine Batterie einen Widerstand hat, der in Reihe mit den Anschlüssen liegt. Ist die Batterie neu, ist er null; mit der Zeit wächst er, und das Gerät beginnt die Schaltung immer stärker zu stören.
--- falsch
Weil seine Ziffernanzeige ihre Energie aus der gemessenen Schaltung bezieht. Der Innenwiderstand ist der Widerstand der leuchtenden Ziffern und wechselt deshalb mit der angezeigten Zahl.
:::
:::karte begriff Messbereich und Bereichsendwert
Was geben der Messbereich und der Bereichsendwert eines Messgeräts an?
---
Der Messbereich ist der Wertebereich der Anzeige. Er reicht bis zum Bereichsendwert, dem größten anzeigbaren Wert; beim Zeigerinstrument ist das der Vollausschlag.
--- falsch
Der Messbereich ist der kleinste Wert, den das Gerät noch sicher anzeigt. Der Bereichsendwert ist der Wert, bei dem das Gerät zerstört wird, weit über dem Vollausschlag.
--- falsch
Der Messbereich ist die Genauigkeit der Anzeige in Prozent. Der Bereichsendwert ist der größte Fehler, den die Anzeige in diesem Bereich höchstens machen darf.
--- falsch
Der Messbereich ist der Wertebereich der Anzeige. Der Bereichsendwert ist der Wert in der Mitte der Skala, bei dem ein Zeigerinstrument am genauesten anzeigt.
:::
:::karte begriff Amperemeter
Was ist ein Amperemeter, wie schließt man es an, und warum soll sein Innenwiderstand klein sein?
---
Ein Strommesser, der in Reihe im Stromkreis liegt: Man trennt den Kreis auf und schickt den ganzen Strom hindurch. An ihm soll keine Spannung abfallen, also soll $R_\mathrm i$ klein sein; ideal ist $R_\mathrm i=0$, real etwa $R_\mathrm i\approx1\,\Omega$.
--- falsch
Ein Strommesser, der parallel zum Bauteil liegt, ohne den Kreis zu öffnen. Durch ihn soll dabei möglichst viel Strom fließen, damit der Zeiger weit ausschlägt, also soll $R_\mathrm i$ klein sein; ideal ist $R_\mathrm i=0$ wie bei einem Stück Draht.
--- falsch
Ein Strommesser, der in Reihe im aufgetrennten Kreis liegt. Er soll den Strom bremsen, damit dieser sich ablesen lässt, also soll $R_\mathrm i$ etwa so groß sein wie der Widerstand des Bauteils, an dem gemessen wird.
--- falsch
Ein Strommesser, der in Reihe im Stromkreis liegt. Durch ihn soll möglichst wenig Strom fließen, damit er nicht überlastet wird, also soll sein Innenwiderstand groß sein, ideal $R_\mathrm i\to\infty$.
:::
:::karte begriff Voltmeter
Was ist ein Voltmeter, wie schließt man es an, und warum soll sein Innenwiderstand groß sein?
---
Ein Spannungsmesser, der parallel liegt: Spannung ist die Differenz zwischen zwei Punkten, also legt man ihn an beide Punkte, ohne den Kreis zu öffnen. Durch ihn soll kein Strom fließen; ideal ist $R_\mathrm i\to\infty$, real etwa $R_\mathrm i\approx10\,\mathrm{M\Omega}$.
--- falsch
Ein Spannungsmesser, der in Reihe liegt: Man trennt den Kreis auf, damit die ganze Spannung an ihm liegt. An ihm soll möglichst viel Spannung abfallen, deshalb ist $R_\mathrm i$ groß, ideal $R_\mathrm i\to\infty$.
--- falsch
Ein Spannungsmesser, der parallel an beiden Punkten liegt. Er soll möglichst viel Strom aufnehmen, damit sein Zeiger weit ausschlägt; deshalb soll sein Innenwiderstand klein sein, ideal $R_\mathrm i=0$.
--- falsch
Ein Spannungsmesser, der parallel an beiden Punkten liegt. Sein großer Innenwiderstand schützt ihn vor zu hoher Spannung; für die Schaltung spielt er keine Rolle, weil das Gerät außerhalb des Stromkreises liegt und ihn nicht verändert.
:::
:::karte zusammenhang Ideale Instrumente
Wie wirken ein ideales Amperemeter und ein ideales Voltmeter auf die Schaltung, in der sie messen?
---
Gar nicht: Das ideale Amperemeter mit $R_\mathrm i=0$ wirkt wie ein Stück Draht, das ideale Voltmeter mit $R_\mathrm i\to\infty$ wie eine offene Stelle. Für die Schaltung sind beide nicht vorhanden.
--- falsch
Das ideale Amperemeter mit $R_\mathrm i=0$ wirkt wie eine offene Stelle, das ideale Voltmeter mit $R_\mathrm i\to\infty$ wie ein Stück Draht; beide trennen die Schaltung an ihrer Stelle in zwei Teile.
--- falsch
Sie wirken wie Widerstände von 1 $\Omega$ beziehungsweise 10 M$\Omega$. Diese Werte heißen ideal, weil sie die Schaltung so wenig stören, wie es ein Gerät überhaupt erlaubt.
--- falsch
Beide wirken wie ein Stück Draht zwischen ihren Anschlüssen. Für die Schaltung sind sie trotzdem nicht vorhanden, weil ideale Instrumente keine Energie verbrauchen.
:::
:::karte zusammenhang Anzeige fast ohne Strom
Wenn durch ein ideales Voltmeter kein Strom fließt, wie kann ein reales Voltmeter dann überhaupt etwas anzeigen?
---
Der ideale Fall ist eine Grenze, kein Gerät: Ein großer Innenwiderstand macht den Strom klein, nicht null. Digitale Geräte kommen mit sehr wenig Strom aus, weil die Energie für die Anzeige aus ihrer eigenen Batterie stammt.
--- falsch
Es misst das elektrische Feld zwischen den Anschlüssen, ohne dass Ladung fließt. Auch ein Zeiger schlägt deshalb ganz ohne Strom aus, solange zwischen den Anschlüssen eine Spannung liegt, ähnlich wie bei einem Kondensator.
--- falsch
Es zieht kurz einen großen Strom, liest dabei ab und sperrt danach wieder. Im Mittel fließt so kein Strom, und die Schaltung wird trotz des kurzen Stoßes überhaupt nicht verändert; so arbeiten Digitalmultimeter.
--- falsch
Es nimmt den Strom aus seiner eigenen Batterie und schickt ihn durch die Schaltung. Dieser Strom ersetzt den Strom, der durch das Gerät abfließt, sodass in der Schaltung insgesamt nichts fehlt.
:::
:::karte formel Spannung am Messwerk
Welche Spannung liegt bei Vollausschlag an einem Messwerk mit 50 µ A Vollausschlag und 2 k$\Omega$ Eigenwiderstand, und was folgt daraus für seine Skala?
---
$U_\mathrm M=R_\mathrm MI_\mathrm M=100$ mV. Die Skala ließe sich mit 50 µ A oder mit 100 mV beschriften: zwei Namen für denselben Ausschlag. Das Messwerk ist schon Amperemeter und Voltmeter zugleich.
--- falsch
$U_\mathrm M=I_\mathrm M/R_\mathrm M=25$ nV. Diese Spannung ist so klein, dass sich die Skala nur in Strom beschriften lässt; als Voltmeter taugt das Messwerk erst mit einem eigenen Spannungsteil.
--- falsch
$U_\mathrm M=R_\mathrm MI_\mathrm M=100$ mV, aber diese Spannung zeigt das Messwerk nicht an: Es reagiert nur auf Strom, und eine Beschriftung der Skala in Volt wäre deshalb falsch.
--- falsch
$U_\mathrm M=R_\mathrm MI_\mathrm M=100$ V. Die Skala ließe sich auch in Volt beschriften, aber nur bis 100 V; bei höheren Spannungen wird das Messwerk überlastet.
:::
:::karte zusammenhang Amperemeter an der Quelle
Was geschieht, wenn man ein Amperemeter mit 10 $\Omega$ Innenwiderstand und 10 mA Messbereich versehentlich direkt an eine 9-V-Quelle legt?
---
Sein kleiner Widerstand begrenzt den Strom kaum: Es fließen $I=9\,\mathrm{V}/10\,\Omega=0{,}9$ A, das Neunzigfache des Bereichs. In Gefahr ist das Amperemeter.
--- falsch
Fast nichts: Ein Amperemeter misst nur den Strom und lässt die Spannung durch. Es zeigt einen Strom knapp über dem Bereichsende an, die Quelle bleibt dabei unbelastet.
--- falsch
Es zeigt 9 V an, weil jedes Messgerät an einer Quelle deren Spannung anzeigt. Der Strom bleibt so klein wie bei einem Voltmeter, und nichts wird beschädigt.
--- falsch
Sein kleiner Widerstand begrenzt den Strom kaum, aber in Gefahr ist nur die Quelle: Am kleinen Widerstand des Geräts wird kaum Leistung umgesetzt, es hält jeden Strom aus.
:::
:::karte zusammenhang Voltmeter in Reihe
Was geschieht, wenn ein Voltmeter mit 200 k$\Omega$ Innenwiderstand versehentlich in Reihe mit 1,8 k$\Omega$ an einer 9-V-Quelle liegt?
---
Sein großer Widerstand begrenzt den Strom auf 44,6 µ A, fast die ganze Quellspannung liegt am Gerät: Es zeigt 8,92 V, am Widerstand bleiben 80 mV. Nichts geht kaputt, aber die Schaltung arbeitet nicht mehr.
--- falsch
Es zeigt die Spannung am Widerstand richtig an, weil in einer Reihenschaltung durch beide derselbe Strom fließt; der Fehler beträgt wie beim richtigen Anschluss nur wenige Prozent, je nach Innenwiderstand.
--- falsch
Es fließt ein großer Strom, weil sich die beiden Widerstände in Reihe gegenseitig aufheben; das Voltmeter brennt durch, bevor es überhaupt etwas anzeigen kann.
--- falsch
Es zeigt null an, weil durch ein Voltmeter grundsätzlich kein Strom fließen kann; die Schaltung arbeitet dagegen unverändert weiter, als wäre das Gerät gar nicht da, und die Quelle treibt weiter 5 mA.
:::
::::
