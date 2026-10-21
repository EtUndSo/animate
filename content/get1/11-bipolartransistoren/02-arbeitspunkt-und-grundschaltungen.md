---
title: Arbeitspunkt und Grundschaltungen des Transistors
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Bipolartransistoren
order: 110200
summary: Wie man einen Bipolartransistor in seinen Arbeitspunkt bringt und dort hält, obwohl Stromverstärkung und Basis-Emitter-Spannung streuen: Arbeitsgerade und Betriebsgrenzen, lineare Ersatzschaltbilder, Basiswiderstand, Strom- und Spannungsgegenkopplung, Stromspiegel, Inverter und die drei Grundschaltungen. Kompakte Fassung; die ausführliche enthält zusätzlich die größte Verlustleistung, den Kompromiss der Spannungsgegenkopplung, die Grenzen des Stromspiegels und weitere Beispiele.
tags: Arbeitspunkt, Basisspannungsteiler, Emitterwiderstand, Gegenkopplung, Emitterschaltung, Kollektorschaltung, Basisschaltung
stil: 3
fassung: kompakt
---

## Worum es geht

Bevor ein Transistor verstärkt oder schaltet, muss die Schaltung festlegen, welcher Kollektorstrom bei welcher Spannung fließt. Seine Kennwerte sind dabei unsicher: Die Stromverstärkung $B$ liegt beim BC547C, der Verstärkungsgruppe C des BC547, zwischen 420 und 800, und die Basis-Emitter-Spannung sinkt um 2 mV je Kelvin.
**Der Arbeitspunkt eines Transistors ist der Punkt, an dem seine Kennlinien und die Gleichungen der äußeren Schaltung zugleich gelten; gute Schaltungen legen ihn so fest, dass die unsicheren Kennwerte des Transistors, Stromverstärkung und Basis-Emitter-Spannung, kaum eingehen: durch Gegenkopplung oder dadurch, dass sie sich wie im Stromspiegel herauskürzen.**

Vorausgesetzt werden die Arbeitsbereiche und Annahme und Probe aus [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html), die Arbeitsgerade aus [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html) und die Ersatzspannungsquelle aus [Ersatzquellen nach Thévenin und Norton](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/ersatzquellen-thevenin-norton.html).

:::grafik
Szene: get1/bipolartransistoren/02-arbeitsgerade-grenzen · Vorlage: kennlinienfeld-arbeitsgerade
**Abbildung 1:** (a) Ausgangskennlinienfeld des Beispieltransistors (BC547C-artig, $I_B$ = 2 bis 10 µA) mit der Arbeitsgeraden eines Kollektorwiderstands von 2,2 kΩ an 10 V, von (10 V; 0) nach (0; 4,55 mA), und dem Arbeitspunkt in der Mitte bei 5,1 V und 2,23 mA. (b) Größerer Maßstab bis 50 V und 160 mA mit den Grenzen des BC547: 45 V, 100 mA und die Hyperbel der höchsten Verlustleistung von 625 mW. Die Gerade aus (a) liegt dicht am Ursprung; eine zweite Gerade, 200 Ω an 30 V, schneidet die Hyperbel und reicht über 100 mA hinaus. Der Arbeitspunkt ist der Schnittpunkt von Kennlinie und Arbeitsgerade; jede Gerade muss in den Grenzen bleiben.
:::

## Arbeitspunkt, Arbeitsgerade und Betriebsgrenzen

*Wo arbeitet ein Transistor in einer Schaltung, und welche Arbeitspunkte verträgt er?*

**Die Akteure:**

- __$U_{CC}$__, __$R_C$__: Versorgungsspannung und __Kollektorwiderstand__ des Kollektorkreises; 10 V und 2,2 kΩ im Beispiel.
- __Arbeitspunkt__: das Paar aus Kollektorstrom und $U_{CE}$, bei dem der Transistor ohne Signal arbeitet.

**Das Zusammenspiel:** Das Kennlinienfeld des Transistors gibt vor, welcher Kollektorstrom bei welcher Spannung fließen kann. Der Kollektorkreis setzt eine zweite Bedingung: Was am Kollektorwiderstand abfällt, fehlt an $U_{CE}$. Beide zusammen lassen nur einen Punkt zu, den __Arbeitspunkt__ (Abbildung 1).

:::formel Gesetz
$$U_{CE} = U_{CC} - R_C\,I_C$$
:::

**So liest man das:** Die __Arbeitsgerade__ verbindet den Leerlauf, 10 V ohne Strom, mit dem Kurzschlussstrom $U_{CC}/R_C$, hier 4,55 mA. Alle Arbeitspunkte, die der Kollektorkreis zulässt, liegen auf ihr.

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

