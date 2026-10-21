---
title: Arbeitspunkt und Grundschaltungen des Transistors
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Bipolartransistoren
order: 110200
summary: Wie man einen Bipolartransistor in seinen Arbeitspunkt bringt und dort hält, obwohl Stromverstärkung und Basis-Emitter-Spannung streuen und mit der Temperatur wandern: Arbeitsgerade und Betriebsgrenzen, lineare Ersatzschaltbilder, Basiswiderstand, Strom- und Spannungsgegenkopplung, Stromspiegel, Inverter und die drei Grundschaltungen. Ausführliche Fassung mit allen Herleitungen, dem vollständigen Transistormodell zum Vergleich und Beispielen am BC547C.
tags: Arbeitspunkt, Basisspannungsteiler, Emitterwiderstand, Gegenkopplung, Emitterschaltung, Kollektorschaltung, Basisschaltung
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Bevor ein Transistor verstärkt oder schaltet, muss die Schaltung festlegen, welcher Kollektorstrom bei welcher Spannung fließt. Das Problem: Die Kennwerte des Transistors sind unsicher. Die Stromverstärkung $B$ liegt beim BC547C, der Verstärkungsgruppe C des BC547, irgendwo zwischen 420 und 800, und die Basis-Emitter-Spannung sinkt um 2 mV je Kelvin.
**Der Arbeitspunkt eines Transistors ist der Punkt, an dem seine Kennlinien und die Gleichungen der äußeren Schaltung zugleich gelten; gute Schaltungen legen ihn so fest, dass die unsicheren Kennwerte des Transistors, Stromverstärkung und Basis-Emitter-Spannung, kaum eingehen: durch Gegenkopplung oder dadurch, dass sie sich wie im Stromspiegel herauskürzen.**

Vorausgesetzt werden die Arbeitsbereiche, das Rechnen mit Annahme und Probe und die Streuung von $B$ aus [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html), die Arbeitsgerade aus [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html) und die Ersatzspannungsquelle aus [Ersatzquellen nach Thévenin und Norton](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/ersatzquellen-thevenin-norton.html). Darauf baut [Der Transistor als Verstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker.html) auf.

:::grafik
Szene: get1/bipolartransistoren/02-arbeitsgerade-grenzen · Vorlage: kennlinienfeld-arbeitsgerade
**Abbildung 1:** (a) Ausgangskennlinienfeld des Beispieltransistors (BC547C-artig, $I_B$ = 2 bis 10 µA) mit der Arbeitsgeraden eines Kollektorwiderstands von 2,2 kΩ an 10 V, von (10 V; 0) nach (0; 4,55 mA), und dem Arbeitspunkt in der Mitte bei 5,1 V und 2,23 mA. (b) Größerer Maßstab bis 50 V und 160 mA mit den Grenzen des BC547: 45 V, 100 mA und die Hyperbel der höchsten Verlustleistung von 625 mW. Die Gerade aus (a) liegt dicht am Ursprung; eine zweite Gerade, 200 Ω an 30 V, schneidet die Hyperbel und reicht über 100 mA hinaus. Der Arbeitspunkt ist der Schnittpunkt von Kennlinie und Arbeitsgerade; jede Gerade muss in den Grenzen bleiben.
:::

## Arbeitspunkt, Arbeitsgerade und Betriebsgrenzen

*Wo arbeitet ein Transistor in einer Schaltung, und welche Arbeitspunkte verträgt er?*

**Die Akteure:**

- __$U_{CC}$__: Versorgungsspannung des Kollektorkreises; 10 V im Beispiel.
- __$R_C$__: __Kollektorwiderstand__ zwischen Versorgung und Kollektor; 2,2 kΩ.
- __Arbeitspunkt__: das Wertepaar aus Kollektorstrom $I_C$ und Spannung $U_{CE}$, bei dem der Transistor ohne Signal arbeitet.
- __$P$__: __Verlustleistung__ des Transistors, im Wesentlichen $U_{CE}$ mal $I_C$; sie wird zu Wärme.

**Das Zusammenspiel:** Der Transistor gibt mit seinem Ausgangskennlinienfeld vor, welcher Kollektorstrom bei welcher Spannung $U_{CE}$ fließen kann; welche Kennlinie gilt, legt der Basisstrom fest. Der Kollektorkreis gibt eine zweite Bedingung vor: Was am Kollektorwiderstand abfällt, fehlt an $U_{CE}$. Beide zusammen lassen nur einen Punkt zu, den __Arbeitspunkt__ (Abbildung 1), genauso wie bei der Diode.

:::formel Gesetz
$$U_{CE} = U_{CC} - R_C\,I_C$$
:::

**So liest man das:** Die __Arbeitsgerade__ verbindet den Leerlauf (kein Strom, die volle Versorgungsspannung am Transistor) mit dem Kurzschlussstrom $U_{CC}/R_C$ (keine Spannung am Transistor), bei 10 V und 2,2 kΩ also 10 V mit 4,55 mA. Ein größerer Widerstand macht sie flacher. Alle Arbeitspunkte, die der Kollektorkreis zulässt, liegen auf ihr.

Idee der Herleitung: Maschenregel im Kollektorkreis.

:::herleitung
**Ausgangspunkt:** die Maschenregel aus [Kirchhoffsche Gesetze](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/kirchhoffsche-gesetze.html) und das ohmsche Gesetz.

**Annahmen:** (i) Im Kollektorkreis liegen nur die Quelle, der Widerstand und die Kollektor-Emitter-Strecke; (ii) der Emitter liegt an Masse.

**Schritt 1**: Der Umlauf über Quelle, Widerstand und Transistor ergibt:

$$U_{CC} = R_C\,I_C + U_{CE}$$

**Schritt 2** (entscheidender Schritt): Nach $U_{CE}$ aufgelöst:

$$U_{CE} = U_{CC} - R_C\,I_C$$

**Ergebnis:**

$$U_{CE} = U_{CC} - R_C\,I_C$$

**Woher die Faktoren kommen:** Im Kennlinienfeld hat die Gerade die Steigung $-1/R_C$: Je 2,2 V weniger an $U_{CE}$ fließt 1 mA mehr.

**Proben:** Einheit V. Grenzfälle: Bei $I_C$ = 0 ist $U_{CE}$ = $U_{CC}$; bei $U_{CE}$ = 0 fließt $U_{CC}/R_C$.

**Grenzen:** Liegt auch im Emitterkreis ein Widerstand, kommt dessen Spannung hinzu, und die Gerade wird flacher (Abschnitt *Stromgegenkopplung mit Emitterwiderstand*).
:::

Ob der Transistor schalten oder verstärken soll, bestimmt, wo auf der Geraden man ihn betreibt (Skript, S. 178). Als __Schalter__ springt er zwischen zwei Endpunkten: gesperrt bei 10 V ohne Strom und gesättigt bei 0,2 V und 4,45 mA. In beiden ist die Verlustleistung klein, null bzw. 0,9 mW, und der Abstand zwischen Ein und Aus ist so groß wie möglich. Als __Verstärker__ arbeitet er im aktiven Bereich, wo der Kollektorstrom dem Eingang folgt. Damit ein Signal in beide Richtungen gleich weit ausschlagen kann, legt man den Arbeitspunkt in die Mitte zwischen der Sättigungsgrenze und der Versorgung: bei 10 V auf 5,1 V und 2,23 mA. Dort ist die Verlustleistung am größten, 11,4 mW.

Für jeden Transistor gelten __Betriebsgrenzen__ (Skript, S. 181–182, Bild 11.9). Beim BC547 sind es höchstens 45 V zwischen Kollektor und Emitter, 100 mA Kollektorstrom und 625 mW Verlustleistung bei 25 °C Umgebung. Die Leistungsgrenze ist im Kennlinienfeld eine Hyperbel, weil $U_{CE}$ mal $I_C$ konstant ist: bei 10 V 62,5 mA, bei 45 V nur 13,9 mA. Der Text des Skripts nennt nur die ersten beiden Grenzen; Bild 11.9 zeigt die Hyperbel als dritte. Die Leistung wird zu Wärme: Mit einem Wärmewiderstand von 200 K/W zur Umgebung erwärmen 11,4 mW den Übergang um 2,3 K, 625 mW um 125 K, bis an die zulässigen 150 °C.

Die größte Leistung, die ein Arbeitspunkt auf der Geraden haben kann, liegt bei halber Versorgungsspannung:

$$P_\mathrm{max} = \frac{U_{CC}^2}{4\,R_C}$$

Idee der Herleitung: Man schreibt die Leistung längs der Geraden als Funktion von $U_{CE}$ und sucht ihr Maximum.

:::herleitung
**Ausgangspunkt:** die Arbeitsgerade und die Verlustleistung als Produkt aus $U_{CE}$ und $I_C$ (der kleine Beitrag des Basisstroms bleibt weg).

**Annahmen:** (i) Der Arbeitspunkt liegt auf der Arbeitsgeraden.

**Schritt 1**: Mit der Arbeitsgeraden nach dem Strom aufgelöst:

$$P = U_{CE}\,I_C = \frac{U_{CE}\,(U_{CC} - U_{CE})}{R_C}$$

**Schritt 2** (entscheidender Schritt): Das ist eine nach unten geöffnete Parabel in $U_{CE}$ mit den Nullstellen 0 und $U_{CC}$; ihr Scheitel liegt in der Mitte, bei $U_{CC}/2$.

**Schritt 3**: Eingesetzt:

$$P_\mathrm{max} = \frac{U_{CC}/2\cdot U_{CC}/2}{R_C} = \frac{U_{CC}^2}{4\,R_C}$$

**Ergebnis:**

$$P_\mathrm{max} = \frac{U_{CC}^2}{4\,R_C}$$

**Woher die Faktoren kommen:** Die 4 entsteht, weil im Maximum Spannung und Strom je halb so groß sind wie ihre Endwerte.

**Proben:** Einheit V²/Ω = W. Zahlenwert: 100 V² durch 8,8 kΩ ergibt 11,4 mW.

**Grenzen:** Gilt für einen reinen Widerstand im Kollektorkreis; die Mitte des Skripts, 5,1 V, liegt nur 0,1 V neben dem Maximum.
:::

