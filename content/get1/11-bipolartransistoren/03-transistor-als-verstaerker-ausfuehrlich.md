---
title: Der Transistor als Verstärker
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Bipolartransistoren
order: 110500
summary: Wie ein Bipolartransistor eine kleine Spannungsänderung in eine große verwandelt und wovon die Verstärkung abhängt: Groß- und Kleinsignal, Steilheit, reale Kennlinien mit Eingangs- und Ausgangswiderstand, erweitertes und Kleinsignal-Ersatzschaltbild, Spannungsverstärkung der Emitterschaltung mit und ohne Emitterwiderstand, die drei Grundschaltungen für kleine Signale und die Spannungsstabilisierung mit Z-Diode und Transistor. Ausführliche Fassung mit allen Herleitungen, Verzerrung, Datenblattvergleich, Kondensatoren und dem Lastverhalten des Längsreglers.
tags: Verstärker, Kleinsignal, Ersatzschaltbild, Steilheit, Spannungsverstärkung, Emitterschaltung
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Ein Mikrofon liefert Spannungsänderungen von wenigen Millivolt, ein Lautsprecher oder ein Analog-Digital-Umsetzer braucht Volt. Ein Transistor, der in seinem Arbeitspunkt ruht, kann eine kleine Änderung in eine große, formgleiche verwandeln, wenn die Schaltung um ihn herum dafür gebaut ist.
**Ein Transistor verstärkt, weil eine kleine Änderung der Basis-Emitter-Spannung den Kollektorstrom mit der Steilheit $I_C/U_T$ ändert und ein Widerstand diese Stromänderung in eine große Spannungsänderung verwandelt; gleichmäßig gelingt das nur für Änderungen, die klein gegen $U_T$ sind, und ein Emitterwiderstand tauscht Verstärkung gegen Linearität und Unabhängigkeit vom Transistor.**

Vorausgesetzt werden die Transfergleichung aus [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html), der Arbeitspunkt mit Stromgegenkopplung und die drei Grundschaltungen aus [Arbeitspunkt und Grundschaltungen des Transistors](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/arbeitspunkt-und-grundschaltungen.html) und der differentielle Widerstand aus [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html). Darauf baut [Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html) auf; in seinem Inneren arbeiten solche Stufen.

:::grafik
Szene: get1/bipolartransistoren/03-verstaerkerstufe · Vorlage: schaltung-und-zeitverlauf
**Abbildung 1:** (a) Die Verstärkerstufe aus dem vorigen Artikel: Versorgung 10 V, Basisspannungsteiler 330 kΩ und 68 kΩ, Kollektorwiderstand 3,9 kΩ, Emitterwiderstand 1 kΩ mit parallelem Emitterkondensator 470 µF; die Signalquelle hängt über einen Koppelkondensator von 1 µF an der Basis, der Ausgang über 1 µF am Kollektor. (b) Zeitverläufe bei 1 kHz: Das Basispotenzial schwankt um 1 mV um seinen Ruhewert 1,602 V, das Kollektorpotenzial um 136 mV um seinen Ruhewert 6,306 V, gegenphasig; hinter dem Ausgangskondensator bleibt nur die Änderung um null. Eine Änderung von einem Millivolt an der Basis erscheint 136-fach vergrößert und umgekehrt am Kollektor.
:::

## Groß- und Kleinsignal

*Wie stark ändert sich der Kollektorstrom, wenn sich die Basis-Emitter-Spannung ein wenig ändert, und warum gilt das nur für kleine Änderungen?*

:::grafik
Szene: get1/bipolartransistoren/03-tangente · Vorlage: kennlinie-tangente
**Abbildung 2:** Kollektorstrom des Beispieltransistors über $U_{BE}$ um den Arbeitspunkt der Verstärkerstufe (0,653 V; 0,947 mA) mit der Tangente der Steigung 36,6 mS. Darunter zwei Eingangssignale, Sinus mit 1 mV und mit 10 mV Amplitude, daneben die Kollektorströme: Bei 1 mV schwingt der Strom um +3,9 % und −3,8 %, fast wie auf der Tangente; bei 10 mV um +47 % und −32 %, sichtbar unsymmetrisch. Im Kleinen ist die Kennlinie eine Gerade, im Großen verzerrt sie das Signal.
:::

Um verstärken zu können, ruht der Transistor in einem Arbeitspunkt im aktiven Bereich, eingestellt wie im vorigen Artikel; das Signal ist eine kleine Änderung um diesen Ruhezustand. Man zerlegt deshalb jede Größe in zwei Teile.

**Die Akteure:**

- __Ruhewerte__: die Werte im Arbeitspunkt, groß geschrieben ($U_{BE}$, $I_C$, $U_{CE}$); in der Verstärkerstufe 0,653 V, 0,947 mA und 5,36 V.
- __Kleinsignal__: die Änderungen um diese Ruhewerte, klein geschrieben ($u_{be}$, $i_c$, $u_{ce}$); in der Stufe einige Millivolt bzw. einige Mikroampere. Der momentane Wert ist die Summe aus Ruhewert und Änderung. Mit __Großsignal__ meint man diese Gesamtwerte und ihr Verhalten auf der ganzen, gekrümmten Kennlinie.
- __$U_T$__: Temperaturspannung, 25,85 mV bei 300 K; die Spannungsskala der Exponentialkennlinie.
- __$g_m$__: __Steilheit__, Änderung des Kollektorstroms je Änderung der Basis-Emitter-Spannung; in mS (Millisiemens, Milliampere je Volt); 36,6 mS in der Stufe.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Nach der Transfergleichung ([Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html), Abschnitt *Der Transistoreffekt*) wächst der Kollektorstrom exponentiell mit $U_{BE}$: Je 25,85 mV mehr wird er 2,72-mal so groß, je 59,5 mV zehnmal so groß.

**Schritt 2**: Eine Änderung $u_{be}$ multipliziert den Strom deshalb mit einem Faktor, der nur vom Verhältnis $u_{be}/U_T$ abhängt, in jedem Arbeitspunkt mit demselben. 1 mV mehr heben ihn um 3,94 %, 1 mV weniger senken ihn um 3,79 %.

**Schritt 3**: Ist $u_{be}$ klein gegen $U_T$, ändert sich der Strom proportional zur Spannung; die Kennlinie wirkt wie ihre Tangente im Arbeitspunkt (Abbildung 2). Das ist derselbe Schritt wie beim differentiellen Widerstand der Diode ([Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html), Abschnitt *Der differentielle Widerstand*), nur steuert hier die Spannung zwischen Basis und Emitter den Strom in einem anderen Zweig, dem Kollektorzweig.

**Schritt 4**: Bei größeren Änderungen bricht die Proportionalität: 10 mV heben den Strom um 47 %, −10 mV senken ihn nur um 32 %. Ein sinusförmiges Eingangssignal wird unsymmetrisch weitergegeben, also verzerrt. Als klein gilt eine Änderung beim Transistor deshalb, solange $u_{be}$ klein gegen $U_T$ bleibt, in der Praxis höchstens einige Millivolt.

:::formel Formel
$$g_m = \frac{\partial I_C}{\partial U_{BE}}\Big|_{U_{CE}\ \mathrm{fest}} = \frac{I_C}{U_T}$$
:::

**So liest man das:** Die Steilheit ist die Steigung der Tangente in Abbildung 2; mit ihr wird aus einer kleinen Spannungsänderung $u_{be}$ die Stromänderung $g_m u_{be}$. Sie hängt nur vom Ruhestrom und der Temperatur ab, nicht von $B$, der Fläche oder dem Sättigungsstrom: doppelter Ruhestrom, doppelte Steilheit. In der Verstärkerstufe sind es 36,6 mS, am Datenblattpunkt 2 mA 77,4 mS. Den Kehrwert $1/g_m$ nennt man $r_e$, hier 27,3 Ω bzw. 12,9 Ω.

Idee der Herleitung: Man leitet die Transfergleichung nach $U_{BE}$ ab; die Exponentialfunktion reproduziert sich dabei selbst.

:::herleitung
**Ausgangspunkt:** die Transfergleichung aus [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html), dort hergeleitet im Abschnitt *Der Transistoreffekt*.

**Annahmen:** (i) aktiver Bereich, in dem die Transfergleichung gilt; (ii) $U_{CE}$ fest. Der Early-Effekt ändert den Strom nur über $U_{CE}$ und wirkt dann als konstanter Faktor $F$.

**Schritt 1**: Transfergleichung mit dem Faktor $F$ des Early-Effekts:

$$I_C = I_S\,\exp\!\Big(\frac{U_{BE}}{U_T}\Big)\,F(U_{CE})$$

**Schritt 2** (entscheidender Schritt): Ableiten nach $U_{BE}$ bei fester $U_{CE}$; die Exponentialfunktion ist ihre eigene Ableitung, die innere Ableitung liefert $1/U_T$:

$$\frac{\partial I_C}{\partial U_{BE}} = \frac{1}{U_T}\,I_S\,\exp\!\Big(\frac{U_{BE}}{U_T}\Big)\,F(U_{CE}) = \frac{I_C}{U_T}$$

**Ergebnis:**

$$g_m = \frac{I_C}{U_T}$$

**Woher die Faktoren kommen:** $1/U_T$ ist die innere Ableitung des Exponenten; $I_C$ steht da, weil die Ableitung der Exponentialfunktion wieder sie selbst ist: Die Steigung der Kennlinie ist proportional zu ihrer Höhe.

**Proben:** Einheit A/V = S. Zahlenwert: 0,947 mA durch 25,85 mV ergibt 36,6 mS; die numerische Ableitung des vollständigen Modells liefert denselben Wert. Grenzfall: Ohne Ruhestrom, im Sperrbereich, ist die Steilheit null, der Transistor verstärkt nicht.

**Grenzen:** Die Tangente gilt nur für kleine Änderungen. Bei großen Strömen, beim BC547C gegen 100 mA, wächst der Strom langsamer als exponentiell, und die Steilheit bleibt unter $I_C/U_T$.
:::

::::beispiel Steilheit der Verstärkerstufe und Genauigkeit der Tangente
**Gegeben:** Ruhestrom 0,947 mA (Verstärkerstufe aus dem vorigen Artikel, vollständiges Modell); $U_T$ = 25,85 mV; Änderungen von ±1 mV und ±10 mV.

**Gesucht:** die Steilheit und die Stromänderungen nach der Tangente und genau.

**Rechnung:** Steilheit:

$$g_m = \frac{0{,}947\ \mathrm{mA}}{25{,}85\ \mathrm{mV}} = 36{,}6\ \mathrm{mS}$$

Nach der Tangente bewirkt 1 mV die Stromänderung 36,6 µA, 3,87 % des Ruhestroms. Genau:

$$\exp\Big(\frac{1\ \mathrm{mV}}{25{,}85\ \mathrm{mV}}\Big) - 1 = +3{,}94\ \%, \qquad \exp\Big(\frac{-1\ \mathrm{mV}}{25{,}85\ \mathrm{mV}}\Big) - 1 = -3{,}79\ \%$$

Für ±10 mV ergibt die Tangente ±38,7 %, genau sind es +47,2 % und −32,1 %.

**Ergebnis:** **36,6 mS; die Tangente stimmt bei 1 mV auf 2 % genau, bei 10 mV liegt sie um 22 % daneben.**

**Einordnung:** Ein einziges Millivolt ändert den Strom um 4 %, denn die Spannungsskala der Exponentialfunktion ist $U_T$, 26 mV. Ein ohmscher Widerstand an 0,65 V änderte seinen Strom durch dasselbe Millivolt nur um 0,15 %. Dieselbe Steilheit hat bei diesem Strom jeder Bipolartransistor, gleich welcher Bauart.
::::

## Die realen Kennlinien

*Worin unterscheiden sich die echten Kennlinien von den idealisierten, und wie misst man den Unterschied?*

:::grafik
Szene: get1/bipolartransistoren/03-reale-kennlinien · Vorlage: kennlinie-ideal-real
**Abbildung 3:** Idealisierte und reale Kennlinien nach Skript Bild 11.19 und 11.20, mit den Werten des Beispieltransistors. (a) Eingangskennlinie, $I_B$ über $U_{BE}$: idealisiert senkrecht bei 0,6 V, real exponentiell; die Tangente im Arbeitspunkt (0,673 V; 4 µA) schneidet die Spannungsachse bei 0,647 V und hat die Steigung 1/(6,46 kΩ). (b) Ausgangskennlinien, $I_C$ über $U_{CE}$, für $I_B$ = 2, 4, 6 und 8 µA: idealisiert waagrecht ab 0,2 V, real leicht steigend; nach links verlängert treffen sich die realen Geraden bei −70 V. Im Arbeitspunkt 2 mA und 5 V beträgt die Steigung 1/(37,5 kΩ). Die realen Kennlinien haben endliche Steigungen; ihre Kehrwerte sind der Eingangs- und der Ausgangswiderstand.
:::

Für die Arbeitspunkte im vorigen Artikel genügten idealisierte Kennlinien (Skript, S. 188–189, Bilder 11.19 und 11.20): Die Eingangskennlinie steigt bei 0,6 V senkrecht an, die Ausgangskennlinien verlaufen oberhalb von 0,2 V waagrecht. Senkrecht heißt, dass sich der Basisstrom ohne jede Spannungsänderung ändern könnte; das Skript sagt, der Eingangswiderstand $R_{BE}$ sei null. Waagrecht heißt, dass der Kollektorstrom nicht von $U_{CE}$ abhängt; der Ausgangsleitwert $G_{CE}$ ist null, der Transistor eine ideale Stromquelle. Abbildung 3 zeigt, dass beides nur Näherungen sind.

**Die Akteure:**

