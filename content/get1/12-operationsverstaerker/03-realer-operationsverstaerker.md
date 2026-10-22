---
title: Der reale Operationsverstärker
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Operationsverstärker
order: 120700
summary: Wie sich ein realer OPV vom idealen unterscheidet und was die Abweichungen in einer gegengekoppelten Schaltung bewirken: endliche Verstärkung, Aussteuergrenzen, Offsetspannung, Eingangsruheströme, Gleichtaktunterdrückung, Bandbreite und Anstiegsgeschwindigkeit. Kompakte Fassung; die ausführliche enthält zusätzlich Ein- und Ausgangswiderstand unter Gegenkopplung, die Ausgangsstufe, die Betriebsspannungsunterdrückung im Einzelnen, die Herkunft der endlichen Gleichtaktunterdrückung und das Überschwingen des Spannungsfolgers.
tags: realer OPV, Verstärkungs-Bandbreite-Produkt, Transitfrequenz, Slew Rate, Offsetspannung, Eingangsruhestrom, CMRR
stil: 3
fassung: kompakt
---

## Worum es geht

Die goldenen Regeln setzen einen OPV voraus, der unendlich verstärkt, keinen Eingangsstrom aufnimmt und beliebig schnell ist. Ein realer OPV wie der verbreitete 741 erfüllt keine dieser Annahmen, und doch stimmen die Grundschaltungen meist auf Promille. Wann sie nicht mehr stimmen, folgt aus einem Prinzip:

**Ein realer OPV ist ein idealer mit kleinen Fehlerquellen: Fehler im Verstärker teilt die Gegenkopplung durch die Schleifenverstärkung, Fehler an den Eingängen verstärkt sie wie ein Signal; weil die Schleifenverstärkung mit der Frequenz fällt, wirkt die Gegenkopplung nur bis zu einer Grenzfrequenz, und große Signale begrenzen zusätzlich Aussteuerbereich und Anstiegsgeschwindigkeit.**

Vorausgesetzt werden Rückkopplungsfaktor und Schleifenverstärkung aus [Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html) und die Schaltungen aus [Die OPV-Grundschaltungen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/opv-grundschaltungen.html). Das Skript behandelt den realen OPV in Abschnitt 12.7 (S. 212); Ruheströme, Bandbreite und Anstiegsgeschwindigkeit sind nach dem Datenblatt ergänzt.

:::grafik
Szene: get1/operationsverstaerker/03-ersatzschaltbild · Vorlage: schaltplan
**Abbildung 1:** Ersatzschaltbild des Beispiel-OPV (Art 741 an ±15 V). In der Mitte ein OPV mit der endlichen Leerlaufverstärkung $v_D$ = 200 000, die oberhalb von 5 Hz mit der Frequenz fällt, und der Anstiegsgrenze 0,5 V/µs. Außen die übrigen Abweichungen als Bauteile: vor dem Pluseingang eine Spannungsquelle von 1 mV (Offsetspannung), an jedem Eingang eine Stromquelle von 80 nA in den OPV hinein (Eingangsruheströme), zwischen den Eingängen 2 MΩ (Eingangswiderstand), in Reihe zum Ausgang 75 Ω (Ausgangswiderstand). Daneben die Grenzen: Ausgang ±14 V, Eingänge ±13 V, Gleichtaktunterdrückung 95 dB. Links umrandet die Quellen an den Eingängen, rechts die Abweichungen im Verstärker. Wo eine Abweichung sitzt, entscheidet, was die Gegenkopplung mit ihr macht.
:::

## Was am realen OPV anders ist

*Worin weicht ein realer OPV vom idealen ab, und warum wirken die Abweichungen so verschieden?*

Das Skript schlägt vor, reale Einflüsse wie die endliche Verstärkung zum idealen OPV hinzuzufügen (S. 198); in der Praxis hängt man jede Abweichung als kleine Quelle oder als Widerstand an, wie in Abbildung 1. Die Offsetspannung ist eine kleine Fehlspannung zwischen den Eingängen, der Ruhestrom fließt ständig in jeden Eingang, der Offsetstrom ist der Unterschied der beiden, und die Gleichtaktunterdrückung sagt, wie schwach eine gemeinsame Spannung beider Eingänge wirkt. Die Werte stammen aus den Datenblättern des LM741 und, für Ausgangswiderstand und Transitfrequenz, des µA741:

| Eigen­schaft | idealer OPV | Beispiel-OPV: typisch; garantiert |
|---|---|---|
| Leerlauf­verstärkung $v_D$ | unendlich | 200 000; mindestens 50 000 |
| Verstärkung bei hohen Frequen­zen | unverändert | ab 5 Hz fallend, bei 1 MHz gleich 1 |
| Anstiegs­geschwindig­keit | unbegrenzt | 0,5 V/µs |
| Ausgangs­bereich an ±15 V | ±15 V | ±14 V an 10 kΩ, ±13 V an 2 kΩ |
| Offset­spannung | 0 | 1 mV; höchstens 5 mV |
| Ruhe­strom, Offset­strom | 0 | 80 nA und 20 nA; höchstens 500 nA und 200 nA |
| Gleichtakt­unter­drückung | unendlich | 95 dB; mindestens 80 dB |
| Eingangs-, Ausgangs­widerstand | unendlich, 0 | 2 MΩ, 75 Ω |

Entscheidend ist, wo eine Abweichung sitzt. Die endliche Leerlaufverstärkung und der Ausgangswiderstand wirken im Verstärker selbst: Sie verschieben den Ausgang, die Rückführung meldet die Verschiebung an den Minuseingang, und der OPV regelt sie bis auf einen kleinen Rest aus. Offsetspannung, Ruheströme und Gleichtakteinfluss wirken dagegen an den Eingängen wie eine zusätzliche Eingangsspannung. Die kann der OPV vom Signal nicht unterscheiden, und er verstärkt sie mit. Die goldenen Regeln gelten deshalb weiter, solange die Schleifenverstärkung groß ist und kein Signal an eine Grenze stößt; die Abweichungen rechnet man einzeln aus und überlagert sie.

Dazu kommen Grenzen großer Signale. Zwischen dem Ausgang und jeder Versorgung liegen Transistoren der Ausgangsstufe, an denen Spannung abfällt (Skript S. 199): Der Ausgang bleibt an ±15 V typisch bei ±14 V, mit 2 kΩ Last bei ±13 V, und mehr als seinen Kurzschlussstrom von typisch 25 mA liefert er nicht. Die Eingänge müssen zwischen −12 V und +12 V bleiben, typisch reicht es bis ±13 V; sonst arbeitet die Eingangsstufe nicht mehr richtig.

## Endliche Leerlaufverstärkung

*Um wie viel weicht die Verstärkung einer Schaltung vom Widerstandsverhältnis ab?*

**Die Akteure:**

- __$k$__: Rückkopplungsfaktor, der Anteil der Ausgangsspannung, der bei $U_E$ = 0 über den Teiler aus $R_2$ und $R_1$ am Minuseingang ankommt, beim nichtinvertierenden wie beim invertierenden Verstärker:

$$k = \frac{R_1}{R_1 + R_2}$$

- __$k\,v_D$__: Schleifenverstärkung ([Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html), Abschnitt *Der Ruhezustand*); mit $k$ = 0,1 und dem Beispiel-OPV 20 000.
- __$A_\mathrm{ideal}$__: Verstärkung mit idealem OPV, beim nichtinvertierenden Verstärker $1/k$, beim invertierenden $-R_2/R_1$.

**Das Zusammenspiel:** Für den Ausgang $U_A$ braucht der OPV zwischen seinen Eingängen die Differenzspannung $U_A/v_D$, bei 2 V und 200 000 also 10 µV. Der Ausgang bleibt deshalb gerade so weit hinter dem Wert zurück, den die Widerstände verlangen, dass diese Differenz entsteht. Wie weit, bestimmt die Schleifenverstärkung: Eine Abweichung des Ausgangs kommt mit dem Faktor $k$ am Minuseingang an und wird $v_D$-fach verstärkt.

