---
title: Der Transistor als Verstärker
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Bipolartransistoren
order: 110500
summary: Wie ein Bipolartransistor eine kleine Spannungsänderung in eine große verwandelt und wovon die Verstärkung abhängt: Groß- und Kleinsignal, Steilheit, reale Kennlinien und Kleinsignal-Ersatzschaltbild, Spannungsverstärkung der Emitterschaltung mit und ohne Emitterwiderstand, die Grundschaltungen für kleine Signale und die Spannungsstabilisierung mit Z-Diode und Transistor. Kompakte Fassung; die ausführliche enthält zusätzlich Herleitung und Gültigkeit des erweiterten Ersatzschaltbilds, Kondensatoren und Grenzfrequenz, den Datenblattvergleich, die Herleitungen zu Kollektor- und Basisschaltung und das Lastverhalten des Längsreglers.
tags: Verstärker, Kleinsignal, Ersatzschaltbild, Steilheit, Spannungsverstärkung, Emitterschaltung
stil: 3
fassung: kompakt
---

## Worum es geht

Ein Mikrofon liefert Spannungsänderungen von wenigen Millivolt, ein Lautsprecher braucht Volt. Ein Transistor, der in seinem Arbeitspunkt ruht, kann eine kleine Änderung in eine große, formgleiche verwandeln.
**Ein Transistor verstärkt, weil eine kleine Änderung der Basis-Emitter-Spannung den Kollektorstrom mit der Steilheit $I_C/U_T$ ändert und ein Widerstand diese Stromänderung in eine große Spannungsänderung verwandelt; gleichmäßig gelingt das nur für Änderungen, die klein gegen $U_T$ sind, und ein Emitterwiderstand tauscht Verstärkung gegen Linearität und Unabhängigkeit vom Transistor.**

Vorausgesetzt werden die Transfergleichung aus [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html), die Verstärkerstufe mit Stromgegenkopplung aus [Arbeitspunkt und Grundschaltungen des Transistors](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/arbeitspunkt-und-grundschaltungen.html) und der differentielle Widerstand aus [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html).

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

Zum Verstärken ruht der Transistor in einem Arbeitspunkt im aktiven Bereich; das Signal ist eine kleine Änderung um diesen Ruhezustand.

**Die Akteure:**

- __Ruhewerte__: die Werte im Arbeitspunkt, groß geschrieben ($U_{BE}$, $I_C$, $U_{CE}$); in der Verstärkerstufe 0,653 V, 0,947 mA und 5,36 V.
- __Kleinsignal__: die Änderungen um diese Ruhewerte, klein geschrieben ($u_{be}$, $i_c$, $u_{ce}$); einige Millivolt bzw. Mikroampere. Der momentane Wert ist Ruhewert plus Änderung; mit __Großsignal__ meint man diese Gesamtwerte und ihr Verhalten auf der ganzen, gekrümmten Kennlinie.
- __$U_T$__: Temperaturspannung, 25,85 mV bei 300 K; die Spannungsskala der Exponentialkennlinie.
- __$g_m$__: __Steilheit__, Änderung des Kollektorstroms je Änderung der Basis-Emitter-Spannung; in mS (Milliampere je Volt); 36,6 mS in der Stufe.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Nach der Transfergleichung ([Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html), Abschnitt *Der Transistoreffekt*) wächst der Kollektorstrom exponentiell mit $U_{BE}$: je 25,85 mV um den Faktor 2,72, je 59,5 mV um den Faktor 10.

**Schritt 2**: Eine Änderung $u_{be}$ multipliziert den Strom deshalb mit einem Faktor, der nur von $u_{be}/U_T$ abhängt. 1 mV mehr heben ihn um 3,94 %, 1 mV weniger senken ihn um 3,79 %.

**Schritt 3**: Ist $u_{be}$ klein gegen $U_T$, ändert sich der Strom proportional zur Spannung; die Kennlinie wirkt wie ihre Tangente (Abbildung 2). Das ist dieselbe Linearisierung wie beim differentiellen Widerstand der Diode ([Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html), Abschnitt *Der differentielle Widerstand*), nur steuert hier die Basis-Emitter-Spannung den Strom im Kollektorzweig.

**Schritt 4**: Bei größeren Änderungen bricht die Proportionalität: 10 mV heben den Strom um 47 %, −10 mV senken ihn nur um 32 %. Ein Sinus wird unsymmetrisch weitergegeben, also verzerrt. Als klein gilt eine Änderung, solange $u_{be}$ klein gegen $U_T$ bleibt, praktisch höchstens einige Millivolt.

:::formel Formel
$$g_m = \frac{\partial I_C}{\partial U_{BE}}\Big|_{U_{CE}\ \mathrm{fest}} = \frac{I_C}{U_T}$$
:::

**So liest man das:** Die Steilheit ist die Steigung der Tangente; aus $u_{be}$ macht sie die Stromänderung $g_m u_{be}$. Sie hängt nur vom Ruhestrom und der Temperatur ab, nicht von $B$ oder der Bauart: 36,6 mS in der Stufe, 77,4 mS bei 2 mA. Ihr Kehrwert heißt $r_e$, hier 27,3 Ω.