- __$r_{BE}$__: __differentieller Eingangswiderstand__, Änderung von $U_{BE}$ je Änderung des Basisstroms bei fester $U_{CE}$, der Kehrwert der Steigung in Abbildung 3a; 6,46 kΩ bei 2 mA, 13,7 kΩ in der Verstärkerstufe. Das Skript schreibt $R_{BE}$.
- __$r_{CE}$__: __differentieller Ausgangswiderstand__, Änderung von $U_{CE}$ je Änderung des Kollektorstroms bei festem Basisstrom, der Kehrwert der Steigung in Abbildung 3b; 37,5 kΩ bei 2 mA und 5 V. Das Skript schreibt seinen Kehrwert $G_{CE}$, den Ausgangsleitwert.
- __$\beta$__: __Kleinsignal-Stromverstärkung__, Änderung des Kollektorstroms je Änderung des Basisstroms; im Modell gleich $B$, 500 bei 5 V. $B$ ist das Verhältnis der Ruheströme, $\beta$ das der Änderungen.
- __$U_A$__: __Early-Spannung__, die Spannung, bei der sich die verlängerten Ausgangskennlinien auf der negativen Achse treffen; 70 V beim Beispieltransistor.

**Das Zusammenspiel:** Die Eingangskennlinie ist die Transfergleichung, geteilt durch $B$: Der Basisstrom hängt genauso exponentiell von $U_{BE}$ ab wie der Kollektorstrom, ist aber 500-mal kleiner ([Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html), Abschnitt *Der Basisstrom und die Stromverstärkung*). Seine Änderungen sind deshalb ebenfalls 500-mal kleiner: Dasselbe Millivolt, das in der Stufe den Kollektorstrom um 36,6 µA ändert, ändert den Basisstrom um 73 nA. Für Änderungen wirkt der Eingang wie ein Widerstand von 13,7 kΩ.

Die Ausgangskennlinien steigen wegen des Early-Effekts. Mit wachsender $U_{CE}$ wird die Raumladungszone am gesperrten Kollektor-Basis-Übergang breiter, die neutrale Basis dünner, und durch eine dünnere Basis diffundieren bei gleicher $U_{BE}$ mehr Elektronen. Im Modell ist der Kollektorstrom proportional zur Summe aus $U_A$ und $U_{CE}$; deshalb schneiden alle verlängerten Geraden die Spannungsachse bei $-U_A$ (Abbildung 3b). Mit ihrer Steigung hängt auch das Verhältnis von Kollektor- zu Basisstrom von $U_{CE}$ ab; das meint das Skript mit dem Satz, die Verstärkung sei „abhängig von $U_{CE}$“ (S. 188).

:::formel Formel
$$r_{BE} = \frac{\partial U_{BE}}{\partial I_B}\Big|_{U_{CE}\ \mathrm{fest}} = \frac{U_T}{I_B} = \frac{\beta}{g_m}$$
:::

**So liest man das:** Der Eingangswiderstand ist die Temperaturspannung, geteilt durch den Basisstrom, und damit $\beta$-mal so groß wie $r_e$: 13,7 kΩ in der Stufe gegen 27,3 Ω. Je größer der Ruhestrom, desto kleiner ist er.

Idee der Herleitung: Man leitet den Basisstrom nach $U_{BE}$ ab, genau wie den Kollektorstrom bei der Steilheit.

:::herleitung
**Ausgangspunkt:** die Transfergleichung und die Stromverstärkung aus [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html): Der Basisstrom ist der Kollektorstrom geteilt durch die Stromverstärkung.

**Annahmen:** (i) aktiver Bereich wie bei der Steilheit; (ii) $U_{CE}$ fest; (iii) die Stromverstärkung hängt nicht vom Strom ab, dann ist das Verhältnis der Änderungen $\beta$ gleich dem der Ruheströme.

**Schritt 1**: Basisstrom als Exponentialfunktion von $U_{BE}$, mit dem Verhältnis $\beta$ der Ströme im Arbeitspunkt:

$$I_B = \frac{I_C}{\beta} = \frac{I_S\,F(U_{CE})}{\beta}\,\exp\!\Big(\frac{U_{BE}}{U_T}\Big)$$

**Schritt 2** (entscheidender Schritt): Ableiten nach $U_{BE}$ wie bei der Steilheit:

$$\frac{\partial I_B}{\partial U_{BE}} = \frac{I_B}{U_T}$$

**Schritt 3**: Kehrwert, dann den Basisstrom durch den Kollektorstrom und die Steilheit ausdrücken:

$$r_{BE} = \frac{U_T}{I_B} = \frac{U_T\,\beta}{I_C} = \frac{\beta}{g_m}$$

**Ergebnis:**

$$r_{BE} = \frac{U_T}{I_B} = \frac{\beta}{g_m}$$

**Woher die Faktoren kommen:** $\beta$ kommt hinzu, weil durch die Basis nur der $\beta$-te Teil des Stroms fließt, der auf dieselbe Spannungsänderung reagiert.

**Proben:** Einheit V/A = Ω. Zahlenwert: 25,85 mV durch 1,885 µA ergibt 13,7 kΩ; 502 durch 36,6 mS ebenso. Grenzfall: Ohne Basisstrom wird der Eingangswiderstand unendlich.

**Grenzen:** Hängt die Stromverstärkung vom Strom ab, wie beim realen BC547C unter 0,1 mA und über 10 mA, unterscheidet sich $\beta$ vom Verhältnis der Ruheströme; dann gilt die zweite Form mit dem gemessenen $\beta$.
:::

:::formel Formel
$$r_{CE} = \frac{\partial U_{CE}}{\partial I_C}\Big|_{I_B\ \mathrm{fest}} = \frac{U_A + U_{CE}}{I_C}$$
:::

**So liest man das:** Der Ausgangswiderstand wächst mit der Early-Spannung und sinkt mit dem Strom: 37,5 kΩ bei 2 mA und 5 V, 79,6 kΩ in der Verstärkerstufe. Oft rechnet man mit der Näherung $U_A/I_C$, weil $U_{CE}$ klein gegen $U_A$ ist; am Datenblattpunkt macht das 7 % aus.

Idee der Herleitung: Die Ausgangskennlinie ist eine Gerade durch den Punkt $-U_A$ auf der Spannungsachse; ihr Kehrwert der Steigung ist Abstand durch Höhe.

:::herleitung
**Ausgangspunkt:** das Modell des Early-Effekts: Bei festem Basisstrom ist der Kollektorstrom proportional zur Summe aus $U_A$ und $U_{CE}$, die Ausgangskennlinie also eine Gerade durch den Punkt $-U_A$.

**Annahmen:** (i) aktiver Bereich; (ii) Basisstrom fest; (iii) $U_A$ für alle Ströme gleich (lineares Early-Modell).

**Schritt 1**: Kollektorstrom mit dem Wert $I_{C0}$, den er bei verschwindender $U_{CE}$ hätte:

$$I_C = I_{C0}\,\frac{U_A + U_{CE}}{U_A}$$

**Schritt 2** (entscheidender Schritt): Ableiten nach $U_{CE}$ und $I_{C0}$ durch den Strom im Arbeitspunkt ausdrücken:

$$\frac{\partial I_C}{\partial U_{CE}} = \frac{I_{C0}}{U_A} = \frac{I_C}{U_A + U_{CE}}$$

**Ergebnis:**

$$r_{CE} = \frac{U_A + U_{CE}}{I_C}$$

**Woher die Faktoren kommen:** Der Zähler ist der Abstand des Arbeitspunkts vom gemeinsamen Schnittpunkt $-U_A$, der Nenner seine Höhe.

**Proben:** Einheit V/A = Ω. Zahlenwert: 75 V durch 2 mA ergibt 37,5 kΩ; die numerische Ableitung des Modells ebenso. Grenzfall: Ohne Early-Effekt, unendliche $U_A$, wird $r_{CE}$ unendlich, der Transistor eine ideale Stromquelle.

**Grenzen:** Reale Transistoren haben keine exakt gemeinsame Early-Spannung; das Datenblatt nennt deshalb den gemessenen Ausgangsleitwert. Nahe der Sättigung gilt die Gerade nicht mehr.
:::

::::beispiel Eingangs- und Ausgangswiderstand am Datenblattpunkt im Vergleich mit dem BC547C
**Gegeben:** Beispieltransistor bei 2 mA und 5 V: Basisstrom 4,00 µA, $\beta$ = 500, Steilheit 77,4 mS, $U_A$ = 70 V. Datenblatt des BC547C bei denselben Bedingungen und 1 kHz (Vishay, Gruppe C): Eingangswiderstand 6, typisch 8,7 und höchstens 15 kΩ; Ausgangsleitwert typisch 60 µS, höchstens 110 µS; Kleinsignal-Stromverstärkung (onsemi) 450, typisch 600, höchstens 900.

**Gesucht:** $r_{BE}$ und $r_{CE}$ des Beispieltransistors und der Vergleich.

**Rechnung:**

$$r_{BE} = \frac{25{,}85\ \mathrm{mV}}{4{,}00\ \mu\mathrm{A}} = 6{,}46\ \mathrm{k\Omega}, \qquad r_{CE} = \frac{70\ \mathrm{V} + 5\ \mathrm{V}}{2\ \mathrm{mA}} = 37{,}5\ \mathrm{k\Omega}$$

Der Kehrwert von $r_{CE}$ ist 26,7 µS. Mit dem typischen $\beta$ von 600 wäre der Eingangswiderstand 600 durch 77,4 mS, also 7,76 kΩ.

**Ergebnis:** **$r_{BE}$ = 6,46 kΩ, $r_{CE}$ = 37,5 kΩ.**

**Einordnung:** Der Eingangswiderstand liegt im Bereich des Datenblatts; vom typischen Wert trennt ihn vor allem das typische $\beta$ von 600 statt 500. Der Ausgangsleitwert ist mit 26,7 µS kleiner als der typische Wert 60 µS, der 16,7 kΩ entspricht: Der Beispieltransistor hat einen schwächeren Early-Effekt als ein typischer BC547C. In der Verstärkerstufe macht das 5,6 % der Verstärkung aus.
::::

:::frage
„Warum ist $r_{BE}$ so groß? Vom Emitter aus hat derselbe Übergang doch nur 27 Ω.“
Beide Werte beschreiben dieselbe Barriere, gesehen von verschiedenen Strömen. Eine Änderung von $U_{BE}$ ändert alle Ströme über die Barriere um denselben Bruchteil. Am Emitter fließt der ganze Strom, 0,949 mA; seine Änderung ist groß, der Widerstand $U_T$ durch Emitterstrom klein, 27,2 Ω, fast genau $r_e$. Durch die Basis fließt nur der 500. Teil; dieselbe Spannungsänderung bewegt dort 500-mal weniger Strom, der Widerstand ist 500-mal größer, 13,7 kΩ. Deshalb erscheint auch ein Widerstand im Emitterzweig, von der Basis aus gesehen, mit dem Faktor $\beta + 1$ vergrößert (Abschnitt *Der Emitterwiderstand im Signalweg*).
:::

:::frage
„Was bedeuten $h_{ie}$, $h_{fe}$ und $h_{oe}$ im Datenblatt?“
Datenblätter beschreiben den Transistor für kleine Signale als Zweitor in Hybridform ([Zweitore und ihre Parameter](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/zweitore.html)): Eingang zwischen Basis und Emitter, Ausgang zwischen Kollektor und Emitter, der Index e steht für die Emitterschaltung. $h_{ie}$ ist der Eingangswiderstand bei kurzgeschlossenem Ausgang, also $r_{BE}$; $h_{fe}$ die Kleinsignal-Stromverstärkung $\beta$; $h_{oe}$ der Ausgangsleitwert bei offenem Eingang, also der Kehrwert von $r_{CE}$. $h_{re}$ beschreibt, wie stark die Ausgangsspannung auf den Eingang zurückwirkt, beim BC547C typisch 3·10⁻⁴; fast immer lässt man diese Rückwirkung weg. Das Kleinsignal-Ersatzschaltbild im Abschnitt *Die Ersatzschaltbilder* ist genau dieses Zweitor ohne Rückwirkung.
:::

:::fehlvorstellung
„$r_{BE}$ und $r_{CE}$ sind Widerstände aus Halbleitermaterial im Transistor.“
Das liegt nahe, weil Ersatzschaltbilder sie mit demselben Symbol zeichnen wie echte Widerstände. Sie sind aber Steigungen von Kennlinien, also differentielle Widerstände: $r_{BE}$ entsteht an der Basis-Emitter-Barriere, $r_{CE}$ aus der Verformung der Basis durch den Early-Effekt. Deshalb hängen sie vom Arbeitspunkt ab: $r_{BE}$ beträgt bei 2 mA 6,46 kΩ, bei 0,947 mA 13,7 kΩ, $r_{CE}$ 37,5 bzw. 79,6 kΩ. Ein Stück Material hätte bei jedem Strom denselben Widerstand; die echten Bahnwiderstände der dotierten Gebiete gibt es auch, sie sind aber klein.
:::

## Die Ersatzschaltbilder

*Wie fasst man die realen Kennlinien in einer Schaltung aus Quellen und Widerständen zusammen, und was bleibt davon für die Änderungen?*

:::grafik
Szene: get1/bipolartransistoren/03-ersatzschaltbilder · Vorlage: schaltung-zustaende
**Abbildung 4:** Zwei Ersatzschaltbilder des npn-Transistors mit den Werten des Beispieltransistors bei 2 mA und 5 V. (a) Erweitertes Ersatzschaltbild nach Skript Bild 11.21: zwischen Basis und Emitter eine Spannungsquelle 0,647 V in Reihe mit $r_{BE}$ = 6,46 kΩ; zwischen Kollektor und Emitter eine gesteuerte Stromquelle, die das 500-Fache des Basisstroms abzüglich 0,133 mA liefert, parallel dazu $r_{CE}$ = 37,5 kΩ. (b) Kleinsignal-Ersatzschaltbild für die Änderungen: zwischen Basis und Emitter nur $r_{BE}$, zwischen Kollektor und Emitter die Stromquelle $g_m u_{be}$, gleichbedeutend mit $\beta i_b$, und $r_{CE}$. Für Änderungen fallen die festen Quellen weg; übrig bleiben der Eingangswiderstand, die gesteuerte Quelle und der Ausgangswiderstand.
:::

