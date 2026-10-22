---
title: Der reale Operationsverstärker
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Operationsverstärker
order: 120700
summary: Wie sich ein realer OPV vom idealen unterscheidet und was jede Abweichung in einer gegengekoppelten Schaltung bewirkt: endliche und mit der Frequenz fallende Verstärkung, Aussteuergrenzen, Offsetspannung, Eingangsruheströme, Gleichtakt- und Betriebsspannungsunterdrückung, Bandbreite und Anstiegsgeschwindigkeit. Ausführliche Fassung mit allen Herleitungen, dem Ausgangswiderstand unter Gegenkopplung, der Temperaturdrift des Offsets, der Herkunft der endlichen Gleichtaktunterdrückung und dem Überschwingen des Spannungsfolgers.
tags: realer OPV, Verstärkungs-Bandbreite-Produkt, Transitfrequenz, Slew Rate, Offsetspannung, Eingangsruhestrom, CMRR
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Die goldenen Regeln rechnen mit einem OPV, dessen Verstärkung unendlich ist, in dessen Eingänge kein Strom fließt und der beliebig schnell reagiert. Ein realer OPV wie der verbreitete 741 erfüllt keine dieser Annahmen, und doch stimmen die Ergebnisse der Grundschaltungen meist auf Promille. Wann sie nicht mehr stimmen und um wie viel, folgt aus einem Prinzip:

**Ein realer OPV ist ein idealer mit kleinen Fehlerquellen: Fehler im Verstärker teilt die Gegenkopplung durch die Schleifenverstärkung, Fehler an den Eingängen verstärkt sie wie ein Signal; weil die Schleifenverstärkung mit der Frequenz fällt, wirkt die Gegenkopplung nur bis zu einer Grenzfrequenz, und große Signale begrenzen zusätzlich Aussteuerbereich und Anstiegsgeschwindigkeit.**

Vorausgesetzt werden die Gegenkopplung mit Rückkopplungsfaktor und Schleifenverstärkung aus [Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html) und die Schaltungen aus [Die OPV-Grundschaltungen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/opv-grundschaltungen.html).

:::grafik
Szene: get1/operationsverstaerker/03-ersatzschaltbild · Vorlage: schaltplan
**Abbildung 1:** Ersatzschaltbild des Beispiel-OPV (Art 741 an ±15 V). In der Mitte ein OPV mit der endlichen Leerlaufverstärkung $v_D$ = 200 000, die oberhalb von 5 Hz mit der Frequenz fällt, und der Anstiegsgrenze 0,5 V/µs. Außen die übrigen Abweichungen als Bauteile: vor dem Pluseingang eine Spannungsquelle von 1 mV (Offsetspannung), an jedem Eingang eine Stromquelle von 80 nA in den OPV hinein (Eingangsruheströme), zwischen den Eingängen 2 MΩ (Eingangswiderstand), in Reihe zum Ausgang 75 Ω (Ausgangswiderstand). Daneben die Grenzen: Ausgang ±14 V, Eingänge ±13 V, Gleichtaktunterdrückung 95 dB. Links umrandet die Quellen an den Eingängen, rechts die Abweichungen im Verstärker. Wo eine Abweichung sitzt, entscheidet, was die Gegenkopplung mit ihr macht.
:::

## Was am realen OPV anders ist

*Worin weicht ein realer OPV vom idealen ab, und warum wirken die Abweichungen so verschieden?*

In der Praxis denkt man sich einen idealen OPV und hängt jede Abweichung als kleine Quelle oder als Widerstand an, wie in Abbildung 1. Die Offsetspannung ist dabei eine kleine Fehlspannung zwischen den Eingängen; der Ruhestrom fließt ständig in jeden Eingang, und der Offsetstrom ist der Unterschied der beiden Ruheströme; die beiden Unterdrückungen geben an, wie schwach eine gemeinsame Spannung an beiden Eingängen bzw. eine Schwankung der Versorgung auf den Ausgang wirkt. Die Werte stehen im Datenblatt, als typischer Wert und, wo angegeben, als garantierte Grenze. Für den Beispiel-OPV gelten die des LM741 an ±15 V und bei 25 °C; Ausgangswiderstand und Transitfrequenz stammen aus Datenblättern des µA741, den Eingangswiderstand gibt das LM741-Datenblatt für ±20 V an:

| Eigen­schaft | idealer OPV | Beispiel-OPV: typisch; garantiert |
|---|---|---|
| Leerlauf­verstärkung $v_D$ | unendlich | 200 000; mindestens 50 000 |
| Verstärkung bei hohen Frequen­zen | unverändert | ab 5 Hz fallend, bei 1 MHz gleich 1 |
| Anstiegs­geschwindig­keit | unbegrenzt | 0,5 V/µs |
| Ausgangs­bereich an ±15 V | ±15 V | ±14 V an 10 kΩ, ±13 V an 2 kΩ; ±12 V bzw. ±10 V |
| Eingangs­bereich | unbegrenzt | ±13 V; ±12 V |
| Offset­spannung | 0 | 1 mV; höchstens 5 mV |
| Eingangs­ruhe­strom | 0 | 80 nA; höchstens 500 nA |
| Offset­strom | 0 | 20 nA; höchstens 200 nA |
| Eingangs­widerstand | unendlich | 2 MΩ; mindestens 0,3 MΩ |
| Ausgangs­widerstand | 0 | 75 Ω |
| Gleichtakt­unter­drückung | unendlich | 95 dB; mindestens 80 dB |
| Betriebs­spannungs­unter­drückung | unendlich | 96 dB; mindestens 86 dB |

:::grafik
Szene: get1/operationsverstaerker/03-fehlerorte · Vorlage: schaltung-zustaende
**Abbildung 2:** Zwei Arten von Abweichungen am nichtinvertierenden Verstärker mit $R_1$ = 10 kΩ und $R_2$ = 90 kΩ, Verstärkung 10. (a) Abweichungen im Verstärker: Sinkt die Leerlaufverstärkung von 200 000 auf 50 000, ändert sich die Verstärkung nur von 9,9995 auf 9,998; der Ausgangswiderstand von 75 Ω wirkt wie 3,75 mΩ. (b) Abweichung am Eingang: Eine Offsetspannung von 1 mV vor dem Pluseingang erscheint bei 0 V Eingangsspannung als 10 mV am Ausgang. Was im Verstärker entsteht, teilt die Gegenkopplung, was am Eingang entsteht, verstärkt sie wie ein Signal.
:::

Die Tabelle wirkt wie eine Liste unabhängiger Mängel. Für die Schaltung zählt aber vor allem, wo eine Abweichung sitzt (Abbildung 2).

Ein Teil entsteht im Verstärker selbst, zwischen der Differenzspannung und dem Ausgang: die endliche und von Exemplar zu Exemplar schwankende Leerlaufverstärkung und der Ausgangswiderstand. Sie verschieben den Ausgang gegen den Wert, den die äußere Schaltung verlangt. Diese Verschiebung kommt über die Rückführung an den Minuseingang zurück, und der OPV regelt sie nach. Übrig bleibt nur ein kleiner Bruchteil: In Abbildung 2a ändert ein Rückgang der Leerlaufverstärkung um drei Viertel die Verstärkung der Schaltung um 0,015 %.

Der andere Teil entsteht an den Eingängen: die Offsetspannung, die Ruheströme, der Einfluss von Gleichtakt- und Versorgungsspannung und das Rauschen. Er wirkt wie eine zusätzliche Eingangsspannung, und die kann der OPV vom Signal nicht unterscheiden. Er regelt den Ausgang so, dass sie zusammen mit dem Signal verstärkt wird; in Abbildung 2b erscheint 1 mV Offset als 10 mV am Ausgang.

Dazu kommen Grenzen, die keine kleinen Fehler sind. Die Leerlaufverstärkung fällt mit der Frequenz und mit ihr die Schleifenverstärkung, auf der die Gegenkopplung beruht; und der Ausgang kann weder beliebig groß noch beliebig schnell werden. Die goldenen Regeln bleiben gültig, solange die Schleifenverstärkung groß ist und kein Signal an eine Grenze stößt. Die Abweichungen rechnet man dann einzeln aus und überlagert sie, weil die Schaltung linear ist.

:::analogie
Ein Thermostat regelt eine Raumtemperatur nach demselben Muster. Er vergleicht den Wert seines Fühlers mit dem eingestellten Sollwert und verstellt die Heizung, bis beide übereinstimmen. Schwankt die Leistung der Heizung oder steht ein Fenster offen, gleicht die Regelung das aus, und der Raum bleibt auf dem Sollwert. Meldet der Fühler aber 1 K zu viel, regelt der Thermostat den Raum zuverlässig auf 1 K unter den Sollwert, denn den Fehler kann er vom echten Messwert nicht unterscheiden.

