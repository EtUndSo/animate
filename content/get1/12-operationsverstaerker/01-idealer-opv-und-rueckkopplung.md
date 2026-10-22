---
title: Der Operationsverstärker – idealer OPV und Rückkopplung
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Operationsverstärker
order: 120100
summary: Was ein Operationsverstärker ist, wie sein Differenzverstärker nur den Unterschied zweier Spannungen verstärkt und warum erst die Rückkopplung aus der riesigen Verstärkung eine berechenbare Schaltung macht: Rauschen, Differenzverstärker, idealer OPV und Komparator, Gegen- und Mitkopplung, Schmitt-Trigger. Kompakte Fassung; die ausführliche enthält zusätzlich Schrot- und 1/f-Rauschen mit Formeln, eine Messkette mit Vorverstärker, die Gleichtaktunterdrückung, den Flash-Wandler im Einzelnen, die Frequenzkompensation und weitere Beispiele.
tags: Operationsverstärker, OPV, idealer OPV, Differenzverstärker, virtueller Kurzschluss, Gegenkopplung
stil: 3
fassung: kompakt
---

## Worum es geht

Sensoren liefern oft nur Millivolt, überlagert von Störungen. Der __Operationsverstärker__, kurz OPV, ist eine integrierte Schaltung aus vielen Transistoren mit zwei Eingängen und einem Ausgang, die solche Spannungen verstärkt, vergleicht und miteinander verrechnet, und zwar genau, obwohl die Kennwerte ihrer Transistoren streuen. Nach diesen Rechenoperationen ist sie benannt.

**Ein Operationsverstärker verstärkt nur die Differenz seiner beiden Eingangsspannungen, und das so stark, dass er allein nur „größer“ oder „kleiner“ melden kann; erst die Rückführung der Ausgangsspannung macht ihn brauchbar: Wirkt sie der Differenz entgegen (Gegenkopplung), regelt der Ausgang die Differenz praktisch auf null, und die äußeren Widerstände bestimmen das Ergebnis; verstärkt sie die Differenz (Mitkopplung), kippt der Ausgang an eine Grenze und bleibt dort.**

Vorausgesetzt werden die Transfergleichung des Bipolartransistors aus [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html), die Steilheit aus [Der Transistor als Verstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker.html), der Stromspiegel aus [Arbeitspunkt und Grundschaltungen des Transistors](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/arbeitspunkt-und-grundschaltungen.html), der Spannungsteiler aus [Zusammenschaltung von Widerständen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/zusammenschaltung-von-widerstaenden.html) und das Laden eines Kondensators aus [Laden und Entladen des Kondensators](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/laden-und-entladen.html). Darauf bauen [Die OPV-Grundschaltungen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/opv-grundschaltungen.html) und [Der reale Operationsverstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/realer-operationsverstaerker.html) auf.

:::grafik
Szene: get1/operationsverstaerker/01-opv-kennlinie · Vorlage: schaltung-und-kennlinie
**Abbildung 1:** (a) Schaltsymbol des Operationsverstärkers: links der nichtinvertierende Eingang (+) und der invertierende Eingang (−), dazwischen der Zählpfeil der Differenzspannung $U_D$ vom Plus- zum Minuseingang; rechts der Ausgang mit $U_A$ gegen Masse; oben und unten die Versorgung +15 V und −15 V. (b) Übertragungskennlinie des Beispiel-OPV (Art 741), $U_A$ über $U_D$ von −200 µV bis +200 µV: zwischen −70 µV und +70 µV eine Gerade mit der Steigung 200 000, außerhalb waagrecht bei +14 V bzw. −14 V; gestrichelt die Versorgung ±15 V. Proportional zur Differenz ist der Ausgang nur in einem Fenster von ±70 µV; außerhalb meldet er nur ihr Vorzeichen.
:::

## Rauschen und Signal-Rausch-Verhältnis

*Wie beschreibt man eine Störspannung, deren Verlauf sich nicht vorhersagen lässt, und woher kommt sie?*

:::grafik
Szene: get1/operationsverstaerker/01-rauschen · Vorlage: zeitverlauf-und-spektrum
**Abbildung 2:** (a) Rauschspannung eines 10-kΩ-Widerstands bei 300 K über 20 µs, gemessen mit 1 MHz Bandbreite: ein unregelmäßiges Zittern um null; waagrechte Linien bei ±12,9 µV, dem Effektivwert. (b) Rauschdichte in nV/√Hz über der Frequenz von 0,1 Hz bis 1 MHz, beide Achsen logarithmisch: beim Widerstand waagrecht bei 12,9 nV/√Hz; beim Beispiel-OPV waagrecht bei 23 nV/√Hz und unterhalb der Eckfrequenz 100 Hz ansteigend, bei 10 Hz auf 76 nV/√Hz, bei 1 Hz auf 231 nV/√Hz. Den Verlauf des Rauschens kann man nicht vorhersagen, seine Größe aber genau angeben: als Effektivwert und als Dichte über der Frequenz.
:::

Jeder Widerstand und jeder Transistor erzeugt an seinen Anschlüssen eine kleine, zufällig schwankende Spannung, auch ohne Strom von außen: das __Rauschen__. Man kann es sich als Überlagerung sehr vieler Sinusschwingungen mit zufälligen Amplituden und Phasen vorstellen. Sein Verlauf ist nicht vorhersagbar, ein __Zufallsprozess__ (Abbildung 2a), und sein Mittelwert ist null. Man misst es deshalb mit dem __Effektivwert__, der Wurzel aus dem zeitlichen Mittelwert des Quadrats (Querstrich); er ist die Gleichspannung, die an einem Widerstand im Mittel dieselbe Leistung umsetzt:

$$U_\mathrm{eff} = \sqrt{\overline{u^2}}$$

**Die Akteure:**

- __$U_r$__: Effektivwert der Rauschspannung $u_r(t)$, im Skript $u_{r,\mathrm{eff}}$; bei einem 10-kΩ-Widerstand und 1 MHz Bandbreite 12,9 µV.
- __$|u_r(f)|^2$__: __spektrale Rauschdichte__, der Anteil am mittleren Quadrat der Rauschspannung je Hertz Bandbreite bei der Frequenz $f$; in V²/Hz. Datenblätter geben ihre Wurzel in nV/√Hz an, beim 10-kΩ-Widerstand 12,9 nV/√Hz. Im Skript heißt sie Rauschspannungsdichte.

**Das Zusammenspiel:** Sinusschwingungen verschiedener Frequenz tragen zum mittleren Quadrat unabhängig voneinander bei; ihre Beiträge addieren sich. Deshalb verteilt man das mittlere Quadrat als Dichte über die Frequenz und gewinnt den Effektivwert durch Aufsummieren zurück (Skript S. 195, Gleichung 12.1):

:::formel Definition
$$U_r = \sqrt{\int_0^\infty |u_r(f)|^2\,df}$$
:::

**So liest man das:** Bei konstanter Dichte wächst der Effektivwert mit der Wurzel der Bandbreite: Ein 10-kΩ-Widerstand rauscht im Hörbereich bis 20 kHz mit 1,82 µV, über 1 MHz mit 12,9 µV. Aus demselben Grund addieren sich unabhängige Rauschquellen quadratisch: 23 nV/√Hz eines OPV und 12,9 nV/√Hz einer Quelle ergeben 26,4 nV/√Hz.

Idee der Herleitung: Man quadriert eine Summe von Sinusschwingungen; alle Mischprodukte verschiedener Frequenzen mitteln sich zu null.

:::herleitung
**Ausgangspunkt:** die Definition des Effektivwerts über das mittlere Quadrat und die Vorstellung des Rauschens als Summe von Sinusschwingungen (Skript S. 195).

**Annahmen:** (i) Das Rauschen ist eine Summe von Sinusschwingungen mit verschiedenen Frequenzen $f_i$, Amplituden $\hat u_i$ und Phasen $\phi_i$. (ii) Die Mittelungszeit $T_m$ ist lang gegen alle Perioden, auch gegen die Kehrwerte der Frequenzabstände.

**Schritt 1**: Rauschspannung als Summe, mit der Abkürzung $\alpha_i$ für das Argument $2\pi f_i t + \phi_i$:

$$u_r(t) = \sum_i \hat u_i \cos\alpha_i$$

**Schritt 2**: Beim Quadrieren entstehen die Quadrate der einzelnen Glieder und Mischprodukte je zweier verschiedener Glieder:

$$u_r^2 = \sum_i \hat u_i^2 \cos^2\alpha_i + \sum_{i \ne j} \hat u_i\,\hat u_j \cos\alpha_i \cos\alpha_j$$

**Schritt 3** (entscheidender Schritt): Ein Produkt zweier Kosinus ist die halbe Summe aus dem Kosinus der Summe und dem Kosinus der Differenz der Argumente:

$$\cos\alpha_i\,\cos\alpha_j = \tfrac{1}{2}\cos(\alpha_i + \alpha_j) + \tfrac{1}{2}\cos(\alpha_i - \alpha_j)$$

Für $i \ne j$ schwingen beide Glieder, mit den Frequenzen $f_i + f_j$ und $f_i - f_j$, und mitteln sich über lange Zeit zu null. Für gleiche Indizes ist das zweite Glied konstant 1/2; das Quadrat eines Kosinus hat deshalb den Mittelwert 1/2.

**Schritt 4**: Übrig bleiben die mittleren Quadrate der einzelnen Komponenten:

$$\overline{u_r^2} = \sum_i \frac{\hat u_i^2}{2}$$

**Schritt 5**: Fasst man die Beiträge aller Komponenten in einem schmalen Frequenzband $df$ zu $|u_r(f)|^2\,df$ zusammen, wird die Summe zum Integral über die Frequenz. Die Wurzel ergibt den Effektivwert.

