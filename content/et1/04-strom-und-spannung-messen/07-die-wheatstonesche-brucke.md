---
title: Stufe 6: Die Wheatstonesche Brücke
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom und Spannung messen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Kapitel 4: Strom und Spannung messen
order: 1140700
summary: R=U/I addiert die Fehler zweier Anzeigen.
tags: 
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
$R=U/I$ addiert die Fehler zweier Anzeigen. Im Rechenmodell sind das $\pm1{,}1\,\%$ bei der Spannung und $\pm2\,\%$ beim Strom, zusammen bis zu $\pm3{,}1\,\%$. Die Brücke braucht von ihrem Instrument nur eine Aussage: null oder nicht null.
:::

**Die Idee.** Zwei Spannungsteiler hängen an derselben Quelle (Abb. [8](#abb-8)). Ein empfindliches Instrument verbindet ihre Mittelpunkte. Teilen beide im selben Verhältnis, liegen die Mittelpunkte auf demselben Potenzial, zwischen ihnen besteht keine Spannung, und durch das Instrument fließt kein Strom. Man verstellt einen Widerstand, bis der Zeiger auf null steht: der Abgleich. Wenn kein Strom fließt, entnimmt das Instrument der Schaltung nichts. Sein Innenwiderstand wirkt nicht, und seine Skala wird nicht gebraucht.

:::abbildung et1/k4bruecke 8
Links das Prinzip. Rechts die praktische Ausführung: $R_1$ und $R_2$ sind die Teile eines Widerstandsdrahts, der Schleifkontakt legt ihr Verhältnis fest.
:::

:::satz Satz 6.1 (Abgleichbedingung)
<span class="anker" id="satz-6-1"></span>

Fließt durch das Instrument kein Strom, gilt

<span class="anker" id="gl-6-1"></span>
$$R_4=R_3\,\frac{R_2}{R_1}. \tag{6.1}$$
:::

⁠**So liest man das:** $R_3$ ist ein genau bekannter Referenzwiderstand. Von $R_1$ und $R_2$ zählt nur das einstellbare, bekannte Verhältnis, ihre Werte sind belanglos. $R_4$ ist gesucht. In der Gleichung fehlen $U_\mathrm q$ und der Innenwiderstand des Instruments. Schwankt die Quelle, verschieben sich beide Mittelpunkte gleich. **Gültigkeit:** exakt im Abgleich. Wie genau man ihn trifft, hängt davon ab, welche kleine Abweichung das Instrument noch zeigt.

:::herleitung Abgleich
Ohne Querstrom liefert die Knotenregel $I_1=I_2$ und $I_3=I_4$. Gleiche Potenziale der Mittelpunkte ergeben $U_{R2}=U_{R4}$ und $U_{R1}=U_{R3}$. Also ist

$$\frac{U_{R4}}{U_{R3}}=\frac{U_{R2}}{U_{R1}} \quad\Rightarrow\quad \frac{I_4R_4}{I_3R_3}=\frac{I_2R_2}{I_1R_1} \quad\Rightarrow\quad \frac{R_4}{R_3}=\frac{R_2}{R_1}.$$
:::

::::beispiel
Mit $R_2/R_1=1{,}8$ und $R_3=1$ k$\Omega$ steht der Zeiger bei $R_4=1800\,\Omega$ auf null, beide Mittelpunkte liegen auf 5,786 V. Sind $R_3$ und das Verhältnis auf je 0,1 % genau, ist $R_4$ auf $\pm0{,}2\,\%$ genau, mehr als 15-mal besser als $U/I$. Die Genauigkeit stammt nun aus Widerständen, und die lassen sich viel genauer fertigen als Zeigerskalen.
::::

⁠**Grenzfall:** Mit wachsendem $R_4$ läuft der rechte Mittelpunkt von 0 bis $U_\mathrm q$. Die Spannung am Instrument wechselt dabei genau einmal das Vorzeichen, es gibt also genau eine Abgleichstellung.

:::frage In der Brücke fließt doch Strom. Was genau ist null?
Nur der Strom im Querzweig. Durch beide Teiler fließen im Beispiel je 3,214 mA, die Quelle arbeitet normal.
:::

**Schleifdraht und Dekaden.** Im Schleifdraht (gleichmäßiger Widerstandsdraht mit verschiebbarem Kontakt, Länge $l$, Gesamtwiderstand $R_0$) ist bei der Kontaktstellung $x$ der untere Teil $R_2=R_0\,x/l$ und der obere $R_1=R_0\,(1-x/l)$. Daraus folgt $R_4=R_3\,x/(l-x)$, und $R_0$ fällt heraus. Für 1800 $\Omega$ bei $l=1$ m steht der Kontakt bei $x=642{,}9$ mm. Genauere Brücken stellen $R_3$ dekadisch ein: Stufenschalter mit je $9\times100\,\Omega$, $9\times10\,\Omega$, $9\times1\,\Omega$ und $9\times0{,}1\,\Omega$ liefern je eine Ziffer, $R_2/R_1$ ist ein in Zehnerpotenzen umschaltbarer Multiplikator. Mit dem Faktor 10 und der Schalterstellung 180,0 $\Omega$ ergeben sich 1800 $\Omega$ in Schritten von 1 $\Omega$. Als Nullanzeige taugt auch ein Voltmeter, denn im Abgleich sind die Spannungen an $R_2$ und $R_4$ gleich.

:::ltspice Der Abgleich hängt nicht vom Instrument ab
⁠**Zeichnen:** Quelle `voltage` mit 9 V am Netz `o`. `R1` = 1k von `o` nach `l`, `R2` = 1.8k von `l` nach Masse, `R3` = 1k von `o` nach `r`, `R4` = `{RX}` von `r` nach Masse. Das Messwerk ist `Rd` = 2k von `l` nach `r`.

⁠**Direktiven:** `.step param RX 1700 1900 10` und `.op`

⁠**Was du siehst:** Zeichne `I(Rd)` über `RX`: Die Kurve geht bei 1800 durch null, bei 1700 sind es $+36{,}4$ µ A, bei 1900 $-33{,}6$ µ A. Setze `Rd` auf 1 oder 1Meg: Die Kurve ändert ihre Höhe, der Nulldurchgang bleibt bei 1800. Bei 0,1 % Abweichung (1801,8 $\Omega$) fließen im Messwerk nur 0,63 µ A, also 1,3 % des Vollausschlags. Für Aufgabe [7](#aufg-7): Mit `R1` = 356.1 und `R2` = 643.9 (Kontakt 1 mm daneben) wandert der Nulldurchgang auf 1808 $\Omega$.
:::

:::aufgabe Aufgabe 7 ★★ Schleifdraht
<span class="anker" id="aufg-7"></span>

Der Draht ist 1 m lang, $R_3=1$ k$\Omega$. (a) Der Abgleich gelingt bei $x=642{,}9$ mm. Wie groß ist $R_4$? (b) Der Kontakt ist auf $\pm1$ mm ablesbar. Welcher Fehler von $R_4$ folgt daraus? (c) Wiederhole (b) für $R_3=1{,}8$ k$\Omega$ und $R_3=100\,\Omega$. Warum wählt man $R_3$ in der Größe von $R_4$?

:::loesung
(a) $R_4=1\,\mathrm{k\Omega}\cdot642{,}9/357{,}1=1800\,\Omega$. (b) Eine Verschiebung um $\Delta x$ ändert $x/(l-x)$ relativ um $\Delta x\,(1/x+1/(l-x))$. Das sind $1\,\mathrm{mm}\cdot(1/642{,}9+1/357{,}1)/\mathrm{mm}=\pm0{,}44\,\%$.

(c) $R_3=1{,}8$ k$\Omega$: $x=500$ mm, $\pm0{,}40\,\%$. $R_3=100\,\Omega$: $x=947{,}4$ mm, $\pm2{,}0\,\%$. Der Fehler ist am kleinsten, wenn der Kontakt in der Mitte steht, also bei $R_3\approx R_4$. Nahe dem Drahtende wiegt derselbe Millimeter relativ schwer.
:::
:::

::::formelsammlung
**Abgleichbedingung**

$$R_4=R_3\,\frac{R_2}{R_1}$$

Gilt, wenn durch das Instrument kein Strom fließt. $R_3$ ist ein genau bekannter Referenzwiderstand, von $R_1$ und $R_2$ zählt nur das einstellbare, bekannte Verhältnis, $R_4$ ist gesucht. $U_\mathrm q$ und der Innenwiderstand des Instruments kommen nicht vor. Exakt im Abgleich; wie genau man ihn trifft, hängt von der kleinsten Abweichung ab, die das Instrument noch zeigt.

**Schleifdraht**

$$R_2=R_0\,x/l,\qquad R_1=R_0\,(1-x/l),\qquad R_4=R_3\,x/(l-x)$$

Gleichmäßiger Widerstandsdraht der Länge $l$ mit dem Gesamtwiderstand $R_0$, $x$ Stellung des Kontakts; $R_0$ fällt heraus.

**Ablesefehler am Schleifdraht**

$$\Delta x\,(1/x+1/(l-x))$$

Relative Änderung von $x/(l-x)$ und damit von $R_4$, wenn der Kontakt um $\Delta x$ verschoben ist. Am kleinsten steht der Kontakt in der Mitte, also für $R_3\approx R_4$; nahe dem Drahtende wiegt derselbe Millimeter relativ schwer.
::::

::::lernkarten
:::karte begriff Wheatstonesche Messbrücke
Wie ist die Wheatstonesche Messbrücke aufgebaut, und wozu dient sie?
---
Eine Schaltung zum Vergleich von Widerständen: Zwei Spannungsteiler hängen an derselben Quelle, ein empfindliches Instrument verbindet ihre Mittelpunkte. Der gesuchte Widerstand wird über ein bekanntes Verhältnis mit einem Referenzwiderstand verglichen.
--- falsch
Eine Schaltung zum Messen von Spannungen: Zwei Spannungsteiler hängen in Reihe an der Quelle, das Instrument liegt parallel zur Quelle. Sie misst die Quellspannung besonders genau, indem sie sie in vier gleiche Teile zerlegt und jeden Teil einzeln anzeigt.
--- falsch
Eine Schaltung zum Vergleich von Widerständen: Vier Widerstände liegen in Reihe an einer Quelle, ein Instrument misst den Strom durch die Kette, einmal vor und einmal nach dem Austausch eines Widerstands.
--- falsch
Eine Schaltung zum Vergleich von Widerständen: Zwei Spannungsteiler hängen an derselben Quelle, das Instrument liegt in Reihe mit der Quelle. Es misst den Gesamtstrom, aus dem man mit $R=U/I$ den gesuchten Widerstand bestimmt.
:::
:::karte begriff Abgleich
Was versteht man unter dem Abgleich einer Wheatstoneschen Brücke, und was gilt dann für das Instrument?
---
Den Zustand, in dem das Instrument null anzeigt; man verstellt dazu einen Widerstand. Dann teilen beide Spannungsteiler im selben Verhältnis, die Mittelpunkte liegen auf demselben Potenzial, und durch das Instrument fließt kein Strom.
--- falsch
Den Zustand, in dem das Instrument seinen Vollausschlag zeigt; man verstellt dazu die Quellspannung. Dann ist die Brücke am empfindlichsten, und durch das Instrument fließt der größte Strom, den die Schaltung liefern kann.
--- falsch
Das Eichen des Instruments vor der Messung mit einem bekannten Widerstand. Danach zeigt es den gesuchten Widerstand direkt an, und sein Innenwiderstand ist bereits herausgerechnet.
--- falsch
Den Zustand, in dem das Instrument null anzeigt; man verstellt dazu einen Widerstand. Dann führen beide Teiler keinen Strom mehr, die Quelle ist entlastet, und an allen vier Widerständen liegt keine Spannung mehr an.
:::
:::karte formel Abgleichbedingung
Welche Bedingung gilt im Abgleich der Brücke, und welche Rolle spielen dabei $R_1$, $R_2$ und $R_3$?
---
$R_4=R_3\,\frac{R_2}{R_1}$: $R_3$ ist ein genau bekannter Referenzwiderstand, von $R_1$ und $R_2$ zählt nur das einstellbare, bekannte Verhältnis, ihre Werte sind belanglos. $R_4$ ist gesucht.
--- falsch
$R_4=R_3\,\frac{R_1}{R_2}$: $R_3$ ist der Referenzwiderstand, $R_1$ und $R_2$ müssen einzeln genau bekannt sein, weil ihre Werte und nicht nur ihr Verhältnis in die Bedingung eingehen.
--- falsch
$R_4=R_1+R_2-R_3$: Im Abgleich sind die Widerstände beider Zweige gleich groß; $R_1$, $R_2$ und $R_3$ müssen deshalb einzeln genau bekannt sein, damit die Summe stimmt.
--- falsch
$R_4=R_3\,\frac{R_2}{R_1}$, aber nur bei der Quellspannung, mit der die Brücke geeicht wurde: Schwankt $U_\mathrm q$, verschiebt sich der Abgleich, und $R_3$ muss nachgestellt werden.
:::
:::karte herleitung Abgleichbedingung
Leite die Abgleichbedingung $R_4=R_3R_2/R_1$ her, ausgehend davon, dass durch das Instrument kein Strom fließt.
---
Ohne Querstrom liefert die Knotenregel $I_1=I_2$ und $I_3=I_4$, weil an den Mittelpunkten kein Strom abzweigt.
---
Gleiche Potenziale der Mittelpunkte ergeben $U_{R2}=U_{R4}$ und $U_{R1}=U_{R3}$, weil beide Teiler an derselben Quelle hängen und zwischen den Mittelpunkten keine Spannung besteht.
---
Also ist $\frac{U_{R4}}{U_{R3}}=\frac{U_{R2}}{U_{R1}}$ und mit dem ohmschen Gesetz $\frac{I_4R_4}{I_3R_3}=\frac{I_2R_2}{I_1R_1}$, weil an jedem Widerstand die Spannung gleich Strom mal Widerstand ist.
---
Es bleibt $\frac{R_4}{R_3}=\frac{R_2}{R_1}$, weil sich wegen $I_3=I_4$ und $I_1=I_2$ die Ströme herauskürzen.
:::
:::karte zusammenhang Unabhängig von Instrument und Quelle
Warum hängt das Ergebnis des Abgleichs weder vom Innenwiderstand des Instruments noch von seiner Skala noch von der Quellspannung ab?
---
Im Abgleich fließt durch das Instrument kein Strom, es entnimmt der Schaltung nichts; von ihm wird nur die Aussage null oder nicht null gebraucht. Schwankt die Quelle, verschieben sich beide Mittelpunkte gleich.
--- falsch
Weil Innenwiderstand, Skala und Quellspannung vor jeder Messung gemeinsam geeicht werden; ihre Fehler heben sich deshalb heraus, solange die letzte Eichung nicht zu lange zurückliegt und die Temperatur gleich bleibt.
--- falsch
Weil das Instrument in der Brücke nur sehr kleine Ströme führt; sein Innenwiderstand und die Quelle wirken deshalb nur schwach, aber in genau bekannter Weise, die man herausrechnet.
--- falsch
Die Quellspannung geht sehr wohl ein, nur der Innenwiderstand nicht: Steigt $U_\mathrm q$, verschiebt sich der Mittelpunkt mit dem größeren Widerstand stärker, und der Abgleich wandert.
:::
:::karte zusammenhang Was im Abgleich null ist
In der abgeglichenen Brücke fließt doch Strom. Was genau ist im Abgleich null?
---
Nur der Strom im Querzweig zwischen den Mittelpunkten. Durch beide Teiler fließt weiter Strom, im Beispiel je 3,214 mA; die Quelle arbeitet normal.
--- falsch
Der Strom aus der Quelle: Im Abgleich heben sich die Ströme beider Teiler auf, sodass die Quelle nichts mehr liefert und nirgends Energie umgesetzt wird.
--- falsch
Die Spannung an allen vier Widerständen: Im Abgleich liegt die ganze Quellspannung am Instrument, und die vier Widerstände sind spannungslos.
--- falsch
Der Strom durch $R_4$: Im Abgleich fließt der ganze Strom des rechten Teilers über das Instrument in den linken, und $R_4$ bleibt stromlos.
:::
:::karte zusammenhang Genauigkeit der Brücke
Warum bestimmt die Brücke einen Widerstand genauer als die Rechnung $R=U/I$ aus zwei Anzeigen?
---
$R=U/I$ addiert die Fehler zweier Anzeigen, im Beispiel bis zu $\pm3{,}1\,\%$. Die Brücke braucht vom Instrument nur die Aussage null oder nicht null; die Genauigkeit stammt aus Widerständen, und die lassen sich viel genauer fertigen als Zeigerskalen.
--- falsch
Weil die Brücke mit vier Widerständen misst, deren Fehler sich gegenseitig ausgleichen; je mehr Bauteile an einer Messung beteiligt sind, desto kleiner wird nach dieser Regel der Gesamtfehler, bei vier Teilen etwa auf ein Viertel.
--- falsch
Weil das Instrument der Brücke eine feinere Skala hat: Es zeigt den Widerstand direkt in Ohm an, sodass die fehleranfällige Umrechnung aus Strom und Spannung ganz entfällt.
--- falsch
Weil die Brücke mit einer höheren Quellspannung arbeitet: Der Anzeigefehler bleibt in Volt gleich, ist aber im Verhältnis zur größeren Spannung kleiner, und das Ergebnis wird im selben Maß genauer, wie die Spannung steigt.
:::
:::karte formel Schleifdraht
Wie bestimmt man $R_4$ mit einem Schleifdraht (gleichmäßiger Widerstandsdraht der Länge $l$ mit verschiebbarem Kontakt), wenn der Abgleich bei der Kontaktstellung $x$ gelingt?
---
Der untere Teil ist $R_2=R_0\,x/l$, der obere $R_1=R_0\,(1-x/l)$ mit dem Gesamtwiderstand $R_0$. Daraus folgt $R_4=R_3\,x/(l-x)$; $R_0$ fällt heraus.
--- falsch
Der untere Teil ist $R_2=R_0\,x/l$, der obere $R_1=R_0\,(1-x/l)$. Daraus folgt $R_4=R_3\,x/l$; der Gesamtwiderstand $R_0$ muss dazu genau bekannt sein.
--- falsch
Aus der Stellung folgt direkt $R_4=R_0\,x/l$; $R_3$ wird beim Schleifdraht nicht gebraucht, weil der Draht selbst den Vergleichswiderstand bildet.
--- falsch
Daraus folgt $R_4=R_3\,(l-x)/x$: Je weiter der Kontakt zum Drahtende $x=l$ wandert, desto kleiner ist der gesuchte Widerstand; $R_0$ fällt heraus.
:::
:::karte zusammenhang Kontakt in der Mitte
Warum wählt man beim Schleifdraht den Referenzwiderstand $R_3$ etwa so groß wie den gesuchten Widerstand $R_4$?
---
Dann steht der Kontakt nahe der Mitte, und der Ablesefehler ist am kleinsten: Eine Verschiebung um $\Delta x$ ändert $R_4$ relativ um $\Delta x\,(1/x+1/(l-x))$. Nahe dem Drahtende wiegt derselbe Millimeter relativ schwer.
--- falsch
Damit durch beide Zweige derselbe Strom fließt; sonst erwärmt sich der Zweig mit dem kleineren Widerstand stärker, und der Abgleich wandert mit der Temperatur langsam weg, während man noch abliest.
--- falsch
Damit der Kontakt nahe am Drahtende steht; dort ist der Draht am gleichmäßigsten, und ein Millimeter Ablesefehler wirkt sich auf das Ergebnis am wenigsten aus.
--- falsch
Weil die Brücke sonst keinen Abgleich hat: Nur bei $R_3=R_4$ wechselt die Spannung am Instrument ihr Vorzeichen, bei allen anderen Werten bleibt sie positiv.
:::
:::karte zusammenhang Dekadische Brücke
Wie stellen genauere Brücken den Referenzwiderstand $R_3$ und das Verhältnis $R_2/R_1$ ein?
---
$R_3$ wird dekadisch eingestellt: Stufenschalter mit je $9\times100\,\Omega$, $9\times10\,\Omega$, $9\times1\,\Omega$ und $9\times0{,}1\,\Omega$ liefern je eine Ziffer. $R_2/R_1$ ist ein in Zehnerpotenzen umschaltbarer Multiplikator.
--- falsch
$R_3$ ist ein Drehwiderstand mit stufenloser Skala, $R_2/R_1$ ein zweiter, dessen Stellung man ebenfalls an einer Skala abliest; aus beiden Skalen ergibt sich $R_4$ durch Multiplizieren.
--- falsch
$R_3$ bleibt fest bei 1 k$\Omega$, nur $R_2/R_1$ wird in Schritten von 0,1 umgeschaltet; feinere Werte zeigt das Instrument als kleinen Restausschlag an, den man abliest.
--- falsch
Man tauscht $R_3$ von Hand gegen andere Normwiderstände, bis der Zeiger null zeigt; $R_1$ und $R_2$ sind fest und gleich groß, ihr Verhältnis ist also immer eins.
:::
:::karte zusammenhang Genau eine Abgleichstellung
Warum gibt es bei der Brücke genau eine Stellung von $R_4$, bei der das Instrument null zeigt?
---
Mit wachsendem $R_4$ läuft der rechte Mittelpunkt von 0 bis $U_\mathrm q$. Die Spannung am Instrument wechselt dabei genau einmal das Vorzeichen.
--- falsch
Weil das Instrument nur in eine Richtung ausschlagen kann: Ist $R_4$ zu groß, bleibt der Zeiger am Anschlag, und ein zweiter Nulldurchgang ist nicht möglich.
--- falsch
Es gibt zwei Stellungen, eine kleine und eine große; man nimmt diejenige, bei der der Zeiger langsamer durch null geht, weil sie die genauere ist.
--- falsch
Weil der Strom durch $R_4$ mit wachsendem Widerstand erst steigt und dann fällt; beim Höchstwert dieses Stroms zeigt das Instrument null.
:::
:::karte zusammenhang Wie genau der Abgleich gelingt
Wovon hängt ab, wie genau man den Abgleich einer Brücke trifft?
---
Davon, welche kleine Abweichung das Instrument noch zeigt. Mit dem Messwerk aus 2 k$\Omega$ als Nullanzeige fließen bei 0,1 % Abweichung von $R_4$ nur 0,63 µ A, also 1,3 % des Vollausschlags.
--- falsch
Von der Teilung der Skala: Je feiner die Skala geteilt ist, desto genauer liest man den Wert ab, bei dem die Brücke abgeglichen ist, gleich wie stark der Zeiger reagiert.
--- falsch
Allein vom Innenwiderstand des Instruments: Nur ein Instrument mit $R_\mathrm i=0$ zeigt den Abgleich genau an, jedes andere verschiebt die Nullstellung.
--- falsch
Von der Dauer der Messung: Je länger man wartet, desto genauer stellt sich der Zeiger auf null ein, weil sich die Brücke mit der Zeit selbst abgleicht.
:::
::::