Idee der Herleitung: Ableiten der Transfergleichung; die Exponentialfunktion reproduziert sich dabei selbst.

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

**Gesucht:** Steilheit und Stromänderungen nach der Tangente und genau.

**Rechnung:**

$$g_m = \frac{0{,}947\ \mathrm{mA}}{25{,}85\ \mathrm{mV}} = 36{,}6\ \mathrm{mS}$$

Nach der Tangente ändert 1 mV den Strom um 36,6 µA oder 3,87 %, genau sind es +3,94 % und −3,79 %. Für ±10 mV liefert die Tangente ±38,7 %, genau +47,2 % und −32,1 %.

**Ergebnis:** **36,6 mS; die Tangente stimmt bei 1 mV auf 2 % genau, bei 10 mV liegt sie um 22 % daneben.**

**Einordnung:** Ein einziges Millivolt ändert den Strom um 4 %, denn die Spannungsskala der Exponentialfunktion ist $U_T$, 26 mV. Ein ohmscher Widerstand an 0,65 V änderte seinen Strom durch dasselbe Millivolt nur um 0,15 %.
::::

## Reale Kennlinien und Kleinsignal-Ersatzschaltbild

*Welche Widerstände zeigt der echte Transistor, und was bleibt von ihm für die Änderungen übrig?*

:::grafik
Szene: get1/bipolartransistoren/03-reale-kennlinien · Vorlage: kennlinie-ideal-real
**Abbildung 3:** Idealisierte und reale Kennlinien nach Skript Bild 11.19 und 11.20, mit den Werten des Beispieltransistors. (a) Eingangskennlinie, $I_B$ über $U_{BE}$: idealisiert senkrecht bei 0,6 V, real exponentiell; die Tangente im Arbeitspunkt (0,673 V; 4 µA) schneidet die Spannungsachse bei 0,647 V und hat die Steigung 1/(6,46 kΩ). (b) Ausgangskennlinien, $I_C$ über $U_{CE}$, für $I_B$ = 2, 4, 6 und 8 µA: idealisiert waagrecht ab 0,2 V, real leicht steigend; nach links verlängert treffen sich die realen Geraden bei −70 V. Im Arbeitspunkt 2 mA und 5 V beträgt die Steigung 1/(37,5 kΩ). Die realen Kennlinien haben endliche Steigungen; ihre Kehrwerte sind der Eingangs- und der Ausgangswiderstand.
:::

Die Arbeitspunkte im vorigen Artikel kamen mit idealisierten Kennlinien aus (Skript, S. 188–189): Die Eingangskennlinie steigt bei 0,6 V senkrecht an, das Skript sagt, der Eingangswiderstand $R_{BE}$ sei null; die Ausgangskennlinien verlaufen waagrecht, der Ausgangsleitwert $G_{CE}$ ist null. Real haben beide eine Steigung (Abbildung 3).

**Die Akteure:**

- __$r_{BE}$__: __differentieller Eingangswiderstand__, Änderung von $U_{BE}$ je Änderung des Basisstroms; 13,7 kΩ in der Stufe. Im Skript $R_{BE}$.
- __$r_{CE}$__: __differentieller Ausgangswiderstand__, Änderung von $U_{CE}$ je Änderung des Kollektorstroms bei festem Basisstrom; 79,6 kΩ in der Stufe. Im Skript sein Kehrwert $G_{CE}$.
- __$\beta$__: __Kleinsignal-Stromverstärkung__, Änderung des Kollektorstroms je Änderung des Basisstroms; im Modell gleich $B$, rund 500.
- __$U_A$__: __Early-Spannung__, bei der sich die verlängerten Ausgangskennlinien auf der negativen Achse treffen; 70 V.

**Das Zusammenspiel:** Der Basisstrom folgt derselben Exponentialfunktion wie der Kollektorstrom, ist aber 500-mal kleiner; dasselbe Millivolt ändert ihn deshalb nur um 73 nA statt 36,6 µA, und der Eingang wirkt wie 13,7 kΩ. Die Ausgangskennlinien steigen wegen des Early-Effekts: Mit wachsender $U_{CE}$ wird die neutrale Basis dünner, und durch sie diffundieren mehr Elektronen.

:::formel Formel
$$r_{BE} = \frac{\partial U_{BE}}{\partial I_B}\Big|_{U_{CE}\ \mathrm{fest}} = \frac{U_T}{I_B} = \frac{\beta}{g_m}$$
:::

**So liest man das:** $r_{BE}$ ist $\beta$-mal so groß wie $r_e$: Durch die Basis fließt nur der $\beta$-te Teil des Stroms, der auf dieselbe Spannungsänderung reagiert.

Idee der Herleitung: Ableiten des Basisstroms nach $U_{BE}$, wie bei der Steilheit.

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

**So liest man das:** Der Ausgangswiderstand ist der Abstand des Arbeitspunkts vom Schnittpunkt $-U_A$, geteilt durch den Strom: 37,5 kΩ bei 2 mA und 5 V. Ein typischer BC547C hat mit 60 µS Ausgangsleitwert (16,7 kΩ) einen stärkeren Early-Effekt als der Beispieltransistor.