**Ergebnis:**

$$U_r = \sqrt{\int_0^\infty |u_r(f)|^2\,df}$$

**Woher die Faktoren kommen:** Die Wurzel stammt aus der Definition des Effektivwerts, das Integral aus der Summe der Beiträge. Mischterme gibt es nicht, weil sich Sinusschwingungen verschiedener Frequenz im Mittel nicht beeinflussen.

**Proben:** Einheit: Die Wurzel aus V²/Hz mal Hz ist V. Zahlenwert: 12,87 nV/√Hz mal der Wurzel aus 10⁶ Hz ergibt 12,9 µV. Spezialfall: Zwei Sinusschwingungen mit je 1 V Amplitude bei 50 Hz und 150 Hz haben zusammen den Effektivwert 1,000 V, die Wurzel aus 0,5 V² + 0,5 V²; die Summe der einzelnen Effektivwerte, 1,414 V, wäre falsch.

**Grenzen:** Das Integral ist nur endlich, wenn die Dichte zu hohen Frequenzen schneller als 1/f abfällt und zu tiefen Frequenzen nicht wie 1/f anwächst. Nach oben begrenzen in realen Schaltungen die Kapazitäten die Bandbreite, nach unten die Messdauer.
:::

Ob Rauschen stört, sagt das __Signal-Rausch-Verhältnis__ (englisch signal-to-noise ratio, SNR), das Verhältnis der Leistungen von Signal und Rauschen am selben Widerstand. Mit dem Effektivwert __$U_S$__ des Signals, meist in __Dezibel__ (dB) angegeben:

:::formel Definition
$$\mathrm{SNR} = \frac{U_S^2}{U_r^2}$$
$$\mathrm{SNR}_\mathrm{dB} = 10\,\lg\frac{U_S^2}{U_r^2}$$
:::

**So liest man das:** Je größer das Verhältnis, desto weniger fällt das Rauschen auf. Ein Faktor 10 in der Spannung sind 20 dB, weil das Verhältnis die Quadrate enthält. Ein Signal von 1 mV liegt 54,8 dB über dem Rauschen eines 10-kΩ-Widerstands im Hörbereich.

:::fehlvorstellung
„Wenn man das Nutzsignal verstärkt, wird das Signal-Rausch-Verhältnis besser.“ So steht es im Skript (S. 195). Ein Verstärker hebt aber das Rauschen, das schon im Signal steckt, um denselben Faktor an und fügt eigenes hinzu: Ein Sensor mit 1 mV und 10 kΩ hat im Hörbereich 54,8 dB, hinter einem OPV mit 23 nV/√Hz bleiben 48,6 dB. Verstärkung schützt nur gegen Rauschen, das erst danach hinzukommt, etwa aus einer Folgestufe; besser wird das Verhältnis außerdem, wenn man die Bandbreite auf die des Signals begrenzt.
:::

Die wichtigste Quelle ist das __thermische Rauschen__. Die Leitungselektronen eines Widerstands bewegen sich ungeordnet; in jedem Augenblick überwiegt zufällig eine Richtung, und dieser schwankende Nettostrom erzeugt eine schwankende Spannung an den Klemmen.

**Die Akteure:**

- __$k_B$__: Boltzmann-Konstante, 1,380649·10⁻²³ J/K, im Skript $k$. Sie rechnet eine Temperatur in eine Energie um; im thermischen Gleichgewicht trägt jeder Energieterm, der quadratisch von einer Größe abhängt, im Mittel $k_B T/2$ (__Gleichverteilungssatz__ der kinetischen Gastheorie).
- __$T$__: absolute Temperatur, 300 K; sie treibt die ungeordnete Bewegung.
- __$R$__: Widerstandswert.

:::formel Gesetz
$$|u_{r,R}(f)|^2 = 4\,k_B\,T\,R$$
:::

**So liest man das:** Die Dichte ist proportional zu Temperatur und Widerstand und hängt nicht von der Frequenz ab; die Rauschspannung wächst mit der Wurzel: 4,07 nV/√Hz bei 1 kΩ, 12,9 nV/√Hz bei 10 kΩ, 129 nV/√Hz bei 1 MΩ. Woran die Elektronen stoßen, bestimmt nur den Wert von $R$; bei gegebenem $R$ zählt allein die Temperatur. Zufällig ist die Wärmebewegung, nicht die ortsfesten Gitterfehler, die das Skript für die Unvorhersagbarkeit mitverantwortlich macht (S. 195).

Idee der Herleitung: Man schließt einen Kondensator an den Widerstand an; im thermischen Gleichgewicht muss seine Energie im Mittel $k_B T/2$ betragen, und daraus folgt, wie stark der Widerstand rauschen muss.

:::herleitung
**Ausgangspunkt:** der Gleichverteilungssatz: Im thermischen Gleichgewicht bei der Temperatur $T$ trägt jeder Energieterm, der quadratisch von einer Größe abhängt, im Mittel die Energie $k_B T/2$.

**Annahmen:** (i) Ein Widerstand $R$ und ein Kondensator $C$ sind miteinander verbunden und im thermischen Gleichgewicht bei $T$; sonst ist nichts angeschlossen. (ii) Das Rauschen des Widerstands hat eine von der Frequenz unabhängige Dichte $|u_{r,R}|^2$, die gesucht ist. (iii) Aus der Wechselstromrechnung, die erst nach diesem Kurs folgt, wird ein Ergebnis übernommen: Die RC-Schaltung lässt Rauschen mit konstanter Dichte so durch, als ob sie alle Frequenzen bis $1/(4RC)$ unverändert und alle höheren gar nicht passieren ließe; diese __Rauschbandbreite__ ist das π/2-fache ihrer Grenzfrequenz $1/(2\pi RC)$. Die Rechnung dazu geht über diesen Kurs hinaus; der Kasten zeigt deshalb die Beweisidee.

**Schritt 1**: Die Energie des Kondensators, $\tfrac{1}{2}C u^2$, ist quadratisch in seiner Spannung. Nach dem Gleichverteilungssatz:

$$\frac{1}{2}\,C\,\overline{u^2} = \frac{1}{2}\,k_B T$$

$$\overline{u^2} = \frac{k_B T}{C}$$

**Schritt 2**: Dieselbe Spannung ist das Rauschen des Widerstands, gefiltert durch die RC-Schaltung. Nach Gleichung 12.1, mit der Rauschbandbreite aus (iii):

$$\overline{u^2} = |u_{r,R}|^2\cdot\frac{1}{4RC}$$

**Schritt 3** (entscheidender Schritt): Beide Ausdrücke beschreiben dieselbe Spannung. Gleichsetzen:

$$|u_{r,R}|^2\cdot\frac{1}{4RC} = \frac{k_B T}{C}$$

**Ergebnis:**

$$|u_{r,R}(f)|^2 = 4\,k_B\,T\,R$$

**Woher die Faktoren kommen:** $k_B T$ stammt aus dem Gleichverteilungssatz, also aus der Thermodynamik und nicht aus dem Material. $R$ steht da, weil ein größerer Widerstand mit demselben Kondensator eine schmalere Bandbreite hat: Dieselbe mittlere Energie verteilt sich auf weniger Hertz, die Dichte steigt. Die 4 stammt aus der Rauschbandbreite $1/(4RC)$.

**Proben:** Einheit: J/K mal K mal Ω ergibt J·Ω = V²·s = V²/Hz. Zahlenwert: 4 · 1,380649·10⁻²³ J/K · 300 K · 1 kΩ = 1,66·10⁻¹⁷ V²/Hz, die Wurzel 4,07 nV/√Hz. Grenzfall: Ein Kurzschluss, $R$ = 0, rauscht nicht. Kontrolle: 10 kΩ an 10 pF haben die Rauschbandbreite 2,5 MHz; mit der Dichte $4 k_B T R$ ergibt das 20,35 µV, genau die Wurzel aus $k_B T/C$.

**Grenzen:** Die Dichte ist konstant bis zu Frequenzen der Größenordnung $k_B T/h$, bei 300 K etwa 6 THz ($h$ Plancksches Wirkungsquantum); darüber fällt sie ab. Fließt ein Strom durch den Widerstand, kann bei manchen Bauarten stromabhängiges Zusatzrauschen hinzukommen, das die Formel nicht erfasst.
:::

::::beispiel Rauschen eines 10-kΩ-Widerstands im Hörbereich
**Gegeben:** $R$ = 10 kΩ bei 300 K; Bandbreite 20 kHz; $k_B$ = 1,380649·10⁻²³ J/K.

**Gesucht:** Rauschdichte, Effektivwert und das Signal-Rausch-Verhältnis eines Signals von 1 mV.

**Rechnung:**

$$|u_{r,R}|^2 = 4\cdot 1{,}380649\cdot10^{-23}\ \frac{\mathrm{J}}{\mathrm{K}}\cdot 300\ \mathrm{K}\cdot 10^4\ \Omega = 1{,}66\cdot10^{-16}\ \frac{\mathrm{V}^2}{\mathrm{Hz}}$$

Die Wurzel ist 12,87 nV/√Hz; bei konstanter Dichte:

$$U_r = 12{,}87\ \frac{\mathrm{nV}}{\sqrt{\mathrm{Hz}}}\cdot\sqrt{20\,000\ \mathrm{Hz}} = 1{,}82\ \mu\mathrm{V}$$

$$\mathrm{SNR}_\mathrm{dB} = 10\,\lg\frac{(1\ \mathrm{mV})^2}{(1{,}82\ \mu\mathrm{V})^2} = 54{,}8\ \mathrm{dB}$$

**Ergebnis:** **12,9 nV/√Hz, 1,82 µV, 54,8 dB.**