:::formel Formel
$$A = \frac{A_\mathrm{ideal}}{1 + \dfrac{1}{k\,v_D}}$$
$$\frac{A_\mathrm{ideal} - A}{A_\mathrm{ideal}} = \frac{1}{1 + k\,v_D}$$
:::

**So liest man das:** Der relative Fehler ist praktisch der Kehrwert der Schleifenverstärkung und wächst mit der gewünschten Verstärkung: Mit dem Beispiel-OPV sind es bei $1/k$ = 10 0,005 %, bei 101 0,05 %, bei 1001 0,5 %. Schwankungen von $v_D$ gehen nur mit demselben Bruchteil ein. Ebenso regelt die Gegenkopplung den Spannungsabfall am Ausgangswiderstand aus; mit $k$ = 0,1 wirken die 75 Ω wie 3,75 mΩ.

Idee der Herleitung: Man setzt das Potential des Minuseingangs, das der Teiler aus Eingangs- und Ausgangsspannung bildet, in die Gleichung des OPV ein und löst nach $U_A$ auf.

:::herleitung
**Ausgangspunkt:** die Gleichung des OPV im linearen Bereich, $U_A = v_D U_D$ ([Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung-ausfuehrlich.html), Abschnitt *Der ideale Operationsverstärker*), und das Überlagerungsprinzip für den Spannungsteiler ([Das Superpositionsverfahren](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/superpositionsverfahren.html)); für den nichtinvertierenden Verstärker das Ergebnis aus *Der Ruhezustand* im selben Artikel.

**Annahmen:** (i) In die Eingänge fließt kein Strom; der Teiler ist unbelastet. (ii) Der Ausgang liegt nicht an einer Grenze. (iii) Gleichspannung oder langsame Änderungen, so dass $v_D$ = 200 000 gilt.

**Schritt 1**: Invertierender Verstärker: Der Minuseingang liegt am Teiler zwischen $U_E$ (über $R_1$) und $U_A$ (über $R_2$). Nach dem Überlagerungsprinzip ist sein Potential die Summe der Beiträge beider Spannungen:

$$U_{e-} = \frac{R_2}{R_1 + R_2}\,U_E + \frac{R_1}{R_1 + R_2}\,U_A = (1 - k)\,U_E + k\,U_A$$

**Schritt 2**: Der Pluseingang liegt an Masse, also ist $U_D = -U_{e-}$. In die Gleichung des OPV eingesetzt:

$$U_A = -v_D\,\big((1 - k)\,U_E + k\,U_A\big)$$

**Schritt 3** (entscheidender Schritt): $U_A$ steht auf beiden Seiten; Ordnen ergibt:

$$U_A\,(1 + k\,v_D) = -v_D\,(1 - k)\,U_E$$

**Schritt 4**: Der Faktor vor $U_E$ lässt sich durch das Widerstandsverhältnis ausdrücken:

$$\frac{1 - k}{k} = \frac{R_2/(R_1 + R_2)}{R_1/(R_1 + R_2)} = \frac{R_2}{R_1}$$

Damit, nach Erweitern mit $k$:

$$A = \frac{U_A}{U_E} = -\frac{R_2}{R_1}\cdot\frac{k\,v_D}{1 + k\,v_D}$$

**Schritt 5**: Nichtinvertierender Verstärker: Dort gilt nach *Der Ruhezustand*

$$A = \frac{v_D}{1 + k\,v_D} = \frac{1}{k}\cdot\frac{k\,v_D}{1 + k\,v_D}$$

**Ergebnis:** In beiden Fällen ist der Faktor hinter $A_\mathrm{ideal}$ derselbe:

$$A = \frac{A_\mathrm{ideal}}{1 + \dfrac{1}{k\,v_D}}$$

$$\frac{A_\mathrm{ideal} - A}{A_\mathrm{ideal}} = 1 - \frac{k\,v_D}{1 + k\,v_D} = \frac{1}{1 + k\,v_D}$$

**Woher die Faktoren kommen:** Die 1 im Nenner von $1 + k v_D$ stammt aus der Differenzspannung, die der OPV selbst für seinen Ausgang braucht; $k v_D$ aus der Rückführung, die den Ausgang nachregelt.

**Proben:** Einheitenlos. Grenzfall $v_D$ gegen unendlich: $A = A_\mathrm{ideal}$. Zahlenwert für $R_1$ = 10 kΩ, $R_2$ = 20 kΩ: $k$ = 1/3, $k v_D$ = 66 667, $A$ = −1,99997 wie in [Die OPV-Grundschaltungen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/opv-grundschaltungen.html).

**Grenzen:** Für Wechselspannungen ist $v_D$ kleiner, bei 5 Hz schon 141 000, und der OPV verschiebt den Ausgang zeitlich; dann gilt der Abschnitt *Frequenzgang und Verstärkungs-Bandbreite-Produkt*. Liegt der Ausgang an einer Grenze, gilt die Gleichung des OPV nicht.
:::

::::beispiel Verstärkungsfehler eines invertierenden Verstärkers mit A = −100
**Gegeben:** $R_1$ = 1 kΩ, $R_2$ = 100 kΩ; Beispiel-OPV mit $v_D$ = 200 000 (typisch) bzw. 50 000 (garantiert).

**Gesucht:** die Verstärkung mit beiden Werten von $v_D$.

**Rechnung:** Rückkopplungsfaktor und Schleifenverstärkung:

$$k = \frac{1\ \mathrm{k}\Omega}{101\ \mathrm{k}\Omega} = 0{,}00990$$

$$k\,v_D = 1980$$

$$A = \frac{-100}{1 + 1/1980} = -99{,}95$$

Mit 50 000 ist $k v_D$ = 495:

$$A = \frac{-100}{1 + 1/495} = -99{,}80$$

**Ergebnis:** **$A$ = −99,95 bzw. −99,80, ein Fehler von 0,05 % bzw. 0,2 %.**

**Einordnung:** Der Rückgang von $v_D$ um 75 % ändert $A$ nur um 0,15 %. Widerstände mit 1 % Toleranz verfälschen $R_2/R_1$ um bis zu 2 %; die Genauigkeit bestimmen hier die Widerstände.
::::

## Offsetspannung

*Warum liefert ein OPV ohne Eingangssignal eine Ausgangsspannung, und mit welchem Faktor erscheint dieser Fehler am Ausgang?*

:::grafik
Szene: get1/operationsverstaerker/03-offset · Vorlage: schaltung-und-kennlinie
**Abbildung 2:** (a) Ursache: Kollektorstrom über der Basis-Emitter-Spannung nach der Transfergleichung für zwei Transistoren derselben Bauart, $I_C$ logarithmisch von 1 µA bis 10 mA, $U_{BE}$ von 0,45 V bis 0,75 V; der Beispieltransistor ($I_S$ = 10⁻¹⁴ A) und ein zweiter mit 4 % größerem $I_S$ ergeben zwei parallele Geraden, waagrecht um 1,01 mV gegeneinander verschoben, was im ganzen Diagramm nicht zu sehen ist; eine Lupe um 0,5 mA mit $U_{BE}$ von 0,634 V bis 0,640 V zeigt den Abstand. (b) Wirkung: invertierender Verstärker mit $R_1$ = 10 kΩ und $R_2$ = 20 kΩ, Eingang auf 0 V gelegt, die Offsetspannung als Quelle von 1 mV vor dem Pluseingang; beide Eingänge des inneren OPV auf 1 mV, 0,1 µA durch $R_1$ und $R_2$, Ausgang 3 mV. Daneben dieselbe Schaltung umgezeichnet: Für die Offsetquelle ist sie ein nichtinvertierender Verstärker mit $1 + R_2/R_1$ = 3. Die Offsetspannung wird mit der Rauschverstärkung verstärkt, nicht mit der Signalverstärkung.
:::

**Die Akteure:**