::::beispiel Arbeitsgerade, Mitte und Grenzen an 10 V und 2,2 kΩ
**Gegeben:** $U_{CC}$ = 10 V, $R_C$ = 2,2 kΩ, Sättigungsspannung 0,2 V; BC547: 45 V, 100 mA, 625 mW. Zum Vergleich eine zweite Gerade mit 200 Ω an 30 V.

**Gesucht:** Endpunkte der Geraden, Arbeitspunkt in der Mitte und seine Leistung; ob die zweite Gerade zulässig ist.

**Rechnung:** Kurzschlussstrom und Mitte:

$$\frac{U_{CC}}{R_C} = \frac{10\ \mathrm{V}}{2{,}2\ \mathrm{k\Omega}} = 4{,}55\ \mathrm{mA}, \qquad U_{CE} = \frac{10\ \mathrm{V} + 0{,}2\ \mathrm{V}}{2} = 5{,}1\ \mathrm{V}$$

$$I_C = \frac{10\ \mathrm{V} - 5{,}1\ \mathrm{V}}{2{,}2\ \mathrm{k\Omega}} = 2{,}23\ \mathrm{mA}, \qquad P = 5{,}1\ \mathrm{V}\cdot2{,}23\ \mathrm{mA} = 11{,}4\ \mathrm{mW}$$

Zweite Gerade:

$$\frac{30\ \mathrm{V}}{200\ \Omega} = 150\ \mathrm{mA}, \qquad P_\mathrm{max} = \frac{(30\ \mathrm{V})^2}{4\cdot200\ \Omega} = 1{,}13\ \mathrm{W}$$

**Ergebnis:** **Mitte bei 5,1 V und 2,23 mA mit 11,4 mW; die Gerade mit 200 Ω an 30 V überschreitet 100 mA und 625 mW.**

**Einordnung:** Im ersten Fall bleibt jeder Punkt der Geraden weit in den Grenzen, auch wenn der Arbeitspunkt wandert. Im zweiten würde ein Schalter beim Einschalten 150 mA ziehen wollen, und ein Verstärker in der Mitte setzte fast doppelt so viel Leistung um, wie der BC547 verträgt.
::::

## Die linearen Ersatzschaltbilder

*Wie rechnet man mit einem Transistor wie mit einem gewöhnlichen Netzwerk?*

:::grafik
Szene: get1/bipolartransistoren/02-ersatzschaltbilder · Vorlage: schaltung-zustaende
**Abbildung 2:** Die linearen Ersatzschaltbilder des npn-Transistors nach dem Skript. (a) Sperrbereich: alle drei Anschlüsse offen. (b) Aktiver Bereich: zwischen Basis und Emitter eine Spannungsquelle 0,6 V, zwischen Kollektor und Emitter eine gesteuerte Stromquelle $B\,I_B$. (c) Sättigung: Basis-Emitter wie in (b), Kollektor-Emitter eine Spannungsquelle 0,2 V. Darunter die zugehörigen linearisierten Kennlinien: Eingang mit Knick bei 0,6 V, Steuerkennlinie mit der Steigung $B$ bis zur Sättigung und danach waagrecht, Ausgang mit senkrechtem Ast bei 0,2 V. In jedem Bereich wird der Transistor zu Quellen, mit denen man wie in jedem linearen Netz rechnet.
:::

Für Handrechnungen ersetzt das Skript den Transistor in jedem Arbeitsbereich durch ein lineares Netzwerk (S. 182–184, Bilder 11.10 bis 11.13), mit den Modellwerten $U_{BE,\mathrm{ein}}$ = 0,6 V und $U_{CE,\mathrm{sat}}$ = 0,2 V. Abbildung 2 zeigt die drei Ersatzschaltbilder. Im Sperrbereich fließt kein Strom. In beiden leitenden Bereichen wird der Basis-Emitter-Übergang zur Spannungsquelle, wie die Diode im Modell mit Durchlassspannung. Zwischen Kollektor und Emitter liegt im aktiven Bereich eine gesteuerte Stromquelle, deren Strom das $B$-Fache des Basisstroms ist, in der Sättigung eine Spannungsquelle mit 0,2 V. Am Emitter treffen in jedem Ersatzschaltbild Basis- und Kollektorstrom zusammen.

Weil man vorher nicht weiß, welches Ersatzschaltbild gilt, rechnet man wie bei der Diode mit Annahme und Probe: einen Bereich annehmen, mit seinem Ersatzschaltbild rechnen, die Bedingung des Bereichs prüfen. Die drei Bedingungen und ein durchgerechnetes Beispiel stehen im Abschnitt *Die Arbeitsbereiche* von [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html). In der linearisierten Steuerkennlinie (Abbildung 2) wird die Kurve in der Sättigung waagrecht. Das Skript sagt dazu, die Stromverstärkung sinke dort auf null (S. 182); genau genommen wird die Steigung null, während das Verhältnis von Kollektor- zu Basisstrom nur unter $B$ sinkt.

Zum Vergleich nennt dieser Artikel immer wieder Werte des __vollständigen Modells__. Das ist der Beispieltransistor aus [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html) ohne Vereinfachungen: Der Kollektorstrom folgt der Transfergleichung mit dem Sättigungsstrom $10^{-14}$ A, $B$ beträgt 500 bei 5 V, und durch den Early-Effekt ist der Kollektorstrom proportional zur Summe aus 70 V und $U_{CE}$. Die Sättigung entsteht darin von selbst, sobald auch der Kollektor-Basis-Übergang leitet.

::::beispiel Welcher Bereich? Drei Messungen am Beispieltransistor
**Gegeben:** Beispieltransistor mit $B$ = 500, Modellwerte 0,6 V und 0,2 V. Gemessen werden (a) 20 µA Basisstrom und 4,45 mA Kollektorstrom; (b) 4 µA Basisstrom bei 5 V zwischen Kollektor und Emitter; (c) 0,3 V zwischen Basis und Emitter.

**Gesucht:** der Bereich und das passende Ersatzschaltbild.

**Rechnung:** (a) Der Transistor könnte mehr liefern, als fließt:

$$B\,I_B = 500\cdot20\ \mu\mathrm{A} = 10\ \mathrm{mA} > 4{,}45\ \mathrm{mA}$$

also Sättigung. (b) Die Spannung liegt über 0,2 V, und es fließt Basisstrom: aktiver Bereich mit

$$I_C = 500\cdot4\ \mu\mathrm{A} = 2\ \mathrm{mA}$$

(c) 0,3 V liegen unter 0,6 V: Sperrbereich.

**Ergebnis:** **(a) Sättigung, Abbildung 2c; (b) aktiv mit 2 mA, Abbildung 2b; (c) gesperrt, Abbildung 2a.**

**Einordnung:** Für (a) zeigt das vollständige Modell, dass dabei 0,14 V zwischen Kollektor und Emitter liegen; die 0,2 V des Ersatzschaltbilds sind eine sichere Näherung. Bei (c) fließen in Wirklichkeit kleine Ströme, beim Beispieltransistor 1,1 nA Kollektor- und 2 pA Basisstrom, die das Ersatzschaltbild zu null setzt.
::::

## Der Basiswiderstand und warum der Arbeitspunkt wandert

*Wie stellt ein Basiswiderstand den Arbeitspunkt ein, und warum genügt das nicht?*

:::grafik
Szene: get1/bipolartransistoren/02-einstellungen · Vorlage: schaltplan
**Abbildung 3:** Drei Schaltungen zur Arbeitspunkteinstellung an 10 V. (a) Basiswiderstand $R_B$ = 2,2 MΩ von der Versorgung zur Basis, $R_C$ = 2,2 kΩ. (b) Stromgegenkopplung: Basisspannungsteiler $R_1$ = 330 kΩ, $R_2$ = 68 kΩ, Emitterwiderstand $R_E$ = 1 kΩ, $R_C$ = 3,9 kΩ; daneben der Teiler als Ersatzspannungsquelle mit $U_q$ = 1,71 V und $R_i$ = 56,4 kΩ. (c) Spannungsgegenkopplung: $R_B$ = 1 MΩ vom Kollektor zur Basis, $R_C$ = 2,2 kΩ. Drei Wege, den Basisstrom festzulegen, mit sehr verschiedener Abhängigkeit von $B$.
:::

Die einfachste Einstellung ist ein Widerstand $R_B$ von einer Spannung zur Basis (Abbildung 3a, Skript Bild 11.4). Er legt den Basisstrom fest, denn an ihm liegt die Ansteuerspannung abzüglich der 0,6 V der Basis-Emitter-Strecke.

**Die Akteure:**

- __$U_\mathrm{ein}$__: Spannung, an der der Basiswiderstand liegt; hier die Versorgung, 10 V. Das Skript nennt sie $U_E$.
- __$R_B$__: __Basiswiderstand__; 2,2 MΩ.

:::formel Formel
$$I_B = \frac{U_\mathrm{ein} - U_{BE,\mathrm{ein}}}{R_B}$$

$$I_C = B\,I_B$$

$$U_{CE} = U_{CC} - R_C\,B\,I_B$$
:::

**So liest man das:** Der Basiswiderstand bestimmt den Basisstrom, $B$ macht daraus den Kollektorstrom, und die Arbeitsgerade liefert die Spannung. Die Formeln gelten im aktiven Bereich; ergibt sich weniger als 0,2 V, ist der Transistor gesättigt, und unter 0,6 V an der Basis sperrt er. $B$ geht voll ein: Doppeltes $B$ ergibt doppelten Kollektorstrom.

Idee der Herleitung: Man setzt das Ersatzschaltbild des aktiven Bereichs ein und wendet die Maschenregel auf Basis- und Kollektorkreis an.

:::herleitung
**Ausgangspunkt:** das Ersatzschaltbild des aktiven Bereichs (Abbildung 2b) und die Maschenregel.

**Annahmen:** (i) aktiver Bereich (Probe danach); (ii) Modellwert 0,6 V zwischen Basis und Emitter.

**Schritt 1**: Basiskreis: An $R_B$ liegt die Ansteuerspannung abzüglich der Quelle des Ersatzschaltbilds:

$$I_B = \frac{U_\mathrm{ein} - U_{BE,\mathrm{ein}}}{R_B}$$

**Schritt 2**: Die gesteuerte Stromquelle liefert den Kollektorstrom:

$$I_C = B\,I_B$$

**Schritt 3** (entscheidender Schritt): Arbeitsgerade mit diesem Strom:

$$U_{CE} = U_{CC} - R_C\,B\,I_B$$

**Ergebnis:**

$$I_B = \frac{U_\mathrm{ein} - U_{BE,\mathrm{ein}}}{R_B}$$

$$I_C = B\,I_B$$

$$U_{CE} = U_{CC} - R_C\,B\,I_B$$

**Woher die Faktoren kommen:** Der Basiskreis kennt den Transistor nur als 0,6-V-Quelle; erst $B$ verbindet ihn mit dem Kollektorkreis.

**Proben:** Mit 10 V, 2,2 MΩ, $B$ = 500 und 2,2 kΩ: 4,27 µA, 2,14 mA, 5,30 V; mehr als 0,2 V, die Annahme hält.

**Grenzen:** Ergibt Schritt 3 weniger als 0,2 V, gilt das Ersatzschaltbild der Sättigung (Skript, S. 179).
:::

::::beispiel Basiswiderstand für die Mitte und drei Exemplare
**Gegeben:** $U_{CC}$ = $U_\mathrm{ein}$ = 10 V, $R_C$ = 2,2 kΩ, Beispieltransistor mit $B$ = 500; Exemplare des BC547C mit 420 und 800; Modellwerte 0,6 V und 0,2 V; Widerstände aus der Normreihe E12, der üblichen Abstufung im Handel.

**Gesucht:** $R_B$ für die Mitte; die Arbeitspunkte der drei Exemplare.

**Rechnung:** Die Mitte verlangt 2,23 mA (Beispiel zur Arbeitsgeraden), also

$$I_B = \frac{2{,}23\ \mathrm{mA}}{500} = 4{,}45\ \mu\mathrm{A}, \qquad R_B = \frac{10\ \mathrm{V} - 0{,}6\ \mathrm{V}}{4{,}45\ \mu\mathrm{A}} = 2{,}11\ \mathrm{M\Omega} \;\rightarrow\; 2{,}2\ \mathrm{M\Omega}$$

Mit 2,2 MΩ fließen 4,27 µA Basisstrom, und für die drei Exemplare:

$$B = 420\!:\ 1{,}80\ \mathrm{mA},\ 6{,}05\ \mathrm{V}, \qquad B = 500\!:\ 2{,}14\ \mathrm{mA},\ 5{,}30\ \mathrm{V}, \qquad B = 800\!:\ 3{,}42\ \mathrm{mA},\ 2{,}48\ \mathrm{V}$$

**Ergebnis:** **2,2 MΩ; je nach Exemplar liegt der Arbeitspunkt zwischen 2,5 und 6,1 V.**

**Einordnung:** Innerhalb einer einzigen Verstärkungsgruppe wandert der Arbeitspunkt um mehr als ein Drittel der Geraden; mit $B$ = 800 bleiben nach unten nur noch 2,3 V Aussteuerung. Das vollständige Modell ergibt für $B$ = 500 fast dieselben Werte (2,13 mA und 5,32 V). Für $B$ = 800 liegt $U_{CE}$ dort mit 2,77 V um 0,29 V höher, weil die Stromverstärkung bei kleinerer $U_{CE}$ durch den Early-Effekt etwas sinkt und die echte $U_{BE}$ über 0,6 V liegt.
::::

Warum der Arbeitspunkt wandert, zeigt die Formel: Der Kollektorstrom ist $B$-mal der Basisstrom, und alles, was $B$ verändert, verschiebt ihn im selben Verhältnis. Das sind die Fertigungsstreuung (beim BC547C der Faktor 1,9 zwischen 420 und 800) und die Temperatur, mit der $B$ um 0,5 bis 1 % je Kelvin steigt. Die Temperaturdrift von $U_{BE}$, 2 mV je Kelvin, spielt hier kaum eine Rolle, weil am Basiswiderstand 9,4 V liegen: Sie ändert den Basisstrom nur um 0,02 % je Kelvin. Das Skript fordert deshalb, den Kollektorstrom durch die äußere Beschaltung festzulegen statt durch $B$ (S. 179).

:::fehlvorstellung
„Mit dem Basiswiderstand stelle ich den Kollektorstrom ein.“
Das liegt nahe, weil der Widerstand die einzige Stellgröße der Schaltung ist. Er stellt aber den Basisstrom ein; der Kollektorstrom ist dessen $B$-Faches und erbt jede Streuung von $B$. Im Beispiel liefern drei Exemplare derselben Gruppe 1,80, 2,14 und 3,42 mA. Einen festen Kollektorstrom ergibt erst eine Schaltung, in der $B$ nur in kleinen Korrekturen vorkommt (Abschnitt *Stromgegenkopplung mit Emitterwiderstand*).
:::

## Stromgegenkopplung mit Emitterwiderstand

*Wie macht ein Emitterwiderstand den Kollektorstrom unabhängig von $B$ und von der Temperatur?*

:::grafik
Szene: get1/bipolartransistoren/02-gegenkopplung-kette · Vorlage: blockbild
**Abbildung 4:** Wirkungskette der Stromgegenkopplung, als Kreis gezeichnet: Der Kollektorstrom steigt (etwa weil der Transistor wärmer ist oder ein größeres $B$ hat), der Emitterstrom und damit die Spannung am Emitterwiderstand steigen, bei fester Basisspannung bleibt weniger $U_{BE}$, die Stufe am Basis-Emitter-Übergang wächst, und der Kollektorstrom sinkt zurück. Jede Abweichung erzeugt ihre eigene Gegenwirkung.
:::

**Die Akteure:**

- __$R_E$__: __Emitterwiderstand__ zwischen Emitter und Masse; 1 kΩ im Beispiel.
- __$U_B$__: Potenzial der Basis gegen Masse; im Beispiel rund 1,6 V.
- __$R_1$__, __$R_2$__: __Basisspannungsteiler__ von der Versorgung nach Masse, der die Basisspannung erzeugt; 330 kΩ und 68 kΩ.
- __$U_q$__, __$R_i$__: Leerlaufspannung und Innenwiderstand des Teilers, betrachtet als Ersatzspannungsquelle; 1,71 V und 56,4 kΩ.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Liegt die Basis auf einer festen Spannung, liegt der Emitter um die 0,6 V der Basis-Emitter-Strecke tiefer. Die Spannung am Emitterwiderstand ist damit festgelegt, und mit ihr der Emitterstrom: Bei 1,6 V an der Basis und 1 kΩ fließt 1,0 mA. $B$ kommt darin nicht vor (Skript, Beispielschaltung 2, S. 179).

**Schritt 2**: Wodurch das stabil ist, zeigt Abbildung 4. Will der Kollektorstrom steigen, steigt die Spannung am Emitterwiderstand, und bei fester Basisspannung bleibt weniger für $U_{BE}$. Die Stufe am Basis-Emitter-Übergang wächst, und der Strom geht zurück. Diese Rückwirkung, bei der eine Änderung ihre eigene Ursache schwächt, heißt __Gegenkopplung__, hier __Stromgegenkopplung__, weil der Kollektorstrom selbst die rückwirkende Spannung erzeugt.

**Schritt 3**: Dasselbe gilt für die Temperatur. Sinkt $U_{BE}$ um 2 mV je Kelvin, steigt die Spannung am Emitterwiderstand um diese 2 mV, also der Strom um 2 µA je Kelvin bei 1 kΩ: 0,2 % je Kelvin bei 1 mA, gegenüber 8 % je Kelvin, wenn man $U_{BE}$ festhielte.

**Schritt 4**: In der Praxis erzeugt ein __Basisspannungsteiler__ die Basisspannung (Abbildung 3b, Skript Bild 11.6). Als Ersatzspannungsquelle betrachtet (Bild 11.7) hat er einen Innenwiderstand, an dem der Basisstrom einen kleinen Spannungsabfall erzeugt. Weil der Basisstrom $B$ enthält, schleicht sich $B$ über diesen Abfall wieder ein, aber nur als Korrektur: Ein Basisstrom von 2 µA erzeugt an 56,4 kΩ 0,11 V.

:::formel Formel
$$I_C = \frac{U_q - U_{BE,\mathrm{ein}}}{R_E\,(1 + 1/B) + R_i/B}, \qquad I_C \approx \frac{U_q - U_{BE,\mathrm{ein}}}{R_E}$$
:::

**So liest man das:** Die Leerlaufspannung des Teilers abzüglich der Basis-Emitter-Spannung liegt fast ganz am Emitterwiderstand und bestimmt den Strom. $B$ steht nur in den Korrekturen $R_E/B$ und $R_i/B$, im Beispiel 2 Ω und 113 Ω neben 1000 Ω; deshalb ergeben 10 % mehr $B$ nur rund 1 % mehr Strom. Die Näherung rechts gilt, wenn $R_E$ viel größer ist als $R_i/B$ und $B$ groß ist (Skript, Gl. 11.1). Den letzten Schritt des Skripts, auch $U_{BE}$ wegzulassen, darf man nur bei Basisspannungen weit über 0,6 V gehen; mit den 1,71 V des Beispiels ergäbe er 1,71 mA statt 0,99 mA.

Idee der Herleitung: Man ersetzt den Teiler durch seine Ersatzspannungsquelle und geht einmal um den Basiskreis bis Masse.

:::herleitung
**Ausgangspunkt:** die Ersatzspannungsquelle aus [Ersatzquellen nach Thévenin und Norton](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/ersatzquellen-thevenin-norton.html), das Ersatzschaltbild des aktiven Bereichs und die Knotenregel am Emitter.

**Annahmen:** (i) aktiver Bereich; (ii) Modellwert 0,6 V zwischen Basis und Emitter; (iii) $B$ ist im Arbeitspunkt konstant.

**Schritt 1**: Der Teiler wirkt auf die Basis wie eine Quelle mit Leerlaufspannung und Innenwiderstand:

$$U_q = \frac{R_2}{R_1 + R_2}\,U_{CC}, \qquad R_i = \frac{R_1\,R_2}{R_1 + R_2}$$

**Schritt 2**: Knotenregel am Emitter mit dem Kollektorstrom $B\,I_B$:

$$I_E = I_B + B\,I_B = (1 + B)\,I_B$$

