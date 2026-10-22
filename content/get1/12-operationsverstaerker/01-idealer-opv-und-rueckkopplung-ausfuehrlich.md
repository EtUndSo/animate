---
title: Der Operationsverstärker – idealer OPV und Rückkopplung
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Operationsverstärker
order: 120100
summary: Was ein Operationsverstärker ist, wie sein Differenzverstärker nur den Unterschied zweier Spannungen verstärkt und warum erst die Rückkopplung aus der riesigen Verstärkung eine berechenbare Schaltung macht: Rauschen und Signal-Rausch-Verhältnis, Differenzverstärker, idealer OPV und Komparator, Gegen- und Mitkopplung mit Einschwingen und Stabilität, Schmitt-Trigger. Ausführliche Fassung mit allen Herleitungen, den Rauschquellen im Einzelnen, dem Gleichtaktverhalten, dem Flash-Wandler und dem Kompensationskondensator.
tags: Operationsverstärker, OPV, idealer OPV, Differenzverstärker, virtueller Kurzschluss, Gegenkopplung
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Ein Sensor liefert oft nur Millivolt, und auf seiner Leitung liegen Störungen, die so groß sein können wie das Signal selbst. Schaltungen sollen solche Spannungen trotzdem genau verstärken, vergleichen und miteinander verrechnen, unabhängig davon, wie stark die Kennwerte der einzelnen Transistoren streuen. Das Bauteil dafür ist der __Operationsverstärker__, kurz OPV: eine integrierte Schaltung aus vielen Transistoren mit zwei Eingängen und einem Ausgang, die je nach äußerer Beschaltung addiert, subtrahiert, integriert oder vergleicht; daher der Name, nach den Rechenoperationen.

**Ein Operationsverstärker verstärkt nur die Differenz seiner beiden Eingangsspannungen, und das so stark, dass er allein nur „größer“ oder „kleiner“ melden kann; erst die Rückführung der Ausgangsspannung macht ihn brauchbar: Wirkt sie der Differenz entgegen (Gegenkopplung), regelt der Ausgang die Differenz praktisch auf null, und die äußeren Widerstände bestimmen das Ergebnis; verstärkt sie die Differenz (Mitkopplung), kippt der Ausgang an eine Grenze und bleibt dort.**

Vorausgesetzt werden die Transfergleichung des Bipolartransistors aus [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html), die Steilheit aus [Der Transistor als Verstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker.html), der Stromspiegel aus [Arbeitspunkt und Grundschaltungen des Transistors](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/arbeitspunkt-und-grundschaltungen.html), der Spannungsteiler aus [Zusammenschaltung von Widerständen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/zusammenschaltung-von-widerstaenden.html) und das Laden eines Kondensators aus [Laden und Entladen des Kondensators](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/laden-und-entladen.html). Darauf bauen [Die OPV-Grundschaltungen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/opv-grundschaltungen.html) und [Der reale Operationsverstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/realer-operationsverstaerker.html) auf.

:::grafik
Szene: get1/operationsverstaerker/01-opv-kennlinie · Vorlage: schaltung-und-kennlinie
**Abbildung 1:** (a) Schaltsymbol des Operationsverstärkers: links der nichtinvertierende Eingang (+) und der invertierende Eingang (−), dazwischen der Zählpfeil der Differenzspannung $U_D$ vom Plus- zum Minuseingang; rechts der Ausgang mit $U_A$ gegen Masse; oben und unten die Versorgung +15 V und −15 V. (b) Übertragungskennlinie des Beispiel-OPV (Art 741), $U_A$ über $U_D$ von −200 µV bis +200 µV: zwischen −70 µV und +70 µV eine Gerade mit der Steigung 200 000, außerhalb waagrecht bei +14 V bzw. −14 V; gestrichelt die Versorgung ±15 V. Proportional zur Differenz ist der Ausgang nur in einem Fenster von ±70 µV; außerhalb meldet er nur ihr Vorzeichen.
:::

## Rauschen und Signal-Rausch-Verhältnis

*Wie beschreibt man eine Störspannung, deren Verlauf sich nicht vorhersagen lässt, und wie vergleicht man sie mit einem Signal?*

:::grafik
Szene: get1/operationsverstaerker/01-rauschen · Vorlage: zeitverlauf-und-spektrum
**Abbildung 2:** (a) Rauschspannung eines 10-kΩ-Widerstands bei 300 K über 20 µs, gemessen mit 1 MHz Bandbreite: ein unregelmäßiges Zittern um null; waagrechte Linien bei ±12,9 µV, dem Effektivwert. (b) Rauschdichte in nV/√Hz über der Frequenz von 0,1 Hz bis 1 MHz, beide Achsen logarithmisch: beim Widerstand waagrecht bei 12,9 nV/√Hz; beim Beispiel-OPV waagrecht bei 23 nV/√Hz und unterhalb der Eckfrequenz 100 Hz ansteigend, bei 10 Hz auf 76 nV/√Hz, bei 1 Hz auf 231 nV/√Hz. Den Verlauf des Rauschens kann man nicht vorhersagen, seine Größe aber genau angeben: als Effektivwert und als Dichte über der Frequenz.
:::

Jeder Widerstand und jeder Transistor erzeugt an seinen Anschlüssen eine kleine, unregelmäßig schwankende Spannung, auch wenn von außen kein Strom fließt. Diese Störgröße heißt __Rauschen__. Man kann sie sich als Überlagerung sehr vieler Sinusschwingungen mit verschiedenen Frequenzen, zufälligen Amplituden und zufälligen Phasen vorstellen. Ihren Verlauf kann man deshalb nicht vorhersagen; er ist ein __Zufallsprozess__, und man beschreibt ihn mit Mittelwerten (Abbildung 2a).

Der zeitliche Mittelwert des Rauschens ist null; einen Gleichanteil zählt man nicht zum Rauschen. Ein brauchbares Maß ist der __Effektivwert__, die Wurzel aus dem Mittelwert des Quadrats:

$$U_\mathrm{eff} = \sqrt{\overline{u^2}}$$

$$\overline{u^2} = \frac{1}{T_m}\int_0^{T_m} u^2(t)\,dt$$

Dabei ist $T_m$ eine Mittelungszeit, lang gegen alle Schwankungen. Man definiert ihn so, weil eine Spannung $u$ an einem Widerstand $R$ die Leistung $u^2/R$ umsetzt: Der Effektivwert ist die Gleichspannung, die im Mittel dieselbe Leistung umsetzt. Ein Sinus mit 1 V Amplitude hat 0,707 V (Herleitungskasten unten, Schritt 3).

**Die Akteure:**

- __$u_r(t)$__: Rauschspannung, ihr Momentanwert; in V; Mittelwert null.
- __$U_r$__: ihr Effektivwert, im Skript $u_{r,\mathrm{eff}}$; in V; bei einem 10-kΩ-Widerstand, gemessen mit 1 MHz Bandbreite, 12,9 µV.
- __$|u_r(f)|^2$__: __spektrale Rauschdichte__, der Anteil am mittleren Quadrat der Rauschspannung, der auf ein Hertz Bandbreite in der Umgebung der Frequenz $f$ entfällt; in V²/Hz; beim 10-kΩ-Widerstand 1,66·10⁻¹⁶ V²/Hz. Datenblätter geben ihre Wurzel $|u_r(f)|$ in nV/√Hz an, hier 12,9 nV/√Hz. Das Skript nennt $|u_r(f)|^2$ Rauschspannungsdichte.

**Das Zusammenspiel:** Jede Sinuskomponente des Rauschens steuert zum mittleren Quadrat ihr eigenes mittleres Quadrat bei; Komponenten verschiedener Frequenzen beeinflussen einander dabei nicht, ihre Beiträge addieren sich. Deshalb kann man das mittlere Quadrat als Dichte auf die Frequenzachse verteilen und durch Aufsummieren über alle Frequenzen den Effektivwert zurückgewinnen (Skript S. 195, Gleichung 12.1):

:::formel Definition
$$U_r = \sqrt{\int_0^\infty |u_r(f)|^2\,df}$$
:::

**So liest man das:** Aus der Dichte über der Frequenz wird eine Spannung. Ist die Dichte in einem Band der Breite $\Delta f$ konstant und außerhalb null, bleibt die Wurzel aus Dichte mal Bandbreite:

$$U_r = |u_r|\,\sqrt{\Delta f}$$

Der Effektivwert wächst also mit der Wurzel der Bandbreite. Ein 10-kΩ-Widerstand rauscht im Hörbereich bis 20 kHz mit 1,82 µV, über 1 MHz mit 12,9 µV. Deshalb begrenzt man in Messschaltungen die Bandbreite auf das, was das Signal braucht.

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

**Unabhängige Quellen addieren sich quadratisch.** Dasselbe Argument gilt für zwei Rauschquellen, die nichts voneinander wissen, etwa zwei Widerstände oder einen Widerstand und einen Verstärker. Das Mittel des Produkts ihrer Spannungen ist dann null; es bleiben die mittleren Quadrate:

$$U_{r,\mathrm{ges}} = \sqrt{U_{r1}^2 + U_{r2}^2}$$

Ein OPV mit 23 nV/√Hz an einer Quelle mit 10 kΩ (12,9 nV/√Hz) rauscht zusammen mit 26,4 nV/√Hz, nicht mit 35,9. Die größere Quelle bestimmt das Ergebnis; die kleinere hebt es hier nur um 15 %.

Idee der Herleitung: Man quadriert die Summe der beiden Spannungen und mittelt.

:::herleitung
**Ausgangspunkt:** die Definition des Effektivwerts über das mittlere Quadrat.

**Annahmen:** (i) Die Quellen sind unabhängig: Der Wert der einen sagt nichts über den Wert der anderen. (ii) Beide haben den Mittelwert null.

**Schritt 1**: Quadrat der Summe:

$$(u_1 + u_2)^2 = u_1^2 + 2\,u_1 u_2 + u_2^2$$

**Schritt 2** (entscheidender Schritt): Bei unabhängigen Quellen ist der Mittelwert eines Produkts das Produkt der Mittelwerte, hier null mal null; der Mischterm verschwindet:

$$\overline{u_1 u_2} = 0$$

**Schritt 3**: Mitteln und Wurzel ziehen:

$$\sqrt{\overline{(u_1 + u_2)^2}} = \sqrt{\overline{u_1^2} + \overline{u_2^2}}$$

**Ergebnis:**

$$U_{r,\mathrm{ges}} = \sqrt{U_{r1}^2 + U_{r2}^2}$$

**Woher die Faktoren kommen:** Der Mischterm, der bei formgleichen, gleichphasigen Spannungen die einfache Summe ergäbe, verschwindet bei unabhängigen Quellen im Mittel.

**Proben:** Die Wurzel aus 23² + 12,87² ergibt 26,4, in nV/√Hz. Spezialfall: Zwei gleich große unabhängige Quellen ergeben das 1,41-fache einer einzelnen, nicht das Doppelte.

**Grenzen:** Stammen beide Anteile aus derselben Ursache, etwa eine Störung, die zwei Leitungen gleichzeitig erreicht, verschwindet der Mischterm nicht; solche Anteile addieren sich mit ihrem Vorzeichen. Genau das nutzt der Differenzverstärker.
:::

Ob Rauschen stört, hängt davon ab, wie groß das Signal daneben ist. Das __Signal-Rausch-Verhältnis__ (englisch signal-to-noise ratio, SNR) vergleicht die Leistungen, die Signal und Rauschen am selben Widerstand umsetzen; der Widerstand kürzt sich dabei heraus. Man vergleicht Leistungen, weil sich unabhängige Anteile in den Leistungen addieren. Da das Verhältnis viele Zehnerpotenzen umfassen kann, gibt man es meist logarithmisch in __Dezibel__ (dB) an, als zehnfachen Zehnerlogarithmus.

**Die Akteure:**

- __$U_S$__: Effektivwert des Signals; in V; im Beispiel unten 1 mV.

:::formel Definition
$$\mathrm{SNR} = \frac{U_S^2}{U_r^2}$$
$$\mathrm{SNR}_\mathrm{dB} = 10\,\lg\frac{U_S^2}{U_r^2}$$
:::