### Das erweiterte Ersatzschaltbild

Das Skript fasst die realen Kennlinien im erweiterten Ersatzschaltbild zusammen (S. 189, Bild 11.21), das es Großsignal-Ersatzschaltbild nennt: am Eingang eine Spannungsquelle in Reihe mit $R_{BE}$, am Ausgang eine Stromquelle parallel zu $R_{CE}$. Welche Werte die Quellen haben, sagt es nicht; man wählt sie passend zum Arbeitspunkt. Nimmt man die Tangenten an die Kennlinien im Arbeitspunkt, ergeben sich die Werte in Abbildung 4a.

**Die Akteure:**

- __$U_0$__: Spannung, bei der die Tangente an die Eingangskennlinie die Spannungsachse schneidet; 0,647 V am Datenblattpunkt.
- __$U_{BE,\mathrm{AP}}$__, __$U_{CE,\mathrm{AP}}$__: die Spannungen im Arbeitspunkt, an dem die Tangenten anliegen; 0,673 V und 5 V am Datenblattpunkt.

**Das Zusammenspiel:** Am Eingang ersetzt man die Exponentialkennlinie durch ihre Tangente im Arbeitspunkt. Die Tangente ist eine Gerade mit der Steigung $1/r_{BE}$ durch den Punkt $U_0$; eine Gerade dieser Art beschreibt eine Spannungsquelle $U_0$ in Reihe mit $r_{BE}$. Am Ausgang ersetzt man das Kennlinienfeld ebenso durch seine Tangente im Arbeitspunkt, nur in zwei Richtungen: Eine Änderung des Basisstroms ändert den Kollektorstrom um das $\beta$-Fache, eine Änderung von $U_{CE}$ um $1/r_{CE}$ je Volt. Das ergibt eine Stromquelle parallel zu $r_{CE}$. Sie liefert das $\beta$-Fache des Basisstroms, vermindert um den Strom, den $r_{CE}$ im Arbeitspunkt schon führt, 5 V durch 37,5 kΩ, also 0,133 mA.

:::formel Formel
$$U_{BE} = U_0 + r_{BE}\,I_B$$

$$U_0 = U_{BE,\mathrm{AP}} - U_T$$

$$I_C = \beta\,I_B + \frac{U_{CE} - U_{CE,\mathrm{AP}}}{r_{CE}}$$
:::

**So liest man das:** Die Eingangstangente schneidet die Achse immer genau eine Temperaturspannung tiefer, 0,647 V statt 0,673 V. Die Ausgangsgleichung stimmt bei 5 V für jeden Basisstrom; bei anderen Spannungen weicht sie ab, weil die echten Ausgangskennlinien von $-U_A$ aus auseinanderlaufen. Für einen anderen Arbeitspunkt ändern sich alle Werte.

Idee der Herleitung: Man legt im Arbeitspunkt Tangenten an die Eingangskennlinie und an das Ausgangskennlinienfeld und ordnet die Geradengleichungen nach Quellen und Widerständen.

:::herleitung
**Ausgangspunkt:** die Steigungen $1/r_{BE}$, $\beta$ und $1/r_{CE}$ aus dem Abschnitt *Die realen Kennlinien* und die Tangente einer Funktion im Arbeitspunkt.

**Annahmen:** (i) aktiver Bereich; (ii) Tangenten im Arbeitspunkt mit Basisstrom $I_{B,\mathrm{AP}}$ und Spannung $U_{CE,\mathrm{AP}}$; (iii) im Arbeitspunkt ist der Kollektorstrom das $\beta$-Fache des Basisstroms, wie im Modell.

**Schritt 1**: Tangente der Eingangskennlinie durch den Arbeitspunkt mit der Steigung $1/r_{BE}$:

$$U_{BE} = U_{BE,\mathrm{AP}} + r_{BE}\,(I_B - I_{B,\mathrm{AP}})$$

**Schritt 2** (entscheidender Schritt): Mit $r_{BE}$ gleich $U_T/I_{B,\mathrm{AP}}$ ist das Produkt $r_{BE}\,I_{B,\mathrm{AP}}$ genau $U_T$; der Achsenabschnitt ist deshalb:

$$U_0 = U_{BE,\mathrm{AP}} - r_{BE}\,I_{B,\mathrm{AP}} = U_{BE,\mathrm{AP}} - U_T$$

**Schritt 3**: Der Kollektorstrom hängt von $I_B$ und $U_{CE}$ ab; seine Tangentialebene im Arbeitspunkt hat in Richtung des Basisstroms die Steigung $\beta$, in Richtung von $U_{CE}$ die Steigung $1/r_{CE}$:

$$I_C = I_{C,\mathrm{AP}} + \beta\,(I_B - I_{B,\mathrm{AP}}) + \frac{U_{CE} - U_{CE,\mathrm{AP}}}{r_{CE}}$$

**Schritt 4**: Nach (iii) ist $I_{C,\mathrm{AP}}$ gleich $\beta I_{B,\mathrm{AP}}$; die Ruheströme heben sich weg:

$$I_C = \beta\,I_B + \frac{U_{CE} - U_{CE,\mathrm{AP}}}{r_{CE}}$$

**Ergebnis:**

$$U_{BE} = U_0 + r_{BE}\,I_B$$

$$U_0 = U_{BE,\mathrm{AP}} - U_T$$

$$I_C = \beta\,I_B + \frac{U_{CE} - U_{CE,\mathrm{AP}}}{r_{CE}}$$

**Woher die Faktoren kommen:** Dass $U_0$ genau $U_T$ unter dem Arbeitspunkt liegt, folgt aus der Exponentialform: Steigung und Höhe sind proportional, das Verhältnis ist $U_T$. Am Ausgang steht $\beta$, die Steigung in Richtung des Basisstroms; der Abzug $U_{CE,\mathrm{AP}}/r_{CE}$ ist der Strom, den $r_{CE}$ im Arbeitspunkt schon führt.

**Proben:** Einheiten V bzw. A. Zahlenwerte bei 2 mA: 672,7 mV − 25,85 mV = 646,9 mV; im Arbeitspunkt liefert die Quelle 500 mal 4 µA minus 0,133 mA, also 1,867 mA, und $r_{CE}$ führt 5 V durch 37,5 kΩ, 0,133 mA, zusammen 2,000 mA. Für Änderungen bleibt das $\beta$-Fache der Basisstromänderung, wie im Kleinsignal-Ersatzschaltbild.

**Grenzen:** Der Eingang ist nur in der Nähe von $I_{B,\mathrm{AP}}$ richtig beschrieben; bei halbem und doppeltem Basisstrom liegt die Gerade 5 bzw. 8 mV über der wahren Kennlinie. Am Ausgang stimmt die Gleichung bei 5 V für jeden Basisstrom; bei 2 µA und 10 V liegt sie 6,3 % zu hoch, bei 8 µA und 10 V 3,1 % zu tief.
:::

::::beispiel Werte des erweiterten Ersatzschaltbilds und seine Gültigkeit
**Gegeben:** Beispieltransistor am Datenblattpunkt: $U_{BE}$ = 672,7 mV, $I_B$ = 4,00 µA, $U_{CE}$ = 5 V, $r_{BE}$ = 6,46 kΩ, $\beta$ = 500, $r_{CE}$ = 37,5 kΩ; zum Vergleich die Basisströme 1, 2, 8 und 16 µA und die Spannungen 1 und 10 V.

**Gesucht:** $U_0$, der Abzug der Stromquelle und die Abweichungen des Ersatzschaltbilds vom Modell.

**Rechnung:**

$$U_0 = 672{,}7\ \mathrm{mV} - 25{,}85\ \mathrm{mV} = 646{,}9\ \mathrm{mV}, \qquad \frac{U_{CE,\mathrm{AP}}}{r_{CE}} = \frac{5\ \mathrm{V}}{37{,}5\ \mathrm{k\Omega}} = 0{,}133\ \mathrm{mA}$$

Die Gerade liefert bei 8 µA 646,9 mV plus 6,46 kΩ mal 8 µA, also 698,6 mV; die wahre Kennlinie hat dort 690,6 mV, 7,9 mV weniger. Ebenso: bei 2 µA 5,0 mV zu viel, bei 1 µA 16,4 mV, bei 16 µA 41,7 mV. Am Ausgang liefert das Ersatzschaltbild bei 2 µA und 10 V 1,133 mA, das Modell 1,067 mA; bei 8 µA und 10 V 4,133 gegen 4,267 mA; bei 5 V stimmt es für jeden Basisstrom.

**Ergebnis:** **$U_0$ = 0,647 V, Quelle 500 mal Basisstrom minus 0,133 mA; Eingang zwischen halbem und doppeltem Ruhestrom auf 8 mV genau, Ausgang bis 10 V auf gut 6 %.**

**Einordnung:** Das genügt für Arbeitspunktrechnungen, die die Schaltung ohnehin nur auf einige zehn Millivolt genau festlegt. Für die Signale des Verstärkers, Millivolt um den Arbeitspunkt, braucht man den festen Anteil gar nicht.
::::

:::frage
„Warum heißt das Ersatzschaltbild im Skript Großsignal-Ersatzschaltbild, wenn es mit diesen Werten nur nahe am Arbeitspunkt gilt?“
Weil es die Gesamtwerte liefert, die Ruhewerte samt Änderungen, und nicht nur die Änderungen. Mit Tangentenwerten gilt es in einem Bereich um den Arbeitspunkt, beim Beispieltransistor am Eingang zwischen etwa halbem und doppeltem Ruhestrom auf 8 mV, am Ausgang bis 10 V auf gut 6 % genau. Man kann die Werte auch so wählen, dass die Geraden einen größeren Bereich im Mittel am besten treffen, wie bei der Knickkennlinie der Diode; dann verteilt sich der Fehler. Für große Aussteuerung, etwa beim Schalten, ist die Exponentialkennlinie selbst nötig oder das einfachere Modell mit festen 0,6 V aus dem vorigen Artikel.
:::

### Das Kleinsignal-Ersatzschaltbild

**Die Akteure:**

- __$i_b$__, __$u_{ce}$__: Änderungen des Basisstroms und der Kollektor-Emitter-Spannung; mit $u_{be}$ und $i_c$ aus dem ersten Abschnitt die vier Kleinsignalgrößen.

**Das Zusammenspiel:** Jede Größe ist Ruhewert plus Änderung. Setzt man das in das erweiterte Ersatzschaltbild ein, erfüllen die Ruhewerte die Gleichungen schon für sich allein, und für die Änderungen bleibt eine eigene, lineare Schaltung übrig. Das ist das Überlagerungsprinzip ([Das Superpositionsverfahren](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/superpositionsverfahren.html)), angewandt auf Ruhewerte und Änderungen. Eine feste Spannungsquelle wie $U_0$ ändert ihre Spannung nie; für Änderungen wirkt sie wie ein Kurzschluss. Ebenso fällt der feste Abzug der Stromquelle weg. Am Eingang bleibt deshalb nur $r_{BE}$, am Ausgang die Quelle mit dem $\beta$-Fachen der Basisstromänderung und $r_{CE}$ parallel (Abbildung 4b).

Die gesteuerte Quelle lässt sich auf zwei Arten schreiben. Als stromgesteuerte Quelle liefert sie das $\beta$-Fache der Basisstromänderung, wie im Ersatzschaltbild des Skripts. Als spannungsgesteuerte Quelle liefert sie $g_m u_{be}$. Beides ist dasselbe, denn die Basisstromänderung ist $u_{be}/r_{BE}$ und das Produkt $g_m r_{BE}$ ist $\beta$. Physikalisch steuert die Spannung: $U_{BE}$ setzt die Barriere und damit den Kollektorstrom, der Basisstrom ist die Folge ([Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html), Abschnitt *Strom- oder Spannungssteuerung*). Die Stromsicht ist bequem, wenn die Basis über einen großen Widerstand angesteuert wird.

Dieselbe Regel gilt für die Schaltung um den Transistor. Die Versorgung liegt fest; für Änderungen ist ihr Anschluss mit Masse verbunden. Ein großer Kondensator ändert seine Spannung während einer Signalperiode kaum, wenn seine Zeitkonstante mit der umgebenden Schaltung lang gegen die Periode ist ([Laden und Entladen des Kondensators](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/laden-und-entladen.html)); für Signale wirkt er wie ein Kurzschluss, für Gleichstrom wie eine Unterbrechung.

:::formel Formel
$$i_b = \frac{u_{be}}{r_{BE}}, \qquad i_c = g_m\,u_{be} + \frac{u_{ce}}{r_{CE}} = \beta\,i_b + \frac{u_{ce}}{r_{CE}}$$
:::

**So liest man das:** Für Änderungen ist der Transistor ein lineares Zweitor aus drei Elementen: Der Eingang ist ein Widerstand, der Ausgang eine von $u_{be}$ gesteuerte Stromquelle mit einem Widerstand parallel. Am Datenblattpunkt sind das 6,46 kΩ, 77,4 mS und 37,5 kΩ, in der Verstärkerstufe 13,7 kΩ, 36,6 mS und 79,6 kΩ.

Idee der Herleitung: Man ersetzt die Kennlinien im Arbeitspunkt durch ihre Tangenten und rechnet nur mit den Änderungen.

:::herleitung
**Ausgangspunkt:** die Definitionen von $g_m$, $r_{BE}$ und $r_{CE}$ als Ableitungen der Kennlinien im Arbeitspunkt.