- __$U_{os}$__: __Offsetspannung__, die Differenzspannung, die man zwischen die Eingänge legen muss, damit der Ausgang null wird (Skript S. 212); beim Beispiel-OPV typisch 1 mV, höchstens 5 mV, mit zufälligem Vorzeichen. Im Ersatzschaltbild ist sie eine Spannungsquelle vor dem Pluseingang; die außen angelegte Spannung, die den Ausgang auf null bringt, ist gleich groß und hebt sie gerade auf.
- __$1/k$__: __Rauschverstärkung__ (englisch noise gain), der Faktor, mit dem eine Spannung am Pluseingang am Ausgang erscheint, gleich $1 + R_2/R_1$, mit 10 kΩ und 20 kΩ also 3; auch das Eigenrauschen des OPV wird mit ihr verstärkt.
- __$U_{A,os}$__: der Anteil der Ausgangsspannung, den die Offsetspannung verursacht.

**Das Zusammenspiel:** Die beiden Hälften der Eingangsstufe sind nie genau gleich; das Skript spricht von „Mismatching“. Haben die Eingangstransistoren um 4 % verschiedene Sättigungsströme $I_S$, braucht der eine nach der Transfergleichung ([Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html)) für denselben Strom 1,01 mV mehr Basis-Emitter-Spannung (Abbildung 2a).

**Das Zusammenspiel in Schritten** (invertierender Verstärker mit $R_1$ = 10 kΩ und $R_2$ = 20 kΩ, Eingang auf 0 V gelegt, Abbildung 2b):

**Schritt 1**: Die Offsetquelle liegt zwischen Masse und dem Pluseingang des inneren, idealen OPV; dieser Eingang liegt auf 1 mV.

**Schritt 2**: Die Gegenkopplung hält den Minuseingang ebenfalls auf 1 mV.

**Schritt 3**: Weil der Eingang $U_E$ auf 0 V liegt, fließen durch $R_1$ 0,1 µA vom Minuseingang zur Eingangsquelle.

**Schritt 4**: Dieser Strom kommt über $R_2$ vom Ausgang; an $R_2$ fallen 2 mV ab, und der Ausgang liegt bei 3 mV.

**Schritt 5**: Für die Offsetquelle ist die Schaltung also ein nichtinvertierender Verstärker: Sie wird mit der Rauschverstärkung $1 + R_2/R_1$ = 3 verstärkt, nicht mit −2.

:::formel Formel
$$U_{A,os} = \Big(1 + \frac{R_2}{R_1}\Big)\,U_{os} = \frac{U_{os}}{k}$$
:::

**So liest man das:** Die Offsetspannung erscheint mit der Rauschverstärkung am Ausgang, gleich, an welchem Eingang das Signal liegt. Beim nichtinvertierenden Verstärker ist das die Verstärkung, beim invertierenden ihr Betrag plus 1: Mit $A$ = −100 werden aus 1 mV 101 mV.

Idee der Herleitung: Man setzt nach dem Überlagerungsprinzip das Signal null und berechnet die Schaltung allein mit der Offsetquelle.

:::herleitung
**Ausgangspunkt:** das Überlagerungsprinzip für lineare Netze ([Das Superpositionsverfahren](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/superpositionsverfahren.html)) und die Verstärkung des nichtinvertierenden Verstärkers, hergeleitet in [Die OPV-Grundschaltungen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/opv-grundschaltungen.html), Abschnitt *Der nichtinvertierende Verstärker und der Impedanzwandler*.

**Annahmen:** (i) Der reale OPV ist ein idealer mit der Offsetquelle $U_{os}$ vor dem Pluseingang (Ersatzschaltbild, Abbildung 1). (ii) Die übrigen Abweichungen werden getrennt betrachtet. (iii) Der Ausgang liegt nicht an einer Grenze.

**Schritt 1**: Überlagerung: Die Signalquelle $U_E$ wird null gesetzt, also durch einen Kurzschluss ersetzt. Beim invertierenden Verstärker liegt $R_1$ dann zwischen Minuseingang und Masse, beim nichtinvertierenden ohnehin.

**Schritt 2** (entscheidender Schritt): Was übrig bleibt, ist in beiden Fällen ein nichtinvertierender Verstärker mit dem Eingang $U_{os}$ am Pluseingang des inneren OPV:

$$U_{A,os} = \Big(1 + \frac{R_2}{R_1}\Big)\,U_{os}$$

**Schritt 3**: Mit $k = R_1/(R_1 + R_2)$ ist der Faktor der Kehrwert von $k$:

$$1 + \frac{R_2}{R_1} = \frac{R_1 + R_2}{R_1} = \frac{1}{k}$$

**Schritt 4**: Der Beitrag addiert sich zu dem des Signals:

$$U_A = A\,U_E + \frac{U_{os}}{k}$$

**Ergebnis:**

$$U_{A,os} = \Big(1 + \frac{R_2}{R_1}\Big)\,U_{os} = \frac{U_{os}}{k}$$

**Woher die Faktoren kommen:** Die 1 steht für die Offsetspannung selbst, die über den virtuellen Kurzschluss am Minuseingang wieder erscheint; $R_2/R_1$ für den Spannungsabfall an $R_2$, den der Strom $U_{os}/R_1$ verursacht.

**Proben:** Einheit V. Zahlenwerte: 10 kΩ und 20 kΩ ergeben 3 mV, 1 kΩ und 100 kΩ 101 mV. Grenzfall Spannungsfolger, $R_2$ = 0: Die Offsetspannung erscheint unverändert am Ausgang.

**Grenzen:** Die Rechnung gilt für Gleichspannung. Die Offsetspannung selbst ändert sich mit Temperatur, Versorgungsspannung und Lebensdauer (Frage unten).
:::

::::beispiel Offsetfehler eines Thermoelement-Verstärkers
**Gegeben:** Thermoelement Typ K mit 4,096 mV bei 100 °C gegen die Vergleichsstelle bei 0 °C (Normtabelle), im Mittel 40,96 µV/K; nichtinvertierender Verstärker mit $R_1$ = 1 kΩ und $R_2$ = 100 kΩ; Beispiel-OPV mit $U_{os}$ = 1 mV (typisch) bzw. 5 mV (höchstens).

**Gesucht:** die Ausgangsspannung bei 100 °C und der Messfehler durch die Offsetspannung in Kelvin.

**Rechnung:** Verstärkung und Rauschverstärkung sind hier gleich, 101:

$$U_A = 101\cdot 4{,}096\ \mathrm{mV} = 413{,}7\ \mathrm{mV}$$

$$U_{A,os} = 101\cdot 1\ \mathrm{mV} = 101\ \mathrm{mV}$$

Weil Signal und Offset gleich verstärkt werden, genügt der Vergleich am Eingang:

$$\frac{1\ \mathrm{mV}}{40{,}96\ \mu\mathrm{V/K}} = 24{,}4\ \mathrm{K}$$

**Ergebnis:** **Der Ausgang zeigt bei 0 °C schon 101 mV, als wäre die Messstelle 24 K wärmer, bei umgekehrtem Vorzeichen des Offsets entsprechend kälter; mit 5 mV wären es 122 K.**

**Einordnung:** Der Verstärkungsfehler aus der endlichen Leerlaufverstärkung macht bei 100 °C nur 0,05 K aus. Für kleine Gleichspannungen ist die Offsetspannung der wichtigste Fehler eines OPV.
::::

:::fehlvorstellung
„Der Umkehrer hat die Verstärkung −1; seine Offsetspannung wird deshalb nicht verstärkt.“ Das liegt nahe, weil man im invertierenden Verstärker jede Spannung mit $-R_2/R_1$ verrechnet. Die Offsetspannung liegt aber vor dem Pluseingang, und für sie ist die Schaltung ein nichtinvertierender Verstärker (Schritt 5). Beim Umkehrer mit zweimal 10 kΩ erscheint 1 mV Offset als 2 mV am Ausgang.
:::

:::frage
„Warum ändert sich die Offsetspannung mit der Temperatur?“
Ein Offset aus ungleichen Sättigungsströmen ist die Temperaturspannung $U_T$ mal dem Logarithmus des Stromverhältnisses. Das Verhältnis hängt nicht von der Temperatur ab, $U_T$ aber wächst proportional zur absoluten Temperatur; 1 mV bei 300 K wächst deshalb um 3,3 µV/K. Beim Thermoelement-Verstärker verschiebt das die Anzeige um 0,8 K je 10 K Erwärmung der Elektronik. Dazu hängt der Offset von der Versorgungsspannung ab und ändert sich langsam über die Lebensdauer (Skript S. 212).
:::