Idee der Herleitung: Die Ausgangskennlinie ist eine Gerade durch $-U_A$; der Kehrwert ihrer Steigung ist Abstand durch Höhe.

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

Das Skript fasst beides im erweiterten Ersatzschaltbild zusammen (S. 189, Bild 11.21): am Eingang eine Spannungsquelle in Reihe mit $R_{BE}$, am Ausgang eine Stromquelle parallel zu $R_{CE}$. Die Werte nennt es nicht. Wählt man die Tangenten an die Kennlinien im Arbeitspunkt, sind es beim Beispieltransistor bei 2 mA am Eingang 0,647 V und 6,46 kΩ, am Ausgang eine Quelle mit dem 500-Fachen des Basisstroms abzüglich 0,133 mA und 37,5 kΩ (Abbildung 4a).

:::grafik
Szene: get1/bipolartransistoren/03-ersatzschaltbilder · Vorlage: schaltung-zustaende
**Abbildung 4:** Zwei Ersatzschaltbilder des npn-Transistors mit den Werten des Beispieltransistors bei 2 mA und 5 V. (a) Erweitertes Ersatzschaltbild nach Skript Bild 11.21: zwischen Basis und Emitter eine Spannungsquelle 0,647 V in Reihe mit $r_{BE}$ = 6,46 kΩ; zwischen Kollektor und Emitter eine gesteuerte Stromquelle, die das 500-Fache des Basisstroms abzüglich 0,133 mA liefert, parallel dazu $r_{CE}$ = 37,5 kΩ. (b) Kleinsignal-Ersatzschaltbild für die Änderungen: zwischen Basis und Emitter nur $r_{BE}$, zwischen Kollektor und Emitter die Stromquelle $g_m u_{be}$, gleichbedeutend mit $\beta i_b$, und $r_{CE}$. Für Änderungen fallen die festen Quellen weg; übrig bleiben der Eingangswiderstand, die gesteuerte Quelle und der Ausgangswiderstand.
:::

**Die Akteure:**

- __$i_b$__, __$u_{ce}$__: Änderungen des Basisstroms und der Kollektor-Emitter-Spannung.

Für die Änderungen braucht man die festen Anteile nicht. Nach dem Überlagerungsprinzip ([Das Superpositionsverfahren](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/superpositionsverfahren.html)) erfüllen die Ruhewerte ihre Gleichungen für sich, und für die Änderungen bleibt eine lineare Schaltung: das __Kleinsignal-Ersatzschaltbild__ (Abbildung 4b). Eine feste Spannungsquelle ändert sich nie und wirkt für Änderungen wie ein Kurzschluss; dasselbe gilt für die Versorgung und für große Kondensatoren, deren Spannung sich während einer Signalperiode kaum ändert. Die gesteuerte Quelle kann man als $g_m u_{be}$ oder als $\beta i_b$ schreiben, beides ist dasselbe; physikalisch steuert die Spannung $U_{BE}$, der Basisstrom ist die Folge.

:::formel Formel
$$i_b = \frac{u_{be}}{r_{BE}}, \qquad i_c = g_m\,u_{be} + \frac{u_{ce}}{r_{CE}} = \beta\,i_b + \frac{u_{ce}}{r_{CE}}$$
:::

**So liest man das:** Für Änderungen ist der Transistor ein Widerstand am Eingang und eine von $u_{be}$ gesteuerte Stromquelle mit parallelem Widerstand am Ausgang; in der Stufe 13,7 kΩ, 36,6 mS und 79,6 kΩ.

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

:::frage
„Warum ist $r_{BE}$ so groß? Vom Emitter aus hat derselbe Übergang doch nur 27 Ω.“
Beide Werte beschreiben dieselbe Barriere, gesehen von verschiedenen Strömen. Eine Änderung von $U_{BE}$ ändert alle Ströme über die Barriere um denselben Bruchteil. Am Emitter fließt der ganze Strom, seine Änderung ist groß und der Widerstand klein, 27 Ω; durch die Basis fließt nur der 500. Teil, der Widerstand ist 500-mal größer, 13,7 kΩ. Aus demselben Grund erscheint ein Widerstand im Emitterzweig, von der Basis aus gesehen, um den Faktor $\beta + 1$ vergrößert.
:::

## Die Spannungsverstärkung der Emitterschaltung

*Wie groß ist die Verstärkung einer Stufe, und wovon hängt sie ab?*

:::grafik
Szene: get1/bipolartransistoren/03-signalweg · Vorlage: schaltung-signalfluss
**Abbildung 5:** Kleinsignal-Ersatzschaltbild der Verstärkerstufe mit Emitterkondensator. Koppelkondensatoren, Emitterkondensator und Versorgung sind für Signale Kurzschlüsse; deshalb liegen die Teilerwiderstände 330 kΩ und 68 kΩ parallel zum Eingang und $R_C$ = 3,9 kΩ vom Kollektor nach Masse. Der Transistor ist durch $r_{BE}$ = 13,7 kΩ, die Stromquelle $g_m u_{be}$ mit 36,6 mS und $r_{CE}$ = 79,6 kΩ ersetzt. Eingetragen ist die Kette für 1 mV: 1 mV zwischen Basis und Emitter, 36,6 µA Kollektorstromänderung, −136 mV am Kollektor. Die Verstärkung ist die Steilheit mal dem Widerstand, in den die Stromänderung fließt.
:::

