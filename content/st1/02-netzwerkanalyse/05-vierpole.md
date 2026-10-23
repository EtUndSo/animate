---
title: Vierpole: Parameterformen und Zusammenschaltung
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / Netzwerkanalyse
order: 33020500
summary: Wie man eine lineare Schaltung mit einem Eingangs- und einem Ausgangstor durch vier Parameter vollständig beschreibt und aus den Matrizen der Teile die Matrix einer Zusammenschaltung gewinnt. Kompakte Fassung mit hergeleiteter Admittanz-, Impedanz- und Kettenform, Umrechnung, Umkehrungssatz, Eingangsadmittanz unter Last, Regeln für Ketten-, Parallel- und Reihenschaltung samt Torbedingung und der Verstärkung einer Signalkette; die ausführliche Fassung enthält zusätzlich Ersatzschaltbild, Leistungsbilanz, Hybridform und eine Bipolarstufe.
tags: Vierpol, Admittanzform, Impedanzform, Kettenform, Zusammenschaltung
stil: 3
fassung: kompakt
---

## Worum es geht

Verstärker, Filter und Leitungen haben einen Eingang und einen Ausgang. Setzt man sie zu Systemen zusammen, beschreibt man jeden Block nur durch sein Verhalten an den Anschlüssen, statt sein Inneres immer neu zu berechnen. Drei Kenngrößen wie beim Ersatzzweitor genügen dafür nur, solange der Ausgang nicht auf den Eingang zurückwirkt; vollständig sind es vier Parameter, die sich auf mehrere gleichwertige Arten anordnen lassen. Alles hängt an einem Prinzip:

**Ein lineares Zweitor ist durch zwei lineare Gleichungen zwischen seinen vier Torgrößen vollständig beschrieben; jede Parameterform ordnet dieselben Gleichungen nach einem anderen Paar vorgegebener Größen, und bei einer Zusammenschaltung nimmt man die Form, deren vorgegebene Größen allen Teilen gemeinsam sind: Dann addieren sich die Matrizen, in der Kette multiplizieren sie sich.**

Vorausgesetzt werden das Rechnen mit [Zeigern](/wissen/elektrotechnik/1-semester/mathematische-methoden-der-elektrotechnik/komplexe-zahlen-und-zeiger/zeiger-und-sinussignale.html), Matrizen, Inverse und Determinante aus [Netzwerkgleichungen systematisch aufstellen: modifizierte Knotenanalyse](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/modifizierte-knotenanalyse.html), Testquellen und das Ersatzzweitor aus [Testquellen und Transientenanalyse linearer Schaltungen](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/testquellen-und-transientenanalyse.html) und die Verstärkerstufe aus [Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/ersatzquellen-maschen-und-knotenanalyse.html); eine erste Einführung gibt [Zweitore und ihre Parameter](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/zweitore.html). Auf den Vierpolen bauen die Transistorgrundschaltungen auf, in denen jede Stufe als Zweitor in einer Kette steht.

:::grafik
Szene: st1/netzwerkanalyse/05-uebersicht · Vorlage: blockbild
**Abbildung 1:** (a) Ein Zweitor als Kasten mit dem Eingangstor aus den Klemmen 1 und 1′ und dem Ausgangstor aus 2 und 2′; die Ströme $\underline I_1$ und $\underline I_2$ fließen an den oberen Klemmen hinein und an den unteren heraus, die Spannungen $\underline U_1$ und $\underline U_2$ zeigen von oben nach unten. (b) Drei Zusammenschaltungen zweier Zweitore a und b mit der jeweils passenden Form: Kettenschaltung, Ausgang von a an den Eingang von b, $\mathbf A = \mathbf A_\mathrm a\mathbf A_\mathrm b$; Parallelschaltung, beide Tore parallel, $\mathbf Y = \mathbf Y_\mathrm a + \mathbf Y_\mathrm b$; Reihenschaltung, beide Tore in Reihe, $\mathbf Z = \mathbf Z_\mathrm a + \mathbf Z_\mathrm b$. In der Form, deren vorgegebene Größen allen Teilen gemeinsam sind, wird jede Zusammenschaltung zu einer Addition oder Multiplikation der Matrizen.
:::

## Tor, Torbedingung und Zweitor

*Wann darf man eine Schaltung mit vier Anschlüssen durch Spannung und Strom an zwei Anschlusspaaren beschreiben?*

Eine Schaltung mit vier Anschlüssen heißt __Vierpol__. Fasst man ihre Klemmen paarweise zu __Toren__ zusammen, 1 und 1′ zum Eingangstor (Tor 1), 2 und 2′ zum Ausgangstor (Tor 2), hat jedes Tor nur dann einen einzigen Strom, wenn die __Torbedingung__ gilt: Was an der oberen Klemme eines Tores hineinfließt, fließt an der unteren desselben Tores wieder heraus. Dann heißt der Vierpol __Zweitor__ (Abbildung 1 a).

**Die Akteure:**

- __$\underline U_1$__, __$\underline U_2$__: Torspannungen, als Zeiger von der oberen zur unteren Klemme gezählt; in V.
- __$\underline I_1$__, __$\underline I_2$__: Torströme, in die obere Klemme hinein gezählt; in A. __$\underline I_{1'}$__, __$\underline I_{2'}$__: die Ströme, die an den unteren Klemmen 1′ und 2′ herausfließen.

:::formel Definition
$$\underline I_1 = \underline I_{1'}, \qquad \underline I_2 = \underline I_{2'}\,$$
:::

Die Torbedingung hängt von der Beschaltung ab, nicht von der Schaltung allein. Hängt an jedem Tor ein eigener Zweipol, eine Signalquelle links und eine Last rechts, gilt sie von selbst, weil der Strom aus der Quelle nur über Klemme 1′ zu ihr zurückkehren kann. Verbindet man dagegen Zweitore miteinander, kann ein Teil des Stroms einen anderen Rückweg nehmen; dann entscheidet sie darüber, ob die Rechenregeln der Zusammenschaltung gelten (Abschnitt *Parallel- und Reihenschaltung*).

Beide Ströme werden in das Zweitor hinein gezählt, beide Spannungen von oben nach unten, an jedem Tor also wie bei einem Verbraucher; diese Vereinbarung heißt __symmetrisches Zählpfeilsystem__. Im Inneren dürfen lineare Bauelemente und gesteuerte Quellen liegen, deren Steuergröße eine Spannung oder ein Strom im Inneren ist, aber keine unabhängigen Quellen, die ohne Anregung an den Toren Ströme trieben. Ein Transistorverstärker erfüllt das in seinem [Kleinsignal-Ersatzschaltbild](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung.html), dem linearen Modell für kleine Änderungen um den Arbeitspunkt. Alle Größen sind Zeiger bei einer festen Kreisfrequenz ω.

:::frage
„Warum zählt man auch den Ausgangsstrom in das Zweitor hinein, er fließt doch zur Last heraus?“
Ein Zählpfeil legt nur fest, welche Richtung positiv zählt; fließt der Strom anders herum, wird sein Zeiger negativ. Am RC-Glied mit kurzgeschlossenem Ausgang ist $\underline I_2$ bei 1 V am Eingang −1 mA: 1 mA fließt aus Klemme 2 heraus. Die symmetrische Wahl macht beide Gleichungen gleich gebaut, sodass die Umkehrbarkeit als Gleichheit zweier Parameter ablesbar ist. Nur die Kettenform zählt den Ausgangsstrom hinaus, weil er dort als Eingangsstrom des nächsten Glieds weiterläuft.
:::

## Vier Größen, zwei Gleichungen

*Warum genügen vier Zahlen, um ein lineares Zweitor vollständig zu beschreiben, und warum gibt es mehrere Formen?*

Als Beispiel dient das __RC-Glied__: ein Widerstand $R$ = 1 kΩ in der oberen Leitung zwischen den Klemmen 1 und 2 und ein Kondensator $C$ = 100 nF von Klemme 2 zur durchgehenden unteren Leitung, bei ω = 10⁴ 1/s mit der Admittanz j·1 mS. Liegen an beiden Toren Spannungen, fließt in Klemme 1 der Strom durch den Widerstand, und in Klemme 2 fließt, was der Kondensator aufnimmt, abzüglich dessen, was über den Widerstand ankommt. Jeder Strom ist eine Summe aus einem Anteil proportional zu $\underline U_1$ und einem proportional zu $\underline U_2$:

$$\underline I_1 = 1\ \mathrm{mS}\cdot\underline U_1 - 1\ \mathrm{mS}\cdot\underline U_2, \qquad \underline I_2 = -1\ \mathrm{mS}\cdot\underline U_1 + (1 + j)\ \mathrm{mS}\cdot\underline U_2\,$$

Die vier Zahlen 1, −1, −1 und (1 + j) mS legen für jedes Spannungspaar beide Ströme fest; mit 1 V und 0,5 V sind es 0,5 mA und (−0,5 + 0,5j) mA. Für jedes lineare Zweitor gilt dasselbe, denn nach dem Überlagerungssatz ist jeder Strom die Summe der Ströme, die jede Torspannung allein hervorruft. Man schreibt die zwei Gleichungen als Produkt einer Matrix mit einem Spaltenvektor: Jede Zeile der Matrix wird elementweise mit dem Vektor multipliziert und aufsummiert, wie bei den Knotengleichungen.

Idee der Herleitung: Man regt mit zwei Spannungsquellen an, lässt jeweils eine wirken und überlagert die beiden Antworten.

:::herleitung
**Ausgangspunkt:** der Überlagerungssatz für lineare Netze aus [Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/ersatzquellen-maschen-und-knotenanalyse-ausfuehrlich.html): Die Antwort auf mehrere unabhängige Quellen ist die Summe der Antworten auf jede einzelne, und jede Antwort ist proportional zu ihrer Quelle.

**Annahmen:** (i) Das Zweitor ist linear und enthält keine unabhängigen Quellen. (ii) Alle Größen sind Zeiger bei derselben Kreisfrequenz. (iii) Die Schaltung mit idealen Spannungsquellen an beiden Toren hat eine eindeutige Lösung; die Determinante ihres Gleichungssystems ist nicht null.

**Schritt 1**: Nur die Quelle an Tor 1 wirkt, die an Tor 2 ist abgeschaltet, also ein Kurzschluss. Jeder Strom ist proportional zu $\underline U_1$; die Faktoren für die beiden Torströme heißen $\underline Y_{11}$ und $\underline Y_{21}$:

$$\underline I_1 = \underline Y_{11}\,\underline U_1, \qquad \underline I_2 = \underline Y_{21}\,\underline U_1\,$$

**Schritt 2**: Ebenso wirkt nur die Quelle an Tor 2, Tor 1 ist kurzgeschlossen; die Faktoren heißen $\underline Y_{12}$ und $\underline Y_{22}$:

$$\underline I_1 = \underline Y_{12}\,\underline U_2, \qquad \underline I_2 = \underline Y_{22}\,\underline U_2\,$$

**Schritt 3** (entscheidender Schritt): Wirken beide Quellen, addieren sich nach dem Überlagerungssatz die Anteile:

$$\underline I_1 = \underline Y_{11}\,\underline U_1 + \underline Y_{12}\,\underline U_2, \qquad \underline I_2 = \underline Y_{21}\,\underline U_1 + \underline Y_{22}\,\underline U_2\,$$

**Ergebnis:** Zwei Gleichungen mit vier Faktoren, die nur vom Inneren des Zweitors abhängen:

$$\begin{pmatrix} \underline I_1 \\ \underline I_2 \end{pmatrix} = \begin{pmatrix} \underline Y_{11} & \underline Y_{12} \\ \underline Y_{21} & \underline Y_{22} \end{pmatrix}\begin{pmatrix} \underline U_1 \\ \underline U_2 \end{pmatrix}$$

**Woher die Faktoren kommen:** Jeder Faktor ist ein Strom an einem Tor je Volt an einem Tor, gemessen mit dem jeweils anderen Tor im Kurzschluss; der erste Index nennt das Tor des Stroms, der zweite das der Spannung.

**Proben:** Einheit: Strom durch Spannung, also Siemens. RC-Glied mit 1 V und 0,5 V: Durch den Widerstand fließen 1 mS mal 0,5 V, also 0,5 mA, und das ist $\underline I_1$. Am Ausgang kommen diese 0,5 mA an, und der Kondensator nimmt j·1 mS mal 0,5 V auf, also 0,5j mA; von außen fließen deshalb (−0,5 + 0,5j) mA hinein, wie die Formel ergibt.

**Grenzen:** Erzwingt die Schaltung eine Beziehung zwischen den beiden Torspannungen, etwa weil beide Tore an denselben Knoten liegen, widersprechen sich zwei beliebige Quellen, Annahme (iii) ist verletzt, und es gibt diese Form nicht; dann nimmt man eine der anderen (Abschnitt *Umrechnung*).
:::

**Kurz gesagt:** Die Antwort eines linearen Zweitors auf zwei Torspannungen ist die Summe seiner Antworten auf jede einzelne.

Welche zwei der vier Torgrößen man vorgibt, ist frei; aus vier Größen lassen sich auf sechs Arten zwei auswählen, und die beiden übrigen folgen aus ihnen. Drei dieser Formen sind die gebräuchlichsten, weil zu ihnen die drei häufigsten Zusammenschaltungen passen:

| Form und vorgegebene Größen | Parameter bestimmt mit |
|---|---|
| Admittanzform $\mathbf Y$: $\underline U_1$, $\underline U_2$ | Kurzschluss an einem Tor |
| Impedanzform $\mathbf Z$: $\underline I_1$, $\underline I_2$ | Leerlauf an einem Tor |
| Kettenform $\mathbf A$: $\underline U_2$, $-\underline I_2$ | Leerlauf und Kurzschluss am Ausgang |

Die übrigen drei sind die Hybridform, die Eingangsstrom und Ausgangsspannung vorgibt und Bipolartransistoren besonders knapp beschreibt, sowie die inverse Hybrid- und die inverse Kettenform.