Als __Schalter__ springt der Transistor zwischen den Endpunkten, gesperrt (10 V, kein Strom) und gesättigt (0,2 V, 4,45 mA); in beiden setzt er kaum Leistung um (Skript, S. 178). Als __Verstärker__ arbeitet er im aktiven Bereich, am besten in der Mitte zwischen Sättigungsgrenze und Versorgung, damit ein Signal in beide Richtungen gleich weit ausschlagen kann: bei 5,1 V und 2,23 mA. Dabei darf er seine __Betriebsgrenzen__ nicht überschreiten, beim BC547 45 V, 100 mA und 625 mW __Verlustleistung__, das Produkt aus $U_{CE}$ und $I_C$, das als Wärme abgeführt werden muss. Weil dieses Produkt an der Grenze konstant ist, bildet sie im Kennlinienfeld eine Hyperbel (Skript, S. 181–182, Bild 11.9). Längs der Arbeitsgeraden wächst die Spannung, während der Strom sinkt, und ihr Produkt ist bei halber Versorgungsspannung am größten; in der Mitte setzt der Transistor 11,4 mW um. Die Gerade mit 200 Ω an 30 V in Abbildung 1 wäre unzulässig, weil sie über 100 mA und 625 mW hinausreicht.

## Die linearen Ersatzschaltbilder

*Wie rechnet man mit einem Transistor wie mit einem gewöhnlichen Netzwerk?*

:::grafik
Szene: get1/bipolartransistoren/02-ersatzschaltbilder · Vorlage: schaltung-zustaende
**Abbildung 2:** Die linearen Ersatzschaltbilder des npn-Transistors nach dem Skript. (a) Sperrbereich: alle drei Anschlüsse offen. (b) Aktiver Bereich: zwischen Basis und Emitter eine Spannungsquelle 0,6 V, zwischen Kollektor und Emitter eine gesteuerte Stromquelle $B\,I_B$. (c) Sättigung: Basis-Emitter wie in (b), Kollektor-Emitter eine Spannungsquelle 0,2 V. Darunter die zugehörigen linearisierten Kennlinien: Eingang mit Knick bei 0,6 V, Steuerkennlinie mit der Steigung $B$ bis zur Sättigung und danach waagrecht, Ausgang mit senkrechtem Ast bei 0,2 V. In jedem Bereich wird der Transistor zu Quellen, mit denen man wie in jedem linearen Netz rechnet.
:::

Für Handrechnungen ersetzt das Skript den Transistor in jedem Bereich durch Quellen (S. 182–184): Basis-Emitter eine Spannungsquelle mit $U_{BE,\mathrm{ein}}$ = 0,6 V, Kollektor-Emitter im aktiven Bereich eine gesteuerte Stromquelle mit dem $B$-fachen Basisstrom, in der Sättigung eine Spannungsquelle mit $U_{CE,\mathrm{sat}}$ = 0,2 V; im Sperrbereich ist alles offen (Abbildung 2). Welches Ersatzschaltbild gilt, findet man wie bei der Diode mit Annahme und Probe; Bedingungen und Beispiel stehen in [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html), Abschnitt *Die Arbeitsbereiche*.

Zum Vergleich nennt der Artikel stellenweise Werte des __vollständigen Modells__: des Beispieltransistors aus [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html) ohne Vereinfachungen, mit der Transfergleichung, $B$ = 500 bei 5 V und dem Early-Effekt, durch den der Kollektorstrom mit $U_{CE}$ leicht wächst.

## Der Basiswiderstand und warum der Arbeitspunkt wandert

*Wie stellt ein Basiswiderstand den Arbeitspunkt ein, und warum genügt das nicht?*

:::grafik
Szene: get1/bipolartransistoren/02-einstellungen · Vorlage: schaltplan
**Abbildung 3:** Drei Schaltungen zur Arbeitspunkteinstellung an 10 V. (a) Basiswiderstand $R_B$ = 2,2 MΩ von der Versorgung zur Basis, $R_C$ = 2,2 kΩ. (b) Stromgegenkopplung: Basisspannungsteiler $R_1$ = 330 kΩ, $R_2$ = 68 kΩ, Emitterwiderstand $R_E$ = 1 kΩ, $R_C$ = 3,9 kΩ; daneben der Teiler als Ersatzspannungsquelle mit $U_q$ = 1,71 V und $R_i$ = 56,4 kΩ. (c) Spannungsgegenkopplung: $R_B$ = 1 MΩ vom Kollektor zur Basis, $R_C$ = 2,2 kΩ. Drei Wege, den Basisstrom festzulegen, mit sehr verschiedener Abhängigkeit von $B$.
:::