**Annahmen:** (i) kleine Änderungen, sodass die Tangenten genügen; (ii) keine Rückwirkung der Ausgangsspannung auf den Eingang; beim BC547C wirkt sie laut Datenblatt nur mit dem Bruchteil 3·10⁻⁴.

**Schritt 1**: Der Basisstrom hängt nach (ii) nur von $U_{BE}$ ab; seine Änderung ist die Steigung mal der Spannungsänderung:

$$i_b = \frac{\partial I_B}{\partial U_{BE}}\,u_{be} = \frac{u_{be}}{r_{BE}}$$

**Schritt 2** (entscheidender Schritt): Der Kollektorstrom hängt von $U_{BE}$ und $U_{CE}$ ab; seine Änderung ist die Summe beider Beiträge, jeder mit seiner Steigung:

$$i_c = \frac{\partial I_C}{\partial U_{BE}}\,u_{be} + \frac{\partial I_C}{\partial U_{CE}}\,u_{ce} = g_m\,u_{be} + \frac{u_{ce}}{r_{CE}}$$

**Schritt 3**: Mit $u_{be}$ gleich $r_{BE}\,i_b$ und $g_m r_{BE}$ gleich $\beta$:

$$g_m\,u_{be} = g_m\,r_{BE}\,i_b = \beta\,i_b$$

**Ergebnis:**

$$i_b = \frac{u_{be}}{r_{BE}}, \qquad i_c = g_m\,u_{be} + \frac{u_{ce}}{r_{CE}} = \beta\,i_b + \frac{u_{ce}}{r_{CE}}$$

**Woher die Faktoren kommen:** Jede Steigung einer Kennlinie wird zu einem Element: die Eingangssteigung zu $r_{BE}$, die Steuerwirkung zu $g_m$, die Ausgangssteigung zu $r_{CE}$.

**Proben:** Einheiten A. Grenzfall $u_{ce}$ = 0: Kollektorstromänderung gleich $\beta$ mal Basisstromänderung, wie in der Definition von $\beta$. Zahlenwert: 1 mV ergibt 73 nA Basis- und 36,6 µA Kollektorstromänderung, das Verhältnis 502.

**Grenzen:** nur für kleine Änderungen (Abschnitt *Groß- und Kleinsignal*) und niedrige Frequenzen; bei hohen Frequenzen kommen die Kapazitäten der Übergänge hinzu.
:::

## Die Spannungsverstärkung der Emitterschaltung

*Wie groß ist die Verstärkung einer Stufe, und wovon hängt sie ab?*

:::grafik
Szene: get1/bipolartransistoren/03-signalweg · Vorlage: schaltung-signalfluss
**Abbildung 5:** Kleinsignal-Ersatzschaltbild der Verstärkerstufe mit Emitterkondensator. Koppelkondensatoren, Emitterkondensator und Versorgung sind für Signale Kurzschlüsse; deshalb liegen die Teilerwiderstände 330 kΩ und 68 kΩ parallel zum Eingang und $R_C$ = 3,9 kΩ vom Kollektor nach Masse. Der Transistor ist durch $r_{BE}$ = 13,7 kΩ, die Stromquelle $g_m u_{be}$ mit 36,6 mS und $r_{CE}$ = 79,6 kΩ ersetzt. Eingetragen ist die Kette für 1 mV: 1 mV zwischen Basis und Emitter, 36,6 µA Kollektorstromänderung, −136 mV am Kollektor. Die Verstärkung ist die Steilheit mal dem Widerstand, in den die Stromänderung fließt.
:::

**Die Akteure:**

- __$C_1$__, __$C_2$__: __Koppelkondensatoren__ am Eingang und am Ausgang; je 1 µF. Sie lassen die Änderungen durch und trennen die Gleichspannungen der Stufe von Quelle und Last.
- __$C_E$__: __Emitterkondensator__ parallel zu $R_E$; 470 µF. Er hält das Emitterpotenzial für Signale fest; man sagt, er __überbrückt__ $R_E$.
- __$u_\mathrm{ein}$__, __$u_\mathrm{aus}$__: Signalspannungen am Eingang und am Ausgang, gegen Masse.
- __$v_u$__: __Spannungsverstärkung__, $u_\mathrm{aus}$ geteilt durch $u_\mathrm{ein}$; −136 in der Stufe.
- __$R_L$__: Lastwiderstand am Ausgang, etwa der Eingang der nächsten Stufe; 10 kΩ im Beispiel.
- __$r_\mathrm{ein}$__, __$r_\mathrm{aus}$__: __Eingangs-__ und __Ausgangswiderstand__ der Stufe. Mit $r_\mathrm{ein}$ belastet die Stufe die Quelle; mit $r_\mathrm{aus}$ wirkt sie auf die Last wie eine Quelle mit Innenwiderstand ([Ersatzquellen nach Thévenin und Norton](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/ersatzquellen-thevenin-norton.html)).

**Das Zusammenspiel in Schritten:**

**Schritt 1**: $C_1$ und $C_2$ sperren den Gleichstrom: Quelle und Last verschieben den Arbeitspunkt nicht, die Basis bleibt auf 1,602 V, der Kollektor auf 6,306 V. $C_E$ hält den Emitter für Signale auf seinen 0,949 V. Damit ist der Emitter der gemeinsame Anschluss von Ein- und Ausgang: eine Emitterschaltung.

**Schritt 2**: Weil der Emitter festliegt, erscheint die Eingangsänderung vollständig als $u_{be}$. Ein Millivolt ändert den Kollektorstrom um 36,6 µA.

**Schritt 3**: Die Stromänderung fließt durch $R_C$ zur Versorgung, die für Signale an Masse liegt, und zum kleinen Teil durch $r_{CE}$. Mehr Kollektorstrom heißt mehr Spannungsabfall an $R_C$ und damit ein tieferes Kollektorpotenzial: Das Ausgangssignal hat das umgekehrte Vorzeichen.

**Schritt 4**: Die Ausgangsänderung ist die Stromänderung mal $R_C$ parallel $r_{CE}$, 36,6 µA mal 3,72 kΩ, also −136 mV (Abbildung 5). Die Stromverstärkung $B$ kommt in dieser Kette nicht vor.

:::formel Formel
$$v_u = \frac{u_\mathrm{aus}}{u_\mathrm{ein}} = -g_m\,(R_C \parallel r_{CE} \parallel R_L) \approx -g_m\,R_C = -\frac{U_{RC}}{U_T}$$

$$r_\mathrm{ein} = R_1 \parallel R_2 \parallel r_{BE}$$

$$r_\mathrm{aus} = R_C \parallel r_{CE}$$
:::

**So liest man das:** $R_C \parallel r_{CE} \parallel R_L$ ist der Widerstand der Parallelschaltung, $U_{RC}$ die Ruhespannung an $R_C$. Ohne $r_{CE}$ und Last hängt die Verstärkung nur von dieser Ruhespannung ab: 3,694 V durch 25,85 mV ergibt −142,9. $r_{CE}$ senkt sie auf −136,2, eine Last von 10 kΩ auf −99,3. Weil $U_{RC}$ kleiner bleiben muss als die Versorgung, sind mit einem ohmschen Kollektorwiderstand an 10 V höchstens rund 387 möglich, in der Praxis deutlich weniger. Mehr erlaubt eine Stromquelle als Kollektorlast, etwa ein Stromspiegel; dann begrenzt $r_{CE}$, und die Grenze ist $g_m r_{CE}$, in der Stufe 2915. Der Eingangswiderstand von 11,0 kΩ ist vor allem $r_{BE}$, der Ausgangswiderstand von 3,72 kΩ vor allem $R_C$.

Idee der Herleitung: Man setzt das Kleinsignal-Ersatzschaltbild ein, schließt Versorgung und Kondensatoren kurz und wendet die Knotenregel am Kollektor an.

:::herleitung
**Ausgangspunkt:** das Kleinsignal-Ersatzschaltbild des Transistors und die Regel, dass Versorgung und große Kondensatoren für Signale Kurzschlüsse sind.

**Annahmen:** (i) $C_1$, $C_2$ und $C_E$ so groß, dass an ihnen keine Signalspannung abfällt; (ii) Quelle ohne Innenwiderstand; (iii) kleine Signale.

**Schritt 1**: Der Emitter liegt für Signale an Masse, die Basis an der Quelle:

$$u_{be} = u_\mathrm{ein}$$

**Schritt 2**: Am Kollektor liegen für Signale $R_C$ (über die Versorgung), $R_L$ (über $C_2$) und $r_{CE}$ parallel nach Masse. Die Stromquelle zieht $g_m u_{be}$ aus dem Kollektorknoten zum Emitter; die Knotenregel am Kollektor lautet:

$$g_m\,u_{be} + \frac{u_\mathrm{aus}}{R_C \parallel r_{CE} \parallel R_L} = 0$$

**Schritt 3** (entscheidender Schritt): Nach $u_\mathrm{aus}$ aufgelöst; das Minus entsteht, weil die Quelle Strom aus dem Knoten zieht:

$$u_\mathrm{aus} = -g_m\,(R_C \parallel r_{CE} \parallel R_L)\,u_\mathrm{ein}$$

**Schritt 4**: Ohne $r_{CE}$ und Last, mit $g_m$ gleich $I_C/U_T$ und $I_C R_C$ gleich der Ruhespannung $U_{RC}$:

$$v_u \approx -g_m\,R_C = -\frac{I_C\,R_C}{U_T} = -\frac{U_{RC}}{U_T}$$

**Schritt 5**: Von der Quelle aus liegen $R_1$ (über die Versorgung), $R_2$ und $r_{BE}$ (über den festgehaltenen Emitter) parallel nach Masse:

$$r_\mathrm{ein} = R_1 \parallel R_2 \parallel r_{BE}$$

**Schritt 6**: Vom Ausgang aus, bei kurzgeschlossenem Eingang, ist $u_{be}$ null und die Stromquelle liefert nichts; es bleiben $R_C$ und $r_{CE}$ parallel:

$$r_\mathrm{aus} = R_C \parallel r_{CE}$$

**Ergebnis:**

$$v_u = -g_m\,(R_C \parallel r_{CE} \parallel R_L) \approx -g_m\,R_C = -\frac{U_{RC}}{U_T}$$

$$r_\mathrm{ein} = R_1 \parallel R_2 \parallel r_{BE}$$

$$r_\mathrm{aus} = R_C \parallel r_{CE}$$

**Woher die Faktoren kommen:** $g_m$ wandelt die Eingangsspannung in einen Strom, der Widerstand am Kollektor wandelt ihn zurück in eine Spannung; das Minus ist die Richtung der Stromquelle.

**Proben:** Einheit S mal Ω, die Verstärkung ist eine reine Zahl. Zahlenwert: 36,6 mS mal 3,718 kΩ ergibt 136,2; die numerische Rechnung mit dem vollständigen Modell ebenso. Grenzfall: Ohne Ruhestrom ist die Steilheit null und die Verstärkung auch.

**Grenzen:** Hat die Quelle einen Innenwiderstand, teilt sich die Eingangsspannung zwischen ihm und $r_\mathrm{ein}$. Bei tiefen Frequenzen wirken die Kondensatoren nicht mehr als Kurzschlüsse.
:::

::::beispiel Verstärkung, Eingangs- und Ausgangswiderstand der Verstärkerstufe
**Gegeben:** Stufe aus dem vorigen Artikel (10 V; 330 kΩ und 68 kΩ; $R_C$ = 3,9 kΩ; $R_E$ = 1 kΩ mit $C_E$); Arbeitspunkt nach dem vollständigen Modell 0,947 mA und 5,36 V; daraus 36,6 mS, $r_{BE}$ = 13,7 kΩ, $r_{CE}$ = 79,6 kΩ; Last 10 kΩ über $C_2$.

**Gesucht:** Verstärkung ohne und mit Last, Eingangs- und Ausgangswiderstand.

**Rechnung:** Ohne Last:

$$R_C \parallel r_{CE} = \frac{3{,}9\ \mathrm{k\Omega}\cdot79{,}6\ \mathrm{k\Omega}}{3{,}9\ \mathrm{k\Omega} + 79{,}6\ \mathrm{k\Omega}} = 3{,}72\ \mathrm{k\Omega}, \qquad v_u = -36{,}6\ \mathrm{mS}\cdot3{,}72\ \mathrm{k\Omega} = -136$$

Mit 10 kΩ Last liegen 2,71 kΩ am Kollektor:

$$v_u = -36{,}6\ \mathrm{mS}\cdot2{,}71\ \mathrm{k\Omega} = -99{,}3$$

Eingangs- und Ausgangswiderstand, mit dem Teiler 56,4 kΩ:

$$r_\mathrm{ein} = 56{,}4\ \mathrm{k\Omega} \parallel 13{,}7\ \mathrm{k\Omega} = 11{,}0\ \mathrm{k\Omega}, \qquad r_\mathrm{aus} = 3{,}72\ \mathrm{k\Omega}$$

**Ergebnis:** **$v_u$ = −136 ohne, −99,3 mit 10 kΩ Last; $r_\mathrm{ein}$ = 11,0 kΩ, $r_\mathrm{aus}$ = 3,72 kΩ.**

**Einordnung:** Die Last nimmt ein Viertel der Verstärkung, weil sie mit dem Ausgangswiderstand von 3,72 kΩ einen Spannungsteiler bildet. Der vereinfachte Wert −142,9 aus der Ruhespannung am Kollektorwiderstand liegt nur 5 % über dem genauen.
::::