:::frage
„Lässt sich die Offsetspannung nicht abgleichen?“
Für eine Temperatur ja: Der 741 hat zwei Anschlüsse (1 und 5), über die ein Potentiometer die Stromaufteilung in der Eingangsstufe verschiebt, laut Datenblatt im Bereich von ±15 mV, angegeben für ±20 V Versorgung. Die Temperaturdrift bleibt im Allgemeinen. Wo kleine Gleichspannungen zählen, nimmt man Präzisions-OPVs mit Offsetspannungen im Mikrovoltbereich, etwa mit eingebautem, ständig wiederholtem Nullabgleich (Chopper- oder Auto-Zero-Verstärker).
:::

## Eingangsruheströme

*Warum fließt in die Eingänge eines OPV Strom, und was bewirkt er an den Widerständen der Schaltung?*

:::grafik
Szene: get1/operationsverstaerker/03-ruhestroeme · Vorlage: schaltung-strompfade
**Abbildung 3:** Invertierender Verstärker mit $R_1$ = 100 kΩ und $R_2$ = 1 MΩ, Eingang auf 0 V gelegt, Ruheströme von je 80 nA in beide Eingänge (Strompfeile). (a) Pluseingang direkt an Masse: Beide Eingänge auf 0 V, durch $R_1$ kein Strom, der Ruhestrom des Minuseingangs kommt ganz über $R_2$ vom Ausgang, der Ausgang liegt auf 80 mV. (b) Mit $R_3$ = 90,9 kΩ zwischen Pluseingang und Masse: Pluseingang und Minuseingang auf −7,27 mV, durch $R_1$ fließen 72,7 nA aus Masse zu, durch $R_2$ nur noch 7,27 nA, der Ausgang liegt auf 0 V; mit 20 nA Unterschied der Ruheströme wären es ±20 mV. Gleiche Ströme an gleichen Widerständen heben sich auf; übrig bleibt der Unterschied der Ströme.
:::

**Die Akteure:**

- __$I_{B+}$__, __$I_{B-}$__: Ruheströme in den Plus- und in den Minuseingang, je rund 80 nA, in den OPV hinein.
- __$I_B$__, __$I_{os}$__: __Eingangsruhestrom__, der Mittelwert beider, und __Offsetstrom__, der Betrag ihres Unterschieds; typisch 80 nA und 20 nA.
- __$R_3$__: Widerstand zwischen Pluseingang und Masse, der die Wirkung der Ruheströme ausgleicht.
- __$U_{A,B}$__: der Anteil der Ausgangsspannung, den die Ruheströme verursachen.

**Das Zusammenspiel:** Die Eingänge des 741 sind die Basisanschlüsse seiner Eingangstransistoren, und jeder braucht einen Basisstrom: rund 10 µA Kollektorstrom durch eine Stromverstärkung um 125, also 80 nA. Dieser Strom fließt immer, auch ohne Differenzspannung. Mit dem Eingangswiderstand von 2 MΩ hat er nichts zu tun; der beschreibt nur, wie sich der Strom mit der Differenzspannung ändert, bei 25 µV um 12,5 pA.

Wirksam wird der Ruhestrom an den Widerständen (Abbildung 3). Liegt der Pluseingang an Masse, hält die Gegenkopplung auch den Minuseingang auf 0 V; durch $R_1$ fließt nichts, und $I_{B-}$ muss ganz über $R_2$ vom Ausgang kommen: 1 MΩ mal 80 nA ergibt 80 mV. Ein Widerstand $R_3$ zwischen Pluseingang und Masse senkt dessen Potential durch $I_{B+}$ auf −7,27 mV, und der Minuseingang folgt. Nun fließen 72,7 nA aus Masse durch $R_1$ zu, und den Rest von $I_{B-}$ liefert der Ausgang über $R_2$, ohne von 0 V abzuweichen. Das gelingt, wenn $R_3$ gleich der Parallelschaltung von $R_1$ und $R_2$ ist; übrig bleibt der Offsetstrom mal $R_2$, 20 mV statt 80 mV.

:::formel Formel
$$U_{A,B} = R_2\,I_{B-} - \Big(1 + \frac{R_2}{R_1}\Big)\,R_3\,I_{B+}$$
$$R_3 = \frac{R_1\,R_2}{R_1 + R_2}$$
$$U_{A,B} = R_2\,(I_{B-} - I_{B+})$$
:::

**So liest man das:** Die erste Zeile gilt für jedes $R_3$, auch für null; ohne Ausgleich wächst der Fehler mit dem Rückkopplungswiderstand, nicht mit der Verstärkung. Mit dem Ausgleichswiderstand der zweiten Zeile bleibt nur der Offsetstrom mal $R_2$. Für Megaohm-Widerstände nimmt man OPVs mit Feldeffekttransistoren am Eingang, deren Ruheströme Pikoampere betragen.

Idee der Herleitung: Man setzt Signal und Offsetspannung null und stellt die Knotenregel am Minuseingang auf, dessen Potential die Gegenkopplung dem Pluseingang nachführt.

:::herleitung
**Ausgangspunkt:** die Knotenregel, das Ohmsche Gesetz und die erste goldene Regel für den inneren, idealen OPV.

**Annahmen:** (i) Die Ruheströme sind Stromquellen, die in die Eingänge hinein fließen (Ersatzschaltbild, Abbildung 1). (ii) Signal und Offsetspannung sind nach dem Überlagerungsprinzip null gesetzt; $R_1$ liegt damit zwischen Minuseingang und Masse. (iii) Die Gegenkopplung hält die Differenzspannung des inneren OPV auf null.

**Schritt 1**: Pluseingang: Durch $R_3$ fließt $I_{B+}$ von Masse zum Eingang; dessen Potential liegt um den Spannungsabfall darunter:

$$U_{e+} = -R_3\,I_{B+}$$

**Schritt 2**: Wegen der Gegenkopplung liegt der Minuseingang ebenso:

$$U_{e-} = U_{e+}$$

**Schritt 3** (entscheidender Schritt): Knotenregel am Minuseingang: Was über $R_1$ aus Masse und über $R_2$ vom Ausgang zufließt, fließt als $I_{B-}$ in den OPV:

$$\frac{0 - U_{e-}}{R_1} + \frac{U_{A,B} - U_{e-}}{R_2} = I_{B-}$$

**Schritt 4**: Mit $R_2$ multipliziert und nach $U_{A,B}$ aufgelöst:

$$U_{A,B} = R_2\,I_{B-} + \Big(1 + \frac{R_2}{R_1}\Big)\,U_{e-}$$

**Schritt 5**: $U_{e-}$ aus den Schritten 1 und 2 eingesetzt:

$$U_{A,B} = R_2\,I_{B-} - \Big(1 + \frac{R_2}{R_1}\Big)\,R_3\,I_{B+}$$

**Schritt 6**: Mit $R_3$ gleich der Parallelschaltung wird der Faktor vor $I_{B+}$ genau $R_2$:

$$\Big(1 + \frac{R_2}{R_1}\Big)\,\frac{R_1\,R_2}{R_1 + R_2} = \frac{R_1 + R_2}{R_1}\cdot\frac{R_1\,R_2}{R_1 + R_2} = R_2$$

**Ergebnis:**

$$U_{A,B} = R_2\,I_{B-} - \Big(1 + \frac{R_2}{R_1}\Big)\,R_3\,I_{B+}$$

$$U_{A,B} = R_2\,(I_{B-} - I_{B+})$$

**Woher die Faktoren kommen:** $R_2$ vor $I_{B-}$, weil dieser Strom bei festgehaltenem Minuseingang durch $R_2$ fließen muss; $1 + R_2/R_1$ vor dem Spannungsabfall an $R_3$, weil diese Spannung am Pluseingang wie eine Offsetspannung mit der Rauschverstärkung erscheint.

**Proben:** Einheit Ω·A = V. Zahlenwerte für 100 kΩ und 1 MΩ: ohne $R_3$ 80 mV; mit 90,9 kΩ und gleichen Strömen 0; mit 90 nA in den Plus- und 70 nA in den Minuseingang −20 mV. Grenzfall $R_2$ = 0: Ohne Rückkopplungswiderstand verursacht $I_{B-}$ keine Spannung.

