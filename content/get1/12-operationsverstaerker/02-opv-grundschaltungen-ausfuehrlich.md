---
title: Die OPV-Grundschaltungen
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Operationsverstärker
order: 120500
summary: Wie man gegengekoppelte OPV-Schaltungen mit zwei Regeln berechnet und was jede Grundschaltung tut: invertierender und nichtinvertierender Verstärker, Impedanzwandler, Addierer und Subtrahierer, Integrator und Differenzierer, Logarithmierer, Exponentialschaltung und Multiplizierer, Transimpedanzverstärker, negativer Widerstand und hintereinandergeschaltete Stufen. Ausführliche Fassung mit allen Herleitungen, Aussteuergrenzen, Eingangswiderständen, dem Gleichtaktfehler des Subtrahierers, dem Schwingen des Differenzierers am realen OPV, dem Temperaturgang des Logarithmierers und der Stabilität des negativen Widerstands.
tags: OPV, invertierender Verstärker, nichtinvertierender Verstärker, Spannungsfolger, Addierer, Subtrahierer, Integrator
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Ein Operationsverstärker allein kann nur vergleichen. Erst die Bauteile um ihn herum machen aus ihm einen Verstärker mit genau festgelegter Verstärkung, einen Addierer, einen Integrator oder einen Logarithmierer. Was die einzelne Schaltung tut, folgt jedes Mal aus denselben zwei Regeln.

**Bei Gegenkopplung stellt sich der Ausgang des OPV so ein, dass zwischen seinen Eingängen keine Spannung liegt, und in die Eingänge des idealen OPV fließt kein Strom; aus diesen beiden Regeln und den Gleichungen der äußeren Bauteile folgt jede Grundschaltung, und welche Bauteile im Eingangs- und im Rückkopplungszweig sitzen, Widerstand, Kondensator oder Diode, bestimmt die Rechenoperation.**

Vorausgesetzt werden die goldenen Regeln und die Gegenkopplung aus [Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html), die Kirchhoffschen Gesetze aus [Die Kirchhoffschen Gesetze](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/kirchhoffsche-gesetze.html), die Kondensatorgleichung aus [Laden und Entladen des Kondensators](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/laden-und-entladen.html) und die Diodenkennlinie aus [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html). Darauf baut [Der reale Operationsverstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/realer-operationsverstaerker.html) auf, der zeigt, wo die idealen Ergebnisse dieses Artikels abweichen.

:::grafik
Szene: get1/operationsverstaerker/02-invertierer · Vorlage: schaltung-und-zeitverlauf
**Abbildung 1:** (a) Invertierender Verstärker nach Skript Bild 12.7 mit $R_1$ = 10 kΩ und $R_2$ = 20 kΩ an einer Eingangsspannung von 1 V: Pluseingang an Masse, Minuseingang auf 0 V (virtuelle Masse), ein Strom von 0,1 mA von der Quelle durch $R_1$ und weiter durch $R_2$ zum Ausgang, der Ausgang auf −2 V; der Strompfeil führt am OPV-Eingang vorbei. (b) Zeitverläufe bei sinusförmiger Eingangsspannung mit 5 V Amplitude: mit $R_2$ = 20 kΩ gegenphasig mit 10 V Amplitude; mit $R_2$ = 30 kΩ verlangt die Schaltung 15 V, der Ausgang bleibt bei ±14 V stehen und ist in 23 % jeder Periode abgeflacht. Der Strom durch $R_1$ muss durch $R_2$; deshalb bestimmt das Widerstandsverhältnis die Verstärkung, bis der Ausgang an seine Grenze stößt.
:::

## Das Rechenverfahren

*Wie berechnet man eine OPV-Schaltung, und wann darf man mit einer Differenzspannung von null rechnen?*

Für den idealen OPV gelten bei Gegenkopplung zwei Regeln, hergeleitet in [Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html), Abschnitt *Die goldenen Regeln*: Zwischen den Eingängen liegt keine Spannung, die Differenzspannung $U_D$ ist null, und in die Eingänge fließt kein Strom. Die zweite Regel folgt aus dem unendlichen Eingangswiderstand. Die erste ist ein Ergebnis der Regelung: Der Ausgang verstellt sich so lange, bis $U_D$ verschwindet. Sie gilt deshalb nur, solange die Gegenkopplung wirkt und der Ausgang nicht an seiner Grenze liegt, beim Beispiel-OPV (Art 741 an ±15 V) bei ±14 V. Das Skript fasst das Vorgehen in einem Schema zusammen (S. 214, Bild 12.22), Abbildung 2.

:::grafik
Szene: get1/operationsverstaerker/02-rechenschema · Vorlage: ablaufdiagramm
**Abbildung 2:** Ablaufdiagramm nach Skript Bild 12.22. Start, dann die Frage „mit- oder gegengekoppelt?“. Mitgekoppelt: $U_D$ ist nicht null, der Ausgang liegt in der Regel an $U_{A,\min}$ oder $U_{A,\max}$. Gegengekoppelt: die Frage „übersteuert?“; ja: $U_D$ ist nicht null, der Ausgang liegt an einer Grenze; nein: $U_D$ = 0, der Ausgang liegt zwischen den Grenzen. Alle Zweige münden in „mit Ohmschem Gesetz und Kirchhoffschen Regeln rechnen“. Die Regel $U_D$ = 0 ist eine Folge der Gegenkopplung, keine Eigenschaft des Bauteils.
:::

**Schritt 1**: Prüfen, wohin der Ausgang zurückwirkt: auf den Minuseingang (Gegenkopplung) oder auf den Pluseingang (Mitkopplung).

**Schritt 2**: Bei Gegenkopplung annehmen, dass der Ausgang nicht an einer Grenze liegt; dann sind $U_D$ = 0 und die Eingänge stromlos.

**Schritt 3**: Mit Ohmschem Gesetz und Kirchhoffschen Regeln die Ausgangsspannung berechnen.

**Schritt 4**: Probe: Liegt das Ergebnis zwischen den Grenzen? Wenn nicht, war die Annahme falsch; der Ausgang liegt an der Grenze, und $U_D$ ist nicht null.

## Der invertierende Verstärker

*Warum liegt der Minuseingang auf 0 V, obwohl er nicht mit Masse verbunden ist, und was folgt daraus für die Verstärkung?*

**Die Akteure:**

- __$U_E$__, __$U_A$__: Eingangs- und Ausgangsspannung gegen Masse; im Beispiel 1 V und −2 V.
- __$R_1$__: Widerstand zwischen Quelle und Minuseingang, 10 kΩ; __$R_2$__: Rückkopplungswiderstand vom Ausgang zum Minuseingang, 20 kΩ.
- __$I$__: Strom durch $R_1$ und $R_2$; im Beispiel 0,1 mA.
- __$A$__: Verstärkung der Schaltung, das Verhältnis von $U_A$ zu $U_E$ (so im Skript).

**Das Zusammenspiel in Schritten** (Abbildung 1a, Skript Bild 12.7):

**Schritt 1**: Der Pluseingang liegt an Masse. Die Gegenkopplung über $R_2$ regelt $U_D$ auf null; also liegt auch der Minuseingang auf 0 V, ohne mit Masse verbunden zu sein. Man nennt ihn deshalb __virtuelle Masse__.

**Schritt 2**: An $R_1$ liegt die ganze Eingangsspannung. Es fließt der Strom $U_E/R_1$, bei 1 V und 10 kΩ 0,1 mA.

**Schritt 3**: In den OPV-Eingang kann dieser Strom nicht fließen; er fließt weiter durch $R_2$ zum Ausgang.