**Einordnung:** Ein Signal von 10 µV läge nur 14,8 dB über diesem Rauschen. Hochohmige Quellen rauschen stärker: 1 MΩ bringt im selben Band 18,2 µV.
::::

Das Skript nennt drei weitere Arten (S. 195–196). __Weiß__ heißt ein Spektrum mit gleicher Dichte bei allen Frequenzen, wie das thermische; das ist eine Form, keine eigene Ursache, und unendliche Leistung hat nur das Modell. __Schrotrauschen__ entsteht, weil die Zahl der Ladungsträger, die eine Barriere wie den pn-Übergang unabhängig voneinander überqueren, je Zeitabschnitt schwankt. __1/f-Rauschen__, ebenfalls nach seiner Spektralform benannt, stammt unter anderem von langsamen Umladungen in Störstellen und beherrscht tiefe Frequenzen, bei Universal-OPVs unterhalb von etwa 100 Hz.

## Der Differenzverstärker

*Wie antwortet eine Schaltung nur auf den Unterschied zweier Spannungen?*

:::grafik
Szene: get1/operationsverstaerker/01-differenzverstaerker · Vorlage: schaltung-und-kennlinie
**Abbildung 3:** (a) Differenzverstärker nach Skript Bild 12.1 mit Werten, abweichend vom Skript mit dem Emitter von Q3 an −15 V statt an Masse, damit die Eingänge um 0 V liegen dürfen: zwei gleiche npn-Transistoren Q1 und Q2 (Beispieltransistor, Art BC547C) mit je einem Kollektorwiderstand $R_C$ = 10 kΩ an +15 V; die Emitter verbunden und über eine Stromquelle von 1 mA (Transistor Q3) an −15 V; die Eingänge $U_{e1}$ und $U_{e2}$ an den Basen, der Ausgang $U_A$ zwischen den Kollektoren, Zählpfeil vom Kollektor von Q1 zum Kollektor von Q2. Ruhewerte bei gleichen Eingängen auf 0 V: je 0,499 mA, Kollektoren auf 10,0 V, Emitterknoten auf −0,635 V. (b) Die Kollektorströme $I_{C1}$ und $I_{C2}$ über $U_{e1} - U_{e2}$ von −150 mV bis +150 mV: zwei gegenläufige S-Kurven, die sich bei 0 mV und 0,5 mA kreuzen und zusammen stets 1 mA ergeben; gestrichelt die Tangente im Nullpunkt mit der Steigung 9,67 mS; markiert die Werte bei ±100 mV, 98 % und 2 %. Die Stromquelle hält die Summe fest, die Differenz der Eingänge verteilt sie.
:::

Stören zwei parallel geführte Leitungen gleich, etwa durch eingestreutes Netzbrummen, steckt die Information im Unterschied der beiden. Der __Differenzverstärker__ (Skript S. 196–197), die Eingangsstufe jedes OPV, verstärkt genau diesen Unterschied; Abbildung 3a zeigt ihn mit den Werten des Beispiels.

**Die Akteure:**

- __$U_{e1}$__, __$U_{e2}$__: Eingangsspannungen an den Basen, gegen Masse.
- __$I_0$__: Strom der Stromquelle Q3 im gemeinsamen Emitterzweig, dem __Fußpunkt__, im Skript $I_{Q3}$; 1 mA.
- __$\varphi_E$__: Potential des gemeinsamen Emitterknotens; in Ruhe −0,635 V.
- __$I_{C1}$__, __$I_{C2}$__: Kollektorströme, in Ruhe je 0,499 mA. Die Kollektorwiderstände __$R_C$__ = 10 kΩ an +15 V machen daraus die Kollektorpotentiale $U_{a1}$ und $U_{a2}$.
- __$U_A$__: Ausgangsspannung zwischen den Kollektoren, die Differenz $U_{a1} - U_{a2}$.
- __$U_{Gl}$__: __Gleichtaktspannung__, der Mittelwert der beiden Eingangsspannungen, also der Anteil, den beide gemeinsam haben.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Q3 arbeitet als Stromquelle wie der Ausgangstransistor eines Stromspiegels ([Arbeitspunkt und Grundschaltungen des Transistors](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/arbeitspunkt-und-grundschaltungen.html), Abschnitt *Der Stromspiegel*): Die Summe der beiden Emitterströme liegt bei 1 mA fest.

**Schritt 2**: Beide Emitter hängen am selben Knoten; die Basis-Emitter-Spannungen unterscheiden sich deshalb genau um $U_{e1} - U_{e2}$. Nach der Transfergleichung legt dieser Unterschied das Stromverhältnis fest: Je 25,85 mV, die $U_{e1}$ höher liegt, führt Q1 das 2,72-fache des Stroms von Q2.

**Schritt 3**: Summe fest, Verhältnis durch die Differenz bestimmt: Beide Ströme hängen nur von $U_{e1} - U_{e2}$ ab. Hebt man beide Eingänge um 5 V an, steigt der Emitterknoten mit, von −0,635 V auf 4,363 V; die Ströme ändern sich um 0,01 %, der Ausgang bleibt bei null. Die Gleichtaktspannung erreicht den Ausgang nicht.

**Schritt 4**: Bei einer kleinen Änderung von $U_{e1}$ wandert der Emitterknoten um die Hälfte mit, denn der Strom, den Q1 gewinnt, muss Q2 verlieren. Jeder Transistor bekommt also die halbe Differenz.

**Schritt 5**: Bei ±100 mV fließen 98 % des Stroms durch einen Transistor: Die Stufe wird zum __Stromschalter__, ihr Ausgang nähert sich ±10 V (Abbildung 3b). Gleichmäßig verstärkt sie nur Differenzen, die klein gegen $2U_T$ sind, also gegen 52 mV.

:::formel Formel
$$I_{C1} = \frac{I_0}{1 + \exp\big(-(U_{e1} - U_{e2})/U_T\big)}$$
:::

**So liest man das:** Bei gleichen Eingängen teilt sich der Strom je zur Hälfte, bei 25,85 mV Differenz führt Q1 73 %, bei 100 mV 98 %; $I_{C2}$ ist der Rest bis $I_0$. Die Gleichtaktspannung kommt in der Formel nicht vor.

Idee der Herleitung: Man bildet den Quotienten der beiden Transfergleichungen; darin kürzt sich das Potential des Emitterknotens heraus.

:::herleitung
**Ausgangspunkt:** die Transfergleichung des Bipolartransistors, hergeleitet in [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html), Abschnitt *Der Transistoreffekt*:

$$I_C = I_S\,\exp\Big(\frac{U_{BE}}{U_T}\Big)$$

**Annahmen:** (i) Q1 und Q2 sind gleich (gleiches $I_S$) und gleich warm. (ii) Beide arbeiten im aktiven Bereich. (iii) Die Basisströme werden vernachlässigt, so dass die Kollektorströme zusammen $I_0$ ergeben; bei $B$ = 500 ist das ein Fehler von 0,2 %. (iv) Der Early-Effekt wird vernachlässigt.

**Schritt 1**: Basis-Emitter-Spannungen mit dem gemeinsamen Emitterpotential:

$$U_{BE1} = U_{e1} - \varphi_E$$

$$U_{BE2} = U_{e2} - \varphi_E$$

**Schritt 2** (entscheidender Schritt): Quotient der Transfergleichungen; $I_S$ und $\varphi_E$ kürzen sich heraus:

$$\frac{I_{C1}}{I_{C2}} = \exp\Big(\frac{U_{BE1} - U_{BE2}}{U_T}\Big) = \exp\Big(\frac{U_{e1} - U_{e2}}{U_T}\Big)$$

**Schritt 3**: Mit $I_{C2} = I_0 - I_{C1}$ wird daraus eine Gleichung für $I_{C1}$ allein:

$$I_{C1}\,\Big(1 + \exp\Big(-\frac{U_{e1} - U_{e2}}{U_T}\Big)\Big) = I_0$$

**Ergebnis:**

$$I_{C1} = \frac{I_0}{1 + \exp\big(-(U_{e1} - U_{e2})/U_T\big)}$$

**Woher die Faktoren kommen:** Die Exponentialfunktion stammt aus der Transfergleichung. Dass nur die Differenz auftritt, liegt am gemeinsamen Emitterknoten, dessen Potential sich im Quotienten kürzt; $I_0$ liefert die Stromquelle.

**Proben:** Einheit A. Bei gleichen Eingängen ergibt sich $I_0/2$, für sehr große positive Differenzen $I_0$, für sehr große negative null. Zahlenwert bei 100 mV: Der Kehrwert von 1 + exp(−3,868) ist 0,9795; das vollständige Modell mit Basisströmen und Early-Effekt ergibt 0,977.

**Grenzen:** Sinkt ein Kollektor so tief, dass der Transistor in die Sättigung gerät, oder verlässt Q3 seinen aktiven Bereich, gilt die Formel nicht mehr. Mit einem Widerstand statt der Stromquelle ist die Summe nicht mehr fest.
:::

Für kleine Differenzen genügt die Tangente der Stromaufteilung im Nullpunkt. Mit der Steilheit eines Transistors beim halben Fußpunktstrom,

$$g_m = \frac{I_0}{2\,U_T}$$

ergibt sich die __Differenzverstärkung__ der Stufe, im Skript $A$, hier wie in [Der Transistor als Verstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker.html) $v_u$:

:::formel Formel
$$v_u = \frac{U_A}{U_{e1} - U_{e2}} = -g_m\,R_C$$
:::