**Grenzen:** Beim nichtinvertierenden Verstärker gilt dieselbe Rechnung; $R_3$ ist dort der Innenwiderstand der Quelle am Pluseingang, den man gegebenenfalls ergänzt. OPVs, die ihre Ruheströme intern ausgleichen, haben Offsetströme in der Größe der Ruheströme selbst; bei ihnen nützt $R_3$ nichts. $R_3$ trägt zudem eigenes Rauschen bei, das man mit einem parallelen Kondensator verringert.
:::

## Gleichtakt- und Betriebsspannungsunterdrückung

*Wie stark wirkt eine Spannung, die beide Eingänge gemeinsam haben, auf den Ausgang, und wann spielt das eine Rolle?*

:::grafik
Szene: get1/operationsverstaerker/03-gleichtakt · Vorlage: schaltung-zustaende
**Abbildung 4:** (a) Spannungsfolger mit 10 V am Eingang: Beide Eingänge liegen auf 10 V, die Gleichtaktspannung ist 10 V; mit 95 dB wirkt sie wie eine Differenzspannung von 0,18 mV, und der Ausgang weicht um 0,18 mV von 10 V ab. (b) Invertierender Verstärker: Beide Eingänge liegen auf 0 V, gleich welches Signal anliegt; es entsteht kein Gleichtaktfehler. (c) Skala der Gleichtaktunterdrückung von 60 dB bis 120 dB mit den zugehörigen Verhältnissen 10³ bis 10⁶; markiert 95 dB (Beispiel-OPV typisch, 56 000), 80 dB (garantiert, 10 000) und 61 dB (Subtrahierer mit 1 % Widerstandsabweichung aus den Grundschaltungen). Eine Gleichtaktspannung wirkt wie eine kleine Differenzspannung, aber nur, wo die Eingänge mit dem Signal mitlaufen.
:::

**Die Akteure:**

- __$U_{Gl}$__: Gleichtaktspannung, der Mittelwert der beiden Eingangsspannungen ([Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html), Abschnitt *Der Differenzverstärker*).
- __$v_{Gl}$__: __Gleichtaktverstärkung__, die Änderung der Ausgangsspannung je Volt Gleichtaktspannung ohne Rückkopplung; beim Beispiel-OPV dem Betrag nach 3,6.
- __$\mathrm{CMRR}$__: __Gleichtaktunterdrückung__ (englisch common mode rejection ratio); beim Beispiel-OPV 56 000 oder 95 dB, garantiert 10 000 oder 80 dB.

:::formel Definition
$$\mathrm{CMRR} = \left|\frac{v_D}{v_{Gl}}\right|$$
$$\mathrm{CMRR}_\mathrm{dB} = 20\,\lg\left|\frac{v_D}{v_{Gl}}\right|$$
:::

Das Verhältnis gibt an, wie viel schwächer eine Gleichtaktspannung wirkt als eine gleich große Differenzspannung; in Dezibel rechnet man mit 20 lg wie beim Signal-Rausch-Verhältnis. Das Skript nennt für die Praxis 60 dB bis 120 dB mit b = 10⁻³ bzw. 10⁻⁴ (S. 212); gemeint ist offenbar der Kehrwert $|v_{Gl}/v_D|$, und zu 120 dB gehört 10⁻⁶. Mit der „Instabilität der Eingangsspannung im Gleichtaktbetrieb“ meint es eine Spannung, die an beiden Eingängen gleich anliegt.

**Das Zusammenspiel:** Am Ausgang addieren sich die verstärkte Differenz- und die verstärkte Gleichtaktspannung. Ob das zählt, hängt davon ab, wo die Eingänge liegen (Abbildung 4): Beim invertierenden Verstärker liegen beide auf 0 V. Beim Spannungsfolger und beim nichtinvertierenden Verstärker laufen sie mit dem Signal mit; 10 V am Folger wirken beim Beispiel-OPV wie 0,18 mV Differenz.

:::formel Formel
$$U_A = v_D\,\Big(U_D \pm \frac{U_{Gl}}{\mathrm{CMRR}}\Big)$$
:::

**So liest man das:** Eine Gleichtaktspannung verschiebt den Ausgang, als läge zwischen den Eingängen zusätzlich eine Spannung vom Betrag $U_{Gl}/\mathrm{CMRR}$, mit vom Exemplar abhängigem Vorzeichen, und die Gegenkopplung gibt sie mit der Rauschverstärkung weiter; je größer die Unterdrückung, desto kleiner dieser Beitrag. Weil $U_{Gl}$ am nichtinvertierenden Verstärker mit dem Signal wächst, wirkt der Fehler dort wie ein kleiner Verstärkungsfehler.

Idee der Herleitung: Man schreibt die Ausgangsspannung als Summe aus Differenz- und Gleichtaktwirkung und klammert die Differenzverstärkung aus.

:::herleitung
**Ausgangspunkt:** die Definitionen der Differenzverstärkung $v_D$, der Gleichtaktverstärkung $v_{Gl}$ und der Gleichtaktunterdrückung.

**Annahmen:** (i) Der OPV arbeitet im linearen Bereich. (ii) Die Wirkungen von Differenz- und Gleichtaktspannung überlagern sich ungestört.

**Schritt 1**: Ausgangsspannung als Summe beider Wirkungen:

$$U_A = v_D\,U_D + v_{Gl}\,U_{Gl}$$

**Schritt 2** (entscheidender Schritt): Die Gleichtaktverstärkung durch die Unterdrückung ausgedrückt; ihr Vorzeichen hängt vom Exemplar ab:

$$|v_{Gl}| = \frac{v_D}{\mathrm{CMRR}}$$

**Schritt 3**: Eingesetzt und $v_D$ ausgeklammert:

$$U_A = v_D\,U_D \pm \frac{v_D}{\mathrm{CMRR}}\,U_{Gl} = v_D\,\Big(U_D \pm \frac{U_{Gl}}{\mathrm{CMRR}}\Big)$$

**Ergebnis:**

$$U_A = v_D\,\Big(U_D \pm \frac{U_{Gl}}{\mathrm{CMRR}}\Big)$$

**Woher die Faktoren kommen:** $U_{Gl}/\mathrm{CMRR}$ ist der Betrag der Differenzspannung, die am Ausgang dasselbe bewirken würde wie die Gleichtaktspannung.

**Proben:** Einheit V. Grenzfall unendliche Unterdrückung: Es bleibt $U_A = v_D U_D$. Zahlenwert: 10 V durch 56 234 ergeben 0,178 mV.

**Grenzen:** Die Unterdrückung nimmt mit der Frequenz ab; die Datenblattwerte gelten für Gleichspannung und tiefe Frequenzen.
:::

Ähnlich wirkt eine Änderung der Versorgungsspannung, die laut Skript die Offsetspannung verschiebt (S. 212): beim Beispiel-OPV um 16 µV je Volt, die __Betriebsspannungsunterdrückung__ von 96 dB.

## Frequenzgang und Verstärkungs-Bandbreite-Produkt

*Bis zu welcher Frequenz hält eine gegengekoppelte Schaltung ihre Verstärkung, und warum hängt diese Grenze von der Verstärkung ab?*

:::grafik
Szene: get1/operationsverstaerker/03-frequenzgang · Vorlage: kennlinie-loglog
**Abbildung 5:** Verstärkung über der Frequenz von 1 Hz bis 10 MHz, beide Achsen logarithmisch. Die Leerlaufverstärkung des Beispiel-OPV liegt bei tiefen Frequenzen bei 200 000, ist bei der Eckfrequenz 5 Hz auf das 0,707-fache gefallen und fällt darüber um den Faktor 10 je Dekade, durch 1000 bei 1 kHz und 1 bei 1 MHz. Dazu die Verstärkung gegengekoppelter Schaltungen mit der Rauschverstärkung 1, 10, 100 und 1000: waagrecht, bis sie die fallende Gerade bei 1 MHz, 100 kHz, 10 kHz und 1 kHz erreichen, dann mit ihr fallend; an jeder Ecke das 0,707-fache markiert. Der senkrechte Abstand zwischen der Kurve des OPV und der Schaltung ist die Schleifenverstärkung, beschriftet für die Rauschverstärkung 10 bei 1 kHz: 100. Wo der Abstand verschwindet, endet die Bandbreite.
:::