## Admittanzform: Ströme aus den Spannungen

*Welche Ströme fließen in ein Zweitor, wenn beide Torspannungen vorgegeben sind, und wie bestimmt man die vier Faktoren?*

:::grafik
Szene: st1/netzwerkanalyse/05-kurzschluss-leerlauf · Vorlage: schaltbild-messung
**Abbildung 2:** Das RC-Glied (1 kΩ längs, 100 nF quer, ω = 10⁴ 1/s) in vier Versuchen. (a) Ausgang kurzgeschlossen, 1 V am Eingang: Der Kondensator ist überbrückt, $\underline I_1$ = 1 mA, $\underline I_2$ = −1 mA; das ergibt $\underline Y_{11}$ = 1 mS und $\underline Y_{21}$ = −1 mS. (b) Eingang kurzgeschlossen, 1 V am Ausgang: $\underline I_1$ = −1 mA, $\underline I_2$ = (1 + j) mA; $\underline Y_{12}$ = −1 mS, $\underline Y_{22}$ = (1 + j) mS. (c) Ausgang offen, 1 mA in den Eingang: $\underline U_1$ = (1 − j) V, $\underline U_2$ = −j V; $\underline Z_{11}$ = (1 − j) kΩ, $\underline Z_{21}$ = −j kΩ. (d) Eingang offen, 1 mA in den Ausgang: beide Spannungen −j V; $\underline Z_{12}$ = $\underline Z_{22}$ = −j kΩ. Admittanzparameter misst man mit kurzgeschlossenem, Impedanzparameter mit offenem Gegentor.
:::

**Die Akteure:**

- __$\underline Y_{11}$__, __$\underline Y_{12}$__, __$\underline Y_{21}$__, __$\underline Y_{22}$__: die __Admittanzparameter__ oder Y-Parameter; in S. Beim RC-Glied 1 mS, −1 mS, −1 mS und (1 + j) mS.
- __$\mathbf Y$__: die __Admittanzmatrix__ oder Leitwertmatrix aus diesen vier Parametern, die Form heißt auch __Leitwertform__; nicht zu verwechseln mit der Knotenleitwertmatrix __$\mathbf Y_\mathrm K$__ der Knotenanalyse, die eine Zeile je Knoten hat.

:::formel Definition
$$\underline I_1 = \underline Y_{11}\,\underline U_1 + \underline Y_{12}\,\underline U_2, \qquad \underline I_2 = \underline Y_{21}\,\underline U_1 + \underline Y_{22}\,\underline U_2\,$$

$$\begin{pmatrix} \underline I_1 \\ \underline I_2 \end{pmatrix} = \mathbf Y\begin{pmatrix} \underline U_1 \\ \underline U_2 \end{pmatrix}, \qquad \mathbf Y = \begin{pmatrix} \underline Y_{11} & \underline Y_{12} \\ \underline Y_{21} & \underline Y_{22} \end{pmatrix}\,$$
:::

**So liest man das:** Die Ströme folgen aus den Spannungen. Eine vorgegebene Spannung null ist ein Kurzschluss; deshalb bestimmt man jeden Parameter mit einer Spannung an einem Tor und dem anderen Tor im Kurzschluss, wie die Herleitung oben zeigt (Abbildung 2 a und b):

$$\underline Y_{11} = \frac{\underline I_1}{\underline U_1}\bigg|_{\underline U_2 = 0}, \qquad \underline Y_{21} = \frac{\underline I_2}{\underline U_1}\bigg|_{\underline U_2 = 0}, \qquad \underline Y_{12} = \frac{\underline I_1}{\underline U_2}\bigg|_{\underline U_1 = 0}, \qquad \underline Y_{22} = \frac{\underline I_2}{\underline U_2}\bigg|_{\underline U_1 = 0}\,$$

$\underline Y_{11}$ heißt __Kurzschluss-Eingangsadmittanz__, $\underline Y_{22}$ __Kurzschluss-Ausgangsadmittanz__, $\underline Y_{21}$ __Kurzschluss-Übertragungsadmittanz__ vorwärts, bei Transistoren __Steilheit__, und $\underline Y_{12}$ die rückwärts; sie gibt an, wie stark der Ausgang auf den Eingang zurückwirkt.

**Kurz gesagt:** Jeder Y-Parameter ist der Strom an einem Tor je Volt an einem Tor, während das jeweils andere Tor kurzgeschlossen ist.

:::frage
„Darf man den Ausgang eines Verstärkers zum Messen mit einem Draht kurzschließen?“
Gemeint ist ein Kurzschluss für das Signal, nicht für den Arbeitspunkt. Ein Draht vom Drain der Verstärkerstufe nach Masse legte auch die Gleichspannung des Drains auf null; der Transistor führte keinen Strom mehr, und seine Steilheit wäre null. Man schließt deshalb nur den Wechselanteil kurz, über einen Kondensator, dessen Impedanz bei der Messfrequenz klein ist gegen die Impedanz am Tor: 10 µF haben bei 1 kHz 15,9 Ω, 0,18 % der 8,90 kΩ am Drain.
:::

Ein π aus drei Admittanzen, einem Querzweig an jedem Tor und einem Längszweig dazwischen, hat auf der Diagonalen den jeweiligen Querzweig plus den Längszweig und daneben den negativen Längszweig: Bei kurzgeschlossenem Gegentor fließt der Strom eines Tors durch dessen Querzweig und durch den Längszweig, und was durch den Längszweig fließt, verlässt das andere Tor. Das RC-Glied ist ein solches π ohne Querzweig am Eingang.

Die Verstärkerstufe, eine Source-Schaltung mit der Steilheit $g_m$ = 1 mS, dem Ausgangsleitwert $g_o$ = 25 µS, dem Drainwiderstand $R_D$ = 10 kΩ und dem Source-Widerstand $R_S$ = 1 kΩ, ist als Zweitor zwischen Gate und Masse (Tor 1) und Drain und Masse (Tor 2) beschrieben, wenn man ihr Ersatzzweitor aus dem Artikel über Testquellen umschreibt. Das Gate nimmt keinen Strom auf, also sind $\underline Y_{11}$ und $\underline Y_{12}$ null; bei kurzgeschlossenem Drain fließen je Volt am Gate 0,494 mA in den Drain, $\underline Y_{21}$ ist 0,494 mS; bei kurzgeschlossenem Gate sieht man in den Drain 8,90 kΩ, $\underline Y_{22}$ ist 0,112 mS. Das Ersatzzweitor aus drei Kenngrößen ist also die Admittanzform mit $\underline Y_{12}$ = 0, und seine Leerlaufverstärkung ist $-\underline Y_{21}/\underline Y_{22}$, −4,40.

## Impedanz- und Kettenform

*Welche Spannungen folgen aus vorgegebenen Strömen, und was muss man am Eingang anlegen, damit am Ausgang eine bestimmte Spannung und ein bestimmter Strom herauskommen?*

Gibt man beide Torströme durch Stromquellen vor, sind die Spannungen nach dem Überlagerungssatz Summen von Anteilen proportional zu $\underline I_1$ und $\underline I_2$. Ein vorgegebener Strom null ist ein offenes Tor; die Parameter misst man deshalb im Leerlauf des anderen Tors (Abbildung 2 c und d).

**Die Akteure:**

- __$\underline Z_{11}$__, __$\underline Z_{12}$__, __$\underline Z_{21}$__, __$\underline Z_{22}$__: die __Impedanzparameter__; in Ω. Beim RC-Glied (1 − j) kΩ, −j kΩ, −j kΩ und −j kΩ. __$\mathbf Z$__: die __Impedanzmatrix__ oder Widerstandsmatrix; die Form heißt auch __Widerstandsform__.

:::formel Definition
$$\underline U_1 = \underline Z_{11}\,\underline I_1 + \underline Z_{12}\,\underline I_2, \qquad \underline U_2 = \underline Z_{21}\,\underline I_1 + \underline Z_{22}\,\underline I_2\,$$
:::

**So liest man das:** Jeder Parameter ist eine Spannung je Strom bei offenem Gegentor; $\underline Z_{11}$ heißt __Leerlauf-Eingangsimpedanz__, $\underline Z_{22}$ __Leerlauf-Ausgangsimpedanz__, $\underline Z_{21}$ und $\underline Z_{12}$ __Leerlauf-Übertragungsimpedanz__ vorwärts und rückwärts. Ein __T-Glied__ aus zwei Längsimpedanzen und einer Querimpedanz dazwischen hat die Querimpedanz auf der Nebendiagonalen und auf der Diagonalen die Summe aus ihr und der jeweiligen Längsimpedanz:

$$\mathbf Z = \begin{pmatrix} \underline Z_\text{längs1} + \underline Z_\text{quer} & \underline Z_\text{quer} \\ \underline Z_\text{quer} & \underline Z_\text{quer} + \underline Z_\text{längs2} \end{pmatrix}$$

Ohne Längsimpedanzen bleibt ein __Querglied__, eine Impedanz zwischen zwei durchgehenden Leitungen; sein Gegenstück ist das __Längsglied__, eine Impedanz in der oberen Leitung bei durchgehender unterer.

**Kurz gesagt:** Jeder Z-Parameter ist die Spannung an einem Tor je Ampere in ein Tor, während das jeweils andere Tor offen ist.

Idee der Herleitung: wie bei der Admittanzform, mit Stromquellen statt Spannungsquellen; beim T-Glied genügen zwei Leerlaufversuche.

:::herleitung
**Ausgangspunkt:** der Überlagerungssatz, angewandt auf zwei ideale Stromquellen an den Toren.

**Annahmen:** (i) Das Zweitor ist linear und ohne unabhängige Quellen. (ii) Die Schaltung mit Stromquellen an beiden Toren hat eine eindeutige Lösung.

**Schritt 1**: Nur die Stromquelle an Tor 1 wirkt; die an Tor 2 ist abgeschaltet, ein Leerlauf. Beide Spannungen sind proportional zu $\underline I_1$, mit den Faktoren $\underline Z_{11}$ und $\underline Z_{21}$; ebenso mit Tor 1 offen die Faktoren $\underline Z_{12}$ und $\underline Z_{22}$.

**Schritt 2**: Wirken beide, addieren sich die Anteile:

$$\underline U_1 = \underline Z_{11}\,\underline I_1 + \underline Z_{12}\,\underline I_2, \qquad \underline U_2 = \underline Z_{21}\,\underline I_1 + \underline Z_{22}\,\underline I_2\,$$

**Schritt 3** (T-Glied): Mit $\underline I_2$ = 0 fließt $\underline I_1$ durch die erste Längs- und die Querimpedanz; durch die zweite Längsimpedanz fließt nichts, sie hat keinen Spannungsabfall:

$$\underline U_1 = (\underline Z_\text{längs1} + \underline Z_\text{quer})\,\underline I_1, \qquad \underline U_2 = \underline Z_\text{quer}\,\underline I_1\,$$

**Schritt 4**: Mit $\underline I_1$ = 0 ebenso von der anderen Seite:

$$\underline U_2 = (\underline Z_\text{quer} + \underline Z_\text{längs2})\,\underline I_2, \qquad \underline U_1 = \underline Z_\text{quer}\,\underline I_2\,$$

**Ergebnis:**

$$\mathbf Z = \begin{pmatrix} \underline Z_\text{längs1} + \underline Z_\text{quer} & \underline Z_\text{quer} \\ \underline Z_\text{quer} & \underline Z_\text{quer} + \underline Z_\text{längs2} \end{pmatrix}$$

**Woher die Faktoren kommen:** Die Nebeneinträge sind die Querimpedanz, weil sie der einzige Teil ist, durch den der Strom des einen Tors fließt und an dem das andere Tor abgreift.

**Proben:** Einheit Ω. Querglied allein: alle vier Einträge gleich $\underline Z_\text{quer}$. RC-Glied als T mit $\underline Z_\text{längs1}$ = 1 kΩ, $\underline Z_\text{quer}$ = −j kΩ und $\underline Z_\text{längs2}$ = 0: (1 − j), −j, −j, −j kΩ wie in den Leerlaufversuchen.

**Grenzen:** Erzwingt die Schaltung eine Beziehung zwischen den Torströmen, etwa ein Längsglied, durch das derselbe Strom von Tor 1 zu Tor 2 fließen muss, gibt es keine Impedanzform.
:::

Ein häufiger Fehler ist, $\underline Y_{11}$ für den Kehrwert von $\underline Z_{11}$ zu halten. Beide gehören zu verschiedenen Versuchen, der eine mit kurzgeschlossenem, der andere mit offenem Ausgang: Am RC-Glied ist $\underline Y_{11}$ 1 mS, weil der Kurzschluss den Kondensator überbrückt, $1/\underline Z_{11}$ aber (0,5 + 0,5j) mS, weil im Leerlauf der Kondensator im Strompfad liegt. Zueinander invers sind nur die Matrizen als Ganzes.

Die __Kettenform__ drückt die Eingangsgrößen durch die Ausgangsgrößen aus. Als Ausgangsstrom nimmt sie $-\underline I_2$, den Strom, der aus Klemme 2 heraus zum nächsten Glied fließt; so gehen in einer Kette die Ausgangsgrößen des einen Glieds ohne Vorzeichenwechsel in die Eingangsgrößen des nächsten über.

**Die Akteure:**

- __$\underline A_{11}$__, __$\underline A_{12}$__, __$\underline A_{21}$__, __$\underline A_{22}$__: die __Kettenparameter__, $\underline A_{11}$ und $\underline A_{22}$ ohne Einheit, $\underline A_{12}$ in Ω, $\underline A_{21}$ in S; beim RC-Glied 1 + j, 1 kΩ, j·1 mS und 1. __$\mathbf A$__: die __Kettenmatrix__, im Englischen ABCD-Matrix.

