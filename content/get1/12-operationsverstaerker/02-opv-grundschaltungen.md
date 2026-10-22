---
title: Die OPV-Grundschaltungen
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Operationsverstärker
order: 120500
summary: Wie man gegengekoppelte OPV-Schaltungen mit zwei Regeln berechnet und was jede Grundschaltung tut: invertierender und nichtinvertierender Verstärker, Impedanzwandler, Addierer und Subtrahierer, Integrator und Differenzierer, Logarithmierer, Exponentialschaltung und Multiplizierer, Transimpedanzverstärker, negativer Widerstand und hintereinandergeschaltete Stufen. Kompakte Fassung; die ausführliche enthält zusätzlich das Rechenschema als Bild, den Gleichtaktfehler des Subtrahierers, einen Digital-Analog-Umsetzer, das Schwingen des Differenzierers am realen OPV und die Stabilität des negativen Widerstands im Einzelnen.
tags: OPV, invertierender Verstärker, nichtinvertierender Verstärker, Spannungsfolger, Addierer, Subtrahierer, Integrator
stil: 3
fassung: kompakt
---

## Worum es geht

Ein Operationsverstärker allein kann nur vergleichen. Erst die Bauteile um ihn herum machen aus ihm einen Verstärker mit festgelegter Verstärkung, einen Addierer, einen Integrator oder einen Logarithmierer, und jede dieser Schaltungen folgt aus denselben zwei Regeln.

**Bei Gegenkopplung stellt sich der Ausgang des OPV so ein, dass zwischen seinen Eingängen keine Spannung liegt, und in die Eingänge des idealen OPV fließt kein Strom; aus diesen beiden Regeln und den Gleichungen der äußeren Bauteile folgt jede Grundschaltung, und welche Bauteile im Eingangs- und im Rückkopplungszweig sitzen, Widerstand, Kondensator oder Diode, bestimmt die Rechenoperation.**

Vorausgesetzt werden die goldenen Regeln aus [Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html), die Kirchhoffschen Gesetze ([Die Kirchhoffschen Gesetze](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/kirchhoffsche-gesetze.html)), die Kondensatorgleichung ([Laden und Entladen des Kondensators](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/laden-und-entladen.html)) und die Diodenkennlinie ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html)). Darauf baut [Der reale Operationsverstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/realer-operationsverstaerker.html) auf.

:::grafik
Szene: get1/operationsverstaerker/02-invertierer · Vorlage: schaltung-und-zeitverlauf
**Abbildung 1:** (a) Invertierender Verstärker nach Skript Bild 12.7 mit $R_1$ = 10 kΩ und $R_2$ = 20 kΩ an einer Eingangsspannung von 1 V: Pluseingang an Masse, Minuseingang auf 0 V (virtuelle Masse), ein Strom von 0,1 mA von der Quelle durch $R_1$ und weiter durch $R_2$ zum Ausgang, der Ausgang auf −2 V; der Strompfeil führt am OPV-Eingang vorbei. (b) Zeitverläufe bei sinusförmiger Eingangsspannung mit 5 V Amplitude: mit $R_2$ = 20 kΩ gegenphasig mit 10 V Amplitude; mit $R_2$ = 30 kΩ verlangt die Schaltung 15 V, der Ausgang bleibt bei ±14 V stehen und ist in 23 % jeder Periode abgeflacht. Der Strom durch $R_1$ muss durch $R_2$; deshalb bestimmt das Widerstandsverhältnis die Verstärkung, bis der Ausgang an seine Grenze stößt.
:::

## Das Rechenverfahren

*Wann darf man mit einer Differenzspannung von null rechnen?*

Für den idealen OPV gelten bei Gegenkopplung zwei Regeln ([Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html), Abschnitt *Die goldenen Regeln*): Die Differenzspannung $U_D$ zwischen den Eingängen ist null, und in die Eingänge fließt kein Strom. Die erste ist ein Ergebnis der Regelung und gilt nur, solange der Ausgang nicht an seiner Grenze liegt, beim Beispiel-OPV (Art 741 an ±15 V) bei ±14 V. Das Skript ordnet das in einem Schema (S. 214, Bild 12.22):

**Schritt 1**: Prüfen, ob der Ausgang auf den Minuseingang zurückwirkt (Gegenkopplung) oder auf den Pluseingang (Mitkopplung).

**Schritt 2**: Bei Gegenkopplung $U_D$ = 0 und stromlose Eingänge ansetzen und mit Ohmschem Gesetz und Kirchhoffschen Regeln rechnen.

**Schritt 3**: Probe: Liegt das Ergebnis außerhalb der Grenzen, liegt der Ausgang an der Grenze, und $U_D$ ist nicht null.

## Der invertierende Verstärker

*Warum liegt der Minuseingang auf 0 V, obwohl er nicht mit Masse verbunden ist?*

**Die Akteure:**

- __$U_E$__, __$U_A$__: Eingangs- und Ausgangsspannung gegen Masse; im Beispiel 1 V und −2 V.
- __$R_1$__: Widerstand zwischen Quelle und Minuseingang, 10 kΩ; __$R_2$__: Rückkopplungswiderstand vom Ausgang zum Minuseingang, 20 kΩ.
- __$A$__: Verstärkung der Schaltung, das Verhältnis von $U_A$ zu $U_E$.

**Das Zusammenspiel in Schritten** (Abbildung 1a):

**Schritt 1**: Der Pluseingang liegt an Masse; die Gegenkopplung über $R_2$ regelt $U_D$ auf null. Also liegt der Minuseingang auf 0 V, ohne mit Masse verbunden zu sein: Er ist __virtuelle Masse__.

**Schritt 2**: An $R_1$ liegt die ganze Eingangsspannung; es fließen $U_E/R_1$, bei 1 V 0,1 mA.

**Schritt 3**: In den OPV kann der Strom nicht; er fließt weiter durch $R_2$ zum Ausgang.

**Schritt 4**: Damit er durch $R_2$ von 0 V zum Ausgang fließt, muss der Ausgang um $R_2$ mal 0,1 mA tiefer liegen, auf −2 V. Der Ausgang nimmt den Strom auf, den die Quelle in die virtuelle Masse schiebt; deshalb kehrt sich das Vorzeichen um.

**Schritt 5**: Die Quelle sieht $R_1$ gegen 0 V: Der __Eingangswiderstand__ der Schaltung ist $R_1$.

:::formel Formel
$$A = \frac{U_A}{U_E} = -\frac{R_2}{R_1}$$
:::

**So liest man das:** Nur das Widerstandsverhältnis zählt, hier −2. Mit $R_2$ kleiner als $R_1$ schwächt die Schaltung ab. Mit der endlichen Leerlaufverstärkung des realen OPV (200 000) ergibt sich −1,99997, und der Minuseingang liegt auf 10 µV statt auf null.

Idee der Herleitung: Knotenregel am Minuseingang: Der Strom, der durch $R_1$ ankommt, muss durch $R_2$ weiter.

:::herleitung
**Ausgangspunkt:** die goldenen Regeln ([Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html)), die Knotenregel und das Ohmsche Gesetz.

**Annahmen:** (i) Gegenkopplung über $R_2$; der Ausgang liegt nicht an einer Grenze. (ii) Idealer OPV.

**Schritt 1**: Pluseingang an Masse und $U_D$ = 0: Der Minuseingang liegt auf 0 V.

**Schritt 2**: Strom durch $R_1$, von der Quelle zum Minuseingang:

$$I = \frac{U_E - 0}{R_1}$$

**Schritt 3** (entscheidender Schritt): Knotenregel am Minuseingang; in den OPV fließt nichts, also fließt derselbe Strom durch $R_2$ vom Minuseingang zum Ausgang:

$$\frac{U_E}{R_1} = \frac{0 - U_A}{R_2}$$