**So liest man das:** Je größer das Verhältnis, desto weniger fällt das Rauschen auf. Weil der Logarithmus eines Quadrats doppelt so groß ist wie der Logarithmus der Größe selbst, kann man auch mit $20\,\lg(U_S/U_r)$ rechnen: Ein Faktor 10 in der Spannung sind 20 dB, ein Faktor 2 sind 6 dB. Ein Signal von 1 mV liegt 54,8 dB über dem Rauschen eines 10-kΩ-Widerstands im Hörbereich, ein Signal von 10 µV nur 14,8 dB.

:::fehlvorstellung
„Wenn man das Nutzsignal verstärkt, wird das Signal-Rausch-Verhältnis besser.“ Das liegt nahe, weil das Signal danach größer ist, und das Skript schreibt es so (S. 195). Ein Verstärker hebt aber das Rauschen, das schon im Signal steckt, um denselben Faktor an und fügt sein eigenes hinzu; das Verhältnis an seinem Ausgang ist deshalb bei gleicher Bandbreite höchstens so gut wie an seinem Eingang. Im Beispiel unten (Abbildung 3) sinkt es durch einen OPV von 54,8 dB auf 48,6 dB. Verstärkung hilft gegen Rauschen, das erst hinter dem Verstärker hinzukommt, aus Kabeln, Folgestufen oder dem Analog-Digital-Umsetzer: Gegen eine Folgestufe mit 1 mV Eigenrauschen bleiben ohne Vorverstärker 0 dB, mit Vorverstärker 39,4 dB. Deshalb gehört der rauschärmste Verstärker an den Anfang einer Messkette; besser wird das Verhältnis außerdem, wenn man die Bandbreite auf die des Signals begrenzt.
:::

::::beispiel Signal-Rausch-Verhältnis einer Messkette mit und ohne Vorverstärker
:::grafik
Szene: get1/operationsverstaerker/01-messkette · Vorlage: blockschaltbild-pegel
**Abbildung 3:** Messkette als Blockschaltbild mit den Pegeln im Band bis 20 kHz. Oben: Sensor (Signal 1 mV, Innenwiderstand 10 kΩ, Rauschen 1,82 µV, SNR 54,8 dB) → Vorverstärker (eigenes Rauschen 3,25 µV auf den Eingang bezogen, Verstärkung 100; dahinter Signal 100 mV, Rauschen 373 µV, SNR 48,6 dB) → Folgestufe mit 1 mV Eigenrauschen (SNR 39,4 dB). Unten derselbe Weg ohne Vorverstärker: SNR 0 dB. Der Verstärker verschlechtert das Verhältnis an seiner Stelle, schützt das Signal aber vor dem Rauschen dahinter.
:::

**Gegeben:** Sensor mit 1 mV Signal (Effektivwert) und 10 kΩ Innenwiderstand bei 300 K; Bandbreite 20 kHz; Vorverstärker mit der Rauschdichte 23 nV/√Hz (wie der Beispiel-OPV) und der Verstärkung 100 im ganzen Band, also mit genügend Bandbreite (der 741 selbst käme mit hundertfacher Verstärkung nur bis 10 kHz); Folgestufe mit 1 mV Eigenrauschen (Effektivwert).

**Gesucht:** das SNR am Sensor, hinter dem Vorverstärker und hinter der Folgestufe, mit und ohne Vorverstärker.

**Rechnung:** Rauschen des Sensors und des Verstärkers, beide auf den Eingang bezogen:

$$U_{r1} = 12{,}87\ \frac{\mathrm{nV}}{\sqrt{\mathrm{Hz}}}\cdot\sqrt{20\ \mathrm{kHz}} = 1{,}82\ \mu\mathrm{V}$$

$$U_{r2} = 23\ \frac{\mathrm{nV}}{\sqrt{\mathrm{Hz}}}\cdot\sqrt{20\ \mathrm{kHz}} = 3{,}25\ \mu\mathrm{V}$$

Am Sensor:

$$\mathrm{SNR}_\mathrm{dB} = 20\,\lg\frac{1\ \mathrm{mV}}{1{,}82\ \mu\mathrm{V}} = 54{,}8\ \mathrm{dB}$$

Mit dem Verstärker, die beiden unabhängigen Anteile quadratisch addiert:

$$U_{r,\mathrm{ges}} = \sqrt{1{,}82^2 + 3{,}25^2}\ \mu\mathrm{V} = 3{,}73\ \mu\mathrm{V}$$

$$\mathrm{SNR}_\mathrm{dB} = 20\,\lg\frac{1\ \mathrm{mV}}{3{,}73\ \mu\mathrm{V}} = 48{,}6\ \mathrm{dB}$$

Nach der Verstärkung um 100 stehen 100 mV gegen 373 µV, weiterhin 48,6 dB. Die Folgestufe addiert 1 mV. Mit Vorverstärker:

$$\mathrm{SNR}_\mathrm{dB} = 20\,\lg\frac{100\ \mathrm{mV}}{\sqrt{0{,}373^2 + 1^2}\ \mathrm{mV}} = 39{,}4\ \mathrm{dB}$$

Ohne Vorverstärker trifft das Signal von 1 mV direkt auf das Rauschen von 1 mV:

$$\mathrm{SNR}_\mathrm{dB} = 20\,\lg\frac{1\ \mathrm{mV}}{\sqrt{0{,}00182^2 + 1^2}\ \mathrm{mV}} = 0{,}0\ \mathrm{dB}$$

**Ergebnis:** **Der Vorverstärker senkt das SNR von 54,8 dB auf 48,6 dB, hebt es gegen die Folgestufe aber von 0 dB auf 39,4 dB.**

**Einordnung:** Ohne Vorverstärker wäre das Signal so groß wie das Rauschen der Folgestufe; mit ihm ist es 94-mal größer. Besser als die 48,6 dB hinter dem Verstärker kann die Kette nicht werden.

**Variation:** Mit der Verstärkung 1000 statt 100 ergeben sich hinter der Folgestufe 48,3 dB; ihr Rauschen fällt dann kaum noch ins Gewicht, die Grenze setzt das Rauschen am Eingang.
::::

## Die Quellen des Rauschens

*Woher kommt das Rauschen, und wie groß ist es?*

Das Skript nennt vier Arten (S. 195–196): thermisches Rauschen, weißes Rauschen, Schrotrauschen und 1/f-Rauschen. Thermisches Rauschen und Schrotrauschen sind physikalische Mechanismen; „weiß“ und „1/f“ bezeichnen dagegen Formen des Spektrums, wie unten erklärt.

### Thermisches Rauschen

Die Leitungselektronen eines Widerstands bewegen sich ungeordnet und stoßen dabei ständig mit dem Kristallgitter zusammen. Im Mittel bewegen sich gleich viele in jede Richtung; in jedem Augenblick überwiegt aber zufällig die eine oder die andere. Dieser schwankende Nettostrom erzeugt an den Klemmen eine schwankende Spannung, ohne dass von außen ein Strom fließt: das __thermische Rauschen__.

**Die Akteure:**

- __$k_B$__: Boltzmann-Konstante, 1,380649·10⁻²³ J/K, im Skript $k$. Sie rechnet eine Temperatur in eine Energie um: Bei 300 K ist $k_B T$ = 4,14·10⁻²¹ J. Im thermischen Gleichgewicht steckt in jedem Energieterm, der quadratisch von einer Größe abhängt, im Mittel die Energie $k_B T/2$ (__Gleichverteilungssatz__, aus der kinetischen Gastheorie: $k_B T/2$ Bewegungsenergie je Raumrichtung eines Gasmoleküls).
- __$T$__: absolute Temperatur; 300 K. Sie treibt die ungeordnete Bewegung.
- __$R$__: Widerstandswert; je größer, desto höher die Rauschspannung.

:::formel Gesetz
$$|u_{r,R}(f)|^2 = 4\,k_B\,T\,R$$
:::

**So liest man das:** Die Dichte in V²/Hz ist proportional zu Temperatur und Widerstand und hängt nicht von der Frequenz ab; die Rauschspannung wächst nur mit der Wurzel: 1 kΩ rauscht mit 4,07 nV/√Hz, 10 kΩ mit 12,9 nV/√Hz, 1 MΩ mit 129 nV/√Hz. Woran die Elektronen stoßen, bestimmt nur den Wert von $R$; bei gegebenem $R$ hängt die Dichte allein von der Temperatur ab, wie die Herleitung zeigt. Das Skript führt die Unvorhersagbarkeit des Rauschens auch auf „unregelmäßige Gitterfehler“ zurück (S. 195); Gitterfehler sitzen aber fest, zufällig ist die Wärmebewegung. Irreführend ist dort auch „sporadisch“: Die Rauschspannung ist ständig vorhanden.

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

::::beispiel Rauschen von Widerständen im Hörbereich
**Gegeben:** Widerstände von 1 kΩ, 10 kΩ und 1 MΩ bei 300 K; Bandbreite 20 kHz (Hörbereich); $k_B$ = 1,380649·10⁻²³ J/K.

**Gesucht:** Rauschdichte und Effektivwert.

**Rechnung:** Dichte für 10 kΩ nach dem Gesetz des thermischen Rauschens:

$$|u_{r,R}|^2 = 4\cdot 1{,}380649\cdot10^{-23}\ \frac{\mathrm{J}}{\mathrm{K}}\cdot 300\ \mathrm{K}\cdot 10^4\ \Omega = 1{,}66\cdot10^{-16}\ \frac{\mathrm{V}^2}{\mathrm{Hz}}$$

Die Wurzel ist 12,87 nV/√Hz. Effektivwert über 20 kHz nach Gleichung 12.1 mit konstanter Dichte:

$$U_r = 12{,}87\ \frac{\mathrm{nV}}{\sqrt{\mathrm{Hz}}}\cdot\sqrt{20\,000\ \mathrm{Hz}} = 1{,}82\ \mu\mathrm{V}$$

Für 1 kΩ ergeben sich 0,58 µV, für 1 MΩ 18,2 µV: Hundertfacher Widerstand, zehnfache Rauschspannung.

**Ergebnis:** **1,82 µV bei 10 kΩ, 0,58 µV bei 1 kΩ, 18,2 µV bei 1 MΩ.**

**Einordnung:** Ein Signal von 1 mV liegt 54,8 dB über dem Rauschen des 10-kΩ-Widerstands, eines von 10 µV nur 14,8 dB. Hochohmige Quellen rauschen stärker; wer kleine Spannungen messen will, hält die Widerstände im Signalweg klein.

**Variation:** Gekühlt auf 77 K, die Temperatur von flüssigem Stickstoff, sinkt die Rauschspannung um den Faktor $\sqrt{77/300}$ = 0,507, beim 10-kΩ-Widerstand auf 0,92 µV.
::::

### Weißes Rauschen

Ein Spektrum mit gleicher Dichte bei allen Frequenzen heißt __weiß__, nach dem weißen Licht, das alle Farben gleich stark enthält. Das Skript führt weißes Rauschen als eigene Art neben dem thermischen auf (S. 195); „weiß“ beschreibt aber die Form eines Spektrums, keine Ursache. Thermisches Rauschen und Schrotrauschen sind weiß, 1/f-Rauschen ist es nicht. Die unendliche Gesamtleistung, die das Skript nennt, hat nur das idealisierte Modell, dessen Dichte bis zu beliebig hohen Frequenzen konstant bleibt.

:::frage
„Wenn weißes Rauschen bei allen Frequenzen gleich stark ist, ist seine Leistung dann nicht unendlich?“
Im Modell ja, in jeder realen Schaltung nein. Jede Schaltung hat Kapazitäten, die hohe Frequenzen kurzschließen, und begrenzt damit die Bandbreite. Wie der Herleitungskasten zum thermischen Rauschen zeigt (Schritt 1), bleibt an einer Kapazität $C$ insgesamt die Rauschspannung $\sqrt{k_B T/C}$, gleich wie groß der Widerstand ist: an 10 pF 20,4 µV, an 1 pF 64 µV. Ein größerer Widerstand rauscht stärker, aber in einer schmaleren Bandbreite, und beides hebt sich genau auf. Dieses __kT/C-Rauschen__ begrenzt jede Schaltung, die eine Spannung auf einem Kondensator festhält, etwa am Eingang eines Analog-Digital-Umsetzers.
:::

### Schrotrauschen