**Die Akteure:**

- __$U_\mathrm{ein}$__, __$R_B$__: Spannung, an der der __Basiswiderstand__ liegt, und dieser selbst (Abbildung 3a); hier 10 V und 2,2 MΩ. Das Skript nennt die Spannung $U_E$.

:::formel Formel
$$I_B = \frac{U_\mathrm{ein} - U_{BE,\mathrm{ein}}}{R_B}$$

$$I_C = B\,I_B$$

$$U_{CE} = U_{CC} - R_C\,B\,I_B$$
:::

**So liest man das:** Der Widerstand legt den Basisstrom fest, $B$ macht daraus den Kollektorstrom, die Arbeitsgerade liefert die Spannung (Skript, S. 178). Ergibt sich weniger als 0,2 V, ist der Transistor gesättigt. $B$ geht voll ein.

Idee der Herleitung: Ersatzschaltbild des aktiven Bereichs einsetzen, Maschenregel für Basis- und Kollektorkreis.

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
**Gegeben:** $U_{CC}$ = $U_\mathrm{ein}$ = 10 V, $R_C$ = 2,2 kΩ, Beispieltransistor mit $B$ = 500, Exemplare des BC547C mit 420 und 800; Modellwert 0,6 V; Widerstände aus der Normreihe E12, der üblichen Abstufung im Handel.

**Gesucht:** $R_B$ für die Mitte (2,23 mA) und die Arbeitspunkte der drei Exemplare.

**Rechnung:**

$$I_B = \frac{2{,}23\ \mathrm{mA}}{500} = 4{,}45\ \mu\mathrm{A}, \qquad R_B = \frac{9{,}4\ \mathrm{V}}{4{,}45\ \mu\mathrm{A}} = 2{,}11\ \mathrm{M\Omega} \;\rightarrow\; 2{,}2\ \mathrm{M\Omega}$$

Mit 2,2 MΩ fließen 4,27 µA, und:

$$B = 420\!:\ 1{,}80\ \mathrm{mA},\ 6{,}05\ \mathrm{V}, \qquad B = 500\!:\ 2{,}14\ \mathrm{mA},\ 5{,}30\ \mathrm{V}, \qquad B = 800\!:\ 3{,}42\ \mathrm{mA},\ 2{,}48\ \mathrm{V}$$

**Ergebnis:** **2,2 MΩ; je nach Exemplar liegt der Arbeitspunkt zwischen 2,5 und 6,1 V.**

**Einordnung:** In einer einzigen Verstärkungsgruppe wandert der Arbeitspunkt um mehr als ein Drittel der Geraden.
::::

Der Kollektorstrom ist hier $B$-mal der Basisstrom; alles, was $B$ verändert, verschiebt ihn im selben Verhältnis: die Fertigung um den Faktor 1,9, die Temperatur um 0,5 bis 1 % je Kelvin. Das Skript fordert deshalb, den Strom durch die Beschaltung festzulegen statt durch $B$ (S. 179).

:::fehlvorstellung
„Mit dem Basiswiderstand stelle ich den Kollektorstrom ein.“
Das liegt nahe, weil der Widerstand die einzige Stellgröße ist. Er stellt aber den Basisstrom ein; der Kollektorstrom ist dessen $B$-Faches und erbt jede Streuung, im Beispiel 1,80 bis 3,42 mA. Einen festen Kollektorstrom liefert erst eine Schaltung, in der $B$ nur in kleinen Korrekturen vorkommt (Abschnitt *Stromgegenkopplung mit Emitterwiderstand*).
:::

## Stromgegenkopplung mit Emitterwiderstand

*Wie macht ein Emitterwiderstand den Kollektorstrom unabhängig von $B$ und von der Temperatur?*

**Die Akteure:**

- __$R_E$__: __Emitterwiderstand__ zwischen Emitter und Masse; 1 kΩ.
- __$R_1$__, __$R_2$__: __Basisspannungsteiler__, der die Basisspannung erzeugt (Abbildung 3b); 330 kΩ und 68 kΩ.
- __$U_q$__, __$R_i$__: Leerlaufspannung und Innenwiderstand des Teilers als Ersatzspannungsquelle; 1,71 V und 56,4 kΩ.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Liegt die Basis auf fester Spannung, liegt der Emitter 0,6 V tiefer. Damit ist die Spannung am Emitterwiderstand festgelegt und mit ihr der Emitterstrom: bei 1,6 V an der Basis und 1 kΩ genau 1,0 mA, ohne $B$ (Skript, S. 179).