**So liest man das:** Jeder Transistor bekommt die halbe Differenz, der Ausgang zwischen den Kollektoren sieht beide Änderungen. Der Betrag ist der Spannungsabfall an einem Kollektorwiderstand durch $U_T$, hier 4,99 V durch 25,85 mV, also 193. Das Minuszeichen sagt: Steigt $U_{e1}$, sinkt $U_A$; $U_{e1}$ wirkt invertierend, $U_{e2}$ nichtinvertierend. Das Skript erhält $-2SR$ (S. 197), im Beispiel −387, weil es die ganze Signaländerung an $U_{BE1}$ ansetzt und übersieht, dass der Emitterknoten um die Hälfte mitwandert. Auch seine „Größenordnung 10 000“ erreicht diese Stufe nicht; an 15 V bleibt sie unter 580.

Idee der Herleitung: Man leitet die Stromaufteilung im Nullpunkt ab und rechnet die Stromänderungen über die Kollektorwiderstände in Spannungen um.

:::herleitung
**Ausgangspunkt:** die Stromaufteilung (Formel oben) und die Spannungsabfälle an den Kollektorwiderständen, wie im Skript S. 197.

**Annahmen:** (i) bis (iv) wie bei der Stromaufteilung; (v) die Differenz ist klein gegen $2U_T$. Abkürzung: $x$ steht für $U_{e1} - U_{e2}$.

**Schritt 1**: Ableitung der Stromaufteilung nach $x$:

$$\frac{dI_{C1}}{dx} = \frac{I_0}{U_T}\,\frac{\exp(-x/U_T)}{\big(1 + \exp(-x/U_T)\big)^2}$$

Im Nullpunkt ist der Bruch 1/4:

$$\frac{dI_{C1}}{dx}\Big|_{x=0} = \frac{I_0}{4\,U_T} = \frac{g_m}{2}$$

**Schritt 2**: Weil die Summe fest ist, ändert sich $I_{C2}$ um denselben Betrag in Gegenrichtung:

$$\Delta I_{C1} = \frac{g_m}{2}\,x$$

$$\Delta I_{C2} = -\frac{g_m}{2}\,x$$

**Schritt 3** (entscheidender Schritt): Die Kollektorpotentiale fallen um $R_C$ mal Strom unter die Versorgung $U_{CC}$; der Ausgang ist ihre Differenz:

$$U_{a1} = U_{CC} - R_C\,I_{C1}$$

$$U_{a2} = U_{CC} - R_C\,I_{C2}$$

$$\Delta U_A = -R_C\,(\Delta I_{C1} - \Delta I_{C2}) = -g_m\,R_C\,x$$

**Ergebnis:**

$$v_u = \frac{U_A}{U_{e1} - U_{e2}} = -g_m\,R_C$$

**Woher die Faktoren kommen:** Je Transistor wirkt die halbe Steilheit, weil jeder die halbe Differenz bekommt; der Ausgang zwischen den Kollektoren addiert beide Hälften wieder zur ganzen. Das Minus stammt aus dem Spannungsabfall: Mehr Strom, tieferes Kollektorpotential.

**Proben:** Einheit S·Ω = 1. Zahlenwert: 19,3 mS · 10 kΩ = 193. Das vollständige Modell ergibt −182; den Unterschied macht der Early-Effekt, der wie ein Widerstand von 162 kΩ parallel zu $R_C$ wirkt: −19,3 mS mal 9,42 kΩ ergibt −182. Grenzfall: Ohne Fußpunktstrom gibt es keine Steilheit und keine Verstärkung.

**Grenzen:** Bei 10 mV Differenz bleibt das Ausgangssignal 1,2 % unter dem linearen Wert, bei 26 mV 7,6 %; darüber wird die Stufe zum Stromschalter.
:::

::::beispiel Differenzverstärker mit 1 mA Fußpunktstrom
**Gegeben:** Versorgung ±15 V, $R_C$ = 10 kΩ, ideale Stromquelle mit 1 mA, zwei Beispieltransistoren (Art BC547C, $B$ = 500, Early-Spannung 70 V); $U_T$ = 25,85 mV.

**Gesucht:** (a) Steilheit und Verstärkung; (b) die Wirkung einer Gleichtaktspannung von +5 V.

**Rechnung:** (a) Je Zweig fließen 0,499 mA (halber Emitterstrom abzüglich des Basisstroms, vollständiges Modell):

$$g_m = \frac{0{,}499\ \mathrm{mA}}{25{,}85\ \mathrm{mV}} = 19{,}3\ \mathrm{mS}$$

$$v_u = -19{,}3\ \mathrm{mS}\cdot 10\ \mathrm{k}\Omega = -193$$

Mit Early-Effekt ergibt das vollständige Modell −182.

(b) Beide Eingänge auf +5 V: Der Emitterknoten steigt von −0,635 V auf 4,363 V, die Kollektorströme ändern sich von 0,49907 mA auf 0,49901 mA; $U_A$ bleibt 0.

**Ergebnis:** **Verstärkung −193 (−182 mit Early-Effekt); +5 V Gleichtakt ändern die Ströme um 0,01 %.**

**Einordnung:** Ein Millivolt Differenz verschiebt den Ausgang um 0,19 V, fünf Volt Gleichtakt verschieben ihn gar nicht.
::::

## Der ideale Operationsverstärker und der Komparator

*Was tut ein OPV ohne äußere Beschaltung, und warum taugt er so nicht als Verstärker?*

Im OPV folgen auf den Differenzverstärker weitere Verstärkerstufen und ein Emitterfolger als Ausgang; zusammen verstärken sie 10⁵- bis 10⁶-fach (Skript S. 197). Der __nichtinvertierende Eingang__ (+) entspricht $U_{e2}$ des Differenzverstärkers: Steigt seine Spannung, steigt der Ausgang. Der __invertierende Eingang__ (−) entspricht $U_{e1}$: Steigt seine Spannung, sinkt der Ausgang (Abbildung 1a). Als Beispiel dient ein OPV nach Art des 741 an ±15 V.

**Die Akteure:**

- __$U_{e+}$__, __$U_{e-}$__: Spannungen am Plus- und am Minuseingang, gegen Masse.
- __$U_D$__: __Differenzspannung__ vom Plus- zum Minuseingang:

$$U_D = U_{e+} - U_{e-}$$

- __$v_D$__: __Leerlaufverstärkung__, die Verstärkung ohne äußere Beschaltung; beim 741 typisch 200 000, garantiert mindestens 50 000.
- __$U_A$__: Ausgangsspannung gegen Masse, begrenzt auf $U_{A,\min}$ bis $U_{A,\max}$, beim 741 typisch ±14 V.

:::formel Definition
$$U_A = v_D\,U_D$$
:::

**So liest man das:** Der Ausgang ist die verstärkte Differenzspannung, solange das Ergebnis zwischen den Grenzen liegt; sonst bleibt er an der Grenze. Die Grenzen liegen etwa 1 V unter den Versorgungsspannungen, weil zwischen Ausgang und Versorgung Transistoren liegen (Skript S. 199). Proportional ist der Ausgang deshalb nur in einem schmalen Fenster:

$$|U_D| \le \frac{U_{A,\max}}{v_D} = \frac{14\ \mathrm{V}}{200\,000} = 70\ \mu\mathrm{V}$$

Idee der Herleitung: Man setzt die Ausgangsgrenze in die Definition ein.

:::herleitung
**Ausgangspunkt:** die Definition der Leerlaufverstärkung.

**Annahmen:** (i) symmetrische Ausgangsgrenzen, $U_{A,\min} = -U_{A,\max}$; (ii) die Kennlinie ist innerhalb der Grenzen eine Gerade durch den Nullpunkt.

**Schritt 1**: Im linearen Bereich bleibt der Ausgang innerhalb der Grenzen:

$$|v_D\,U_D| \le U_{A,\max}$$

**Schritt 2**: Teilen durch die positive Verstärkung:

$$|U_D| \le \frac{U_{A,\max}}{v_D}$$

**Ergebnis:** Das Fenster ist $U_{A,\max}/v_D$ breit, nach beiden Seiten.

**Woher die Faktoren kommen:** Je größer die Verstärkung, desto schmaler das Fenster; seine Breite ist die Grenze, geteilt durch die Verstärkung.

**Proben:** 14 V durch 200 000 ergibt 70 µV; mit der garantierten Mindestverstärkung 50 000 sind es 280 µV.

**Grenzen:** Der reale OPV hat eine Offsetspannung, die das Fenster verschiebt (unten); seine Kennlinie ist zudem nur näherungsweise gerade.
:::

Wie schmal das ist, zeigt die __Offsetspannung__: Die Eingangstransistoren sind nie ganz gleich, und der Unterschied wirkt wie eine kleine Spannungsquelle am Eingang, beim 741 typisch 1 mV, 14-mal so weit vom Nullpunkt wie der Rand des Fensters. Selbst mit verbundenen Eingängen läge der Ausgang an einer Grenze. Ohne Rückkopplung arbeitet der OPV deshalb nur als __Komparator__ (Vergleicher, Skript Bild 12.3 und 12.4): Liegt der Pluseingang höher, zeigt der Ausgang +14 V, liegt er tiefer, −14 V. Mehrere Komparatoren an den Abgriffen eines Spannungsteilers bilden einen __Flash-Wandler__, einen schnellen Analog-Digital-Umsetzer (Skript Bild 12.5).

Das Skript (S. 198) idealisiert den OPV mit vier Eigenschaften:

| Eigenschaft des idealen OPV und Folge | Beispiel-OPV (741 an ±15 V) |
|---|---|
| Eingangs­widerstand unendlich: In die Eingänge fließt kein Strom. | 2 MΩ; Eingangs­ruhestrom 80 nA |
| Leerlauf­verstärkung unendlich und frequenz­unabhängig: Mit Gegenkopplung wird $U_D$ null. | 200 000, mindestens 50 000; oberhalb von 5 Hz fallend, bei 1 MHz nur noch 1 |
| Ausgangs­widerstand null: Der Ausgang liefert jeden Strom, den die Schaltung verlangt. | Kurzschluss­strom 25 mA |
| kein Rauschen | 23 nV/√Hz |