**Die Akteure:**

- __$C_1$__, __$C_2$__: __Koppelkondensatoren__ am Eingang und am Ausgang, je 1 µF; sie lassen Änderungen durch und halten die Gleichspannungen von Quelle und Last fern.
- __$C_E$__: __Emitterkondensator__ parallel zu $R_E$, 470 µF; er hält den Emitter für Signale fest, er __überbrückt__ $R_E$.
- __$R_1$__, __$R_2$__: Basisspannungsteiler, 330 kΩ und 68 kΩ.
- __$u_\mathrm{ein}$__, __$u_\mathrm{aus}$__, __$v_u$__: Signalspannungen am Eingang und am Ausgang und die __Spannungsverstärkung__, ihr Verhältnis; −136 in der Stufe.
- __$R_L$__: Lastwiderstand, etwa der Eingang der nächsten Stufe; 10 kΩ.
- __$r_\mathrm{ein}$__, __$r_\mathrm{aus}$__: __Eingangs-__ und __Ausgangswiderstand__ der Stufe; mit $r_\mathrm{ein}$ belastet sie die Quelle, mit $r_\mathrm{aus}$ wirkt sie auf die Last wie eine Quelle mit Innenwiderstand.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: $C_1$ und $C_2$ sperren den Gleichstrom; der Arbeitspunkt bleibt, die Basis auf 1,602 V, der Kollektor auf 6,306 V. $C_E$ hält den Emitter für Signale fest. Der Emitter ist damit der gemeinsame Anschluss: eine Emitterschaltung.

**Schritt 2**: Die Eingangsänderung erscheint vollständig als $u_{be}$; 1 mV ändert den Kollektorstrom um 36,6 µA.

**Schritt 3**: Die Stromänderung fließt durch $R_C$ zur Versorgung, die für Signale an Masse liegt. Mehr Strom heißt mehr Spannungsabfall an $R_C$ und ein tieferes Kollektorpotenzial: Das Signal wird umgekehrt.

**Schritt 4**: Am Kollektor entstehen 36,6 µA mal $R_C$ parallel $r_{CE}$, 3,72 kΩ, also −136 mV (Abbildung 5). $B$ kommt in dieser Kette nicht vor.

:::formel Formel
$$v_u = \frac{u_\mathrm{aus}}{u_\mathrm{ein}} = -g_m\,(R_C \parallel r_{CE} \parallel R_L) \approx -g_m\,R_C = -\frac{U_{RC}}{U_T}$$

$$r_\mathrm{ein} = R_1 \parallel R_2 \parallel r_{BE}$$

$$r_\mathrm{aus} = R_C \parallel r_{CE}$$
:::

**So liest man das:** $\parallel$ steht für die Parallelschaltung, $U_{RC}$ für die Ruhespannung an $R_C$. Ohne $r_{CE}$ und Last hängt die Verstärkung nur von dieser Ruhespannung ab: 3,694 V durch 25,85 mV ergibt −142,9; mit $r_{CE}$ sind es −136,2, mit 10 kΩ Last −99,3. Mit einem ohmschen Kollektorwiderstand kann eine Stufe an 10 V deshalb höchstens rund das 387-Fache erreichen.

Idee der Herleitung: Kleinsignal-Ersatzschaltbild einsetzen, Versorgung und Kondensatoren kurzschließen, Knotenregel am Kollektor.

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
**Gegeben:** Stufe aus dem vorigen Artikel mit $C_E$; Arbeitspunkt 0,947 mA; 36,6 mS, $r_{BE}$ = 13,7 kΩ, $r_{CE}$ = 79,6 kΩ, $R_C$ = 3,9 kΩ, Teiler 56,4 kΩ; Last 10 kΩ.

**Gesucht:** Verstärkung ohne und mit Last, Eingangs- und Ausgangswiderstand.

**Rechnung:**

$$v_u = -36{,}6\ \mathrm{mS}\cdot(3{,}9\ \mathrm{k\Omega} \parallel 79{,}6\ \mathrm{k\Omega}) = -36{,}6\ \mathrm{mS}\cdot3{,}72\ \mathrm{k\Omega} = -136$$

Mit 10 kΩ Last liegen 2,71 kΩ am Kollektor, die Verstärkung ist −99,3.

$$r_\mathrm{ein} = 56{,}4\ \mathrm{k\Omega} \parallel 13{,}7\ \mathrm{k\Omega} = 11{,}0\ \mathrm{k\Omega}, \qquad r_\mathrm{aus} = 3{,}72\ \mathrm{k\Omega}$$

**Ergebnis:** **$v_u$ = −136 ohne, −99,3 mit 10 kΩ Last; $r_\mathrm{ein}$ = 11,0 kΩ, $r_\mathrm{aus}$ = 3,72 kΩ.**