| Im Vergleich | In der Schaltung |
|---|---|
| eingestellte Soll­temperatur | Eingangs­spannung |
| schwankende Heiz­leistung, offenes Fenster | endliche Leerlauf­verstärkung, Ausgangs­widerstand, Last |
| Fühler und Vergleich im Thermostat | Rück­führung über den Teiler, Differenz­bildung am Eingang |
| Fehler von Fühler oder Vergleich | Offset­spannung, Ruhe­ströme, Gleichtakt­einfluss |

**Wo der Vergleich nicht stimmt:** Ein Thermostat schaltet die Heizung meist nur ein und aus, statt stetig zu regeln, und er braucht Minuten statt Mikrosekunden. Außerdem übernimmt er einen Fühlerfehler eins zu eins, während eine Verstärkerschaltung einen Eingangsfehler mit ihrer Verstärkung vergrößert.
:::

## Endliche Leerlaufverstärkung

*Um wie viel weicht die Verstärkung einer Schaltung vom Widerstandsverhältnis ab, und wovon hängt die Abweichung ab?*

**Die Akteure:**

- __$k$__: Rückkopplungsfaktor, der Anteil der Ausgangsspannung, der über den Teiler aus $R_2$ und $R_1$ am Minuseingang ankommt, wenn die Eingangsspannung null ist. Er ist beim nichtinvertierenden und beim invertierenden Verstärker derselbe, denn mit $U_E$ = 0 liegt $R_1$ in beiden Fällen zwischen Minuseingang und Masse:

$$k = \frac{R_1}{R_1 + R_2}$$

- __$k\,v_D$__: Schleifenverstärkung, so stark wird eine Änderung verstärkt, die einmal durch OPV und Teiler läuft ([Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html), Abschnitt *Der Ruhezustand*); mit $k$ = 0,1 und dem Beispiel-OPV 20 000.
- __$A_\mathrm{ideal}$__: Verstärkung mit idealem OPV; beim nichtinvertierenden Verstärker $1/k$, also $1 + R_2/R_1$, beim invertierenden $-R_2/R_1$.

**Das Zusammenspiel:** Damit der Ausgang $U_A$ liefert, braucht der OPV zwischen seinen Eingängen die Differenzspannung $U_A/v_D$, bei 2 V Ausgang und 200 000 also 10 µV. Diese Spannung fehlt der Rückführung: Der Ausgang bleibt gerade so weit hinter dem Wert zurück, den die Widerstände verlangen, dass die nötige Differenz entsteht. Wie weit, entscheidet die Schleifenverstärkung. Eine Abweichung des Ausgangs um 1 V verschiebt den Minuseingang um $k$ mal 1 V, und der OPV verstärkt das $v_D$-fach; je größer $k\,v_D$, desto kleiner die Abweichung, die für die nötige Differenzspannung genügt.

:::formel Formel
$$A = \frac{A_\mathrm{ideal}}{1 + \dfrac{1}{k\,v_D}}$$
$$\frac{A_\mathrm{ideal} - A}{A_\mathrm{ideal}} = \frac{1}{1 + k\,v_D}$$
:::

**So liest man das:** Die Verstärkung bleibt um den Bruchteil $1/(1 + k v_D)$ hinter dem Widerstandsverhältnis zurück, praktisch um den Kehrwert der Schleifenverstärkung. Je größer die gewünschte Verstärkung, desto kleiner $k$ und desto größer der Fehler: Mit dem Beispiel-OPV sind es bei $1/k$ = 10 0,005 %, bei 101 0,05 % und bei 1001 0,5 %. Schwankungen von $v_D$ gehen nur mit demselben Bruchteil ein. Für unendliches $v_D$ wird $A$ genau zum Widerstandsverhältnis.

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

**Gesucht:** die Verstärkung mit beiden Werten von $v_D$ und ihre Änderung zwischen beiden.

**Rechnung:** Rückkopplungsfaktor und Schleifenverstärkung:

$$k = \frac{1\ \mathrm{k}\Omega}{1\ \mathrm{k}\Omega + 100\ \mathrm{k}\Omega} = 0{,}00990$$

$$k\,v_D = 0{,}00990\cdot 200\,000 = 1980$$

$$A = \frac{-100}{1 + 1/1980} = -99{,}95$$

Mit 50 000 ist $k v_D$ = 495:

$$A = \frac{-100}{1 + 1/495} = -99{,}80$$

**Ergebnis:** **$A$ = −99,95 (Fehler 0,05 %) bzw. −99,80 (0,2 %); der Rückgang von $v_D$ um 75 % ändert $A$ um 0,15 %.**

**Einordnung:** Die Schwankung der Leerlaufverstärkung kommt rund 500-fach verkleinert an. Widerstände mit 1 % Toleranz können das Verhältnis $R_2/R_1$ dagegen um bis zu 2 % verfälschen; nicht der OPV, sondern die Widerstände bestimmen hier die Genauigkeit.

**Variation:** Mit $1/k$ = 1001 (nichtinvertierend, 100 Ω und 100 kΩ) wächst der Fehler auf 0,5 % bzw. 2 %.
::::

Dieselbe Nachregelung wirkt auf Ein- und Ausgangswiderstand. Den Spannungsabfall, den ein Laststrom am Ausgangswiderstand $R_a$ verursacht, regelt der OPV aus, bis nur der Bruchteil $1/(1 + k v_D)$ bleibt; mit $k$ = 0,1 wirken die 75 Ω wie 3,75 mΩ: Bei 5 V an 1 kΩ fehlen statt 0,375 V nur 19 µV. Am Eingang des nichtinvertierenden Verstärkers liegt über dem Eingangswiderstand $R_e$ nur die kleine Differenzspannung; durch ihn fließen bei 1 V Eingang 25 pA, als hätte der Eingang 40 GΩ. Was tatsächlich in den Eingang fließt, ist der 3200-mal größere Ruhestrom (Abschnitt *Eingangsruheströme*).

:::frage
„Bleibt der Ausgangswiderstand auch bei hohen Frequenzen so klein?“
Nein. Er ist nur so klein, wie die Schleifenverstärkung groß ist, und die fällt oberhalb von 5 Hz mit der Frequenz (Abschnitt *Frequenzgang und Verstärkungs-Bandbreite-Produkt*). Mit $k$ = 0,1 wirkt der Ausgang bei 1 kHz wie 0,75 Ω, bei 10 kHz wie 7,5 Ω und bei 100 kHz wie 53 Ω; er wächst mit der Frequenz wie bei einer Spule. Lasten, die schnell wechselnde Ströme ziehen, etwa lange Kabel mit ihrer Kapazität, sehen den OPV deshalb mit einem viel größeren Innenwiderstand, als die Rechnung für Gleichspannung ergibt.
:::

## Aussteuergrenzen an Ausgang und Eingängen

*Wie weit kann sich der Ausgang bewegen, und welche Spannungen vertragen die Eingänge?*

:::grafik
Szene: get1/operationsverstaerker/03-aussteuerung · Vorlage: schaltung-und-kennlinie
**Abbildung 3:** (a) Vereinfachte Ausgangsstufe eines OPV wie des 741: zwei Emitterfolger übereinander, ein npn-Transistor zur positiven und ein pnp-Transistor zur negativen Versorgung, ihre Emitter über kleine Widerstände am Ausgang, die Basen von der vorangehenden Stufe getrieben. Eingezeichnet ist der Weg vom Ausgang zur positiven Versorgung: die Basis-Emitter-Strecke des npn-Transistors, rund 0,6 V, und die Sättigungsspannung des Transistors, der seine Basis treibt. (b) Spannungsbereiche als senkrechte Balken neben der Versorgung von −15 V bis +15 V: Ausgang bis ±14 V an 10 kΩ und bis ±13 V an 2 kΩ, Eingänge ±13 V, garantiert ±12 V. Zwischen jeder Signalspannung und der Versorgung liegen Transistorstrecken, an denen Spannung abfällt.
:::

Den Ausgang eines OPV treiben zwei Emitterfolger, einer für positive und einer für negative Spannungen (Abbildung 3a). Damit der obere den Ausgang anhebt, muss seine Basis um eine Basis-Emitter-Spannung von rund 0,6 V höher liegen, und der Transistor, der diese Basis treibt, braucht seinerseits eine kleine Spannung zur Versorgung, seine Sättigungsspannung. Deshalb bleibt der Ausgang rund 1 V unter der Versorgung, beim Beispiel-OPV an ±15 V bei ±14 V; diese Grenzen heißen $U_{A,\min}$ und $U_{A,\max}$.

Mit Last fließt mehr Strom durch die Ausgangstransistoren, und die Spannungsabfälle wachsen: An 2 kΩ, also bei 6,5 mA, erreicht der Ausgang nur noch ±13 V. Zum Schutz begrenzt der OPV seinen Ausgangsstrom auf den __Kurzschlussstrom__, den Strom, den er bei kurzgeschlossenem Ausgang liefert, beim 741 typisch 25 mA. An 200 Ω kommt der Ausgang deshalb nur auf etwa 5 V. Sogenannte __Rail-to-Rail-OPVs__ (englisch rail, die Versorgungsschiene) haben eine andere Ausgangsstufe und kommen bis auf einige zehn Millivolt an die Versorgung heran.