## Rückkopplung: Gegen- und Mitkopplung

*Was ändert sich, wenn ein Teil der Ausgangsspannung an einen Eingang zurückgeführt wird?*

:::grafik
Szene: get1/operationsverstaerker/01-gegen-mit · Vorlage: schaltung-zustaende
**Abbildung 4:** Zwei Schaltungen aus denselben Bauteilen: Beispiel-OPV, $R_2$ = 90 kΩ vom Ausgang zum Teilerknoten, $R_1$ = 10 kΩ vom Teilerknoten nach Masse. Links Gegenkopplung: Teilerknoten am Minuseingang, Eingangsspannung $U_E$ am Pluseingang; darunter die Wirkungskette „$U_A$ steigt → Minuseingang steigt um ein Zehntel davon → $U_D$ sinkt → $U_A$ steigt langsamer“. Rechts Mitkopplung, der invertierende Schmitt-Trigger nach Skript Bild 12.6: Teilerknoten am Pluseingang, $U_E$ am Minuseingang; Wirkungskette „$U_A$ steigt → Pluseingang steigt → $U_D$ steigt → $U_A$ steigt schneller“. Welcher Eingang das zurückgeführte Signal bekommt, entscheidet, ob die Schaltung regelt oder kippt.
:::

Eine __Rückkopplung__ führt einen Teil der Ausgangsgröße auf den Eingang zurück (Skript S. 200). Geht sie beim OPV auf den invertierenden Eingang, wirkt eine Zunahme des Ausgangs der Differenzspannung entgegen, die sie verursacht hat: __Gegenkopplung__. Geht sie auf den nichtinvertierenden Eingang, vergrößert die Zunahme ihre eigene Ursache: __Mitkopplung__. Abbildung 4 zeigt beide mit denselben Bauteilen; links steht der nichtinvertierende Verstärker, rechts der Schmitt-Trigger.

### Der Ruhezustand

*Welche Ausgangsspannung stellt sich bei Gegenkopplung ein, und warum hängt sie kaum vom OPV ab?*

**Die Akteure:**

- __$R_1$__, __$R_2$__: Spannungsteiler, $R_2$ = 90 kΩ vom Ausgang zum Teilerknoten, $R_1$ = 10 kΩ nach Masse.
- __$k$__: __Rückkopplungsfaktor__, der Anteil der Ausgangsspannung am Teilerknoten; 0,1. Weil in den Eingang kein Strom fließt, ist der Teiler unbelastet:

$$k = \frac{R_1}{R_1 + R_2}$$

- __$U_E$__: Eingangsspannung der Schaltung, gegen Masse, am Pluseingang.
- __$A$__: Verstärkung der beschalteten Schaltung, das Verhältnis von $U_A$ zu $U_E$ (so im Skript ab Abschnitt 12.5).

**Das Zusammenspiel:** Der Minuseingang liegt auf $k U_A$; die Differenzspannung ist der Unterschied zwischen dem, was der Eingang verlangt, und dem, was zurückkommt:

$$U_D = U_E - k\,U_A$$

Ist $U_A$ zu klein, treibt ein positives $U_D$ den Ausgang nach oben, ist er zu groß, zieht ein negatives ihn nach unten. Zusammen mit der Gleichung des OPV folgt der Ruhezustand:

:::formel Formel
$$A = \frac{U_A}{U_E} = \frac{v_D}{1 + k\,v_D}$$
$$U_D = \frac{U_E}{1 + k\,v_D}$$
:::

**So liest man das:** Das Produkt $k\,v_D$, die __Schleifenverstärkung__, ist hier 20 000. Ist sie groß gegen 1, kürzt sich $v_D$ heraus, und es bleibt ein Ergebnis, das nur die Widerstände enthalten:

$$A \approx \frac{1}{k} = 1 + \frac{R_2}{R_1}$$

Die riesige, unsichere Leerlaufverstärkung verschwindet aus dem Ergebnis; die Differenzspannung wird winzig.

**Kurz gesagt:** Mit idealem OPV macht der nichtinvertierende Verstärker genau rückgängig, was der Teiler in seiner Rückführung tut: Seine Verstärkung ist der Kehrwert des Rückkopplungsfaktors, solange der Ausgang nicht an einer Grenze liegt.

Idee der Herleitung: Zwei Gleichungen, die des OPV und die Masche über seine Eingänge, werden nach den zwei Unbekannten aufgelöst.

:::herleitung
**Ausgangspunkt:** die Gleichung des OPV im linearen Bereich, $U_A = v_D U_D$, die Maschenregel über die Eingänge und die Teilerregel für den unbelasteten Spannungsteiler.

**Annahmen:** (i) Der Ausgang liegt nicht an einer Grenze. (ii) In die Eingänge fließt kein Strom; der Teiler ist unbelastet. (iii) Ruhezustand: Alle Spannungen sind konstant.

**Schritt 1**: Teilerregel: Der Minuseingang liegt auf dem Anteil $k$ der Ausgangsspannung.

**Schritt 2**: Masche vom Pluseingang über die Eingangsquelle, Masse und den Teiler zum Minuseingang:

$$U_D = U_E - k\,U_A$$

**Schritt 3** (entscheidender Schritt): In die Gleichung des OPV einsetzen; $U_A$ steht dann auf beiden Seiten:

$$U_A = v_D\,(U_E - k\,U_A)$$

**Schritt 4**: Nach $U_A$ ordnen:

$$U_A\,(1 + k\,v_D) = v_D\,U_E$$

**Ergebnis:**

$$A = \frac{U_A}{U_E} = \frac{v_D}{1 + k\,v_D}$$

$$U_D = U_E - k\,U_A = \frac{U_E}{1 + k\,v_D}$$

Für $k v_D \gg 1$ wird die 1 im Nenner vernachlässigbar, und $A$ geht gegen $1/k$; mit dem Teiler ist $1/k$ gleich $(R_1 + R_2)/R_1$.

**Woher die Faktoren kommen:** Die Eingangsspannung teilt sich auf in die Differenzspannung $U_A/v_D$, die der OPV selbst für seinen Ausgang braucht, und den zurückgeführten Anteil $k U_A$. Aus dem ersten Teil wird die 1 im Nenner, aus dem zweiten $k v_D$. Je größer $v_D$, desto weniger zählt die 1, und $A$ geht gegen $1/k$.

**Proben:** Einheitenlos, wie eine Verstärkung. Zahlenwert: $k v_D$ = 20 000, also 200 000/20 001 = 9,9995. Grenzfall ohne Rückkopplung, $k$ = 0: Die Verstärkung ist $v_D$, die des nackten OPV. Grenzfall unendliche Leerlaufverstärkung: Sie ist $1/k$, und $U_D$ ist null.

**Grenzen:** Die Rechnung setzt einen Ruhezustand voraus und sagt nicht, ob er erreicht wird. Für die Mitkopplung, bei der $U_D$ gleich $k U_A - U_E$ ist, liefert sie ebenfalls einen Ruhezustand nahe $U_E/k$, der nie eintritt; den Unterschied erklärt der nächste Abschnitt. Liegt der Ausgang an einer Grenze, gilt die Gleichung des OPV nicht, und $U_D$ ist nicht klein.
:::

::::beispiel Verstärker mit dem Rückkopplungsfaktor 0,1
**Gegeben:** $R_1$ = 10 kΩ, $R_2$ = 90 kΩ; Beispiel-OPV mit $v_D$ = 200 000 (typisch) bzw. 50 000 (mindestens); Ausgangsgrenze +14 V.

**Gesucht:** (a) die Verstärkung mit beiden Leerlaufverstärkungen und $U_D$ bei 5 V am Ausgang; (b) was bei 2 V am Eingang geschieht.

**Rechnung:** (a) $k$ = 10 kΩ/100 kΩ = 0,1:

$$A = \frac{200\,000}{1 + 0{,}1\cdot 200\,000} = 9{,}9995$$

$$A = \frac{50\,000}{1 + 0{,}1\cdot 50\,000} = 9{,}9980$$

Bei 5 V am Ausgang braucht der OPV 5 V / 200 000 = 25 µV.

(b) Verlangt wären 20 V; der Ausgang bleibt bei 14 V stehen, und die Differenzspannung ist nicht mehr klein:

$$U_D = 2\ \mathrm{V} - 0{,}1\cdot 14\ \mathrm{V} = 0{,}6\ \mathrm{V}$$

**Ergebnis:** **(a) A = 9,9995 bzw. 9,998, $U_D$ = 25 µV; (b) Sättigung bei 14 V mit 0,6 V zwischen den Eingängen.**

**Einordnung:** Ein Viertel der Leerlaufverstärkung ändert die Verstärkung der Schaltung um 0,015 %. In der Sättigung liegt zwischen den Eingängen 24 000-mal mehr Spannung als im Normalbetrieb.
::::

:::frage
„Wenn $U_D$ null ist, muss dann nicht auch $U_A = v_D U_D$ null sein?“
$U_D$ ist nicht genau null, sondern so klein, dass man es beim Rechnen vernachlässigen darf: 25 µV bei 5 V Ausgang. Mit 200 000 multipliziert ergeben gerade diese 25 µV die 5 V. Im idealen Modell geht $U_D$ gegen null und $v_D$ gegen unendlich; ihr Produkt bleibt endlich, und die Rückführung legt es fest.
:::

### Warum die Schaltung zur Ruhe kommt

*Warum läuft die gegengekoppelte Schaltung in diesen Ruhezustand, und warum verlässt die mitgekoppelte ihn?*