**Einordnung:** Die Last nimmt ein Viertel der Verstärkung, weil sie mit dem Ausgangswiderstand einen Spannungsteiler bildet.
::::

:::fehlvorstellung
„Die Spannungsverstärkung ist $B$.“
Das liegt nahe, weil $B$ die bekannteste Kennzahl des Transistors ist. Die Spannungsverstärkung entsteht aber aus Steilheit und Kollektorwiderstand; $B$ bestimmt nur den Basisstrom und damit den Eingangswiderstand. Exemplare mit $B$ = 420 und 800 verstärken in der Stufe −133,8- und −141,2-fach, nur weil ihr Ruhestrom um −1,9 bzw. +3,9 % abweicht.
:::

:::frage
„Woher kommt die Leistung des verstärkten Signals?“
Aus der Versorgung; der Transistor steuert nur, wie viel Strom sie durch $R_C$ schickt. Die Stufe nimmt 9,73 mW auf. Ein Signal von 1 mV gibt am Eingang 45 pW ab, an 10 kΩ Last kommen 493 nW an, rund das 10 900-Fache; der Rest der aufgenommenen Leistung wird zu Wärme.
:::

Wie groß das Signal sein darf, entscheidet die Verzerrung. Eine verzerrte Schwingung enthält außer der __Grundschwingung__ mit der Signalfrequenz __Oberschwingungen__ mit doppelter, dreifacher Frequenz. Der __Klirrfaktor__ fasst sie zusammen; hier überwiegt die Oberschwingung mit doppelter Frequenz, und ihr Anteil, ihre Amplitude geteilt durch die der Grundschwingung, heißt $k_2$.

:::formel Formel
$$k_2 \approx \frac{\hat u_{be}}{4\,U_T}$$
:::

**So liest man das:** $\hat u_{be}$ ist die Amplitude der Änderung zwischen Basis und Emitter. Der Klirrfaktor wächst proportional zu ihr, rund 1 % bei 1 mV und 10 % bei 10 mV, für jeden Bipolartransistor gleich. Das vollständige Modell der Stufe ergibt 0,9 % und 8,7 %; bei 10 mV sinkt das Kollektorpotenzial um 1,63 V, steigt aber nur um 1,15 V.

Idee der Herleitung: Man entwickelt die Exponentialfunktion bis zum quadratischen Glied und zerlegt das Quadrat des Sinus.

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

:::fehlvorstellung
„Kleinsignal heißt, dass auch das Ausgangssignal klein ist.“
Das liegt nahe, weil das Wort nach kleinen Spannungen überall klingt. Klein sein muss die Änderung, die die Kennlinie steuert, $u_{be}$ gegen $U_T$. Aus 1 mV am Eingang werden 136 mV am Ausgang bei 0,9 % Klirrfaktor. Wie groß der Ausgang werden darf, hängt von der Verstärkung ab: Mit Emitterkondensator erlaubt 1 % Klirrfaktor nur 0,155 V, mit Gegenkopplung über $R_E$ bleibt es bei 1 V Ausgang bei 0,18 %.
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

**Schritt 1**: Ohne $C_E$ liegt der Emitter nur über $R_E$ an Masse; jede Änderung des Emitterstroms ändert das Emitterpotenzial um das $R_E$-Fache.

**Schritt 2**: Hebt das Signal die Basis, steigt der Strom und mit ihm das Emitterpotenzial; zwischen Basis und Emitter bleibt nur ein Rest. Das ist die Stromgegenkopplung aus dem vorigen Artikel, jetzt für das Signal.

**Schritt 3**: Der Rest ist klein, denn für eine Stromänderung braucht der Transistor nur das $r_e$-Fache an Spannung, 27,3 Ω gegen 1 kΩ. Fast die ganze Eingangsänderung liegt an $R_E$, die Stromänderung ist die Eingangsänderung geteilt durch $R_E + r_e$.

**Schritt 4**: Diese Stromänderung fließt durch $R_C$; die Verstärkung ist rund −3,8, ein Verhältnis zweier Widerstände. Steilheit, $B$ und Temperatur stecken nur noch im kleinen $r_e$.

**Schritt 5**: Der Preis: Die Verstärkung sinkt um den Faktor 36. Gewonnen ist Linearität, weil die gekrümmte Kennlinie nur noch $u_{be}$ bestimmt, ein 37,6stel der Eingangsspannung, und der Rest am linearen $R_E$ abfällt: bei 1 V Ausgang 0,18 % Klirrfaktor statt 6,4 % (Abbildung 6b). Gewonnen sind auch Unabhängigkeit vom Exemplar und ein Eingangswiderstand des Transistors von 517 kΩ statt 13,7 kΩ.

:::formel Formel
$$v_u = -\frac{\beta\,R_C}{r_{BE} + (\beta + 1)\,R_E} \approx -\frac{R_C}{R_E + r_e}$$

$$r_{\mathrm{ein},T} = r_{BE} + (\beta + 1)\,R_E$$
:::