**Schritt 2**: Will der Kollektorstrom steigen, steigt die Spannung am Emitterwiderstand; bei fester Basisspannung bleibt weniger $U_{BE}$, die Stufe am Basis-Emitter-Übergang wächst, und der Strom geht zurück. Diese Rückwirkung einer Änderung auf ihre eigene Ursache heißt __Gegenkopplung__, hier __Stromgegenkopplung__.

**Schritt 3**: Auch die Temperatur wirkt nur noch schwach: Sinkt $U_{BE}$ um 2 mV je Kelvin, steigt der Strom um 2 mV durch 1 kΩ, 0,2 % je Kelvin bei 1 mA statt 8 % bei fester $U_{BE}$.

**Schritt 4**: Der Teiler, der die Basisspannung liefert, hat einen Innenwiderstand; an ihm erzeugt der Basisstrom, der $B$ enthält, einen kleinen Abfall. So kommt $B$ wieder hinein, aber nur als Korrektur.

:::formel Formel
$$I_C = \frac{U_q - U_{BE,\mathrm{ein}}}{R_E\,(1 + 1/B) + R_i/B}, \qquad I_C \approx \frac{U_q - U_{BE,\mathrm{ein}}}{R_E}$$
:::

**So liest man das:** Die Teilerspannung abzüglich $U_{BE}$ liegt fast ganz am Emitterwiderstand. $B$ steht nur in den kleinen Termen $R_E/B$ und $R_i/B$, im Beispiel 2 Ω und 113 Ω neben 1000 Ω (Skript, Gl. 11.1); 10 % mehr $B$ ergeben deshalb nur rund 1 % mehr Strom. Den letzten Schritt des Skripts, auch $U_{BE}$ wegzulassen, darf man nur bei Basisspannungen weit über 0,6 V gehen; hier ergäbe er 1,71 mA statt 0,99 mA.

Idee der Herleitung: Teiler als Ersatzspannungsquelle, dann die Masche über den Basiskreis bis Masse.

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
**Gegeben:** $U_{CC}$ = 10 V, $R_1$ = 330 kΩ, $R_2$ = 68 kΩ, $R_E$ = 1 kΩ, $R_C$ = 3,9 kΩ; $B$ = 500, Exemplare mit 420 und 800; Modellwert 0,6 V.

**Gesucht:** Kollektorstrom und $U_{CE}$ der drei Exemplare.

**Rechnung:** Ersatzquelle und Strom für $B$ = 500:

$$U_q = \frac{68\ \mathrm{k\Omega}}{398\ \mathrm{k\Omega}}\cdot10\ \mathrm{V} = 1{,}7085\ \mathrm{V}, \qquad R_i = \frac{330\ \mathrm{k\Omega}\cdot68\ \mathrm{k\Omega}}{398\ \mathrm{k\Omega}} = 56{,}4\ \mathrm{k\Omega}$$

$$I_C = \frac{1{,}1085\ \mathrm{V}}{1002\ \Omega + 112{,}8\ \Omega} = 0{,}994\ \mathrm{mA}$$

Für 420 und 800 ergeben sich 0,975 und 1,034 mA, $U_{CE}$ liegt bei 5,22, 5,13 und 4,93 V, alle im aktiven Bereich.

**Ergebnis:** **0,975 bis 1,034 mA, der Arbeitspunkt bleibt in der Mitte.**

**Einordnung:** Statt des Faktors 1,9 beim Basiswiderstand streut der Strom um ±3 %. Das vollständige Modell ergibt 0,947 mA, weil die echte $U_{BE}$ bei 0,653 V liegt; deshalb sollte am Emitterwiderstand mindestens etwa 1 V liegen.
::::

:::frage
„Warum muss der Strom durch den Teiler viel größer sein als der Basisstrom?“
Der Basisstrom senkt die Basisspannung am Innenwiderstand des Teilers um $R_i\,I_B$, und weil er mit $B$ schwankt, schwankt diese Absenkung mit. Klein bleibt sie, wenn durch $R_2$ viel mehr fließt als der Basisstrom: im Beispiel 23,5 µA gegen 2 µA, das 12-Fache. Als Faustregel gilt mindestens das Zehnfache.
:::