Auch die Eingänge brauchen Abstand zur Versorgung, denn die Transistoren der Eingangsstufe und ihre Fußpunktstromquelle arbeiten nur mit genügend Spannung zwischen Kollektor und Emitter. Beim Beispiel-OPV dürfen beide Eingänge zwischen −13 V und +13 V liegen, garantiert zwischen −12 V und +12 V; das ist der __Gleichtakt-Eingangsbereich__. Liegt ein Eingang außerhalb, folgt der Ausgang der Differenzspannung nicht mehr richtig; bei manchen OPV-Typen springt er dann sogar an die falsche Grenze. Beim Spannungsfolger, dessen Eingang so groß ist wie sein Ausgang, begrenzt deshalb der Eingangsbereich: Er überträgt nur bis ±13 V.

## Offsetspannung

*Warum liefert ein OPV ohne Eingangssignal eine Ausgangsspannung, und mit welchem Faktor erscheint dieser Fehler am Ausgang?*

:::grafik
Szene: get1/operationsverstaerker/03-offset · Vorlage: schaltung-und-kennlinie
**Abbildung 4:** (a) Ursache: Kollektorstrom über der Basis-Emitter-Spannung nach der Transfergleichung für zwei Transistoren derselben Bauart, $I_C$ logarithmisch von 1 µA bis 10 mA, $U_{BE}$ von 0,45 V bis 0,75 V; der Beispieltransistor ($I_S$ = 10⁻¹⁴ A) und ein zweiter mit 4 % größerem $I_S$ ergeben zwei parallele Geraden, waagrecht um 1,01 mV gegeneinander verschoben, was im ganzen Diagramm nicht zu sehen ist; eine Lupe um 0,5 mA mit $U_{BE}$ von 0,634 V bis 0,640 V zeigt den Abstand. (b) Wirkung: invertierender Verstärker mit $R_1$ = 10 kΩ und $R_2$ = 20 kΩ, Eingang auf 0 V gelegt, die Offsetspannung als Quelle von 1 mV vor dem Pluseingang; beide Eingänge des inneren OPV auf 1 mV, 0,1 µA durch $R_1$ und $R_2$, Ausgang 3 mV. Daneben dieselbe Schaltung umgezeichnet: Für die Offsetquelle ist sie ein nichtinvertierender Verstärker mit $1 + R_2/R_1$ = 3. Die Offsetspannung wird mit der Rauschverstärkung verstärkt, nicht mit der Signalverstärkung.
:::

**Die Akteure:**

- __$U_{os}$__: __Offsetspannung__, die Differenzspannung, die man zwischen die Eingänge legen muss, damit der Ausgang null wird; beim Beispiel-OPV typisch 1 mV, höchstens 5 mV, das Vorzeichen von Exemplar zu Exemplar verschieden. Im Ersatzschaltbild ist sie eine Spannungsquelle vor dem Pluseingang; die außen angelegte Spannung, die den Ausgang auf null bringt, ist gleich groß und hebt sie gerade auf.
- __$I_S$__: Sättigungsstrom eines Eingangstransistors aus der Transfergleichung ([Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html), Abschnitt *Der Transistoreffekt*); beim Beispieltransistor 10⁻¹⁴ A.
- __$1/k$__: __Rauschverstärkung__ (englisch noise gain), der Faktor, mit dem eine Spannung am Pluseingang am Ausgang erscheint, beim Verstärker mit 10 kΩ und 20 kΩ 3; sie ist der Kehrwert des Rückkopplungsfaktors, gleich $1 + R_2/R_1$. Den Namen hat sie, weil auch das Eigenrauschen des OPV mit ihr verstärkt wird.
- __$U_{A,os}$__: der Anteil der Ausgangsspannung, den die Offsetspannung verursacht.

**Das Zusammenspiel:** Die beiden Hälften der Eingangsstufe sind nie genau gleich; üblich ist dafür auch der englische Ausdruck Mismatch. Zwei Transistoren derselben Bauart haben nie genau denselben Sättigungsstrom $I_S$, denn Fläche und Dotierung schwanken bei der Fertigung ein wenig. Damit beide denselben Strom führen, braucht der mit dem kleineren $I_S$ eine größere Basis-Emitter-Spannung; nach der Transfergleichung verlangen 4 % Unterschied 1,01 mV (Abbildung 4a). Ungleiche Kollektorwiderstände oder Stromspiegel wirken ebenso, weil sie bei gleicher Eingangsspannung ungleiche Ströme verlangen; 1 % Unterschied entspricht 0,26 mV. Zusammen wirkt das wie eine kleine Spannungsquelle in Reihe mit einem Eingang. Weil ihr Vorzeichen zufällig ist, zeichnet man sie vor den Pluseingang.

**Das Zusammenspiel in Schritten** (invertierender Verstärker mit $R_1$ = 10 kΩ und $R_2$ = 20 kΩ, Eingang auf 0 V gelegt, Abbildung 4b):

**Schritt 1**: Die Offsetquelle liegt zwischen Masse und dem Pluseingang des inneren, idealen OPV; dieser Eingang liegt deshalb auf 1 mV.

**Schritt 2**: Die Gegenkopplung regelt die Differenzspannung am inneren OPV auf null; sein Minuseingang liegt also ebenfalls auf 1 mV.

**Schritt 3**: Der Eingang $U_E$ liegt auf 0 V. Durch $R_1$ fließen deshalb 0,1 µA vom Minuseingang zur Eingangsquelle.

**Schritt 4**: In den OPV fließt kein Strom; die 0,1 µA kommen über $R_2$ vom Ausgang. An $R_2$ fallen 2 mV ab, und der Ausgang liegt 2 mV über dem Minuseingang, bei 3 mV.

**Schritt 5**: Für die Offsetquelle ist die Schaltung ein nichtinvertierender Verstärker: Sie verstärkt mit $1 + R_2/R_1$ = 3, nicht mit −2. Dieser Faktor ist die Rauschverstärkung $1/k$.

:::formel Formel
$$U_{A,os} = \Big(1 + \frac{R_2}{R_1}\Big)\,U_{os} = \frac{U_{os}}{k}$$
:::

**So liest man das:** Die Offsetspannung erscheint mit der Rauschverstärkung am Ausgang, gleich, an welchem Eingang das Signal liegt. Beim nichtinvertierenden Verstärker ist die Rauschverstärkung gleich der Verstärkung, beim invertierenden um 1 größer als deren Betrag: Mit $A$ = −100 werden aus 1 mV 101 mV, aus den garantierten höchstens 5 mV 0,5 V. Mit derselben Rauschverstärkung erscheint auch das Eigenrauschen des OPV am Ausgang, bei $1/k$ = 101 als 2,3 µV/√Hz statt 23 nV/√Hz ([Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung-ausfuehrlich.html), Abschnitt *Die Quellen des Rauschens*).

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
**Gegeben:** Thermoelement Typ K mit 4,096 mV bei 100 °C gegen die Vergleichsstelle bei 0 °C (Normtabelle), also im Mittel 40,96 µV/K; nichtinvertierender Verstärker mit $R_1$ = 1 kΩ und $R_2$ = 100 kΩ; Beispiel-OPV mit $U_{os}$ = 1 mV (typisch) bzw. 5 mV (höchstens).

**Gesucht:** die Ausgangsspannung bei 100 °C und der Messfehler durch die Offsetspannung in Kelvin.

**Rechnung:** Verstärkung und Rauschverstärkung sind hier gleich:

$$\frac{1}{k} = 1 + \frac{100\ \mathrm{k}\Omega}{1\ \mathrm{k}\Omega} = 101$$

Signal bei 100 °C:

$$U_A = 101\cdot 4{,}096\ \mathrm{mV} = 413{,}7\ \mathrm{mV}$$

Offset am Ausgang:

$$U_{A,os} = 101\cdot 1\ \mathrm{mV} = 101\ \mathrm{mV}$$

In Temperatur umgerechnet; Signal und Offset werden gleich verstärkt, deshalb genügt der Vergleich am Eingang:

$$\frac{1\ \mathrm{mV}}{40{,}96\ \mu\mathrm{V/K}} = 24{,}4\ \mathrm{K}$$

**Ergebnis:** **Der Ausgang zeigt bei 0 °C schon 101 mV, als wäre die Messstelle 24 K wärmer, bei umgekehrtem Vorzeichen des Offsets entsprechend kälter; mit 5 mV wären es 122 K.**

**Einordnung:** Ein Viertel des Messbereichs bis 100 °C geht auf die Offsetspannung zurück, während der Verstärkungsfehler aus der endlichen Leerlaufverstärkung bei 100 °C nur 0,05 K ausmacht. Für kleine Gleichspannungen ist die Offsetspannung der wichtigste Fehler eines OPV.
::::