**Schritt 4**: Nach $U_A$ auflösen:

$$U_A = -\frac{R_2}{R_1}\,U_E$$

**Ergebnis:**

$$A = \frac{U_A}{U_E} = -\frac{R_2}{R_1}$$

**Woher die Faktoren kommen:** $R_1$ legt den Strom fest, $R_2$ macht aus ihm die Ausgangsspannung; das Minus entsteht, weil der Strom von der virtuellen Masse zum Ausgang fließt, also bergab.

**Proben:** Einheitenlos. Zahlenwert: −20 kΩ/10 kΩ = −2. Spezialfall $R_2 = R_1$: $A$ = −1, ein reiner Vorzeichenumkehrer. Grenzfall $R_2$ = 0: Der Ausgang ist mit dem Minuseingang verbunden und liegt auf 0 V.

**Grenzen:** Mit endlicher Leerlaufverstärkung weicht $A$ geringfügig ab (−1,99997 bei 200 000); liegt der Ausgang an einer Grenze, gilt die Rechnung nicht mehr.
:::

Wie weit die Schaltung aussteuern kann, zeigt Abbildung 1b mit 5 V Amplitude am Eingang (das Skript rechnet dasselbe mit ±10 V Grenzen, S. 203–205). Mit $A$ = −2 bleibt der Ausgang mit ±10 V innerhalb der ±14 V. Mit $A$ = −3 verlangt die Schaltung 15 V; der Ausgang bleibt in 23 % der Zeit bei ±14 V stehen, und unverzerrt sind nur Amplituden bis 4,67 V. In dieser Zeit gilt die erste Regel nicht: Im Scheitel liegt der Minuseingang auf 0,25 V.

::::beispiel Invertierender Verstärker mit 10 kΩ und 20 kΩ
**Gegeben:** $R_1$ = 10 kΩ, $R_2$ = 20 kΩ; 1 V am Eingang; Beispiel-OPV mit $v_D$ = 200 000 und ±14 V.

**Gesucht:** Strom, Ausgangsspannung, Spannung am Minuseingang und größte unverzerrte Eingangsamplitude.

**Rechnung:**

$$I = \frac{1\ \mathrm{V}}{10\ \mathrm{k}\Omega} = 0{,}1\ \mathrm{mA}$$

$$U_A = -\frac{20\ \mathrm{k}\Omega}{10\ \mathrm{k}\Omega}\cdot 1\ \mathrm{V} = -2\ \mathrm{V}$$

Am Minuseingang liegt die Differenzspannung, die der OPV für −2 V braucht:

$$\frac{2\ \mathrm{V}}{200\,000} = 10\ \mu\mathrm{V}$$

Unverzerrt bleiben Amplituden bis 14 V/2 = 7 V.

**Ergebnis:** **0,1 mA, −2 V, 10 µV am Minuseingang, bis 7 V Amplitude unverzerrt.**

**Einordnung:** 10 µV sind der 200 000ste Teil der Ausgangsspannung, genau $U_A/v_D$; deshalb darf man mit null rechnen.
::::

:::frage
„Der OPV-Eingang ist unendlich hochohmig. Warum belastet der invertierende Verstärker die Quelle trotzdem mit nur 10 kΩ?“
Die Quelle ist mit $R_1$ verbunden, und dessen anderes Ende liegt auf der virtuellen Masse, also auf 0 V. Für die Quelle ist das ein Widerstand von 10 kΩ gegen Masse; sie liefert 0,1 mA je Volt. Wer die Quelle nicht belasten will, nimmt den nichtinvertierenden Verstärker.
:::

**Mehrere Stufen hintereinander** (Skript S. 213–214, Bild 12.21). Der ideale OPV liefert an seinem Ausgang jeden Strom, ohne dass dessen Spannung nachgibt; eine nachfolgende Stufe belastet ihn nicht, und die Verstärkungen multiplizieren sich. Für zwei invertierende Stufen:

$$A = A_1\,A_2 = \Big(-\frac{R_2}{R_1}\Big)\Big(-\frac{R_4}{R_3}\Big) = \frac{R_2}{R_1}\cdot\frac{R_4}{R_3}$$

Mit −10 und −5 ergibt sich +50; 0,2 V werden zu 10 V. Bei 0,3 V verlangte die zweite Stufe 15 V und begrenzt.

Idee der Herleitung: Die erste Stufe liefert die Eingangsspannung der zweiten, gleich wie viel Strom diese aufnimmt.

:::herleitung
**Ausgangspunkt:** die Verstärkung des invertierenden Verstärkers (oben) und die Eigenschaft des idealen OPV, dass sein Ausgang jeden Strom liefert (Ausgangswiderstand null, Skript S. 198).

**Annahmen:** (i) Beide Stufen sind gegengekoppelt und nicht übersteuert. (ii) Ausgangswiderstand null.

**Schritt 1**: Die erste Stufe macht aus $U_E$ die Zwischenspannung; der Strom, den $R_3$ der zweiten Stufe zieht, ändert sie nicht:

$$U_{A1} = -\frac{R_2}{R_1}\,U_E$$

**Schritt 2** (entscheidender Schritt): Die zweite Stufe sieht $U_{A1}$ als ihre Eingangsspannung:

$$U_A = -\frac{R_4}{R_3}\,U_{A1}$$

**Ergebnis:**

$$U_A = \frac{R_2}{R_1}\cdot\frac{R_4}{R_3}\,U_E$$

**Woher die Faktoren kommen:** Jede Stufe steuert ihr Verhältnis bei; die Minuszeichen multiplizieren sich zu Plus.

**Proben:** (−10) · (−5) = 50; 0,2 V → 10 V. Grenzfall $R_4 = R_3$: Die zweite Stufe kehrt nur das Vorzeichen um.

**Grenzen:** Ein realer OPV hat einen kleinen Ausgangswiderstand; mit Gegenkopplung ist er so klein, dass die Belastung praktisch nicht zählt. Übersteuert eine Stufe, gilt das Produkt nicht mehr.
:::

## Der nichtinvertierende Verstärker und der Impedanzwandler

*Wie verstärkt man, ohne die Quelle zu belasten?*

:::grafik
Szene: get1/operationsverstaerker/02-nichtinvertierer · Vorlage: schaltung-zustaende
**Abbildung 2:** (a) Nichtinvertierender Verstärker nach Skript Bild 12.10 mit $R_1$ = 10 kΩ vom Minuseingang nach Masse und $R_2$ = 20 kΩ vom Ausgang zum Minuseingang; 1 V am Pluseingang, Minuseingang auf 1 V, 0,1 mA durch beide Widerstände, Ausgang auf 3 V. (b) Impedanzwandler nach Skript Bild 12.19: Ausgang direkt am Minuseingang, $U_A = U_E$. (c) Messung an einer Quelle von 5 V mit 100 kΩ Innenwiderstand: links ein Messgerät mit 1 MΩ direkt, Anzeige 4,545 V; rechts mit vorgeschaltetem Impedanzwandler, Anzeige 5,000 V. In den Pluseingang fließt kein Strom; die Quelle wird nicht belastet.
:::

Beim __nichtinvertierenden Verstärker__ (Skript S. 205, Bild 12.10) liegt die Eingangsspannung am Pluseingang; ein Teiler aus $R_2$ und $R_1$ führt einen Teil der Ausgangsspannung auf den Minuseingang. In den Pluseingang fließt kein Strom, die Quelle wird also nicht belastet. Wegen $U_D$ = 0 liegt der Minuseingang auf $U_E$; durch $R_1$ fließt $U_E/R_1$, und derselbe Strom kommt vom Ausgang durch $R_2$. Der Ausgang liegt deshalb noch um den Spannungsabfall an $R_2$ weiter von null entfernt als $U_E$ (Abbildung 2a):