**So liest man das:** $r_{\mathrm{ein},T}$ ist der Eingangswiderstand des Transistors ohne Teiler. Vom Eingang aus erscheint $R_E$ um $\beta + 1$ vergrößert, weil durch ihn der ganze Emitterstrom fließt. In der Praxis lässt man nur einen Teil von $R_E$ im Signalweg und überbrückt den Rest; so stellt man die Verstärkung ein, ohne den Arbeitspunkt zu ändern.

Idee der Herleitung: Kleinsignal-Ersatzschaltbild mit $R_E$ im Emitterzweig, einmal um den Eingangskreis.

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

**Gesucht:** Verstärkung und Eingangswiderstand der Stufe.

**Rechnung:**

$$v_u = -\frac{502{,}4\cdot3{,}9\ \mathrm{k\Omega}}{13{,}71\ \mathrm{k\Omega} + 503{,}4\cdot1\ \mathrm{k\Omega}} = -3{,}79, \qquad r_\mathrm{ein} = 56{,}4\ \mathrm{k\Omega} \parallel 517\ \mathrm{k\Omega} = 50{,}8\ \mathrm{k\Omega}$$

**Ergebnis:** **$v_u$ = −3,79 (vollständiges Modell −3,78), $r_\mathrm{ein}$ = 50,8 kΩ.**

**Einordnung:** Exemplare mit $B$ = 420 und 800 verstärken jetzt −3,786- und −3,796-fach. Bleiben nur 100 Ω von $R_E$ im Signalweg, sind es −30,6 bei unverändertem Arbeitspunkt.
::::

## Die Grundschaltungen für kleine Signale

*Wie verhalten sich Emitter-, Kollektor- und Basisschaltung für kleine Signale?*

:::grafik
Szene: get1/bipolartransistoren/03-grundschaltungen-kleinsignal · Vorlage: schaltung-zustaende
**Abbildung 7:** Kleinsignal-Ersatzschaltbilder der drei Grundschaltungen beim selben Ruhestrom 0,947 mA (36,6 mS, $r_{BE}$ = 13,7 kΩ, $\beta$ = 502) mit je 3,9 kΩ am Ausgang. (a) Emitterschaltung: Eingang an der Basis, Emitter an Masse, Ausgang am Kollektor. (b) Kollektorschaltung: Eingang an der Basis, Kollektor über die Versorgung an Masse, Ausgang am Emitter mit 3,9 kΩ. (c) Basisschaltung: Basis an Masse, Eingang am Emitter, Ausgang am Kollektor. Zu jeder Schaltung Verstärkung, Eingangs- und Ausgangswiderstand. Welcher Anschluss gemeinsam ist, bestimmt, wie Spannung, Strom und Widerstände übertragen werden.
:::

Mit dem Kleinsignal-Ersatzschaltbild erhält jede der drei Grundschaltungen aus dem vorigen Artikel ihre Verstärkung, ihren Eingangs- und ihren Ausgangswiderstand. Abbildung 7 und die Tabelle vergleichen sie beim selben Ruhestrom.

| Grundschaltung | Kleinsignalverhalten bei 0,947 mA und 3,9 kΩ |
|---|---|
| Emitterschaltung | Verstärkung −136, kehrt um; Eingangswiderstand 13,7 kΩ; Ausgangswiderstand 3,72 kΩ |
| Kollektorschaltung (Emitterfolger) | Verstärkung 0,993; Eingangswiderstand 1,88 MΩ; Ausgangswiderstand 27,3 Ω plus Quellwiderstand durch 503 |
| Basisschaltung | Verstärkung +136, kehrt nicht um; Eingangswiderstand 27,2 Ω; Ausgangswiderstand 3,72 kΩ |

Die Kollektorschaltung verstärkt die Spannung nicht, sie wandelt Widerstände: Am Eingang erscheint der Emitterwiderstand um $\beta + 1$ vergrößert, am Ausgang der Innenwiderstand der Quelle um $\beta + 1$ verkleinert, aus 10 kΩ werden 20 Ω. Als __Impedanzwandler__ lässt sie eine hochohmige Quelle eine niederohmige Last treiben. Die Basisschaltung verstärkt wie die Emitterschaltung, aber ohne Umkehr, und hat einen sehr kleinen Eingangswiderstand, weil die Quelle den ganzen Emitterstrom liefern muss.

## Spannungsstabilisierung mit Z-Diode und Transistor

*Wie hält ein Transistor eine Ausgangsspannung fest, obwohl die Eingangsspannung schwankt und die Last Strom zieht?*

:::grafik
Szene: get1/bipolartransistoren/03-stabilisierung · Vorlage: schaltung-und-zeitverlauf
**Abbildung 8:** (a) Spannungsstabilisierung nach Skript Bild 11.28 mit den Werten des Beispiels: Eingangsspannung 12 V mit ±1 V Brummen, $R_1$ = 1 kΩ von der Eingangsspannung zur Basis, Z-Diode 5,6 V von der Basis nach Masse, Kollektor an der Eingangsspannung, Ausgang am Emitter mit 200 Ω Last. (b) Zwei gestapelte Zeitverläufe: oben die Eingangsspannung zwischen 11 und 13 V; unten die Ausgangsspannung zwischen 4,870 und 4,910 V, dazu gestrichelt die Z-Diode allein mit 330 Ω Vorwiderstand an derselben Last, die zwischen 4,15 und 4,91 V dem Eingang folgt. Der Transistor gibt die Spannung der Z-Diode, um $U_{BE}$ vermindert, an die Last weiter; das Brummen wird 50-mal kleiner.
:::