Muss ein Strom eine Potentialbarriere überwinden, etwa am pn-Übergang einer Diode oder eines Transistors ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html)), dann besteht er aus einzelnen Ladungsträgern, die die Barriere unabhängig voneinander überqueren. Wie viele es in einem kurzen Zeitabschnitt sind, schwankt zufällig um den Mittelwert, und mit ihnen schwankt der Strom. Diese Schwankung heißt __Schrotrauschen__.

**Die Akteure:**

- __$|i_r(f)|^2$__: Dichte des Stromrauschens; in A²/Hz.
- __$e$__: Elementarladung, 1,602·10⁻¹⁹ C; die Ladung, in deren Portionen der Strom fließt.
- __$I$__: mittlerer Strom über die Barriere.

$$|i_r(f)|^2 = 2\,e\,I$$

Die Schwankung wächst nur mit der Wurzel des Stroms. Bei 1 mA beträgt sie 17,9 pA/√Hz, über 20 kHz 2,5 nA, ein 400 000stel des Stroms; bei 1 nA sind es 0,25 %, bei 1 pA 8 %. Kleine Ströme, etwa die einer Fotodiode bei schwachem Licht, sind relativ am stärksten verrauscht.

Idee der Herleitung: Man zählt die Ladungsträger, die in einem Zeitfenster die Barriere überqueren; bei unabhängigen Ereignissen ist die Streuung der Anzahl so groß wie die Wurzel ihres Mittelwerts.

:::herleitung
**Ausgangspunkt:** die Statistik unabhängiger Ereignisse (Poisson-Statistik): Treten Ereignisse unabhängig voneinander mit fester mittlerer Rate auf, ist das mittlere Abweichungsquadrat ihrer Anzahl in einem Zeitfenster, die __Varianz__, gleich dem Mittelwert der Anzahl. Diese Eigenschaft geht über den Kurs hinaus und wird hier übernommen.

**Annahmen:** (i) Die Ladungsträger überqueren die Barriere unabhängig voneinander. (ii) Ein Messgerät mit der Bandbreite $\Delta f$ wirkt wie eine Mittelung über Zeitfenster der Länge $\tau_f = 1/(2\Delta f)$; auch das ist ein Ergebnis der Frequenzanalyse jenseits des Kurses. Der Kasten zeigt deshalb die Beweisidee.

**Schritt 1**: Mittlere Anzahl im Fenster:

$$\overline{N} = \frac{I\,\tau_f}{e}$$

**Schritt 2**: Der im Fenster gemittelte Strom ist die Ladung durch die Dauer; sein mittleres Abweichungsquadrat folgt aus der Varianz der Anzahl, die nach dem Ausgangspunkt gleich $\overline{N}$ ist:

$$\overline{\Delta i^2} = \Big(\frac{e}{\tau_f}\Big)^2\,\overline{N} = \frac{e\,I}{\tau_f}$$

**Schritt 3** (entscheidender Schritt): Fensterlänge durch die Bandbreite ausdrücken:

$$\overline{\Delta i^2} = 2\,e\,I\,\Delta f$$

**Ergebnis:**

$$|i_r(f)|^2 = 2\,e\,I$$

**Woher die Faktoren kommen:** $e$, weil der Strom in Portionen fließt; ein kontinuierlicher Ladungsfluss schwankte nicht. $I$ ist die Rate der Portionen. Die 2 stammt aus der Beziehung zwischen Fensterlänge und Bandbreite.

**Proben:** Einheit: C mal A ergibt A²·s = A²/Hz. Zahlenwert: Bei 1 mA und 25 µs Fensterlänge (20 kHz) überqueren im Mittel 1,56·10¹¹ Ladungsträger die Barriere; die relative Schwankung ist der Kehrwert der Wurzel daraus, 2,5·10⁻⁶, dasselbe wie 2,5 nA aus der Formel.

**Grenzen:** Ohne Barriere, im metallischen Leiter, sind die Elektronen nicht unabhängig, und das Schrotrauschen tritt nicht in voller Höhe auf.
:::

### 1/f-Rauschen

Bei tiefen Frequenzen kommt ein Anteil hinzu, dessen Dichte umgekehrt proportional zur Frequenz wächst, das __1/f-Rauschen__. Es entsteht durch verschiedene langsame Schwankungen, etwa wenn Störstellen an Oberflächen Ladungsträger einfangen und wieder freigeben und sich so die Zahl der freien Ladungsträger ändert (Skript S. 196). Die Frequenz, bei der es so groß wird wie der weiße Anteil, heißt __Eckfrequenz__ $f_c$: bei den besten rauscharmen OPVs 1 bis 10 Hz, bei Universal-OPVs bis etwa 100 Hz, bei CMOS-OPVs oft mehrere Kilohertz, wozu die „bis 10 kHz“ des Skripts passen.

**Die Akteure:**

- __$|u_w|$__: Dichte des weißen Anteils, beim Beispiel-OPV 23 nV/√Hz; das Datenblatt gibt diesen Wert bei 1 kHz an, er wird hier näherungsweise als weißer Anteil genommen.
- __$f_c$__: Eckfrequenz; für den Beispiel-OPV angenommen 100 Hz.

Mit diesen beiden Größen lautet die Dichte, als Modell:

$$|u_r(f)|^2 = |u_w|^2\,\Big(1 + \frac{f_c}{f}\Big)$$

Bei 1 Hz ergibt das 231 nV/√Hz, bei 1 kHz 24 nV/√Hz (Abbildung 2b). Jede Frequenzdekade trägt dabei gleich viel 1/f-Rauschen bei, gleich wo sie liegt:

$$\int_{f_1}^{10 f_1} |u_w|^2\,\frac{f_c}{f}\,df = |u_w|^2\,f_c\,\ln 10$$

Von 0,1 Hz bis 1 Hz kommt also so viel 1/f-Rauschen wie von 100 Hz bis 1000 Hz, beim Beispiel-OPV je 349 nV. Für Gleichspannungsmessungen, die lange mitteln, ist es deshalb die Hauptquelle.

Idee der Herleitung: Das Integral von $1/f$ ist der Logarithmus, und der Logarithmus eines festen Verhältnisses hängt nicht von der Lage ab.

:::herleitung
**Ausgangspunkt:** Gleichung 12.1, angewandt auf den 1/f-Anteil des Modells.

**Annahmen:** (i) Die Dichte des 1/f-Anteils ist exakt proportional zu $1/f$. (ii) Betrachtet wird eine Dekade, von $f_1$ bis $10 f_1$.

**Schritt 1**: Integral des 1/f-Anteils über die Dekade:

$$\int_{f_1}^{10 f_1} |u_w|^2\,\frac{f_c}{f}\,df = |u_w|^2\,f_c\,\Big[\ln f\Big]_{f_1}^{10 f_1}$$

**Schritt 2** (entscheidender Schritt): Die Differenz zweier Logarithmen ist der Logarithmus des Quotienten; $f_1$ kürzt sich heraus:

$$\ln(10 f_1) - \ln f_1 = \ln 10$$

**Ergebnis:**

$$\int_{f_1}^{10 f_1} |u_w|^2\,\frac{f_c}{f}\,df = |u_w|^2\,f_c\,\ln 10$$

**Woher die Faktoren kommen:** $\ln 10$ ist der Logarithmus des Frequenzverhältnisses einer Dekade; $|u_w|^2 f_c$ ist die Stärke des 1/f-Anteils.

**Proben:** Einheit: V²/Hz mal Hz ergibt V². Zahlenwert: 23 nV/√Hz mal der Wurzel aus 100 Hz · 2,303 ergibt 349 nV je Dekade.

**Grenzen:** Streng genommen wüchse das Rauschen zu immer tieferen Frequenzen ohne Grenze weiter: Jede Dekade fügt dem mittleren Quadrat (349 nV)² hinzu, der Effektivwert wächst mit der Wurzel aus der Zahl der Dekaden. Praktisch begrenzt die Messdauer die tiefste erfasste Frequenz.
:::

::::beispiel Rauschen des Beispiel-OPV bei tiefen und hohen Frequenzen
**Gegeben:** Beispiel-OPV mit dem weißen Anteil 23 nV/√Hz und der Eckfrequenz 100 Hz (Modell oben).

**Gesucht:** der Effektivwert von 0,1 Hz bis 10 Hz und von 1 kHz bis 20 kHz, jeweils mit und ohne 1/f-Anteil.

**Rechnung:** Gleichung 12.1 mit dem Modell; das Integral über den weißen Anteil ist Dichte mal Bandbreite, das über den 1/f-Anteil der Logarithmus des Frequenzverhältnisses:

$$U_r = |u_w|\,\sqrt{(f_2 - f_1) + f_c\,\ln\frac{f_2}{f_1}}$$

Von 0,1 Hz bis 10 Hz:

$$U_r = 23\ \frac{\mathrm{nV}}{\sqrt{\mathrm{Hz}}}\cdot\sqrt{9{,}9\ \mathrm{Hz} + 100\ \mathrm{Hz}\cdot\ln 100} = 499\ \mathrm{nV}$$

Ohne 1/f-Anteil wären es 72 nV. Von 1 kHz bis 20 kHz ergeben sich 3,20 µV gegen 3,17 µV ohne 1/f-Anteil.

**Ergebnis:** **Unter 10 Hz rauscht der OPV fast siebenmal stärker, als sein weißer Anteil allein erwarten ließe; von 1 kHz bis 20 kHz erhöht der 1/f-Anteil das Rauschen um 0,8 %, im ganzen Hörbereich ab 20 Hz um 1,7 %.**

**Einordnung:** Wer Gleichspannungen oder sehr langsame Signale misst, etwa mit einer Waage oder einem Thermometer, kämpft mit dem 1/f-Rauschen; dafür gibt es OPVs mit Eckfrequenzen um 1 Hz. Im Audiobereich zählt fast nur der weiße Anteil.
::::

## Der Differenzverstärker

*Wie baut man eine Schaltung, die nur auf den Unterschied zweier Spannungen antwortet und auf den Anteil, den beide gemeinsam haben, gar nicht?*

Liegt eine Störung auf einer Signalleitung und in gleicher Größe auf einer zweiten, parallel geführten Leitung, etwa eingestreutes Netzbrummen oder das Rauschen einer gemeinsamen Versorgung, dann steckt die Information im Unterschied der beiden Leitungen. Der __Differenzverstärker__ verstärkt genau diesen Unterschied (Skript S. 196–197). Er ist die Eingangsstufe jedes Operationsverstärkers; Abbildung 4a zeigt ihn mit den Werten des Beispiels. Das Skript schreibt dazu, das verstärkte Nutzsignal führe zu besseren SNR-Werten (S. 196); besser wird das Verhältnis hier, weil das gemeinsame Rauschen herausfällt, nicht durch die Verstärkung.

:::grafik
Szene: get1/operationsverstaerker/01-differenzverstaerker · Vorlage: schaltung-und-kennlinie
**Abbildung 4:** (a) Differenzverstärker nach Skript Bild 12.1 mit Werten, abweichend vom Skript mit dem Emitter von Q3 an −15 V statt an Masse, damit die Eingänge um 0 V liegen dürfen: zwei gleiche npn-Transistoren Q1 und Q2 (Beispieltransistor, Art BC547C) mit je einem Kollektorwiderstand $R_C$ = 10 kΩ an +15 V; die Emitter verbunden und über eine Stromquelle von 1 mA (Transistor Q3) an −15 V; die Eingänge $U_{e1}$ und $U_{e2}$ an den Basen, der Ausgang $U_A$ zwischen den Kollektoren, Zählpfeil vom Kollektor von Q1 zum Kollektor von Q2. Ruhewerte bei gleichen Eingängen auf 0 V: je 0,499 mA, Kollektoren auf 10,0 V, Emitterknoten auf −0,635 V. (b) Die Kollektorströme $I_{C1}$ und $I_{C2}$ über $U_{e1} - U_{e2}$ von −150 mV bis +150 mV: zwei gegenläufige S-Kurven, die sich bei 0 mV und 0,5 mA kreuzen und zusammen stets 1 mA ergeben; gestrichelt die Tangente im Nullpunkt mit der Steigung 9,67 mS; markiert die Werte bei ±100 mV, 98 % und 2 %. Die Stromquelle hält die Summe fest, die Differenz der Eingänge verteilt sie.
:::

**Die Akteure:**