**Schritt 4**: Damit 0,1 mA durch $R_2$ vom Minuseingang auf 0 V zum Ausgang fließen, muss der Ausgang um $R_2 I$ tiefer liegen, auf −2 V. Der Ausgang nimmt also den Strom auf, den die Quelle in die virtuelle Masse schiebt; deshalb kehrt sich das Vorzeichen um.

**Schritt 5**: Die Quelle sieht $R_1$ gegen die virtuelle Masse: Der __Eingangswiderstand__ der Schaltung, das Verhältnis von Eingangsspannung zu Eingangsstrom, ist $R_1$, hier 10 kΩ.

:::formel Formel
$$A = \frac{U_A}{U_E} = -\frac{R_2}{R_1}$$
:::

**So liest man das:** Die Verstärkung hängt nur vom Widerstandsverhältnis ab, wie bei jeder Gegenkopplung; hier ist sie −2. Mit $R_2$ kleiner als $R_1$ schwächt die Schaltung ab, mit größerem verstärkt sie; das Minus kehrt das Vorzeichen um. Mit der endlichen Leerlaufverstärkung von 200 000 ergibt die vollständige Rechnung −1,99997, und der Minuseingang liegt nicht genau auf null, sondern auf 10 µV.

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

Wie weit der Verstärker aussteuern kann, zeigt Abbildung 1b mit einer sinusförmigen Eingangsspannung von 5 V Amplitude; das Skript rechnet dasselbe mit Grenzen von ±10 V (S. 203–205, Bilder 12.8 und 12.9). Mit $A$ = −2 erreicht der Ausgang ±10 V und bleibt innerhalb der ±14 V des Beispiel-OPV. Mit $A$ = −3 verlangt die Schaltung 15 V; der Ausgang bleibt bei ±14 V stehen, in jeder Halbwelle von 69° bis 111°, also 23 % der Zeit. Unverzerrt verstärkt sie nur Amplituden bis 14 V/3 = 4,67 V. Während der Begrenzung gilt die erste Regel nicht: Im Scheitel liegt der Minuseingang auf 0,25 V statt auf null. Das Skript fasst die Bedingung in den Satz, die Versorgungsspannung sei dann kleiner als die größtmögliche Ausgangsspannung (S. 205); gemeint ist, dass die rechnerische Ausgangsspannung die Aussteuergrenze übersteigt, und die liegt etwas unter der Versorgung.

::::beispiel Invertierender Verstärker mit 10 kΩ und 20 kΩ
**Gegeben:** $R_1$ = 10 kΩ, $R_2$ = 20 kΩ; Eingangsspannung 1 V; Beispiel-OPV mit $v_D$ = 200 000 und den Grenzen ±14 V.

**Gesucht:** Strom, Ausgangsspannung, Spannung am Minuseingang, Eingangswiderstand und die größte unverzerrte Eingangsamplitude; dazu die Begrenzung mit $R_2$ = 30 kΩ bei 5 V Amplitude.

**Rechnung:**

$$I = \frac{1\ \mathrm{V}}{10\ \mathrm{k}\Omega} = 0{,}1\ \mathrm{mA}$$

$$U_A = -\frac{20\ \mathrm{k}\Omega}{10\ \mathrm{k}\Omega}\cdot 1\ \mathrm{V} = -2\ \mathrm{V}$$

Am Minuseingang liegt mit dem realen $v_D$ die Differenzspannung, die der OPV für −2 V braucht:

$$\frac{2\ \mathrm{V}}{200\,000} = 10\ \mu\mathrm{V}$$

Der Eingangswiderstand ist $R_1$ = 10 kΩ. Unverzerrt bleiben Eingangsamplituden bis 14 V/2 = 7 V. Mit $R_2$ = 30 kΩ und 5 V Amplitude verlangt die Schaltung 15 V; der Ausgang begrenzt, solange

$$15\ \mathrm{V}\cdot|\sin\varphi| > 14\ \mathrm{V}$$

also von 69,0° bis 111,0° jeder Halbwelle, 42° von 180° oder 23,4 % der Zeit.

**Ergebnis:** **0,1 mA, −2 V, 10 µV am Minuseingang, 10 kΩ Eingangswiderstand, bis 7 V Amplitude unverzerrt; mit −3 begrenzt der Ausgang 23 % der Zeit.**

**Einordnung:** 10 µV sind der 200 000ste Teil der Ausgangsspannung, genau $U_A/v_D$; deshalb darf man mit null rechnen. In der Begrenzung steigt die Spannung am Minuseingang dagegen auf 0,25 V, 25 000-mal mehr: Dann ist der Minuseingang keine virtuelle Masse mehr.
::::

:::frage
„Der Eingang des OPV ist unendlich hochohmig. Warum belastet der invertierende Verstärker die Quelle trotzdem mit nur 10 kΩ?“
Die Quelle ist nicht mit dem OPV-Eingang verbunden, sondern mit $R_1$, und dessen anderes Ende liegt auf der virtuellen Masse, also auf 0 V. Für die Quelle ist das dasselbe wie ein Widerstand von 10 kΩ gegen Masse: Sie liefert 0,1 mA je Volt. Wer die Quelle nicht belasten will, nimmt den nichtinvertierenden Verstärker (nächster Abschnitt) oder macht $R_1$ groß; bei gleicher Verstärkung wird dann auch $R_2$ groß.
:::

:::fehlvorstellung
„Wenn der Minuseingang ohnehin auf 0 V liegt, kann man ihn auch gleich mit Masse verbinden.“ Das liegt nahe, weil die Spannung dieselbe ist. Verbindet man ihn aber, fließt der Strom aus $R_1$ nach Masse ab statt durch $R_2$, und der OPV arbeitet ohne Rückführung: Schon seine Offsetspannung treibt den Ausgang an eine Grenze ([Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html), Abschnitt *Der ideale Operationsverstärker*). Die virtuelle Masse entsteht erst dadurch, dass der Ausgang den Strom durch $R_2$ abnimmt; sie ist ein Ergebnis der Regelung, kein Anschluss.
:::

**Mehrere Stufen hintereinander** (Skript S. 213–214, Bild 12.21). Der ideale OPV liefert an seinem Ausgang jeden Strom, ohne dass dessen Spannung nachgibt. Eine nachfolgende Stufe belastet ihn deshalb nicht, und ihre Verstärkung multipliziert sich mit der der ersten. Zwei invertierende Stufen ergeben

$$A = A_1\,A_2 = \Big(-\frac{R_2}{R_1}\Big)\Big(-\frac{R_4}{R_3}\Big) = \frac{R_2}{R_1}\cdot\frac{R_4}{R_3}$$

Die beiden Minuszeichen heben sich auf. Mit −10 und −5 ist die Gesamtverstärkung +50: 0,2 V am Eingang ergeben −2 V zwischen den Stufen und +10 V am Ausgang. Bei 0,3 V verlangte die zweite Stufe 15 V und begrenzt; jede Stufe muss für sich innerhalb ihrer Grenzen bleiben.

Idee der Herleitung: Die erste Stufe liefert die Eingangsspannung der zweiten, unabhängig davon, wie viel Strom die zweite aufnimmt.

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

*Wie verstärkt man, ohne die Quelle zu belasten, und wozu dient ein Verstärker mit der Verstärkung 1?*