:::formel Formel
$$A = \frac{U_A}{U_E} = 1 + \frac{R_2}{R_1}$$
:::

**So liest man das:** Die Verstärkung ist positiv und mindestens 1 (Skript Gl. 12.5); mit denselben Widerständen wie oben ergibt sich +3 statt −2.

**Kurz gesagt:** Mit idealem OPV macht der nichtinvertierende Verstärker genau rückgängig, was sein Teiler tut: Seine Verstärkung ist der Kehrwert des Anteils, den der Teiler von der Ausgangsspannung an den Minuseingang zurückgibt, solange der Ausgang nicht an einer Grenze liegt.

Idee der Herleitung: Der unbelastete Teiler setzt den Minuseingang auf einen festen Anteil der Ausgangsspannung, und die erste Regel verlangt, dass dieser Anteil gleich $U_E$ ist.

:::herleitung
**Ausgangspunkt:** die goldenen Regeln und die Spannungsteilerregel ([Zusammenschaltung von Widerständen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/zusammenschaltung-von-widerstaenden.html)).

**Annahmen:** (i) Gegenkopplung über den Teiler, Ausgang nicht an einer Grenze. (ii) Kein Strom in den Minuseingang; der Teiler ist unbelastet.

**Schritt 1**: Spannungsteiler: Der Minuseingang liegt auf dem Anteil $R_1/(R_1 + R_2)$ der Ausgangsspannung:

$$U_{e-} = \frac{R_1}{R_1 + R_2}\,U_A$$

**Schritt 2** (entscheidender Schritt): $U_D$ = 0 verlangt, dass der Minuseingang auf der Spannung des Pluseingangs liegt:

$$\frac{R_1}{R_1 + R_2}\,U_A = U_E$$

**Ergebnis:**

$$A = \frac{U_A}{U_E} = \frac{R_1 + R_2}{R_1} = 1 + \frac{R_2}{R_1}$$

**Woher die Faktoren kommen:** Die 1 steht für den Teil der Ausgangsspannung, der am Minuseingang ankommt und $U_E$ ausgleicht; $R_2/R_1$ für den Spannungsabfall an $R_2$, den derselbe Strom zusätzlich verursacht.

**Proben:** Einheitenlos. Zahlenwert: 1 + 20/10 = 3. Grenzfall $R_2$ = 0 oder $R_1$ unendlich: $A$ = 1, der Impedanzwandler.

**Grenzen:** Mit endlicher Leerlaufverstärkung 2,99996 statt 3. Die Eingangsspannung darf nicht so groß werden, dass der Ausgang die Grenze erreicht.
:::

Führt man den ganzen Ausgang zurück, entsteht der __Impedanzwandler__ oder __Spannungsfolger__ (Skript S. 210, Bild 12.19) mit der Verstärkung 1:

$$U_A = U_E$$

Er verstärkt nicht, aber er trennt: Er nimmt der Quelle keinen Strom ab und liefert der Last jeden Strom. Vor einem Spannungsmessgerät macht er dessen Innenwiderstand unschädlich ([Strom- und Spannungsmessung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strom-und-spannungsmessung/strom-und-spannungsmessung.html)).

::::beispiel Spannungsmessung an einer hochohmigen Quelle
**Gegeben:** Quelle mit 5 V und 100 kΩ Innenwiderstand; Messgerät mit 1 MΩ; Impedanzwandler mit dem Beispiel-OPV, dessen Eingang 80 nA Ruhestrom aufnimmt.

**Gesucht:** die Anzeige direkt und mit Impedanzwandler.

**Rechnung:** Direkt bilden Innenwiderstand und Messgerät einen Spannungsteiler:

$$U = 5\ \mathrm{V}\cdot\frac{1\ \mathrm{M}\Omega}{1{,}1\ \mathrm{M}\Omega} = 4{,}545\ \mathrm{V}$$

Mit Impedanzwandler fließt nur der Ruhestrom durch den Innenwiderstand: 80 nA mal 100 kΩ sind 8 mV, die Anzeige ist 4,992 V; mit idealem OPV 5,000 V.

**Ergebnis:** **4,545 V direkt (−9,1 %), 4,992 V mit dem 741 als Impedanzwandler (−0,16 %).**

**Einordnung:** Der Fehler sinkt auf ein 57stel; was übrig bleibt, sind Eingangsruhestrom und Offsetspannung des realen OPV.
::::

## Addierer und Subtrahierer

*Wie verrechnet ein OPV mehrere Spannungen?*

:::grafik
Szene: get1/operationsverstaerker/02-addierer-subtrahierer · Vorlage: schaltung-zustaende
**Abbildung 3:** (a) Addierer nach Skript Bild 12.11 mit drei Eingängen über $R_1$ = 10 kΩ, $R_2$ = 20 kΩ und $R_3$ = 40 kΩ an der virtuellen Masse, Rückkopplung $R_4$ = 10 kΩ; an den Eingängen 5 V, 0 V und 5 V (Code 101): Ströme 0,5 mA, 0 und 0,125 mA, zusammen 0,625 mA durch $R_4$, Ausgang −6,25 V. (b) Subtrahierer nach Skript Bild 12.12 mit $R_1$ = $R_3$ = 10 kΩ und $R_2$ = $R_4$ = 100 kΩ; $U_{E1}$ = 2,500 V, $U_{E2}$ = 2,505 V, beide Eingänge auf 2,2773 V, Ausgang 50 mV. An der virtuellen Masse addieren sich Ströme; der Subtrahierer verstärkt nur die Differenz, wenn die Widerstandsverhältnisse gleich sind.
:::

Schließt man an die virtuelle Masse mehrere Eingangswiderstände an, erhält man den __Addierer__ (Skript Bild 12.11, Abbildung 3a). Jede Quelle schiebt ihren eigenen Strom in den Knoten; keine stört die andere, weil er auf 0 V festgehalten wird. Alle Ströme zusammen fließen durch $R_4$ zum Ausgang. Mit den Eingangsspannungen __$U_1$__, __$U_2$__, __$U_3$__ an den Widerständen __$R_1$__, __$R_2$__, __$R_3$__:

:::formel Formel
$$U_A = -\Big(\frac{R_4}{R_1}\,U_1 + \frac{R_4}{R_2}\,U_2 + \frac{R_4}{R_3}\,U_3\Big)$$
:::

**So liest man das:** eine negative, gewichtete Summe; mit gleichen Widerständen die einfache Summe. Mit 10, 20 und 40 kΩ an 10 kΩ macht die Schaltung aus drei Bits eine Spannung, Code 101 an 5 V ergibt −6,25 V.

**Kurz gesagt:** Mit idealem OPV ist die Antwort des Addierers auf alle Eingänge zusammen die Summe seiner Antworten auf jeden Eingang allein, während die übrigen an Masse liegen; das gilt, solange der Ausgang nicht an einer Grenze liegt.

Idee der Herleitung: Knotenregel an der virtuellen Masse mit drei zufließenden Strömen.

:::herleitung
**Ausgangspunkt:** die goldenen Regeln, die Knotenregel und das Ohmsche Gesetz, wie beim invertierenden Verstärker.

**Annahmen:** (i) Gegenkopplung über $R_4$, Ausgang nicht an einer Grenze. (ii) Idealer OPV.

**Schritt 1**: Der Minuseingang liegt auf 0 V; durch jeden Eingangswiderstand fließt:

$$I_i = \frac{U_i}{R_i}$$

**Schritt 2** (entscheidender Schritt): Knotenregel; alle Ströme fließen durch $R_4$ weiter (Skript: $I_4 = I_1 + I_2 + I_3$):

$$\frac{U_1}{R_1} + \frac{U_2}{R_2} + \frac{U_3}{R_3} = \frac{0 - U_A}{R_4}$$