:::formel Definition
$$\underline U_1 = \underline A_{11}\,\underline U_2 + \underline A_{12}\,(-\underline I_2), \qquad \underline I_1 = \underline A_{21}\,\underline U_2 + \underline A_{22}\,(-\underline I_2)\,$$
:::

**So liest man das:** Man bestimmt die Parameter am Ausgang, offen und kurzgeschlossen, in denselben Versuchen wie Abbildung 2 c und a:

$$\underline A_{11} = \frac{\underline U_1}{\underline U_2}\bigg|_{\underline I_2 = 0}, \qquad \underline A_{21} = \frac{\underline I_1}{\underline U_2}\bigg|_{\underline I_2 = 0}, \qquad \underline A_{12} = \frac{\underline U_1}{-\underline I_2}\bigg|_{\underline U_2 = 0}, \qquad \underline A_{22} = \frac{\underline I_1}{-\underline I_2}\bigg|_{\underline U_2 = 0}\,$$

$\underline A_{11}$ ist die __reziproke Leerlauf-Spannungsübertragung__, der Kehrwert der Leerlaufverstärkung $\underline A_V$ aus dem Artikel über Testquellen; $\underline A_{21}$ heißt Leerlauf-Übertragungsadmittanz, $\underline A_{12}$ Kurzschluss-Übertragungsimpedanz und $\underline A_{22}$ reziproke Kurzschluss-Stromübertragung. Längs- und Querglied haben besonders übersichtliche Kettenmatrizen: Das Längsglied mit der Impedanz $\underline Z$ lässt den Strom durch und senkt die Spannung um $\underline Z$ mal Strom, das Querglied mit der Admittanz $\underline Y$ lässt die Spannung durch und zweigt $\underline Y$ mal Spannung ab:

$$\mathbf A_\text{längs} = \begin{pmatrix} 1 & \underline Z \\ 0 & 1 \end{pmatrix}, \qquad \mathbf A_\text{quer} = \begin{pmatrix} 1 & 0 \\ \underline Y & 1 \end{pmatrix}\,$$

Idee der Herleitung: Man schreibt Maschen- und Knotenregel des Glieds direkt in der Form der Kettengleichungen.

:::herleitung
**Ausgangspunkt:** Maschenregel und Knotenregel am Längs- und am Querglied; die Kettengleichungen.

**Annahmen:** (i) Die untere Leitung ist durchgehend. (ii) Die Zählpfeile sind die der Kettenform: $-\underline I_2$ fließt aus Klemme 2 heraus.

**Schritt 1**: Messvorschriften. Mit offenem Ausgang, $\underline I_2$ = 0, bleibt in jeder Kettengleichung nur das Glied mit $\underline U_2$, mit kurzgeschlossenem Ausgang, $\underline U_2$ = 0, nur das mit $-\underline I_2$; geteilt durch die verbleibende Größe ergeben sich die vier Vorschriften:

$$\underline U_1 = \underline A_{11}\,\underline U_2, \quad \underline I_1 = \underline A_{21}\,\underline U_2 \quad (\underline I_2 = 0), \qquad \underline U_1 = \underline A_{12}\,(-\underline I_2), \quad \underline I_1 = \underline A_{22}\,(-\underline I_2) \quad (\underline U_2 = 0)\,$$

**Schritt 2**: Längsglied. Der Strom, der in Klemme 1 hineinfließt, verlässt Klemme 2, und an der Impedanz fällt die Spannung $\underline Z$ mal diesem Strom ab:

$$\underline I_1 = -\underline I_2, \qquad \underline U_1 = \underline U_2 + \underline Z\,(-\underline I_2)\,$$

**Schritt 3**: Querglied. Beide Tore liegen an denselben Leitungen, und an Klemme 1 fließt zusätzlich der Strom durch die Admittanz hinein:

$$\underline U_1 = \underline U_2, \qquad \underline I_1 = \underline Y\,\underline U_2 + (-\underline I_2)\,$$

**Ergebnis:** Abgelesen sind das die beiden Matrizen:

$$\mathbf A_\text{längs} = \begin{pmatrix} 1 & \underline Z \\ 0 & 1 \end{pmatrix}, \qquad \mathbf A_\text{quer} = \begin{pmatrix} 1 & 0 \\ \underline Y & 1 \end{pmatrix}\,$$

**Woher die Faktoren kommen:** Die Einsen auf der Diagonalen besagen, dass das Glied Spannung bzw. Strom ungeändert weitergibt; der eine Nebeneintrag ist das einzige Bauteil.

**Proben:** Einheiten: $\underline Z$ steht bei $-\underline I_2$ in der Spannungsgleichung, also in Ω; $\underline Y$ bei $\underline U_2$ in der Stromgleichung, in S. Determinante beider Matrizen 1.

**Grenzen:** Die Kettenform gibt es für beide Glieder, auch wo eine andere Form fehlt (Abschnitt *Umrechnung*).
:::

::::beispiel Das RC-Glied in Admittanz-, Impedanz- und Kettenform
**Gegeben:** RC-Glied mit $R$ = 1 kΩ längs und $C$ = 100 nF quer bei ω = 10⁴ 1/s, also j·1 mS für den Kondensator und $j\omega RC$ = j.

**Gesucht:** $\mathbf Y$, $\mathbf Z$ und $\mathbf A$.

**Rechnung:** Kurzschlussversuche: Mit kurzgeschlossenem Ausgang ist der Kondensator überbrückt, der Strom fließt durch $R$ hinein und am Ausgang heraus; mit kurzgeschlossenem Eingang fließt der Strom aus Tor 2 durch $R$ und durch $C$:

$$\mathbf Y = \begin{pmatrix} 1/R & -1/R \\ -1/R & 1/R + j\omega C \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ -1 & 1 + j \end{pmatrix}\mathrm{mS}$$

Leerlaufversuche, mit dem RC-Glied als T aus der Längsimpedanz 1 kΩ und der Querimpedanz −j·1 kΩ:

$$\mathbf Z = \begin{pmatrix} 1 - j & -j \\ -j & -j \end{pmatrix}\mathrm{k\Omega}$$

Kettenparameter: Bei offenem Ausgang ist die Eingangsspannung $1 + j\omega RC$-mal die Ausgangsspannung und der Eingangsstrom der Kondensatorstrom; bei kurzgeschlossenem Ausgang fließt der Eingangsstrom ganz durch $R$:

$$\mathbf A = \begin{pmatrix} 1 + j\omega RC & R \\ j\omega C & 1 \end{pmatrix} = \begin{pmatrix} 1 + j & 1\ \mathrm{k\Omega} \\ j\cdot 1\ \mathrm{mS} & 1 \end{pmatrix}$$

**Ergebnis:** **$\mathbf Y$ mit 1, −1, −1 und (1 + j) mS; $\mathbf Z$ mit (1 − j), −j, −j und −j kΩ; $\mathbf A$ mit 1 + j, 1 kΩ, j·1 mS und 1. Leerlauf-Spannungsübertragung $1/(1 + j)$, Betrag 0,707, Winkel −45°.**

**Einordnung:** $\mathbf Z$ ist die Inverse von $\mathbf Y$; die erste Zeile von $\mathbf Z$ mal der ersten Spalte von $\mathbf Y$ ergibt (1 − j) · 1 + (−j)(−1), also 1. Der Kehrwert von $\underline Z_{11}$, (0,5 + 0,5j) mS, ist dagegen nicht $\underline Y_{11}$ = 1 mS. $\mathbf A$ ist das Produkt der Matrizen von Längsglied und Querglied, wie der Abschnitt *Kettenschaltung* zeigt.
::::

## Umrechnung zwischen den Formen

*Wie gewinnt man aus einer Form jede andere, und gibt es jede Form für jedes Zweitor?*

Alle Formen enthalten dieselben zwei Gleichungen; man gewinnt die eine aus der anderen, indem man nach dem anderen Paar von Größen auflöst. Zwischen Admittanz- und Impedanzform ist das eine Inversion: Man vertauscht die Diagonaleinträge, polt die Nebeneinträge um und teilt durch die __Determinante__, das Produkt der Diagonaleinträge minus das der Nebeneinträge.

**Die Akteure:**

- __$\det\mathbf Y$__, __$\det\mathbf Z$__, __$\det\mathbf A$__: die Determinanten der drei Matrizen; beim RC-Glied j·1 mS², −j·1 kΩ² und 1.

:::formel Formel
$$\mathbf Z = \mathbf Y^{-1} = \frac{1}{\det\mathbf Y}\begin{pmatrix} \underline Y_{22} & -\underline Y_{12} \\ -\underline Y_{21} & \underline Y_{11} \end{pmatrix}, \qquad \mathbf Y = \mathbf Z^{-1} = \frac{1}{\det\mathbf Z}\begin{pmatrix} \underline Z_{22} & -\underline Z_{12} \\ -\underline Z_{21} & \underline Z_{11} \end{pmatrix}\,$$

$$\mathbf A = -\frac{1}{\underline Y_{21}}\begin{pmatrix} \underline Y_{22} & 1 \\ \det\mathbf Y & \underline Y_{11} \end{pmatrix}, \qquad \mathbf Y = \frac{1}{\underline A_{12}}\begin{pmatrix} \underline A_{22} & -\det\mathbf A \\ -1 & \underline A_{11} \end{pmatrix}\,$$

$$\mathbf A = \frac{1}{\underline Z_{21}}\begin{pmatrix} \underline Z_{11} & \det\mathbf Z \\ 1 & \underline Z_{22} \end{pmatrix}, \qquad \mathbf Z = \frac{1}{\underline A_{21}}\begin{pmatrix} \underline A_{11} & \det\mathbf A \\ 1 & \underline A_{22} \end{pmatrix}\,$$

$$\det\mathbf A = \frac{\underline Y_{12}}{\underline Y_{21}} = \frac{\underline Z_{12}}{\underline Z_{21}}$$
:::

**So liest man das:** Jede Umrechnung teilt durch einen Parameter oder eine Determinante; ist dieser Nenner null, gibt es die Zielform nicht, weil sich ihre vorgegebenen Größen nicht unabhängig wählen lassen. Das Querglied hat keine Admittanzform, weil seine Torspannungen gleich sind, das Längsglied keine Impedanzform, weil durch beide Tore derselbe Strom fließt. Die Verstärkerstufe hat keine Impedanzform, weil ihr Gate keinen Strom aufnimmt: Die erste Zeile ihrer Admittanzmatrix ist null, $\det\mathbf Y$ ebenfalls. Ihre Kettenmatrix existiert, mit den Einträgen −0,2275, −2,025 kΩ, 0 und 0; der Kehrwert von −0,2275 ist die Leerlaufverstärkung −4,396.

**Kurz gesagt:** Die Impedanzmatrix macht rückgängig, was die Admittanzmatrix bewirkt: Diese rechnet von den Spannungen zu den Strömen, jene von den Strömen zu den Spannungen.

Idee der Herleitung: Man löst jeweils eine Gleichung nach der Größe auf, die in der Zielform vorgegeben ist, und setzt sie in die andere ein.

:::herleitung
**Ausgangspunkt:** die Admittanz-, Impedanz- und Kettengleichungen; die Inverse einer 2×2-Matrix.

**Annahmen:** (i) Die Ausgangsform existiert. (ii) Der Nenner, durch den geteilt wird, ist nicht null.

**Schritt 1**: Admittanz- und Impedanzform. Die Impedanzform drückt die Spannungen durch die Ströme aus, löst also die Admittanzgleichungen nach den Spannungen auf; das leistet die Inverse:

$$\mathbf Z = \mathbf Y^{-1} = \frac{1}{\det\mathbf Y}\begin{pmatrix} \underline Y_{22} & -\underline Y_{12} \\ -\underline Y_{21} & \underline Y_{11} \end{pmatrix}, \qquad \det\mathbf Y = \underline Y_{11}\underline Y_{22} - \underline Y_{12}\underline Y_{21}\,$$

Ebenso umgekehrt $\mathbf Y = \mathbf Z^{-1}$.

**Schritt 2**: Von der Admittanz- zur Kettenform. Die zweite Admittanzgleichung, nach $\underline U_1$ aufgelöst und mit $-\underline I_2$ geschrieben:

$$\underline U_1 = -\frac{\underline Y_{22}}{\underline Y_{21}}\,\underline U_2 - \frac{1}{\underline Y_{21}}\,(-\underline I_2)$$

**Schritt 3**: In die erste Admittanzgleichung eingesetzt; der Faktor vor $\underline U_2$ wird $\underline Y_{12} - \underline Y_{11}\underline Y_{22}/\underline Y_{21}$, also $-\det\mathbf Y/\underline Y_{21}$:

$$\underline I_1 = -\frac{\det\mathbf Y}{\underline Y_{21}}\,\underline U_2 - \frac{\underline Y_{11}}{\underline Y_{21}}\,(-\underline I_2)$$

Die vier Faktoren der Schritte 2 und 3 bilden $\mathbf A$.

**Schritt 4**: Von der Ketten- zur Admittanzform. Die erste Kettengleichung nach $-\underline I_2$ aufgelöst ergibt $\underline I_2$ aus den Spannungen; eingesetzt in die zweite folgt $\underline I_1$:

$$\underline I_2 = -\frac{1}{\underline A_{12}}\,\underline U_1 + \frac{\underline A_{11}}{\underline A_{12}}\,\underline U_2, \qquad \underline I_1 = \frac{\underline A_{22}}{\underline A_{12}}\,\underline U_1 + \Big(\underline A_{21} - \frac{\underline A_{11}\underline A_{22}}{\underline A_{12}}\Big)\underline U_2\,$$

Der Faktor in der Klammer ist $-\det\mathbf A/\underline A_{12}$.

**Schritt 5**: Von der Impedanz- zur Kettenform. Die zweite Impedanzgleichung nach $\underline I_1$ aufgelöst, dann in die erste eingesetzt:

$$\underline I_1 = \frac{1}{\underline Z_{21}}\,\underline U_2 + \frac{\underline Z_{22}}{\underline Z_{21}}\,(-\underline I_2), \qquad \underline U_1 = \frac{\underline Z_{11}}{\underline Z_{21}}\,\underline U_2 + \frac{\underline Z_{11}\underline Z_{22} - \underline Z_{12}\underline Z_{21}}{\underline Z_{21}}\,(-\underline I_2)\,$$

**Schritt 6**: Von der Ketten- zur Impedanzform. Die zweite Kettengleichung nach $\underline U_2$ aufgelöst, dann in die erste eingesetzt:

$$\underline U_2 = \frac{1}{\underline A_{21}}\,\underline I_1 + \frac{\underline A_{22}}{\underline A_{21}}\,\underline I_2, \qquad \underline U_1 = \frac{\underline A_{11}}{\underline A_{21}}\,\underline I_1 + \frac{\underline A_{11}\underline A_{22} - \underline A_{12}\underline A_{21}}{\underline A_{21}}\,\underline I_2\,$$

**Schritt 7** (entscheidender Schritt für die Eigenschaften): Die Determinante der Kettenmatrix aus Schritt 2 und 3:

$$\begin{aligned} \det\mathbf A &= \frac{\underline Y_{22}\,\underline Y_{11}}{\underline Y_{21}^2} - \frac{\det\mathbf Y}{\underline Y_{21}^2} \\ &= \frac{\underline Y_{11}\underline Y_{22} - \underline Y_{11}\underline Y_{22} + \underline Y_{12}\underline Y_{21}}{\underline Y_{21}^2} = \frac{\underline Y_{12}}{\underline Y_{21}} \end{aligned}$$

Aus Schritt 5 ebenso:

$$\det\mathbf A = \frac{\underline Z_{11}\underline Z_{22} - \det\mathbf Z}{\underline Z_{21}^2} = \frac{\underline Z_{12}}{\underline Z_{21}}$$

**Ergebnis:** die sechs Umrechnungen und die Determinante wie in der Formel oben.

**Woher die Faktoren kommen:** Der Nenner ist jedes Mal der Faktor der Größe, nach der aufgelöst wird; die Determinante entsteht, wo zwei Produkte von Parametern voneinander abgezogen werden.

**Proben:** RC-Glied: $-1/\underline Y_{21}$ ergibt 1 kΩ, also $\underline A_{12}$; $-\det\mathbf Y/\underline Y_{21}$ ergibt j·1 mS, also $\underline A_{21}$; $\underline Y_{12}/\underline Y_{21}$ ergibt 1, also $\det\mathbf A$. Eine beliebig gewählte Matrix ohne Symmetrie, mit (2 + j), (−0,5 + 0,2j), (3 − j) und (1 + 0,5j) mS, ergibt in beiden Richtungen dieselben Matrizen, und $\det\mathbf A$ ist dort −0,170 + 0,010j, genau $\underline Y_{12}/\underline Y_{21}$.

**Grenzen:** Ist ein Nenner null, gibt es die Zielform nicht; die Ausgangsform beschreibt das Zweitor dann weiterhin vollständig.
:::

## Reziprozität und Rückwirkungsfreiheit

*Was verraten die Parameter über das Innere eines Zweitors?*

Beim RC-Glied sind $\underline Y_{12}$ und $\underline Y_{21}$ gleich, beide −1 mS: 1 V an einem Tor treibt bei kurzgeschlossenem anderem Tor dort denselben Strom heraus, gleich in welcher Richtung. Nach dem __Umkehrungssatz__ (Reziprozitätstheorem) gilt das für jedes Zweitor aus Widerständen, Kondensatoren und Spulen, auch gekoppelten, und idealen Übertragern; ein solches Zweitor heißt __reziprok__ oder umkehrbar:

:::formel Satz
$$\underline Y_{12} = \underline Y_{21} \quad\Longleftrightarrow\quad \underline Z_{12} = \underline Z_{21} \quad\Longleftrightarrow\quad \det\mathbf A = 1$$
:::

**So liest man das:** Die drei Bedingungen sind gleichwertig, soweit die jeweilige Form existiert, und ein reziprokes Zweitor hat nur drei unabhängige Parameter. Gesteuerte Quellen heben die Reziprozität in der Regel auf, weil ihr Eintragsmuster in der Knotenleitwertmatrix unsymmetrisch ist; die Verstärkerstufe überträgt mit 0,494 mS vorwärts und mit null rückwärts. Entscheidend ist die Symmetrie der Bauelemente, nicht ihre Passivität: Es gibt passive Zweitore, die nicht reziprok sind, etwa Richtungsleitungen aus vormagnetisiertem Ferrit in der Hochfrequenztechnik, die Signale nur in einer Richtung durchlassen.

**Kurz gesagt:** In einem Zweitor aus Widerständen, Kondensatoren und Spulen ist der Kurzschlussstrom am einen Tor je Volt am anderen in beiden Richtungen derselbe.

Idee der Herleitung: Die Übertragungsimpedanzen sind Einträge der Inversen der Knotenleitwertmatrix; diese ist für R, L und C symmetrisch, und mit ihr ihre Inverse.

:::herleitung
**Ausgangspunkt:** die Knotengleichungen $\mathbf Y_\mathrm K\,\underline{\vec U} = \underline{\vec I}_q$ mit den Knotenpotentialen $\underline{\vec U}$ und den eingespeisten Strömen $\underline{\vec I}_q$; die Teststromquelle zwischen zwei Knoten aus dem Artikel über Testquellen.

**Annahmen:** (i) Das Zweitor besteht aus Widerständen, Kondensatoren und Spulen, die Spulen auch magnetisch gekoppelt. (ii) $\mathbf Y_\mathrm K$ ist invertierbar; dann hat die Schaltung mit Stromquellen an den Toren eine eindeutige Lösung, und die Impedanzform existiert. Sind die Tore galvanisch getrennt, verbindet man vorher 1′ mit 2′; über diese eine Verbindung fließt kein Strom, und das Torverhalten bleibt gleich.

**Schritt 1**: Jeder Zweipol trägt seine Admittanz mit Plus in die Diagonalplätze seiner beiden Knoten und mit Minus in die beiden Nebenplätze ein; dieses Muster ist symmetrisch. Gekoppelte Spulen, deren Magnetfelder einander durchsetzen, tragen die Inverse ihrer Induktivitätsmatrix ein, der Matrix aus Selbst- und Gegeninduktivitäten, geteilt durch jω; weil die Gegeninduktivität in beiden Richtungen gleich ist, sind beide Matrizen symmetrisch. Also ist $\mathbf Y_\mathrm K$ symmetrisch, gleich ihrer __Transponierten__, der an der Diagonalen gespiegelten Matrix; und mit ihr ist ihre Inverse symmetrisch, denn die Inverse der Transponierten ist die Transponierte der Inversen.

**Schritt 2**: Für den Leerlaufversuch an Tor 1 speist eine Stromquelle $\underline I_1$ in Klemme 1 und nimmt ihn an Klemme 1′ wieder auf. Die rechte Seite ist $\underline I_1\,\vec t_1$, wobei der __Torvektor__ $\vec t_1$ in der Zeile von Klemme 1 eine 1, in der von 1′ eine −1 und sonst Nullen enthält (liegt 1′ auf dem Bezugsknoten, entfällt die −1); $\vec t_2$ entsprechend für Tor 2.

**Schritt 3**: Die Potentiale sind $\mathbf Y_\mathrm K^{-1}\,\vec t_1\,\underline I_1$. Die Spannung an Tor 2 ist das Potential von Klemme 2 minus das von 2′, also das Skalarprodukt mit $\vec t_2$:

$$\underline Z_{21} = \frac{\underline U_2}{\underline I_1}\bigg|_{\underline I_2 = 0} = \vec t_2^{\,\mathsf T}\,\mathbf Y_\mathrm K^{-1}\,\vec t_1, \qquad \underline Z_{12} = \vec t_1^{\,\mathsf T}\,\mathbf Y_\mathrm K^{-1}\,\vec t_2\,$$

**Schritt 4** (entscheidender Schritt): Eine Zahl ist gleich ihrer Transponierten. Mit der Symmetrie aus Schritt 1:

$$\underline Z_{12} = \big(\vec t_1^{\,\mathsf T}\,\mathbf Y_\mathrm K^{-1}\,\vec t_2\big)^{\mathsf T} = \vec t_2^{\,\mathsf T}\,\big(\mathbf Y_\mathrm K^{-1}\big)^{\mathsf T}\,\vec t_1 = \vec t_2^{\,\mathsf T}\,\mathbf Y_\mathrm K^{-1}\,\vec t_1 = \underline Z_{21}$$

**Schritt 5**: Die beiden anderen Bedingungen folgen aus der Umrechnung. Nach ihr ist

$$\underline Y_{12} = -\frac{\underline Z_{12}}{\det\mathbf Z}, \qquad \underline Y_{21} = -\frac{\underline Z_{21}}{\det\mathbf Z}, \qquad \det\mathbf A = \frac{\underline Z_{12}}{\underline Z_{21}}\,$$

Die beiden Admittanzen sind also genau dann gleich, wenn $\underline Z_{12}$ und $\underline Z_{21}$ es sind, und genau dann ist $\det\mathbf A$ gleich 1.

**Ergebnis:**

$$\underline Y_{12} = \underline Y_{21} \quad\Longleftrightarrow\quad \underline Z_{12} = \underline Z_{21} \quad\Longleftrightarrow\quad \det\mathbf A = 1$$

**Woher die Faktoren kommen:** Die Gleichheit stammt allein aus der Symmetrie der Eintragsmuster, nicht aus der Größe der Bauteile; deshalb gilt sie für jede Bemessung und jede Frequenz.

**Proben:** RC-Glied: $\underline Z_{12}$ und $\underline Z_{21}$ sind beide −j kΩ, $\det\mathbf A$ ist 1. Gegenprobe: In der Knotenleitwertmatrix der Verstärkerstufe steht die gesteuerte Quelle mit +1 mS in Zeile D, Spalte G, aber nicht in Zeile G, Spalte D; die Matrix ist unsymmetrisch. Mit Signalquelle und Last, wie im Artikel über Ersatzquellen, erzeugt 1 µA in das Gate −23,26 mV am Drain, 1 µA in den Drain aber nichts am Gate.

**Grenzen:** Ideale Übertrager haben kein Eintragsmuster in der Knotenleitwertmatrix; als Grenzfall fest gekoppelter Spulen sind sie ebenfalls reziprok. Gibt es keine Impedanzform, führt dasselbe Argument mit der Matrix der modifizierten Knotenanalyse zum Ziel, deren Einträge für Spannungsquellen an den Toren ebenfalls symmetrisch sind.
:::

Ein Zweitor, in dem der Ausgang überhaupt nicht auf den Eingang wirkt, nennt man __rückwirkungsfrei__; überträgt es vorwärts, ist es der Grenzfall eines nicht reziproken Zweitors. Nach der Umrechnung sind dafür, soweit die Formen existieren, drei Bedingungen gleichwertig, denn $\underline Z_{12}$ ist $-\underline Y_{12}/\det\mathbf Y$ und $\det\mathbf A$ ist $\underline Y_{12}/\underline Y_{21}$:

$$\underline Y_{12} = 0 \quad\Longleftrightarrow\quad \underline Z_{12} = 0 \quad\Longleftrightarrow\quad \det\mathbf A = 0$$

Die Verstärkerstufe mit Source-Widerstand ist rückwirkungsfrei, deshalb beschreibt sie das Ersatzzweitor mit drei Kenngrößen vollständig. Sie ist zugleich __aktiv__, kann also insgesamt mehr Wirkleistung abgeben, als sie aufnimmt: Bei 10 mV am Gate liefert sie an 10 kΩ eine Amplitude von 23,26 mV und damit 27 nW, während das Gate keine Leistung aufnimmt; die Energie stammt aus der Versorgungsspannung. Ein __passives__ Zweitor wie das RC-Glied kann insgesamt nie mehr Wirkleistung abgeben, als es aufnimmt.

## Rückwirkung im Betrieb: die Eingangsadmittanz unter Last

*Welche Admittanz sieht eine Quelle am Eingang, wenn am Ausgang eine Last hängt, und warum ist das nicht $\underline Y_{11}$?*

:::grafik
Szene: st1/netzwerkanalyse/05-rueckwirkung-cgd · Vorlage: schaltbild-kurve
**Abbildung 3:** (a) Kleinsignal-Ersatzschaltbild der Stufe ohne Source-Widerstand als Zweitor mit Tor 1 zwischen Gate und Masse und Tor 2 zwischen Drain und Masse, bei ω = 10⁸ 1/s: $C_{gs}$ = 100 fF vom Gate nach Masse, $C_{gd}$ = 20 fF vom Gate zum Drain, gesteuerte Quelle $g_m\underline U_1$ mit $g_m$ = 1 mS vom Drain nach Masse, $G_D + g_o$ = 125 µS am Drain; außerhalb die Last $R_L$. (b) Eingangskapazität $C_\mathrm{ein}$ in fF (100 bis 300) über $R_L$ in kΩ (0,1 bis 1000, logarithmisch): 122 fF bei 0,1 kΩ, 138 fF bei 1 kΩ, 209 fF bei 10 kΩ, 268 fF bei 100 kΩ, 279 fF bei 1 MΩ; gestrichelt die Grenzen 120 fF bei kurzgeschlossenem und 280 fF bei offenem Ausgang. Über die Gate-Drain-Kapazität sieht der Eingang die Last.
:::

**Die Akteure:**