- __$U_{e1}$__, __$U_{e2}$__: Eingangsspannungen an den Basen von Q1 und Q2, gegen Masse; in V.
- __$I_0$__: Strom der Stromquelle im gemeinsamen Emitterzweig, dem __Fußpunkt__, im Skript $I_{Q3}$; 1 mA. Er treibt beide Transistoren und begrenzt ihre Summe.
- __$\varphi_E$__: Potential des gemeinsamen Emitterknotens; in Ruhe −0,635 V.
- __$I_{C1}$__, __$I_{C2}$__: Kollektorströme; in Ruhe je 0,499 mA.
- __$R_C$__: Kollektorwiderstände, 10 kΩ an +15 V; sie machen aus den Strömen die Kollektorpotentiale $U_{a1}$ und $U_{a2}$, in Ruhe 10,0 V.
- __$U_A$__: Ausgangsspannung zwischen den Kollektoren, die Differenz $U_{a1} - U_{a2}$; in Ruhe 0.
- __$U_{Gl}$__: __Gleichtaktspannung__, der Mittelwert der beiden Eingänge, also der Anteil, den beide gemeinsam haben:

$$U_{Gl} = \frac{U_{e1} + U_{e2}}{2}$$

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Q3 arbeitet als Stromquelle, wie der Ausgangstransistor eines Stromspiegels ([Arbeitspunkt und Grundschaltungen des Transistors](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/arbeitspunkt-und-grundschaltungen.html), Abschnitt *Der Stromspiegel*): Er führt 1 mA, weitgehend unabhängig von der Spannung an ihm. Alles, was oben durch Q1 und Q2 fließt, muss unten durch Q3; die Summe der beiden Emitterströme liegt damit fest.

**Schritt 2**: Beide Emitter hängen am selben Knoten. Die Basis-Emitter-Spannungen sind deshalb $U_{e1} - \varphi_E$ und $U_{e2} - \varphi_E$ und unterscheiden sich genau um $U_{e1} - U_{e2}$. Nach der Transfergleichung ([Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html), Abschnitt *Der Transistoreffekt*) legt dieser Unterschied das Verhältnis der Kollektorströme fest: Je 25,85 mV, die $U_{e1}$ höher liegt, führt Q1 das 2,72-fache des Stroms von Q2.

:::grafik
Szene: get1/operationsverstaerker/01-gleichtakt · Vorlage: schaltung-zustaende
**Abbildung 5:** Der Differenzverstärker aus Abbildung 4 in drei Zuständen nebeneinander, beide Eingänge jeweils auf derselben Spannung: −5 V, 0 V und +5 V. Der Emitterknoten liegt auf −5,633 V, −0,635 V und +4,363 V, folgt den Eingängen also im Abstand der Basis-Emitter-Spannung. Die Kollektorströme bleiben in allen drei Zuständen bei 0,499 mA (Änderung 0,01 %), die Ausgangsspannung bei 0. Der Emitterknoten folgt dem Gleichtakt; die Basis-Emitter-Spannungen und damit die Ströme bleiben.
:::

**Schritt 3**: Summe fest, Verhältnis durch die Differenz bestimmt: Damit liegen beide Ströme fest, und sie hängen nur von $U_{e1} - U_{e2}$ ab. Hebt man beide Eingänge gemeinsam an, steigt der Emitterknoten um denselben Betrag mit, und beide Basis-Emitter-Spannungen bleiben, wie sie sind (Abbildung 5). Bei +5 V an beiden Eingängen liegt der Knoten auf 4,363 V statt auf −0,635 V, die Ströme ändern sich um 0,01 %, der Ausgang bleibt bei null. Die Gleichtaktspannung erreicht den Ausgang nicht.

**Schritt 4**: Kleine Differenzen: Ändert sich nur $U_{e1}$ um einen kleinen Betrag, bewegt sich der Emitterknoten um die Hälfte mit, im vollständigen Modell um 0,4998 der Änderung. Denn was Q1 an Strom gewinnt, muss Q2 verlieren, und das verlangt gleich große, entgegengesetzte Änderungen der beiden Basis-Emitter-Spannungen. Jeder Transistor bekommt also die halbe Differenz. Mit der Steilheit $g_m$ = 19,3 mS je Transistor ändern sich die Kollektorströme um die halbe Steilheit mal der Differenz, gegenläufig, und zwischen den Kollektoren erscheint die Differenz 193-fach.

**Schritt 5**: Große Differenzen: Bei ±100 mV fließen schon 98 % des Stroms durch einen Transistor; mehr als den Strom der Stromquelle kann er nicht übernehmen. Der Differenzverstärker wird zum __Stromschalter__, und die Ausgangsspannung nähert sich ±10 V, dem Produkt aus $R_C$ und 1 mA (Abbildung 4b). Gleichmäßig verstärkt er nur Differenzen, die klein gegen $2U_T$ sind, also gegen 52 mV.

:::fehlvorstellung
„Der Differenzverstärker löscht auch das Rauschen seiner Transistoren aus.“ Das liegt nahe, weil er Störungen unterdrückt, die an beiden Eingängen ankommen. Herausfallen kann aber nur, was an beiden Eingängen gleich ist. Das Eigenrauschen jedes Transistors und jedes Kollektorwiderstands entsteht unabhängig vom anderen; es wirkt wie eine Differenz und wird verstärkt wie ein Signal. Weil sich unabhängige Quellen quadratisch addieren (Abschnitt *Rauschen und Signal-Rausch-Verhältnis*), rauscht ein Differenzverstärker sogar um den Faktor 1,41 stärker als eine einzelne Emitterschaltung mit demselben Strom je Transistor. Er unterdrückt gemeinsame Störungen wie Brummen auf beiden Leitungen oder Schwankungen der Versorgung, nicht das Eigenrauschen.
:::

Die Stromaufteilung als Formel:

:::formel Formel
$$I_{C1} = \frac{I_0}{1 + \exp\big(-(U_{e1} - U_{e2})/U_T\big)}$$
:::

**So liest man das:** Bei gleichen Eingängen teilt sich der Strom je zur Hälfte. Bei 25,85 mV Differenz führt Q1 73 %, bei 100 mV 98 %, bei −100 mV 2 %; $I_{C2}$ ist jeweils der Rest bis $I_0$. Die Gleichtaktspannung kommt in der Formel nicht vor: Die Aufteilung hängt nur von der Differenz ab.

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

ergibt sich die __Differenzverstärkung__ der Stufe. Das Skript nennt sie $A$; hier heißt sie wie in [Der Transistor als Verstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker.html) $v_u$:

:::formel Formel
$$v_u = \frac{U_A}{U_{e1} - U_{e2}} = -g_m\,R_C$$
:::

**So liest man das:** Der Differenzverstärker verstärkt wie eine Emitterschaltung, nur teilen sich zwei Transistoren die Differenz: Jeder bekommt die Hälfte, und der Ausgang zwischen den Kollektoren sieht beide Änderungen. Der Betrag ist der Spannungsabfall an einem Kollektorwiderstand durch $U_T$, hier 4,99 V durch 25,85 mV, also 193. Das Minuszeichen sagt, dass $U_A$ sinkt, wenn $U_{e1}$ steigt: $U_{e1}$ wirkt invertierend, $U_{e2}$ nichtinvertierend. Nimmt man den Ausgang nur an einem Kollektor gegen Masse ab, halbiert sich der Betrag.

Das Skript erhält $A = -2SR$ (S. 197), im Beispiel −387, weil es die ganze Signaländerung an $U_{BE1}$ ansetzt; der gemeinsame Emitterknoten wandert aber um die Hälfte mit (Schritt 4). Auch die „Größenordnung 10 000“ (S. 197) erreicht diese Stufe nicht: Ihre Verstärkung ist $U_{RC}/U_T$, und weil der Spannungsabfall an $R_C$ unter der Versorgung bleibt, sind es an 15 V weniger als 580. Gleichung 12.3 schließlich schreibt die Verstärkung positiv; bezogen auf $U_{e1} - U_{e2}$ ist sie negativ, wie das Skript selbst mit $-2SR$ erhält.

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
**Gegeben:** Versorgung ±15 V, $R_C$ = 10 kΩ, ideale Stromquelle mit 1 mA im Fußpunkt, zwei Beispieltransistoren (Art BC547C, $B$ = 500, Early-Spannung 70 V, wie in [Der Transistor als Verstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker.html)); $U_T$ = 25,85 mV.

**Gesucht:** (a) Ruhewerte und Verstärkung, (b) die Wirkung einer Gleichtaktspannung von +5 V, (c) die Stromaufteilung bei 100 mV Differenz.

**Rechnung:** (a) Je Zweig fließt der halbe Emitterstrom abzüglich des Basisstroms; das vollständige Modell ergibt 0,499 mA. Steilheit und Verstärkung:

$$g_m = \frac{0{,}499\ \mathrm{mA}}{25{,}85\ \mathrm{mV}} = 19{,}3\ \mathrm{mS}$$

$$v_u = -19{,}3\ \mathrm{mS}\cdot 10\ \mathrm{k}\Omega = -193$$

Die Kollektoren liegen auf 15 V − 4,99 V = 10,0 V, der Emitterknoten auf −0,635 V. Mit Early-Effekt ergibt das vollständige Modell −182.

(b) Beide Eingänge auf +5 V: Der Emitterknoten steigt auf 4,363 V; die Kollektorströme ändern sich von 0,49907 mA auf 0,49901 mA, um 0,012 %; $U_A$ bleibt 0.

(c) 100 mV Differenz:

$$\frac{I_{C1}}{I_0} = \frac{1}{1 + \exp(-100\ \mathrm{mV}/25{,}85\ \mathrm{mV})} = 0{,}980$$

**Ergebnis:** **Verstärkung −193 (−182 mit Early-Effekt); +5 V Gleichtakt ändern die Ströme um 0,01 %; bei 100 mV Differenz führt Q1 98 % des Stroms.**

**Einordnung:** Ein Millivolt Differenz verschiebt den Ausgang um 0,19 V, fünf Volt Gleichtakt verschieben ihn gar nicht. Mit 100 mV ist die Stufe schon ganz übersteuert; als Verstärker arbeitet sie nur mit Differenzen von wenigen Millivolt.
::::

:::frage
„Reicht im Fußpunkt nicht ein Widerstand statt des dritten Transistors?“
Für den Ausgang zwischen den Kollektoren ja, solange die Schaltung genau symmetrisch ist: Beide Ströme ändern sich dann gleich, ihre Differenz bleibt null. Am einzelnen Kollektor nicht: Mit 14,4 kΩ nach −15 V ändert 1 V Gleichtakt den Fußpunktstrom um rund 7 % und das Potential eines Kollektors um 0,35 V. Eine Differenz wirkt dort 90,5-fach, der Gleichtakt −0,35-fach; das Verhältnis, 262 oder 48 dB, heißt __Gleichtaktunterdrückung__. Die Stromquelle hält den Fußpunktstrom fest und macht die Unterdrückung um Größenordnungen besser; welche Werte reale OPVs erreichen, steht in [Der reale Operationsverstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/realer-operationsverstaerker.html).
:::

:::frage
„Die Stufe verstärkt 193-fach. Wie kommt ein OPV auf 200 000?“
Mit Widerständen als Last bleibt die Verstärkung unter $U_{RC}/U_T$, an 15 V unter 580. Integrierte OPVs ersetzen die Kollektorwiderstände deshalb durch einen Stromspiegel. Für Gleichstrom lässt er den Ruhestrom durch, ohne viel Spannung zu verbrauchen; für Änderungen wirkt er wie ein sehr großer Widerstand, der Ausgangswiderstand der Transistoren aus dem Early-Effekt ([Der Transistor als Verstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker.html), Abschnitt *Die realen Kennlinien*). Mit dem Beispieltransistor ergäbe das rund 1500-fache Verstärkung in einer Stufe. Der 741 erreicht seine 200 000 mit einer solchen Eingangsstufe, einer zweiten Verstärkerstufe und einem Emitterfolger als Ausgang.
:::

## Der ideale Operationsverstärker

*Welche Eigenschaften hat ein OPV, und welche Idealisierungen erlauben einfaches Rechnen?*