:::grafik
Szene: get1/operationsverstaerker/01-einschwingen · Vorlage: zeitverlauf
**Abbildung 5:** (a) Gegenkopplung mit $k$ = 0,1: Die Eingangsspannung springt bei $t$ = 0 von 0 auf 10 mV. Oben $U_A$ über $t$ von 0 bis 12 µs: exponentieller Anstieg auf 0,1 V, nach 1,59 µs bei 63 %, nach 11 µs auf 0,1 % am Endwert, ohne Überschwingen; die Anfangssteigung 63 mV/µs als gestrichelte Tangente. Darunter $U_D$ über derselben Zeitachse, logarithmisch: von 10 mV auf 5,8 µV nach 12 µs fallend, der Endwert 0,5 µV gestrichelt. (b) Mitkopplung (Schmitt-Trigger mit $U_E$ = 0) aus einer Anfangsabweichung von 0,13 mV am Ausgang, Zeitachse 0 bis 50 µs: $U_A$ wächst exponentiell mit derselben Zeitkonstante, ab etwa 0,8 V linear mit der größten Anstiegsgeschwindigkeit des 741, 0,5 V/µs, und erreicht 13 V nach 38 µs; gestrichelt der rein exponentielle Verlauf ohne diese Grenze, 13 V nach 18 µs. Gegenkopplung lässt jede Abweichung abklingen, Mitkopplung lässt sie mit derselben Zeitkonstante wachsen.
:::

Die Rechnung oben setzt voraus, dass sich nichts mehr ändert. Ob die Schaltung dorthin kommt, entscheidet eine Eigenschaft, die im idealen Modell fehlt: Ein realer OPV kann seinen Ausgang nicht springen lassen. In seinem Inneren lädt die Eingangsstufe einen Kondensator mit einem Strom proportional zu $U_D$; deshalb ändert sich der Ausgang mit einer Geschwindigkeit proportional zu $U_D$.

**Die Akteure:**

- __$f_T$__: __Transitfrequenz__ des OPV, die Frequenz, bei der seine Verstärkung auf 1 gefallen ist, im Datenblatt Verstärkungs-Bandbreite-Produkt; beim 741 1 MHz.
- __$\omega_T$__: die zugehörige Kreisfrequenz $2\pi f_T$, 6,28·10⁶ 1/s: 1 mV Differenzspannung lässt den Ausgang um 6,28 V je Millisekunde steigen.
- __$\tau$__: Zeitkonstante des Einschwingens.

:::formel Formel
$$\frac{dU_A}{dt} = \omega_T\,U_D$$
:::

**So liest man das:** Solange $U_D$ positiv ist, steigt der Ausgang, solange es negativ ist, fällt er; still steht er nur bei $U_D$ = 0. Das gilt, solange $U_D$ klein ist und die Geschwindigkeit unter der Grenze des OPV bleibt, beim 741 0,5 V/µs.

Idee der Herleitung: Die Eingangsstufe liefert einen Strom proportional zu $U_D$, und dieser Strom lädt einen Kondensator, dessen Spannung den Ausgang bestimmt.

:::herleitung
**Ausgangspunkt:** die Kondensatorgleichung $i = C\,du/dt$ ([Laden und Entladen des Kondensators](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/laden-und-entladen.html)) und der innere Aufbau eines OPV wie des 741: Eingangsstufe (Differenzverstärker), zweite Verstärkerstufe mit einem Kondensator $C_c$ zwischen ihrem Eingang und ihrem Ausgang, dem __Kompensationskondensator__ (30 pF beim 741), Emitterfolger als Ausgang.

**Annahmen:** (i) Die Eingangsstufe liefert in die zweite Stufe einen Strom, der proportional zu $U_D$ ist, mit dem Faktor $G_{m1}$, ihrer Steilheit; das gilt für kleine $U_D$. (ii) Die zweite Stufe verstärkt so stark, dass sich ihr Eingangspotential praktisch nicht ändert; der ganze Strom fließt deshalb in den Kondensator. (iii) Der Emitterfolger gibt die Spannung am Ausgang der zweiten Stufe mit dem Faktor 1 weiter. (iv) Die Leerlaufverstärkung wird als unendlich behandelt; mit 200 000 ändert das die Ergebnisse um weniger als 0,01 %. Die Polung der Stufen ist so gewählt, dass ein positives $U_D$ den Ausgang hebt.

**Schritt 1**: Strom der Eingangsstufe:

$$i = G_{m1}\,U_D$$

**Schritt 2** (entscheidender Schritt): Der Strom lädt den Kondensator. Weil seine eine Seite, der Eingang der zweiten Stufe, festliegt, ändert sich die Spannung an der anderen Seite, dem Ausgang, mit der vollen Kondensatorspannung:

$$\frac{dU_A}{dt} = \frac{i}{C_c} = \frac{G_{m1}}{C_c}\,U_D$$

**Ergebnis:**

$$\frac{dU_A}{dt} = \omega_T\,U_D$$

$$\omega_T = \frac{G_{m1}}{C_c}$$

**Woher die Faktoren kommen:** $G_{m1}$ sagt, wie stark die Eingangsstufe auf $U_D$ antwortet, $C_c$, wie träge der Knoten ist, den sie lädt.

**Proben:** Einheit: S/F = (A/V)/(A·s/V) = 1/s. Zahlenwert: Mit 30 pF und dem Datenblattwert 1 MHz folgt $G_{m1}$ = 2π · 1 MHz · 30 pF = 0,19 mS. Zum Namen: Für eine Sinusspannung $U_D$ der Frequenz $f$ ergibt die Integration am Ausgang eine Amplitude, die das $f_T/f$-fache beträgt; bei $f = f_T$ ist sie gleich der Eingangsamplitude, die Verstärkung 1.

**Grenzen:** Bei größeren $U_D$ arbeitet die Eingangsstufe nicht mehr linear und schaltet schließlich ganz auf eine Seite (Stromschalter, Abschnitt *Der Differenzverstärker*); mehr als ihren Fußpunktstrom kann sie nicht liefern. Dann ändert sich der Ausgang mit einer festen Höchstgeschwindigkeit, der __Anstiegsgeschwindigkeit__ (englisch slew rate), beim 741 0,5 V/µs; das entspricht 15 µA Ladestrom in 30 pF.
:::

**Das Zusammenspiel in Schritten** (Gegenkopplung wie in Abbildung 4 links; die Eingangsspannung springt von 0 auf 10 mV):

**Schritt 1**: Im ersten Moment ist $U_A$ noch null, $U_D$ also die ganze Eingangsspannung; der Ausgang beginnt mit 63 mV/µs zu steigen.

**Schritt 2**: Mit $U_A$ steigt die zurückgeführte Spannung am Minuseingang; $U_D$ wird kleiner und der Anstieg langsamer, je näher $U_A$ dem Wert $U_E/k$ = 0,1 V kommt. Über das Ziel schießt der Ausgang nicht, denn umkehren könnte er erst, wenn $U_D$ das Vorzeichen wechselt.

**Schritt 3**: Die Abweichung vom Endwert klingt exponentiell ab, wie die Spannung eines Kondensators, der sich über einen Widerstand lädt, mit 1,59 µs Zeitkonstante; nach 11 µs fehlen noch 0,1 % (Abbildung 5a).

**Schritt 4**: Still steht der Ausgang erst bei $U_D$ = 0. Darum regelt die Gegenkopplung die Differenzspannung auf null; mit der endlichen Leerlaufverstärkung bleibt der Rest $U_A/v_D$, hier 0,5 µV.

Bei der Mitkopplung (Abbildung 4 rechts) ist $U_D = k U_A - U_E$, und das Vorzeichen kehrt sich um: Liegt $U_A$ ein wenig über dem Ruhewert, ist $U_D$ positiv, und der Ausgang entfernt sich immer schneller. Die Abweichung wächst mit derselben Zeitkonstante, aus 0,13 mV werden in 18 µs 13 V, mit der Anstiegsgrenze des 741 in 38 µs (Abbildung 5b). Der Ruhezustand der Mitkopplung existiert, ist aber __instabil__. Für die Gegenkopplung lautet der Verlauf nach dem Sprung:

$$U_A(t) = \frac{U_E}{k}\,\Big(1 - \exp\Big(-\frac{t}{\tau}\Big)\Big)$$

$$\tau = \frac{1}{k\,\omega_T}$$

Idee der Herleitung: Man setzt die Masche in das Modell des OPV ein und erhält dieselbe Gleichung wie beim Laden eines Kondensators.

:::herleitung
**Ausgangspunkt:** das Modell des OPV (Formel oben) und die Masche über die Eingänge, bei Gegenkopplung $U_D = U_E - k U_A$.

**Annahmen:** (i) $U_E$ springt bei $t$ = 0 von 0 auf einen festen Wert und bleibt dort; vorher war $U_A$ null. (ii) Der Sprung ist klein gegen 80 mV, die Differenzspannung, bei der die Eingangsstufe des 741 ihren ganzen Strom liefern müsste (die Anstiegsgeschwindigkeit 0,5 V/µs geteilt durch $\omega_T$, gleich welches $k$); dann arbeitet sie linear. Für 10 mV ist das erfüllt. (iii) Der Ausgang erreicht keine Grenze; der Teiler ist unbelastet.

**Schritt 1**: Masche einsetzen:

$$\frac{dU_A}{dt} = \omega_T\,(U_E - k\,U_A)$$

**Schritt 2**: Die Abweichung vom Endwert heißt $\delta$; weil $U_E$ konstant ist, hat sie dieselbe Ableitung wie $U_A$:

$$\delta = U_A - \frac{U_E}{k}$$

$$\frac{d\delta}{dt} = -k\,\omega_T\,\delta$$

**Schritt 3** (entscheidender Schritt): Eine Größe, deren Änderungsrate proportional zu ihr selbst ist, mit negativem Faktor, nimmt exponentiell ab, wie die Spannung an einem Kondensator, der sich über einen Widerstand entlädt; Ableiten bestätigt die Lösung:

$$\delta(t) = \delta(0)\,\exp\Big(-\frac{t}{\tau}\Big)$$

$$\tau = \frac{1}{k\,\omega_T}$$

**Schritt 4**: Anfangswert: $U_A$ beginnt bei null, also ist $\delta(0) = -U_E/k$:

$$U_A(t) = \frac{U_E}{k}\,\Big(1 - \exp\Big(-\frac{t}{\tau}\Big)\Big)$$

**Schritt 5**: Mitkopplung: Mit $U_D = k U_A - U_E$ kehrt sich das Vorzeichen in Schritt 2 um, und aus dem Abklingen wird ein Anwachsen:

$$\frac{d\delta}{dt} = +k\,\omega_T\,\delta$$

$$\delta(t) = \delta(0)\,\exp\Big(+\frac{t}{\tau}\Big)$$

**Ergebnis:** Bei Gegenkopplung klingt jede Abweichung mit der Zeitkonstante $\tau$ ab, bei Mitkopplung wächst sie mit derselben Zeitkonstante:

$$\tau = \frac{1}{k\,\omega_T}$$

**Woher die Faktoren kommen:** $k$: Je größer der zurückgeführte Anteil, desto stärker wirkt eine Abweichung auf ihre eigene Änderung, desto schneller geht es. $\omega_T$: die Geschwindigkeit des OPV.

**Proben:** Einheit: 1/(1/s) = s. Zahlenwert: 1/(0,1 · 6,283·10⁶ 1/s) = 1,59 µs. Eine Simulation des Einpolmodells mit der endlichen Leerlaufverstärkung 200 000 ergibt beim Sprung um 10 mV nach 1 µs 46,7 mV, die Formel ebenfalls 46,7 mV. Grenzfall ohne Rückkopplung, $k$ = 0: $\tau$ wird unendlich, der Ausgang integriert $U_D$ ohne Ende und läuft an eine Grenze wie beim Komparator.

**Grenzen:** Bei größeren Sprüngen arbeitet die Eingangsstufe nicht mehr linear; ab 80 mV steigt der Ausgang zunächst mit seiner Höchstgeschwindigkeit, also linear statt exponentiell. Weitere, kleinere Verzögerungen im realen OPV können bei großem $k$ ein leichtes Überschwingen erzeugen ([Der reale Operationsverstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/realer-operationsverstaerker.html)).
:::

Das Skript erklärt das Einschwingen als Folge von Zyklen, in denen der Ausgang auf $v_D U_D$ springt und $U_D$ das Vorzeichen wechselt (S. 202). Durchgerechnet schaukelt sich dieses Bild auf, statt zur Ruhe zu kommen: Mit $k$ = 0,1 und $v_D$ = 200 000 wächst die Abweichung je Zyklus um den Faktor −20 000. Die Schaltung kommt zur Ruhe, weil sich ihr Ausgang stetig bewegt, ohne dass $U_D$ das Vorzeichen wechselt.

### Die goldenen Regeln

*Mit welchen Regeln berechnet man gegengekoppelte Schaltungen?*

Für gegengekoppelte Schaltungen mit idealem OPV folgen daraus die __goldenen Regeln__: Die Differenzspannung ist null, weil die Gegenkopplung den Ausgang so lange verstellt, bis sie es ist; und in die Eingänge fließt kein Strom. Das Skript rechnet ab Abschnitt 12.5 immer so (S. 203). In Abbildung 4 links muss dann $k U_A$ gleich $U_E$ sein, und $A = 1/k$ folgt ohne jede Rechnung mit $v_D$. Den Zustand nennt man auch __virtuellen Kurzschluss__: Die Eingänge liegen auf gleichem Potential, als wären sie verbunden, ohne es zu sein.

:::merke
**Die erste goldene Regel gilt nur bei Gegenkopplung und nur, solange der Ausgang nicht an einer Grenze liegt.** Bei Mitkopplung und in der Sättigung ist $U_D$ nicht null.
:::

:::fehlvorstellung
„Virtueller Kurzschluss heißt, dass die Eingänge leitend verbunden sind und Strom zwischen ihnen fließen kann.“ Das liegt am Namen. Tatsächlich sind die Eingänge nicht verbunden; bei 25 µV fließen durch 2 MΩ Eingangswiderstand 12,5 pA, und der Ruhestrom von rund 80 nA, den jeder Eingang des 741 aufnimmt, fließt in den OPV hinein, nicht von einem Eingang zum anderen. Null ist die Spannung nur, weil der Ausgang sie ständig nachregelt. Liegt der Ausgang an einer Grenze, erscheint sie wieder: Im Beispiel zum Ruhezustand liegen bei 2 V Eingangsspannung 0,6 V zwischen den Eingängen.
:::

## Der Schmitt-Trigger

*Wozu taugt eine mitgekoppelte Schaltung, und warum hat sie ein Gedächtnis?*

:::grafik
Szene: get1/operationsverstaerker/01-schmitt-kennlinie · Vorlage: kennlinie-hysterese
**Abbildung 6:** Übertragungskennlinie des invertierenden Schmitt-Triggers aus Abbildung 4 rechts ($k$ = 0,1, Ausgangsgrenzen ±14 V): $U_A$ über $U_E$ von −3 V bis +3 V. Von links kommend liegt der Ausgang auf +14 V und springt bei $U_E$ = +1,4 V senkrecht auf −14 V; von rechts kommend bleibt er auf −14 V und springt erst bei −1,4 V zurück auf +14 V. Pfeile zeigen die Laufrichtung; gestrichelt dazwischen die Gerade der instabilen Ruhezustände mit der Steigung 10. Zwischen −1,4 V und +1,4 V hängt der Ausgang davon ab, von welcher Seite der Eingang kam.
:::

Beim __invertierenden Schmitt-Trigger__ (Abbildung 4 rechts, Skript S. 201, Bild 12.6) liegt die Eingangsspannung am Minuseingang, und der Teiler führt ein Zehntel der Ausgangsspannung auf den Pluseingang. Wie im vorigen Abschnitt gezeigt, liegt sein Ausgang immer an einer Grenze, bei +14 V oder −14 V. Weil der Pluseingang dem Ausgang folgt, verschiebt jeder Wechsel die Schwelle für den nächsten.

:::frage
„Warum bleibt ein Schmitt-Trigger beim Einschalten nicht bei 0 V stehen, wenn sein Eingang auf 0 V liegt?“
Rechnerisch ist das ein Ruhezustand, wie das Skript schreibt (S. 201): $U_D$ ist null. Er ist aber instabil, wie das labile Gleichgewicht der Mechanik. Jede Abweichung wächst mit 1,59 µs Zeitkonstante, und Abweichungen gibt es immer: die Offsetspannung von 1 mV oder, ohne sie, das Rauschen der Widerstände, 12,9 µV bei 10 kΩ und 1 MHz. Daraus werden nach 38 µs 13 V; welche Grenze der Ausgang erreicht, entscheidet das Vorzeichen der ersten Abweichung.
:::

**Die Akteure:**

- __$U_{R1,\max}$__, __$U_{R1,\min}$__: obere und untere __Schaltschwelle__, die Eingangsspannungen, bei denen der Ausgang kippt; benannt wie im Skript nach der Spannung an $R_1$ bei den beiden Ausgangsgrenzen; +1,4 V und −1,4 V.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Liegt der Ausgang bei +14 V, liegt der Pluseingang auf 1,4 V. Solange $U_E$ darunter bleibt, ist $U_D$ positiv, und der Ausgang bleibt oben.

**Schritt 2**: Steigt $U_E$ über 1,4 V, wird $U_D$ negativ, der Ausgang fällt, mit ihm der Pluseingang, und $U_D$ wird noch negativer: Die Mitkopplung treibt den Ausgang bis −14 V.

**Schritt 3**: Jetzt liegt der Pluseingang auf −1,4 V. Erst wenn $U_E$ darunter fällt, kippt der Ausgang zurück. Zwischen den Schwellen hängt er von der Vorgeschichte ab: Die Kennlinie bildet eine __Hystereseschleife__ (Abbildung 6) mit der Breite 2,8 V, der __Hysterese__.

:::formel Formel
$$U_{R1,\max} = k\,U_{A,\max}$$
$$U_{R1,\min} = k\,U_{A,\min}$$
:::

**So liest man das:** Die Schwellen sind die Spannungen, die der Teiler aus den beiden Ausgangsgrenzen macht; die Hysterese ist $k$ mal der gesamte Ausgangshub. Mit $k$ = 0,1 und ±14 V liegen sie bei ±1,4 V, mit dem garantierten Mindesthub ±12 V bei ±1,2 V.

Idee der Herleitung: Bei festem Ausgang kippt die Schaltung dort, wo $U_D$ das Vorzeichen wechselt.

:::herleitung
**Ausgangspunkt:** die Masche über die Eingänge des Schmitt-Triggers: Der Pluseingang liegt auf $k U_A$, der Minuseingang auf $U_E$, also ist $U_D = k U_A - U_E$ (Skript S. 201).

**Annahmen:** (i) Der Ausgang liegt an einer seiner Grenzen (Abschnitt *Warum die Schaltung zur Ruhe kommt*). (ii) Der Teiler ist unbelastet. (iii) $U_E$ ändert sich langsam gegen den Kippvorgang, der einige 10 µs dauert.

**Schritt 1**: Ausgang oben:

$$U_D = k\,U_{A,\max} - U_E$$

**Schritt 2**: $U_D$ wechselt das Vorzeichen, wenn $U_E$ den Wert $k U_{A,\max}$ überschreitet; der Ausgang beginnt zu fallen, und die Mitkopplung treibt ihn bis $U_{A,\min}$.