:::grafik
Szene: get1/operationsverstaerker/02-nichtinvertierer · Vorlage: schaltung-zustaende
**Abbildung 3:** (a) Nichtinvertierender Verstärker nach Skript Bild 12.10 mit $R_1$ = 10 kΩ vom Minuseingang nach Masse und $R_2$ = 20 kΩ vom Ausgang zum Minuseingang; 1 V am Pluseingang, Minuseingang auf 1 V, 0,1 mA durch beide Widerstände, Ausgang auf 3 V. (b) Impedanzwandler nach Skript Bild 12.19: Ausgang direkt am Minuseingang, $U_A = U_E$. (c) Messung an einer Quelle von 5 V mit 100 kΩ Innenwiderstand: links ein Messgerät mit 1 MΩ direkt, Anzeige 4,545 V; rechts mit vorgeschaltetem Impedanzwandler, Anzeige 5,000 V. In den Pluseingang fließt kein Strom; die Quelle wird nicht belastet.
:::

Beim __nichtinvertierenden Verstärker__ (Skript S. 205, Bild 12.10) liegt die Eingangsspannung am Pluseingang, und ein Spannungsteiler aus $R_2$ (vom Ausgang) und $R_1$ (nach Masse) führt einen Teil der Ausgangsspannung auf den Minuseingang. Es ist die Grundschleife aus [Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html), Abschnitt *Rückkopplung: Gegen- und Mitkopplung*. Die Größen heißen wie beim invertierenden Verstärker.

**Das Zusammenspiel in Schritten** (Abbildung 3a):

**Schritt 1**: In den Pluseingang fließt kein Strom. Die Quelle gibt keine Leistung ab, gleich wie groß ihr Innenwiderstand ist.

**Schritt 2**: Wegen $U_D$ = 0 liegt der Minuseingang auf $U_E$, im Beispiel 1 V; durch $R_1$ fließen 0,1 mA nach Masse.

**Schritt 3**: Dieser Strom kommt vom Ausgang durch $R_2$; der Ausgang liegt deshalb um $R_2$ mal 0,1 mA über dem Minuseingang, auf 3 V.

**Schritt 4**: Mit denselben Widerständen wie beim invertierenden Verstärker ergibt sich +3 statt −2. Kleiner als 1 kann die Verstärkung nicht werden, denn der Ausgang muss um den Spannungsabfall an $R_2$ weiter von null entfernt liegen als $U_E$, damit durch $R_2$ der Strom fließt, den $R_1$ verlangt.

:::formel Formel
$$A = \frac{U_A}{U_E} = 1 + \frac{R_2}{R_1}$$
:::

**So liest man das:** Die Verstärkung ist positiv und mindestens 1 (Skript Gl. 12.5), hier 3; mit der endlichen Leerlaufverstärkung 2,99996. Je größer $R_2$ gegen $R_1$, desto größer die Verstärkung. Ohne $R_2$, wenn der Ausgang direkt mit dem Minuseingang verbunden ist, wird sie genau 1.

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

:::frage
„Kann der nichtinvertierende Verstärker auch abschwächen?“
Nein. Seine Verstärkung $1 + R_2/R_1$ ist mindestens 1: Der Minuseingang liegt auf $U_E$, und der Ausgang liegt noch um den Spannungsabfall an $R_2$ weiter von null entfernt. Zum Abschwächen setzt man einen Spannungsteiler vor einen Impedanzwandler oder nimmt den invertierenden Verstärker mit $R_2$ kleiner als $R_1$.
:::

Führt man den ganzen Ausgang zurück, ergibt sich der __Impedanzwandler__, auch __Spannungsfolger__ genannt (Skript S. 210, Bild 12.19, Abbildung 3b), mit der Verstärkung 1:

$$U_A = U_E$$

Das folgt aus der ersten Regel unmittelbar, denn der Minuseingang ist der Ausgang. Der Impedanzwandler verstärkt nicht, aber er trennt: Er nimmt der Quelle keinen Strom ab und liefert der Last jeden Strom, den sie braucht. Das Skript nennt das Spannungsmessgerät als Anwendung: Ein Messgerät mit endlichem Innenwiderstand belastet die Quelle und zeigt zu wenig an ([Strom- und Spannungsmessung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strom-und-spannungsmessung/strom-und-spannungsmessung.html)); mit vorgeschaltetem Impedanzwandler sieht die Quelle keinen Verbraucher mehr.

::::beispiel Spannungsmessung an einer hochohmigen Quelle
**Gegeben:** Quelle mit 5 V Leerlaufspannung und 100 kΩ Innenwiderstand; Messgerät mit 1 MΩ Innenwiderstand; Impedanzwandler mit dem Beispiel-OPV, dessen Eingang einen Ruhestrom von 80 nA aufnimmt.

**Gesucht:** die Anzeige direkt, mit realem und mit idealem Impedanzwandler.

**Rechnung:** Direkt bilden Innenwiderstand und Messgerät einen Spannungsteiler:

$$U = 5\ \mathrm{V}\cdot\frac{1\ \mathrm{M}\Omega}{1{,}1\ \mathrm{M}\Omega} = 4{,}545\ \mathrm{V}$$

Mit dem realen Impedanzwandler fließt nur der Ruhestrom durch den Innenwiderstand und senkt die Spannung um

$$80\ \mathrm{nA}\cdot 100\ \mathrm{k}\Omega = 8\ \mathrm{mV}$$

auf 4,992 V. Mit idealem Impedanzwandler fließt nichts, die Anzeige ist 5,000 V.

**Ergebnis:** **4,545 V direkt (−9,1 %), 4,992 V mit dem 741 als Impedanzwandler (−0,16 %), 5,000 V ideal.**

**Einordnung:** Der Impedanzwandler verkleinert den Messfehler um das 57-Fache. Was beim 741 übrig bleibt, sind sein Eingangsruhestrom und seine Offsetspannung von typisch 1 mV, zusammen 4,991 bis 4,993 V; OPVs mit Feldeffekttransistoren am Eingang nehmen nur Pikoampere auf ([Der reale Operationsverstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/realer-operationsverstaerker.html)).
::::

## Addierer und Subtrahierer

*Wie verrechnet ein OPV mehrere Spannungen miteinander?*

:::grafik
Szene: get1/operationsverstaerker/02-addierer-subtrahierer · Vorlage: schaltung-zustaende
**Abbildung 4:** (a) Addierer nach Skript Bild 12.11 mit drei Eingängen über $R_1$ = 10 kΩ, $R_2$ = 20 kΩ und $R_3$ = 40 kΩ an der virtuellen Masse, Rückkopplung $R_4$ = 10 kΩ; an den Eingängen 5 V, 0 V und 5 V (Code 101): Ströme 0,5 mA, 0 und 0,125 mA, zusammen 0,625 mA durch $R_4$, Ausgang −6,25 V. (b) Subtrahierer nach Skript Bild 12.12 mit $R_1$ = $R_3$ = 10 kΩ und $R_2$ = $R_4$ = 100 kΩ; $U_{E1}$ = 2,500 V, $U_{E2}$ = 2,505 V, beide Eingänge auf 2,2773 V, Ausgang 50 mV. An der virtuellen Masse addieren sich Ströme; der Subtrahierer verstärkt nur die Differenz, wenn die Widerstandsverhältnisse gleich sind.
:::

Schließt man an den Minuseingang des invertierenden Verstärkers mehrere Eingangswiderstände an, erhält man den __Addierer__ (Skript S. 205–206, Bild 12.11, Abbildung 4a). Jede Quelle schiebt ihren eigenen Strom in die virtuelle Masse. Dort stört keine die andere, weil der Knoten auf 0 V festgehalten wird, gleich wie viel Strom ankommt. Alle Ströme zusammen fließen durch den Rückkopplungswiderstand zum Ausgang.

**Die Akteure:**

- __$U_1$__, __$U_2$__, __$U_3$__: die Eingangsspannungen, gegen Masse.
- __$R_1$__, __$R_2$__, __$R_3$__: die zugehörigen Eingangswiderstände; __$R_4$__: der Rückkopplungswiderstand.