:::frage
„Kostet der Emitterwiderstand nicht Verstärkung?“
Ja, für Signale wirkt die Gegenkopplung genauso wie für langsame Änderungen und senkt die Spannungsverstärkung. Deshalb überbrückt man den Emitterwiderstand in Verstärkern oft mit einem Kondensator: Für die langsame Arbeitspunkteinstellung ist er da, für das schnelle Signal kurzgeschlossen. Wie das genau wirkt, behandelt [Der Transistor als Verstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker.html).
:::

## Spannungsgegenkopplung

*Wie stabilisiert ein Widerstand vom Kollektor zur Basis den Arbeitspunkt, und was kostet das?*

Bei der __Spannungsgegenkopplung__ hängt der Basiswiderstand am Kollektor (Abbildung 3c, Skript Bild 11.8). Steigt der Kollektorstrom, sinkt $U_{CE}$, am Basiswiderstand liegt weniger Spannung, und der Basisstrom sinkt.

:::formel Formel
$$I_C = \frac{U_{CC} - U_{BE,\mathrm{ein}}}{R_C\,(1 + 1/B) + R_B/B}$$
:::

**So liest man das:** Ist $R_C$ viel größer als $R_B/B$, hängt der Strom kaum von $B$ ab (Skript, Gl. 11.2). Dann liegt am Basiswiderstand aber nur die kleine Spannung $R_B\,I_B$, und $U_{CE}$ rückt nahe an $U_{BE}$ und damit nahe an die Sättigungsgrenze. Mit 1 MΩ liegt der Arbeitspunkt in der Mitte, der Strom streut aber zwischen 2,05 und 2,72 mA; mit 100 kΩ streut er nur ±2,4 %, doch $U_{CE}$ beträgt bloß 1,1 bis 1,5 V. Für Verstärker ist deshalb die Stromgegenkopplung die Regel.

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

## Der Stromspiegel

*Wie überträgt man einen Strom genau in einen anderen Zweig?*

:::grafik
Szene: get1/bipolartransistoren/02-stromspiegel · Vorlage: schaltung-und-kennlinie
**Abbildung 4:** (a) Stromspiegel nach Skript Bild 11.15 an 10 V: $T_1$ mit verbundenem Kollektor und Basis über den Referenzwiderstand 10 kΩ an der Versorgung, $T_2$ mit derselben Basis und demselben Emitter, im Kollektorkreis die Last $R_L$. (b) Kollektorstrom von $T_2$ über $U_{CE2}$ von 0 bis 10 V (vollständiges Modell), dazu waagrecht der Referenzstrom 0,935 mA: ab etwa 0,3 V fast waagrecht, bei 1 V gleich dem Referenzstrom, bei 5 V um 5,7 % darüber. Der Spiegel liefert den Referenzstrom an jede Last, solange $T_2$ im aktiven Bereich bleibt.
:::

**Die Akteure:**

- __$T_1$__, __$T_2$__: zwei gleich gebaute Transistoren, möglichst auf einem Chip.
- __$I_\mathrm{ref}$__, __$R_\mathrm{ref}$__: __Referenzstrom__ und der Widerstand, der ihn einstellt; 0,94 mA und 10 kΩ. Das Skript nennt den Widerstand $R_C$.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Bei $T_1$ sind Kollektor und Basis verbunden; er arbeitet als Diode, deren $U_{BE}$ sich auf den Referenzstrom einstellt, beim Beispieltransistor auf 0,65 V.

**Schritt 2**: $T_2$ hat dieselbe $U_{BE}$, denn Basen und Emitter sind verbunden. Nach der Transfergleichung hängt der Kollektorstrom exponentiell von $U_{BE}$ ab, mit dem Sättigungsstrom als Vorfaktor (Abschnitt *Der Transistoreffekt* in [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html)). $T_2$ führt deshalb denselben Kollektorstrom, sofern er denselben Sättigungsstrom hat: Kopiert wird über die gemeinsame Spannung.

**Schritt 3**: Die beiden Basisströme stammen aus dem Referenzstrom; für die Kopie fehlen bei $B$ = 500 deshalb 0,4 %.

**Schritt 4**: Diesen Strom liefert $T_2$ in jede Last, solange $U_{CE2}$ über etwa 0,3 V bleibt: Sein Kollektor ist eine __Stromquelle__. Wegen des Early-Effekts (die Basis wird mit wachsender Kollektorspannung etwas dünner) steigt der Strom mit $U_{CE2}$ leicht an; bei 5 V liegt er 5,7 % über dem Referenzstrom.

:::formel Formel
$$I_{C2} = \frac{I_\mathrm{ref}}{1 + 2/B}$$
:::