**Ergebnis:**

$$U_A = -\Big(\frac{R_4}{R_1}\,U_1 + \frac{R_4}{R_2}\,U_2 + \frac{R_4}{R_3}\,U_3\Big)$$

**Woher die Faktoren kommen:** Jeder Eingangswiderstand bestimmt, wie viel Strom seine Quelle beisteuert, $R_4$ macht aus der Summe die Spannung.

**Proben:** Mit nur einem Eingang ergibt sich der invertierende Verstärker. Zahlenwert: Code 101 mit 5 V ergibt −(5 V + 1,25 V) = −6,25 V.

**Grenzen:** Übersteigt die Summe die Aussteuergrenze, begrenzt der Ausgang.
:::

Beim __Subtrahierer__ (Skript Bild 12.12, Abbildung 3b) liegt __$U_{E1}$__ über $R_1$ am Minuseingang, __$U_{E2}$__ über den Teiler aus $R_3$ und $R_4$ am Pluseingang. Das Skript rechnet mit dem Überlagerungsprinzip: Für $U_{E1}$ allein ist die Schaltung ein invertierender Verstärker, für $U_{E2}$ allein ein nichtinvertierender hinter einem Spannungsteiler.

:::formel Formel
$$U_A = \frac{R_1 + R_2}{R_1}\cdot\frac{R_4}{R_3 + R_4}\,U_{E2} - \frac{R_2}{R_1}\,U_{E1}$$
$$U_A = \frac{R_2}{R_1}\,(U_{E2} - U_{E1})$$
:::

**So liest man das:** Die zweite Zeile (Gl. 12.7) gilt nur, wenn $R_4/R_3$ gleich $R_2/R_1$ ist, etwa mit $R_3$ gleich $R_1$ und $R_4$ gleich $R_2$; dann bleibt allein die Differenz. Mit 10 kΩ und 100 kΩ werden aus 2,505 V gegen 2,500 V am Ausgang 50 mV, die gemeinsamen 2,5 V verschwinden. Im Zwischenschritt des Skripts steht $R_3$ statt $R_4$ im Zähler des Teilers (S. 207), und im Abschnitt 12.8 steht im Endergebnis derselben Schaltung in einem Nenner $R_3$, wo $R_1$ stehen müsste (S. 213); richtig ist die erste Zeile oben.

Idee der Herleitung: Überlagerung der beiden Eingänge, jeder einzeln als invertierender bzw. nichtinvertierender Verstärker.

:::herleitung
**Ausgangspunkt:** das Überlagerungsprinzip für lineare Netze und die beiden Verstärkerformeln dieses Artikels.

**Annahmen:** (i) Gegenkopplung über $R_2$, Ausgang nicht an einer Grenze. (ii) Idealer OPV; in den Pluseingang fließt kein Strom, der Teiler $R_3$, $R_4$ ist unbelastet.

**Schritt 1**: Nur $U_{E1}$, $U_{E2}$ kurzgeschlossen: Durch $R_3$ und $R_4$ fließt kein Strom, der Pluseingang liegt auf 0 V; invertierender Verstärker:

$$U_{A1} = -\frac{R_2}{R_1}\,U_{E1}$$

**Schritt 2**: Nur $U_{E2}$, $U_{E1}$ kurzgeschlossen: Der Pluseingang liegt auf der Spannung an $R_4$:

$$U_{e+} = \frac{R_4}{R_3 + R_4}\,U_{E2}$$

**Schritt 3** (entscheidender Schritt): Für diese Spannung ist die Schaltung ein nichtinvertierender Verstärker, denn $R_1$ liegt jetzt am kurzgeschlossenen Eingang, also an Masse:

$$U_{A2} = \Big(1 + \frac{R_2}{R_1}\Big)\,\frac{R_4}{R_3 + R_4}\,U_{E2}$$

**Schritt 4**: Überlagern:

$$U_A = U_{A1} + U_{A2}$$

**Ergebnis:**

$$U_A = \frac{R_1 + R_2}{R_1}\cdot\frac{R_4}{R_3 + R_4}\,U_{E2} - \frac{R_2}{R_1}\,U_{E1}$$

Ist $R_4/R_3$ gleich $R_2/R_1$, etwa mit $R_3$ gleich $R_1$ und $R_4$ gleich $R_2$, wird der erste Faktor

$$\frac{R_1 + R_2}{R_1}\cdot\frac{R_4}{R_3 + R_4} = \Big(1 + \frac{R_2}{R_1}\Big)\cdot\frac{R_2/R_1}{1 + R_2/R_1} = \frac{R_2}{R_1}$$

und es bleibt die Differenz, verstärkt um $R_2/R_1$.

**Zweiter Weg** (Skript 12.8, S. 213, über die Potentiale): Der Pluseingang liegt auf dem Teilerwert, und wegen $U_D$ = 0 liegt der Minuseingang ebenso:

$$U_{e-} = U_{e+} = \frac{R_4}{R_3 + R_4}\,U_{E2}$$

Durch $R_1$ fließt der Strom $(U_{E1} - U_{e-})/R_1$, und derselbe Strom fließt weiter durch $R_2$ zum Ausgang:

$$U_A = U_{e-} - R_2\,\frac{U_{E1} - U_{e-}}{R_1} = \frac{R_1 + R_2}{R_1}\,U_{e-} - \frac{R_2}{R_1}\,U_{E1}$$

Mit $U_{e-}$ eingesetzt ist das dasselbe Ergebnis.

**Woher die Faktoren kommen:** $R_2/R_1$ ist die invertierende Verstärkung für $U_{E1}$; der Teiler $R_4/(R_3 + R_4)$ und die nichtinvertierende Verstärkung $1 + R_2/R_1$ zusammen sind die Verstärkung für $U_{E2}$.

**Proben:** Gleiche Eingänge bei abgeglichenen Widerständen: $U_A$ = 0. Zahlenwert: 10 · 5 mV = 50 mV.

**Grenzen:** Weichen die Verhältnisse ab, geht auch die gemeinsame Spannung beider Eingänge zum Teil durch.
:::

## Integrator und Differenzierer

*Was geschieht, wenn im Rückkopplungsweg ein Kondensator sitzt?*

:::grafik
Szene: get1/operationsverstaerker/02-integrator · Vorlage: schaltung-und-zeitverlauf
**Abbildung 4:** (a) Integrator nach Skript Bild 12.13 mit $R$ = 10 kΩ und $C$ = 100 nF ($RC$ = 1 ms); darunter Eingang Rechteck ±1 V mit 1 kHz und Ausgang Dreieck mit 0,5 V Spitze-Spitze, gegenläufig: Während der Eingang +1 V hat, fällt der Ausgang mit 1 V je Millisekunde. (b) Differenzierer nach Skript Bild 12.14 mit denselben Bauteilen, vertauscht, mit idealem OPV; Eingang Dreieck ±1 V mit 1 kHz (Steigung ±4 V/ms), Ausgang Rechteck ∓4 V. Der Kondensator im Rückkopplungsweg integriert, am Eingang differenziert er.
:::

**Die Akteure:**

- __$u_E(t)$__, __$u_A(t)$__: Eingangs- und Ausgangsspannung als Funktionen der Zeit, klein geschrieben, weil sie sich ändern.
- __$R$__ = 10 kΩ am Eingang, __$C$__ = 100 nF im Rückkopplungsweg; __$RC$__ = 1 ms ist die Zeitkonstante.

**Das Zusammenspiel in Schritten** (Abbildung 4a):

**Schritt 1**: Der Minuseingang ist virtuelle Masse; durch $R$ fließt $u_E/R$, bei 1 V 0,1 mA.