:::formel Formel
$$U_A = -\Big(\frac{R_4}{R_1}\,U_1 + \frac{R_4}{R_2}\,U_2 + \frac{R_4}{R_3}\,U_3\Big)$$
:::

**So liest man das:** Der Ausgang ist die negative, gewichtete Summe der Eingänge; jedes Gewicht ist ein Widerstandsverhältnis. Mit gleichen Widerständen wird es die einfache Summe, für weitere Eingänge setzt sich das Schema fort. Mit 10, 20 und 40 kΩ an 10 kΩ sind die Gewichte 1, 1/2 und 1/4: Die Schaltung macht aus drei Bits eine Spannung, ein einfacher Digital-Analog-Umsetzer.

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

::::beispiel Addierer als 3-Bit-Digital-Analog-Umsetzer
**Gegeben:** $R_4$ = 10 kΩ; Eingangswiderstände 10 kΩ (höchstwertiges Bit), 20 kΩ und 40 kΩ; jede Eingangsspannung ist 0 V (Bit 0) oder 5 V (Bit 1).

**Gesucht:** die Ausgangsspannung für alle Codes.

**Rechnung:** Die Gewichte sind 10/10 = 1, 10/20 = 0,5 und 10/40 = 0,25. Für den Code 101:

$$U_A = -(1\cdot 5\ \mathrm{V} + 0{,}5\cdot 0\ \mathrm{V} + 0{,}25\cdot 5\ \mathrm{V}) = -6{,}25\ \mathrm{V}$$

Die acht Codes von 000 bis 111 ergeben 0, −1,25, −2,5, … bis −8,75 V.

**Ergebnis:** **Stufen von 1,25 V; Code 101 ergibt −6,25 V.**

**Einordnung:** Die Stufe ist das Gewicht des niedrigsten Bits mal 5 V. Für viele Bits bräuchte man Widerstände über viele Zehnerpotenzen mit hoher Genauigkeit; praktische Umsetzer verwenden deshalb Netze aus nur zwei Widerstandswerten.
::::

Beim __Subtrahierer__ (Skript S. 206–207, Bild 12.12, Abbildung 4b) liegt $U_{E1}$ über $R_1$ am Minuseingang, der über $R_2$ gegengekoppelt ist, und $U_{E2}$ über den Teiler aus $R_3$ und $R_4$ am Pluseingang. Das Skript rechnet mit dem Überlagerungsprinzip ([Das Superpositionsverfahren](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/superpositionsverfahren.html)), das gilt, weil der ideale OPV in der Gegenkopplung linear arbeitet. Ist nur $U_{E1}$ da, fließt durch $R_3$ und $R_4$ kein Strom, der Pluseingang liegt auf 0 V, und es bleibt ein invertierender Verstärker. Ist nur $U_{E2}$ da, liegt der Pluseingang auf dem Teilerwert von $U_{E2}$, und die Schaltung verstärkt ihn nichtinvertierend.

**Die Akteure:**

- __$U_{E1}$__, __$U_{E2}$__: die beiden Eingangsspannungen; __$R_1$__ bis __$R_4$__ wie in Bild 12.12, $R_4$ vom Pluseingang nach Masse.

:::formel Formel
$$U_A = \frac{R_1 + R_2}{R_1}\cdot\frac{R_4}{R_3 + R_4}\,U_{E2} - \frac{R_2}{R_1}\,U_{E1}$$
$$U_A = \frac{R_2}{R_1}\,(U_{E2} - U_{E1})$$
:::

**So liest man das:** Die erste Zeile (Skript Gl. 12.6) gilt immer. Nur wenn $R_4/R_3$ gleich $R_2/R_1$ ist, etwa mit $R_3$ gleich $R_1$ und $R_4$ gleich $R_2$ wie im Skript, gehen beide Eingänge mit gleichem Faktor ein, und es bleibt die zweite Zeile (Gl. 12.7): die Differenz, verstärkt um $R_2/R_1$. Mit 10 kΩ und 100 kΩ werden aus 5 mV Differenz 50 mV, auch wenn beide Eingänge auf 2,5 V liegen.

Im Zwischenschritt schreibt das Skript für den Pluseingang $U_{E2}\,R_3/(R_3 + R_4)$ (S. 207); dort liegt aber die Spannung an $R_4$, wie Gl. 12.6 richtig enthält. Dieselbe Schaltung rechnet das Skript in Abschnitt 12.8 noch einmal über die Potentiale der Eingänge (S. 213, Bild 12.20; zweiter Weg im Herleitungskasten). Die vorletzte Zeile ist dort richtig, im Endergebnis steht aber in einem Nenner $R_3$, wo $R_1$ stehen müsste. Solange $R_3$ gleich $R_1$ ist, fällt das nicht auf; mit 1, 2, 3 und 4 kΩ ergibt die richtige Formel für $U_{E2}$ = 1 V und $U_{E1}$ = 0 (im Skript $U_2$ und $U_1$) 1,714 V, die des Skripts 0,571 V.

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

::::beispiel Subtrahierer an einer Messbrücke
**Gegeben:** $R_1$ = $R_3$ = 10 kΩ, $R_2$ = $R_4$ = 100 kΩ; $U_{E1}$ = 2,500 V, $U_{E2}$ = 2,505 V, wie an den beiden Abgriffen einer Messbrücke.

**Gesucht:** die Ausgangsspannung und die Spannung an den Eingängen des OPV.

**Rechnung:**

$$U_A = \frac{100\ \mathrm{k}\Omega}{10\ \mathrm{k}\Omega}\cdot(2{,}505\ \mathrm{V} - 2{,}500\ \mathrm{V}) = 50\ \mathrm{mV}$$

Beide OPV-Eingänge liegen auf dem Teilerwert:

$$U_{e+} = \frac{100}{110}\cdot 2{,}505\ \mathrm{V} = 2{,}2773\ \mathrm{V}$$

**Ergebnis:** **50 mV am Ausgang; die Eingänge des OPV liegen auf 2,2773 V.**

**Einordnung:** Die 2,5 V, die beide Brückenabgriffe gemeinsam haben, verschwinden; nur die 5 mV Unterschied werden verstärkt. Anders als beim invertierenden Verstärker liegt der Minuseingang hier nicht auf 0 V: Die erste Regel verlangt nur gleiche Spannungen an beiden Eingängen.
::::

:::frage
„Warum müssen beim Subtrahierer die Widerstandsverhältnisse so genau stimmen?“
Weil er die Differenz nur dann bildet, wenn beide Eingänge mit genau entgegengesetzt gleichen Faktoren eingehen. Mit $R_4$ = 101 kΩ statt 100 kΩ verstärkt die Schaltung auch eine gemeinsame Spannung beider Eingänge, um 0,009: Bei 2,5 V auf beiden Eingängen erscheinen 22,5 mV am Ausgang, fast halb so viel wie das Nutzsignal von 50 mV. Das Verhältnis von Differenz- zu Gleichtaktverstärkung, die Gleichtaktunterdrückung, ist dann 1110 oder 61 dB, mit 0,1 % Abweichung 81 dB. Deshalb nimmt man abgeglichene Widerstandsnetzwerke oder fertige Differenzverstärker-Bausteine mit integrierten Widerständen.
:::

## Integrator und Differenzierer

*Was geschieht, wenn im Rückkopplungsweg ein Kondensator sitzt?*