**So liest man das:** Der Ausgangsstrom ist der Referenzstrom, verkleinert um die beiden Basisströme, und hängt nicht von der Last ab (Skript, Gl. 11.3). Mehrere Transistoren an derselben Basisleitung liefern mehrere Kopien.

Idee der Herleitung: Gleiche Spannung an gleichen Transistoren ergibt gleiche Ströme; die Knotenregel verteilt den Referenzstrom.

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
**Gegeben:** $U_{CC}$ = 10 V, $R_\mathrm{ref}$ = 10 kΩ, $B$ = 500; Modellwert 0,6 V.

**Gesucht:** Referenzstrom, Kopie, größte Last.

**Rechnung:**

$$I_\mathrm{ref} = \frac{9{,}4\ \mathrm{V}}{10\ \mathrm{k\Omega}} = 0{,}94\ \mathrm{mA}, \qquad I_{C2} = \frac{0{,}94\ \mathrm{mA}}{1{,}004} = 0{,}936\ \mathrm{mA}, \qquad R_{L,\mathrm{max}} = \frac{9{,}7\ \mathrm{V}}{0{,}936\ \mathrm{mA}} = 10{,}4\ \mathrm{k\Omega}$$

**Ergebnis:** **0,936 mA für jede Last bis 10,4 kΩ.**

**Einordnung:** $B$ = 420 oder 800 ändert die Kopie um weniger als 0,2 %. Mehr macht der Early-Effekt aus: Bei 5 V liegt die Kopie 5,7 % über dem Referenzstrom.
::::

:::fehlvorstellung
„Der Spiegel kopiert den Strom, weil beide Basen denselben Basisstrom bekommen.“
Das liegt nahe, weil die Basen verbunden sind. Kopiert wird aber über die gemeinsame Spannung $U_{BE}$; die gleichen Basisströme sind die Folge. Deshalb versagt der Spiegel bei ungleichen Transistoren: 10 % mehr Sättigungsstrom bei $T_2$ ergeben 10 % mehr Strom, 1 K Temperaturunterschied 8 %.
:::

## Der Inverter

*Wie wird aus dem Transistor ein logisches Nicht-Glied?*

:::grafik
Szene: get1/bipolartransistoren/02-inverter · Vorlage: schaltung-und-kennlinie
**Abbildung 5:** (a) Inverter nach Skript Bild 11.16: Eingang über $R_B$ = 10 kΩ an der Basis, $R_C$ = 1 kΩ an 5 V, Ausgang am Kollektor. (b) Ausgangsspannung über der Eingangsspannung von 0 bis 2 V. Modell: waagrecht bei 5 V bis 0,6 V, dann eine Gerade mit der Steigung −50 bis auf 0,2 V bei 0,696 V, danach waagrecht. Vollständiges Modell (gestrichelt): weicher, 4,89 V bei 0,6 V, 3,41 V bei 0,7 V, 0,25 V bei 0,8 V. Der Arbeitspunkt durchläuft alle drei Bereiche; zwischen den Pegeln liegt ein schmaler Übergang.
:::

Ein __Inverter__ kehrt ein logisches Signal um (Skript, S. 186–188). Unter 0,6 V am Eingang sperrt der Transistor, und am Ausgang liegt die Versorgung; ist der Eingang hoch genug, sättigt er, und am Ausgang liegen 0,2 V (Abbildung 5). Dazwischen fällt der Ausgang mit der Steigung $-B\,R_C/R_B$, und der Pegel ist weder 0 noch 1.

**Die Akteure:**

- __$U_{\mathrm{ein,sat}}$__: Eingangsspannung, ab der der Transistor gesättigt ist; im Skript $U_{E,\mathrm{sat}}$.

:::formel Formel
$$U_{\mathrm{ein,sat}} = \frac{(U_{CC} - U_{CE,\mathrm{sat}})\,R_B}{B\,R_C} + U_{BE,\mathrm{ein}}$$
:::

**So liest man das:** Der erste Summand ist die Breite des Übergangs; sie ist klein, wenn $R_B$ klein gegen $B\,R_C$ ist. Im Skript fehlen in dieser Formel (Gl. 11.4, S. 188) der Widerstand $R_C$ und die Klammer um die Differenz aus $U_{CC}$ und $U_{CE,\mathrm{sat}}$; auf S. 187 steht außerdem „0,6 Ω“ statt 0,6 V.

Idee der Herleitung: Ausgangsspannung des aktiven Bereichs gleich der Sättigungsspannung setzen und nach dem Eingang auflösen.

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
**Gegeben:** $U_{CC}$ = 5 V, $R_C$ = 1 kΩ, $R_B$ = 10 kΩ, $B$ = 500 (mindestens 420); Eingang 0 oder 3,3 V; Modellwerte 0,6 V und 0,2 V, für die Übersteuerung 0,7 V.