- __$C_{gs}$__, __$C_{gd}$__: Gate-Source- und Gate-Drain-Kapazität der Stufe ohne Source-Widerstand, 100 fF und 20 fF wie im Artikel über die modifizierte Knotenanalyse.
- __$g_m$__ = 1 mS und __$g_o$__ = 25 µS wie bei der Verstärkerstufe oben; die gesteuerte Quelle liefert $g_m$ mal Gate-Source-Spannung. __$G_D$__: Leitwert des Drainwiderstands, 1/$R_D$ = 100 µS; mit $g_o$ zusammen 125 µS am Drain.
- __$\underline Y_L$__: Admittanz der Last am Ausgang; 0,1 mS für $R_L$ = 10 kΩ.
- __$\underline Y_\mathrm{ein}$__: Eingangsadmittanz im Betrieb, $\underline I_1/\underline U_1$ mit angeschlossener Last. __$C_\mathrm{ein}$__: die Kapazität, die ihr Imaginärteil darstellt, Imaginärteil durch ω.

**Das Zusammenspiel:**

**Schritt 1**: $\underline Y_{11}$ ist mit kurzgeschlossenem Ausgang definiert. Im Betrieb hängt dort eine Last, und die Ausgangsspannung ist nicht null.

**Schritt 2**: Die Last nimmt den Strom $\underline Y_L\,\underline U_2$ auf, der aus dem Zweitor herausfließt; $\underline I_2$ ist also $-\underline Y_L\,\underline U_2$. Mit der zweiten Admittanzgleichung folgt die Ausgangsspannung; die Stufe verstärkt mit 10 kΩ Last −4,44-fach.

**Schritt 3**: Über $\underline Y_{12}$ treibt diese Ausgangsspannung einen zusätzlichen Strom in den Eingang, den die Quelle als veränderte Admittanz spürt.

**Schritt 4**: Ohne Rückwirkung, mit $\underline Y_{12}$ = 0, bleibt die Eingangsadmittanz für jede Last $\underline Y_{11}$.

**Schritt 5**: In der Stufe verbindet nur $C_{gd}$ den Drain mit dem Gate; $\underline Y_{12}$ ist $-j\omega C_{gd}$, bei 10⁸ 1/s nur −j·2 µS, 0,2 % von $\underline Y_{21}$. Mit der Verstärkung multipliziert wirken die 20 fF am Eingang aber wie 20 fF mal (1 + 4,44), also 109 fF: Die Eingangskapazität steigt von 120 fF bei kurzgeschlossenem Ausgang auf 209 fF mit Last und 280 fF offen (Abbildung 3 b). Diese Vervielfachung heißt __Miller-Effekt__; sie begrenzt die Bandbreite von Verstärkerstufen.

:::formel Formel
$$\underline Y_\mathrm{ein} = \frac{\underline I_1}{\underline U_1} = \underline Y_{11} - \frac{\underline Y_{12}\,\underline Y_{21}}{\underline Y_{22} + \underline Y_L}, \qquad \frac{\underline U_2}{\underline U_1} = -\frac{\underline Y_{21}}{\underline Y_{22} + \underline Y_L}\,$$
:::

**So liest man das:** Die Eingangsadmittanz hängt über das Produkt aus Rückwärts- und Vorwärtsübertragung von der Last ab: Kurzgeschlossen bleibt $\underline Y_{11}$, offen ergibt sich $1/\underline Z_{11}$, jede Last liegt dazwischen. Ebenso hängt die Ausgangsadmittanz von der Quelle am Eingang ab, mit deren Admittanz $\underline Y_\mathrm{sig}$:

$$\underline Y_\mathrm{aus} = \underline Y_{22} - \frac{\underline Y_{12}\,\underline Y_{21}}{\underline Y_{11} + \underline Y_\mathrm{sig}}$$

**Kurz gesagt:** Ohne Rückwirkung sieht der Eingang die Last nicht.

Idee der Herleitung: Man ersetzt in der zweiten Admittanzgleichung den Ausgangsstrom durch den Laststrom, löst nach der Ausgangsspannung auf und setzt sie in die erste ein.

:::herleitung
**Ausgangspunkt:** die Admittanzgleichungen und die Last als Zweipol am Ausgang.

**Annahmen:** (i) Die Last ist ein linearer Zweipol mit der Admittanz $\underline Y_L$. (ii) $\underline Y_{22} + \underline Y_L$ ist nicht null. (iii) Für die Ausgangsadmittanz ist $\underline Y_{11} + \underline Y_\mathrm{sig}$ nicht null.

**Schritt 1**: Der Strom $\underline I_2$ fließt in das Zweitor hinein, also aus der Last heraus; die Last nimmt bei der Spannung $\underline U_2$ den Strom $\underline Y_L\,\underline U_2$ auf:

$$\underline I_2 = -\underline Y_L\,\underline U_2$$

**Schritt 2**: In die zweite Admittanzgleichung eingesetzt und nach $\underline U_2$ aufgelöst:

$$-\underline Y_L\,\underline U_2 = \underline Y_{21}\,\underline U_1 + \underline Y_{22}\,\underline U_2, \qquad \underline U_2 = -\frac{\underline Y_{21}}{\underline Y_{22} + \underline Y_L}\,\underline U_1\,$$

**Schritt 3** (entscheidender Schritt): In die erste Admittanzgleichung eingesetzt; der Eingangsstrom bekommt über $\underline Y_{12}$ einen Anteil, der von der Last abhängt:

$$\underline I_1 = \underline Y_{11}\,\underline U_1 + \underline Y_{12}\,\underline U_2 = \Big(\underline Y_{11} - \frac{\underline Y_{12}\,\underline Y_{21}}{\underline Y_{22} + \underline Y_L}\Big)\underline U_1$$

**Schritt 4**: Für die Ausgangsadmittanz dieselben Schritte mit vertauschten Toren. Die Quelle am Eingang ist abgeschaltet und wirkt als Admittanz $\underline Y_\mathrm{sig}$, die den Strom aus Tor 1 aufnimmt. In die erste Admittanzgleichung eingesetzt und nach $\underline U_1$ aufgelöst:

$$-\underline Y_\mathrm{sig}\,\underline U_1 = \underline Y_{11}\,\underline U_1 + \underline Y_{12}\,\underline U_2, \qquad \underline U_1 = -\frac{\underline Y_{12}}{\underline Y_{11} + \underline Y_\mathrm{sig}}\,\underline U_2\,$$

In die zweite eingesetzt:

$$\underline I_2 = \Big(\underline Y_{22} - \frac{\underline Y_{12}\,\underline Y_{21}}{\underline Y_{11} + \underline Y_\mathrm{sig}}\Big)\underline U_2$$

**Ergebnis:**

$$\underline Y_\mathrm{ein} = \underline Y_{11} - \frac{\underline Y_{12}\,\underline Y_{21}}{\underline Y_{22} + \underline Y_L}, \qquad \frac{\underline U_2}{\underline U_1} = -\frac{\underline Y_{21}}{\underline Y_{22} + \underline Y_L}, \qquad \underline Y_\mathrm{aus} = \underline Y_{22} - \frac{\underline Y_{12}\,\underline Y_{21}}{\underline Y_{11} + \underline Y_\mathrm{sig}}\,$$

**Woher die Faktoren kommen:** $\underline Y_{21}$ trägt das Signal zum Ausgang, die Last bestimmt mit $\underline Y_{22}$ die Spannung dort, und $\underline Y_{12}$ trägt sie zurück; der Bruch ist der Weg einmal hin und zurück.

**Proben:** Einheit S. Grenzfall offener Ausgang, mit der Umrechnung in die Impedanzform:

$$\underline Y_\mathrm{ein}\Big|_{\underline Y_L = 0} = \frac{\underline Y_{11}\underline Y_{22} - \underline Y_{12}\underline Y_{21}}{\underline Y_{22}} = \frac{1}{\underline Z_{11}}$$

RC-Glied mit 1 kΩ Last: 1 − 1/(2 + j), also (0,6 + 0,2j) mS, der Kehrwert von 1 kΩ in Reihe mit Kondensator und Last parallel, (1,5 − 0,5j) kΩ.

**Grenzen:** Eine Last, die ihrerseits mit dem Eingang verbunden ist, verletzt Annahme (i); dann ist die Gesamtschaltung neu zu berechnen.
:::

::::beispiel Eingangskapazität einer Stufe mit Gate-Drain-Kapazität
**Gegeben:** Stufe ohne Source-Widerstand, $C_{gs}$ = 100 fF, $C_{gd}$ = 20 fF, $g_m$ = 1 mS, $G_D + g_o$ = 125 µS, Last $R_L$ = 10 kΩ, also 100 µS; ω = 10⁸ 1/s, also $j\omega C_{gs}$ = j·10 µS und $j\omega C_{gd}$ = j·2 µS.

**Gesucht:** die Admittanzmatrix und die Eingangskapazität bei kurzgeschlossenem Ausgang, mit 10 kΩ und offen.

**Rechnung:** Kurzschlussversuche: Mit kurzgeschlossenem Drain liegen beide Kapazitäten am Gate gegen Masse; in den Drain fließt von außen der Strom der gesteuerten Quelle, vermindert um den Strom, der über $C_{gd}$ vom Gate ankommt. Mit kurzgeschlossenem Gate sieht der Drain $G_D + g_o$ und $C_{gd}$:

$$\mathbf Y = \begin{pmatrix} j\omega(C_{gs} + C_{gd}) & -j\omega C_{gd} \\ g_m - j\omega C_{gd} & G_D + g_o + j\omega C_{gd} \end{pmatrix}$$

$$\mathbf Y = \begin{pmatrix} j\,12 & -j\,2 \\ 1000 - j\,2 & 125 + j\,2 \end{pmatrix}\mathrm{\mu S}$$

Mit 10 kΩ Last, in µS:

$$\underline Y_\mathrm{ein} = j\,12 - \frac{(-j\,2)(1000 - j\,2)}{225 + j\,2} = (0{,}097 + j\,20{,}89)\ \mathrm{\mu S}, \qquad C_\mathrm{ein} = \frac{20{,}89\ \mathrm{\mu S}}{10^8\ \mathrm{s^{-1}}} = 208{,}9\ \mathrm{fF}\,$$

Offen ergibt dieselbe Formel mit 125 + j·2 im Nenner (0,288 + j·28,0) µS, also 280,0 fF; kurzgeschlossen bleibt $\underline Y_{11}$ mit 120 fF. Die Verstärkung mit Last ist $-(1000 - j\,2)/(225 + j\,2)$, also −4,444 + 0,048j. Dieselbe Zahl in anderer Ordnung: Der Eingangsstrom ist $\underline Y_{11}\underline U_1 + \underline Y_{12}\underline U_2$, und mit dieser Verstärkung wird daraus exakt

$$\begin{aligned} \underline Y_\mathrm{ein} &= j\omega C_{gs} + j\omega C_{gd}\Big(1 - \frac{\underline U_2}{\underline U_1}\Big) \\ &= j\,10 + j\,2\,(5{,}444 - 0{,}048j) \\ &= (0{,}097 + j\,20{,}89)\ \mathrm{\mu S} \end{aligned}$$

**Ergebnis:** **$C_\mathrm{ein}$ = 120 fF bei kurzgeschlossenem Ausgang, 208,9 fF mit 10 kΩ Last und 280,0 fF bei offenem Ausgang.**

**Einordnung:** Die Gate-Drain-Kapazität wirkt mit dem Faktor 1 plus Verstärkungsbetrag, 5,44 mit Last und 9 ohne. Treibt eine Signalquelle mit 10 kΩ das Gate, rückt die Ecke des Tiefpasses aus Quellwiderstand und Eingangskapazität grob abgeschätzt von 159 MHz mit $C_{gs}$ allein auf 76 MHz.
::::

:::fehlvorstellung
„$\underline Y_{11}$ ist die Eingangsadmittanz des Zweitors.“ Das liegt nahe, weil $\underline Y_{11}$ Kurzschluss-Eingangsadmittanz heißt und beim rückwirkungsfreien Ersatzzweitor tatsächlich die Eingangsadmittanz ist. Sie ist es aber nur bei kurzgeschlossenem Ausgang. In der Stufe mit Gate-Drain-Kapazität ist $\underline Y_{11}$ eine Kapazität von 120 fF; mit der Last von 10 kΩ sieht die Quelle 209 fF, das 1,74-Fache. Auch passive Zweitore wirken zurück: Die Eingangsadmittanz des zweistufigen RC-Tiefpasses, im Artikel über Testquellen bei offenem Ausgang zu (0,667 + 0,333j) mS bestimmt, sinkt mit 1 kΩ Last auf (0,600 + 0,300j) mS.
:::

## Kettenschaltung: Matrizen multiplizieren statt Übertragungen

*Wie berechnet man hintereinandergeschaltete Zweitore, und warum ist die Übertragung einer Kette nicht das Produkt der Einzelübertragungen?*

:::grafik
Szene: st1/netzwerkanalyse/05-rc-kette · Vorlage: schaltbild-kurve
**Abbildung 4:** (a) Zwei RC-Glieder (je 1 kΩ längs, 100 nF quer) in Kette, der zweistufige RC-Tiefpass; über jedem Glied seine Kettenmatrix, über beiden das Produkt mit den Einträgen 3j, (2 + j) kΩ, (−1 + 2j) mS und 1 + j. Am Verbindungsknoten der Strom, der das erste Glied als $-\underline I_{2\mathrm a}$ verlässt und als $\underline I_{1\mathrm b}$ in das zweite fließt; daneben die Eingangsimpedanz des zweiten Glieds, (1 − j) kΩ, als Last des ersten. (b) Betrag der Leerlauf-Spannungsübertragung über ω von 10² bis 10⁶ 1/s (logarithmisch): Kette 0,967 bei 10³, 0,333 bei 10⁴ und 0,0097 bei 10⁵ 1/s; gestrichelt das Produkt der Einzelübertragungen, 0,990, 0,500 und 0,0099. Das zweite Glied belastet das erste; deshalb ist die Kette nicht das Produkt der Einzelübertragungen, die Kettenmatrix aber das Produkt der Kettenmatrizen.
:::

**Die Akteure:**