:::fehlvorstellung
„Die Spannungsverstärkung ist $B$.“
Das liegt nahe, weil $B$ die bekannteste Kennzahl des Transistors ist und er den Basisstrom um $B$ verstärkt. Die Spannungsverstärkung entsteht aber aus Steilheit und Kollektorwiderstand; $B$ bestimmt nur, wie viel Strom die Quelle liefern muss, also den Eingangswiderstand. Exemplare mit $B$ = 420 und 800 verstärken in der Stufe −133,8- und −141,2-fach, 1,8 % weniger und 3,7 % mehr als mit $B$ = 500; das liegt allein daran, dass ihr Ruhestrom um −1,9 und +3,9 % abweicht (0,930 und 0,984 mA). Ihr Eingangswiderstand dagegen ändert sich von 9,72 auf 15,3 kΩ.
:::

:::frage
„Woher kommt die Leistung des verstärkten Signals?“
Aus der Versorgung. Der Transistor steuert nur, wie viel Strom sie durch $R_C$ schickt. Die Stufe nimmt aus der Versorgung 9,73 mW auf. Ein Signal von 1 mV gibt am Eingang 45 pW ab, an einer Last von 10 kΩ kommen 493 nW an, rund das 10 900-Fache. Fast die gesamte aufgenommene Leistung wird in $R_C$, $R_E$ und im Transistor zu Wärme; ein winziger Teil, gesteuert vom Eingang, geht als Signal an die Last.
:::

:::frage
„Wie groß müssen die Kondensatoren sein?“
So groß, dass ihre Zeitkonstante mit dem Widerstand, den sie sehen, lang gegen die Signalperiode ist. $C_1$ sieht den Eingangswiderstand 11,0 kΩ; mit 1 µF beträgt die Zeitkonstante 11 ms. Allein würde er die Verstärkung bei 14 Hz auf 71 % senken; diese Frequenz heißt __untere Grenzfrequenz__, ihre Rechnung braucht die Wechselstromrechnung. $C_E$ sieht nur $R_E$ parallel $r_e$, 26,6 Ω, weil vom Emitter aus der Transistor mit $r_e$ wirkt. Für eine ähnliche Grenze von 13 Hz braucht er deshalb 470 µF; mit 100 µF läge sie bei 60 Hz. $C_2$ mit 1 µF vor 10 kΩ Last ergibt 12 Hz. Alle drei zusammen senken die Verstärkung schon bei 30 Hz auf 71 % und bei 50 Hz auf 87 %.
:::

Wie groß das Eingangssignal sein darf, entscheidet die Verzerrung. Nach Abbildung 2 schwingt der Kollektorstrom bei 10 mV um +47 % und −32 %; am Ausgang der Stufe wird daraus eine unsymmetrische Schwingung. Eine verzerrte Schwingung enthält außer der __Grundschwingung__ mit der Signalfrequenz __Oberschwingungen__ mit der doppelten, dreifachen Frequenz; beim Audioverstärker hört man sie als Klirren.

**Die Akteure:**

- __$\hat u_{be}$__: Amplitude der sinusförmigen Änderung zwischen Basis und Emitter; 1 bis 10 mV im Beispiel.
- __$k_2$__: Anteil der Oberschwingung mit doppelter Frequenz, ihre Amplitude geteilt durch die der Grundschwingung; in Prozent. Der __Klirrfaktor__ fasst alle Oberschwingungen zusammen; weil die höheren hier viel kleiner sind, bei 10 mV 0,45 %, ist er praktisch gleich $k_2$.

:::formel Formel
$$k_2 \approx \frac{\hat u_{be}}{4\,U_T}$$
:::

**So liest man das:** Der Klirrfaktor wächst proportional zur Eingangsamplitude: rund 1 % bei 1 mV, rund 10 % bei 10 mV. Wer weniger als 1 % will, darf die Emitterschaltung mit etwa 1 mV ansteuern; am Ausgang sind das dann 136 mV. Die Skala ist wieder $U_T$, und deshalb ist dieser Wert für jeden Bipolartransistor derselbe.

Idee der Herleitung: Man entwickelt die Exponentialfunktion bis zum quadratischen Glied und zerlegt das Quadrat des Sinus in einen Gleichanteil und eine Schwingung doppelter Frequenz.

:::herleitung
**Ausgangspunkt:** die Transfergleichung, nach der der Kollektorstrom mit $\exp(u_{be}/U_T)$ wächst, und die Reihenentwicklung der Exponentialfunktion.

**Annahmen:** (i) Emitter für Signale fest, sodass die ganze Eingangsänderung als $u_{be}$ wirkt; (ii) $\hat u_{be}$ klein genug, dass die Glieder dritter und höherer Ordnung keine Rolle spielen; (iii) der Ausgang ist proportional zur Kollektorstromänderung, ohne Early-Effekt.

**Schritt 1**: Relative Stromänderung mit der Abkürzung $x$ für $\hat u_{be}/U_T$:

$$\frac{i_c}{I_C} = \exp\big(x\,\sin\omega t\big) - 1 \approx x\,\sin\omega t + \frac{x^2}{2}\,\sin^2\omega t$$

**Schritt 2** (entscheidender Schritt): Das Quadrat des Sinus ist ein Gleichanteil plus eine Schwingung doppelter Frequenz:

$$\sin^2\omega t = \frac{1}{2} - \frac{1}{2}\,\cos 2\omega t$$

**Schritt 3**: Eingesetzt:

$$\frac{i_c}{I_C} \approx \frac{x^2}{4} + x\,\sin\omega t - \frac{x^2}{4}\,\cos 2\omega t$$

**Schritt 4**: Verhältnis der Amplituden von doppelter und einfacher Frequenz:

$$k_2 = \frac{x^2/4}{x} = \frac{x}{4} = \frac{\hat u_{be}}{4\,U_T}$$

**Ergebnis:**

$$k_2 \approx \frac{\hat u_{be}}{4\,U_T}$$

**Woher die Faktoren kommen:** Die 2 im Nenner des quadratischen Glieds und die 2 aus der Zerlegung des Quadrats ergeben zusammen die 4. Der Gleichanteil $x^2/4$ aus Schritt 3 verschiebt zugleich den Mittelwert des Stroms nach oben.

**Proben:** ohne Einheit. Zahlenwerte: 1 mV durch 4 mal 25,85 mV ergibt 0,97 %, 10 mV ergeben 9,7 %; die genaue Zerlegung der reinen Exponentialfunktion liefert 0,967 % und 9,61 %. Grenzfall: Für verschwindende Amplitude verschwindet die Verzerrung, die Kennlinie wirkt als Tangente.

**Grenzen:** Ab etwa 10 mV werden die höheren Glieder merklich. Der Early-Effekt wirkt in der Stufe als schwache Gegenkopplung und senkt den Klirrfaktor etwas, auf 0,88 % bzw. 8,7 %.
:::

::::beispiel Verzerrung der Verstärkerstufe bei 1 mV und bei 10 mV
**Gegeben:** Verstärkerstufe mit $C_E$ (vollständiges Modell), Verstärkung −136; Eingangsamplituden 1 mV und 10 mV.

**Gesucht:** Klirrfaktor, Ausschläge des Kollektorpotenzials nach unten und oben.

**Rechnung:** Nach der Näherung:

$$k_2 \approx \frac{1\ \mathrm{mV}}{4\cdot25{,}85\ \mathrm{mV}} = 0{,}97\ \%, \qquad k_2 \approx \frac{10\ \mathrm{mV}}{4\cdot25{,}85\ \mathrm{mV}} = 9{,}7\ \%$$

Die Rechnung mit dem vollständigen Modell ergibt 0,88 % und 8,7 %. Bei 10 mV sinkt das Kollektorpotenzial um 1,63 V, steigt aber nur um 1,15 V; sein Mittelwert liegt 120 mV unter dem Ruhewert.

**Ergebnis:** **0,9 % Klirrfaktor bei 1 mV, 8,7 % bei 10 mV; bei 10 mV ist der Ausschlag nach unten um gut 40 % größer als nach oben.**

**Einordnung:** 8,7 % hört man als deutliches Klirren. Unter 0,1 % bliebe der Klirrfaktor nach der Näherung erst bei Eingangsamplituden unter 0,1 mV.
::::

:::fehlvorstellung
„Kleinsignal heißt, dass auch das Ausgangssignal klein ist.“
Das liegt nahe, weil das Wort nach kleinen Spannungen überall klingt. Klein sein muss die Änderung, die die Kennlinie des Transistors steuert, also $u_{be}$ gegen $U_T$; der Ausgang ist um die Verstärkung größer: 1 mV am Eingang ergeben 136 mV am Ausgang bei 0,9 % Klirrfaktor. Wie groß er werden darf, hängt deshalb von der Verstärkung ab. Mit Emitterkondensator erlaubt 1 % Klirrfaktor nur 0,155 V, obwohl Versorgung und Sättigung am Kollektor 3,7 V Platz ließen; mit Gegenkopplung über $R_E$ bleibt der Klirrfaktor bei 1 V Ausgang bei 0,18 %.
:::

## Der Emitterwiderstand im Signalweg

*Was ändert sich, wenn der Emitterkondensator fehlt, und warum baut man Stufen trotzdem oft so?*

:::grafik
Szene: get1/bipolartransistoren/03-emitterwiderstand · Vorlage: kennlinie-parameter
**Abbildung 6:** Verstärkerstufe mit und ohne Emitterkondensator (vollständiges Modell). (a) Übertragungskennlinien, Änderung des Kollektorpotenzials über der Änderung des Basispotenzials: mit $C_E$ Steigung −136, schon bei ±10 mV deutlich gekrümmt (−1,63 V und +1,15 V); ohne $C_E$ Steigung −3,78, bis ±263 mV fast gerade (−1,00 V und +0,99 V). (b) Ausgangsspannung mit 1 V Amplitude über eine Periode: mit $C_E$ aus 7,3 mV Eingang, unsymmetrisch (−1,14 V und +0,88 V), Klirrfaktor 6,4 %; ohne $C_E$ aus 263 mV Eingang, symmetrisch, 0,18 %. Der Emitterwiderstand tauscht Verstärkung gegen Linearität.
:::

**Die Akteure:**

- __$1 + g_m R_E$__: Faktor, um den die Gegenkopplung bei gleicher Eingangsspannung $u_{be}$ und damit die Verstärkung verkleinert; 37,6 in der Stufe, ohne $r_{CE}$ gerechnet.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Ohne $C_E$ liegt der Emitter nur über $R_E$ an Masse. Jede Änderung des Emitterstroms ändert das Emitterpotenzial um das $R_E$-Fache der Stromänderung.

**Schritt 2**: Hebt das Signal die Basis, steigt der Strom und mit ihm das Emitterpotenzial; zwischen Basis und Emitter bleibt nur der Rest. Das ist die Stromgegenkopplung, die im vorigen Artikel den Arbeitspunkt festhält ([Arbeitspunkt und Grundschaltungen des Transistors](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/arbeitspunkt-und-grundschaltungen.html), Abschnitt *Stromgegenkopplung mit Emitterwiderstand*), jetzt für das Signal.

**Schritt 3**: Der Rest ist klein, denn für eine Stromänderung braucht der Transistor nur das $r_e$-Fache an Spannung, 27,3 Ω gegen 1 kΩ. Fast die ganze Eingangsänderung liegt an $R_E$; die Stromänderung ist die Eingangsänderung geteilt durch $R_E + r_e$.

**Schritt 4**: Diese Stromänderung fließt durch $R_C$: Die Verstärkung ist ungefähr $R_C$ durch $R_E + r_e$, also −3,80; das vollständige Modell ergibt −3,78. Sie ist ein Verhältnis zweier Widerstände. Steilheit, $B$ und Temperatur stecken nur noch im kleinen $r_e$.

**Schritt 5**: Der Preis: Die Verstärkung sinkt um den Faktor 36, von −136 auf −3,78; ohne $r_{CE}$ gerechnet ist der Faktor genau $1 + g_m R_E$. Gewonnen ist Linearität: Die gekrümmte Kennlinie bestimmt nur noch $u_{be}$, ein 37,6stel der Eingangsspannung; der Rest fällt am linearen $R_E$ ab. Bei 1 V Ausgangsamplitude sind es deshalb 0,18 % Klirrfaktor statt 6,4 % (Abbildung 6b). Gewonnen ist Unabhängigkeit: Exemplare mit $B$ = 420 und 800 verstärken −3,786- und −3,796-fach statt −133,8- und −141,2-fach. Und der Eingangswiderstand des Transistors steigt von 13,7 kΩ auf 517 kΩ.

:::formel Formel
$$v_u = -\frac{\beta\,R_C}{r_{BE} + (\beta + 1)\,R_E} \approx -\frac{R_C}{R_E + r_e}$$

$$r_{\mathrm{ein},T} = r_{BE} + (\beta + 1)\,R_E$$
:::

**So liest man das:** $r_{\mathrm{ein},T}$ ist der Eingangswiderstand des Transistors allein, ohne den Basisspannungsteiler. Für großes $\beta$ geht die Verstärkung in das Widerstandsverhältnis über; ohne $R_E$ wird sie wieder $-g_m R_C$. Vom Eingang aus erscheint $R_E$ um den Faktor $\beta + 1$ vergrößert, weil durch ihn der ganze Emitterstrom fließt, durch die Basis aber nur der $(\beta + 1)$-te Teil davon. $r_{CE}$ fehlt in der Formel, weil er mit $R_E$ im Emitterzweig wie 2,8 MΩ wirkt; neben 3,9 kΩ spielt das keine Rolle. In der Praxis legt man die Verstärkung über den Teil von $R_E$ fest, der im Signalweg bleibt, und überbrückt nur den Rest mit $C_E$; der Arbeitspunkt hängt am ganzen $R_E$ und bleibt dabei unverändert.

Idee der Herleitung: Man setzt das Kleinsignal-Ersatzschaltbild mit $R_E$ im Emitterzweig ein und geht einmal um den Eingangskreis.