:::grafik
Szene: get1/operationsverstaerker/02-integrator · Vorlage: schaltung-und-zeitverlauf
**Abbildung 5:** (a) Integrator nach Skript Bild 12.13 mit $R$ = 10 kΩ und $C$ = 100 nF ($RC$ = 1 ms); darunter Eingang Rechteck ±1 V mit 1 kHz und Ausgang Dreieck mit 0,5 V Spitze-Spitze, gegenläufig: Während der Eingang +1 V hat, fällt der Ausgang mit 1 V je Millisekunde. (b) Differenzierer nach Skript Bild 12.14 mit denselben Bauteilen, vertauscht, mit idealem OPV; Eingang Dreieck ±1 V mit 1 kHz (Steigung ±4 V/ms), Ausgang Rechteck ∓4 V. Der Kondensator im Rückkopplungsweg integriert, am Eingang differenziert er.
:::

**Die Akteure:**

- __$u_E(t)$__, __$u_A(t)$__: Eingangs- und Ausgangsspannung als Funktionen der Zeit; klein geschrieben, weil sie sich ändern (das Skript schreibt sie groß).
- __$R$__: Eingangswiderstand, 10 kΩ; __$C$__: Kondensator im Rückkopplungsweg, 100 nF.
- __$RC$__: Zeitkonstante, 1 ms; sie legt fest, wie schnell sich der Ausgang je Volt Eingangsspannung ändert.

**Das Zusammenspiel in Schritten** (Abbildung 5a):

**Schritt 1**: Wie beim invertierenden Verstärker liegt der Minuseingang auf der virtuellen Masse; durch $R$ fließt $u_E/R$, bei 1 V 0,1 mA.

**Schritt 2**: Der Strom kann nur in den Kondensator. Dessen Spannung ändert sich mit der Geschwindigkeit Strom durch Kapazität ([Laden und Entladen des Kondensators](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/laden-und-entladen.html)), hier 1 V je Millisekunde.

**Schritt 3**: Die eine Seite des Kondensators liegt auf 0 V, die andere ist der Ausgang. Der Ausgang fällt also mit 1 V je Millisekunde, solange 1 V am Eingang liegt; nach 14 ms erreicht er −14 V.

**Schritt 4**: Über die Zeit summiert sich das: Die Ausgangsspannung ist das negative Integral der Eingangsspannung, geteilt durch $RC$. Ein Rechteck von ±1 V mit 1 kHz wird zu einem Dreieck, das in jeder halben Millisekunde um 0,5 V steigt oder fällt.

:::formel Formel
$$u_A(t) = -\frac{1}{RC}\int_0^t u_E(t')\,dt' + u_A(0)$$
:::

**So liest man das:** Der Ausgang ändert sich umso schneller, je größer die Eingangsspannung und je kleiner $RC$ ist; bei $u_E$ = 0 bleibt er stehen, weil der Kondensator seine Ladung hält. $u_A(0)$ ist die Ausgangsspannung zur Zeit null; sie entspricht der Ladung, die der Kondensator dann trägt.

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
**Gegeben:** $R$ = 10 kΩ, $C$ = 100 nF, Ausgang anfangs auf 0 V, Grenzen ±14 V; (a) konstant 1 V am Eingang; (b) Rechteck ±1 V mit 1 kHz.

**Gesucht:** die Steigung und die Zeit bis zur Grenze; die Form des Ausgangs beim Rechteck.

**Rechnung:** (a)

$$RC = 10\ \mathrm{k}\Omega\cdot 100\ \mathrm{nF} = 1\ \mathrm{ms}$$

$$\frac{du_A}{dt} = -\frac{1\ \mathrm{V}}{1\ \mathrm{ms}} = -1\ \frac{\mathrm{V}}{\mathrm{ms}}$$

Bis −14 V vergehen 14 ms. (b) Jede Halbperiode dauert 0,5 ms; in ihr ändert sich der Ausgang um

$$\frac{1\ \mathrm{V}\cdot 0{,}5\ \mathrm{ms}}{1\ \mathrm{ms}} = 0{,}5\ \mathrm{V}$$

abwechselnd nach unten und nach oben.

**Ergebnis:** **(a) −1 V/ms, −14 V nach 14 ms; (b) ein Dreieck mit 0,5 V Spitze-Spitze.**

**Einordnung:** Aus Rechtecken Dreiecke zu machen, ist die Grundlage vieler Signalgeneratoren. Die Rampe zeigt auch, warum ein Integrator ohne Gegenmaßnahme nicht lange in der Mitte bleibt.
::::

:::frage
„Läuft der Integrator nicht irgendwann weg?“
Doch, sobald am Eingang auch nur eine kleine Gleichspannung liegt oder ein kleiner Gleichstrom fließt. Schon die Offsetspannung des 741 von typisch 1 mV wirkt wie eine Eingangsspannung: Der Ausgang wandert um 1 V je Sekunde und liegt nach 14 s an der Grenze; der Eingangsruhestrom von 80 nA lädt den Kondensator zusätzlich mit 0,8 V je Sekunde. Praktische Integratoren werden deshalb vor jeder Messung über einen Schalter parallel zu $C$ entladen oder bekommen einen großen Widerstand parallel zum Kondensator. Mit 1 MΩ entstehen aus dem Offset nur noch 0,1 V und aus dem Ruhestrom 80 mV, und als Integrator arbeitet die Schaltung für Frequenzen deutlich über 1,6 Hz.
:::

Vertauscht man $R$ und $C$, wird aus dem Integrieren ein Differenzieren (Skript S. 208, Bild 12.14, Abbildung 5b). Der __Differenzierer__ hat den Kondensator zwischen Eingang und virtueller Masse; an ihm liegt deshalb die ganze Eingangsspannung, und sein Strom ist $C$ mal ihrer Änderungsgeschwindigkeit. Dieser Strom fließt durch $R$ zum Ausgang:

:::formel Formel
$$u_A(t) = -RC\,\frac{du_E}{dt}$$
:::

**So liest man das:** Der Ausgang zeigt, wie schnell sich der Eingang ändert, nicht wie groß er ist. Ein Dreieck von ±1 V mit 1 kHz steigt und fällt mit 4 V/ms und wird zu einem Rechteck von ∓4 V.

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

:::frage
„Warum sieht man Differenzierer in der Praxis so selten?“
Aus zwei Gründen. Erstens verstärken sie schnelle Änderungen am stärksten, und am schnellsten ändert sich das Rauschen: Für einen Sinus der Frequenz $f$ ist das Verhältnis der Amplituden $2\pi f RC$, denn die Ableitung von $\sin(2\pi f t)$ hat die Amplitude $2\pi f$; mit den Bauteilen oben 0,63 bei 100 Hz, 6,3 bei 1 kHz und 63 bei 10 kHz. Zweitens schwingt die Schaltung mit einem realen OPV: Weil dessen Ausgang nur mit endlicher Geschwindigkeit folgt, bilden Kondensator und OPV einen schwach gedämpften Schwingkreis, mit dem 741 bei 12,6 kHz und mit der Güte 79. Das Dreieck aus Abbildung 5b erzeugt dann statt eines sauberen Rechtecks Schwingungen bis an die Aussteuergrenze. Ein Widerstand von 1 kΩ in Reihe zum Kondensator dämpft das und begrenzt die Verstärkung hoher Frequenzen auf 10.
:::

## Logarithmierer, Exponentialfunktion und Multiplizierer

*Wie rechnet ein OPV mit Logarithmen, und wie entsteht daraus ein Produkt?*

:::grafik
Szene: get1/operationsverstaerker/02-logarithmierer · Vorlage: kennlinie-semilog
**Abbildung 6:** (a) Logarithmierer nach Skript Bild 12.15 mit $R$ = 10 kΩ und der Beispieldiode im Rückkopplungsweg (Anode am Minuseingang); daneben die Exponentialschaltung nach Bild 12.16 mit der Diode am Eingang (Anode an $U_E$, Kathode am Minuseingang) und $R$ = 10 kΩ im Rückkopplungsweg. (b) $U_A$ des Logarithmierers über $U_E$ von 10 mV bis 10 V, $U_E$ logarithmisch: eine Gerade von −466 mV über −526 mV und −586 mV bis −645 mV, je Dekade 59,5 mV; gestrichelt die Kennlinie bei 310 K: steiler, 61,5 mV je Dekade, und um 27 mV (bei 10 mV) bis 21 mV (bei 10 V) höher, bei 1 V um 23 mV. Die Diode im Rückkopplungsweg macht aus dem Strom eine Spannung, die mit dem Logarithmus wächst.
:::

Setzt man eine Diode in den Rückkopplungsweg (Skript S. 209, Bild 12.15), muss der Eingangsstrom $U_E/R$ durch sie fließen. Die Diode stellt ihre Spannung so ein, dass sie genau diesen Strom führt. Nach ihrer Kennlinie ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html)) wächst der Strom exponentiell mit der Spannung; umgekehrt wächst die Spannung mit dem Logarithmus des Stroms. Der Ausgang liegt um diese Diodenspannung unter der virtuellen Masse; so entsteht der __Logarithmierer__.