Im OPV folgen auf den Differenzverstärker weitere Verstärkerstufen und ein Emitterfolger als Ausgang; zusammen erreichen sie Verstärkungen von 10⁵ bis 10⁶ (Skript S. 197). Für das Beschalten genügt das Verhalten an den Anschlüssen (Abbildung 1a): zwei Eingänge, ein Ausgang und zwei Versorgungsanschlüsse, die man im Schaltbild oft weglässt. Der __nichtinvertierende Eingang__ (+) entspricht $U_{e2}$ des Differenzverstärkers: Steigt seine Spannung, steigt der Ausgang. Der __invertierende Eingang__ (−) entspricht $U_{e1}$: Steigt seine Spannung, sinkt der Ausgang. Als Beispiel dient ein OPV nach Art des verbreiteten 741 an ±15 V.

**Die Akteure:**

- __$U_{e+}$__, __$U_{e-}$__: Spannungen am nichtinvertierenden und am invertierenden Eingang, gegen Masse; in V.
- __$U_D$__: __Differenzspannung__, die Spannung vom Plus- zum Minuseingang; in V; im linearen Betrieb höchstens ±70 µV:

$$U_D = U_{e+} - U_{e-}$$

- __$v_D$__: __Leerlaufverstärkung__, die Verstärkung der Differenzspannung ohne äußere Beschaltung; beim 741 typisch 200 000, garantiert mindestens 50 000.
- __$U_A$__: Ausgangsspannung gegen Masse; begrenzt auf den Bereich von $U_{A,\min}$ bis $U_{A,\max}$, beim 741 an ±15 V typisch −14 V bis +14 V, garantiert ±12 V.

:::formel Definition
$$U_A = v_D\,U_D$$
:::

**So liest man das:** Der Ausgang ist die verstärkte Differenzspannung, solange das Ergebnis zwischen den Ausgangsgrenzen liegt; sonst bleibt er an der Grenze. Die Grenzen liegen etwa 1 V unter den Versorgungsspannungen, weil zwischen Ausgang und Versorgung Transistoren liegen, an denen Spannung abfällt (Skript S. 199). Proportional ist der Ausgang deshalb nur in einem schmalen Fenster der Differenzspannung:

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

Wie schmal dieses Fenster ist, zeigt ein Vergleich. Die Eingangstransistoren eines OPV sind nie ganz gleich; der Unterschied wirkt wie eine kleine Spannungsquelle am Eingang, die __Offsetspannung__. Beim 741 beträgt sie typisch 1 mV und liegt damit 14-mal so weit vom Nullpunkt wie der Rand des Fensters. Selbst mit verbundenen Eingängen läge der Ausgang deshalb an einer Grenze. Dazu ist die Leerlaufverstärkung nur nach unten garantiert und hängt von Temperatur und Frequenz ab (Skript S. 198). Als Verstärker lässt sich der OPV ohne Rückkopplung nicht betreiben.

::::beispiel Linearer Bereich des Beispiel-OPV
**Gegeben:** Beispiel-OPV (Art 741) an ±15 V: Ausgangsgrenzen typisch ±14 V; Leerlaufverstärkung typisch 200 000, mindestens 50 000; Offsetspannung typisch 1 mV.

**Gesucht:** die Breite des linearen Fensters und ihr Vergleich mit der Offsetspannung.

**Rechnung:**

$$\frac{14\ \mathrm{V}}{200\,000} = 70\ \mu\mathrm{V}$$

$$\frac{14\ \mathrm{V}}{50\,000} = 280\ \mu\mathrm{V}$$

Die Offsetspannung ist 14,3-mal so groß wie die Fenstergrenze von 70 µV.

**Ergebnis:** **Linear ist der OPV nur zwischen −70 µV und +70 µV (garantiert ±280 µV); die Offsetspannung von 1 mV liegt weit außerhalb.**

**Einordnung:** Schon das thermische Rauschen eines 10-kΩ-Widerstands über 1 MHz Bandbreite, 12,9 µV, beträgt fast ein Fünftel der Fenstergrenze von 70 µV. Ohne Rückkopplung ist der Ausgang eines OPV nicht in der Mitte zu halten.
::::

Die Eigenschaften des idealen OPV nach dem Skript (S. 198), mit den Folgen beim Rechnen und den Werten des Beispiel-OPV:

| Eigenschaft des idealen OPV und Folge | Beispiel-OPV (741 an ±15 V) |
|---|---|
| Eingangswiderstand unendlich: In die Eingänge fließt kein Strom. | 2 MΩ; Eingangsruhestrom 80 nA |
| Leerlaufverstärkung unendlich und frequenzunabhängig: Mit Gegenkopplung wird $U_D$ null. | 200 000, mindestens 50 000; oberhalb von 5 Hz fallend, bei 1 MHz nur noch 1 |
| Ausgangswiderstand null: Der Ausgang liefert jeden Strom, den die Schaltung verlangt. | Kurzschlussstrom 25 mA |
| kein Rauschen | 23 nV/√Hz |

Die Idealisierung trägt, weil die Abweichungen klein gegen das sind, was die äußere Schaltung bewirkt. Durch den Eingangswiderstand fließen bei 25 µV Differenzspannung nur 12,5 pA; maßgeblich ist beim 741 der Eingangsruhestrom von 80 nA, und auch der ist gegen die 50 µA im Spannungsteiler des Rückkopplungsbeispiels (5 V an 100 kΩ) klein, 0,16 %. Wo sie doch zählen, behandelt [Der reale Operationsverstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/realer-operationsverstaerker.html).

## Der Komparator und der Flash-Wandler

*Was leistet ein OPV ohne Rückführung des Ausgangs?*

Weil schon 70 µV den Ausgang an eine Grenze treiben, meldet ein unbeschalteter OPV nur, welcher Eingang höher liegt. Legt man an den Pluseingang eine Spannung $U_1$ und an den Minuseingang eine Vergleichsspannung $U_2$ (Skript Bild 12.3), dann zeigt der Ausgang +14 V, sobald $U_1$ um mehr als 70 µV höher liegt, und −14 V, sobald es um mehr als 70 µV tiefer liegt. Eine solche Schaltung heißt __Komparator__ (Vergleicher). Ihre Kennlinie ist eine Stufe an der Stelle, an der $U_1$ und $U_2$ gleich sind (Skript Bild 12.4); genau betrachtet ist sie eine sehr steile Gerade in einem Fenster von 140 µV (Abbildung 1b). Im Idealfall springt der Ausgang auf die Versorgungsspannungen; real bleibt er darunter, beim 741 um etwa 1 V.

Eine Anwendung, die gerade dieses Schalten nutzt, ist der __Flash-Wandler__, ein Analog-Digital-Umsetzer (Skript Bild 12.5). Ein Spannungsteiler aus gleichen Widerständen erzeugt aus einer Referenzspannung $U_{Ref}$ eine Reihe von Schwellen, und an jeder Schwelle vergleicht ein Komparator die Eingangsspannung $U_E$. Alle Komparatoren, deren Schwelle unter $U_E$ liegt, zeigen „hoch“; ihre Anzahl ist der Messwert (Abbildung 6 im Beispiel unten). Für $n$ Bit braucht man $2^n - 1$ Komparatoren; üblich sind $2^n$ gleiche Widerstände, dann liegt der $m$-te Abgriff von unten auf

$$U_m = \frac{m}{2^n}\,U_{Ref}$$

Das Skript (Bild 12.5) kommt mit einem Widerstand weniger aus und legt den obersten Komparator direkt an $U_{Ref}$; dann liegen die Schwellen bei $m/(2^n - 1)$ mal $U_{Ref}$. Alle Komparatoren vergleichen gleichzeitig; deshalb ist der Wandler so schnell wie ein einzelner Komparator. Der Preis ist die Zahl der Komparatoren, 255 für 8 Bit und 1023 für 10 Bit. Flash-Wandler stehen deshalb dort, wo es auf Geschwindigkeit ankommt und wenige Bit genügen.

Idee der Herleitung: Spannungsteilerregel für eine Kette gleicher Widerstände.

:::herleitung
**Ausgangspunkt:** die Spannungsteilerregel für unbelastete Reihenschaltungen ([Zusammenschaltung von Widerständen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/zusammenschaltung-von-widerstaenden.html)).

**Annahmen:** (i) $2^n$ gleiche Widerstände $R$ zwischen $U_{Ref}$ und Masse; (ii) die Komparatoreingänge nehmen keinen Strom auf, der Teiler ist unbelastet.

**Schritt 1**: Durch die Kette fließt überall derselbe Strom:

$$I = \frac{U_{Ref}}{2^n\,R}$$

**Schritt 2** (entscheidender Schritt): Unter dem $m$-ten Abgriff liegen $m$ Widerstände; an ihnen fällt die Spannung des Abgriffs ab:

$$U_m = m\,R\,I$$

**Ergebnis:**

$$U_m = \frac{m}{2^n}\,U_{Ref}$$

**Woher die Faktoren kommen:** $m/2^n$ ist der Anteil der Widerstände, die unter dem Abgriff liegen.

**Proben:** Einheit V. Mit 2 V und 2 Bit: 0,5 V, 1,0 V, 1,5 V. Grenzfall $m = 2^n$: der obere Anschluss, $U_{Ref}$.

**Grenzen:** Ziehen die Komparatoreingänge Strom, verschieben sich die Schwellen; ungleiche Widerstände verschieben sie ebenfalls.
:::

::::beispiel Flash-Wandler mit 2 Bit
:::grafik
Szene: get1/operationsverstaerker/01-flash-wandler · Vorlage: schaltung
**Abbildung 6:** 2-Bit-Flash-Wandler: vier gleiche Widerstände von 1 kΩ zwischen $U_{Ref}$ = 2 V und Masse, Abgriffe auf 1,5 V, 1,0 V und 0,5 V an den Minuseingängen dreier Komparatoren; die Eingangsspannung $U_E$ = 1,2 V liegt an allen Pluseingängen. Die Ausgänge, von oben nach unten: −14 V, +14 V, +14 V, beschriftet als 0, 1, 1. Darunter die vier Bereiche 0–0,5 V, 0,5–1,0 V, 1,0–1,5 V und 1,5–2 V mit den Binärwerten 00 bis 11, markiert der Bereich 1,0–1,5 V. Die Zahl der Komparatoren, die „hoch“ zeigen, ist der Messwert.
:::

**Gegeben:** $U_{Ref}$ = 2 V, vier gleiche Widerstände (2 Bit), drei ideale Komparatoren; Eingangsspannung $U_E$ = 1,2 V.

**Gesucht:** die Schwellen, die Ausgänge der Komparatoren und der Messwert.

**Rechnung:** Schwellen nach der Teilerregel:

$$U_m = \frac{m}{4}\cdot 2\ \mathrm{V} = 0{,}5\ \mathrm{V};\ 1{,}0\ \mathrm{V};\ 1{,}5\ \mathrm{V}$$

1,2 V liegen über 0,5 V und 1,0 V, aber unter 1,5 V: Zwei Komparatoren zeigen +14 V, einer −14 V.

**Ergebnis:** **Zwei Komparatoren sind „hoch“; der Messwert ist 2, binär 10, also 1,0 V bis 1,5 V.**

**Einordnung:** Die Auflösung ist die Stufe von 0,5 V; jedes Bit mehr halbiert sie und verdoppelt fast die Zahl der Komparatoren. Mit 8 Bit und 2 V wären es 7,8 mV Stufe und 255 Komparatoren.
::::

## Rückkopplung: Gegen- und Mitkopplung

*Was ändert sich, wenn ein Teil der Ausgangsspannung an einen Eingang zurückgeführt wird?*

:::grafik
Szene: get1/operationsverstaerker/01-gegen-mit · Vorlage: schaltung-zustaende
**Abbildung 7:** Zwei Schaltungen aus denselben Bauteilen: Beispiel-OPV, $R_2$ = 90 kΩ vom Ausgang zum Teilerknoten, $R_1$ = 10 kΩ vom Teilerknoten nach Masse. Links Gegenkopplung: Teilerknoten am Minuseingang, Eingangsspannung $U_E$ am Pluseingang; darunter die Wirkungskette „$U_A$ steigt → Minuseingang steigt um ein Zehntel davon → $U_D$ sinkt → $U_A$ steigt langsamer“. Rechts Mitkopplung, der invertierende Schmitt-Trigger nach Skript Bild 12.6: Teilerknoten am Pluseingang, $U_E$ am Minuseingang; Wirkungskette „$U_A$ steigt → Pluseingang steigt → $U_D$ steigt → $U_A$ steigt schneller“. Welcher Eingang das zurückgeführte Signal bekommt, entscheidet, ob die Schaltung regelt oder kippt.
:::