**Die Akteure:**

- __$f$__: Frequenz eines sinusförmigen Signals; in Hz.
- __$v_D(f)$__: Leerlaufverstärkung bei der Frequenz $f$, das Verhältnis der Amplituden von Ausgangs- und Differenzspannung; bei tiefen Frequenzen 200 000, bei der Eckfrequenz 5 Hz 141 000, weit darüber $f_T/f$.
- __$f_T$__: Transitfrequenz, bei der die Leerlaufverstärkung auf 1 gefallen ist; 1 MHz ([Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html), Abschnitt *Warum die Schaltung zur Ruhe kommt*).
- __$\hat U_E$__, __$\hat U_A$__: Amplituden der Eingangs- und der Ausgangsspannung.
- __$f_g$__: __Grenzfrequenz__ der Schaltung, bei der ihre Verstärkung auf das 0,707-fache gefallen ist, um 3 dB.

**Das Zusammenspiel in Schritten** (nichtinvertierender Verstärker mit der Rauschverstärkung 10, Abbildung 5):

**Schritt 1**: Für Wechselspannungen verhält sich der OPV wie ein Integrator: Sein Ausgang ändert sich mit $\omega_T = 2\pi f_T$ mal der Differenzspannung, und für einen Sinus der Frequenz $f$ ist die Ausgangsamplitude das $f_T/f$-fache der Differenzamplitude. Ab 5 Hz fällt die Leerlaufverstärkung deshalb um den Faktor 10 je Dekade.

**Schritt 2**: Mit ihr fällt die Schleifenverstärkung $k\,v_D(f)$, bei 1 kHz auf 100, bei 10 kHz auf 10; in Abbildung 5 ist sie der Abstand der beiden Kurven. Solange sie groß ist, verstärkt die Schaltung mit $1/k$.

**Schritt 3**: Bei der Frequenz $k f_T$, hier 100 kHz, ist sie 1: Die Differenzspannung, die der OPV braucht, ist so groß wie das zurückgeführte Signal. Weil der integrierende OPV seinen Ausgang um eine Viertelperiode verschiebt, addieren sich die beiden Amplituden wie die Seiten eines rechtwinkligen Dreiecks; die Verstärkung ist auf das 0,707-fache gefallen.

**Schritt 4**: Darüber folgt die Schaltung der Leerlaufverstärkung $f_T/f$; mehr als der OPV allein kann sie nicht verstärken.

:::formel Formel
$$f_g = k\,f_T$$
$$\hat U_A = \frac{\hat U_E/k}{\sqrt{1 + (f/f_g)^2}}$$
:::

**So liest man das:** Die Bandbreite ist Rückkopplungsfaktor mal Transitfrequenz; beim nichtinvertierenden Verstärker ist $1/k$ die Verstärkung, und Verstärkung mal Bandbreite ergibt $f_T$, das __Verstärkungs-Bandbreite-Produkt__. Mit dem Beispiel-OPV reicht die Rauschverstärkung 10 bis 100 kHz, 101 bis 9,9 kHz, der Umkehrer mit −1 bis 500 kHz. Beim invertierenden Verstärker steht in der zweiten Zeile $R_2/R_1$ statt $1/k$ vor dem Bruch.

Idee der Herleitung: Man setzt einen sinusförmigen Ausgang in das Integratormodell des OPV ein und fasst den Sinus- und den Kosinusanteil der Eingangsspannung zu einer Amplitude zusammen.

:::herleitung
**Ausgangspunkt:** das Modell des OPV, nach dem sich sein Ausgang mit $\omega_T$ mal der Differenzspannung ändert, hergeleitet in [Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html), Abschnitt *Warum die Schaltung zur Ruhe kommt*, und die Masche des nichtinvertierenden Verstärkers.

**Annahmen:** (i) Die Eingangsspannung ist sinusförmig mit der Kreisfrequenz $\omega = 2\pi f$, und die Schaltung ist eingeschwungen. (ii) $f$ liegt weit über 5 Hz, so dass das Integratormodell gilt. (iii) Die Amplitude ist so klein, dass die Anstiegsgeschwindigkeit nicht begrenzt (Abschnitt *Anstiegsgeschwindigkeit und Leistungsbandbreite*).

**Schritt 1**: Modell und Masche, die zeitabhängigen Größen mit kleinen Buchstaben:

$$\frac{du_A}{dt} = \omega_T\,u_D$$

$$u_D = u_E - k\,u_A$$

Zusammen:

$$\frac{du_A}{dt} = \omega_T\,(u_E - k\,u_A)$$

**Schritt 2**: Ansatz für den Ausgang, ein Sinus mit noch unbekannter Amplitude und Verschiebung $\varphi$, und seine Ableitung:

$$u_A = \hat U_A\,\sin(\omega t - \varphi)$$

$$\frac{du_A}{dt} = \omega\,\hat U_A\,\cos(\omega t - \varphi)$$

**Schritt 3**: Die Gleichung aus Schritt 1 nach $u_E$ aufgelöst und eingesetzt:

$$u_E = \frac{1}{\omega_T}\,\frac{du_A}{dt} + k\,u_A$$

$$u_E = \frac{\omega}{\omega_T}\,\hat U_A\cos(\omega t - \varphi) + k\,\hat U_A\sin(\omega t - \varphi)$$

**Schritt 4** (entscheidender Schritt): Ein Kosinus und ein Sinus derselben Frequenz ergeben zusammen wieder einen Sinus. Nach dem Additionstheorem zerlegt man einen Sinus mit der Amplitude $R$ und der Verschiebung $\psi$, mit der Abkürzung $x$ für $\omega t - \varphi$:

$$R\,\sin(x + \psi) = R\cos\psi\,\sin x + R\sin\psi\,\cos x$$

Der Vergleich mit Schritt 3 legt die beiden Faktoren fest:

$$R\cos\psi = k\,\hat U_A$$

$$R\sin\psi = \frac{\omega}{\omega_T}\,\hat U_A$$

Quadriert und addiert, weil die Summe der Quadrate von Kosinus und Sinus 1 ist; $R$ ist die Amplitude der Eingangsspannung:

$$\hat U_E = R = \hat U_A\,\sqrt{k^2 + (\omega/\omega_T)^2}$$

**Schritt 5**: Nach $\hat U_A$ aufgelöst und $k$ aus der Wurzel gezogen; dabei ist $\omega/(k\omega_T)$ gleich $f/(k f_T)$:

$$\hat U_A = \frac{\hat U_E/k}{\sqrt{1 + \big(f/(k f_T)\big)^2}}$$

**Ergebnis:**

$$f_g = k\,f_T$$

$$\hat U_A = \frac{\hat U_E/k}{\sqrt{1 + (f/f_g)^2}}$$

**Woher die Faktoren kommen:** Der Kosinusanteil ist die Differenzspannung, die der integrierende OPV für seinen Ausgang braucht, der Sinusanteil das zurückgeführte Signal; gleich groß sind beide bei $f = k f_T$, und dort ergibt die Wurzel √2.

**Proben:** Einheitenlos. Grenzfall tiefe Frequenzen: $1/k$. Bei der Grenzfrequenz das 0,707-fache. Zahlenwert: Rauschverstärkung 10 bei 20 kHz ergibt 10 durch √1,04, also 9,81. Zeitbereich: Die Zeitkonstante des Einschwingens aus *Warum die Schaltung zur Ruhe kommt*, der Kehrwert von $k\,\omega_T$, ist 1,59 µs, und 1 durch 2π mal 1,59 µs ergibt wieder 100 kHz. Beim invertierenden Verstärker steht in der Masche vor $u_E$ der Faktor $-(1 - k)$ statt 1; die Grenzfrequenz bleibt $k f_T$.

**Grenzen:** Für große Amplituden begrenzt die Anstiegsgeschwindigkeit; in der Nähe von $f_T$ wirken weitere Verzögerungen im OPV, die das Modell nicht enthält und die beim Spannungsfolger ein leichtes Überschwingen erzeugen.
:::