- __$\mathbf A_\mathrm a$__, __$\mathbf A_\mathrm b$__: Kettenmatrizen des ersten und des zweiten Glieds; ihre Torgrößen tragen den Index a bzw. b. __$\mathbf A$__: Kettenmatrix der ganzen Kette.

Das Produkt zweier Matrizen ist die Matrix, die dasselbe bewirkt wie beide nacheinander: Ihr Eintrag in Zeile i und Spalte k ist die Summe der Produkte aus Zeile i der linken und Spalte k der rechten Matrix. Längsglied mit 1 kΩ mal Querglied mit j·1 mS ergibt die Kettenmatrix des RC-Glieds; in umgekehrter Reihenfolge entsteht eine andere Matrix, denn beim Matrizenprodukt kommt es auf die Reihenfolge an:

$$\begin{pmatrix} 1 & 1\ \mathrm{k\Omega} \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ j\cdot 1\ \mathrm{mS} & 1 \end{pmatrix} = \begin{pmatrix} 1 + j & 1\ \mathrm{k\Omega} \\ j\cdot 1\ \mathrm{mS} & 1 \end{pmatrix}, \qquad \begin{pmatrix} 1 & 0 \\ j\cdot 1\ \mathrm{mS} & 1 \end{pmatrix}\begin{pmatrix} 1 & 1\ \mathrm{k\Omega} \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1\ \mathrm{k\Omega} \\ j\cdot 1\ \mathrm{mS} & 1 + j \end{pmatrix}\,$$

**Das Zusammenspiel:**

**Schritt 1**: In der __Kettenschaltung__ ist das Ausgangstor des ersten Glieds mit dem Eingangstor des zweiten verbunden: gleiche Spannung, und der Strom, der das erste Glied verlässt, fließt in das zweite hinein. Die Torbedingung gilt von selbst, weil die Tore nur über zwei Leitungen verbunden sind.

**Schritt 2**: Wegen $-\underline I_2$ in der Kettenform ist der Ausgangsvektor des ersten Glieds genau der Eingangsvektor des zweiten.

**Schritt 3**: Setzt man die Kettengleichung des zweiten Glieds in die des ersten ein, steht vor den Ausgangsgrößen das Produkt der Matrizen, in der Reihenfolge der Glieder.

**Schritt 4**: Jede Einzelübertragung $1/\underline A_{11}$ gilt bei offenem Ausgang. In der Kette belastet das zweite RC-Glied das erste mit seiner Eingangsimpedanz (1 − j) kΩ; zwischen den Gliedern liegen je Volt am Eingang nur 0,333 − 0,333j statt 0,5 − 0,5j.

**Schritt 5**: Die Kette überträgt bei ω = 10⁴ 1/s den Betrag 1/3; das Produkt der Einzelübertragungen ergäbe 1/2, um 50 % zu viel. Die Kettenmatrix enthält die Belastung, weil $\underline A_{21}$ und $\underline A_{22}$ des zweiten Glieds den Strom beschreiben, den es aufnimmt.

:::formel Satz
$$\mathbf A = \mathbf A_\mathrm a\,\mathbf A_\mathrm b$$
:::

**So liest man das:** Links steht das Glied am Eingang; mehr Glieder ergeben $\mathbf A_\mathrm a\mathbf A_\mathrm b\mathbf A_\mathrm c\cdots$. Mit einer Last $\underline Y_L$ am Ende ist $-\underline I_2$ gleich $\underline Y_L\,\underline U_2$, und es folgen Übertragung und Eingangsadmittanz der Kette:

$$\frac{\underline U_2}{\underline U_1} = \frac{1}{\underline A_{11} + \underline A_{12}\,\underline Y_L}, \qquad \underline Y_\mathrm{ein} = \frac{\underline A_{21} + \underline A_{22}\,\underline Y_L}{\underline A_{11} + \underline A_{12}\,\underline Y_L}\,$$

Die Einzelübertragungen multiplizieren sich nur, wenn das zweite Glied das erste nicht belastet, wenn es also bei offenem Ausgang keinen Strom aufnimmt oder das erste Glied seine Ausgangsspannung unabhängig vom Ausgangsstrom hält: Zwei Verstärkerstufen, deren Gates keinen Strom ziehen, verstärken offen 19,32-fach, genau 4,396².

**Kurz gesagt:** Die Kettenmatrix einer Kette ist das Produkt der Kettenmatrizen in der Reihenfolge der Glieder.

Idee der Herleitung: Man setzt die Kettengleichung des zweiten Glieds in die des ersten ein und multipliziert aus.

:::herleitung
**Ausgangspunkt:** die Kettengleichungen beider Glieder und die Verbindungsbedingungen am gemeinsamen Tor.

**Annahmen:** (i) Beide Glieder haben eine Kettenform. (ii) Sie sind nur über die beiden Leitungen des gemeinsamen Tors verbunden.

**Schritt 1**: Die Kettengleichungen der beiden Glieder:

$$\begin{pmatrix} \underline U_{1\mathrm a} \\ \underline I_{1\mathrm a} \end{pmatrix} = \mathbf A_\mathrm a\begin{pmatrix} \underline U_{2\mathrm a} \\ -\underline I_{2\mathrm a} \end{pmatrix}, \qquad \begin{pmatrix} \underline U_{1\mathrm b} \\ \underline I_{1\mathrm b} \end{pmatrix} = \mathbf A_\mathrm b\begin{pmatrix} \underline U_{2\mathrm b} \\ -\underline I_{2\mathrm b} \end{pmatrix}\,$$

**Schritt 2**: Am gemeinsamen Tor gleiche Spannung, und der Strom aus dem ersten Glied fließt in das zweite:

$$\underline U_{2\mathrm a} = \underline U_{1\mathrm b}, \qquad -\underline I_{2\mathrm a} = \underline I_{1\mathrm b}\,$$

**Schritt 3** (entscheidender Schritt): Der rechte Vektor der ersten Gleichung ist damit der linke der zweiten; eingesetzt:

$$\begin{pmatrix} \underline U_{1\mathrm a} \\ \underline I_{1\mathrm a} \end{pmatrix} = \mathbf A_\mathrm a\,\mathbf A_\mathrm b\begin{pmatrix} \underline U_{2\mathrm b} \\ -\underline I_{2\mathrm b} \end{pmatrix}$$

**Schritt 4**: Ausgeschrieben ist das Produkt zweier 2×2-Matrizen, Zeile mal Spalte:

$$\underline A_{11} = \underline A_{11\mathrm a}\underline A_{11\mathrm b} + \underline A_{12\mathrm a}\underline A_{21\mathrm b}, \qquad \underline A_{12} = \underline A_{11\mathrm a}\underline A_{12\mathrm b} + \underline A_{12\mathrm a}\underline A_{22\mathrm b}\,$$

$$\underline A_{21} = \underline A_{21\mathrm a}\underline A_{11\mathrm b} + \underline A_{22\mathrm a}\underline A_{21\mathrm b}, \qquad \underline A_{22} = \underline A_{21\mathrm a}\underline A_{12\mathrm b} + \underline A_{22\mathrm a}\underline A_{22\mathrm b}\,$$

**Schritt 5**: Mit einer Last am Ende ist $-\underline I_2$ gleich $\underline Y_L\,\underline U_2$; die Kettengleichungen ergeben dann:

$$\underline U_1 = (\underline A_{11} + \underline A_{12}\,\underline Y_L)\,\underline U_2, \qquad \underline I_1 = (\underline A_{21} + \underline A_{22}\,\underline Y_L)\,\underline U_2\,$$

Das Verhältnis der beiden Spannungen ist die Übertragung, der Quotient $\underline I_1/\underline U_1$ die Eingangsadmittanz.

**Ergebnis:**

$$\mathbf A = \mathbf A_\mathrm a\,\mathbf A_\mathrm b$$

**Woher die Faktoren kommen:** Im Eintrag $\underline A_{11}$ der Kette steht neben $\underline A_{11\mathrm a}\underline A_{11\mathrm b}$, dem Produkt der beiden Leerlaufübertragungen, das Glied $\underline A_{12\mathrm a}\underline A_{21\mathrm b}$: der Längsanteil des ersten Glieds mal dem Strom, den das zweite aufnimmt. Es ist die Belastung.

**Proben:** Einheiten: $\underline A_{12\mathrm a}\underline A_{21\mathrm b}$ ist Ω mal S, ohne Einheit wie $\underline A_{11}$. RC-Tiefpass: $(1 + j)^2 + 1\ \mathrm{k\Omega}\cdot j\cdot 1\ \mathrm{mS}$ ergibt 2j + j, also 3j, ohne das Belastungsglied nur 2j. Determinante: Nach dem Determinantenproduktsatz ist die Determinante eines Produkts das Produkt der Determinanten; eine Kette reziproker Glieder mit Determinante 1 ist wieder reziprok.

**Grenzen:** Hat ein Glied keine Kettenform, etwa ein Zweitor ohne Vorwärtsübertragung, rechnet man die Kette mit einer anderen Form oder direkt.
:::

::::beispiel Zweistufiger RC-Tiefpass als Kette zweier RC-Glieder
**Gegeben:** zwei RC-Glieder mit je 1 kΩ und 100 nF bei ω = 10⁴ 1/s; Kettenmatrix eines Glieds mit 1 + j, 1 kΩ, j·1 mS und 1.

**Gesucht:** Kettenmatrix der Kette, Leerlaufübertragung, Eingangs- und Ausgangsimpedanz.

**Rechnung:** Zeile mal Spalte, in kΩ und mS:

$$\mathbf A = \begin{pmatrix} (1 + j)^2 + j & (1 + j) + 1 \\ j(1 + j) + j & j + 1 \end{pmatrix} = \begin{pmatrix} 3j & (2 + j)\ \mathrm{k\Omega} \\ (-1 + 2j)\ \mathrm{mS} & 1 + j \end{pmatrix}$$

Leerlaufübertragung, verglichen mit dem Produkt der Einzelübertragungen:

$$\frac{\underline U_2}{\underline U_1} = \frac{1}{3j} = -\frac{j}{3}, \qquad \Big(\frac{1}{1 + j}\Big)^2 = \frac{1}{2j} = -\frac{j}{2}\,$$

Eingangsimpedanz bei offenem Ausgang und Ausgangsimpedanz bei kurzgeschlossenem Eingang:

$$\underline Z_{11} = \frac{\underline A_{11}}{\underline A_{21}} = \frac{3j}{-1 + 2j}\ \mathrm{k\Omega} = (1{,}2 - 0{,}6j)\ \mathrm{k\Omega}, \qquad \frac{1}{\underline Y_{22}} = \frac{\underline A_{12}}{\underline A_{11}} = \frac{2 + j}{3j}\ \mathrm{k\Omega} = (0{,}333 - 0{,}667j)\ \mathrm{k\Omega}\,$$

**Ergebnis:** **Die Kette überträgt offen −j/3, Betrag 0,333; Eingangsimpedanz (1,2 − 0,6j) kΩ, Ausgangsimpedanz (0,333 − 0,667j) kΩ.**

**Einordnung:** Dieselben drei Zahlen lieferte im Artikel über Testquellen die modifizierte Knotenanalyse der ganzen Schaltung; hier entstehen sie aus zwei 2×2-Matrizen. Das Produkt der Einzelübertragungen läge um 50 % zu hoch; weit unterhalb und oberhalb der Eckfrequenz ist der Fehler klein, 0,967 gegen 0,990 bei 10³ 1/s.

**Variation:** Reihenfolge mit der Verstärkerstufe und 10 kΩ Last: RC-Glied vor der Stufe ergibt 1,644 mit Winkel 135°, die Stufe vor dem RC-Glied nur 0,435 mit Winkel 101°. Gemessen an der Stufe allein, 2,326, lässt das RC-Glied davor das 0,707-Fache durch, dahinter nur das 0,187-Fache: Dort lädt der Kondensator über die 8,90 kΩ der Stufe und den Widerstand des RC-Glieds, parallel zur Last rund 5 kΩ statt 1 kΩ, und die Eckfrequenz sinkt auf ein Fünftel.
::::

:::fehlvorstellung
„Die Übertragung einer Kette ist das Produkt der Einzelübertragungen.“ Das liegt nahe, weil man Blöcke in Signalflussplänen so verknüpft. Es gilt aber nur, wenn kein Glied den Ausgang des vorigen belastet oder wenn man jede Einzelübertragung unter der tatsächlichen Last bestimmt. Der zweistufige RC-Tiefpass überträgt bei seiner Eckfrequenz 1/3, nicht 1/2, weil das zweite Glied dem ersten (1 − j) kΩ als Last anbietet; die Kettenmatrix erfasst das.
:::

## Parallel- und Reihenschaltung

*Wann darf man bei zusammengeschalteten Zweitoren die Admittanz- bzw. Impedanzmatrizen addieren?*

:::grafik
Szene: st1/netzwerkanalyse/05-reihenschaltung-t · Vorlage: schaltbild-vergleich
**Abbildung 5:** Zwei T-Glieder aus je drei Widerständen von 1 kΩ, Eingänge in Reihe, Ausgänge in Reihe. (a) Beide mit durchgehender unterer Leitung: Die untere Leitung des oberen Glieds verbindet die oberen Klemmen des unteren Glieds; mit 1 mA in Tor 1 und offenem Tor 2 fließen je 0,5 mA in die beiden oberen Klemmen des unteren Glieds, aber 1 mA aus seiner Klemme 1′ (Strompfeile mit Werten, rot markiert); Potentiale 3,5 V, 2,5 V, 1,5 V und 1,0 V; Impedanzmatrix 3,5, 2,5, 2,5 und 3,5 kΩ statt der Summe 4, 2, 2 und 4 kΩ. (b) Das untere Glied umgedreht, seine durchgehende Leitung oben an der unteren Leitung des oberen Glieds: Impedanzmatrix gleich der Summe. (c) Brune-Test: Eingänge in Reihe mit 1 mA gespeist, Ausgänge offen und noch nicht verbunden; zwischen den zu verbindenden Ausgangsklemmen liegen in (a) 1 V, in (b) 0 V. Ob man Impedanzmatrizen addieren darf, entscheidet die Torbedingung jedes Teils.
:::