:::herleitung
**Ausgangspunkt:** das Kleinsignal-Ersatzschaltbild des Transistors, die Maschenregel im Eingangskreis und die Knotenregel am Emitter.

**Annahmen:** (i) $C_1$ und $C_2$ Kurzschlüsse, kein $C_E$; (ii) Quelle ohne Innenwiderstand; (iii) $r_{CE}$ vernachlässigt: Mit $R_E$ im Emitterzweig wirkt er vom Kollektor aus wie 2,8 MΩ, groß gegen $R_C$; (iv) keine Last.

**Schritt 1**: Knotenregel am Emitter: Durch $R_E$ fließt die Summe aus Basis- und Kollektorstromänderung:

$$i_e = i_b + \beta\,i_b = (\beta + 1)\,i_b$$

**Schritt 2** (entscheidender Schritt): Maschenregel von der Quelle über $r_{BE}$ und $R_E$ nach Masse; durch $R_E$ fließt der $(\beta + 1)$-fache Basisstrom:

$$u_\mathrm{ein} = r_{BE}\,i_b + R_E\,(\beta + 1)\,i_b$$

**Schritt 3**: Daraus Basisstrom und Eingangswiderstand des Transistors:

$$i_b = \frac{u_\mathrm{ein}}{r_{BE} + (\beta + 1)\,R_E}$$

$$r_{\mathrm{ein},T} = \frac{u_\mathrm{ein}}{i_b} = r_{BE} + (\beta + 1)\,R_E$$

**Schritt 4**: Die Kollektorstromänderung $\beta i_b$ zieht Strom aus dem Kollektorknoten; am Ausgang:

$$u_\mathrm{aus} = -\beta\,i_b\,R_C = -\frac{\beta\,R_C}{r_{BE} + (\beta + 1)\,R_E}\,u_\mathrm{ein}$$

**Schritt 5**: Zähler und Nenner durch $\beta$ geteilt; mit $r_{BE}/\beta$ gleich $1/g_m$, also $r_e$, und $(\beta + 1)/\beta$ fast 1:

$$v_u = -\frac{R_C}{r_e + \frac{\beta + 1}{\beta}\,R_E} \approx -\frac{R_C}{R_E + r_e}$$

**Ergebnis:**

$$v_u = -\frac{\beta\,R_C}{r_{BE} + (\beta + 1)\,R_E} \approx -\frac{R_C}{R_E + r_e}$$

$$r_{\mathrm{ein},T} = r_{BE} + (\beta + 1)\,R_E$$

**Woher die Faktoren kommen:** $\beta + 1$ zählt Basis- und Kollektorstrom, die beide durch $R_E$ fließen; $r_e$ ist der kleine Spannungsbedarf des Transistors selbst.

**Proben:** ohne Einheit bzw. Ω. Zahlenwerte: 502,4 mal 3,9 kΩ durch 13,71 kΩ plus 503,4 mal 1 kΩ ergibt −3,789; die Näherung −3,796; das vollständige Modell −3,782. Grenzfall $R_E$ = 0: Es bleibt $-\beta R_C/r_{BE}$, also $-g_m R_C$ wie mit Emitterkondensator.

**Grenzen:** Mit Last tritt $R_C \parallel R_L$ an die Stelle von $R_C$; bei sehr kleinem $R_E$ wird $r_{CE}$ wieder wichtig.
:::

::::beispiel Verstärkerstufe ohne Emitterkondensator
**Gegeben:** dieselbe Stufe ohne $C_E$: $R_C$ = 3,9 kΩ, $R_E$ = 1 kΩ, $\beta$ = 502, $r_{BE}$ = 13,7 kΩ, $r_e$ = 27,3 Ω, Teiler 56,4 kΩ.

**Gesucht:** Verstärkung, Eingangswiderstand der Stufe, Klirrfaktor bei 1 V Ausgangsamplitude.

**Rechnung:**

$$v_u = -\frac{502{,}4\cdot3{,}9\ \mathrm{k\Omega}}{13{,}71\ \mathrm{k\Omega} + 503{,}4\cdot1\ \mathrm{k\Omega}} = -3{,}79, \qquad v_u \approx -\frac{3{,}9\ \mathrm{k\Omega}}{1\ \mathrm{k\Omega} + 27{,}3\ \Omega} = -3{,}80$$

Eingangswiderstand des Transistors 517 kΩ, mit dem Teiler:

$$r_\mathrm{ein} = 56{,}4\ \mathrm{k\Omega} \parallel 517\ \mathrm{k\Omega} = 50{,}8\ \mathrm{k\Omega}$$

Für 1 V am Ausgang braucht die Stufe 263 mV am Eingang; das vollständige Modell ergibt dann 0,18 % Klirrfaktor, mit $C_E$ bei 7,3 mV Eingang 6,4 %.

**Ergebnis:** **$v_u$ = −3,79 (vollständiges Modell −3,78), $r_\mathrm{ein}$ = 50,8 kΩ, 0,18 % Klirrfaktor statt 6,4 %.**

**Einordnung:** Die Verstärkung ist um den Faktor 36 kleiner, der Klirrfaktor bei gleicher Ausgangsamplitude um den Faktor 35. Jetzt begrenzt der Basisspannungsteiler den Eingangswiderstand.

**Variation:** Bleiben nur 100 Ω von $R_E$ im Signalweg und werden die übrigen 900 Ω durch $C_E$ überbrückt, ergibt die Formel −30,6, das vollständige Modell −30,3, bei 30,0 kΩ Eingangswiderstand. Der Arbeitspunkt bleibt derselbe, weil für Gleichstrom weiterhin 1 kΩ wirken.
::::

## Die drei Grundschaltungen für kleine Signale

*Wie verhalten sich Emitter-, Kollektor- und Basisschaltung für kleine Signale?*

:::grafik
Szene: get1/bipolartransistoren/03-grundschaltungen-kleinsignal · Vorlage: schaltung-zustaende
**Abbildung 7:** Kleinsignal-Ersatzschaltbilder der drei Grundschaltungen beim selben Ruhestrom 0,947 mA (36,6 mS, $r_{BE}$ = 13,7 kΩ, $\beta$ = 502) mit je 3,9 kΩ am Ausgang. (a) Emitterschaltung: Eingang an der Basis, Emitter an Masse, Ausgang am Kollektor. (b) Kollektorschaltung: Eingang an der Basis, Kollektor über die Versorgung an Masse, Ausgang am Emitter mit 3,9 kΩ. (c) Basisschaltung: Basis an Masse, Eingang am Emitter, Ausgang am Kollektor. Zu jeder Schaltung Verstärkung, Eingangs- und Ausgangswiderstand. Welcher Anschluss gemeinsam ist, bestimmt, wie Spannung, Strom und Widerstände übertragen werden.
:::

Im vorigen Artikel haben die drei Grundschaltungen ihre Gleichspannungskennlinien gezeigt (Abschnitt *Die drei Grundschaltungen*). Für kleine Signale ersetzt man den Transistor durch sein Kleinsignal-Ersatzschaltbild und erhält für jede Schaltung Verstärkung, Eingangs- und Ausgangswiderstand. Die Tabelle vergleicht sie beim selben Ruhestrom.

| Grundschaltung | Kleinsignalverhalten bei 0,947 mA und 3,9 kΩ |
|---|---|
| Emitterschaltung | Verstärkung −136, kehrt um; Eingangswiderstand 13,7 kΩ; Ausgangswiderstand 3,72 kΩ; Stromverstärkung 502 bei kurzgeschlossenem Ausgang |
| Kollektorschaltung (Emitterfolger) | Verstärkung 0,993; Eingangswiderstand 1,88 MΩ; Ausgangswiderstand 27,3 Ω plus Quellwiderstand durch 503; Stromverstärkung 503 |
| Basisschaltung | Verstärkung +136, kehrt nicht um; Eingangswiderstand 27,2 Ω; Ausgangswiderstand 3,72 kΩ; Stromverstärkung 0,998 |

Die __Kollektorschaltung__ verstärkt die Spannung nicht, aber sie verwandelt Widerstände: Am Eingang erscheint ihr Emitterwiderstand um $\beta + 1$ vergrößert, am Ausgang der Innenwiderstand der Quelle um $\beta + 1$ verkleinert. Sie heißt deshalb auch __Impedanzwandler__: Eine hochohmige Quelle kann über sie eine niederohmige Last treiben.

:::formel Formel
$$v_u = \frac{R_E}{R_E + r_e}, \qquad r_\mathrm{ein} = r_{BE} + (\beta + 1)\,R_E, \qquad r_\mathrm{aus} \approx r_e + \frac{R_q}{\beta + 1}$$
:::

**So liest man das:** $R_q$ ist der Innenwiderstand der Signalquelle; $R_E$ steht für alles, was am Emitter für Signale nach Masse liegt, auch $r_{CE}$, weil der Kollektor über die Versorgung an Masse liegt. Die Verstärkung liegt knapp unter 1, weil zwischen Basis und Emitter die kleine Spannung $r_e i_e$ bleibt. Vom Ausgang aus sieht man den Transistor als $r_e$ und die Quelle durch den Faktor $\beta + 1$ verkleinert: Mit 10 kΩ Quellwiderstand sind es 27,3 Ω plus 19,9 Ω, zusammen 47,2 Ω.

Idee der Herleitung: Dieselbe Masche wie beim Emitterwiderstand, nur wird jetzt die Spannung am Emitterwiderstand als Ausgang abgegriffen.

:::herleitung
**Ausgangspunkt:** das Kleinsignal-Ersatzschaltbild, die Maschenregel im Eingangskreis und die Knotenregel am Emitter.

**Annahmen:** (i) Kollektor über die Versorgung an Masse; (ii) $r_{CE}$ liegt damit für Signale parallel zum Emitterwiderstand, und $R_E$ steht für diese Parallelschaltung; (iii) keine weitere Last.

**Schritt 1**: Wie im Abschnitt *Der Emitterwiderstand im Signalweg* ist der Eingangswiderstand und der Emitterstrom:

$$r_\mathrm{ein} = r_{BE} + (\beta + 1)\,R_E, \qquad i_e = (\beta + 1)\,i_b = \frac{(\beta + 1)\,u_\mathrm{ein}}{r_{BE} + (\beta + 1)\,R_E}$$

**Schritt 2** (entscheidender Schritt): Ausgang ist die Spannung an $R_E$; Zähler und Nenner durch $\beta + 1$ geteilt, mit $r_{BE}/(\beta + 1)$ fast $r_e$:

$$v_u = \frac{R_E\,i_e}{u_\mathrm{ein}} = \frac{(\beta + 1)\,R_E}{r_{BE} + (\beta + 1)\,R_E} \approx \frac{R_E}{R_E + r_e}$$

**Schritt 3**: Ausgangswiderstand ohne $R_E$: Eine Änderung $u$ am Emitter, bei Quelle mit Innenwiderstand $R_q$ an der Basis, treibt den Basisstrom $u/(R_q + r_{BE})$ und damit den Emitterstrom $(\beta + 1)$ mal so viel:

$$r_\mathrm{aus} = \frac{R_q + r_{BE}}{\beta + 1} \approx r_e + \frac{R_q}{\beta + 1}$$

**Ergebnis:**

$$v_u = \frac{R_E}{R_E + r_e}, \qquad r_\mathrm{ein} = r_{BE} + (\beta + 1)\,R_E, \qquad r_\mathrm{aus} \approx r_e + \frac{R_q}{\beta + 1}$$

**Woher die Faktoren kommen:** Der Faktor $\beta + 1$ ist das Verhältnis von Emitter- zu Basisstrom; er vergrößert Widerstände auf der Emitterseite, von der Basis aus gesehen, und verkleinert Widerstände auf der Basisseite, vom Emitter aus gesehen.

**Proben:** Einheiten stimmen. Zahlenwerte bei 0,947 mA mit 3,9 kΩ parallel 79,6 kΩ, also 3,72 kΩ: 3,72 kΩ durch 3,745 kΩ ergibt 0,993; 13,7 kΩ plus 503,4 mal 3,72 kΩ ergibt 1,88 MΩ. Der Emitterfolger aus dem vorigen Artikel (5 V, 1 kΩ, 2 V am Eingang) hat bei 2 V nach der Formel 0,981, das vollständige Modell ergibt 0,9807; zwischen 2 und 3 V gemittelt sind es 0,985, wie im vorigen Artikel.

**Grenzen:** Mit großer Last am Emitter tritt $R_E \parallel R_L$ an die Stelle von $R_E$; der Ausgangswiderstand gilt für kleine Signale um den Arbeitspunkt.
:::

::::beispiel Emitterfolger als Impedanzwandler
**Gegeben:** Kollektorschaltung bei 0,947 mA mit $R_E$ = 3,9 kΩ, für Signale parallel zu $r_{CE}$ = 79,6 kΩ, zusammen 3,72 kΩ ($r_e$ = 27,3 Ω, $\beta$ = 502); Signalquelle mit 10 kΩ Innenwiderstand.

**Gesucht:** Eingangs- und Ausgangswiderstand, Verstärkung.

**Rechnung:**

$$r_\mathrm{ein} = 13{,}7\ \mathrm{k\Omega} + 503{,}4\cdot3{,}72\ \mathrm{k\Omega} = 1{,}88\ \mathrm{M\Omega}, \qquad r_\mathrm{aus} \approx 27{,}3\ \Omega + \frac{10\ \mathrm{k\Omega}}{503{,}4} = 47{,}2\ \Omega$$

$$v_u = \frac{3{,}72\ \mathrm{k\Omega}}{3{,}72\ \mathrm{k\Omega} + 27{,}3\ \Omega} = 0{,}993$$

**Ergebnis:** **Eingang 1,88 MΩ, Ausgang 47,2 Ω, Verstärkung 0,993.**