**Schritt 3** (entscheidender Schritt): Im neuen Zustand gilt

$$U_D = k\,U_{A,\min} - U_E$$

An der eben überschrittenen Schwelle ist das $k$ mal der negative Ausgangshub, hier −2,8 V. Der neue Zustand ist stabil; ein Zurückkippen findet nicht statt.

**Schritt 4**: Zurück kippt der Ausgang erst, wenn $U_D$ wieder positiv wird, also wenn $U_E$ unter $k U_{A,\min}$ fällt.

**Ergebnis:**

$$U_{R1,\max} = k\,U_{A,\max}$$

$$U_{R1,\min} = k\,U_{A,\min}$$

**Woher die Faktoren kommen:** $k$ stammt aus dem Teiler, die Grenzen stammen aus dem OPV.

**Proben:** Einheit V. Zahlenwert: 0,1 · 14 V = 1,4 V. Grenzfall $k$ = 0: Beide Schwellen liegen bei null, die Schaltung ist ein Komparator ohne Hysterese. Das Skript erhält dieselben Schwellen (S. 202).

**Grenzen:** Die Schwellen sind nur so genau wie die Ausgangsgrenzen, die mit Last, Temperatur und Exemplar streuen.
:::

Wozu das Gedächtnis gut ist, zeigt ein verrauschtes Signal. Ein Komparator ohne Hysterese, der einen langsamen Sinus mit überlagertem Rauschen mit null vergleicht, schaltet an jedem Nulldurchgang viele Male hin und her, denn solange der Sinus durch das Rauschband läuft, kreuzt das Rauschen die Schwelle immer wieder. Der Schmitt-Trigger schaltet nur einmal: Um zurückzuschalten, müsste das Rauschen den Eingang bis unter die andere Schwelle drücken, um mehr als 2 V. Der Preis ist eine Verzögerung bis zum Erreichen der Schwelle.

::::beispiel Schmitt-Trigger an einem verrauschten Signal
**Gegeben:** invertierender Schmitt-Trigger mit $R_1$ = 10 kΩ und $R_2$ = 90 kΩ, Ausgangsgrenzen ±14 V; Eingang: Kosinus mit 3 V Amplitude und 50 Hz, dazu Rauschen mit 0,2 V Effektivwert, gleichmäßig verteilt bis 100 kHz.

**Gesucht:** Schwellen, Hysterese, Schaltzeitpunkt; Vergleich mit einem Komparator.

**Rechnung:**

$$U_{R1,\max} = 0{,}1\cdot 14\ \mathrm{V} = 1{,}4\ \mathrm{V}$$

$$U_{R1,\min} = 0{,}1\cdot(-14\ \mathrm{V}) = -1{,}4\ \mathrm{V}$$

Hysterese 2,8 V. Ohne Rauschen erreicht das Signal den Betrag 1,4 V beim Phasenwinkel

$$\arcsin\frac{1{,}4\ \mathrm{V}}{3\ \mathrm{V}} = 27{,}8°$$

nach dem Nulldurchgang, bei 20 ms Periode nach 1,55 ms. Mit dem Rauschen schaltet der Schmitt-Trigger früher, sobald Signal und Rauschen zusammen die Schwelle erreichen, in einer Simulation über 40 ms nach 0,9 bis 1,1 ms. Der ideale Komparator schaltet dort 43- bis 59-mal je Nulldurchgang, der Schmitt-Trigger genau einmal.

**Ergebnis:** **Schwellen ±1,4 V, Hysterese 2,8 V; ein sauberer Wechsel je Nulldurchgang, mit Rauschen 0,9 bis 1,1 ms nach dem Nulldurchgang.**

**Einordnung:** So gewinnt man aus verrauschten oder langsamen Signalen saubere Schaltflanken, etwa an den Eingängen von Digitalbausteinen.
::::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Differenz­verstärker | Nur die Differenz zählt; gemeinsame Störungen fallen als Gleichtakt heraus. |
| Komparator | Ohne Rückführung meldet die riesige Verstärkung nur das Vorzeichen der Differenz. |
| Ruhezustand, goldene Regeln | Rückführung gegen die Differenz: Der Ausgang lässt die Differenz verschwinden, die Widerstände bestimmen das Ergebnis. |
| Einschwingen | Jede Änderung des Ausgangs verkleinert bei Gegenkopplung ihre eigene Ursache. |
| Schmitt-Trigger | Rückführung mit der Differenz: Der Ausgang kippt an eine Grenze und bleibt dort. |

Ein Operationsverstärker verstärkt nur die Differenz seiner beiden Eingangsspannungen, und das so stark, dass er allein nur „größer“ oder „kleiner“ melden kann; erst die Rückführung der Ausgangsspannung macht ihn brauchbar: Wirkt sie der Differenz entgegen, regelt der Ausgang die Differenz praktisch auf null, und die äußeren Widerstände bestimmen das Ergebnis; verstärkt sie die Differenz, kippt der Ausgang an eine Grenze und bleibt dort.

## Bedeutung und Ausblick

Fast jede analoge Schaltung enthält gegengekoppelte OPVs, deren Ergebnis so genau ist wie ihre Widerstände; mitgekoppelte formen Schaltflanken. Die Grenzen des idealen Modells behandelt [Der reale Operationsverstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/realer-operationsverstaerker.html); als Nächstes berechnet [Die OPV-Grundschaltungen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/opv-grundschaltungen.html) mit den goldenen Regeln Verstärker, Addierer, Subtrahierer und Integrator.

**In der ausführlichen Fassung:** eine Messkette mit Vorverstärker, Schrot- und 1/f-Rauschen mit Formeln, das kT/C-Rauschen, der Differenzverstärker mit Widerstand im Fußpunkt und sein Eigenrauschen, wie ein OPV auf 200 000-fache Verstärkung kommt, der Flash-Wandler mit Beispiel, die Frequenzkompensation, der Vergleich mit einer Kompensationswaage und das Mehrfachschalten eines Komparators im Bild. [Zur ausführlichen Fassung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung-ausfuehrlich.html)

:::kern
- Rauschen beschreibt man durch Effektivwert und Rauschdichte; der Effektivwert wächst mit der Wurzel der Bandbreite, unabhängige Quellen addieren sich quadratisch.
- Thermisches Rauschen eines Widerstands: $|u_{r,R}|^2 = 4 k_B T R$, bei 10 kΩ 12,9 nV/√Hz. Verstärken allein verbessert das Signal-Rausch-Verhältnis nicht.
- Im Differenzverstärker hält die Stromquelle die Summe der Ströme fest; die Differenz der Eingänge verteilt sie, der Gleichtakt nicht. Verstärkung $v_u = -g_m R_C$.
- Der OPV verstärkt $U_D$ mit $v_D$ ≈ 200 000, linear aber nur in ±70 µV; ohne Rückkopplung ist er ein Komparator.
- Gegenkopplung: $A = v_D/(1 + k v_D) \approx 1/k$; die Widerstände bestimmen das Ergebnis.
- Die Gegenkopplung kommt zur Ruhe, weil sich der Ausgang mit endlicher Geschwindigkeit bewegt und jede Änderung ihre Ursache verkleinert; Zeitkonstante $1/(k\omega_T)$.
- Goldene Regeln: $U_D = 0$ nur bei Gegenkopplung im linearen Bereich; keine Eingangsströme beim idealen OPV immer.
- Mitkopplung kippt den Ausgang an eine Grenze; der Schmitt-Trigger schaltet bei $k U_{A,\max}$ und $k U_{A,\min}$ und hat ein Gedächtnis.
:::

:::quiz
F: Warum ändert eine Gleichtaktspannung die Kollektorströme des Differenzverstärkers nicht?
A: Die Stromquelle hält die Summe fest, und das Verhältnis hängt nur vom Unterschied der Basis-Emitter-Spannungen ab. Der gemeinsame Emitterknoten folgt der Gleichtaktspannung, so dass beide Basis-Emitter-Spannungen gleich bleiben.
F: Stimmt es, dass ein Verstärker das Signal-Rausch-Verhältnis verbessert?
A: Nicht durch das Verstärken: Er hebt Signal und vorhandenes Rauschen um denselben Faktor an und fügt eigenes Rauschen hinzu; er schützt nur gegen Rauschen, das erst hinter ihm hinzukommt. Besser wird das Verhältnis durch Begrenzen der Bandbreite.
F: Ein OPV mit der Leerlaufverstärkung 50 000 wird mit k = 0,1 gegengekoppelt. Wie groß ist die Verstärkung der Schaltung?
A: 50 000/(1 + 0,1 · 50 000) = 9,998, fast genau 1/k = 10.
F: Warum stellt sich in einer gegengekoppelten Schaltung U_D ≈ 0 ein, und warum schwingt sie dabei nicht hin und her?
A: Der Ausgang ändert sich mit einer Geschwindigkeit proportional zu U_D; jede Änderung verkleinert U_D über die Rückführung, bis der Ausgang steht, und das tut er nur bei U_D ≈ 0. Die Annäherung ist exponentiell, ohne Vorzeichenwechsel von U_D.
F: Stimmt es, dass beim virtuellen Kurzschluss ein Strom zwischen den Eingängen fließt?
A: Nein. Die Eingänge sind nicht verbunden und nehmen keinen Strom auf; die Spannung zwischen ihnen ist nur null, weil der Ausgang sie nachregelt. In der Sättigung ist sie es nicht mehr.
F: Warum hat der Schmitt-Trigger zwei verschiedene Schaltschwellen?
A: Der Pluseingang liegt auf k mal der Ausgangsspannung, und die hat zwei Werte; je nach Zustand liegt die Schwelle bei +1,4 V oder bei −1,4 V.
:::