Bei der __Parallelschaltung__ liegen die Eingangstore zweier Zweitore parallel und ebenso die Ausgangstore: Beide Teile haben dieselben Torspannungen, ihre Torströme addieren sich, also addieren sich die Admittanzmatrizen. Bei der __Reihenschaltung__ liegen die Tore in Reihe: Durch beide Teile fließen dieselben Torströme, ihre Spannungen addieren sich, also addieren sich die Impedanzmatrizen.

**Die Akteure:**

- __$\mathbf Y_\mathrm a$__, __$\mathbf Y_\mathrm b$__ bzw. __$\mathbf Z_\mathrm a$__, __$\mathbf Z_\mathrm b$__: Admittanz- bzw. Impedanzmatrizen der beiden Teile; für das T-Glied aus drei 1-kΩ-Widerständen 2, 1, 1 und 2 kΩ.

:::formel Satz
$$\mathbf Y = \mathbf Y_\mathrm a + \mathbf Y_\mathrm b \quad\text{(parallel)}, \qquad \mathbf Z = \mathbf Z_\mathrm a + \mathbf Z_\mathrm b \quad\text{(in Reihe)}$$
:::

**So liest man das:** Alle vier Einträge addieren sich, bei mehr als zwei Teilen ebenso, solange jedes Teil seine Torbedingung behält. Ein Längsglied zwischen Eingang und Ausgang, etwa die Gate-Drain-Kapazität, ist ein parallel geschaltetes Zweitor: Die Stufe aus dem Abschnitt *Rückwirkung im Betrieb* ist das Transistor-Zweitor mit j·10, 0, 1000 und 125 µS plus das Längsglied $C_{gd}$ mit j·2, −j·2, −j·2 und j·2 µS, und die Summe ist ihre Admittanzmatrix; die ganze Rückwirkung stammt aus dem Längsglied. Bei Schaltungen an gemeinsamer Masse ist die Parallelschaltung sicher, weil alle unteren Klemmen ein einziger Knoten sind.

**Kurz gesagt:** Die Admittanzmatrix der Parallelschaltung ist die Summe der Admittanzmatrizen und die Impedanzmatrix der Reihenschaltung die Summe der Impedanzmatrizen, solange jedes Teil seine Torbedingung behält.

Bei der Reihenschaltung ist diese Bedingung leicht verletzt:

**Schritt 1**: In Reihe liegen die untere Eingangsklemme des einen und die obere des anderen Teils aneinander, ebenso am Ausgang.

**Schritt 2**: Bei zwei T-Gliedern mit durchgehender unterer Leitung verbindet die untere Leitung des oberen Glieds damit die beiden oberen Klemmen des unteren und überbrückt dessen Längswiderstände, zusammen 2 kΩ.

**Schritt 3**: Der Strom teilt sich anders auf, als die Torgrößen annehmen: Mit 1 mA in Tor 1 und offenem Tor 2 fließen je 0,5 mA in die beiden oberen Klemmen des unteren Glieds, aber 1 mA aus seiner Klemme 1′. Seine Torbedingung ist verletzt, und die Summenregel, die für das untere Glied die Torströme der Zusammenschaltung annimmt, 1 mA und 0, rechnet mit falschen Strömen.

**Schritt 4**: Die Impedanzmatrix ist 3,5, 2,5, 2,5 und 3,5 kΩ statt der Summe 4, 2, 2 und 4 kΩ.

**Schritt 5**: Dreht man das untere Glied um, trifft seine durchgehende Leitung die untere Leitung des oberen Glieds; nichts wird überbrückt, und die Summe stimmt. Prüfen lässt sich das mit dem __Brune-Test__: Eingänge in Reihe speisen, Ausgänge offen und unverbunden lassen und die Spannung zwischen den Klemmen messen, die verbunden werden sollen; ist sie null, auch mit vertauschten Toren, gilt die Regel. Bei den T-Gliedern liegen dort 1 V. Für die Parallelschaltung prüft man ebenso, mit parallel gespeisten Eingängen und einzeln kurzgeschlossenen Ausgängen.

Idee der Herleitung: Man setzt die gemeinsamen Spannungen bzw. Ströme in die Gleichungen beider Teile ein und addiert.

:::herleitung
**Ausgangspunkt:** die Knotenregel an den verbundenen Klemmen und die Admittanzgleichungen beider Teile.

**Annahmen:** (i) Beide Teile haben eine Admittanzform. (ii) Jedes Teil behält in der Zusammenschaltung seine Torbedingung.

**Schritt 1**: Parallel liegende Tore haben dieselbe Spannung:

$$\underline U_{1\mathrm a} = \underline U_{1\mathrm b} = \underline U_1, \qquad \underline U_{2\mathrm a} = \underline U_{2\mathrm b} = \underline U_2\,$$

**Schritt 2**: An den verbundenen oberen Klemmen teilt sich der Torstrom der Zusammenschaltung auf die beiden Teile auf:

$$\underline I_1 = \underline I_{1\mathrm a} + \underline I_{1\mathrm b}, \qquad \underline I_2 = \underline I_{2\mathrm a} + \underline I_{2\mathrm b}\,$$

**Schritt 3** (entscheidender Schritt): Wegen Annahme (ii) gilt für jedes Teil seine Admittanzform mit denselben Spannungen; die Summe ist:

$$\begin{pmatrix} \underline I_1 \\ \underline I_2 \end{pmatrix} = \mathbf Y_\mathrm a\begin{pmatrix} \underline U_1 \\ \underline U_2 \end{pmatrix} + \mathbf Y_\mathrm b\begin{pmatrix} \underline U_1 \\ \underline U_2 \end{pmatrix} = (\mathbf Y_\mathrm a + \mathbf Y_\mathrm b)\begin{pmatrix} \underline U_1 \\ \underline U_2 \end{pmatrix}$$

**Ergebnis:**

$$\mathbf Y = \mathbf Y_\mathrm a + \mathbf Y_\mathrm b$$

**Woher die Faktoren kommen:** Die Summe stammt aus der Knotenregel an den verbundenen Klemmen; dass es die Admittanzmatrizen sind, daraus, dass die Spannungen gemeinsam sind.

**Proben:** Einheit S. Zwei gleiche Querglieder von 1 mS parallel haben keine Admittanzform, wohl aber zwei gleiche Längsglieder: 1 mS und 1 mS ergeben 2 mS, die Parallelschaltung zweier Widerstände von 1 kΩ.

**Grenzen:** Ist die Torbedingung eines Teils verletzt, beschreibt seine Admittanzmatrix nicht mehr seine Ströme; ob sie hält, prüft der Brune-Test, der bei der Reihenschaltung beschrieben ist.
:::

:::herleitung
**Ausgangspunkt:** die Maschenregel über die in Reihe liegenden Tore und die Impedanzgleichungen beider Teile.

**Annahmen:** (i) Beide Teile haben eine Impedanzform. (ii) Jedes Teil behält in der Zusammenschaltung seine Torbedingung.

**Schritt 1**: In Reihe liegende Tore führen denselben Strom, und die Torspannung der Zusammenschaltung ist die Summe:

$$\underline I_{1\mathrm a} = \underline I_{1\mathrm b} = \underline I_1, \qquad \underline U_1 = \underline U_{1\mathrm a} + \underline U_{1\mathrm b}\,$$

und ebenso am Ausgang.

**Schritt 2** (entscheidender Schritt): Wegen Annahme (ii) gilt für jedes Teil seine Impedanzform mit denselben Strömen:

$$\begin{pmatrix} \underline U_1 \\ \underline U_2 \end{pmatrix} = \mathbf Z_\mathrm a\begin{pmatrix} \underline I_1 \\ \underline I_2 \end{pmatrix} + \mathbf Z_\mathrm b\begin{pmatrix} \underline I_1 \\ \underline I_2 \end{pmatrix} = (\mathbf Z_\mathrm a + \mathbf Z_\mathrm b)\begin{pmatrix} \underline I_1 \\ \underline I_2 \end{pmatrix}$$

**Schritt 3**: Gegenprobe an den T-Gliedern mit unterer Masseleitung, $\underline I_1$ = 1 mA, $\underline I_2$ = 0. Der Strom fließt durch den ersten Längswiderstand und den Querwiderstand des oberen Glieds, dann durch die beiden parallel liegenden Längswiderstände des unteren, 0,5 kΩ, und dessen Querwiderstand zur unteren Leitung:

$$\underline U_1 = 1\ \mathrm{mA}\cdot(1 + 1 + 0{,}5 + 1)\ \mathrm{k\Omega} = 3{,}5\ \mathrm V$$

**Schritt 4**: Durch die zweiten Längswiderstände fließt nichts; die Ausgangsspannung ist die Spannung vom Mittelpunkt des oberen Glieds zur unteren Leitung:

$$\underline U_2 = 1\ \mathrm{mA}\cdot(1 + 0{,}5 + 1)\ \mathrm{k\Omega} = 2{,}5\ \mathrm V$$

Aus Symmetrie folgen $\underline Z_{22}$ = 3,5 kΩ und $\underline Z_{12}$ = 2,5 kΩ.

**Ergebnis:** bei erhaltener Torbedingung

$$\mathbf Z = \mathbf Z_\mathrm a + \mathbf Z_\mathrm b$$

und bei den T-Gliedern mit unterer Masseleitung stattdessen 3,5, 2,5, 2,5 und 3,5 kΩ.

**Woher die Faktoren kommen:** Die Summe stammt aus der Maschenregel; die 0,5 kΩ der Gegenprobe aus den beiden überbrückten Längswiderständen, die nun parallel statt in getrennten Zweigen liegen.

**Proben:** Umgedrehtes unteres Glied: Der Strom fließt durch je einen Längs- und den Querwiderstand beider Glieder, 4 V; die Ausgangsspannung ist die Spannung an den beiden Querwiderständen, 2 V; das ist die Summe.

**Grenzen:** Die Regel gilt für jede Bemessung, wenn die Torbedingung hält; ob sie hält, hängt von der Anordnung ab, nicht von den Werten.
:::

::::beispiel Zwei T-Glieder in Reihe, falsch und richtig verbunden
**Gegeben:** zwei T-Glieder aus je drei Widerständen von 1 kΩ.

**Gesucht:** die Impedanzmatrix der Reihenschaltung in beiden Anordnungen und der Brune-Test.

**Rechnung:** Ein T-Glied: Bei offenem Ausgang fließt der Strom durch einen Längs- und den Querwiderstand, und der Ausgang greift die Spannung am Querwiderstand ab:

$$\mathbf Z_\mathrm a = \mathbf Z_\mathrm b = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}\mathrm{k\Omega}, \qquad \mathbf Z_\mathrm a + \mathbf Z_\mathrm b = \begin{pmatrix} 4 & 2 \\ 2 & 4 \end{pmatrix}\mathrm{k\Omega}\,$$

Beide mit unterer Masseleitung, 1 mA in Tor 1: Der Strom fließt durch Längs- und Querwiderstand des oberen Glieds, dann durch die beiden parallel liegenden Längswiderstände des unteren, 0,5 kΩ, und dessen Querwiderstand. Die Ausgangsspannung ist die Spannung vom Mittelpunkt des oberen Glieds zur unteren Leitung:

$$\underline U_1 = 1\ \mathrm{mA}\cdot 3{,}5\ \mathrm{k\Omega} = 3{,}5\ \mathrm V, \qquad \underline U_2 = 1\ \mathrm{mA}\cdot 2{,}5\ \mathrm{k\Omega} = 2{,}5\ \mathrm V\,$$

Aus Symmetrie folgt die ganze Matrix:

$$\mathbf Z = \begin{pmatrix} 3{,}5 & 2{,}5 \\ 2{,}5 & 3{,}5 \end{pmatrix}\mathrm{k\Omega} \neq \mathbf Z_\mathrm a + \mathbf Z_\mathrm b$$

Brune-Test mit 1 mA und unverbundenen Ausgängen: Die untere Leitung des oberen Glieds liegt auf 2 V, der Mittelpunkt des unteren auf 1 V, und zwischen den zu verbindenden Klemmen liegt 1 V. Umgedreht sind beide Klemmen Teil derselben durchgehenden Leitung, und die Spannung ist null; dann fließt der Strom durch je einen Längs- und den Querwiderstand beider Glieder, 4 V, und der Ausgang greift die beiden Querwiderstände ab, 2 V.

**Ergebnis:** **Mit beiden Masseleitungen unten 3,5, 2,5, 2,5 und 3,5 kΩ, falsch; mit umgedrehtem unterem Glied 4, 2, 2 und 4 kΩ, die Summe.**

**Einordnung:** Der Fehler ist kein Rundungsproblem: Die untere Leitung des oberen Glieds legt die beiden Längswiderstände des unteren parallel. In Schaltungen mit gemeinsamer Masse sind Parallelschaltungen deshalb unproblematisch, Reihenschaltungen nur, wenn die gemeinsame Leitung des einen Teils auf eine durchgehende Leitung des anderen trifft, wie beim Emitterwiderstand eines Transistors.
::::

## Zweitore in der Signalverarbeitung

*Wie viel Signal kommt durch eine Kette von Verstärkerstufen zwischen Quelle und Last, und wo geht es verloren?*