**Schritt 2**: Der Strom kann nur in den Kondensator; dessen Spannung ändert sich mit Strom durch Kapazität, hier 1 V je Millisekunde.

**Schritt 3**: Die eine Seite des Kondensators liegt auf 0 V, die andere ist der Ausgang; der Ausgang fällt also mit 1 V/ms, solange 1 V anliegt, und erreicht nach 14 ms −14 V.

**Schritt 4**: Über die Zeit summiert sich das zum Integral: Ein Rechteck von ±1 V mit 1 kHz wird zu einem Dreieck, das je halbe Millisekunde um 0,5 V steigt oder fällt.

:::formel Formel
$$u_A(t) = -\frac{1}{RC}\int_0^t u_E(t')\,dt' + u_A(0)$$
:::

**So liest man das:** Der Ausgang ändert sich umso schneller, je größer die Eingangsspannung und je kleiner $RC$ ist; bei $u_E$ = 0 bleibt er stehen, weil der Kondensator seine Ladung hält. $u_A(0)$ ist die Ausgangsspannung zur Zeit null.

Idee der Herleitung: Der Strom aus der virtuellen Masse lädt den Kondensator; seine Spannung ist das Integral des Stroms.

:::herleitung
**Ausgangspunkt:** die Kondensatorgleichung ([Laden und Entladen des Kondensators](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/laden-und-entladen.html)) und die goldenen Regeln.

**Annahmen:** (i) Gegenkopplung über $C$, Ausgang nicht an einer Grenze. (ii) Idealer OPV, idealer Kondensator ohne Leckstrom.

**Schritt 1**: Virtuelle Masse; Strom durch $R$ zum Minuseingang:

$$i(t) = \frac{u_E(t)}{R}$$

**Schritt 2**: Kein Strom in den OPV: Derselbe Strom fließt durch $C$ vom Minuseingang zum Ausgang. Mit dem Zählpfeil der Kondensatorspannung in Stromrichtung ist sie die Spannung vom Minuseingang zum Ausgang:

$$u_C = 0 - u_A$$

**Schritt 3** (entscheidender Schritt): Kondensatorgleichung:

$$i = C\,\frac{du_C}{dt} = -C\,\frac{du_A}{dt}$$

$$\frac{du_A}{dt} = -\frac{u_E}{RC}$$

**Schritt 4**: Von 0 bis $t$ integrieren:

$$u_A(t) = -\frac{1}{RC}\int_0^t u_E(t')\,dt' + u_A(0)$$

**Woher die Faktoren kommen:** $1/R$ macht aus der Spannung den Strom, $1/C$ aus dem Strom die Spannungsänderung; das Minus kommt wie beim invertierenden Verstärker daher, dass der Strom von der virtuellen Masse zum Ausgang fließt.

**Proben:** Einheit: V·s/(Ω·F) = V, denn Ω·F = s. Zahlenwert: 1 V über 1 ms bei $RC$ = 1 ms ergibt −1 V. Grenzfall $u_E$ = 0: Der Ausgang bleibt stehen.

**Grenzen:** Jede noch so kleine Gleichspannung am Eingang treibt den Ausgang mit der Zeit an die Grenze.
:::

::::beispiel Integrator mit 10 kΩ und 100 nF
**Gegeben:** $R$ = 10 kΩ, $C$ = 100 nF, Ausgang anfangs 0 V, Grenzen ±14 V; (a) 1 V konstant; (b) Rechteck ±1 V mit 1 kHz.

**Gesucht:** Steigung, Zeit bis zur Grenze, Form beim Rechteck.

**Rechnung:** (a) $RC$ = 1 ms, also

$$\frac{du_A}{dt} = -\frac{1\ \mathrm{V}}{1\ \mathrm{ms}} = -1\ \frac{\mathrm{V}}{\mathrm{ms}}$$

bis −14 V nach 14 ms. (b) Je Halbperiode von 0,5 ms ändert sich der Ausgang um 1 V · 0,5 ms/1 ms = 0,5 V.

**Ergebnis:** **(a) −1 V/ms, Grenze nach 14 ms; (b) Dreieck mit 0,5 V Spitze-Spitze.**

**Einordnung:** Aus Rechtecken Dreiecke zu machen, ist die Grundlage vieler Signalgeneratoren.
::::

:::frage
„Läuft der Integrator nicht irgendwann weg?“
Doch, sobald am Eingang auch nur eine kleine Gleichspannung liegt. Schon die Offsetspannung des 741 von typisch 1 mV lässt den Ausgang um 1 V je Sekunde wandern; nach 14 s liegt er an der Grenze, und der Eingangsruhestrom von 80 nA wirkt ähnlich stark. Praktische Integratoren werden deshalb über einen Schalter entladen oder bekommen einen großen Widerstand parallel zum Kondensator; mit 1 MΩ bleiben aus dem Offset nur rund 0,1 V.
:::

Vertauscht man $R$ und $C$, entsteht der __Differenzierer__ (Skript Bild 12.14, Abbildung 4b): Am Kondensator liegt die ganze Eingangsspannung, sein Strom ist $C$ mal ihrer Änderungsgeschwindigkeit, und dieser Strom fließt durch $R$ zum Ausgang:

:::formel Formel
$$u_A(t) = -RC\,\frac{du_E}{dt}$$
:::

**So liest man das:** Der Ausgang zeigt, wie schnell sich der Eingang ändert: Ein Dreieck mit ±4 V/ms wird zu einem Rechteck von ∓4 V. Weil schnelle Änderungen am stärksten verstärkt werden, verstärkt der Differenzierer auch Rauschen stark.

**Kurz gesagt:** Ein Differenzierer hinter einem Integrator mit demselben $RC$ macht rückgängig, was der Integrator getan hat: Die beiden Minuszeichen heben sich auf, und am Ende steht wieder die Eingangsspannung. Das gilt mit idealen OPVs und Bauteilen, solange kein Ausgang an einer Grenze liegt; in umgekehrter Reihenfolge nur bis auf eine feste Spannung aus den Anfangswerten.

Idee der Herleitung: Der Kondensator sieht die ganze Eingangsspannung; sein Strom ist ihre Ableitung, mal $C$.

:::herleitung
**Ausgangspunkt:** die Kondensatorgleichung und die goldenen Regeln.

**Annahmen:** (i) Gegenkopplung über $R$, Ausgang nicht an einer Grenze. (ii) Idealer OPV und idealer Kondensator.

**Schritt 1**: Virtuelle Masse: Am Kondensator liegt die Eingangsspannung, und es fließt

$$i = C\,\frac{du_E}{dt}$$

**Schritt 2** (entscheidender Schritt): Der Strom fließt durch $R$ vom Minuseingang zum Ausgang:

$$u_A = 0 - R\,i$$

**Ergebnis:**

$$u_A(t) = -RC\,\frac{du_E}{dt}$$

**Woher die Faktoren kommen:** $C$ macht aus der Spannungsänderung den Strom, $R$ aus dem Strom die Ausgangsspannung.

**Proben:** Einheit: Ω·F·V/s = V. Zahlenwert: 1 ms · 4 V/ms = 4 V. Grenzfall konstanter Eingang: Ausgang null.

**Grenzen:** Sprünge am Eingang verlangten unendlich große Ausgangsspannungen; der Ausgang begrenzt. Hohe Frequenzen werden stark verstärkt, und mit einem realen OPV wird die Schaltung zu einem schwach gedämpften Schwingkreis: mit dem 741 (1 MHz) und diesen Bauteilen mit einer Resonanz bei 12,6 kHz und der Güte 79.
:::

## Logarithmierer, Exponentialfunktion und Multiplizierer

*Wie rechnet ein OPV mit Logarithmen?*

:::grafik
Szene: get1/operationsverstaerker/02-logarithmierer · Vorlage: kennlinie-semilog
**Abbildung 5:** (a) Logarithmierer nach Skript Bild 12.15 mit $R$ = 10 kΩ und der Beispieldiode im Rückkopplungsweg (Anode am Minuseingang); daneben die Exponentialschaltung nach Bild 12.16 mit der Diode am Eingang (Anode an $U_E$, Kathode am Minuseingang) und $R$ = 10 kΩ im Rückkopplungsweg. (b) $U_A$ des Logarithmierers über $U_E$ von 10 mV bis 10 V, $U_E$ logarithmisch: eine Gerade von −466 mV über −526 mV und −586 mV bis −645 mV, je Dekade 59,5 mV; gestrichelt die Kennlinie bei 310 K: steiler, 61,5 mV je Dekade, und um 27 mV (bei 10 mV) bis 21 mV (bei 10 V) höher, bei 1 V um 23 mV. Die Diode im Rückkopplungsweg macht aus dem Strom eine Spannung, die mit dem Logarithmus wächst.
:::

Mit einer Diode im Rückkopplungsweg (Skript Bild 12.15) muss der Eingangsstrom $U_E/R$ durch die Diode. Sie stellt ihre Spannung so ein, dass sie genau diesen Strom führt; da ihr Strom exponentiell mit der Spannung wächst ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html)), wächst ihre Spannung mit dem Logarithmus des Stroms. Der Ausgang liegt um diese Spannung unter der virtuellen Masse: der __Logarithmierer__.