**Schritt 3**: Maschenregel von der Ersatzquelle über $R_i$, die Basis-Emitter-Strecke und $R_E$ nach Masse:

$$U_q = R_i\,I_B + U_{BE,\mathrm{ein}} + R_E\,(1 + B)\,I_B$$

**Schritt 4** (entscheidender Schritt): Nach dem Basisstrom aufgelöst und mit $B$ multipliziert; Zähler und Nenner werden dabei durch $B$ geteilt:

$$I_C = B\,\frac{U_q - U_{BE,\mathrm{ein}}}{R_i + (1 + B)\,R_E} = \frac{U_q - U_{BE,\mathrm{ein}}}{R_E\,(1 + 1/B) + R_i/B}$$

**Schritt 5**: Für $R_i/B$ klein gegen $R_E$ und $B$ groß gegen 1 bleibt nur $R_E$ im Nenner.

**Ergebnis:**

$$I_C = \frac{U_q - U_{BE,\mathrm{ein}}}{R_E\,(1 + 1/B) + R_i/B}, \qquad I_C \approx \frac{U_q - U_{BE,\mathrm{ein}}}{R_E}$$

**Woher die Faktoren kommen:** $(1 + 1/B)$ entsteht, weil durch $R_E$ der Emitterstrom fließt, nicht der Kollektorstrom; $R_i/B$ ist der Innenwiderstand des Teilers, vom Basis- auf den Kollektorstrom umgerechnet.

**Proben:** Einheit V/Ω = A. Grenzfall $R_i$ = 0, eine feste Basisspannung wie in Schritt 1 des Zusammenspiels:

$$I_C = \frac{U_q - U_{BE,\mathrm{ein}}}{R_E\,(1 + 1/B)}$$

Zahlenwert der allgemeinen Formel: 1,1085 V durch 1114,8 Ω ergibt 0,994 mA; im Grenzfall wären es 1,1085 V durch 1002 Ω, also 1,106 mA.

**Grenzen:** $U_{BE}$ ist in Wirklichkeit kein fester Wert, beim Beispieltransistor 0,65 V statt 0,6 V; da die Differenz im Zähler steht, sollte die Spannung am Emitterwiderstand mindestens etwa 1 V betragen. Die Herleitung gilt nur im aktiven Bereich.
:::

::::beispiel Stromgegenkopplung für 1 mA an 10 V
**Gegeben:** $U_{CC}$ = 10 V, $R_1$ = 330 kΩ, $R_2$ = 68 kΩ, $R_E$ = 1 kΩ, $R_C$ = 3,9 kΩ (Abbildung 3b); Beispieltransistor mit $B$ = 500, Exemplare mit 420 und 800; Modellwert 0,6 V; $U_{BE}$ sinkt bei 1 mA um 2,10 mV je Kelvin.

**Gesucht:** Ersatzquelle, Kollektorstrom und $U_{CE}$ für die drei Exemplare; Temperaturdrift.

**Rechnung:** Ersatzquelle:

$$U_q = \frac{68\ \mathrm{k\Omega}}{398\ \mathrm{k\Omega}}\cdot10\ \mathrm{V} = 1{,}7085\ \mathrm{V}, \qquad R_i = \frac{330\ \mathrm{k\Omega}\cdot68\ \mathrm{k\Omega}}{398\ \mathrm{k\Omega}} = 56{,}4\ \mathrm{k\Omega}$$

Kollektorstrom für $B$ = 500:

$$I_C = \frac{1{,}7085\ \mathrm{V} - 0{,}6\ \mathrm{V}}{1000\ \Omega\cdot1{,}002 + 56{,}4\ \mathrm{k\Omega}/500} = \frac{1{,}1085\ \mathrm{V}}{1114{,}8\ \Omega} = 0{,}994\ \mathrm{mA}$$

Ebenso 0,975 mA für $B$ = 420 und 1,034 mA für $B$ = 800; $U_{CE}$ liegt bei 5,22, 5,13 und 4,93 V. Temperaturdrift:

$$\frac{\Delta I_C}{\Delta T} = \frac{2{,}10\ \mathrm{mV/K}}{1114{,}8\ \Omega} = 1{,}88\ \mu\mathrm{A/K}$$

**Ergebnis:** **0,975 bis 1,034 mA, $U_{CE}$ 4,9 bis 5,2 V, Drift über $U_{BE}$ 0,19 % je Kelvin.**

**Einordnung:** Wo der Basiswiderstand den Strom um den Faktor 1,9 streuen ließ, sind es hier ±3 %, und der Arbeitspunkt bleibt in der Mitte der Geraden. Das vollständige Modell ergibt 0,947 mA, 5 % weniger, weil die echte $U_{BE}$ mit 0,653 V über dem Modellwert liegt; deshalb wählt man die Spannung am Emitterwiderstand nicht kleiner als etwa 1 V. Zur Drift über $U_{BE}$ kommt der Temperaturgang von $B$, 0,5 bis 1 % je Kelvin, der nur zu einem Zehntel durchschlägt: zusammen 0,24 bis 0,29 % je Kelvin.
::::

:::frage
„Warum muss der Strom durch den Teiler viel größer sein als der Basisstrom?“
Der Basisstrom fließt durch den Innenwiderstand des Teilers und senkt die Basisspannung um $R_i\,I_B$; weil $I_B$ mit $B$ schwankt, schwankt diese Absenkung mit. Klein bleibt sie, wenn der Strom durch $R_2$ viel größer ist als der Basisstrom, dann ist $R_i/B$ klein gegen $R_E$. Im Beispiel fließen 23,5 µA durch $R_2$, das 12-Fache von 2 µA Basisstrom, und $R_i/B$ ist mit 113 Ω ein Neuntel von $R_E$; als Faustregel gilt mindestens das Zehnfache. Ein noch steiferer Teiler verringert die Streuung weiter, kostet aber Strom aus der Versorgung.
:::

:::frage
„Kostet der Emitterwiderstand nicht Verstärkung?“
Ja, für Signale wirkt die Gegenkopplung genauso wie für langsame Änderungen und senkt die Spannungsverstärkung. Deshalb überbrückt man den Emitterwiderstand in Verstärkern oft mit einem Kondensator: Für die langsame Arbeitspunkteinstellung ist er da, für das schnelle Signal kurzgeschlossen. Wie das genau wirkt, behandelt [Der Transistor als Verstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker.html).
:::

Das Skript verweist das Temperaturproblem auf eine spätere Veranstaltung (S. 179). Die Stromgegenkopplung löst es zum großen Teil schon: Statt 8 % je Kelvin bei fester $U_{BE}$ ändert sich der Strom im Beispiel um 0,24 bis 0,29 % je Kelvin, rund dreißigmal weniger.

## Spannungsgegenkopplung

*Wie stabilisiert ein Widerstand vom Kollektor zur Basis den Arbeitspunkt, und was kostet das?*

:::grafik
Szene: get1/bipolartransistoren/02-streuung-vergleich · Vorlage: kennlinie-parameter
**Abbildung 5:** Kollektorstrom über der Stromverstärkung von 300 bis 1000 für die drei Schaltungen aus Abbildung 3, einfaches Modell. Mit Basiswiderstand wächst er proportional zu $B$ (1,80 mA bei 420, 3,42 mA bei 800), mit Spannungsgegenkopplung schwächer (2,05 bis 2,72 mA), mit Stromgegenkopplung fast gar nicht (0,975 bis 1,034 mA). Markiert ist die Spanne des BC547C von 420 bis 800. Je stärker der Strom auf seine eigene Ansteuerung zurückwirkt, desto weniger zählt $B$.
:::

Bei der __Spannungsgegenkopplung__ hängt der Basiswiderstand am Kollektor (Abbildung 3c, Skript Bild 11.8). Steigt der Kollektorstrom, fällt mehr Spannung am Kollektorwiderstand ab, $U_{CE}$ sinkt, und am Basiswiderstand liegt weniger Spannung: Der Basisstrom sinkt und bremst den Anstieg. Zurückgeführt wird die Spannung am Ausgang, daher der Name.

:::formel Formel
$$I_C = \frac{U_{CC} - U_{BE,\mathrm{ein}}}{R_C\,(1 + 1/B) + R_B/B}$$
:::

**So liest man das:** $B$ steht nur noch in den Termen $R_B/B$ und $R_C/B$, und $R_C/B$ ist winzig. Ist $R_C$ viel größer als $R_B/B$, bleibt näherungsweise $(U_{CC} - U_{BE,\mathrm{ein}})/R_C$, unabhängig von $B$ (Skript, Gl. 11.2). Was das Skript nicht sagt: Am Basiswiderstand liegt dann nur die kleine Spannung $R_B\,I_B$, $U_{CE}$ rückt also bis auf wenige Zehntelvolt an $U_{BE}$ heran, und der Arbeitspunkt sitzt nahe der Sättigungsgrenze.

Idee der Herleitung: Maschenregel von der Versorgung über $R_C$, $R_B$ und die Basis-Emitter-Strecke.

:::herleitung
**Ausgangspunkt:** die Maschenregel, die Knotenregel am Kollektor und das Ersatzschaltbild des aktiven Bereichs.

**Annahmen:** (i) aktiver Bereich; (ii) Modellwert 0,6 V; (iii) $B$ konstant.

**Schritt 1**: Durch $R_C$ fließen der Kollektorstrom und der Basisstrom, der über $R_B$ zur Basis weiterfließt:

$$U_{CC} = R_C\,(I_C + I_B) + R_B\,I_B + U_{BE,\mathrm{ein}}$$

**Schritt 2** (entscheidender Schritt): Mit dem Basisstrom als Kollektorstrom geteilt durch $B$:

$$U_{CC} - U_{BE,\mathrm{ein}} = I_C\,\Big[R_C\,\Big(1 + \frac{1}{B}\Big) + \frac{R_B}{B}\Big]$$

**Ergebnis:**

$$I_C = \frac{U_{CC} - U_{BE,\mathrm{ein}}}{R_C\,(1 + 1/B) + R_B/B}$$

**Woher die Faktoren kommen:** $(1 + 1/B)$, weil auch der Basisstrom durch $R_C$ fließt; $R_B/B$ ist der Basiswiderstand, auf den Kollektorstrom umgerechnet.