**Gesucht:** Kante der Sättigung; wie viel mehr Basisstrom als nötig bei 3,3 V fließt (Übersteuerung).

**Rechnung:**

$$U_{\mathrm{ein,sat}} = \frac{4{,}8\ \mathrm{V}\cdot10\ \mathrm{k\Omega}}{500\cdot1\ \mathrm{k\Omega}} + 0{,}6\ \mathrm{V} = 0{,}696\ \mathrm{V}, \qquad I_B = \frac{3{,}3\ \mathrm{V} - 0{,}7\ \mathrm{V}}{10\ \mathrm{k\Omega}} = 0{,}26\ \mathrm{mA}$$

Nötig wären mit $B$ = 420 nur 4,8 mA durch 420, also 11,4 µA.

**Ergebnis:** **Kante bei 0,70 V; bei 3,3 V fließt 23-mal so viel Basisstrom, wie die Sättigung braucht.**

**Einordnung:** Beide logischen Pegel liegen weit von der Kante; die Streuung von $B$ verschiebt sie nur um Hundertstelvolt.
::::

## Die drei Grundschaltungen

*Welche Möglichkeiten gibt es, einen Transistor zwischen Eingang und Ausgang zu schalten?*

:::grafik
Szene: get1/bipolartransistoren/02-grundschaltungen · Vorlage: schaltung-und-kennlinie
**Abbildung 6:** Die drei Grundschaltungen an 5 V mit ihren Gleichspannungskennlinien (vollständiges Modell). (a) Emitterschaltung: Eingang über 10 kΩ an der Basis, Ausgang am Kollektor mit 1 kΩ; fallende Kennlinie wie der Inverter. (b) Kollektorschaltung: Kollektor an 5 V, Eingang an der Basis, Ausgang am Emitter mit 1 kΩ nach Masse; Ausgang folgt dem Eingang um gut 0,6 V tiefer (1,34 V bei 2 V, 4,31 V bei 5 V). (c) Basisschaltung: Basis an Masse, Eingang über 1 kΩ am Emitter (negative Spannungen), Ausgang am Kollektor mit 1 kΩ; steigende Kennlinie (4,63 V bei −1 V, 2,68 V bei −3 V, 0,70 V bei −5 V). Welcher Anschluss Ein- und Ausgang gemeinsam ist, bestimmt, ob die Schaltung umkehrt, folgt oder nicht umkehrend überträgt.
:::

Der Transistor hat drei Anschlüsse; einer gehört zu Eingang und Ausgang zugleich und gibt der __Grundschaltung__ ihren Namen (Skript, S. 190–192, Abbildung 6). Auch die Versorgung zählt dabei als gemeinsamer Anschluss, denn eine konstante Quelle trägt zu Signaländerungen nichts bei.

| Grundschaltung | Ein- und Ausgang, Verhalten |
|---|---|
| Emitterschaltung | Eingang an der Basis, Ausgang am Kollektor; Kennlinie fallend und steil, mit Basiswiderstand der Inverter; Stromverstärkung $B$ |
| Kollektorschaltung (Emitterfolger) | Eingang an der Basis, Ausgang am Emitter; Kennlinie steigend, Ausgang um $U_{BE}$ tiefer, Steigung knapp 1; Stromverstärkung $B + 1$ |
| Basisschaltung | Eingang am Emitter, Ausgang am Kollektor; Kennlinie steigend, nicht umkehrend; Stromverstärkung knapp 1 |

Bei der __Kollektorschaltung__, auch __Emitterfolger__, folgt der Ausgang am Emitter dem Eingang an der Basis:

:::formel Formel
$$U_\mathrm{aus} = U_\mathrm{ein} - U_{BE,\mathrm{ein}}$$
:::

**So liest man das:** Die Spannungsverstärkung ist knapp 1, die Stromverstärkung $B + 1$: Mit 1 kΩ am Emitter und 2 V am Eingang liefert die Quelle 2,8 µA, die Last bekommt 1,4 mA.

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