Hinter einem Brückengleichrichter schwankt die Spannung mit 100 Hz, dem Takt der gleichgerichteten Halbwellen; das ist das __Brummen__. Eine Z-Diode mit Vorwiderstand glättet es nur bei kleinem Laststrom ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html), Abschnitt *Die Z-Diode*); an 200 Ω sperrt sie, und der Ausgang folgt dem Eingang. Das Skript setzt deshalb einen Transistor dazwischen (S. 192–193, Bild 11.28; Abbildung 8).

**Die Akteure:**

- __$U_\mathrm{ein}$__, __$U_\mathrm{aus}$__: Eingangsspannung, 12 V mit ±1 V Brummen, und stabilisierte Ausgangsspannung am Emitter; im Skript $U_E$ und $U_A$.
- __$R_1$__: Vorwiderstand für Z-Diode und Basis; 1 kΩ.
- __$U_Z$__, __$r_Z$__: Spannung der Z-Diode, 5,6 V bei 5 mA, und ihr differentieller Widerstand, 20 Ω.
- __$R_L$__: Last; 200 Ω, entsprechend 24,5 mA.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: $R_1$ und die Z-Diode halten die Basis auf 5,63 V.

**Schritt 2**: Der Transistor arbeitet als Emitterfolger; sein Emitter liegt um $U_{BE}$ tiefer, 0,737 V bei 24,5 mA, also auf 4,890 V.

**Schritt 3**: Der Laststrom fließt vom Eingang durch Kollektor und Emitter; über die Basis fließt nur sein 500. Teil, 48 µA, und nur den muss $R_1$ außer dem Z-Strom liefern. Deshalb darf $R_1$ dreimal so groß sein wie der Vorwiderstand der Z-Diode allein.

**Schritt 4**: Der Transistor nimmt die Differenz zwischen Ein- und Ausgang auf, 7,1 V, und setzt 174 mW in Wärme um; weil er in Reihe zur Last liegt, heißt die Schaltung __Längsregler__.

**Schritt 5**: Ein Volt mehr am Eingang treibt rund 1 mA mehr durch $R_1$; die Spannung der Z-Diode steigt dabei nur um 20 mV, und der Emitterfolger gibt das weiter. Aus 2 V Brummen werden 39,7 mV.

:::formel Formel
$$U_\mathrm{aus} = U_Z - U_{BE}$$
:::

**So liest man das:** Der Ausgang liegt um die Basis-Emitter-Spannung unter der Z-Spannung, 5,627 V − 0,737 V = 4,890 V. Das Skript schreibt $U_A = U_Z + U_{BE}$ (S. 193); nach den Zählpfeilen von Bild 11.28 ergibt die Masche aber ein Minus. Mit dem Plus wären es 6,36 V, mehr als die 5,63 V an der Basis, und so hoch kann der Emitter eines leitenden npn-Transistors nicht liegen.

Idee der Herleitung: Maschenregel von Masse über die Z-Diode, die Basis-Emitter-Strecke und den Ausgang.

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

**So liest man das:** Der __Glättungsfaktor__ $G$ ist das Verhältnis der Schwankungen. Er wächst mit $R_1$, und ein großes $R_1$ erlaubt erst der Transistor: 1 + 1 kΩ/20 Ω = 51, genau gerechnet 50,4.

Idee der Herleitung: $R_1$ und $r_Z$ teilen die Brummänderung, der Emitterfolger gibt sie fast unverändert weiter.

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
**Gegeben:** Eingangsspannung 11 bis 13 V; $R_1$ = 1 kΩ; Z-Diode 5,6 V bei 5 mA mit $r_Z$ = 20 Ω; Beispieltransistor; Last 200 Ω.

**Gesucht:** Ausgangsspannung, Brummen am Ausgang, Verlustleistung des Transistors.

**Rechnung:** Bei 12 V liefert das vollständige Modell 5,627 V an der Z-Diode und 0,737 V zwischen Basis und Emitter:

$$U_\mathrm{aus} = 5{,}627\ \mathrm{V} - 0{,}737\ \mathrm{V} = 4{,}890\ \mathrm{V}$$

Bei 11 V sind es 4,870 V, bei 13 V 4,910 V, also 39,7 mV Brummen und $G$ = 50,4. Verlustleistung bei 12 V:

$$P = (12\ \mathrm{V} - 4{,}89\ \mathrm{V})\cdot24{,}4\ \mathrm{mA} = 174\ \mathrm{mW}$$

**Ergebnis:** **4,890 V am Ausgang, 39,7 mV Brummen statt 2 V; der Transistor setzt 149 bis 198 mW um.**