::::beispiel Verstärker mit dem Betrag 100 für Signale bis 20 kHz
**Gegeben:** Beispiel-OPV mit $f_T$ = 1 MHz; (a) eine invertierende Stufe mit $R_1$ = 1 kΩ und $R_2$ = 100 kΩ; (b) zwei invertierende Stufen mit je 10 kΩ und 100 kΩ hintereinander.

**Gesucht:** Grenzfrequenz und Betrag der Verstärkung bei 20 kHz.

**Rechnung:** (a) Rauschverstärkung 101:

$$f_g = \frac{1\ \mathrm{MHz}}{101} = 9{,}90\ \mathrm{kHz}$$

$$|A| = \frac{100}{\sqrt{1 + (20/9{,}90)^2}} = 44{,}4$$

(b) Je Stufe Rauschverstärkung 11:

$$f_g = \frac{1\ \mathrm{MHz}}{11} = 90{,}9\ \mathrm{kHz}$$

$$|A| = \Big(\frac{10}{\sqrt{1 + (20/90{,}9)^2}}\Big)^2 = 95{,}4$$

Zusammen fallen beide Stufen bei 58,5 kHz auf das 0,707-fache.

**Ergebnis:** **Einstufig bleibt bei 20 kHz der Betrag 44,4, zweistufig 95,4.**

**Einordnung:** Jede der beiden Stufen braucht nur ein Zehntel der Verstärkung und hat gut die neunfache Bandbreite; das Vorzeichen kehrt sich zweimal um, die Gesamtverstärkung ist +100.
::::

:::fehlvorstellung
„Der 741 hat eine Transitfrequenz von 1 MHz, also verstärkt er Signale bis 1 MHz.“ Das liegt nahe, weil Datenblätter die Transitfrequenz als Bandbreite angeben. Bei 1 MHz ist seine Verstärkung aber schon auf 1 gefallen; nur ein Spannungsfolger reicht so weit. Mit der Rauschverstärkung 101 endet die Schaltung bei 9,9 kHz, mitten im Hörbereich.
:::

## Anstiegsgeschwindigkeit und Leistungsbandbreite

*Warum verzerrt ein Verstärker große Signale schon bei Frequenzen, die er klein noch sauber überträgt?*

:::grafik
Szene: get1/operationsverstaerker/03-anstieg · Vorlage: zeitverlauf
**Abbildung 6:** Zeitverläufe am nichtinvertierenden Verstärker mit der Rauschverstärkung 10 ($R_1$ = 10 kΩ, $R_2$ = 90 kΩ, Beispiel-OPV), je zwei Perioden. (a) Eingang 0,05 V bei 20 kHz: Ausgang ein Sinus mit 0,49 V Amplitude, gestrichelt der verlangte mit 0,5 V. (b) Eingang 1 V bei 5 kHz: Ausgang ein Sinus mit 9,99 V, größte Steigung 0,31 V/µs, unter der Grenze. (c) Eingang 1 V bei 20 kHz: Verlangt wären 10 V mit 1,26 V/µs Steigung; der Ausgang läuft mit 0,5 V/µs als Dreieck auf und ab und erreicht nur ±6,0 V, gestrichelt der verlangte Sinus. Die Bandbreite begrenzt kleine Signale, die Anstiegsgeschwindigkeit große.
:::

**Die Akteure:**

- __$\mathrm{SR}$__: Anstiegsgeschwindigkeit (englisch slew rate), die größte Änderungsgeschwindigkeit der Ausgangsspannung; beim Beispiel-OPV 0,5 V/µs. Sie entsteht, wenn die Eingangsstufe bei großer Differenzspannung ganz umschaltet, im Modell ab rund 80 mV, und den Kompensationskondensator mit ihrem vollen Strom lädt ([Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html), Abschnitt *Warum die Schaltung zur Ruhe kommt*).
- __$f_P$__: die höchste Frequenz, bis zu der ein Sinus mit der Amplitude $\hat U_A$ am Ausgang die Anstiegsgrenze nicht erreicht; für die volle Ausgangsamplitude heißt sie __Leistungsbandbreite__ (englisch full power bandwidth).

**Das Zusammenspiel in Schritten** (Rauschverstärkung 10, Abbildung 6):

**Schritt 1**: Ein Sinus ändert sich im Nulldurchgang am schnellsten, mit 2π mal Frequenz mal Amplitude: 10 V bei 20 kHz verlangen 1,26 V/µs, bei 5 kHz 0,31 V/µs.

**Schritt 2**: Liegt das unter der Anstiegsgeschwindigkeit, folgt der Ausgang, und nur die Bandbreite begrenzt (Abbildung 6b).

**Schritt 3**: Liegt es darüber, bleibt der Ausgang zurück, die Differenzspannung wächst, bis die Eingangsstufe ihren ganzen Strom liefert (im Modell ab 80 mV), und der Ausgang steigt nur noch mit 0,5 V/µs. Er kehrt erst um, wenn der verlangte Verlauf ihn einholt: Aus dem Sinus wird ein Dreieck, bei 20 kHz mit höchstens 6,25 V Amplitude, in der Simulation 6,0 V (Abbildung 6c).

**Schritt 4**: Welche Grenze gilt, hängt von der Amplitude ab: Ein Sinus mit 0,5 V kommt bei 20 kHz mit 0,49 V an (Abbildung 6a). Bei der Rauschverstärkung 10 begrenzt bis 0,8 V Ausgangsamplitude die Bandbreite, darüber die Anstiegsgeschwindigkeit.

:::formel Formel
$$f_P = \frac{\mathrm{SR}}{2\pi\,\hat U_A}$$
:::

**So liest man das:** Je größer die Amplitude, desto früher beginnt die Verzerrung: Mit dem Beispiel-OPV bleibt ein Sinus mit 1 V bis 79,6 kHz unverzerrt, mit 10 V nur bis 7,96 kHz, mit der vollen Aussteuerung von 14 V bis 5,68 kHz. Die Grenze hängt nicht von der Verstärkung ab, nur von der Amplitude am Ausgang.

Idee der Herleitung: Man vergleicht die größte Steigung eines Sinus mit der Anstiegsgeschwindigkeit.

:::herleitung
**Ausgangspunkt:** die Ableitung der Sinusfunktion und die Definition der Anstiegsgeschwindigkeit als größte Änderungsgeschwindigkeit des Ausgangs.

**Annahmen:** (i) Die verlangte Ausgangsspannung ist ein Sinus mit der Amplitude $\hat U_A$ und der Kreisfrequenz $\omega = 2\pi f$. (ii) Unverzerrt heißt: Die verlangte Steigung ist nirgends größer als die Anstiegsgeschwindigkeit.

**Schritt 1**: Verlangter Verlauf, zeitabhängig und deshalb klein geschrieben, und seine Ableitung:

$$u_A = \hat U_A\,\sin(\omega t)$$

$$\frac{du_A}{dt} = \omega\,\hat U_A\,\cos(\omega t)$$

**Schritt 2** (entscheidender Schritt): Der Kosinus erreicht im Nulldurchgang des Sinus seinen größten Betrag 1; die größte Steigung ist deshalb:

$$\Big|\frac{du_A}{dt}\Big|_{\max} = 2\pi f\,\hat U_A$$

**Schritt 3**: Unverzerrt bleibt der Ausgang, solange diese Steigung die Anstiegsgeschwindigkeit nicht übersteigt:

$$2\pi f\,\hat U_A \le \mathrm{SR}$$

**Ergebnis:**

$$f_P = \frac{\mathrm{SR}}{2\pi\,\hat U_A}$$

**Woher die Faktoren kommen:** $2\pi f$ stammt aus der Ableitung des Sinus, $\hat U_A$ daher, dass ein größerer Sinus in derselben Zeit einen längeren Weg zurücklegt.

**Proben:** Einheit (V/s)/V = 1/s. Zahlenwert: 0,5 V/µs durch 2π mal 10 V ergibt 7,96 kHz. Grenzfall kleiner Amplituden: $f_P$ wird sehr groß, und es begrenzt die Bandbreite.