Die __Basisschaltung__ hat die Basis an Masse und das Signal am Emitter; fast der ganze Eingangsstrom kommt am Kollektor heraus. Steigt die Eingangsspannung, wird sie also weniger negativ, sinkt der Strom aus dem Emitter, mit ihm der Kollektorstrom und der Abfall an $R_C$: Die Ausgangsspannung steigt, die Schaltung kehrt nicht um (Abbildung 6c). Wie sich die drei Schaltungen für kleine Signale verhalten, behandelt [Der Transistor als Verstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker.html).

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Basiswiderstand | $B$ geht voll ein; der Arbeitspunkt wandert mit jedem Exemplar. |
| Strom­gegen­kopplung | Der Emitterwiderstand setzt den Strom; $B$ und $U_{BE}$ bleiben kleine Korrekturen. |
| Spannungs­gegen­kopplung | Rückwirkung über $U_{CE}$; je unabhängiger von $B$, desto näher an der Sättigung. |
| Stromspiegel | Gleiche Spannung an gleichen Transistoren: Die unsicheren Kennwerte kürzen sich heraus. |
| Inverter und Grundschaltungen | Wohin der Arbeitspunkt läuft und welcher Anschluss gemeinsam ist, bestimmt das Verhalten. |

Der Arbeitspunkt eines Transistors ist der Punkt, an dem seine Kennlinien und die Gleichungen der äußeren Schaltung zugleich gelten; gute Schaltungen legen ihn so fest, dass die unsicheren Kennwerte des Transistors, Stromverstärkung und Basis-Emitter-Spannung, kaum eingehen: durch Gegenkopplung oder dadurch, dass sie sich wie im Stromspiegel herauskürzen.

## Bedeutung und Ausblick

Die Stromgegenkopplung mit Basisspannungsteiler ist die übliche Arbeitspunkteinstellung diskreter Verstärkerstufen, Stromspiegel stecken in jedem Operationsverstärker. Wie die Schaltungen kleine Signale verstärken, zeigt [Der Transistor als Verstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker.html).

**In der ausführlichen Fassung:** die größte Verlustleistung auf der Arbeitsgeraden und die Erwärmung, Bereichsbestimmung aus Messwerten, die Wirkungskette der Gegenkopplung, die Empfindlichkeit der Spannungsgegenkopplung als Formel, die Grenzen des Stromspiegels durch Early-Effekt, Paarung und Temperatur, der reale Übergang des Inverters, der Emitterfolger mit Rechnung und die Steigungen der Grundschaltungen, jeweils mit dem vollständigen Transistormodell zum Vergleich. [Zur ausführlichen Fassung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/arbeitspunkt-und-grundschaltungen-ausfuehrlich.html)

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
A: Der Basiswiderstand legt nur den Basisstrom fest; der Kollektorstrom ist dessen $B$-Faches und folgt jeder Streuung von $B$. Mit 2,2 MΩ an 10 V liefern Exemplare mit $B$ = 420 und 800 1,80 und 3,42 mA.
F: Warum macht ein Emitterwiderstand den Kollektorstrom fast unabhängig von $B$?
A: Bei fester Basisspannung liegt am Emitterwiderstand die Basisspannung minus $U_{BE}$, und sie legt den Emitterstrom fest. Steigt der Strom, steigt die Spannung am Widerstand, $U_{BE}$ sinkt, und der Strom geht zurück; $B$ bleibt nur in kleinen Korrekturen.
F: Wie groß ist der Kollektorstrom der Stromgegenkopplung mit 330 kΩ, 68 kΩ und 1 kΩ an 10 V?
A: Die Ersatzquelle hat 1,7085 V und 56,4 kΩ; mit $B$ = 500 fließen 1,1085 V durch 1114,8 Ω, also 0,994 mA. Für 420 und 800 sind es 0,975 und 1,034 mA.
F: Stimmt es, dass man mit dem Basiswiderstand den Kollektorstrom einstellt?
A: Nein. Er stellt den Basisstrom ein; der Kollektorstrom ist dessen $B$-Faches und streut mit $B$. Einen festen Kollektorstrom liefert erst eine Gegenkopplung.
F: Warum kopiert der Stromspiegel den Strom?
A: $T_1$ stellt als Diode seine $U_{BE}$ auf den Referenzstrom ein, und $T_2$ hat dieselbe $U_{BE}$; gleiche Spannung an gleichen Transistoren ergibt nach der Transfergleichung gleiche Ströme. Die beiden Basisströme kosten bei $B$ = 500 0,4 %.
F: Stimmt es, dass der Spiegel kopiert, weil beide Basen denselben Strom bekommen?
A: Nein. Kopiert wird über die gemeinsame Spannung $U_{BE}$; gleiche Basisströme sind die Folge. Bei ungleichen Transistoren versagt die Kopie: 10 % mehr Sättigungsstrom ergeben 10 % mehr Strom.
:::