:::fehlvorstellung
„Der Umkehrer hat die Verstärkung −1; seine Offsetspannung wird deshalb nicht verstärkt.“ Das liegt nahe, weil man im invertierenden Verstärker jede Spannung mit $-R_2/R_1$ verrechnet. Die Offsetspannung liegt aber vor dem Pluseingang, nicht am Signaleingang, und für sie ist die Schaltung ein nichtinvertierender Verstärker (Schritt 5 oben). Beim Umkehrer mit zweimal 10 kΩ erscheint 1 mV Offset als 2 mV am Ausgang; der Spannungsfolger, dessen Verstärkung ebenfalls den Betrag 1 hat, gibt ihn unverändert weiter.
:::

:::frage
„Warum ändert sich die Offsetspannung mit der Temperatur?“
Ein Offset, der aus ungleichen Sättigungsströmen stammt, ist die Temperaturspannung $U_T$ mal dem Logarithmus des Stromverhältnisses. Das Verhältnis der beiden $I_S$ hängt nicht von der Temperatur ab, $U_T$ aber wächst proportional zur absoluten Temperatur. Ein Offset von 1 mV bei 300 K wächst deshalb um ein Dreihundertstel je Kelvin, um 3,3 µV/K; beim Thermoelement-Verstärker oben verschiebt das die Anzeige um 0,8 K je 10 K Erwärmung der Elektronik. Datenblätter nennen diese __Offsetdrift__, für die ausgesuchte Variante LM741A höchstens 15 µV/K. Dazu hängt der Offset von der Versorgungsspannung ab (Abschnitt *Gleichtakt- und Betriebsspannungsunterdrückung*) und ändert sich langsam über die Lebensdauer.
:::

:::frage
„Lässt sich die Offsetspannung nicht abgleichen?“
Für eine Temperatur ja. Der 741 hat dafür zwei Anschlüsse (1 und 5), die zu den Emitterwiderständen des Stromspiegels in der Eingangsstufe führen. Ein Potentiometer dort verschiebt die Stromaufteilung, bis der Ausgang null ist, laut Datenblatt im Bereich von ±15 mV, angegeben für ±20 V Versorgung. Die Temperaturdrift beseitigt das im Allgemeinen nicht. Bei Wechselspannungssignalen legt man einen Kondensator in Reihe zu $R_1$: Für Gleichspannung arbeitet die Schaltung dann als Spannungsfolger und gibt den Offset unverstärkt weiter, und den Rest trennt ein Kondensator am Ausgang ab. Wo kleine Gleichspannungen zählen, nimmt man Präzisions-OPVs mit Offsetspannungen im Mikrovoltbereich, etwa solche mit eingebautem, ständig wiederholtem Nullabgleich (Chopper- oder Auto-Zero-Verstärker).
:::

## Eingangsruheströme

*Warum fließt in die Eingänge eines OPV Strom, und was bewirkt er an den Widerständen der Schaltung?*

:::grafik
Szene: get1/operationsverstaerker/03-ruhestroeme · Vorlage: schaltung-strompfade
**Abbildung 5:** Invertierender Verstärker mit $R_1$ = 100 kΩ und $R_2$ = 1 MΩ, Eingang auf 0 V gelegt, Ruheströme von je 80 nA in beide Eingänge (Strompfeile). (a) Pluseingang direkt an Masse: Beide Eingänge auf 0 V, durch $R_1$ kein Strom, der Ruhestrom des Minuseingangs kommt ganz über $R_2$ vom Ausgang, der Ausgang liegt auf 80 mV. (b) Mit $R_3$ = 90,9 kΩ zwischen Pluseingang und Masse: Pluseingang und Minuseingang auf −7,27 mV, durch $R_1$ fließen 72,7 nA aus Masse zu, durch $R_2$ nur noch 7,27 nA, der Ausgang liegt auf 0 V; mit 20 nA Unterschied der Ruheströme wären es ±20 mV. Gleiche Ströme an gleichen Widerständen heben sich auf; übrig bleibt der Unterschied der Ströme.
:::

**Die Akteure:**

- __$I_{B+}$__, __$I_{B-}$__: Ruheströme in den Plus- und in den Minuseingang, beim Beispiel-OPV je rund 80 nA, in den OPV hinein.
- __$I_B$__: __Eingangsruhestrom__, der Mittelwert beider; typisch 80 nA, höchstens 500 nA.
- __$I_{os}$__: __Offsetstrom__, der Betrag ihres Unterschieds; typisch 20 nA, höchstens 200 nA.
- __$R_3$__: Widerstand zwischen Pluseingang und Masse, der die Wirkung der Ruheströme ausgleichen soll.
- __$U_{A,B}$__: der Anteil der Ausgangsspannung, den die Ruheströme verursachen.

**Das Zusammenspiel:** Die Eingänge des 741 sind die Basisanschlüsse seiner Eingangstransistoren. Jeder Transistor braucht einen Basisstrom, den Kollektorstrom geteilt durch die Stromverstärkung ([Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html)); beim 741 führen die Eingangstransistoren rund 10 µA, und mit einer Stromverstärkung um 125 ergibt das 80 nA. Dieser Strom fließt immer, auch wenn zwischen den Eingängen keine Spannung liegt. Mit dem Eingangswiderstand von 2 MΩ hat er nichts zu tun; der beschreibt nur, wie sich der Eingangsstrom mit der Differenzspannung ändert, bei 25 µV um 12,5 pA. Weil die beiden Transistoren nie ganz gleich sind, unterscheiden sich ihre Basisströme um den Offsetstrom. Wirksam werden die Ströme an den Widerständen, durch die sie fließen müssen.

**Das Zusammenspiel in Schritten** (invertierender Verstärker mit $R_1$ = 100 kΩ und $R_2$ = 1 MΩ, Eingang auf 0 V gelegt, Abbildung 5):

**Schritt 1**: Ohne $R_3$ liegt der Pluseingang an Masse, und die Gegenkopplung hält den Minuseingang ebenfalls auf 0 V. Durch $R_1$ fließt kein Strom, denn an beiden Enden liegen 0 V.

**Schritt 2**: Der Ruhestrom $I_{B-}$ muss trotzdem in den Minuseingang. Er kann nur über $R_2$ vom Ausgang kommen, und der Ausgang stellt sich auf 1 MΩ mal 80 nA ein, auf 80 mV (Abbildung 5a).

**Schritt 3**: Mit $R_3$ fließt $I_{B+}$ durch $R_3$ in den Pluseingang und senkt dessen Potential unter Masse, bei 90,9 kΩ auf −7,27 mV. Die Gegenkopplung zieht den Minuseingang mit.

**Schritt 4**: Jetzt liegt der Minuseingang 7,27 mV unter Masse, und durch $R_1$ fließen 72,7 nA aus Masse zu. Für $I_{B-}$ fehlen nur noch 7,27 nA, und die liefert der Ausgang über $R_2$ bei 0 V: An $R_2$ fallen 7,27 mV ab, genau so viel, wie der Minuseingang unter Masse liegt (Abbildung 5b).

**Schritt 5**: Das gelingt, wenn $R_3$ so groß ist wie der Widerstand, den der Minuseingang bei 0 V am Ausgang nach Masse sieht: $R_1$ und $R_2$ parallel, 90,9 kΩ. Gleiche Ruheströme an gleichen Widerständen verschieben dann beide Eingänge gleich, und übrig bleibt nur der Unterschied der Ströme: 1 MΩ mal 20 nA, also 20 mV statt 80 mV.

:::formel Formel
$$U_{A,B} = R_2\,I_{B-} - \Big(1 + \frac{R_2}{R_1}\Big)\,R_3\,I_{B+}$$
$$R_3 = \frac{R_1\,R_2}{R_1 + R_2}$$
$$U_{A,B} = R_2\,(I_{B-} - I_{B+})$$
:::

**So liest man das:** Die erste Zeile gilt für jedes $R_3$, auch für $R_3$ = 0. Ohne Ausgleich erscheint der Ruhestrom des Minuseingangs mal $R_2$ am Ausgang; der Fehler wächst mit dem Rückkopplungswiderstand, nicht mit der Verstärkung. Mit $R_3$ gleich der Parallelschaltung von $R_1$ und $R_2$ (zweite Zeile) bleibt nur der Offsetstrom mal $R_2$ (dritte Zeile), dessen Vorzeichen von Exemplar zu Exemplar wechselt. Mit 10 kΩ und 20 kΩ wie in den Grundschaltungen sind es ohne Ausgleich 1,6 mV, weniger als die 3 mV aus der Offsetspannung; mit 1 MΩ dagegen 80 mV.

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

::::beispiel Ruhestromfehler eines hochohmigen Verstärkers
**Gegeben:** invertierender Verstärker mit $R_1$ = 100 kΩ und $R_2$ = 1 MΩ, Verstärkung −10; Beispiel-OPV mit $I_B$ = 80 nA und $I_{os}$ = 20 nA (typisch), höchstens 500 nA bzw. 200 nA; $U_{os}$ = 1 mV.