**Einordnung:** Die Z-Diode allein liefert an derselben Last nur 4,15 bis 4,91 V und stabilisiert nicht. Der Längsregler arbeitet, solange die Z-Diode im Durchbruch bleibt: Für 1 mA Z-Strom muss die Eingangsspannung mindestens 6,57 V betragen; die Bedingung des Skripts, $U_E$ größer als $U_Z$, reicht dafür nicht.
::::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Steilheit und Verzerrung | Eine kleine Änderung von $U_{BE}$ ändert den Strom um denselben Bruchteil; gleichmäßig nur, solange sie klein gegen $U_T$ bleibt. |
| Ersatz­schaltbilder | Für Änderungen zählen nur Steigungen: Eingangs­widerstand, Steilheit, Ausgangs­widerstand. |
| Spannungs­verstärkung | Der Kollektor­widerstand verwandelt die Stromänderung zurück in eine Spannung; $B$ kommt nicht vor. |
| Emitter­widerstand | Die gekrümmte Kennlinie bestimmt nur noch einen kleinen Teil der Eingangsspannung: weniger Verstärkung, dafür linear und unabhängig vom Transistor. |
| Grund­schaltungen und Längsregler | Der gemeinsame Anschluss entscheidet, ob die Steilheit Spannung verstärkt oder als Emitterfolger Widerstände wandelt und Strom liefert. |

Ein Transistor verstärkt, weil eine kleine Änderung der Basis-Emitter-Spannung den Kollektorstrom mit der Steilheit $I_C/U_T$ ändert und ein Widerstand diese Stromänderung in eine große Spannungsänderung verwandelt; gleichmäßig gelingt das nur für Änderungen, die klein gegen $U_T$ sind, und ein Emitterwiderstand tauscht Verstärkung gegen Linearität und Unabhängigkeit vom Transistor.

## Bedeutung und Ausblick

Die Emitterschaltung mit Emitterwiderstand im Signalweg ist die Grundform diskreter Vorverstärker; im Audioverstärker des Praktikums arbeitet der BC547C so, mit einem kleinen, nicht überbrückten Emitterwiderstand. Längsregler stecken in vielen Netzteilen. Wie sich mit vielen solchen Stufen und Gegenkopplung ein nahezu idealer Verstärker bauen lässt, zeigt [Der Operationsverstärker – idealer OPV und Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html).

**In der ausführlichen Fassung:** das erweiterte Ersatzschaltbild mit hergeleiteten Werten und seiner Gültigkeit, der Datenblattvergleich mit den h-Parametern des BC547C, die Größe der Kondensatoren und die untere Grenzfrequenz, die Kollektor- und Basisschaltung mit Herleitungen und einem Impedanzwandler-Beispiel, das Lastverhalten des Längsreglers und seine kleinste Eingangsspannung. [Zur ausführlichen Fassung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker-ausfuehrlich.html)

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
A: Der Kollektorstrom wächst exponentiell mit $U_{BE}$; eine Änderung multipliziert ihn mit einem Faktor, der nur von $u_{be}/U_T$ abhängt. Proportional ist die Stromänderung nur für $u_{be}$ klein gegen $U_T$; 10 mV heben den Strom um 47 %, senken ihn aber nur um 32 %.
F: Wie groß ist die Steilheit bei 0,947 mA, und welche Kollektorstromänderung bewirkt 1 mV?
A: 0,947 mA durch 25,85 mV ergibt 36,6 mS; 1 mV ändert den Kollektorstrom um 36,6 µA.
F: Warum hängt die Spannungsverstärkung der Emitterschaltung nicht von $B$ ab?
A: Die Eingangsspannung setzt über die Steilheit direkt den Kollektorstrom, und $R_C$ verwandelt dessen Änderung zurück in eine Spannung: $v_u$ ist etwa $-g_m R_C$, also $-U_{RC}/U_T$. $B$ bestimmt nur den Basisstrom und damit den Eingangswiderstand.
F: Stimmt es, dass die Spannungsverstärkung gleich $B$ ist?
A: Nein. Die Stufe verstärkt −136-fach bei $B$ = 500; Exemplare mit 420 und 800 liefern −133,8 und −141,2, nur weil sich ihr Ruhestrom um −1,9 bzw. +3,9 % verschiebt.
F: Warum macht ein Emitterwiderstand im Signalweg die Verstärkung fast unabhängig vom Transistor?
A: Ohne Emitterkondensator folgt der Emitter der Basis; fast die ganze Eingangsänderung liegt an $R_E$. Die Stromänderung ist die Eingangsänderung durch $R_E + r_e$, die Verstärkung etwa $-R_C/(R_E + r_e)$, also −3,8; Exemplare mit $B$ = 420 und 800 liefern −3,786 und −3,796.
F: Stimmt es, dass bei Kleinsignalen auch das Ausgangssignal klein sein muss?
A: Nein. Klein sein muss $u_{be}$ gegen $U_T$; der Ausgang ist um die Verstärkung größer, aus 1 mV werden 136 mV. Wie groß er sein darf, hängt von der Verstärkung ab: mit Emitterkondensator 0,155 V bei 1 % Klirrfaktor, mit Gegenkopplung über $R_E$ 1 V bei 0,18 %.
:::