**Proben:** Einheit A. Grenzfall $R_B$ = 0: Basis und Kollektor verbunden, der Transistor wirkt als Diode mit $(U_{CC} - U_{BE,\mathrm{ein}})/(R_C\,(1 + 1/B))$. Zahlenwert mit 10 V, 2,2 kΩ, 1 MΩ und 500: 9,4 V durch 4204 Ω ergibt 2,24 mA.

**Grenzen:** aktiver Bereich; $U_{CE}$ ist hier nie kleiner als $U_{BE}$, die Sättigung erreicht die Schaltung nicht.
:::

Wie stark $B$ noch wirkt, lässt sich direkt an den Spannungen ablesen:

$$\frac{\Delta I_C/I_C}{\Delta B/B} \approx \frac{U_{CE} - U_{BE,\mathrm{ein}}}{U_{CC} - U_{BE,\mathrm{ein}}}$$

Der Bruch ist der Faktor, mit dem eine kleine relative Änderung von $B$ auf den Kollektorstrom durchschlägt. In der Mitte, bei 5,07 V, sind es 0,48: 10 % mehr $B$ ergeben 4,8 % mehr Strom. Klein wird der Faktor nur, wenn $U_{CE}$ nahe an $U_{BE}$ liegt, also nahe der Sättigungsgrenze; dort bleibt kaum Platz für ein Signal. Mitte und Unabhängigkeit von $B$ schließen sich bei dieser Schaltung aus (Abbildung 6). Zum Vergleich: Beim Basiswiderstand ist der Faktor 1, bei der Stromgegenkopplung des Beispiels 0,1.

Idee der Herleitung: Man bildet die relative Änderung des Stroms nach $B$ und drückt Zähler und Nenner durch die Spannungen der Schaltung aus.

:::herleitung
**Ausgangspunkt:** die Formel der Spannungsgegenkopplung und die Masche über den Basiswiderstand.

**Annahmen:** (i) $B$ ist groß gegen 1, sodass $(1 + 1/B)$ gleich 1 gesetzt werden darf; (ii) kleine Änderungen von $B$.

**Schritt 1**: Mit (i) lautet die Formel:

$$I_C = \frac{U_{CC} - U_{BE,\mathrm{ein}}}{R_C + R_B/B}$$

**Schritt 2**: Relative Änderung nach $B$, alle anderen Größen fest; nur der Nenner hängt von $B$ ab, und seine Ableitung nach $B$ ist $-R_B/B^2$:

$$\frac{\Delta I_C/I_C}{\Delta B/B} = \frac{R_B/B}{R_C + R_B/B}$$

**Schritt 3** (entscheidender Schritt): Zähler und Nenner mit $I_C$ erweitert. Oben steht $R_B\,I_B$, die Spannung am Basiswiderstand, also $U_{CE} - U_{BE,\mathrm{ein}}$; unten nach Schritt 1 $U_{CC} - U_{BE,\mathrm{ein}}$:

$$\frac{\Delta I_C/I_C}{\Delta B/B} = \frac{R_B\,I_B}{(R_C + R_B/B)\,I_C} = \frac{U_{CE} - U_{BE,\mathrm{ein}}}{U_{CC} - U_{BE,\mathrm{ein}}}$$

**Ergebnis:**

$$\frac{\Delta I_C/I_C}{\Delta B/B} \approx \frac{U_{CE} - U_{BE,\mathrm{ein}}}{U_{CC} - U_{BE,\mathrm{ein}}}$$

**Woher die Faktoren kommen:** Der Zähler ist der Teil der Spannung, über den $B$ wirkt (am Basiswiderstand), der Nenner die ganze Spannung, die den Strom treibt.

**Proben:** Einheitenlos. Mit 1 MΩ: 4,47 V durch 9,4 V ergibt 0,48; nachgerechnet steigt der Strom von $B$ = 500 auf 600 um 8,6 %, im Mittel also 0,43 je relativer Änderung, etwas weniger, weil der Faktor mit wachsendem $B$ sinkt.

**Grenzen:** für kleine Änderungen; bei großen Sprüngen wie von 420 auf 800 rechnet man besser direkt mit der Formel.
:::

:::grafik
Szene: get1/bipolartransistoren/02-spannungsgk-kompromiss · Vorlage: kennlinie-parameter
**Abbildung 6:** Spannungsgegenkopplung an 10 V mit 2,2 kΩ, zwei gestapelte Diagramme über $R_B$ von 50 kΩ bis 2 MΩ (logarithmisch), je für $B$ = 420 und 800: oben der Kollektorstrom, unten $U_{CE}$. Bei 100 kΩ liegen die Ströme dicht beieinander (3,85 und 4,04 mA), $U_{CE}$ aber nur bei 1,5 und 1,1 V; bei 1 MΩ liegt $U_{CE}$ um die Mitte (5,5 und 4,0 V), dafür streut der Strom von 2,05 bis 2,72 mA. Unabhängigkeit von $B$ gibt es bei dieser Schaltung nur nahe der Sättigung.
:::

::::beispiel Spannungsgegenkopplung: Mitte oder Unabhängigkeit
**Gegeben:** $U_{CC}$ = 10 V, $R_C$ = 2,2 kΩ; (a) $R_B$ = 1 MΩ, (b) $R_B$ = 100 kΩ; Exemplare mit $B$ = 420, 500 und 800; Modellwert 0,6 V.

**Gesucht:** Kollektorstrom und $U_{CE}$.

**Rechnung:** (a) Für $B$ = 500:

$$I_C = \frac{9{,}4\ \mathrm{V}}{2{,}2\ \mathrm{k\Omega}\cdot1{,}002 + 1\ \mathrm{M\Omega}/500} = \frac{9{,}4\ \mathrm{V}}{4204\ \Omega} = 2{,}24\ \mathrm{mA}, \qquad U_{CE} = 5{,}07\ \mathrm{V}$$

Ebenso 2,05 mA bei 5,48 V für 420 und 2,72 mA bei 4,00 V für 800. (b) Für $B$ = 500:

$$I_C = \frac{9{,}4\ \mathrm{V}}{2204\ \Omega + 200\ \Omega} = 3{,}91\ \mathrm{mA}, \qquad U_{CE} = 1{,}38\ \mathrm{V}$$

Ebenso 3,85 mA bei 1,52 V für 420 und 4,04 mA bei 1,10 V für 800.

**Ergebnis:** **(a) Mitte, aber der Strom streut um den Faktor 1,33; (b) nur ±2,4 % Streuung, aber $U_{CE}$ nur 1,1 bis 1,5 V.**

**Einordnung:** (a) streut weniger als der Basiswiderstand mit dem Faktor 1,9, aber viel mehr als die Stromgegenkopplung. (b) hält den Strom fest, lässt nach unten aber nur rund 1 V Aussteuerung. Deshalb ist für Verstärkerstufen die Stromgegenkopplung mit Basisspannungsteiler die Regel.
::::

## Der Stromspiegel

*Wie überträgt man einen Strom genau in einen anderen Zweig?*

:::grafik
Szene: get1/bipolartransistoren/02-stromspiegel · Vorlage: schaltung-und-kennlinie
**Abbildung 7:** (a) Stromspiegel nach Skript Bild 11.15 an 10 V: $T_1$ mit verbundenem Kollektor und Basis über den Referenzwiderstand 10 kΩ an der Versorgung, $T_2$ mit derselben Basis und demselben Emitter, im Kollektorkreis die Last $R_L$. (b) Kollektorstrom von $T_2$ über $U_{CE2}$ von 0 bis 10 V (vollständiges Modell), dazu waagrecht der Referenzstrom 0,935 mA: ab etwa 0,3 V fast waagrecht, bei 1 V gleich dem Referenzstrom, bei 5 V um 5,7 % darüber. Der Spiegel liefert den Referenzstrom an jede Last, solange $T_2$ im aktiven Bereich bleibt.
:::

**Die Akteure:**

- __$T_1$__, __$T_2$__: zwei gleich gebaute Transistoren, möglichst nebeneinander auf einem Chip.
- __$I_\mathrm{ref}$__: __Referenzstrom__, den der Spiegel kopiert; 0,94 mA im Beispiel.
- __$R_\mathrm{ref}$__: Widerstand, der den Referenzstrom einstellt; 10 kΩ. Das Skript nennt ihn $R_C$.
- __$R_L$__: Last, in die der kopierte Strom fließt.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Bei $T_1$ sind Kollektor und Basis verbunden. $U_{CB}$ ist null, $T_1$ kann also nie in Sättigung geraten. Er arbeitet als Diode, deren Spannung $U_{BE}$ sich so einstellt, dass sein Kollektorstrom den Referenzstrom aufnimmt, bis auf die Basisströme: beim Beispieltransistor auf 0,65 V.

**Schritt 2**: $T_2$ hat dieselbe $U_{BE}$, denn Basen und Emitter sind verbunden. Nach der Transfergleichung hängt der Kollektorstrom exponentiell von $U_{BE}$ ab, mit dem Sättigungsstrom als Vorfaktor (Abschnitt *Der Transistoreffekt* in [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html)). $T_2$ führt deshalb denselben Kollektorstrom, sofern er denselben Sättigungsstrom hat. Kopiert wird über die gemeinsame Spannung.

**Schritt 3**: Die Basisströme beider Transistoren stammen aus dem Referenzstrom; für die Kopie bleiben deshalb nur $1/(1 + 2/B)$ davon, bei $B$ = 500 0,4 % weniger.

**Schritt 4**: Diesen Strom liefert $T_2$ in jede Last, solange er im aktiven Bereich bleibt, also bis $U_{CE2}$ auf etwa 0,3 V sinkt: Der Kollektor von $T_2$ ist eine __Stromquelle__. Wegen des Early-Effekts (die Basis von $T_2$ wird mit wachsender Kollektorspannung etwas dünner) steigt der Strom mit $U_{CE2}$ um 1,4 % des Referenzstroms je Volt; bei 5 V liegt er 5,7 % über dem Referenzstrom, mehr als der Fehler durch die Basisströme.

:::formel Formel
$$I_{C2} = \frac{I_\mathrm{ref}}{1 + 2/B}$$
:::