**Die Akteure:**

- __$I_S$__: Sättigungsstrom der Diode; bei der Beispieldiode 1,457·10⁻¹⁴ A.
- __$U_T$__: Temperaturspannung, 25,85 mV bei 300 K.
- __$U_{Di}$__: Spannung an der Diode, von der Anode zur Kathode; das Skript schreibt $U_D$, das hier die Differenzspannung bezeichnet.

:::formel Formel
$$U_A = -U_T\,\ln\frac{U_E}{R\,I_S}$$
:::

**So liest man das:** Jede Zehnerpotenz am Eingang verschiebt den Ausgang um denselben Betrag, $U_T \ln 10$ = 59,5 mV: Mit $R$ = 10 kΩ ergeben 10 mV am Eingang −466 mV, 1 V −586 mV und 10 V −645 mV (Abbildung 6b). Die Schaltung arbeitet nur mit positiven Eingangsspannungen. Bei negativen sperrt die Diode, die Gegenkopplung reißt ab, und der Ausgang läuft an eine Grenze.

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

Für Messzwecke taugt die einfache Schaltung kaum, weil $U_T$ und vor allem $I_S$ stark von der Temperatur abhängen. Bei 310 K statt 300 K liegt der Ausgang bei 1 V Eingang um 23 mV höher; das sind 0,39 Dekaden, als wäre die Eingangsspannung 2,5-mal kleiner. Zugleich wächst die Steigung mit $U_T$ von 59,5 auf 61,5 mV je Dekade. Praktische Logarithmierer verwenden einen Transistor statt der Diode (Skript S. 209), weil sein Kollektorstrom der Exponentialfunktion über viele Zehnerpotenzen genauer folgt: Der Rekombinationsstrom fließt in den Basisanschluss ([Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html)). Den Temperaturgang beseitigt er allein nicht: Einen zweiten, gleichen Transistor auf demselben Chip nutzt man, um $I_S$ herauszurechnen, und den Gang von $U_T$, 3,3 % je 10 K, gleicht eine temperaturabhängige Verstärkung aus.

Vertauscht man Diode und Widerstand (Skript Bild 12.16), bestimmt die Eingangsspannung die Diodenspannung und damit einen exponentiell wachsenden Strom, den $R$ in die Ausgangsspannung umsetzt; das ist die __Exponentialschaltung__:

$$U_A = -R\,I_S\,\exp\Big(\frac{U_E}{U_T}\Big)$$

Je 59,5 mV mehr am Eingang verzehnfachen den Ausgang: Mit 10 kΩ und der Beispieldiode ergeben 0,50 V −36,6 mV, 0,55 V −0,253 V und 0,60 V −1,75 V.

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

Mit beiden Schaltungen lässt sich multiplizieren, weil der Logarithmus eines Produkts die Summe der Logarithmen ist (Skript S. 210, Bilder 12.17 und 12.18, Abbildung 7): Zwei Logarithmierer bilden die Logarithmen von $U_X$ und $U_Y$, ein Addierer summiert sie, und eine Exponentialschaltung macht aus der Summe wieder ein Produkt.

:::grafik
Szene: get1/operationsverstaerker/02-multiplizierer · Vorlage: blockschaltbild
**Abbildung 7:** Oben das Schema nach Skript Bild 12.17: $U_X$ und $U_Y$ → je ein Logarithmierer → Addierer → Exponentialschaltung → Produkt. Darunter die Schaltung nach Bild 12.18 mit Werten: Logarithmierer mit $R_L$ = 10 kΩ und Beispieldiode, Addierer mit gleichen Widerständen, Exponentialschaltung mit $R_L$ = 10 kΩ; Beschriftung des Ergebnisses $-U_X U_Y/(R_L I_S)$ mit dem Faktor 6,9·10⁹ je Volt. Rechts als Ergänzung ein dritter Logarithmierer für eine Referenzspannung von 10 V, dessen Ausgang über einen Umkehrer in den Addierer geht und so abgezogen wird; dann ergibt sich $-U_X U_Y/(10\ \mathrm{V})$, bei 2 V und 3 V also −0,6 V. Der Logarithmus macht aus dem Produkt eine Summe; brauchbar wird das Ergebnis erst mit einer Referenz.
:::

Rechnet man die gezeichnete Schaltung mit gleichen Bauteilen durch, ergibt sich ein Produkt, aber mit einem Maßstab, den das Skript offenlässt:

$$U_A = -\frac{U_X\,U_Y}{R_L\,I_S}$$

Mit $R_L$ = 10 kΩ und der Beispieldiode ist der Faktor $1/(R_L I_S)$ = 6,9·10⁹ je Volt; schon 1 mV an beiden Eingängen verlangte −6862 V. Brauchbar wird die Schaltung erst, wenn der Addierer zusätzlich den Logarithmus einer Referenzspannung abzieht; dazu geht der Ausgang eines dritten Logarithmierers über einen Umkehrer (Verstärkung −1) in den Addierer. Dann ist das Ergebnis $-U_X U_Y/U_{Ref}$, mit 10 V Referenz bei 2 V und 3 V also −0,6 V. Auch integrierte Multiplizierer wie der AD633 haben einen festen Maßstab aus einer inneren 10-V-Referenz; sie multiplizieren aber in einer Transistorzelle direkt mit Strömen, ohne getrennte Logarithmier- und Exponentialstufen, und verarbeiten auch negative Eingänge. Die Schaltung hier verarbeitet nur positive, weil der Logarithmus nur für positive Zahlen erklärt ist.

Idee der Herleitung: Die Formeln der drei Stufen werden hintereinander eingesetzt; die beiden Logarithmen addieren sich, die Exponentialfunktion hebt den Logarithmus auf.

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

Den Rechenschaltungen verdankt der Operationsverstärker seinen Namen (Skript S. 209): Er entstand in den 1940er-Jahren als Baustein von Analogrechnern, die Differentialgleichungen mit Addierern und Integratoren lösten.

## Transimpedanzverstärker und negativer Widerstand

*Wie misst ein OPV einen Strom, und wie macht er einen Widerstand negativ?*