Eine __Rückkopplung__ führt einen Teil der Ausgangsgröße auf den Eingang zurück (Skript S. 200). Beim OPV entscheidet der Eingang über die Wirkung. Geht die Rückführung auf den invertierenden Eingang, wirkt eine Zunahme des Ausgangs der Differenzspannung entgegen, die sie verursacht hat; das ist __Gegenkopplung__. Geht sie auf den nichtinvertierenden Eingang, vergrößert eine Zunahme des Ausgangs ihre eigene Ursache; das ist __Mitkopplung__. Das Skript spricht von gegenphasiger und phasenrichtiger Rückführung; gemeint ist dasselbe. Abbildung 7 zeigt beide mit denselben Bauteilen. Die linke Schaltung heißt nichtinvertierender Verstärker, die rechte Schmitt-Trigger; beide Namen erklären sich unten.

:::frage
„Woran erkennt man in einer Schaltung, ob sie gegen- oder mitgekoppelt ist?“
Man verfolgt eine kleine Erhöhung des Ausgangs durch die Rückführung. Kommt sie am Minuseingang an und senkt so $U_D$, ist die Kopplung gegen; kommt sie am Pluseingang an und hebt $U_D$, ist sie mit. Ein Widerstandsteiler gibt das Vorzeichen unverändert weiter. Enthält der Rückführungsweg selbst ein invertierendes Glied, etwa eine weitere invertierende Verstärkerstufe, kehrt sich die Zuordnung um; maßgeblich ist immer, ob die Rückführung $U_D$ verkleinert oder vergrößert.
:::

### Der Ruhezustand

*Welche Ausgangsspannung stellt sich bei Gegenkopplung ein, und warum hängt sie kaum vom OPV ab?*

**Die Akteure:**

- __$R_1$__, __$R_2$__: Spannungsteiler; $R_2$ = 90 kΩ vom Ausgang zum Teilerknoten, $R_1$ = 10 kΩ vom Teilerknoten nach Masse.
- __$k$__: __Rückkopplungsfaktor__, der Anteil der Ausgangsspannung, der am Teilerknoten ankommt; hier 0,1. Weil in den Eingang des OPV kein Strom fließt, ist der Teiler unbelastet:

$$k = \frac{R_1}{R_1 + R_2}$$

- __$U_E$__: Eingangsspannung der Schaltung, gegen Masse, am Pluseingang.
- __$A$__: Verstärkung der beschalteten Schaltung, das Verhältnis von $U_A$ zu $U_E$; so heißt sie im Skript ab Abschnitt 12.5.

**Das Zusammenspiel:** Der Minuseingang liegt auf $k U_A$. Die Differenzspannung ist deshalb der Unterschied zwischen dem, was am Eingang verlangt wird, und dem, was vom Ausgang zurückkommt:

$$U_D = U_E - k\,U_A$$

Ist $U_A$ zu klein, ist $U_D$ positiv und treibt den Ausgang nach oben; ist $U_A$ zu groß, ist $U_D$ negativ und zieht ihn nach unten. Zugleich verlangt der OPV, dass $U_A$ das $v_D$-fache von $U_D$ ist. Beides zusammen legt den Ruhezustand fest:

:::formel Formel
$$A = \frac{U_A}{U_E} = \frac{v_D}{1 + k\,v_D}$$
$$U_D = \frac{U_E}{1 + k\,v_D}$$
:::

**So liest man das:** Das Produkt $k\,v_D$ heißt __Schleifenverstärkung__; so stark wird eine Änderung verstärkt, die einmal durch OPV und Teiler läuft. Ist sie groß gegen 1, kürzt sich $v_D$ heraus, und es bleibt ein Ergebnis, das nur die Widerstände enthalten:

$$A \approx \frac{1}{k} = 1 + \frac{R_2}{R_1}$$

Hier ist das 10. Mit 200 000 ergibt sich genauer 9,9995, mit 50 000 noch 9,998: Ein Viertel der Leerlaufverstärkung ändert das Ergebnis um 0,015 %. Die Differenzspannung wird dabei winzig, bei 5 V am Ausgang 25 µV.

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

**Gesucht:** (a) die Verstärkung mit beiden Leerlaufverstärkungen und die Differenzspannung bei 5 V am Ausgang; (b) was bei 2 V am Eingang geschieht.

**Rechnung:** (a) Rückkopplungsfaktor und Schleifenverstärkung:

$$k = \frac{10\ \mathrm{k}\Omega}{10\ \mathrm{k}\Omega + 90\ \mathrm{k}\Omega} = 0{,}1$$

$$A = \frac{200\,000}{1 + 0{,}1\cdot 200\,000} = 9{,}9995$$

$$A = \frac{50\,000}{1 + 0{,}1\cdot 50\,000} = 9{,}9980$$

Bei 5 V am Ausgang braucht der OPV die Differenzspannung 5 V / 200 000 = 25 µV.

(b) Mit 2 V am Eingang verlangt die Schaltung 20 V am Ausgang; der Ausgang bleibt bei 14 V stehen. Die Differenzspannung ist dann nicht mehr klein:

$$U_D = 2\ \mathrm{V} - 0{,}1\cdot 14\ \mathrm{V} = 0{,}6\ \mathrm{V}$$

**Ergebnis:** **(a) A = 9,9995 bzw. 9,998, $U_D$ = 25 µV; (b) der Ausgang sättigt bei 14 V, und zwischen den Eingängen liegen 0,6 V.**

**Einordnung:** Eine Änderung der Leerlaufverstärkung um 75 % ändert die Verstärkung der Schaltung um 0,015 %, also 5000-mal weniger; dieser Faktor ist genau $1 + k v_D$ mit dem kleineren $v_D$. In der Sättigung (b) liegt zwischen den Eingängen 24 000-mal mehr Spannung als im Normalbetrieb.
::::

:::frage
„Wenn $U_D$ null ist, muss dann nicht auch $U_A = v_D U_D$ null sein?“
$U_D$ ist nicht genau null, sondern so klein, dass man es beim Rechnen vernachlässigen darf: 25 µV bei 5 V Ausgang. Mit 200 000 multipliziert ergeben gerade diese 25 µV die 5 V. Im idealen Modell geht $U_D$ gegen null und $v_D$ gegen unendlich; ihr Produkt bleibt endlich, und die Rückführung legt es fest. Deshalb rechnet man bei Gegenkopplung nicht mit der Gleichung des OPV, sondern mit $U_D$ = 0 und den Gleichungen der äußeren Schaltung.
:::

### Warum die Schaltung zur Ruhe kommt

*Warum läuft die gegengekoppelte Schaltung in diesen Ruhezustand, und warum verlässt die mitgekoppelte ihn?*

:::grafik
Szene: get1/operationsverstaerker/01-einschwingen · Vorlage: zeitverlauf
**Abbildung 8:** (a) Gegenkopplung mit $k$ = 0,1: Die Eingangsspannung springt bei $t$ = 0 von 0 auf 10 mV. Oben $U_A$ über $t$ von 0 bis 12 µs: exponentieller Anstieg auf 0,1 V, nach 1,59 µs bei 63 %, nach 11 µs auf 0,1 % am Endwert, ohne Überschwingen; die Anfangssteigung 63 mV/µs als gestrichelte Tangente. Darunter $U_D$ über derselben Zeitachse, logarithmisch: von 10 mV auf 5,8 µV nach 12 µs fallend, der Endwert 0,5 µV gestrichelt. (b) Mitkopplung (Schmitt-Trigger mit $U_E$ = 0) aus einer Anfangsabweichung von 0,13 mV am Ausgang, Zeitachse 0 bis 50 µs: $U_A$ wächst exponentiell mit derselben Zeitkonstante, ab etwa 0,8 V linear mit der größten Anstiegsgeschwindigkeit des 741, 0,5 V/µs, und erreicht 13 V nach 38 µs; gestrichelt der rein exponentielle Verlauf ohne diese Grenze, 13 V nach 18 µs. Gegenkopplung lässt jede Abweichung abklingen, Mitkopplung lässt sie mit derselben Zeitkonstante wachsen.
:::

Die Rechnung oben setzt voraus, dass sich nichts mehr ändert. Ob die Schaltung dorthin kommt, entscheidet eine Eigenschaft, die im idealen Modell fehlt: Ein realer OPV kann seinen Ausgang nicht springen lassen. In seinem Inneren lädt die Eingangsstufe einen Kondensator mit einem Strom, der proportional zu $U_D$ ist; deshalb ändert sich der Ausgang mit einer Geschwindigkeit, die proportional zu $U_D$ ist.

**Die Akteure:**

- __$f_T$__: __Transitfrequenz__ des OPV, die Frequenz, bei der seine Verstärkung auf 1 gefallen ist; im Datenblatt als Verstärkungs-Bandbreite-Produkt angegeben; beim 741 1 MHz.
- __$\omega_T$__: die zugehörige Kreisfrequenz $2\pi f_T$; 6,28·10⁶ 1/s. Sie gibt an, wie schnell der Ausgang einer Differenzspannung folgt: 1 mV lässt ihn um 6,28 V je Millisekunde steigen.
- __$\tau$__: Zeitkonstante des Einschwingens; in s.

:::formel Formel
$$\frac{dU_A}{dt} = \omega_T\,U_D$$
:::

**So liest man das:** Solange $U_D$ positiv ist, steigt der Ausgang, solange es negativ ist, fällt er; still steht er nur bei $U_D$ = 0. Doppelte Differenzspannung bedeutet doppelte Anstiegsgeschwindigkeit. Die Gleichung gilt, solange $U_D$ klein bleibt und die Geschwindigkeit unter der Grenze des OPV, beim 741 0,5 V/µs.

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

:::frage
„Warum baut man einen Kondensator ein, der den OPV langsam macht?“
Ohne ihn hätte der OPV mehrere innere Verzögerungen ähnlicher Größe. Eine starke Gegenkopplung käme dann mit ihrer Korrektur zu spät, der Ausgang schösse über und könnte dauerhaft schwingen. Der Kondensator macht eine einzige Verzögerung so groß, dass alle anderen daneben kaum zählen; dann verhält sich der OPV wie im Modell oben, und eine Gegenkopplung über einen Spannungsteiler kommt ohne Schwingen zur Ruhe. Diese __Frequenzkompensation__ kostet Geschwindigkeit: Der 741 verstärkt bei 1 MHz nur noch einfach. Mehr dazu in [Der reale Operationsverstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/realer-operationsverstaerker.html).
:::

**Das Zusammenspiel in Schritten** (Gegenkopplung wie in Abbildung 7 links; die Eingangsspannung springt von 0 auf 10 mV):

**Schritt 1**: Im ersten Moment ist $U_A$ noch null, also ist $U_D$ gleich der ganzen Eingangsspannung, 10 mV. Der Ausgang beginnt mit 63 mV/µs zu steigen.

**Schritt 2**: Mit $U_A$ steigt die zurückgeführte Spannung am Minuseingang; $U_D$ wird kleiner und der Anstieg langsamer, je näher $U_A$ dem Wert $U_E/k$ = 0,1 V kommt.

**Schritt 3**: Der Ausgang schießt nicht über: Umkehren könnte er erst, wenn $U_D$ das Vorzeichen wechselt, und null wird $U_D$ erst, wenn der Ausgang angekommen ist.

**Schritt 4**: Die Abweichung vom Endwert nimmt in gleichen Zeitabschnitten um gleiche Faktoren ab, wie die Spannung eines Kondensators, der sich über einen Widerstand lädt. Die Zeitkonstante ist 1,59 µs: Nach 1,59 µs fehlen noch 37 %, nach 11 µs noch 0,1 % (Abbildung 8a).

**Schritt 5**: Still steht der Ausgang erst, wenn $U_D$ null ist. Darum regelt die Gegenkopplung die Differenzspannung auf null; mit der endlichen Leerlaufverstärkung bleibt der Rest $U_A/v_D$, hier 0,5 µV. Beim realen OPV liegt zwischen den Eingängen zusätzlich seine Offsetspannung.