**So liest man das:** Der Ausgangsstrom ist der Referenzstrom, verkleinert um die beiden Basisströme; für großes $B$ ist er gleich dem Referenzstrom (Skript, Gl. 11.3). Er hängt nicht von der Last ab, nur vom Referenzzweig. Mehrere Transistoren an derselben Basisleitung liefern mehrere Kopien, ein Transistor mit doppelter Emitterfläche den doppelten Strom; so lässt sich ein Strom auch vervielfachen.

Idee der Herleitung: Gleiche Spannung an gleichen Transistoren ergibt gleiche Ströme; die Knotenregel am Referenzzweig verteilt den Referenzstrom.

:::herleitung
**Ausgangspunkt:** die Transfergleichung aus [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html) und die Knotenregel.

**Annahmen:** (i) beide Transistoren haben denselben Sättigungsstrom und dieselbe Temperatur; (ii) beide sind im aktiven Bereich; (iii) der Early-Effekt bleibt außer Acht; (iv) $B$ ist für beide gleich und konstant.

**Schritt 1**: Den Referenzstrom liefert die Masche über den Referenzwiderstand und $T_1$:

$$I_\mathrm{ref} = \frac{U_{CC} - U_{BE,\mathrm{ein}}}{R_\mathrm{ref}}$$

**Schritt 2**: Gleiche $U_{BE}$ und nach (i) gleicher Sättigungsstrom ergeben nach der Transfergleichung gleiche Kollektorströme; nach (iv) sind auch die Basisströme gleich:

$$I_{C1} = I_{C2}, \qquad I_{B1} = I_{B2} = \frac{I_{C2}}{B}$$

**Schritt 3** (entscheidender Schritt): Knotenregel am Kollektor von $T_1$: Der Referenzstrom teilt sich in den Kollektorstrom von $T_1$ und die beiden Basisströme:

$$I_\mathrm{ref} = I_{C1} + I_{B1} + I_{B2} = I_{C2}\,\Big(1 + \frac{2}{B}\Big)$$

**Ergebnis:**

$$I_{C2} = \frac{I_\mathrm{ref}}{1 + 2/B}$$

**Woher die Faktoren kommen:** Die 2 zählt die beiden Basisströme, die beide aus dem Referenzzweig gespeist werden.

**Proben:** Einheit A. Grenzfall unendliches $B$: exakte Kopie. Zahlenwert: 0,94 mA durch 1,004 ergibt 0,936 mA.

**Grenzen:** (iii) versagt, sobald $U_{CE2}$ von $U_{BE}$ abweicht: Bei 5 V liegt der Strom 6,2 % über dem Wert bei gleichen Spannungen und 5,7 % über dem Referenzstrom; (i) bei ungleichen Transistoren: 10 % mehr Sättigungsstrom ergeben 10 % mehr Strom, 1 K Temperaturunterschied 8 %.
:::

::::beispiel Ein Stromspiegel für 0,94 mA an 10 V
**Gegeben:** $U_{CC}$ = 10 V, $R_\mathrm{ref}$ = 10 kΩ, Beispieltransistoren mit $B$ = 500 (zum Vergleich 420 und 800); Modellwert 0,6 V.

**Gesucht:** Referenzstrom, kopierter Strom, größte Last.

**Rechnung:** Referenzstrom und Kopie:

$$I_\mathrm{ref} = \frac{10\ \mathrm{V} - 0{,}6\ \mathrm{V}}{10\ \mathrm{k\Omega}} = 0{,}94\ \mathrm{mA}, \qquad I_{C2} = \frac{0{,}94\ \mathrm{mA}}{1 + 2/500} = 0{,}936\ \mathrm{mA}$$

Für $B$ = 420 und 800 ergeben sich 0,9355 und 0,9377 mA. Die Kopie hält, bis $U_{CE2}$ auf 0,3 V sinkt:

$$R_{L,\mathrm{max}} = \frac{10\ \mathrm{V} - 0{,}3\ \mathrm{V}}{0{,}936\ \mathrm{mA}} = 10{,}4\ \mathrm{k\Omega}$$

**Ergebnis:** **0,936 mA für jede Last bis 10,4 kΩ; die Streuung von $B$ zwischen 420 und 800 ändert ihn um 0,23 %.**

**Einordnung:** Das vollständige Modell ergibt einen Referenzstrom von 0,935 mA und als Kopie 0,931 mA bei $U_{CE2}$ = 0,65 V, 0,988 mA bei 5 V und 1,054 mA bei 10 V: Der Early-Effekt ist der größte Fehler. In integrierten Schaltungen gleicht man ihn mit verbesserten Spiegeln aus; die Paarung erreicht man, indem beide Transistoren nebeneinander auf demselben Chip entstehen.
::::

:::fehlvorstellung
„Der Spiegel kopiert den Strom, weil beide Basen denselben Basisstrom bekommen.“
Das liegt nahe, weil die Basen verbunden sind und das Skript mit Basisströmen rechnet. Kopiert wird aber über die gemeinsame Spannung $U_{BE}$: Gleiche Spannung an gleichen Übergängen ergibt nach der Transfergleichung gleiche Kollektorströme, die gleichen Basisströme sind erst die Folge. Deshalb versagt der Spiegel bei ungleichen Transistoren: Hat $T_2$ 10 % mehr Sättigungsstrom, liefert er bei derselben Spannung 10 % mehr Strom.
:::

:::frage
„Warum sollen die beiden Transistoren auf einem Chip sitzen?“
Weil der Spiegel nur bei gleichem Sättigungsstrom und gleicher Temperatur kopiert. Der Sättigungsstrom wächst mit der Emitterfläche und hängt von Dotierung und Basisweite ab; auf einem Chip entstehen beide Transistoren im selben Prozessschritt und gleichen sich auf wenige Prozent. Bei gleicher $U_{BE}$ wächst der Strom außerdem um 8 % je Kelvin: Ist $T_2$ nur 1 K wärmer als $T_1$, liefert er 8 % mehr. Spiegel aus Einzeltransistoren bekommen deshalb oft Emitterwiderstände, die als Stromgegenkopplung die Unterschiede dämpfen.
:::

## Der Inverter

*Wie wird aus dem Transistor ein logisches Nicht-Glied?*

:::grafik
Szene: get1/bipolartransistoren/02-inverter · Vorlage: schaltung-und-kennlinie
**Abbildung 8:** (a) Inverter nach Skript Bild 11.16: Eingang über $R_B$ = 10 kΩ an der Basis, $R_C$ = 1 kΩ an 5 V, Ausgang am Kollektor. (b) Ausgangsspannung über der Eingangsspannung von 0 bis 2 V. Modell: waagrecht bei 5 V bis 0,6 V, dann eine Gerade mit der Steigung −50 bis auf 0,2 V bei 0,696 V, danach waagrecht. Vollständiges Modell (gestrichelt): weicher, 4,89 V bei 0,6 V, 3,41 V bei 0,7 V, 0,25 V bei 0,8 V. Der Arbeitspunkt durchläuft alle drei Bereiche; zwischen den Pegeln liegt ein schmaler Übergang.
:::

Ein __Inverter__ kehrt ein logisches Signal um (Skript, S. 186–188). Ist die Eingangsspannung kleiner als 0,6 V, sperrt der Transistor, durch $R_C$ fließt kein Strom, und am Ausgang liegt die Versorgung: Eingang 0, Ausgang 1. Ist sie groß genug, sättigt er, und am Ausgang liegen 0,2 V: Eingang 1, Ausgang 0. Dazwischen läuft der Arbeitspunkt durch den aktiven Bereich, und der Ausgang fällt mit der Steigung $-B\,R_C/R_B$; dort ist der Pegel weder 0 noch 1. Abbildung 8 zeigt die Kennlinie.

**Die Akteure:**

- __$U_{\mathrm{ein,sat}}$__: Eingangsspannung, ab der der Transistor gesättigt ist; das Skript nennt sie $U_{E,\mathrm{sat}}$.

:::formel Formel
$$U_{\mathrm{ein,sat}} = \frac{(U_{CC} - U_{CE,\mathrm{sat}})\,R_B}{B\,R_C} + U_{BE,\mathrm{ein}}$$
:::

**So liest man das:** Der erste Summand ist die Breite des Übergangs oberhalb von 0,6 V; sie ist klein, wenn $R_B$ klein gegen $B\,R_C$ ist. Mit 10 kΩ, 1 kΩ und $B$ = 500 sind es 96 mV. Weil $B$ streut, verschiebt sich die Kante, bei 420 auf 0,714 V. Im Skript fehlen in dieser Formel (Gl. 11.4, S. 188) und in der Zeile davor der Widerstand $R_C$ und die Klammer um die Differenz aus $U_{CC}$ und $U_{CE,\mathrm{sat}}$; ergänzt man nur $R_C$, ergeben sich 5,6 V statt 0,696 V. Auf S. 187 steht außerdem „0,6 Ω“ statt 0,6 V.

Idee der Herleitung: Man setzt die Ausgangsspannung des aktiven Bereichs gleich der Sättigungsspannung und löst nach dem Eingang auf.

:::herleitung
**Ausgangspunkt:** die Formeln des Basiswiderstands (Abschnitt *Der Basiswiderstand und warum der Arbeitspunkt wandert*) mit der Ausgangsspannung am Kollektor.

**Annahmen:** (i) Modellwerte 0,6 V und 0,2 V; (ii) $B$ konstant; (iii) der Ausgang ist unbelastet.

**Schritt 1**: Im aktiven Bereich gilt:

$$U_\mathrm{aus} = U_{CE} = U_{CC} - B\,R_C\,\frac{U_\mathrm{ein} - U_{BE,\mathrm{ein}}}{R_B}$$

**Schritt 2** (entscheidender Schritt): Am Rand der Sättigung ist $U_\mathrm{aus}$ gleich $U_{CE,\mathrm{sat}}$; nach dem Eingang aufgelöst:

$$U_\mathrm{ein} - U_{BE,\mathrm{ein}} = \frac{(U_{CC} - U_{CE,\mathrm{sat}})\,R_B}{B\,R_C}$$

**Ergebnis:**

$$U_{\mathrm{ein,sat}} = \frac{(U_{CC} - U_{CE,\mathrm{sat}})\,R_B}{B\,R_C} + U_{BE,\mathrm{ein}}$$