:::grafik
Szene: get1/operationsverstaerker/02-transimpedanz-nic · Vorlage: schaltung-zustaende
**Abbildung 8:** (a) Transimpedanzverstärker nach Skript S. 212 mit $R$ = 100 kΩ; eine Fotodiode zwischen Masse und Minuseingang (Anode am Minuseingang, Kathode an Masse) liefert 1 µA Fotostrom in die virtuelle Masse, die Diode liegt auf 0 V, der Ausgang auf −0,1 V. (b) Konverter für negative Impedanzen (NIC) nach Skript S. 211: OPV mit $R$ = 10 kΩ vom Ausgang zum Pluseingang und $R$ = 10 kΩ vom Ausgang zum Minuseingang, $R_2$ = 10 kΩ vom Minuseingang nach Masse; der Pluseingang ist der Anschluss der Schaltung. Daran parallel eine Stromquelle 1 mA mit 10 kΩ Innenwiderstand und eine Last von 1 kΩ: ohne NIC 0,909 mA durch die Last, mit NIC 1,000 mA; Ausgang des OPV auf 2 V. Die virtuelle Masse misst Ströme ohne Spannungsabfall; der negative Widerstand hebt den Innenwiderstand der Quelle auf.
:::

Lässt man beim invertierenden Verstärker den Eingangswiderstand weg und speist einen Strom $I_E$ direkt in die virtuelle Masse, fließt er durch $R$ zum Ausgang (Skript S. 211–212). Die Schaltung heißt __Transimpedanzverstärker__ oder Strom-Spannungs-Wandler:

:::formel Formel
$$U_A = -I_E\,R$$
:::

**So liest man das:** Der Ausgang ist dem Eingangsstrom proportional, $R$ ist der Umrechnungsfaktor in Volt je Ampere. Die Quelle sieht eine Spannung von null: Für sie ist die Schaltung ein Strommessgerät ohne Innenwiderstand. Mit 100 kΩ werden 1 nA zu −0,1 mV, 1 µA zu −0,1 V und 10 µA zu −1 V.

Idee der Herleitung: Der Eingangsstrom kann nur durch $R$; die virtuelle Masse hält die Spannung am Eingang auf null.

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

::::beispiel Fotodiode am Transimpedanzverstärker
**Gegeben:** $R$ = 100 kΩ; eine Fotodiode, die je nach Beleuchtung 1 nA bis 10 µA Fotostrom liefert; idealer OPV mit den Grenzen ±14 V.

**Gesucht:** der Ausgangsbereich und die Spannung an der Fotodiode.

**Rechnung:**

$$U_A = -1\ \mathrm{nA}\cdot 100\ \mathrm{k}\Omega = -0{,}1\ \mathrm{mV}$$

$$U_A = -10\ \mu\mathrm{A}\cdot 100\ \mathrm{k}\Omega = -1\ \mathrm{V}$$

Die Fotodiode liegt zwischen Masse und virtueller Masse, also auf 0 V.

**Ergebnis:** **−0,1 mV bis −1 V, proportional zum Licht; an der Fotodiode liegen 0 V.**

**Einordnung:** Bei 0 V fließt durch die Diode nach ihrer Kennlinie kein Dunkelstrom, $I_S[\exp(0) - 1]$ ist null; gemessen wird nur der Fotostrom ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html), Abschnitt *Fotodiode und Solarzelle*). Über einem Lastwiderstand gemessen, würde die Spannung an der Diode mit dem Licht steigen und ihren Strom verfälschen. Mit dem 741 flösse zusätzlich sein Eingangsruhestrom von 80 nA durch $R$ und überdeckte die kleinsten Fotoströme; für solche Messungen nimmt man OPVs mit Feldeffekttransistoren am Eingang, deren Ruhestrom im Pikoamperebereich liegt.
::::

Der __Konverter für negative Impedanzen__ (englisch negative impedance converter, NIC, Skript S. 211, Abbildung 8b) hat zwei gleiche Widerstände $R$ vom Ausgang zu beiden Eingängen. Der Pluseingang ist der Anschluss der Schaltung, mit der Spannung $U_1$ und dem hineinfließenden Strom $I_1$; am Minuseingang liegt $R_2$ nach Masse, mit $U_2$ und dem Strom $I_2$ durch $R_2$. Wegen der ersten Regel sind $U_1$ und $U_2$ gleich. An beiden Widerständen $R$ liegt deshalb dieselbe Spannung, und vom Ausgang fließt in beide Knoten derselbe Strom. Am Minuseingang fließt er weiter durch $R_2$; am Pluseingang kann er nicht in den OPV und fließt deshalb aus dem Anschluss heraus.

:::formel Formel
$$R_E = \frac{U_1}{I_1} = -R_2$$
:::

**So liest man das:** Steigt die Spannung am Anschluss, fließt Strom heraus statt hinein: Der Anschluss verhält sich wie ein Widerstand von −$R_2$, hier −10 kΩ. Parallel zu einer realen Stromquelle mit 10 kΩ Innenwiderstand hebt er diesen auf: Durch eine Last von 1 kΩ fließen dann 1,000 mA statt 0,909 mA. Im Skript steht dafür $R_2 = R_S$; gemeint ist der Innenwiderstand $R_q$.

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

Die Schaltung ist zugleich gegengekoppelt, über den Widerstand zum Minuseingang, und mitgekoppelt, über den Widerstand zum Pluseingang. Die erste Regel gilt deshalb nur, solange die Gegenkopplung überwiegt; das Skript setzt das stillschweigend voraus. Mit dem Modell aus [Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html), Abschnitt *Warum die Schaltung zur Ruhe kommt*, ergibt sich eine einfache Bedingung: Der Widerstand, der am Pluseingang nach Masse liegt, hier Stromquelle und Last parallel, muss kleiner sein als $R_2$. Mit 1 kΩ Last ist der Anteil, den der Teiler am Pluseingang zurückführt, 0,083, am Minuseingang 0,5; die Schaltung ist stabil. Ohne Last wären beide Anteile 0,5, der Grenzfall.

Idee der Herleitung: Wie in der Rückkopplungsdynamik wird geprüft, ob eine Abweichung des Ausgangs die Differenzspannung verkleinert oder vergrößert.

:::herleitung
**Ausgangspunkt:** das Modell des OPV mit endlicher Geschwindigkeit, $dV_a/dt = \omega_T U_D$, aus [Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html).

**Annahmen:** (i) Am Pluseingang liegt der Widerstand $R_p$ nach Masse (Quelle und Last parallel), dazu gegebenenfalls eine ideale Stromquelle; am Minuseingang $R_2$. (ii) Kein Strom in die Eingänge.

**Schritt 1**: Die Teiler führen die Anteile $k_+$ und $k_-$ der Ausgangsspannung zurück; die Stromquelle verschiebt nur den Pluseingang um einen festen Betrag $U_0$:

$$U_{e+} = k_+\,V_a + U_0$$

$$k_+ = \frac{R_p}{R + R_p}$$

$$k_- = \frac{R_2}{R + R_2}$$

**Schritt 2**: Eingesetzt in das Modell:

$$\frac{dV_a}{dt} = \omega_T\,\big((k_+ - k_-)\,V_a + U_0\big)$$

**Schritt 3** (entscheidender Schritt): Eine Abweichung klingt ab, wenn der Faktor vor $V_a$ negativ ist, und wächst sonst, wie bei Gegen- und Mitkopplung:

$$k_- > k_+$$

Das gilt genau dann, wenn $R_p$ kleiner ist als $R_2$.

**Ergebnis:** Stabil ist der NIC, solange der Widerstand am Pluseingang kleiner ist als $R_2$.

**Woher die Faktoren kommen:** $k_+$ ist die Mitkopplung, $k_-$ die Gegenkopplung; nur ihre Differenz zählt.