**Die Akteure:**

- __$I_S$__: Sättigungsstrom der Diode, bei der Beispieldiode 1,457·10⁻¹⁴ A; __$U_T$__: Temperaturspannung, 25,85 mV.
- __$U_{Di}$__: Spannung an der Diode; das Skript schreibt $U_D$, das hier die Differenzspannung bezeichnet.

:::formel Formel
$$U_A = -U_T\,\ln\frac{U_E}{R\,I_S}$$
:::

**So liest man das:** Jede Zehnerpotenz am Eingang verschiebt den Ausgang um 59,5 mV: Mit 10 kΩ ergeben 10 mV −466 mV, 1 V −586 mV und 10 V −645 mV. Die Schaltung arbeitet nur mit positiven Eingängen, und sie hängt stark von der Temperatur ab: Bei 310 K statt 300 K liegt der Ausgang bei 1 V Eingang um 23 mV höher, als wäre der Eingang 2,5-mal kleiner. Praktische Logarithmierer verwenden Transistoren und gleichen die Temperatur eigens aus (Skript S. 209).

Idee der Herleitung: Die Diodenkennlinie wird nach der Spannung aufgelöst.

:::herleitung
**Ausgangspunkt:** die Diodenkennlinie aus [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html), mit der Diodenspannung $U_{Di}$, und die goldenen Regeln:

$$I = I_S\,\Big[\exp\Big(\frac{U_{Di}}{U_T}\Big) - 1\Big]$$

**Annahmen:** (i) $U_E$ positiv; die Diode leitet und schließt die Gegenkopplung. (ii) Der Strom ist groß gegen $I_S$, die −1 vernachlässigbar (bei 1 µA um den Faktor 7·10⁷). (iii) Ideale Diode ohne Rekombinationsstrom und Bahnwiderstand.

**Schritt 1**: Virtuelle Masse; der Eingangsstrom fließt durch die Diode:

$$I = \frac{U_E}{R}$$

**Schritt 2** (entscheidender Schritt): Die Kennlinie, nach der Spannung aufgelöst:

$$U_{Di} = U_T\,\ln\frac{I}{I_S} = U_T\,\ln\frac{U_E}{R\,I_S}$$

**Schritt 3**: Die Anode liegt auf der virtuellen Masse, die Kathode am Ausgang:

$$U_A = 0 - U_{Di}$$

**Ergebnis:**

$$U_A = -U_T\,\ln\frac{U_E}{R\,I_S}$$

**Woher die Faktoren kommen:** $U_T$ ist die Spannungsskala der Exponentialkennlinie; $R I_S$ ist die Eingangsspannung, bei der der Ausgang null wäre (bei 10 kΩ 0,15 nV, praktisch nie erreicht).

**Proben:** Einheit V. Zahlenwert: 1 V an 10 kΩ ergibt 100 µA; $U_T \ln(100\ \mathrm{µA}/1{,}457\cdot10^{-14}\ \mathrm{A})$ = 0,586 V, also $U_A$ = −0,586 V. Je Dekade $U_T \ln 10$ = 59,5 mV.

**Grenzen:** Die reale Beispieldiode weicht durch Rekombinationsstrom und Bahnwiderstand ab: zwischen 1 µA und 100 µA um weniger als 2 mV, bei 1 mA um 20 mV. Dazu kommt der Temperaturgang (Text).
:::

Vertauscht man Diode und Widerstand (Skript Bild 12.16), bestimmt die Eingangsspannung die Diodenspannung, und $R$ setzt den exponentiell wachsenden Strom in die Ausgangsspannung um:

$$U_A = -R\,I_S\,\exp\Big(\frac{U_E}{U_T}\Big)$$

Je 59,5 mV mehr am Eingang verzehnfachen den Ausgang; 0,60 V ergeben −1,75 V.

Idee der Herleitung: Die Diodenspannung ist die Eingangsspannung; ihr Strom fließt durch $R$.

:::herleitung
**Ausgangspunkt:** die Diodenkennlinie und die goldenen Regeln.

**Annahmen:** (i) $U_E$ positiv und groß gegen $U_T$, die −1 der Kennlinie vernachlässigbar. (ii) Ideale Diode, Ausgang nicht an einer Grenze.

**Schritt 1**: Die Kathode liegt auf der virtuellen Masse, also liegt an der Diode die Eingangsspannung:

$$I = I_S\,\exp\Big(\frac{U_E}{U_T}\Big)$$

**Schritt 2** (entscheidender Schritt): Der Strom fließt durch $R$ vom Minuseingang zum Ausgang:

$$U_A = 0 - R\,I$$

**Ergebnis:**

$$U_A = -R\,I_S\,\exp\Big(\frac{U_E}{U_T}\Big)$$

**Woher die Faktoren kommen:** Die Exponentialfunktion stammt aus der Diode, $R$ macht aus dem Strom die Spannung.

**Proben:** Zahlenwert bei 0,6 V: 10 kΩ · 1,457·10⁻¹⁴ A · exp(23,21) = 1,75 V. Bis auf die Vorzeichen ist sie die Umkehrung des Logarithmierers: Hängt man beide mit einem Umkehrer dazwischen hintereinander, ergibt sich $-U_E$.

**Grenzen:** Ab 0,654 V verlangte die Schaltung mehr als 14 V; dieselben Temperatureinflüsse wie beim Logarithmierer.
:::

Weil der Logarithmus eines Produkts die Summe der Logarithmen ist, lässt sich mit zwei Logarithmierern, einem Addierer und einer Exponentialschaltung multiplizieren (Skript S. 210, Bilder 12.17 und 12.18). Rechnet man die gezeichnete Schaltung durch, ergibt sich

$$U_A = -\frac{U_X\,U_Y}{R_L\,I_S}$$

ein Produkt, aber mit einem Maßstab, den das Skript offenlässt: Mit $R_L$ = 10 kΩ und der Beispieldiode verlangte 1 mV an beiden Eingängen −6862 V. Brauchbar wird die Schaltung erst, wenn der Addierer über einen Umkehrer den Logarithmus einer Referenzspannung abzieht; mit 10 V Referenz ergeben 2 V und 3 V dann −0,6 V.

Idee der Herleitung: Die Formeln der drei Stufen werden hintereinander eingesetzt; die Logarithmen addieren sich, die Exponentialfunktion hebt den Logarithmus auf.