**Woher die Faktoren kommen:** $(U_{CC} - U_{CE,\mathrm{sat}})/R_C$ ist der Kollektorstrom in der Sättigung, geteilt durch $B$ der dafür nötige Basisstrom, mal $R_B$ die Spannung, die er am Basiswiderstand braucht.

**Proben:** Einheit V. Grenzfall $R_B$ = 0: Die Kante liegt bei 0,6 V, der Übergang ist senkrecht. Zahlenwert: 4,8 V mal 10 kΩ durch 500 kΩ ergibt 96 mV, also 0,696 V.

**Grenzen:** Im vollständigen Modell ist $U_{BE}$ nicht fest; der Übergang ist dort etwa doppelt so breit.
:::

::::beispiel Inverter an 5 V mit 3,3-V-Ansteuerung
**Gegeben:** $U_{CC}$ = 5 V, $R_C$ = 1 kΩ, $R_B$ = 10 kΩ; Beispieltransistor mit $B$ = 500, BC547C mindestens 420; Eingang 0 V oder 3,3 V von einem Mikrocontroller; Modellwerte 0,6 V und 0,2 V, für die Übersteuerung 0,7 V.

**Gesucht:** Kante der Sättigung, Steigung, Übersteuerung bei 3,3 V.

**Rechnung:** Kante und Steigung:

$$U_{\mathrm{ein,sat}} = \frac{4{,}8\ \mathrm{V}\cdot10\ \mathrm{k\Omega}}{500\cdot1\ \mathrm{k\Omega}} + 0{,}6\ \mathrm{V} = 0{,}696\ \mathrm{V}, \qquad -\frac{B\,R_C}{R_B} = -50$$

Basisstrom bei 3,3 V und Bedarf für die Sättigung mit $B$ = 420:

$$I_B = \frac{3{,}3\ \mathrm{V} - 0{,}7\ \mathrm{V}}{10\ \mathrm{k\Omega}} = 0{,}26\ \mathrm{mA}, \qquad \frac{4{,}8\ \mathrm{mA}}{420} = 11{,}4\ \mu\mathrm{A}$$

**Ergebnis:** **Kante bei 0,70 V (0,71 V für $B$ = 420), Steigung −50; bei 3,3 V fließt 23-mal so viel Basisstrom, wie die Sättigung braucht (23-fache Übersteuerung).**

**Einordnung:** Die logischen Pegel 0 V und 3,3 V liegen weit von der Kante entfernt; die Streuung von $B$ verschiebt sie nur um Hundertstelvolt. Das vollständige Modell liefert bei 3,3 V am Ausgang 0,067 V, tiefer als die 0,2 V des Modells.
::::

:::frage
„Warum ist der Übergang in Wirklichkeit breiter als im Modell?“
Im Modell bleibt $U_{BE}$ bei 0,6 V, während der Strom von null auf 4,8 mA steigt. Tatsächlich wächst $U_{BE}$ dabei, um 60 mV je Zehnfaches des Stroms, und diese Spannung fehlt am Basiswiderstand. Im vollständigen Modell fällt der Ausgang deshalb zwischen 0,6 und 0,8 V statt zwischen 0,6 und 0,7 V. Für die Logik ist das unerheblich, solange die Pegel weit genug entfernt sind.
:::

## Die drei Grundschaltungen

*Welche Möglichkeiten gibt es, einen Transistor zwischen Eingang und Ausgang zu schalten?*

:::grafik
Szene: get1/bipolartransistoren/02-grundschaltungen · Vorlage: schaltung-und-kennlinie
**Abbildung 9:** Die drei Grundschaltungen an 5 V mit ihren Gleichspannungskennlinien (vollständiges Modell). (a) Emitterschaltung: Eingang über 10 kΩ an der Basis, Ausgang am Kollektor mit 1 kΩ; fallende Kennlinie wie der Inverter. (b) Kollektorschaltung: Kollektor an 5 V, Eingang an der Basis, Ausgang am Emitter mit 1 kΩ nach Masse; Ausgang folgt dem Eingang um gut 0,6 V tiefer (1,34 V bei 2 V, 4,31 V bei 5 V). (c) Basisschaltung: Basis an Masse, Eingang über 1 kΩ am Emitter (negative Spannungen), Ausgang am Kollektor mit 1 kΩ; steigende Kennlinie (4,63 V bei −1 V, 2,68 V bei −3 V, 0,70 V bei −5 V). Welcher Anschluss Ein- und Ausgang gemeinsam ist, bestimmt, ob die Schaltung umkehrt, folgt oder nicht umkehrend überträgt.
:::

Ein- und Ausgangsspannung misst man gegen denselben Bezugspunkt, der Transistor hat aber nur drei Anschlüsse. Einer gehört deshalb zu Eingang und Ausgang zugleich; er gibt der __Grundschaltung__ ihren Namen (Skript, S. 190–192). Auch der Kollektor an der Versorgung zählt als gemeinsamer Anschluss: Ein Signal ist eine Änderung, und eine konstante Quelle trägt zu Änderungen nichts bei; für das Signal wirkt sie wie Masse ([Überlagerungsverfahren](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/superpositionsverfahren.html)).

| Grundschaltung | Ein- und Ausgang, Verhalten |
|---|---|
| Emitterschaltung | Eingang an der Basis, Ausgang am Kollektor; Kennlinie fallend und steil, mit Basiswiderstand der Inverter; Stromverstärkung $B$ |
| Kollektorschaltung (Emitterfolger) | Eingang an der Basis, Ausgang am Emitter; Kennlinie steigend, Ausgang um $U_{BE}$ tiefer, Steigung knapp 1; Stromverstärkung $B + 1$ |
| Basisschaltung | Eingang am Emitter, Ausgang am Kollektor; Kennlinie steigend, nicht umkehrend; Stromverstärkung knapp 1 |

Die __Emitterschaltung__ ist der Inverter des vorigen Abschnitts. Ohne Basiswiderstand, wie in Bild 11.22 des Skripts, liegt der Eingang direkt als $U_{BE}$ an, und der Übergang ist noch schmaler: Beim Beispieltransistor fällt der Ausgang zwischen 0,62 und 0,70 V von 4,7 V auf 0,08 V. Das Skript nennt ihre Kennlinie „dieselbe wie in Abb. 11.18“ (S. 190); gemeint ist Bild 11.17, Bild 11.18 zeigt den Zeitverlauf.

Die __Kollektorschaltung__ heißt auch __Emitterfolger__: Die Ausgangsspannung am Emitter folgt der Eingangsspannung an der Basis, um die Basis-Emitter-Spannung tiefer.

:::formel Formel
$$U_\mathrm{aus} = U_\mathrm{ein} - U_{BE,\mathrm{ein}}$$
:::

**So liest man das:** Solange der Transistor leitet, ist der Ausgang der Eingang minus 0,6 V; die Spannungsverstärkung ist knapp 1, im vollständigen Modell 0,985. Die Stromverstärkung ist $B + 1$: Die Quelle am Eingang liefert nur den Basisstrom, die Last bekommt den Emitterstrom.

Idee der Herleitung: Maschenregel vom Eingang über die Basis-Emitter-Strecke zum Ausgang.

:::herleitung
**Ausgangspunkt:** die Maschenregel und das Ersatzschaltbild des aktiven Bereichs.

**Annahmen:** (i) aktiver Bereich, also Eingang über 0,6 V und unter der Versorgung; (ii) Modellwert 0,6 V.

**Schritt 1**: Der Umlauf vom Eingang (Basis gegen Masse) über die Basis-Emitter-Quelle zum Ausgang (Emitter gegen Masse) ergibt:

$$U_\mathrm{ein} = U_{BE,\mathrm{ein}} + U_\mathrm{aus}$$

**Schritt 2** (entscheidender Schritt): Nach dem Ausgang aufgelöst:

$$U_\mathrm{aus} = U_\mathrm{ein} - U_{BE,\mathrm{ein}}$$

**Ergebnis:**

$$U_\mathrm{aus} = U_\mathrm{ein} - U_{BE,\mathrm{ein}}$$

**Woher die Faktoren kommen:** Der Faktor 1 vor dem Eingang: Zwischen Basis und Emitter liegt nur eine feste Quelle, jede Änderung am Eingang erscheint unverändert am Ausgang.

**Proben:** Einheit V. Grenzfall Eingang unter 0,6 V: Der Transistor sperrt, der Ausgang liegt auf null, die Formel gilt nicht mehr. Zahlenwert: 2 V ergeben 1,4 V, im vollständigen Modell 1,34 V.

**Grenzen:** Im vollständigen Modell wächst $U_{BE}$ mit dem Strom leicht an, die Steigung ist deshalb etwas kleiner als 1.
:::

::::beispiel Emitterfolger an 5 V
**Gegeben:** Kollektor an 5 V, Emitterwiderstand 1 kΩ nach Masse, Eingang 2 V; Beispieltransistor mit $B$ = 500; Modellwert 0,6 V.

**Gesucht:** Ausgangsspannung, Emitter- und Basisstrom.

**Rechnung:**

$$U_\mathrm{aus} = 2\ \mathrm{V} - 0{,}6\ \mathrm{V} = 1{,}4\ \mathrm{V}, \qquad I_E = \frac{1{,}4\ \mathrm{V}}{1\ \mathrm{k\Omega}} = 1{,}4\ \mathrm{mA}, \qquad I_B = \frac{1{,}4\ \mathrm{mA}}{501} = 2{,}8\ \mu\mathrm{A}$$

**Ergebnis:** **1,4 V am Ausgang; die Quelle liefert 2,8 µA, die Last bekommt 1,4 mA.**

**Einordnung:** Das vollständige Modell ergibt 1,34 V, weil $U_{BE}$ bei 1,3 mA 0,663 V beträgt. Von der Quelle aus wirkt der Emitterwiderstand rund 500-mal größer, etwa 0,5 MΩ: Der Emitterfolger trennt eine hochohmige Quelle von einer niederohmigen Last.
::::