**Gesucht:** der Ausgangsfehler durch die Ruheströme ohne und mit Ausgleichswiderstand, verglichen mit dem Fehler durch die Offsetspannung.

**Rechnung:** Ohne $R_3$:

$$U_{A,B} = 1\ \mathrm{M}\Omega\cdot 80\ \mathrm{nA} = 80\ \mathrm{mV}$$

Ausgleichswiderstand:

$$R_3 = \frac{100\ \mathrm{k}\Omega\cdot 1\ \mathrm{M}\Omega}{100\ \mathrm{k}\Omega + 1\ \mathrm{M}\Omega} = 90{,}9\ \mathrm{k}\Omega$$

Mit Ausgleich bleibt der Offsetstrom:

$$|U_{A,B}| = 1\ \mathrm{M}\Omega\cdot 20\ \mathrm{nA} = 20\ \mathrm{mV}$$

Offsetspannung mit der Rauschverstärkung 11:

$$U_{A,os} = 11\cdot 1\ \mathrm{mV} = 11\ \mathrm{mV}$$

**Ergebnis:** **80 mV ohne und 20 mV mit Ausgleichswiderstand, mit den garantierten Höchstwerten 0,5 V bzw. 0,2 V; die Offsetspannung trägt 11 mV bei.**

**Einordnung:** Bei Rückkopplungswiderständen im Megaohmbereich überwiegt der Ruhestrom die Offsetspannung. Dann nimmt man kleinere Widerstände oder einen OPV mit Feldeffekttransistoren am Eingang, deren Ruheströme bei Raumtemperatur im Pikoamperebereich liegen und sich mit je 10 K Erwärmung etwa verdoppeln. Am Integrator aus [Die OPV-Grundschaltungen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/opv-grundschaltungen.html) lädt derselbe Ruhestrom von 80 nA den Kondensator von 100 nF mit 0,8 V/s.

**Variation:** Mit 10 kΩ und 100 kΩ sind es 8 mV ohne und 2 mV mit Ausgleich.
::::

## Gleichtakt- und Betriebsspannungsunterdrückung

*Wie stark wirkt eine Spannung, die beide Eingänge gemeinsam haben, auf den Ausgang, und wann spielt das eine Rolle?*

:::grafik
Szene: get1/operationsverstaerker/03-gleichtakt · Vorlage: schaltung-zustaende
**Abbildung 6:** (a) Spannungsfolger mit 10 V am Eingang: Beide Eingänge liegen auf 10 V, die Gleichtaktspannung ist 10 V; mit 95 dB wirkt sie wie eine Differenzspannung von 0,18 mV, und der Ausgang weicht um 0,18 mV von 10 V ab. (b) Invertierender Verstärker: Beide Eingänge liegen auf 0 V, gleich welches Signal anliegt; es entsteht kein Gleichtaktfehler. (c) Skala der Gleichtaktunterdrückung von 60 dB bis 120 dB mit den zugehörigen Verhältnissen 10³ bis 10⁶; markiert 95 dB (Beispiel-OPV typisch, 56 000), 80 dB (garantiert, 10 000) und 61 dB (Subtrahierer mit 1 % Widerstandsabweichung aus den Grundschaltungen). Eine Gleichtaktspannung wirkt wie eine kleine Differenzspannung, aber nur, wo die Eingänge mit dem Signal mitlaufen.
:::

**Die Akteure:**

- __$U_{Gl}$__: Gleichtaktspannung, der Mittelwert der beiden Eingangsspannungen ([Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html), Abschnitt *Der Differenzverstärker*).
- __$v_{Gl}$__: __Gleichtaktverstärkung__ des OPV, die Änderung der Ausgangsspannung je Volt Gleichtaktspannung ohne Rückkopplung; beim Beispiel-OPV dem Betrag nach 3,6, gegen 200 000 für die Differenzspannung.
- __$\mathrm{CMRR}$__: __Gleichtaktunterdrückung__ (englisch common mode rejection ratio), das Verhältnis von Differenz- zu Gleichtaktverstärkung; beim Beispiel-OPV 56 000 oder 95 dB, garantiert 10 000 oder 80 dB.

:::formel Definition
$$\mathrm{CMRR} = \left|\frac{v_D}{v_{Gl}}\right|$$
$$\mathrm{CMRR}_\mathrm{dB} = 20\,\lg\left|\frac{v_D}{v_{Gl}}\right|$$
:::

Man definiert die Unterdrückung als Verhältnis, weil es angibt, wie viel schwächer eine Gleichtaktspannung wirkt als eine gleich große Differenzspannung. In Dezibel rechnet man mit 20 lg, weil es ein Verhältnis von Spannungen ist, wie beim Signal-Rausch-Verhältnis ([Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html), Abschnitt *Rauschen und Signal-Rausch-Verhältnis*): Ein Faktor 10 sind 20 dB, 95 dB ein Faktor von 56 000.

Praktische Werte liegen zwischen 60 dB und 120 dB, der Kehrwert $|v_{Gl}/v_D|$ also zwischen 10⁻³ und 10⁻⁶; 10⁻⁴ entsprechen 80 dB. Eine Gleichtaktspannung liegt an beiden Eingängen gleich an, etwa als Störung, die auf zwei Leitungen gleichermaßen einwirkt.

:::frage
„Woher kommt die endliche Gleichtaktunterdrückung, wenn die Stromquelle im Fußpunkt des Differenzverstärkers die Summe der Ströme festhält?“
Sie hält sie nur fast fest. Am Differenzverstärker aus [Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html) hebt 1 V Gleichtakt den Emitterknoten um 1 V, und am Transistor der Stromquelle liegt 1 V mehr. Wegen des Early-Effekts wirkt er wie eine Stromquelle mit 84 kΩ Innenwiderstand; der Fußpunktstrom steigt um 12 µA, jeder Kollektorstrom um 5,9 µA, und jedes Kollektorpotential sinkt um 59 mV. Zwischen den Kollektoren hebt sich das auf, aber nur so genau, wie beide Hälften gleich sind: Mit 1 % Unterschied der Kollektorwiderstände bleiben 0,59 mV je Volt Gleichtakt, gegen 193 V je Volt Differenz eine Unterdrückung von 330 000 oder 110 dB. Der 741 bleibt mit typisch 95 dB darunter, weil auch seine Transistoren, sein Stromspiegel und die folgende Stufe nicht genau gleich sind. Präzisions-OPVs gleichen die Eingangsstufe bei der Fertigung ab und speisen sie aus einer Stromquelle mit viel größerem Innenwiderstand; sie erreichen 120 dB und mehr.
:::

**Das Zusammenspiel:** Am Ausgang des OPV addieren sich zwei Wirkungen, die verstärkte Differenzspannung und die verstärkte Gleichtaktspannung. Klammert man die Differenzverstärkung aus, wirkt die Gleichtaktspannung wie eine zusätzliche Differenzspannung vom Betrag $U_{Gl}/\mathrm{CMRR}$, und die verstärkt die Gegenkopplung wie die Offsetspannung mit der Rauschverstärkung. Beim Beispiel-OPV wirken 10 V Gleichtakt wie 0,18 mV Differenzspannung, mit der garantierten Unterdrückung wie 1 mV. Entscheidend ist, ob die Eingänge überhaupt eine gemeinsame Spannung haben (Abbildung 6). Beim invertierenden Verstärker liegen beide auf 0 V, gleich welches Signal anliegt. Beim nichtinvertierenden Verstärker und beim Spannungsfolger laufen beide Eingänge mit dem Signal mit, und an Messbrücken liegen sie auf der halben Brückenspannung.

:::formel Formel
$$U_A = v_D\,\Big(U_D \pm \frac{U_{Gl}}{\mathrm{CMRR}}\Big)$$
:::

**So liest man das:** Eine Gleichtaktspannung verschiebt den Ausgang so, als läge zwischen den Eingängen zusätzlich eine Spannung vom Betrag $U_{Gl}/\mathrm{CMRR}$, mit einem Vorzeichen, das vom Exemplar abhängt. Je größer die Unterdrückung, desto kleiner dieser Beitrag; beim idealen OPV verschwindet er. Weil $U_{Gl}$ beim nichtinvertierenden Verstärker mit dem Signal wächst, wirkt der Fehler dort wie ein kleiner Verstärkungsfehler, den kein Offsetabgleich beseitigt.

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

::::beispiel Gleichtaktfehler am Spannungsfolger und am nichtinvertierenden Verstärker
**Gegeben:** Beispiel-OPV mit 95 dB (typisch) bzw. 80 dB (garantiert) Gleichtaktunterdrückung und 1 mV Offsetspannung; (a) Spannungsfolger mit 10 V am Eingang; (b) nichtinvertierender Verstärker mit der Verstärkung 10 und 1 V am Eingang.

**Gesucht:** der Gleichtaktfehler am Ausgang, verglichen mit dem Offsetfehler.