**Einordnung:** Die Quelle mit 10 kΩ sieht fast nur Leerlauf; die Last sieht statt 10 kΩ eine Quelle mit 47 Ω, also gut 200-mal niederohmiger. Deshalb steht der Emitterfolger am Ausgang vieler Verstärker, vor dem Lautsprecher oder dem Kabel.
::::

Die __Basisschaltung__ hat dieselbe Verstärkung wie die Emitterschaltung, aber ohne Umkehr: Das Signal steuert $U_{BE}$ jetzt vom Emitter aus, und eine steigende Emitterspannung verkleinert $U_{BE}$. Ihr Eingang ist niederohmig, denn die Quelle muss den ganzen Emitterstrom liefern, und ihr Strom kommt fast vollständig am Kollektor heraus. Man nutzt sie, wo ein Strom mit kleinem Spannungshub aufgenommen werden soll und bei hohen Frequenzen.

:::formel Formel
$$v_u = +g_m\,R_C$$

$$r_\mathrm{ein} = \frac{1}{g_m + 1/r_{BE}} \approx r_e$$
:::

**So liest man das:** Verstärkung wie bei der Emitterschaltung, nur mit positivem Vorzeichen, hier +142,9 ohne $r_{CE}$ und +136,2 mit. Der Eingangswiderstand ist der Kehrwert der Summe aus Steilheit und Basisleitwert, 27,2 Ω.

Idee der Herleitung: Man setzt das Kleinsignal-Ersatzschaltbild mit der Basis an Masse ein; die Eingangsspannung liegt jetzt mit umgekehrtem Vorzeichen als $u_{be}$ an.

:::herleitung
**Ausgangspunkt:** das Kleinsignal-Ersatzschaltbild und die Knotenregel am Emitter.

**Annahmen:** (i) Basis für Signale an Masse; (ii) Quelle ohne Innenwiderstand am Emitter; (iii) $r_{CE}$ vernachlässigt.

**Schritt 1**: Mit der Basis an Masse und dem Signal am Emitter ist:

$$u_{be} = -u_\mathrm{ein}$$

**Schritt 2** (entscheidender Schritt): Am Ausgang zieht die Stromquelle $g_m u_{be}$ aus dem Kollektorknoten; wie bei der Emitterschaltung ist $u_\mathrm{aus}$ gleich $-g_m u_{be} R_C$, mit Schritt 1:

$$u_\mathrm{aus} = -g_m\,u_{be}\,R_C = +g_m\,R_C\,u_\mathrm{ein}$$

**Schritt 3**: Die Quelle nimmt den Strom auf, der aus dem Emitter fließt, Basis- und Kollektoranteil zusammen. Gezählt als Strom $i_q$ aus der Quelle in den Emitter:

$$i_q = -\Big(\frac{u_{be}}{r_{BE}} + g_m\,u_{be}\Big) = u_\mathrm{ein}\Big(\frac{1}{r_{BE}} + g_m\Big), \qquad r_\mathrm{ein} = \frac{u_\mathrm{ein}}{i_q} = \frac{1}{g_m + 1/r_{BE}}$$

**Ergebnis:**

$$v_u = +g_m\,R_C$$

$$r_\mathrm{ein} = \frac{1}{g_m + 1/r_{BE}} \approx r_e$$

**Woher die Faktoren kommen:** Das Vorzeichen kehrt sich um, weil die Eingangsspannung $U_{BE}$ von der Emitterseite aus verändert; $1/r_{BE}$ ist der kleine Basisanteil des Emitterstroms.

**Proben:** Einheiten stimmen. Zahlenwerte: 36,6 mS mal 3,9 kΩ ergibt 142,9; 1 durch 36,6 mS plus 0,073 mS ergibt 27,2 Ω. Grenzfall: Ohne Basisstrom, unendliches $r_{BE}$, wird $r_\mathrm{ein}$ genau $r_e$.

**Grenzen:** Mit Innenwiderstand der Quelle teilt sich die Eingangsspannung zwischen diesem und dem kleinen $r_\mathrm{ein}$; eine Quelle mit 1 kΩ verliert fast alles, weshalb man die Basisschaltung mit Strömen ansteuert.
:::

## Spannungsstabilisierung mit Z-Diode und Transistor

*Wie hält ein Transistor eine Ausgangsspannung fest, obwohl die Eingangsspannung schwankt und die Last Strom zieht?*

:::grafik
Szene: get1/bipolartransistoren/03-stabilisierung · Vorlage: schaltung-und-zeitverlauf
**Abbildung 8:** (a) Spannungsstabilisierung nach Skript Bild 11.28 mit den Werten des Beispiels: Eingangsspannung 12 V mit ±1 V Brummen, $R_1$ = 1 kΩ von der Eingangsspannung zur Basis, Z-Diode 5,6 V von der Basis nach Masse, Kollektor an der Eingangsspannung, Ausgang am Emitter mit 200 Ω Last. (b) Zwei gestapelte Zeitverläufe: oben die Eingangsspannung zwischen 11 und 13 V; unten die Ausgangsspannung zwischen 4,870 und 4,910 V, dazu gestrichelt die Z-Diode allein mit 330 Ω Vorwiderstand an derselben Last, die zwischen 4,15 und 4,91 V dem Eingang folgt. Der Transistor gibt die Spannung der Z-Diode, um $U_{BE}$ vermindert, an die Last weiter; das Brummen wird 50-mal kleiner.
:::

Hinter einem Gleichrichter mit Glättungskondensator schwankt die Spannung mit 100 Hz, im Takt der gleichgerichteten Halbwellen; diese Restwelligkeit heißt __Brummen__ ([Gleichrichtung und Ladungspumpe](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/gleichrichtung-und-ladungspumpe.html)). Eine Z-Diode mit Vorwiderstand glättet sie, solange die Last wenig Strom braucht ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html), Abschnitt *Die Z-Diode*): Eine 5,6-V-Z-Diode mit 330 Ω an 1 kΩ Last ergab dort den Glättungsfaktor 17,8. An 200 Ω versagt dieselbe Schaltung. Der Vorwiderstand kann den Laststrom nicht mehr liefern, die Z-Diode sperrt, und der Ausgang folgt dem Eingang zwischen 4,15 und 4,91 V. Das Skript zeigt die Lösung (S. 192–193, Bild 11.28): einen Transistor als Emitterfolger zwischen Z-Diode und Last (Abbildung 8).

**Die Akteure:**

- __$U_\mathrm{ein}$__: Eingangsspannung, 12 V mit ±1 V Brummen; im Skript $U_E$.
- __$U_\mathrm{aus}$__: stabilisierte Ausgangsspannung am Emitter; 4,89 V; im Skript $U_A$.
- __$R_1$__: Vorwiderstand, der Z-Diode und Basis versorgt; 1 kΩ.
- __$U_Z$__, __$r_Z$__: Spannung der Z-Diode, 5,6 V bei 5 mA, und ihr differentieller Widerstand, 20 Ω.
- __$R_L$__: Last; 200 Ω, entsprechend 24,5 mA.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: $R_1$ und die Z-Diode bilden die Stabilisierung aus dem Diodenartikel; die Z-Diode hält die Basis auf 5,63 V.

**Schritt 2**: Der Transistor arbeitet als Emitterfolger: Sein Emitter folgt der Basis, um $U_{BE}$ tiefer. Bei 24,5 mA Laststrom sind das 0,737 V, der Ausgang liegt auf 4,890 V.

**Schritt 3**: Der Laststrom fließt vom Eingang durch Kollektor und Emitter. Über die Basis fließt nur sein 500. Teil, 48 µA; nur diesen muss $R_1$ zusätzlich zum Z-Strom liefern, nicht den Laststrom. Deshalb darf $R_1$ dreimal so groß sein wie der Vorwiderstand der Z-Diode allein, und die Z-Diode führt trotzdem 5,4 bis 7,3 mA.

**Schritt 4**: Der Transistor nimmt die Differenz zwischen Eingangs- und Ausgangsspannung auf, 7,1 V bei 12 V Eingang, und setzt dabei 174 mW in Wärme um. Weil er in Reihe zur Last liegt, heißt die Schaltung __Längsregler__.

**Schritt 5**: Ein Volt mehr am Eingang treibt rund 1 mA mehr durch $R_1$; die Z-Diode nimmt ihn auf, und ihre Spannung steigt nur um 20 mV. Der Emitterfolger gibt das weiter: Aus 2 V Brummen am Eingang werden 39,7 mV am Ausgang.

:::formel Formel
$$U_\mathrm{aus} = U_Z - U_{BE}$$
:::

**So liest man das:** Die Ausgangsspannung liegt um die Basis-Emitter-Spannung unter der Z-Spannung, hier 5,627 V − 0,737 V = 4,890 V. Das Skript schreibt $U_A = U_Z + U_{BE}$ (S. 193). Nach Bild 11.28 zeigt der Zählpfeil von $U_{BE}$ aber von der Basis zum Emitter, und der Ausgang liegt am Emitter; die Masche ergibt ein Minus. Mit dem Plus wären es 6,36 V. So hoch kann der Emitter eines leitenden npn-Transistors nicht liegen, denn die Basis liegt auf 5,63 V.

Idee der Herleitung: Maschenregel von Masse über die Z-Diode zur Basis, über die Basis-Emitter-Strecke zum Emitter und über den Ausgang zurück.

:::herleitung
**Ausgangspunkt:** die Maschenregel und die Zählpfeile aus Skript Bild 11.28: $U_Z$ von der Kathode der Z-Diode (Basisknoten) zur Masse, $U_{BE}$ von der Basis zum Emitter, $U_\mathrm{aus}$ vom Emitter zur Masse.

**Annahmen:** (i) Die Z-Diode arbeitet im Durchbruch; (ii) der Transistor leitet im aktiven Bereich.

**Schritt 1** (entscheidender Schritt): Vom Basisknoten zur Masse führen zwei Wege, direkt über die Z-Diode oder über die Basis-Emitter-Strecke und den Ausgang; beide ergeben dieselbe Spannung:

$$U_Z = U_{BE} + U_\mathrm{aus}$$

**Schritt 2**: Nach dem Ausgang aufgelöst:

$$U_\mathrm{aus} = U_Z - U_{BE}$$

**Ergebnis:**

$$U_\mathrm{aus} = U_Z - U_{BE}$$

**Woher die Faktoren kommen:** Das Minus steht da, weil die Basis-Emitter-Spannung zwischen dem festen Basispotenzial und dem Ausgang liegt.

**Proben:** Einheit V. Zahlenwert: 5,627 V − 0,737 V = 4,890 V; das vollständige Modell ergibt ebenso 4,890 V. Vorzeichen: Der Ausgang muss unter dem Basispotenzial liegen, sonst wäre der Basis-Emitter-Übergang gesperrt.

**Grenzen:** $U_Z$ und $U_{BE}$ sind keine Festwerte: $U_{BE}$ steigt mit dem Laststrom um 60 mV je Zehnfaches, $U_Z$ mit dem Z-Strom um 20 mV je Milliampere; ohne Durchbruch der Z-Diode gilt die Formel nicht.
:::

:::formel Formel
$$G = \frac{\Delta U_\mathrm{ein}}{\Delta U_\mathrm{aus}} \approx 1 + \frac{R_1}{r_Z}$$
:::

**So liest man das:** Der __Glättungsfaktor__ $G$ ist das Verhältnis der Schwankungen von Eingang und Ausgang. Er hängt hier nur vom Teiler aus $R_1$ und $r_Z$ ab und wird umso größer, je größer $R_1$ ist; das erlaubt erst der Transistor, weil über $R_1$ kein Laststrom mehr fließen muss. Mit 1 kΩ und 20 Ω sind es 51, genau gerechnet 50,4.

Idee der Herleitung: Für die Brummänderungen bilden $R_1$ und $r_Z$ einen Spannungsteiler, und der Emitterfolger gibt die Änderung am Basisknoten fast unverändert an den Ausgang.

:::herleitung
**Ausgangspunkt:** das Kleinsignalbild der Schaltung: Die Z-Diode wirkt für Änderungen als $r_Z$, der Transistor als Emitterfolger.

**Annahmen:** (i) Die Änderung des Basisstroms ist klein gegen die des Z-Stroms, denn vom Basisknoten aus wirkt der Transistor mit Last wie $r_{BE} + (\beta + 1) R_L$, rund 100 kΩ gegen 20 Ω; (ii) die Verstärkung des Emitterfolgers ist fast 1, weil zwischen Basis und Emitter nur die Spannung an $r_e$ = 1,06 Ω liegt, gegen 200 Ω Last; (iii) der Early-Effekt bleibt außer Acht.

**Schritt 1**: Spannungsteiler aus $R_1$ und $r_Z$ für die Änderungen:

$$\Delta U_Z = \frac{r_Z}{R_1 + r_Z}\,\Delta U_\mathrm{ein}$$

**Schritt 2** (entscheidender Schritt): Der Emitterfolger gibt die Änderung weiter:

$$\Delta U_\mathrm{aus} \approx \Delta U_Z = \frac{r_Z}{R_1 + r_Z}\,\Delta U_\mathrm{ein}$$

**Schritt 3**: Kehrwert des Verhältnisses:

$$G = \frac{\Delta U_\mathrm{ein}}{\Delta U_\mathrm{aus}} \approx \frac{R_1 + r_Z}{r_Z} = 1 + \frac{R_1}{r_Z}$$

**Ergebnis:**

$$G \approx 1 + \frac{R_1}{r_Z}$$

**Woher die Faktoren kommen:** Das Verhältnis $R_1/r_Z$ ist der Teiler; die 1 entsteht, weil die Änderung über $R_1$ und $r_Z$ zusammen abfällt.

**Proben:** ohne Einheit. Zahlenwert: 1 + 1000 Ω/20 Ω = 51; das vollständige Modell ergibt 2 V durch 39,7 mV, also 50,4. Grenzfall: Ohne Vorwiderstand ist $G$ gleich 1, der Ausgang folgt dem Eingang.