**Grenzen:** Die Formel sagt, wo die Verzerrung im Modell mit harter Begrenzung beginnt; real setzt sie allmählich ein. Form und Amplitude des verzerrten Signals folgen aus dem Verhalten der umschaltenden Eingangsstufe (Schritte oben).
:::

::::beispiel Kleines und großes Signal am Verstärker mit der Rauschverstärkung 10
**Gegeben:** nichtinvertierender Verstärker mit $R_1$ = 10 kΩ und $R_2$ = 90 kΩ; Beispiel-OPV mit $f_T$ = 1 MHz und 0,5 V/µs; Eingänge (a) 0,05 V bei 20 kHz, (b) 1 V bei 20 kHz.

**Gesucht:** ob der Ausgang unverzerrt bleibt, und seine Amplitude.

**Rechnung:** Verlangte größte Steigung bei 0,5 V bzw. 10 V Ausgangsamplitude:

$$\text{(a)}\quad 2\pi\cdot 20\ \mathrm{kHz}\cdot 0{,}5\ \mathrm{V} = 0{,}063\ \mathrm{V}/\mu\mathrm{s}$$

$$\text{(b)}\quad 2\pi\cdot 20\ \mathrm{kHz}\cdot 10\ \mathrm{V} = 1{,}26\ \mathrm{V}/\mu\mathrm{s}$$

(a) liegt unter 0,5 V/µs; es bleibt der Abfall durch die Bandbreite:

$$\frac{0{,}5\ \mathrm{V}}{\sqrt{1 + (20/100)^2}} = 0{,}490\ \mathrm{V}$$

(b) liegt darüber; das Dreieck erreicht höchstens die Anstiegsgeschwindigkeit mal eine Viertelperiode:

$$0{,}5\ \mathrm{V}/\mu\mathrm{s}\cdot 12{,}5\ \mu\mathrm{s} = 6{,}25\ \mathrm{V}$$

Die Simulation des Modells ergibt 6,0 V.

**Ergebnis:** **(a) Sinus mit 0,49 V, (b) Dreieck mit 6,0 V statt 10 V.**

**Einordnung:** Bei derselben Frequenz kommt das kleine Signal mit 2 % Abfall an, das große nur als Dreieck mit 60 % der Amplitude; eine Bandbreitenangabe allein sagt über große Signale nichts.
::::

## Alles hängt an einem Prinzip

| Einzel­heit | welche Seite des Prinzips sie zeigt |
|---|---|
| Verstärkungs­fehler, kleiner Ausgangs­widerstand | Fehler im Verstärker, durch die Schleifen­verstärkung geteilt |
| Offset­spannung, Ruhe­ströme | Fehler am Eingang, verstärkt mit der Rausch­verstärkung |
| Gleichtakt- und Betriebs­spannungs­einfluss | wirken wie eine kleine Differenz­spannung am Eingang |
| Grenz­frequenz | die Schleifen­verstärkung fällt mit der Frequenz |
| Anstiegs­geschwindig­keit, Aussteuer­grenzen | Grenzen großer Signale, die keine Gegen­kopplung aufhebt |

Ein realer OPV ist ein idealer mit kleinen Fehlerquellen: Fehler im Verstärker teilt die Gegenkopplung durch die Schleifenverstärkung, Fehler an den Eingängen verstärkt sie wie ein Signal; weil die Schleifenverstärkung mit der Frequenz fällt, wirkt die Gegenkopplung nur bis zu einer Grenzfrequenz, und große Signale begrenzen zusätzlich Aussteuerbereich und Anstiegsgeschwindigkeit.

## Bedeutung und Ausblick

Welcher Fehler zählt, bestimmt die Wahl des OPV: für kleine Gleichspannungen Präzisions-OPVs mit Offsetspannungen im Mikrovoltbereich oder OPVs mit Feldeffekttransistoren am Eingang, für große und schnelle Signale hohe Transitfrequenz und Anstiegsgeschwindigkeit. Gerechnet wird mit den garantierten Datenblattwerten; die genauere Behandlung der Offsetspannung folgt laut Skript in Schaltungstechnik 1 und 2 (S. 212).

**In der ausführlichen Fassung:** alle Datenblattwerte, die zwei Arten von Fehlern im Bild und im Vergleich mit einem Thermostat, Ein- und Ausgangswiderstand unter Gegenkopplung, die Ausgangsstufe, der Ausgleichswiderstand Schritt für Schritt, die Herkunft der endlichen Gleichtaktunterdrückung, die Betriebsspannungsunterdrückung und das Überschwingen des Spannungsfolgers. [Zur ausführlichen Fassung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/realer-operationsverstaerker-ausfuehrlich.html)

:::kern
- Ein realer OPV ist ein idealer mit kleinen Fehlerquellen; wie die Gegenkopplung sie behandelt, hängt davon ab, wo sie sitzen.
- Fehler im Verstärker teilt sie durch die Schleifenverstärkung: Der relative Verstärkungsfehler ist rund $1/(k\,v_D)$.
- Fehler an den Eingängen verstärkt sie wie ein Signal, mit der Rauschverstärkung $1/k = 1 + R_2/R_1$, auch beim invertierenden Verstärker.
- Ruheströme ergeben $R_2 I_{B-}$ am Ausgang; mit $R_3 = R_1 \parallel R_2$ am Pluseingang bleibt nur $R_2 I_{os}$.
- Eine Gleichtaktspannung wirkt wie eine Differenzspannung vom Betrag $U_{Gl}/\mathrm{CMRR}$; in Dezibel ist die Unterdrückung $20\,\lg|v_D/v_{Gl}|$.
- Die Bandbreite einer Schaltung ist $k\,f_T$: Rauschverstärkung mal Bandbreite gleich Transitfrequenz.
- Ein großer Sinus bleibt nur bis $f_P = \mathrm{SR}/(2\pi\,\hat U_A)$ unverzerrt.
- Ausgang und Eingänge bleiben beim 741 typisch 1 bis 2 V von der Versorgung entfernt.
:::

:::quiz
F: Warum wird die Offsetspannung beim invertierenden Verstärker mit 1 + R_2/R_1 verstärkt und nicht mit −R_2/R_1?
A: Weil sie vor dem Pluseingang sitzt; setzt man das Signal null, ist die Schaltung für sie ein nichtinvertierender Verstärker. Beim Umkehrer mit −1 erscheint 1 mV deshalb als 2 mV.
F: Warum endet die Bandbreite bei der Frequenz k·f_T?
A: Dort ist die Schleifenverstärkung auf 1 gefallen. Die Differenzspannung, die der integrierende OPV braucht, ist dann so groß wie das zurückgeführte Signal und um eine Viertelperiode verschoben; die Verstärkung sinkt auf das 0,707-fache.
F: Warum verzerrt der 741 einen Sinus mit 10 V Amplitude bei 20 kHz, obwohl die Schaltung mit der Rauschverstärkung 10 bis 100 kHz reicht?
A: Der Sinus verlangt im Nulldurchgang 1,26 V/µs, der 741 schafft 0,5 V/µs. Seine Eingangsstufe schaltet ganz um, und der Ausgang läuft als Dreieck mit rund 6 V Amplitude.
F: Stimmt es, dass ein OPV mit 1 MHz Transitfrequenz Signale bis 1 MHz verstärkt?
A: Nein. Bei 1 MHz ist seine Verstärkung auf 1 gefallen; eine Schaltung mit der Rauschverstärkung 1/k reicht nur bis k·f_T, mit 101 bis 9,9 kHz.
F: Stimmt es, dass der Eingangsruhestrom durch den Eingangswiderstand von 2 MΩ fließt und bei kleiner Differenzspannung verschwindet?
A: Nein. Er ist der Basisstrom der Eingangstransistoren und fließt immer; der Eingangswiderstand beschreibt nur die Änderung mit der Differenzspannung, bei 25 µV 12,5 pA.
F: Bis zu welcher Frequenz bleibt ein Sinus mit 10 V Amplitude am Ausgang des Beispiel-OPV unverzerrt?
A: Bis 0,5 V/µs durch 2π mal 10 V, also 7,96 kHz; darüber läuft der Ausgang an die Anstiegsgrenze.
:::