**Rechnung:** Die Unterdrückung als Verhältnis:

$$\mathrm{CMRR} = 10^{95/20} = 56\,234$$

(a) Gleichtaktspannung 10 V, Rauschverstärkung 1:

$$\frac{10\ \mathrm{V}}{56\,234} = 0{,}178\ \mathrm{mV}$$

Mit 80 dB, also 10 000, ist es 1 mV.

(b) Gleichtaktspannung 1 V wirkt wie 17,8 µV; mit der Rauschverstärkung 10 am Ausgang:

$$10\cdot 17{,}8\ \mu\mathrm{V} = 0{,}178\ \mathrm{mV}$$

Die Offsetspannung ergibt dort 10 mal 1 mV, also 10 mV.

**Ergebnis:** **(a) 0,18 mV bei 10 V, garantiert höchstens 1 mV; (b) 0,18 mV am Ausgang gegen 10 mV aus der Offsetspannung.**

**Einordnung:** Neben der Offsetspannung ist der Gleichtaktfehler eines guten OPV klein, hier 18 Millionstel der Eingangsspannung. Er zählt, wo man die Offsetspannung abgleicht, und an Messbrücken mit kleinen Differenzen. Beim Subtrahierer aus [Die OPV-Grundschaltungen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/opv-grundschaltungen.html) überwiegen ohnehin die Widerstände: 1 % Abweichung ergibt dort 61 dB, 34 dB weniger als der OPV selbst.
::::

:::fehlvorstellung
„Am Spannungsfolger gibt es keinen Gleichtakt, denn zwischen seinen Eingängen liegt keine Spannung.“ Das liegt nahe, weil die Differenzspannung null ist. Gleichtakt ist aber der gemeinsame Pegel beider Eingänge, und beim Folger liegen beide auf der Eingangsspannung. Bei 10 V am Eingang sind das 10 V Gleichtakt, zehnmal so viel wie beim nichtinvertierenden Verstärker mit der Verstärkung 10 und demselben Ausgang; sie wirken wie 0,18 mV Differenzspannung.
:::

Ähnlich wirkt eine Änderung der Versorgungsspannung. Sie verschiebt die Arbeitspunkte im OPV ein wenig und damit seine Offsetspannung. Datenblätter geben das als __Betriebsspannungsunterdrückung__ an (englisch supply voltage rejection ratio, SVRR): beim Beispiel-OPV 96 dB, also 16 µV Offsetänderung je Volt, garantiert 50 µV/V. Sinkt die Versorgung langsam um 100 mV, etwa weil eine Batterie sich entlädt, verschiebt sich die Offsetspannung um 1,6 µV, mit der Rauschverstärkung 101 der Ausgang um 0,16 mV. Für Wechselspannungen auf der Versorgung gilt der Datenblattwert nicht: Die Unterdrückung nimmt wie die Gleichtaktunterdrückung mit der Frequenz ab, bei vielen OPVs schon ab der Eckfrequenz der Leerlaufverstärkung. Brummen wird deshalb weit schlechter unterdrückt, und man blockt jede Versorgung direkt am OPV mit einem Kondensator ab.

## Frequenzgang und Verstärkungs-Bandbreite-Produkt

*Bis zu welcher Frequenz hält eine gegengekoppelte Schaltung ihre Verstärkung, und warum hängt diese Grenze von der Verstärkung ab?*

:::grafik
Szene: get1/operationsverstaerker/03-frequenzgang · Vorlage: kennlinie-loglog
**Abbildung 7:** Verstärkung über der Frequenz von 1 Hz bis 10 MHz, beide Achsen logarithmisch. Die Leerlaufverstärkung des Beispiel-OPV liegt bei tiefen Frequenzen bei 200 000, ist bei der Eckfrequenz 5 Hz auf das 0,707-fache gefallen und fällt darüber um den Faktor 10 je Dekade, durch 1000 bei 1 kHz und 1 bei 1 MHz. Dazu die Verstärkung gegengekoppelter Schaltungen mit der Rauschverstärkung 1, 10, 100 und 1000: waagrecht, bis sie die fallende Gerade bei 1 MHz, 100 kHz, 10 kHz und 1 kHz erreichen, dann mit ihr fallend; an jeder Ecke das 0,707-fache markiert. Der senkrechte Abstand zwischen der Kurve des OPV und der Schaltung ist die Schleifenverstärkung, beschriftet für die Rauschverstärkung 10 bei 1 kHz: 100. Wo der Abstand verschwindet, endet die Bandbreite.
:::

**Die Akteure:**

- __$f$__: Frequenz eines sinusförmigen Signals; in Hz.
- __$v_D(f)$__: Leerlaufverstärkung bei der Frequenz $f$, das Verhältnis der Amplituden von Ausgangs- und Differenzspannung; bei tiefen Frequenzen 200 000, bei der Eckfrequenz 5 Hz das 0,707-fache, 141 000, weit darüber $f_T/f$, also 1000 bei 1 kHz und 1 bei 1 MHz.
- __$f_T$__: Transitfrequenz, die Frequenz, bei der die Leerlaufverstärkung auf 1 gefallen ist; beim Beispiel-OPV 1 MHz ([Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html), Abschnitt *Warum die Schaltung zur Ruhe kommt*).
- __$\hat U_E$__, __$\hat U_A$__: Amplituden der Eingangs- und der Ausgangsspannung.
- __$f_g$__: __Grenzfrequenz__ der Schaltung, bei der ihre Verstärkung auf das 0,707-fache des Werts bei tiefen Frequenzen gefallen ist, um 3 dB.

**Das Zusammenspiel in Schritten** (nichtinvertierender Verstärker mit der Rauschverstärkung 10, Abbildung 7):

**Schritt 1**: Für Wechselspannungen verhält sich der OPV wie ein Integrator: Sein Ausgang ändert sich mit $\omega_T = 2\pi f_T$ mal der Differenzspannung. Für einen Sinus der Frequenz $f$ ist die Ausgangsamplitude deshalb das $f_T/f$-fache der Differenzamplitude. Oberhalb von 5 Hz, wo dieser Wert unter 200 000 sinkt, fällt die Leerlaufverstärkung um den Faktor 10 je Dekade; der Übergang ist gerundet, bei 5 Hz selbst sind es 141 000.

**Schritt 2**: Die Schleifenverstärkung $k\,v_D(f)$ fällt mit: bei 1 kHz 100, bei 10 kHz 10. In Abbildung 7 ist sie der senkrechte Abstand zwischen der Kurve des OPV und der Verstärkung der Schaltung.

**Schritt 3**: Solange sie groß gegen 1 ist, braucht der OPV nur eine kleine Differenzspannung, und die Schaltung verstärkt mit $1/k$ wie bei Gleichspannung.

**Schritt 4**: Bei der Frequenz $k f_T$, hier 100 kHz, ist die Schleifenverstärkung 1: Die Differenzspannung, die der OPV braucht, ist so groß wie das zurückgeführte Signal. Weil der integrierende OPV seinen Ausgang um eine Viertelperiode gegen die Differenzspannung verschiebt, addieren sich die beiden Amplituden wie die Seiten eines rechtwinkligen Dreiecks. Die Eingangsamplitude ist dann √2-mal so groß wie jede von ihnen, und die Verstärkung ist auf das 0,707-fache gefallen.

**Schritt 5**: Darüber folgt die Verstärkung der Schaltung der des OPV, $f_T/f$; mehr als der OPV allein kann die Schaltung nicht verstärken.

:::formel Formel
$$f_g = k\,f_T$$
$$\hat U_A = \frac{\hat U_E/k}{\sqrt{1 + (f/f_g)^2}}$$
:::

**So liest man das:** Die Bandbreite ist das Produkt aus Rückkopplungsfaktor und Transitfrequenz. Beim nichtinvertierenden Verstärker ist $1/k$ die Verstärkung, und Verstärkung mal Bandbreite ergibt $f_T$; daher der Name __Verstärkungs-Bandbreite-Produkt__. Je mehr Verstärkung man verlangt, desto früher endet die Bandbreite: Mit dem Beispiel-OPV reicht die Rauschverstärkung 10 bis 100 kHz, 101 bis 9,9 kHz. Beim invertierenden Verstärker zählt die Rauschverstärkung, nicht der Betrag der Verstärkung: Der Umkehrer mit −1 reicht bis 500 kHz, der Spannungsfolger bis 1 MHz. Die zweite Zeile der Formel gilt für den nichtinvertierenden Verstärker; beim invertierenden steht $R_2/R_1$ statt $1/k$ vor dem Bruch. Unterhalb der Grenzfrequenz ist der Abfall klein, bei einem Fünftel von ihr 2 %, bei einem Zehntel 0,5 %. Die Zeitkonstante von 1,59 µs, mit der dieselbe Schaltung nach einem Sprung einschwingt, ist dieselbe Eigenschaft im Zeitbereich (Herleitung, Proben).

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
**Gegeben:** Beispiel-OPV mit $f_T$ = 1 MHz; (a) eine invertierende Stufe mit $R_1$ = 1 kΩ und $R_2$ = 100 kΩ; (b) zwei invertierende Stufen hintereinander mit je $R_1$ = 10 kΩ und $R_2$ = 100 kΩ.