:::grafik
Szene: st1/netzwerkanalyse/05-signalkette · Vorlage: blockbild-schaltbild
**Abbildung 6:** Oben eine Signalkette als Blockbild: Sensor oder Antenne als Quelle mit Innenwiderstand, Verstärker, Filter, Leitung und ein A/D-Umsetzer als Last, jeder Block ein Zweitor. Darunter zwei Verstärkerstufen als rückwirkungsfreie Zweitore zwischen einer Signalquelle mit $R_\mathrm{sig}$ = 10 kΩ und einer Last $R_L$ = 10 kΩ: jede Stufe mit $R_G$ = 100 kΩ am Eingang, gesteuerter Stromquelle 0,494 mS mal Eingangsspannung und $R_\mathrm{aus}$ = 8,90 kΩ; an jeder Schnittstelle ein Teiler hervorgehoben. Pegel bei 1 mV Quellenspannung: 0,909 mV am ersten Gate, −3,67 mV am zweiten, 8,53 mV an der Last. An jeder Schnittstelle einer Kette geht Signal in einem Teiler verloren.
:::

Signalverarbeitung ist eine Kette von Zweitoren: eine Quelle mit Innenwiderstand, ein Sensor oder eine Antenne, dann Verstärker, Filter und Leitungen und am Ende ein __A/D-Umsetzer__, der die Spannung in Zahlen umsetzt und für die Kette die Last ist. Mit Kettenmatrizen ist die Kette exakt zu berechnen. Für rückwirkungsfreie Stufen genügen drei Größen, Eingangswiderstand, Steilheit und Ausgangswiderstand: Weil nichts zurückwirkt, sieht jede Stufe vom Rest der Kette nur den Eingangswiderstand der nächsten, und an jeder Schnittstelle teilt sich das Signal. In ausgeführten Verstärkern stellt ein Spannungsteiler am Gate jeder Stufe den Arbeitspunkt ein und macht den Eingangswiderstand endlich.

**Die Akteure:**

- __$\underline U_\mathrm{sig}$__, __$R_\mathrm{sig}$__: Leerlaufspannung und Innenwiderstand der Signalquelle; 10 kΩ wie in den vorigen Artikeln.
- __$R_\mathrm{ein}$__, __$R_\mathrm{aus}$__: Eingangs- und Ausgangswiderstand einer rückwirkungsfreien Stufe, die Kehrwerte von $\underline Y_{11}$ und $\underline Y_{22}$; an der Verstärkerstufe 8,90 kΩ am Ausgang.
- __$R_G$__: der Vorspannungsteiler am Gate, 400 kΩ zur Versorgung von 5 V und 133,3 kΩ nach Masse; er stellt 1,25 V ein und wirkt für das Signal als Parallelschaltung beider, 100 kΩ.

:::formel Formel
$$\frac{\underline U_2}{\underline U_\mathrm{sig}} = \frac{R_\mathrm{ein}}{R_\mathrm{sig} + R_\mathrm{ein}}\cdot\Big(-\underline Y_{21}\,\frac{R_\mathrm{aus}\,R_L}{R_\mathrm{aus} + R_L}\Big)$$
:::

**So liest man das:** Die Quellenspannung teilt sich zwischen $R_\mathrm{sig}$ und $R_\mathrm{ein}$, und der gesteuerte Strom fließt in die Parallelschaltung aus $R_\mathrm{aus}$ und $R_L$. In einer Kette ist die Last jeder Stufe der Eingangswiderstand der nächsten. Zwei Verstärkerstufen mit je 100 kΩ Vorspannungsteiler zwischen 10 kΩ Quelle und 10 kΩ Last ergeben 0,9091 mal −4,036 mal −2,326, zusammen 8,53; ohne Teiler wären es 10,22. Am meisten verliert der Ausgang, 47 %, weil 8,90 kΩ Ausgangswiderstand an 10 kΩ fast die Hälfte der Leerlaufspannung kosten.

**Kurz gesagt:** In einer Kette rückwirkungsfreier Stufen ist die Gesamtverstärkung das Produkt der Stufenverstärkungen, jede unter der Last der folgenden Stufe.

Idee der Herleitung: Ohne Rückwirkung sieht die Quelle am Eingang nur $\underline Y_{11}$, und der Ausgang folgt aus der Formel für die Verstärkung unter Last.

:::herleitung
**Ausgangspunkt:** Eingangsadmittanz und Verstärkung unter Last aus dem Abschnitt *Rückwirkung im Betrieb*; der Spannungsteiler.

**Annahmen:** (i) Die Stufe ist rückwirkungsfrei, $\underline Y_{12}$ = 0. (ii) Quelle, Last, $\underline Y_{11}$ und $\underline Y_{22}$ sind reell, also Widerstände bzw. Leitwerte.

**Schritt 1**: Mit $\underline Y_{12}$ = 0 ist die Eingangsadmittanz für jede Last $\underline Y_{11}$, die Stufe ist für die Quelle ein Widerstand $R_\mathrm{ein}$, und die Quellenspannung teilt sich:

$$\underline U_1 = \frac{R_\mathrm{ein}}{R_\mathrm{sig} + R_\mathrm{ein}}\,\underline U_\mathrm{sig}$$

**Schritt 2**: Die Verstärkung unter Last, mit dem Leitwert $1/R_L$ der Last als $\underline Y_L$ und $1/R_\mathrm{aus}$ als $\underline Y_{22}$:

$$\frac{\underline U_2}{\underline U_1} = -\frac{\underline Y_{21}}{1/R_\mathrm{aus} + 1/R_L} = -\underline Y_{21}\,\frac{R_\mathrm{aus}\,R_L}{R_\mathrm{aus} + R_L}$$

**Schritt 3** (entscheidender Schritt): In einer Kette rückwirkungsfreier Stufen hängt die Eingangsadmittanz jeder Stufe nicht von dem ab, was hinter ihr folgt; die Last jeder Stufe ist also der feste Eingangswiderstand der nächsten, und die Faktoren werden der Reihe nach multipliziert.

**Ergebnis:**

$$\frac{\underline U_2}{\underline U_\mathrm{sig}} = \frac{R_\mathrm{ein}}{R_\mathrm{sig} + R_\mathrm{ein}}\cdot\Big(-\underline Y_{21}\,\frac{R_\mathrm{aus}\,R_L}{R_\mathrm{aus} + R_L}\Big)$$

**Woher die Faktoren kommen:** Der erste Bruch ist der Teiler am Eingang, der zweite der Teiler, in den der gesteuerte Strom fließt.

**Proben:** Einheit: S mal Ω, ohne Einheit. Grenzfall unendlicher Eingangswiderstand und unendlicher Last: Leerlaufverstärkung $-\underline Y_{21}R_\mathrm{aus}$, bei der Stufe −4,396. Mit 10 kΩ Last −2,326, wie das Ersatzzweitor im Artikel über Testquellen ergibt.

**Grenzen:** Mit Rückwirkung hängen Ein- und Ausgangsadmittanz von den Nachbarn ab; dann rechnet man mit Kettenmatrizen.
:::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| vier Parameter und drei Formen | zwei lineare Gleichungen, nach verschiedenen Paaren vorgegebener Größen geordnet |
| Kurzschluss- und Leerlaufversuche | eine vorgegebene Größe null lässt in jeder Gleichung ein Glied verschwinden |
| Rückwirkung im Betrieb | im Betrieb ist keine Größe null; über die Rückwärtsübertragung sieht der Eingang die Last |
| Kettenschaltung | die Ausgangsgrößen des einen Glieds sind die vorgegebenen Größen des nächsten |
| Parallel- und Reihenschaltung | gemeinsame Spannungen bzw. Ströme sind die vorgegebenen Größen, solange die Torbedingung hält |

Ein lineares Zweitor ist durch zwei lineare Gleichungen zwischen seinen vier Torgrößen vollständig beschrieben; jede Parameterform ordnet dieselben Gleichungen nach einem anderen Paar vorgegebener Größen, und bei einer Zusammenschaltung nimmt man die Form, deren vorgegebene Größen allen Teilen gemeinsam sind: Dann addieren sich die Matrizen, in der Kette multiplizieren sie sich.

## Bedeutung und Ausblick

Zweitorparameter sind die Sprache, in der Datenblätter und Simulatoren Verstärker, Filter und Leitungen beschreiben; bei hohen Frequenzen misst man stattdessen Streuparameter, die sich in diese Formen umrechnen lassen. Für Netze aus R, L und C gelten sie bei jeder Amplitude, für Transistorschaltungen nur für kleine Signale um einen Arbeitspunkt, und immer für eine feste Frequenz. Als Nächstes folgen die Transistoren, deren Kleinsignalmodelle hier schon als Zweitore auftraten, und die Grundschaltungen, die solche Stufen zu Verstärkern verketten.

**In der ausführlichen Fassung:** das Ersatzschaltbild der Admittanzform als π mit gesteuerter Quelle, die Umrechnung der Verstärkerstufe als eigenes Beispiel, die Leistungsbilanz von RC-Glied und Verstärkerstufe, der Gyrator als passives, nicht reziprokes Zweitor, die Parallelschaltung mit eigener Abbildung, die Bipolarstufe mit Emitterwiderstand als Reihenschaltung, die Hybridform mit den Datenblattparametern des Transistors, die Verstärkerkette als durchgerechnetes Beispiel und zusätzliche Frage-Kästen. [Zur ausführlichen Fassung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/vierpole-ausfuehrlich.html)

:::kern
- Ein lineares Zweitor ist durch zwei lineare Gleichungen zwischen $\underline U_1$, $\underline I_1$, $\underline U_2$ und $\underline I_2$ vollständig beschrieben, sofern an jedem Tor die Torbedingung gilt.
- Admittanzform: Ströme aus Spannungen, Parameter mit kurzgeschlossenem Gegentor; Impedanzform: Spannungen aus Strömen, im Leerlauf; Kettenform: Eingang aus Ausgang mit $-\underline I_2$.
- Die Formen gehen durch Auflösen ineinander über, $\mathbf Z=\mathbf Y^{-1}$; eine Form fehlt, wo ihre vorgegebenen Größen nicht frei wählbar sind.
- Zweitore aus R, L und C sind reziprok, $\underline Y_{12}=\underline Y_{21}$ bzw. $\det\mathbf A=1$; rückwirkungsfrei heißt $\underline Y_{12}=0$ bzw. $\det\mathbf A=0$.
- Im Betrieb sieht der Eingang die Last: $\underline Y_\mathrm{ein}=\underline Y_{11}-\underline Y_{12}\underline Y_{21}/(\underline Y_{22}+\underline Y_L)$.
- Kette: $\mathbf A=\mathbf A_\mathrm a\mathbf A_\mathrm b$ in der Reihenfolge der Glieder; die Einzelübertragungen multiplizieren sich nur ohne Belastung.
- Parallelschaltung: Admittanzmatrizen addieren; Reihenschaltung: Impedanzmatrizen addieren; beides nur, solange jedes Teil seine Torbedingung behält.
- Kette rückwirkungsfreier Stufen: an jeder Schnittstelle ein Teiler, Stufenverstärkung $-\underline Y_{21}\,(R_\mathrm{aus}\parallel R_L)$.
:::

:::quiz
F: Warum ist $\underline Y_{11}$ im Betrieb nicht die Eingangsadmittanz eines Zweitors?
A: $\underline Y_{11}$ gilt bei kurzgeschlossenem Ausgang. Mit Last ist die Ausgangsspannung nicht null und treibt über $\underline Y_{12}$ einen zusätzlichen Eingangsstrom: $\underline Y_\mathrm{ein}=\underline Y_{11}-\underline Y_{12}\underline Y_{21}/(\underline Y_{22}+\underline Y_L)$. Die Stufe mit 20 fF Gate-Drain-Kapazität hat bei kurzgeschlossenem Ausgang 120 fF Eingangskapazität, mit 10 kΩ Last 209 fF.
F: Stimmt es, dass die Übertragung zweier RC-Glieder in Kette das Produkt ihrer Einzelübertragungen ist?
A: Nein. Das zweite Glied belastet das erste mit (1 − j) kΩ. Bei ω = 10⁴ 1/s überträgt die Kette −j/3, Betrag 0,333; das Produkt der Einzelübertragungen ergäbe −j/2, 50 % zu viel. Richtig ist das Produkt der Kettenmatrizen.
F: Warum steht in der Kettenform $-\underline I_2$ statt $\underline I_2$?
A: $-\underline I_2$ ist der Strom, der das Zweitor am Ausgang verlässt und in das nächste Glied hineinfließt. Damit ist der Ausgangsvektor eines Glieds der Eingangsvektor des nächsten, und die Kettenmatrizen multiplizieren sich ohne Vorzeichenwechsel.
F: Warum ergibt die Reihenschaltung zweier T-Glieder mit unterer Masseleitung nicht die Summe ihrer Impedanzmatrizen?
A: Die untere Leitung des oberen Glieds verbindet die oberen Klemmen des unteren und überbrückt dessen Längswiderstände. Mit 1 mA fließen je 0,5 mA in die beiden oberen Klemmen, aber 1 mA aus der unteren: Die Torbedingung ist verletzt. Statt 4, 2, 2 und 4 kΩ ergeben sich 3,5, 2,5, 2,5 und 3,5 kΩ; umgedreht stimmt die Summe.
F: Stimmt es, dass $\underline Y_{11}$ der Kehrwert von $\underline Z_{11}$ ist?
A: Nein. $\underline Y_{11}$ wird bei kurzgeschlossenem, $\underline Z_{11}$ bei offenem Ausgang bestimmt; invers sind nur die Matrizen als Ganzes. Beim RC-Glied ist $\underline Y_{11}$ 1 mS, $1/\underline Z_{11}$ dagegen (0,5 + 0,5j) mS.
F: Wie groß ist die Verstärkung von zwei Verstärkerstufen mit 100 kΩ Vorspannungsteiler zwischen einer 10-kΩ-Quelle und 10 kΩ Last?
A: Eingangsteiler 0,9091, erste Stufe an 100 kΩ −4,036, zweite an 10 kΩ −2,326; zusammen 8,53. Am meisten verliert der Ausgang, weil 8,90 kΩ Ausgangswiderstand an 10 kΩ fast die Hälfte kosten.
:::