Bei der Mitkopplung (Abbildung 7 rechts) steht in derselben Rechnung das andere Vorzeichen, denn dort ist $U_D = k U_A - U_E$. Liegt $U_A$ ein wenig über dem Ruhewert, ist $U_D$ positiv, und der Ausgang steigt weiter, umso schneller, je weiter er sich entfernt. Die Abweichung wächst exponentiell, mit derselben Zeitkonstante von 1,59 µs, bis der Ausgang an eine Grenze stößt. Aus 0,13 mV werden so in 18 µs 13 V; weil der 741 seinen Ausgang höchstens um 0,5 V/µs ändern kann, dauert es 38 µs (Abbildung 8b). Der Ruhezustand der Mitkopplung existiert also, aber jede noch so kleine Abweichung entfernt den Ausgang von ihm; er ist __instabil__.

Für die Gegenkopplung lautet der Verlauf nach einem Sprung der Eingangsspannung, mit der Zeitkonstante $\tau$:

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

::::beispiel Einschwingen eines Verstärkers mit dem Rückkopplungsfaktor 0,1
**Gegeben:** Gegenkopplung mit $k$ = 0,1 (10 kΩ und 90 kΩ); Beispiel-OPV mit $f_T$ = 1 MHz und höchstens 0,5 V/µs; Sprung der Eingangsspannung von 0 auf 10 mV.

**Gesucht:** Zeitkonstante, Anfangssteigung und die Zeit bis auf 0,1 % am Endwert; zum Vergleich die Mitkopplung mit denselben Bauteilen.

**Rechnung:**

$$\tau = \frac{1}{0{,}1\cdot 2\pi\cdot 1\ \mathrm{MHz}} = 1{,}59\ \mu\mathrm{s}$$

Anfangssteigung, mit der ganzen Eingangsspannung als $U_D$:

$$\frac{dU_A}{dt}\Big|_{t=0} = 6{,}28\cdot10^6\ \frac{1}{\mathrm{s}}\cdot 10\ \mathrm{mV} = 62{,}8\ \frac{\mathrm{mV}}{\mu\mathrm{s}}$$

Das liegt unter der Grenze von 0,5 V/µs. Auf 0,1 % genau ist der Ausgang, wenn die Exponentialfunktion auf ein Tausendstel gefallen ist:

$$t = \tau\,\ln 1000 = 1{,}59\ \mu\mathrm{s}\cdot 6{,}91 = 11{,}0\ \mu\mathrm{s}$$

Der Endwert ist 99,995 mV, die Differenzspannung fällt von 10 mV auf 0,5 µV. Mitgekoppelt wächst eine Abweichung von 0,13 mV auf 13 V in

$$t = \tau\,\ln\frac{13\ \mathrm{V}}{0{,}13\ \mathrm{mV}} = 1{,}59\ \mu\mathrm{s}\cdot 11{,}5 = 18{,}3\ \mu\mathrm{s}$$

mit der Anstiegsgrenze des 741 in 38 µs (Simulation).

**Ergebnis:** **$\tau$ = 1,59 µs; nach 11 µs ist der Ausgang auf 0,1 % bei 0,1 V; mitgekoppelt wächst eine Abweichung von 0,13 mV in 18 µs auf 13 V, mit Anstiegsgrenze in 38 µs.**

**Einordnung:** Beide Vorgänge laufen mit derselben Zeitkonstante ab; nur das Vorzeichen der Rückkopplung entscheidet, ob die Abweichung schrumpft oder wächst.

**Variation:** Wird der ganze Ausgang zurückgeführt, $k$ = 1, sinkt $\tau$ auf 0,16 µs; die Grenze von 80 mV für lineares Verhalten bleibt, denn sie hängt nicht von $k$ ab.
::::

Das Skript erklärt das Einschwingen als Folge von Zyklen (S. 202): Der Ausgang springt jeweils auf $v_D U_D$, $U_D$ wechselt das Vorzeichen, und sein Betrag werde von Zyklus zu Zyklus kleiner. Rechnet man dieses Bild durch, geschieht das Gegenteil: Mit $k$ = 0,1, $v_D$ = 200 000 und 0,5 V am Eingang springt der Ausgang auf 100 000 V, dann auf −2·10⁹ V. Die Abweichung wächst je Zyklus um den Faktor −20 000, das Negative der Schleifenverstärkung, beim invertierenden Verstärker des Skripts mit denselben Widerständen ebenso. Ein springender Ausgang käme nur bei einer Schleifenverstärkung unter 1 zur Ruhe, also gerade dann nicht, wenn die Gegenkopplung wirken soll. Die Schaltung kommt zur Ruhe, weil sich ihr Ausgang stetig bewegt, ohne dass $U_D$ das Vorzeichen wechselt.

:::analogie
Eine elektronische Präzisionswaage arbeitet nach demselben Prinzip, der Kraftkompensation: Ein Sensor misst die Neigung des Waagebalkens, eine Regelung treibt Strom durch eine Spule, deren Kraft den Balken in die Waagerechte zurückdrückt. Im Ruhezustand ist die Neigung praktisch null, und der Spulenstrom ist das Messergebnis; wie empfindlich der Sensor und wie stark die Regelung ist, geht nicht ein, nur die Kraft der Spule je Ampere.

| Im Vergleich | In der Schaltung |
|---|---|
| Neigung des Balkens | Differenzspannung $U_D$ |
| Regelung | OPV mit $v_D$ |
| Spulenstrom, die Anzeige | Ausgangsspannung $U_A$ |
| Kraft der Spule je Ampere | Rückkopplungsfaktor $k$ |
| Gewicht auf der Schale | Eingangsspannung $U_E$ |
| Spule drückt gegen die Neigung | Gegenkopplung |
| Spule drückt in Richtung der Neigung, der Balken kippt an den Anschlag | Mitkopplung |

**Wo der Vergleich nicht stimmt:** Der Balken hat eine Masse und kann deshalb überschwingen; der OPV im Modell oben ändert seinen Ausgang nur, solange $U_D$ nicht null ist, und schwingt nicht über. Außerdem vergleicht die Waage Kräfte, der OPV Spannungen.
:::

### Die goldenen Regeln

*Mit welchen zwei Regeln berechnet man gegengekoppelte Schaltungen, und wann gelten sie nicht?*

Aus den beiden vorigen Abschnitten folgen die __goldenen Regeln__, mit denen man gegengekoppelte Schaltungen mit idealem OPV berechnet: Die Differenzspannung ist null, weil die Gegenkopplung den Ausgang so lange verstellt, bis sie es ist; und in die Eingänge fließt kein Strom, weil ihr Widerstand unendlich ist. Das Skript macht die erste ab Abschnitt 12.5 zur ständigen Annahme (S. 203). In Abbildung 7 links muss dann der Teilerknoten auf $U_E$ liegen, $k U_A$ also gleich $U_E$ sein, und $A = 1/k$ folgt ohne jede Rechnung mit $v_D$. Den Zustand nennt man auch __virtuellen Kurzschluss__: Die Eingänge liegen auf gleichem Potential, als wären sie verbunden, ohne es zu sein.

:::merke
**Die erste goldene Regel gilt nur bei Gegenkopplung und nur, solange der Ausgang nicht an einer Grenze liegt.** Bei Mitkopplung und in der Sättigung ist $U_D$ nicht null; die zweite Regel, keine Eingangsströme, gilt beim idealen OPV in jedem Betrieb.
:::

:::fehlvorstellung
„Virtueller Kurzschluss heißt, dass die Eingänge leitend verbunden sind und Strom zwischen ihnen fließen kann.“ Das liegt am Namen und daran, dass die Spannung zwischen ihnen null ist wie bei einem Kurzschluss. Tatsächlich sind die Eingänge nicht verbunden; bei 25 µV fließen durch den Eingangswiderstand von 2 MΩ 12,5 pA, und der Ruhestrom von rund 80 nA, den jeder Eingang des 741 aufnimmt, fließt in den OPV hinein, nicht von einem Eingang zum anderen. Null ist die Spannung nur, weil der Ausgang sie über die Rückführung ständig nachregelt. Hört die Regelung auf, weil der Ausgang an einer Grenze liegt, erscheint die Spannung wieder: Im Beispiel zum Ruhezustand liegen bei 2 V Eingangsspannung 0,6 V zwischen den Eingängen.
:::

## Der Schmitt-Trigger

*Wozu taugt eine mitgekoppelte Schaltung, und warum hat sie ein Gedächtnis?*

:::grafik
Szene: get1/operationsverstaerker/01-schmitt-kennlinie · Vorlage: kennlinie-hysterese
**Abbildung 9:** Übertragungskennlinie des invertierenden Schmitt-Triggers aus Abbildung 7 rechts ($k$ = 0,1, Ausgangsgrenzen ±14 V): $U_A$ über $U_E$ von −3 V bis +3 V. Von links kommend liegt der Ausgang auf +14 V und springt bei $U_E$ = +1,4 V senkrecht auf −14 V; von rechts kommend bleibt er auf −14 V und springt erst bei −1,4 V zurück auf +14 V. Pfeile zeigen die Laufrichtung; gestrichelt dazwischen die Gerade der instabilen Ruhezustände mit der Steigung 10. Zwischen −1,4 V und +1,4 V hängt der Ausgang davon ab, von welcher Seite der Eingang kam.
:::

Abbildung 7 rechts zeigt den __invertierenden Schmitt-Trigger__ (Skript S. 201, Bild 12.6): Die Eingangsspannung liegt am Minuseingang, der Spannungsteiler führt ein Zehntel der Ausgangsspannung auf den Pluseingang. Wie im vorigen Abschnitt gezeigt, verlässt sein Ausgang jeden Zustand dazwischen; er liegt immer an einer Grenze, bei +14 V oder bei −14 V. Weil der Pluseingang dem Ausgang folgt, verschiebt jeder Wechsel die Schwelle, an der der nächste Wechsel stattfindet.

:::frage
„Warum bleibt ein Schmitt-Trigger beim Einschalten nicht bei 0 V stehen, wenn sein Eingang auf 0 V liegt?“
Rechnerisch ist ein Ausgang von 0 V bei 0 V Eingangsspannung ein Ruhezustand, wie das Skript schreibt (S. 201): $U_D$ ist null, nichts ändert sich. Dieser Zustand ist aber instabil, wie das labile Gleichgewicht der Mechanik. Jede noch so kleine Abweichung wächst mit der Zeitkonstante 1,59 µs (Abschnitt *Warum die Schaltung zur Ruhe kommt*), und Abweichungen gibt es immer: die Offsetspannung von typisch 1 mV und selbst ohne sie das Rauschen der Widerstände, 12,9 µV bei 10 kΩ und 1 MHz Bandbreite. Aus diesen 12,9 µV am Pluseingang, 0,13 mV am Ausgang, werden nach 38 µs 13 V. Welche Grenze der Ausgang erreicht, entscheidet das Vorzeichen der ersten Abweichung. Der Satz des Skripts, für 0 V Eingangsspannung verändere sich nichts, gilt deshalb nur für den rechnerischen Zustand, nicht für eine reale Schaltung.
:::

**Die Akteure:**

- __$U_{R1,\max}$__, __$U_{R1,\min}$__: obere und untere __Schaltschwelle__, die Eingangsspannungen, bei denen der Ausgang kippt; benannt wie im Skript nach der Spannung an $R_1$ bei den beiden Ausgangsgrenzen; hier +1,4 V und −1,4 V.
- Dazu $k$, $U_{A,\max}$ und $U_{A,\min}$ wie oben.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Der Ausgang liege bei +14 V. Der Pluseingang liegt dann auf einem Zehntel davon, 1,4 V. Solange $U_E$ darunter bleibt, ist $U_D$ positiv, und der Ausgang bleibt oben.

**Schritt 2**: Steigt $U_E$ über 1,4 V, wird $U_D$ negativ, und der Ausgang beginnt zu fallen. Mit ihm sinkt der Pluseingang, $U_D$ wird noch negativer: Die Mitkopplung beschleunigt den Wechsel, bis der Ausgang bei −14 V ankommt.

**Schritt 3**: Jetzt liegt der Pluseingang auf −1,4 V, und bei 1,4 V Eingangsspannung ist $U_D$ gleich −2,8 V, weit von null entfernt. Eine Eingangsspannung zwischen −1,4 V und +1,4 V ändert nichts mehr; erst unter −1,4 V wird $U_D$ positiv, und der Ausgang kippt zurück.