:::herleitung
**Ausgangspunkt:** die Formeln für Logarithmierer, Addierer und Exponentialschaltung (oben).

**Annahmen:** (i) Gleiche Dioden und gleiche Widerstände $R_L$ in Logarithmierern und Exponentialschaltung; Addierer mit gleichen Widerständen, also Gewicht 1. (ii) $U_X$, $U_Y$ positiv; keine Stufe übersteuert.

**Schritt 1**: Die Logarithmierer liefern:

$$U_{LX} = -U_T\,\ln\frac{U_X}{R_L I_S}$$

$$U_{LY} = -U_T\,\ln\frac{U_Y}{R_L I_S}$$

**Schritt 2**: Der Addierer kehrt das Vorzeichen um und summiert; nach der Regel für die Summe zweier Logarithmen:

$$U_S = -(U_{LX} + U_{LY}) = U_T\,\ln\frac{U_X\,U_Y}{(R_L I_S)^2}$$

**Schritt 3** (entscheidender Schritt): Die Exponentialschaltung hebt den Logarithmus auf:

$$U_A = -R_L I_S\,\exp\Big(\frac{U_S}{U_T}\Big) = -R_L I_S\,\frac{U_X\,U_Y}{(R_L I_S)^2}$$

**Ergebnis:**

$$U_A = -\frac{U_X\,U_Y}{R_L\,I_S}$$

**Woher die Faktoren kommen:** Zweimal $R_L I_S$ steht im Logarithmus, einmal kommt es aus der Exponentialschaltung zurück; einer bleibt im Nenner. Zieht der Addierer über einen Umkehrer den Logarithmus von $U_{Ref}/(R_L I_S)$ ab, wird aus $R_L I_S$ im Nenner $U_{Ref}$.

**Proben:** Einheit: V²/(Ω·A) = V. Zahlenwert: 1 mV · 1 mV/(10 kΩ · 1,457·10⁻¹⁴ A) = 6862 V.

**Grenzen:** Nur positive Eingänge; Temperaturgang und Bauteilstreuung gehen ein, wenn die Dioden nicht gleich warm und gleich sind.
:::

## Transimpedanzverstärker und negativer Widerstand

*Wie misst ein OPV einen Strom, und wie macht er einen Widerstand negativ?*

:::grafik
Szene: get1/operationsverstaerker/02-transimpedanz-nic · Vorlage: schaltung-zustaende
**Abbildung 6:** (a) Transimpedanzverstärker nach Skript S. 212 mit $R$ = 100 kΩ; eine Fotodiode zwischen Masse und Minuseingang (Anode am Minuseingang, Kathode an Masse) liefert 1 µA Fotostrom in die virtuelle Masse, die Diode liegt auf 0 V, der Ausgang auf −0,1 V. (b) Konverter für negative Impedanzen (NIC) nach Skript S. 211: OPV mit $R$ = 10 kΩ vom Ausgang zum Pluseingang und $R$ = 10 kΩ vom Ausgang zum Minuseingang, $R_2$ = 10 kΩ vom Minuseingang nach Masse; der Pluseingang ist der Anschluss der Schaltung. Daran parallel eine Stromquelle 1 mA mit 10 kΩ Innenwiderstand und eine Last von 1 kΩ: ohne NIC 0,909 mA durch die Last, mit NIC 1,000 mA; Ausgang des OPV auf 2 V. Die virtuelle Masse misst Ströme ohne Spannungsabfall; der negative Widerstand hebt den Innenwiderstand der Quelle auf.
:::

Speist man einen Strom $I_E$ direkt in die virtuelle Masse, fließt er durch $R$ zum Ausgang: der __Transimpedanzverstärker__ (Skript S. 211–212, Abbildung 6a).

:::formel Formel
$$U_A = -I_E\,R$$
:::

**So liest man das:** $R$ ist der Umrechnungsfaktor von Strom in Spannung; mit 100 kΩ wird 1 µA zu −0,1 V. Die Quelle sieht 0 V; eine Fotodiode arbeitet so ohne Dunkelstrom, und gemessen wird beim idealen OPV nur ihr Fotostrom. Beim realen OPV fließt zusätzlich sein Eingangsruhestrom durch $R$.

Idee der Herleitung: Der Eingangsstrom kann nur durch $R$; die virtuelle Masse hält den Eingang auf null.

:::herleitung
**Ausgangspunkt:** die goldenen Regeln und das Ohmsche Gesetz.

**Annahmen:** (i) Gegenkopplung über $R$, Ausgang nicht an einer Grenze. (ii) Idealer OPV.

**Schritt 1** (entscheidender Schritt): Kein Strom in den OPV; der Eingangsstrom fließt ganz durch $R$ vom Minuseingang zum Ausgang.

**Schritt 2**: Der Minuseingang liegt auf 0 V:

$$U_A = 0 - R\,I_E$$

**Ergebnis:**

$$U_A = -I_E\,R$$

**Woher die Faktoren kommen:** Nur $R$ setzt Strom in Spannung um; das Minus kommt aus der Stromrichtung.

**Proben:** Einheit Ω·A = V. 1 µA · 100 kΩ = 0,1 V.

**Grenzen:** Ströme über 140 µA verlangten mehr als 14 V.
:::

Der __Konverter für negative Impedanzen__ (NIC, Skript S. 211, Abbildung 6b) hat zwei gleiche Widerstände $R$ vom Ausgang zu beiden Eingängen; der Pluseingang ist der Anschluss (Spannung $U_1$, Strom $I_1$ hinein), am Minuseingang liegt $R_2$ nach Masse (Spannung $U_2$, Strom $I_2$). Wegen der ersten Regel ist $U_1$ gleich $U_2$; vom Ausgang fließt deshalb in beide Knoten derselbe Strom. Am Minuseingang fließt er durch $R_2$, am Pluseingang aus dem Anschluss heraus:

:::formel Formel
$$R_E = \frac{U_1}{I_1} = -R_2$$
:::

**So liest man das:** Steigt die Spannung am Anschluss, fließt Strom heraus: Er verhält sich wie −10 kΩ. Parallel zu einer Stromquelle mit 10 kΩ Innenwiderstand hebt er diesen auf. Weil die Schaltung zugleich mitgekoppelt ist, gilt die erste Regel nur, solange der Widerstand am Pluseingang, Quelle und Last parallel, kleiner ist als $R_2$; das Skript setzt das stillschweigend voraus.

Idee der Herleitung: Gleiche Spannung an beiden Eingängen bedeutet gleiche Ströme in beiden Widerständen $R$; einer fließt hinein, einer heraus.

:::herleitung
**Ausgangspunkt:** die goldenen Regeln, Knotenregel und Ohmsches Gesetz; der Ausgang des OPV liegt auf $V_a$ (Bezeichnung wie im Skript).

**Annahmen:** (i) Die Gegenkopplung überwiegt (Bedingung unten); Ausgang nicht an einer Grenze. (ii) Idealer OPV, beide Widerstände $R$ gleich.

**Schritt 1**: Erste Regel:

$$U_1 = U_2$$

**Schritt 2**: Knotenregel am Minuseingang: Der Strom aus dem Widerstand $R$ zum Minuseingang fließt durch $R_2$:

$$I_2 = \frac{V_a - U_2}{R} = \frac{U_2}{R_2}$$

**Schritt 3** (entscheidender Schritt): Knotenregel am Pluseingang: Der Strom aus dem Widerstand $R$ zum Pluseingang, wegen $U_1 = U_2$ gleich groß, kann nicht in den OPV und verlässt den Knoten durch den Anschluss; der hineinfließende Strom $I_1$ ist deshalb sein Negatives:

$$I_1 = -\frac{V_a - U_1}{R} = -I_2$$