**Gesucht:** Grenzfrequenz und Betrag der Verstärkung bei 20 kHz.

**Rechnung:** (a) Rauschverstärkung 101:

$$f_g = \frac{1\ \mathrm{MHz}}{101} = 9{,}90\ \mathrm{kHz}$$

$$|A| = \frac{100}{\sqrt{1 + (20/9{,}90)^2}} = 44{,}4$$

(b) Je Stufe Rauschverstärkung 11:

$$f_g = \frac{1\ \mathrm{MHz}}{11} = 90{,}9\ \mathrm{kHz}$$

$$|A| = \Big(\frac{10}{\sqrt{1 + (20/90{,}9)^2}}\Big)^2 = 95{,}4$$

Zusammen fallen beide Stufen auf das 0,707-fache, wenn jede auf das 0,841-fache gefallen ist; das ist bei 0,644 mal 90,9 kHz der Fall, bei 58,5 kHz.

**Ergebnis:** **Einstufig bleibt bei 20 kHz nur der Betrag 44,4, zweistufig 95,4; die Grenzfrequenz steigt von 9,9 kHz auf 58,5 kHz.**

**Einordnung:** Die zweite Stufe kostet einen OPV, teilt aber die Verstärkung auf: Jede Stufe braucht nur ein Zehntel, und ihre Bandbreite ist gut neunmal so groß. Zwei invertierende Stufen kehren das Vorzeichen zweimal um; die Gesamtverstärkung ist +100.
::::

:::fehlvorstellung
„Der 741 hat eine Transitfrequenz von 1 MHz, also verstärkt er Signale bis 1 MHz.“ Das liegt nahe, weil Datenblätter die Transitfrequenz als Bandbreite angeben. Bei 1 MHz ist die Verstärkung des OPV aber schon auf 1 gefallen; nur ein Spannungsfolger erreicht diese Grenze. Jede Verstärkung kostet Bandbreite im selben Verhältnis: Mit der Rauschverstärkung 101 endet die Schaltung bei 9,9 kHz, mitten im Hörbereich.
:::

:::frage
„Das Datenblatt nennt für den Spannungsfolger 5 % Überschwingen. Woher kommt das, wenn das Modell keines kennt?“
Das Modell kennt nur eine Verzögerung, die des Kompensationskondensators. Ein realer OPV hat weitere, kleinere, denn jede Transistorstufe braucht Zeit, um ihre Kapazitäten umzuladen. Kommt die Korrektur der Gegenkopplung dadurch verspätet an, hat sich der Ausgang schon über das Ziel hinaus bewegt. Das wirkt nur, wenn die Schleife schnell ist, also bei großem $k$: Ein Modell mit einer zweiten Verzögerung bei 1,9 MHz gibt die 5 % des Spannungsfolgers wieder, und schon mit $k$ = 0,5 verschwindet das Überschwingen. Deshalb legt der Kompensationskondensator die erste Verzögerung so tief, auf 5 Hz, dass die Schleifenverstärkung selbst mit $k$ = 1 auf 1 gefallen ist, bevor die übrigen Verzögerungen wirken; der Preis ist die geringe Transitfrequenz. OPVs, die nur ab einer Mindestverstärkung stabil sind, sind schwächer kompensiert und dafür schneller.
:::

## Anstiegsgeschwindigkeit und Leistungsbandbreite

*Warum verzerrt ein Verstärker große Signale schon bei Frequenzen, die er klein noch sauber überträgt?*

:::grafik
Szene: get1/operationsverstaerker/03-anstieg · Vorlage: zeitverlauf
**Abbildung 8:** Zeitverläufe am nichtinvertierenden Verstärker mit der Rauschverstärkung 10 ($R_1$ = 10 kΩ, $R_2$ = 90 kΩ, Beispiel-OPV), je zwei Perioden. (a) Eingang 0,05 V bei 20 kHz: Ausgang ein Sinus mit 0,49 V Amplitude, gestrichelt der verlangte mit 0,5 V. (b) Eingang 1 V bei 5 kHz: Ausgang ein Sinus mit 9,99 V, größte Steigung 0,31 V/µs, unter der Grenze. (c) Eingang 1 V bei 20 kHz: Verlangt wären 10 V mit 1,26 V/µs Steigung; der Ausgang läuft mit 0,5 V/µs als Dreieck auf und ab und erreicht nur ±6,0 V, gestrichelt der verlangte Sinus. Die Bandbreite begrenzt kleine Signale, die Anstiegsgeschwindigkeit große.
:::

**Die Akteure:**

- __$\mathrm{SR}$__: Anstiegsgeschwindigkeit (englisch slew rate), die größte Änderungsgeschwindigkeit der Ausgangsspannung; beim Beispiel-OPV 0,5 V/µs. Sie entsteht, wenn die Eingangsstufe ganz auf eine Seite schaltet und den Kompensationskondensator mit ihrem vollen Strom lädt; zu 0,5 V/µs und 30 pF gehören rechnerisch 15 µA. Im Modell, in dem die Eingangsstufe bis zu diesem Strom linear arbeitet, geschieht das ab einer Differenzspannung von rund 80 mV; real geht sie allmählich in die Begrenzung über ([Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html), Abschnitt *Warum die Schaltung zur Ruhe kommt*).
- __$f_P$__: die höchste Frequenz, bis zu der ein Sinus mit der Amplitude $\hat U_A$ am Ausgang die Anstiegsgrenze nicht erreicht; für die volle Ausgangsamplitude heißt sie __Leistungsbandbreite__ (englisch full power bandwidth).

**Das Zusammenspiel in Schritten** (Rauschverstärkung 10, Abbildung 8):

**Schritt 1**: Ein Sinus ändert sich im Nulldurchgang am schnellsten, mit 2π mal Frequenz mal Amplitude: 10 V Amplitude bei 20 kHz verlangen 1,26 V/µs, bei 5 kHz 0,31 V/µs.

**Schritt 2**: Liegt das unter der Anstiegsgeschwindigkeit, folgt der Ausgang, und nur die Bandbreite begrenzt: 1 V am Eingang bei 5 kHz ergibt 9,99 V (Abbildung 8b).

**Schritt 3**: Liegt es darüber, bleibt der Ausgang hinter dem verlangten Verlauf zurück. Die Differenzspannung wächst, bis die Eingangsstufe ihren ganzen Strom liefert, im Modell ab 80 mV, und der Ausgang steigt nur noch mit 0,5 V/µs, auf einer Geraden.

**Schritt 4**: Er läuft weiter, bis der verlangte Verlauf ihn einholt, und kehrt dann um. Aus dem Sinus wird ein Dreieck, dessen Amplitude höchstens die Anstiegsgeschwindigkeit mal eine Viertelperiode ist, bei 20 kHz 6,25 V; die Simulation des Modells ergibt 6,0 V, weil die Spitzen abgerundet sind (Abbildung 8c).

**Schritt 5**: Ob die Bandbreite oder die Anstiegsgeschwindigkeit begrenzt, hängt von der Amplitude ab: Ein kleiner Sinus mit 0,5 V Ausgangsamplitude kommt bei 20 kHz mit 0,49 V an (Abbildung 8a). Mit der Rauschverstärkung 10 begrenzt bis 0,8 V Ausgangsamplitude die Bandbreite von 100 kHz, darüber die Anstiegsgeschwindigkeit.

:::formel Formel
$$f_P = \frac{\mathrm{SR}}{2\pi\,\hat U_A}$$
:::

**So liest man das:** Je größer die Amplitude, desto früher beginnt die Verzerrung: Mit dem Beispiel-OPV bleibt ein Sinus mit 1 V bis 79,6 kHz unverzerrt, mit 10 V nur bis 7,96 kHz und mit der vollen Aussteuerung von 14 V, der Leistungsbandbreite, bis 5,68 kHz. Für Audiosignale bis 20 kHz mit großer Amplitude ist der 741 damit zu langsam. Die Grenze hängt nicht von der Verstärkung der Schaltung ab, nur von der Amplitude am Ausgang; real setzt die Verzerrung allmählich ein, weil die Eingangsstufe nicht schlagartig in die Begrenzung geht.

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
**Gegeben:** nichtinvertierender Verstärker mit $R_1$ = 10 kΩ und $R_2$ = 90 kΩ; Beispiel-OPV mit $f_T$ = 1 MHz und 0,5 V/µs; Eingänge (a) 0,05 V bei 20 kHz, (b) 1 V bei 5 kHz, (c) 1 V bei 20 kHz.

**Gesucht:** ob der Ausgang unverzerrt bleibt, und seine Amplitude.

**Rechnung:** Verlangte größte Steigung bei 0,5 V, 10 V und 10 V Ausgangsamplitude:

$$\text{(a)}\quad 2\pi\cdot 20\ \mathrm{kHz}\cdot 0{,}5\ \mathrm{V} = 0{,}063\ \mathrm{V}/\mu\mathrm{s}$$

$$\text{(b)}\quad 2\pi\cdot 5\ \mathrm{kHz}\cdot 10\ \mathrm{V} = 0{,}314\ \mathrm{V}/\mu\mathrm{s}$$

$$\text{(c)}\quad 2\pi\cdot 20\ \mathrm{kHz}\cdot 10\ \mathrm{V} = 1{,}26\ \mathrm{V}/\mu\mathrm{s}$$

(a) und (b) liegen unter 0,5 V/µs; es bleibt der Abfall durch die Bandbreite von 100 kHz:

$$\frac{0{,}5\ \mathrm{V}}{\sqrt{1 + (20/100)^2}} = 0{,}490\ \mathrm{V}$$

$$\frac{10\ \mathrm{V}}{\sqrt{1 + (5/100)^2}} = 9{,}99\ \mathrm{V}$$

(c) liegt darüber; das Dreieck erreicht höchstens die Anstiegsgeschwindigkeit mal eine Viertelperiode:

$$0{,}5\ \mathrm{V}/\mu\mathrm{s}\cdot 12{,}5\ \mu\mathrm{s} = 6{,}25\ \mathrm{V}$$

Die Simulation des Modells ergibt 6,0 V.

**Ergebnis:** **(a) Sinus mit 0,49 V, (b) Sinus mit 9,99 V, (c) Dreieck mit 6,0 V statt 10 V.**

**Einordnung:** Bei 20 kHz überträgt dieselbe Schaltung ein kleines Signal mit 2 % Abfall, ein großes nur als Dreieck mit 60 % der Amplitude. Eine Angabe der Bandbreite allein sagt über große Signale nichts.
::::

## Alles hängt an einem Prinzip

| Einzel­heit | welche Seite des Prinzips sie zeigt |
|---|---|
| Verstärkungs­fehler, Schwankungen der Leerlauf­verstärkung | Fehler im Verstärker, durch die Schleifen­verstärkung geteilt |
| kleiner Aus­gangs-, großer Eingangs­widerstand | dieselbe Nachregelung, an Ausgang und Eingang |
| Offset­spannung beim invertierenden Verstärker | Fehler am Eingang, verstärkt mit der Rausch­verstärkung |
| Ruhe­ströme und Ausgleichs­widerstand | Ströme werden an Widerständen zu Eingangs­fehlern |
| Gleichtakt- und Betriebs­spannungs­unter­drückung | Einflüsse, die wie eine kleine Differenz­spannung wirken |
| Grenz­frequenz, Ausgangs­widerstand bei hohen Frequen­zen | die Schleifen­verstärkung fällt mit der Frequenz |
| Anstiegs­geschwindig­keit, Aussteuer­grenzen | Grenzen großer Signale, die keine Gegen­kopplung aufhebt |

Ein realer OPV ist ein idealer mit kleinen Fehlerquellen: Fehler im Verstärker teilt die Gegenkopplung durch die Schleifenverstärkung, Fehler an den Eingängen verstärkt sie wie ein Signal; weil die Schleifenverstärkung mit der Frequenz fällt, wirkt die Gegenkopplung nur bis zu einer Grenzfrequenz, und große Signale begrenzen zusätzlich Aussteuerbereich und Anstiegsgeschwindigkeit.

## Bedeutung und Ausblick

Aus dem Prinzip folgt, wie man einen OPV auswählt. Für kleine Gleichspannungen von Sensoren zählen Offsetspannung, Drift und Ruheströme; dafür gibt es Präzisions-OPVs mit Offsetspannungen im Mikrovoltbereich und OPVs mit Feldeffekttransistoren am Eingang, deren Ruheströme Pikoampere betragen. Für Audio- und Messsignale hoher Frequenz zählen Transitfrequenz und Anstiegsgeschwindigkeit, für Geräte mit kleiner Versorgungsspannung der Aussteuerbereich, den Rail-to-Rail-OPVs fast ganz nutzen. Ein Datenblatt nennt die meisten dieser Größen mit typischem und garantiertem Wert, manche nur typisch; für eine Schaltung, die mit jedem Exemplar funktionieren soll, rechnet man mit dem garantierten.

Bei Messungen zeigen sich die Abweichungen als Gleichspannung am Ausgang ohne Signal, als Brummen und als Dreieck statt Sinus bei hohen Frequenzen. Wie man die Offsetspannung genauer beschreibt und beseitigt, geht über den Rahmen dieses Artikels hinaus. Mit diesem Artikel endet die Reihe zum Operationsverstärker und damit der Teil über Halbleiterbauelemente; die Physik der Bauelemente vertiefen die Artikel über den [pn-Übergang unter Spannung](/wissen/elektrotechnik/4-semester/grundlagen-elektronischer-materialien-und-bauelemente/bauelemente/diode-pn-uebergang-spannung.html) und den [MOSFET](/wissen/elektrotechnik/4-semester/grundlagen-elektronischer-materialien-und-bauelemente/bauelemente/mosfet.html).

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
F: Warum ist der Verstärkungsfehler einer gegengekoppelten Schaltung umso größer, je größer ihre Verstärkung ist?
A: Weil der relative Fehler der Kehrwert der Schleifenverstärkung k·v_D ist und eine große Verstärkung ein kleines k bedeutet. Mit dem Beispiel-OPV sind es bei der Rauschverstärkung 10 0,005 %, bei 1001 0,5 %.
F: Warum wird die Offsetspannung beim invertierenden Verstärker mit 1 + R_2/R_1 verstärkt und nicht mit −R_2/R_1?
A: Weil sie vor dem Pluseingang sitzt; setzt man das Signal null, ist die Schaltung für sie ein nichtinvertierender Verstärker. Beim Umkehrer mit −1 erscheint 1 mV deshalb als 2 mV.
F: Stimmt es, dass ein OPV mit 1 MHz Transitfrequenz Signale bis 1 MHz verstärkt?
A: Nein. Bei 1 MHz ist seine Verstärkung auf 1 gefallen; eine Schaltung mit der Rauschverstärkung 1/k reicht nur bis k·f_T, mit 101 bis 9,9 kHz.
F: Warum endet die Bandbreite bei der Frequenz k·f_T?
A: Dort ist die Schleifenverstärkung auf 1 gefallen. Die Differenzspannung, die der integrierende OPV braucht, ist dann so groß wie das zurückgeführte Signal und um eine Viertelperiode verschoben; die Verstärkung sinkt auf das 0,707-fache.
F: Warum verzerrt der 741 einen Sinus mit 10 V Amplitude bei 20 kHz, obwohl die Schaltung mit der Rauschverstärkung 10 bis 100 kHz reicht?
A: Der Sinus verlangt im Nulldurchgang 1,26 V/µs, der 741 schafft 0,5 V/µs. Seine Eingangsstufe schaltet ganz um, und der Ausgang läuft als Dreieck mit rund 6 V Amplitude.
F: Stimmt es, dass am Spannungsfolger keine Gleichtaktspannung liegt?
A: Nein. Beide Eingänge liegen auf der Eingangsspannung; bei 10 V sind das 10 V Gleichtakt, die mit 95 dB wie 0,18 mV Differenzspannung wirken.
F: Wie groß muss der Ausgleichswiderstand am Pluseingang eines invertierenden Verstärkers mit 100 kΩ und 1 MΩ sein, und welcher Fehler bleibt?
A: R_3 = R_1 ∥ R_2 = 90,9 kΩ. Statt 80 mV bleibt der Offsetstrom mal R_2, beim Beispiel-OPV 20 mV.
F: Stimmt es, dass der Eingangsruhestrom durch den Eingangswiderstand von 2 MΩ fließt und bei kleiner Differenzspannung verschwindet?
A: Nein. Er ist der Basisstrom der Eingangstransistoren und fließt immer; der Eingangswiderstand beschreibt nur die Änderung mit der Differenzspannung, bei 25 µV 12,5 pA.
F: Welchen Messfehler in Kelvin verursacht 1 mV Offset an einem nichtinvertierenden Verstärker für ein Thermoelement Typ K mit 40,96 µV/K?
A: 1 mV durch 40,96 µV/K, also 24,4 K, unabhängig von der Verstärkung, weil der nichtinvertierende Verstärker Signal und Offset mit demselben Faktor 1/k verstärkt.
F: Warum macht die Gegenkopplung den Ausgangswiderstand klein, aber nicht die Offsetspannung?
A: Ein Spannungsabfall am Ausgangswiderstand ist eine Abweichung des Ausgangs, die über den Teiler zurückkommt und nachgeregelt wird, bis nur 1/(1 + k·v_D) bleibt. Die Offsetspannung sitzt am Eingang; der OPV kann sie vom Signal nicht unterscheiden und verstärkt sie mit 1/k.
:::