**Schritt 4**: Zwischen den Schwellen hängt der Ausgang davon ab, von welcher Seite der Eingang kam: Die Schaltung hat ein Gedächtnis. Die Kennlinie läuft auf verschiedenen Wegen hin und zurück, eine __Hystereseschleife__ (Abbildung 9); ihre Breite, die __Hysterese__, beträgt hier 2,8 V.

:::formel Formel
$$U_{R1,\max} = k\,U_{A,\max}$$
$$U_{R1,\min} = k\,U_{A,\min}$$
:::

**So liest man das:** Die Schwellen sind die Spannungen, die der Teiler aus den beiden Ausgangsgrenzen macht. Ein größerer Rückkopplungsfaktor rückt sie weiter auseinander; die Hysterese ist $k$ mal der gesamte Ausgangshub. Mit $k$ = 0,1 und ±14 V liegen die Schwellen bei ±1,4 V, mit dem garantierten Mindesthub von ±12 V bei ±1,2 V. Weil die Ausgangsgrenzen streuen, streuen auch die Schwellen.

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

:::grafik
Szene: get1/operationsverstaerker/01-schmitt-rauschen · Vorlage: zeitverlauf
**Abbildung 10:** Eingang und Ausgänge über 40 ms. Oben die Eingangsspannung, ein Kosinus mit 3 V Amplitude und 50 Hz, dem Rauschen mit 0,2 V Effektivwert überlagert ist, gleichmäßig verteilt bis 100 kHz; waagrecht gestrichelt 0 V und ±1,4 V. In der Mitte der Ausgang eines idealen, beliebig schnellen invertierenden Komparators mit der Schwelle 0 V: an jedem der vier Nulldurchgänge ein Bündel von 43 bis 59 Umschaltungen innerhalb von 0,6 bis 0,8 ms. Unten der Ausgang des Schmitt-Triggers mit den Schwellen ±1,4 V: genau ein Wechsel je Nulldurchgang, 0,9 bis 1,1 ms danach, früher als die 1,55 ms (27,8°) ohne Rauschen, weil eine Rauschspitze die Schwelle zuerst erreicht. Eine Hysterese, die größer ist als das Rauschen, verhindert das Mehrfachschalten.
:::

Wozu das Gedächtnis gut ist, zeigt ein verrauschtes Signal (Abbildung 10). Ein Komparator ohne Hysterese, der einen langsamen Sinus mit überlagertem Rauschen mit null vergleicht, schaltet an jedem Nulldurchgang viele Male hin und her: Solange der Sinus durch das Rauschband läuft, kreuzt das Rauschen die Schwelle immer wieder. Der Schmitt-Trigger schaltet nur einmal. Um zurückzuschalten, müsste das Rauschen den Eingang bis unter die andere Schwelle drücken, im Moment des Wechsels um mindestens 2,25 V, das 11-fache seines Effektivwerts. So gewinnt man aus verrauschten oder langsamen Signalen saubere Schaltflanken, etwa an den Eingängen von Digitalbausteinen. Der Preis ist eine Verzögerung: Er schaltet erst, wenn Signal und Rauschen zusammen die Schwelle von 1,4 V erreichen, im Beispiel 0,9 bis 1,1 ms nach dem Nulldurchgang.

::::beispiel Schaltschwellen eines Schmitt-Triggers an einem verrauschten Signal
**Gegeben:** invertierender Schmitt-Trigger mit $R_1$ = 10 kΩ und $R_2$ = 90 kΩ; Beispiel-OPV mit den Ausgangsgrenzen typisch ±14 V, mindestens ±12 V; Eingang: Kosinus mit 3 V Amplitude und 50 Hz, dazu Rauschen mit 0,2 V Effektivwert, gleichmäßig verteilt bis 100 kHz.

**Gesucht:** die Schwellen und die Hysterese, der Schaltzeitpunkt und der Vergleich mit einem Komparator.

**Rechnung:** Schwellen:

$$U_{R1,\max} = 0{,}1\cdot 14\ \mathrm{V} = 1{,}4\ \mathrm{V}$$

$$U_{R1,\min} = 0{,}1\cdot(-14\ \mathrm{V}) = -1{,}4\ \mathrm{V}$$

Die Hysterese ist 2,8 V, mit dem Mindesthub ±12 V sind es 2,4 V. Nach einem Nulldurchgang erreicht das Signal den Betrag 1,4 V beim Phasenwinkel

$$\arcsin\frac{1{,}4\ \mathrm{V}}{3\ \mathrm{V}} = 27{,}8°$$

ohne Rauschen also 27,8/360 der Periode von 20 ms später, nach 1,55 ms. Mit dem Rauschen schaltet der Schmitt-Trigger früher, sobald Signal und Rauschen zusammen die Schwelle erreichen; eine Simulation über 40 ms ergibt 0,91 bis 1,09 ms. In diesem Moment müsste das Rauschen den Eingang zum Zurückschalten um 2,25 bis 2,41 V verschieben, um 11 bis 12 Effektivwerte. Der ideale Komparator schaltet in derselben Simulation 210-mal, 43- bis 59-mal je Nulldurchgang; bei breiterem Rauschen wären es entsprechend mehr. Der Schmitt-Trigger schaltet viermal.

**Ergebnis:** **Schwellen ±1,4 V, Hysterese 2,8 V; ein Wechsel je Nulldurchgang, ohne Rauschen nach 1,55 ms, mit Rauschen nach 0,9 bis 1,1 ms, statt 43 bis 59 Wechseln beim Komparator.**

**Einordnung:** Ein Rauschausschlag von 11 Effektivwerten kommt praktisch nie vor; deshalb bleibt es bei einem Wechsel. Die Verzögerung ist der Preis. Eine kleinere Hysterese verkürzt sie, darf aber nicht in die Größenordnung der Rauschschwankungen kommen.
::::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Differenz­verstärker und Gleichtakt | Nur die Differenz zählt: Die Stromquelle hält die Summe fest, die Differenz verteilt sie. |
| Rauschen | Gemeinsame Störungen fallen als Gleichtakt heraus; unabhängiges Eigenrauschen wirkt wie eine Differenz. |
| Komparator und Flash-Wandler | Ohne Rückführung meldet die riesige Verstärkung nur das Vorzeichen der Differenz. |
| Ruhezustand und goldene Regeln | Rückführung gegen die Differenz: Der Ausgang stellt sich so ein, dass die Differenz verschwindet; die Widerstände bestimmen das Ergebnis. |
| Einschwingen | Bei Gegenkopplung verkleinert jede Änderung des Ausgangs ihre eigene Ursache. |
| Schmitt-Trigger | Rückführung mit der Differenz: Der Ausgang kippt an eine Grenze und bleibt dort, bis der Eingang die verschobene Schwelle überschreitet. |

Ein Operationsverstärker verstärkt nur die Differenz seiner beiden Eingangsspannungen, und das so stark, dass er allein nur „größer“ oder „kleiner“ melden kann; erst die Rückführung der Ausgangsspannung macht ihn brauchbar: Wirkt sie der Differenz entgegen, regelt der Ausgang die Differenz praktisch auf null, und die äußeren Widerstände bestimmen das Ergebnis; verstärkt sie die Differenz, kippt der Ausgang an eine Grenze und bleibt dort.

## Bedeutung und Ausblick

Operationsverstärker stecken in fast jeder analogen Schaltung: in Sensorverstärkern, Filtern, Reglern, Audiogeräten und vor jedem Analog-Digital-Umsetzer. Fast immer sind sie gegengekoppelt, so dass das Ergebnis so genau ist wie die Widerstände und unabhängig vom Exemplar. Mitgekoppelte Schaltungen wie der Schmitt-Trigger formen saubere Schaltflanken und erzeugen mit einem Kondensator Rechteckschwingungen. Empfindliche Signale führt man über verdrillte Leitungspaare an einen Differenzeingang; eingestreute Störungen treffen beide Adern gleich und fallen heraus.

Die Grenzen des idealen Modells, also endliche Leerlaufverstärkung und Bandbreite, Anstiegsgeschwindigkeit, Offsetspannung, Eingangsströme und endliche Gleichtaktunterdrückung, behandelt [Der reale Operationsverstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/realer-operationsverstaerker.html). Als Nächstes berechnet [Die OPV-Grundschaltungen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/opv-grundschaltungen.html) mit den goldenen Regeln den invertierenden und den nichtinvertierenden Verstärker, den Spannungsfolger, den Addierer, den Subtrahierer und den Integrator.

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
F: Warum addiert man die Effektivwerte zweier unabhängiger Rauschquellen quadratisch und nicht einfach?
A: Beim Quadrieren der Summe entsteht ein Mischterm aus dem Produkt beider Spannungen. Bei unabhängigen Quellen ist sein Mittelwert das Produkt der Mittelwerte, also null; es bleibt die Summe der mittleren Quadrate.
F: Stimmt es, dass ein Verstärker das Signal-Rausch-Verhältnis verbessert?
A: Nicht durch das Verstärken. Er hebt das Signal und das schon vorhandene Rauschen um denselben Faktor an und fügt eigenes Rauschen hinzu (54,8 dB auf 48,6 dB im Beispiel). Er schützt nur gegen Rauschen, das erst hinter ihm hinzukommt; besser wird das Verhältnis durch Begrenzen der Bandbreite.
F: Wie groß ist die Rauschspannung eines 10-kΩ-Widerstands bei 300 K im Band bis 20 kHz?
A: Die Dichte ist die Wurzel aus 4 k_B T R, 12,9 nV/√Hz; mal der Wurzel aus 20 kHz ergibt das 1,82 µV.
F: Warum ändert eine Gleichtaktspannung die Kollektorströme des Differenzverstärkers nicht?
A: Die Stromquelle hält die Summe fest, und das Verhältnis hängt nur vom Unterschied der Basis-Emitter-Spannungen ab. Der gemeinsame Emitterknoten folgt der Gleichtaktspannung, so dass beide Basis-Emitter-Spannungen gleich bleiben.
F: Warum verstärkt der Differenzverstärker mit −g_m R_C und nicht mit −2 g_m R_C, wie das Skript angibt?
A: Der gemeinsame Emitterknoten wandert um die halbe Eingangsänderung mit; jede Basis-Emitter-Spannung ändert sich nur um die Hälfte, jeder Strom um die halbe Steilheit mal der Differenz.
F: Warum kann man einen OPV ohne Rückkopplung nicht als Verstärker benutzen?
A: Sein linearer Bereich reicht nur bis ±70 µV. Schon die Offsetspannung von typisch 1 mV treibt den Ausgang an eine Grenze, und die Leerlaufverstärkung ist nur nach unten garantiert.
F: Ein OPV mit der Leerlaufverstärkung 50 000 wird mit k = 0,1 gegengekoppelt. Wie groß ist die Verstärkung der Schaltung?
A: 50 000/(1 + 0,1 · 50 000) = 9,998, fast genau 1/k = 10.
F: Warum stellt sich in einer gegengekoppelten Schaltung U_D ≈ 0 ein, und warum schwingt sie dabei nicht hin und her?
A: Der Ausgang ändert sich mit einer Geschwindigkeit proportional zu U_D. Jede Änderung verkleinert U_D über die Rückführung, bis der Ausgang steht, und das tut er nur bei U_D ≈ 0. Die Annäherung ist exponentiell (1,59 µs bei k = 0,1), ohne Vorzeichenwechsel von U_D.
F: Stimmt es, dass beim virtuellen Kurzschluss ein Strom zwischen den Eingängen fließt?
A: Nein. Die Eingänge sind nicht verbunden und nehmen keinen Strom auf; die Spannung zwischen ihnen ist nur null, weil der Ausgang sie über die Rückführung nachregelt. Liegt der Ausgang an einer Grenze, ist sie es nicht mehr, im Beispiel 0,6 V.
F: Warum hat der Schmitt-Trigger zwei verschiedene Schaltschwellen?
A: Der Pluseingang liegt auf k mal der Ausgangsspannung, und die hat zwei Werte. Je nach Zustand liegt die Schwelle deshalb bei +1,4 V oder bei −1,4 V; jeder Wechsel verschiebt die Schwelle für den nächsten.
:::