**Ergebnis:**

$$R_E = \frac{U_1}{I_1} = \frac{U_2}{-I_2} = -R_2$$

**Woher die Faktoren kommen:** Das Minus stammt aus der Gleichheit der Ströme in den beiden $R$: Was am Minuseingang in $R_2$ fließt, fließt am Pluseingang aus dem Anschluss.

**Proben:** Zahlenwerte mit 1 V am Anschluss: $I_2$ = 0,1 mA, $V_a$ = 1 V + 10 kΩ · 0,1 mA = 2 V, $I_1$ = −0,1 mA. Der Wert von $R$ fällt heraus.

**Grenzen:** Der OPV muss die Spannung $V_a$ liefern können; bei ±14 V ist bei 7 V am Anschluss Schluss.
:::

::::beispiel Stromquelle mit negativem Widerstand kompensiert
**Gegeben:** Stromquelle 1 mA mit 10 kΩ Innenwiderstand; NIC mit $R$ = $R_2$ = 10 kΩ parallel; Last 1 kΩ.

**Gesucht:** der Laststrom ohne und mit NIC.

**Rechnung:** Ohne NIC teilt sich der Strom:

$$I_L = 1\ \mathrm{mA}\cdot\frac{10\ \mathrm{k}\Omega}{11\ \mathrm{k}\Omega} = 0{,}909\ \mathrm{mA}$$

Mit NIC haben 10 kΩ und −10 kΩ parallel den Leitwert null; der ganze Strom fließt durch die Last, 1,000 mA. Der OPV-Ausgang liegt auf 2 V. Stabil ist die Schaltung, weil am Pluseingang 0,91 kΩ (Last parallel zu 10 kΩ) liegen, weniger als $R_2$.

**Ergebnis:** **0,909 mA ohne, 1,000 mA mit NIC.**

**Einordnung:** Aus der realen wird eine ideale Stromquelle, bis zu Lasten von 7 kΩ, bei denen der OPV-Ausgang 14 V erreicht.
::::

:::fehlvorstellung
„Ein negativer Widerstand müsste Energie aus dem Nichts liefern.“ Er gibt tatsächlich Leistung ab, bei 1 V am Anschluss 0,1 mW. Sie stammt aber aus der Versorgung des OPV: Der NIC ist eine aktive Schaltung, die einen Strom so steuert, als wäre der Widerstand negativ.
:::

## Alles hängt an einem Prinzip

| Schaltung | welche Seite des Prinzips sie zeigt |
|---|---|
| inver­tierender Verstärker, Addierer | Virtuelle Masse: Die Eingangsströme müssen durch den Rückkopplungs­widerstand. |
| nicht­invertierender Verstärker, Impedanz­wandler, Subtra­hierer | Die erste Regel zwingt den Minuseingang auf die Spannung des Pluseingangs. |
| Integrator, Differen­zierer | Im Rückweg integriert der Kondensator den Strom zur Spannung; am Eingang macht er aus der Änderung der Spannung einen Strom. |
| Logarith­mierer, Exponential­schaltung | Die Diode setzt Strom und Spannung exponentiell ineinander um. |
| Transimpedanz­verstärker, NIC | Strom wird zu Spannung; zusätzliche Mitkopplung kehrt das Vorzeichen eines Widerstands um. |

Bei Gegenkopplung stellt sich der Ausgang des OPV so ein, dass zwischen seinen Eingängen keine Spannung liegt, und in die Eingänge des idealen OPV fließt kein Strom; aus diesen beiden Regeln und den Gleichungen der äußeren Bauteile folgt jede Grundschaltung.

## Bedeutung und Ausblick

Diese Schaltungen stecken in Sensorverstärkern, aktiven Filtern, Reglern und Digital-Analog-Umsetzern. Alle Ergebnisse gelten für den idealen OPV; wie der reale sie verfälscht, zeigt [Der reale Operationsverstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/realer-operationsverstaerker.html).

**In der ausführlichen Fassung:** das Rechenschema als Bild, der invertierende Verstärker in der Begrenzung im Einzelnen und warum man die virtuelle Masse nicht mit Masse verbinden darf, warum der nichtinvertierende Verstärker nicht abschwächen kann, ein 3-Bit-Digital-Analog-Umsetzer, der Gleichtaktfehler des Subtrahierers bei ungleichen Widerständen, Rauschen und Schwingen am Differenzierer, Temperaturgang und Transistor im Logarithmierer, der Multiplizierer mit Referenz im Bild, die Fotodiode am Transimpedanzverstärker und die Stabilitätsbedingung des NIC mit Herleitung. [Zur ausführlichen Fassung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/opv-grundschaltungen-ausfuehrlich.html)

:::kern
- Rechenschema: Gegenkopplung prüfen, Übersteuerung prüfen, dann mit $U_D = 0$ und stromlosen Eingängen rechnen.
- Invertierender Verstärker: Der Minuseingang ist virtuelle Masse; $A = -R_2/R_1$, Eingangswiderstand $R_1$.
- Nichtinvertierender Verstärker: $A = 1 + R_2/R_1$, mindestens 1; der Impedanzwandler mit $A$ = 1 belastet die Quelle nicht.
- Addierer: Die Ströme summieren sich an der virtuellen Masse. Subtrahierer mit gleichen Verhältnissen: $U_A = (R_2/R_1)(U_{E2} - U_{E1})$.
- Integrator: $u_A = -\frac{1}{RC}\int u_E\,dt$; der Differenzierer kehrt das um und verstärkt hohe Frequenzen.
- Logarithmierer: 59,5 mV je Dekade; nur positive Eingänge, stark temperaturabhängig.
- Transimpedanzverstärker: $U_A = -I_E R$; der NIC erzeugt $-R_2$ und ist nur stabil, solange die Gegenkopplung überwiegt.
- Kaskaden: Die Verstärkungen multiplizieren sich, jede Stufe muss in ihren Grenzen bleiben.
:::

:::quiz
F: Warum liegt der Minuseingang des invertierenden Verstärkers auf 0 V, obwohl er nicht mit Masse verbunden ist?
A: Der Pluseingang liegt an Masse, und die Gegenkopplung über R_2 regelt die Differenzspannung auf null; der Ausgang stellt sich so ein, dass der Strom durch R_1 vollständig über R_2 abfließt.
F: Stimmt es, dass der Strom durch R_1 in den Minuseingang des OPV fließt?
A: Nein. In die Eingänge fließt kein Strom; er fließt weiter durch R_2 zum Ausgang, der ihn aufnimmt. Deshalb ist U_A = −R_2 I.
F: Ein invertierender Verstärker hat R_1 = 10 kΩ und R_2 = 30 kΩ. Bis zu welcher Eingangsamplitude bleibt der Ausgang des Beispiel-OPV unverzerrt?
A: Bis 14 V/3 = 4,67 V; darüber begrenzt der Ausgang bei ±14 V.
F: Wozu dient ein Impedanzwandler mit der Verstärkung 1?
A: Er nimmt der Quelle keinen Strom ab und liefert der Last jeden Strom; eine hochohmige Quelle wird nicht belastet (5 V an 100 kΩ: mit idealem OPV 5,000 V statt 4,545 V mit einem 1-MΩ-Messgerät).
F: Warum erzeugt ein Integrator aus einer konstanten Eingangsspannung eine Rampe?
A: Der konstante Strom U_E/R aus der virtuellen Masse lädt den Kondensator gleichmäßig; seine Spannung und damit der Ausgang ändern sich mit konstanter Geschwindigkeit U_E/(RC).
F: Stimmt es, dass ein negativer Widerstand Energie aus dem Nichts erzeugt?
A: Nein. Die Leistung, die er abgibt, stammt aus der Versorgung des OPV; er ist eine aktive Schaltung.
:::