**Grenzen:** Der Early-Effekt und der Basisstrom senken $G$ etwas; ohne Durchbruch der Z-Diode, bei zu kleiner Eingangsspannung, bricht die Glättung zusammen.
:::

::::beispiel Längsregler an 12 V mit Brummen
**Gegeben:** Eingangsspannung 11 bis 13 V; $R_1$ = 1 kΩ; Z-Diode 5,6 V bei 5 mA mit $r_Z$ = 20 Ω (wie im Diodenartikel); Beispieltransistor; Last 200 Ω. Zum Vergleich die Z-Diode allein mit 330 Ω Vorwiderstand an derselben Last.

**Gesucht:** Ausgangsspannung, Brummen am Ausgang, Glättungsfaktor, Ströme und Verlustleistung des Transistors.

**Rechnung:** Bei 12 V liefert das vollständige Modell 5,627 V an der Z-Diode und 0,737 V zwischen Basis und Emitter:

$$U_\mathrm{aus} = 5{,}627\ \mathrm{V} - 0{,}737\ \mathrm{V} = 4{,}890\ \mathrm{V}, \qquad I_L = \frac{4{,}890\ \mathrm{V}}{200\ \Omega} = 24{,}5\ \mathrm{mA}$$

Bei 11 V sind es 4,870 V, bei 13 V 4,910 V:

$$G = \frac{2\ \mathrm{V}}{39{,}7\ \mathrm{mV}} = 50{,}4$$

Basisstrom 48 µA, Z-Strom 5,35 mA bei 11 V und 7,31 mA bei 13 V. Verlustleistung des Transistors bei 12 V:

$$P = (12\ \mathrm{V} - 4{,}89\ \mathrm{V})\cdot24{,}4\ \mathrm{mA} = 174\ \mathrm{mW}$$

Die Z-Diode allein liefert an 200 Ω nur 4,15 bis 4,91 V und führt keinen Strom; sie stabilisiert nicht.

**Ergebnis:** **4,890 V am Ausgang, 39,7 mV Brummen statt 2 V, Glättungsfaktor 50; der Transistor setzt 149 bis 198 mW um.**

**Einordnung:** Der BC547 verträgt nach onsemi 625 mW, nach Vishay 500 mW; bei 198 mW erwärmt er sich mit 200 bzw. 250 K/W um 40 bis 50 K. Gegen die Z-Diode allein gewinnt die Schaltung zweierlei: Sie liefert den Laststrom überhaupt, und sie glättet besser, weil der Vorwiderstand größer sein darf.
::::

:::grafik
Szene: get1/bipolartransistoren/03-lastkennlinie · Vorlage: kennlinie-parameter
**Abbildung 9:** Ausgangsspannung über dem Laststrom bei 12 V Eingang, Laststrom logarithmisch von 0,5 bis 50 mA. Längsregler: von 4,991 V bei 0,5 mA über 4,932 V bei 4,9 mA und 4,890 V bei 24,5 mA bis 4,871 V bei 48,7 mA, ein Abfall von 60 mV je Zehnfaches. Z-Diode allein mit 330 Ω: 5,86 V bei 0,6 mA, 5,52 V bei 18,4 mA, darüber sperrt sie, und die Spannung bricht ein, auf 2,79 V bei 27,9 mA. Der Transistor liefert den Laststrom; die Ausgangsspannung hängt nur noch über $U_{BE}$ schwach von ihm ab.
:::

Mehr Laststrom verlangt eine größere Basis-Emitter-Spannung, 60 mV je Zehnfaches des Stroms, und um diesen Betrag sinkt die Ausgangsspannung (Abbildung 9): Zwischen 0,5 und 48,7 mA fällt sie um 0,12 V. Für kleine Laständerungen um 24,5 mA wirkt der Regler wie eine Quelle mit 1,1 Ω Innenwiderstand, nach der Formel des Emitterfolgers $r_e$ plus der kleine Anteil der Basisseite. Die Z-Diode allein hat 18,9 Ω und sperrt oberhalb von 19,7 mA ganz. Der Laststrom ist nur durch den Transistor begrenzt: Bei 100 Ω, 48,7 mA, setzt er bei 13 V Eingang schon 396 mW um, gut 60 % der 625 mW nach onsemi und fast 80 % der 500 mW nach Vishay.

Das Skript nennt als Bedingung, dass die Eingangsspannung über $U_Z$ liegen muss (S. 193). Das ist nötig, reicht aber nicht: Die Z-Diode braucht einen Mindeststrom, damit sie im Durchbruch bleibt, und den muss $R_1$ zusammen mit dem Basisstrom liefern. Für 1 mA Z-Strom bei 200 Ω Last muss die Eingangsspannung deshalb mindestens 6,57 V betragen, fast ein Volt über der Z-Spannung.

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Steilheit | Eine kleine Änderung von $U_{BE}$ ändert den Strom um denselben Bruchteil; je mehr Ruhestrom, desto mehr Stromänderung. |
| Verzerrung | Gleichmäßig nur, solange $u_{be}$ klein gegen $U_T$ bleibt; die Exponentialkennlinie hebt stärker, als sie senkt. |
| reale Kennlinien und Ersatz­schaltbilder | Für Änderungen zählen nur Steigungen: Eingangs­widerstand, Steilheit, Ausgangs­widerstand. |
| Spannungs­verstärkung | Der Kollektor­widerstand verwandelt die Stromänderung zurück in eine Spannung; $B$ kommt nicht vor. |
| Emitter­widerstand | Die gekrümmte Kennlinie bestimmt nur noch einen kleinen Teil der Eingangsspannung: weniger Verstärkung, dafür linear und unabhängig vom Transistor. |
| Grund­schaltungen | Der gemeinsame Anschluss entscheidet, ob die Steilheit Spannung verstärkt oder Widerstände wandelt. |
| Spannungs­stabilisierung | Die Z-Diode setzt die Spannung, der Transistor liefert den Strom; seine Steilheit macht den Ausgang niederohmig. |

Ein Transistor verstärkt, weil eine kleine Änderung der Basis-Emitter-Spannung den Kollektorstrom mit der Steilheit $I_C/U_T$ ändert und ein Widerstand diese Stromänderung in eine große Spannungsänderung verwandelt; gleichmäßig gelingt das nur für Änderungen, die klein gegen $U_T$ sind, und ein Emitterwiderstand tauscht Verstärkung gegen Linearität und Unabhängigkeit vom Transistor.

## Bedeutung und Ausblick

Die Emitterschaltung mit Emitterwiderstand im Signalweg ist die Grundform diskreter Vorverstärker. Im Audioverstärker des Praktikums arbeitet der BC547C so, mit einem kleinen, nicht überbrückten Emitterwiderstand; zwei Emitterfolger aus BC337 und BC327 treiben dort als Gegentaktstufe den Lautsprecher. Längsregler stecken in vielen Netzteilen. Integrierte Festspannungsregler wie die Reihe 78xx enthalten denselben Längstransistor, steuern ihn aber über einen Verstärker, der die Ausgangsspannung mit einer Referenz vergleicht; dadurch wird auch der Abfall von 60 mV je Zehnfaches viel kleiner.

Die Rechnungen gelten für kleine Signale und niedrige Frequenzen. Bei hohen Frequenzen kommen die Kapazitäten der pn-Übergänge hinzu; der BC547 verstärkt Ströme typisch bis 300 MHz (Transitfrequenz), Spannungsverstärkungen wie hier aber nur bis zu deutlich tieferen Frequenzen. Wie sich mit vielen solchen Stufen und konsequenter Gegenkopplung ein nahezu idealer Verstärker bauen lässt, zeigt [Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html).

:::kern
- Gesamtwert ist Ruhewert plus Kleinsignal; linear nur, solange $u_{be}$ klein gegen $U_T$ bleibt, Klirrfaktor $k_2 \approx \hat u_{be}/(4U_T)$.
- Steilheit $g_m = I_C/U_T$, unabhängig von $B$ und Bauart; ihr Kehrwert ist $r_e$.
- Eingangswiderstand $r_{BE} = \beta/g_m$; Ausgangswiderstand $r_{CE}$ aus dem Early-Effekt, umso größer, je größer $U_A$ und je kleiner $I_C$.
- Kleinsignal-Ersatzschaltbild: $r_{BE}$, Quelle $g_m u_{be}$ gleich $\beta i_b$, $r_{CE}$; feste Spannungen und große Kondensatoren sind für Signale Kurzschlüsse.
- Emitterschaltung: $v_u \approx -g_m R_C = -U_{RC}/U_T$, mit $r_{CE}$ und Last parallel zu $R_C$; sie kehrt um, $B$ kommt nicht vor.
- Emitterwiderstand im Signalweg: $v_u \approx -R_C/(R_E + r_e)$; um $1 + g_m R_E$ weniger Verstärkung, dafür linear und unabhängig vom Transistor.
- Kollektorschaltung: Verstärkung knapp 1, Widerstände um $\beta + 1$ gewandelt; Basisschaltung: $+g_m R_C$ bei Eingangswiderstand $r_e$.
- Längsregler: $U_\mathrm{aus} = U_Z - U_{BE}$; der Laststrom fließt durch den Transistor, über $R_1$ nur Z- und Basisstrom, deshalb glättet der Teiler aus $R_1$ und $r_Z$ stark.
:::

:::quiz
F: Warum darf die Änderung zwischen Basis und Emitter nur wenige Millivolt groß sein?
A: Der Kollektorstrom wächst exponentiell mit $U_{BE}$; eine Änderung multipliziert ihn mit einem Faktor, der nur von $u_{be}/U_T$ abhängt. Proportional ist die Stromänderung nur für $u_{be}$ klein gegen $U_T$; 10 mV heben den Strom um 47 %, senken ihn aber nur um 32 %, und die Stufe klirrt mit 8,7 %.
F: Wie groß ist die Steilheit bei 0,947 mA, und welche Kollektorstromänderung bewirkt 1 mV?
A: 0,947 mA durch 25,85 mV ergibt 36,6 mS; 1 mV ändert den Kollektorstrom um 36,6 µA.
F: Warum hängt die Spannungsverstärkung der Emitterschaltung nicht von $B$ ab?
A: Die Eingangsspannung setzt über die Steilheit $I_C/U_T$ direkt den Kollektorstrom, und $R_C$ verwandelt dessen Änderung zurück in eine Spannung: $v_u$ ist etwa $-g_m R_C$, also $-U_{RC}/U_T$. $B$ bestimmt nur den Basisstrom und damit den Eingangswiderstand.
F: Stimmt es, dass die Spannungsverstärkung gleich $B$ ist?
A: Nein. Die Stufe verstärkt −136-fach bei $B$ = 500; Exemplare mit 420 und 800 liefern −133,8 und −141,2, nur weil sich ihr Ruhestrom um −1,9 bzw. +3,9 % verschiebt. Bei gleichem Ruhestrom wäre die Verstärkung gleich.
F: Stimmt es, dass bei Kleinsignalen auch das Ausgangssignal klein sein muss?
A: Nein. Klein sein muss $u_{be}$ gegen $U_T$; der Ausgang ist um die Verstärkung größer, aus 1 mV werden 136 mV. Wie groß er sein darf, hängt von der Verstärkung ab: mit Emitterkondensator 0,155 V bei 1 % Klirrfaktor, mit Gegenkopplung über $R_E$ 1 V bei 0,18 %.
F: Warum macht ein Emitterwiderstand im Signalweg die Verstärkung fast unabhängig vom Transistor?
A: Ohne Emitterkondensator folgt der Emitter der Basis; fast die ganze Eingangsänderung liegt an $R_E$, zwischen Basis und Emitter bleibt nur ein kleiner Rest. Die Stromänderung ist die Eingangsänderung durch $R_E + r_e$, die Verstärkung etwa $-R_C/(R_E + r_e)$, also −3,8; Exemplare mit $B$ = 420 und 800 liefern −3,786 und −3,796.
F: Warum fallen die festen Quellen im Kleinsignal-Ersatzschaltbild weg?
A: Eine feste Spannung ändert sich nie; für Änderungen wirkt sie wie ein Kurzschluss. Nach dem Überlagerungsprinzip erfüllen die Ruhewerte ihre Gleichungen für sich, und für die Änderungen bleibt eine lineare Schaltung aus $r_{BE}$, der Quelle $g_m u_{be}$ und $r_{CE}$.
F: Stimmt es, dass $r_{BE}$ ein Widerstand aus Halbleitermaterial ist?
A: Nein. $r_{BE}$ ist die Steigung der Eingangskennlinie, ein differentieller Widerstand der Basis-Emitter-Barriere. Er hängt vom Arbeitspunkt ab: 6,46 kΩ bei 2 mA, 13,7 kΩ bei 0,947 mA.
F: Welche Ausgangsspannung liefert der Längsregler mit der 5,6-V-Z-Diode an 200 Ω bei 12 V, und was ergäbe die Formel des Skripts?
A: $U_Z - U_{BE}$ ergibt 5,627 V − 0,737 V = 4,890 V. Mit dem Plus des Skripts wären es 6,36 V, mehr als die 5,63 V an der Basis; das ist bei leitendem Transistor unmöglich.
F: Warum glättet der Längsregler besser als die Z-Diode allein?
A: Über $R_1$ fließt kein Laststrom mehr, außer dem Z-Strom nur der Basisstrom, 48 µA statt 24,5 mA; deshalb darf $R_1$ 1 kΩ groß sein, und die Z-Spannung ändert sich nur um den Bruchteil $r_Z/(R_1 + r_Z)$ des Brummens. Der Glättungsfaktor ist 50 statt 17,8, und an 200 Ω würde die Z-Diode allein gar nicht mehr stabilisieren.
:::