:::fehlvorstellung
„Die Kollektorschaltung verstärkt nicht, ihr Ausgang ist ja sogar kleiner als der Eingang.“
Das liegt nahe, weil die Spannungsverstärkung knapp unter 1 liegt. Verstärkt wird aber der Strom, um den Faktor $B + 1$: Im Beispiel liefert die Quelle 2,8 µA, die Last bekommt 1,4 mA. Die Quelle gibt dabei 5,6 µW ab, an der Last kommen 1,96 mW an, das 350-Fache; den Unterschied liefert die Versorgung. Deshalb steht der Emitterfolger überall, wo eine schwache Quelle eine Last treiben soll.
:::

Bei der __Basisschaltung__ liegt die Basis an Masse, das Signal kommt an den Emitter, der Ausgang ist der Kollektor. Fast der ganze Eingangsstrom kommt als Kollektorstrom heraus; die Stromverstärkung ist knapp 1, nämlich $\alpha$, das Verhältnis von Kollektor- zu Emitterstrom. Mit 1 kΩ vor dem Emitter steigt der Ausgang mit dem Eingang an: Wird die Eingangsspannung weniger negativ, sinkt der Strom aus dem Emitter, mit ihm der Kollektorstrom und der Abfall an $R_C$. Die Steigung beträgt 0,98 (Abbildung 9c), die Schaltung kehrt nicht um.

Das Skript stellt fest, dass die größte Steigung der Basisschaltung größer ist als die der Emitterschaltung (S. 191). Für die gezeichneten Schaltungen ohne Vorwiderstand trifft das zu, der Grund ist aber keine stärkere Steuerwirkung: In beiden Schaltungen legt die Eingangsspannung unmittelbar $U_{BE}$ fest, und bei gleichem Kollektorstrom sind beide Steigungen gleich groß, beim Beispieltransistor bei 2,5 mA −93,5 und +93,5. Die Basisschaltung kann aber mehr Strom führen, bevor sie sättigt, denn ihr Kollektor darf bis etwa −0,4 V unter Masse sinken, während der Kollektor der Emitterschaltung über etwa 0,25 V bleiben muss. Am Rand der Sättigung erreicht sie deshalb +194 bei 5,41 mA, die Emitterschaltung −170 bei 4,72 mA.

Dass sich die Skriptbilder 11.23 und 11.27 viel stärker unterscheiden, liegt an Bild 11.23: Seine Kennlinie fällt über rund 0,5 V Eingangsspannung statt über weniger als 0,1 V wie bei direkter Ansteuerung; das Skript nennt sie selbst dieselbe Kennlinie wie die des Inverters, also mit Basiswiderstand. Wie sich die drei Schaltungen für kleine Signale verhalten, behandelt [Der Transistor als Verstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker.html).

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Arbeitsgerade und Grenzen | Der Kollektorkreis legt fest, welche Punkte möglich sind, der Transistor, welche zulässig sind. |
| Basiswiderstand | $B$ geht voll ein; der Arbeitspunkt wandert mit jedem Exemplar und mit der Temperatur. |
| Strom­gegen­kopplung | Der Emitterwiderstand setzt den Strom; $B$ und $U_{BE}$ bleiben kleine Korrekturen. |
| Spannungs­gegen­kopplung | Rückwirkung über $U_{CE}$; je unabhängiger von $B$, desto näher an der Sättigung. |
| Stromspiegel | Gleiche Spannung an gleichen Transistoren: Die unsicheren Kennwerte kürzen sich heraus. |
| Inverter | Der Arbeitspunkt läuft gezielt vom Sperr- in den Sättigungsbereich. |
| Grundschaltungen | Der gemeinsame Anschluss bestimmt, wie Strom und Spannung übertragen werden. |

Der Arbeitspunkt eines Transistors ist der Punkt, an dem seine Kennlinien und die Gleichungen der äußeren Schaltung zugleich gelten; gute Schaltungen legen ihn so fest, dass die unsicheren Kennwerte des Transistors, Stromverstärkung und Basis-Emitter-Spannung, kaum eingehen: durch Gegenkopplung oder dadurch, dass sie sich wie im Stromspiegel herauskürzen.

## Bedeutung und Ausblick

Die Stromgegenkopplung mit Basisspannungsteiler ist die übliche Arbeitspunkteinstellung diskreter Verstärkerstufen. Stromspiegel stecken in jedem Operationsverstärker, als Stromquellen für die Stufen und als aktive Lasten. Inverter aus einem Transistor schalten Leuchtdioden und Relais und setzen Logikpegel um, und der Emitterfolger entkoppelt Quellen von Lasten.

Diese Rechnungen benutzen das einfache Modell mit festen 0,6 V und konstantem $B$; das vollständige Modell weicht davon in den Arbeitspunkten beim Kollektorstrom um bis zu 5 % ab und bei $U_{CE}$ um bis zu 0,3 V, beim Stromspiegel wegen des Early-Effekts um mehr. Wie die Schaltungen kleine Signale verstärken, welche Rolle der Early-Effekt dabei spielt und wie man Emitterwiderstände für Signale überbrückt, zeigt der nächste Artikel, [Der Transistor als Verstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker.html).

:::kern
- Arbeitspunkt: Schnittpunkt von Kennlinie und Arbeitsgerade $U_{CE} = U_{CC} - R_C\,I_C$; Verstärker in der Mitte, Schalter zwischen Sperrbereich und Sättigung.
- Betriebsgrenzen: höchste Spannung, höchster Strom und die Hyperbel der Verlustleistung; die größte Leistung liegt in der Mitte der Geraden.
- Lineare Ersatzschaltbilder: Basis-Emitter eine 0,6-V-Quelle, Kollektor-Emitter eine Stromquelle $B\,I_B$ oder eine 0,2-V-Quelle; rechnen mit Annahme und Probe.
- Mit Basiswiderstand ist der Kollektorstrom $B$-mal der Basisstrom und wandert mit $B$ und Temperatur.
- Stromgegenkopplung: $I_C \approx (U_q - U_{BE})/R_E$; $B$ und Temperatur wirken nur noch als Korrektur.
- Spannungsgegenkopplung: Unabhängigkeit von $B$ gibt es nur nahe der Sättigung.
- Stromspiegel: $I_{C2} = I_\mathrm{ref}/(1 + 2/B)$; kopiert wird über die gleiche $U_{BE}$ gleicher Transistoren.
- Grundschaltungen: Emitterschaltung kehrt um, Kollektorschaltung folgt um $U_{BE}$ tiefer, Basisschaltung überträgt nicht umkehrend.
:::

:::quiz
F: Warum wandert der Arbeitspunkt mit einem Basiswiderstand so stark?
A: Der Basiswiderstand legt nur den Basisstrom fest; der Kollektorstrom ist dessen $B$-Faches und folgt jeder Streuung von $B$. Mit 2,2 MΩ an 10 V liefern BC547C mit $B$ = 420 und 800 1,80 und 3,42 mA, der Arbeitspunkt liegt bei 6,1 bzw. 2,5 V.
F: Warum macht ein Emitterwiderstand den Kollektorstrom fast unabhängig von $B$?
A: Bei fester Basisspannung liegt am Emitterwiderstand die Basisspannung minus $U_{BE}$, und sie legt den Emitterstrom fest. Steigt der Strom, steigt die Spannung am Widerstand, $U_{BE}$ sinkt, und der Strom geht zurück; $B$ bleibt nur in kleinen Korrekturen.
F: Wie groß ist der Kollektorstrom der Stromgegenkopplung mit 330 kΩ, 68 kΩ und 1 kΩ an 10 V, und wie stark streut er?
A: Die Ersatzquelle hat 1,7085 V und 56,4 kΩ; mit $B$ = 500 fließen 1,1085 V durch 1114,8 Ω, also 0,994 mA. Für 420 und 800 sind es 0,975 und 1,034 mA, nur ±3 %.
F: Warum liegt die größte Verlustleistung in der Mitte der Arbeitsgeraden?
A: Längs der Geraden ist die Leistung $U_{CE}$ mal $(U_{CC} - U_{CE})/R_C$, eine Parabel mit Nullstellen bei 0 und $U_{CC}$; ihr Scheitel liegt bei $U_{CC}/2$. Bei 10 V und 2,2 kΩ sind es 11,4 mW.
F: Stimmt es, dass man mit dem Basiswiderstand den Kollektorstrom einstellt?
A: Nein. Er stellt den Basisstrom ein; der Kollektorstrom ist dessen $B$-Faches und streut mit $B$. Einen festen Kollektorstrom liefert erst eine Gegenkopplung, etwa mit Emitterwiderstand.
F: Was ist der Haken der Spannungsgegenkopplung?
A: Die relative Empfindlichkeit gegen $B$ ist $(U_{CE} - U_{BE})/(U_{CC} - U_{BE})$. In der Mitte sind das 0,48; unabhängig wird der Strom erst, wenn $U_{CE}$ nahe an $U_{BE}$ liegt, also nahe der Sättigungsgrenze, wo kaum Aussteuerung bleibt.
F: Warum kopiert der Stromspiegel den Strom?
A: $T_1$ stellt als Diode seine $U_{BE}$ auf den Referenzstrom ein, und $T_2$ hat dieselbe $U_{BE}$; gleiche Spannung an gleichen Transistoren ergibt nach der Transfergleichung gleiche Ströme. Die beiden Basisströme kosten den Faktor $1/(1 + 2/B)$, bei 500 0,4 %.
F: Stimmt es, dass der Spiegel kopiert, weil beide Basen denselben Strom bekommen?
A: Nein. Kopiert wird über die gemeinsame Spannung $U_{BE}$; gleiche Basisströme sind die Folge. Bei ungleichen Transistoren versagt die Kopie: 10 % mehr Sättigungsstrom ergeben 10 % mehr Strom, 1 K Temperaturunterschied 8 %.
F: Bei welcher Eingangsspannung sättigt der Inverter mit 10 kΩ, 1 kΩ und $B$ = 500 an 5 V?
A: 4,8 V mal 10 kΩ durch 500 mal 1 kΩ ergibt 96 mV, dazu 0,6 V: 0,696 V. Mit $B$ = 420 sind es 0,714 V.
F: Stimmt es, dass die Kollektorschaltung nicht verstärkt?
A: Nein. Ihre Spannungsverstärkung ist knapp 1, aber sie verstärkt den Strom um $B + 1$. Im Beispiel liefert die Quelle 2,8 µA, die Last bekommt 1,4 mA.
:::