**Proben:** 1 kΩ Last parallel zu 10 kΩ ergibt $R_p$ = 0,909 kΩ, $k_+$ = 0,083 gegen $k_-$ = 0,5: stabil. Ohne Last: $R_p$ = 10 kΩ = $R_2$, Grenzfall.

**Grenzen:** Das Modell kennt nur eine Verzögerung; reale NICs brauchen wegen weiterer Verzögerungen einen Sicherheitsabstand.
:::

::::beispiel Stromquelle mit negativem Widerstand kompensiert
**Gegeben:** reale Stromquelle mit 1 mA und $R_q$ = 10 kΩ Innenwiderstand; parallel ein NIC mit $R$ = 10 kΩ und $R_2$ = 10 kΩ; Lasten 1 kΩ, 2 kΩ und 5 kΩ; Beispiel-OPV mit ±14 V.

**Gesucht:** der Laststrom ohne und mit NIC und die Ausgangsspannung des OPV.

**Rechnung:** Ohne NIC teilt sich der Strom zwischen $R_q$ und Last, bei 1 kΩ:

$$I_L = 1\ \mathrm{mA}\cdot\frac{10\ \mathrm{k}\Omega}{10\ \mathrm{k}\Omega + 1\ \mathrm{k}\Omega} = 0{,}909\ \mathrm{mA}$$

Mit NIC liegen 10 kΩ und −10 kΩ parallel; ihr Leitwert ist null, und der ganze Strom fließt durch die Last: 1,000 mA. An der Last liegen 1 V, der OPV-Ausgang liegt nach der Herleitung oben auf 2 V. Mit 2 kΩ und 5 kΩ: ohne NIC 0,833 mA und 0,667 mA, mit NIC jeweils 1,000 mA, der Ausgang auf 4 V und 10 V.

**Ergebnis:** **Mit NIC fließt in jede Last 1,000 mA, solange der OPV-Ausgang nicht an seine Grenze kommt, also bis 7 kΩ.**

**Einordnung:** Der NIC macht aus der realen eine ideale Stromquelle. Er ist in allen drei Fällen stabil, weil am Pluseingang die Last parallel zu $R_q$ liegt und der Widerstand dort kleiner ist als $R_2$.
::::

:::fehlvorstellung
„Ein negativer Widerstand müsste Energie aus dem Nichts liefern.“ Das liegt nahe, weil er Leistung abgibt statt aufnimmt: Bei 1 V am Anschluss fließen 0,1 mA heraus, 0,1 mW. Diese Leistung stammt aus der Versorgung des OPV. Der NIC ist kein passives Bauteil, sondern eine Schaltung mit eigener Energiequelle, die einen Strom so steuert, als wäre der Widerstand negativ.
:::

## Alles hängt an einem Prinzip

| Schaltung | welche Seite des Prinzips sie zeigt |
|---|---|
| inver­tierender Verstärker | Virtuelle Masse: Der Eingangsstrom muss durch den Rückkopplungs­widerstand. |
| nicht­invertierender Verstärker, Impedanz­wandler | Die erste Regel zwingt den Minuseingang auf $U_E$; aus der Quelle fließt kein Strom. |
| Addierer, Subtra­hierer | Ströme addieren sich an der virtuellen Masse; Überlagerung zweier Verstärker. |
| Integrator, Differen­zierer | Im Rückweg integriert der Kondensator den Strom zur Spannung; am Eingang macht er aus der Änderung der Spannung einen Strom. |
| Logarith­mierer, Exponential­schaltung | Die Diode setzt Strom und Spannung exponentiell ineinander um. |
| Transimpedanz­verstärker, NIC | Strom wird zu Spannung; Mitkopplung neben Gegenkopplung kehrt das Vorzeichen eines Widerstands um. |
| Kaskade | Jede Stufe liefert jeden Strom; die Verstärkungen multiplizieren sich. |

Bei Gegenkopplung stellt sich der Ausgang des OPV so ein, dass zwischen seinen Eingängen keine Spannung liegt, und in die Eingänge des idealen OPV fließt kein Strom; aus diesen beiden Regeln und den Gleichungen der äußeren Bauteile folgt jede Grundschaltung, und welche Bauteile im Eingangs- und im Rückkopplungszweig sitzen, bestimmt die Rechenoperation.

## Bedeutung und Ausblick

Mit diesen Schaltungen baute man ganze Analogrechner; heute stecken sie in Sensorverstärkern (Subtrahierer an Messbrücken, Transimpedanzverstärker an Fotodioden), in aktiven Filtern und Reglern (Integratoren) und in Digital-Analog-Umsetzern (gewichtete Addierer). Alle Ergebnisse dieses Artikels gelten für den idealen OPV. Wie endliche Leerlaufverstärkung, begrenzte Geschwindigkeit, Offsetspannung und Eingangsströme sie verfälschen, behandelt [Der reale Operationsverstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/realer-operationsverstaerker.html).

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
A: Nein. In die Eingänge fließt kein Strom; der Strom fließt weiter durch R_2 zum Ausgang, der ihn aufnimmt. Deshalb ist U_A = −R_2 I.
F: Ein invertierender Verstärker hat R_1 = 10 kΩ und R_2 = 30 kΩ. Bis zu welcher Eingangsamplitude bleibt der Ausgang des Beispiel-OPV unverzerrt?
A: Bis 14 V/3 = 4,67 V; darüber begrenzt der Ausgang bei ±14 V.
F: Warum ist die Verstärkung des nichtinvertierenden Verstärkers mindestens 1?
A: Der Minuseingang muss auf U_E liegen, und der Ausgang liegt noch um den Spannungsabfall an R_2 weiter von null entfernt; deshalb ist A = 1 + R_2/R_1.
F: Wozu dient ein Impedanzwandler mit der Verstärkung 1?
A: Er nimmt der Quelle keinen Strom ab und liefert der Last jeden Strom; eine hochohmige Quelle wird nicht belastet (5 V an 100 kΩ: mit idealem OPV 5,000 V statt 4,545 V mit einem 1-MΩ-Messgerät).
F: Warum stört beim Addierer keine Quelle die andere?
A: Alle Eingangswiderstände enden an der virtuellen Masse, die auf 0 V festgehalten wird; jeder Strom hängt nur von seiner eigenen Quelle ab, und alle zusammen fließen durch R_4.
F: Stimmt es, dass der Subtrahierer bei beliebigen Widerständen die Differenz der Eingänge bildet?
A: Nein. Nur wenn R_4/R_3 gleich R_2/R_1 ist, etwa mit R_3 = R_1 und R_4 = R_2, gehen beide Eingänge mit gleichem Faktor ein; sonst geht auch die Gleichtaktspannung durch, bei 1 % Abweichung mit dem Faktor 0,009.
F: Warum erzeugt ein Integrator aus einer konstanten Eingangsspannung eine Rampe?
A: Der konstante Strom U_E/R aus der virtuellen Masse lädt den Kondensator gleichmäßig; seine Spannung und damit der Ausgang ändern sich mit konstanter Geschwindigkeit U_E/(RC).
F: Stimmt es, dass ein negativer Widerstand Energie aus dem Nichts erzeugt?
A: Nein. Die Leistung, die er abgibt, stammt aus der Versorgung des OPV; er ist eine aktive Schaltung.
F: Zwei invertierende Stufen haben die Verstärkungen −10 und −5. Wie groß ist die Gesamtverstärkung, und was geschieht bei 0,3 V am Eingang?
A: (−10)·(−5) = +50; bei 0,3 V verlangte die zweite Stufe 15 V und begrenzt bei 14 V.
:::
