---
title: Vierpole: Parameterformen und Zusammenschaltung
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / Netzwerkanalyse
order: 33020500
summary: Wie man eine lineare Schaltung mit einem Eingangs- und einem Ausgangstor durch vier Parameter vollständig beschreibt, warum es dafür mehrere gleichwertige Formen gibt und wie man aus den Matrizen der Teile die Matrix einer Zusammenschaltung gewinnt. Ausführliche Fassung mit Herleitung der Admittanz-, Impedanz-, Ketten- und Hybridform, der Umrechnungen, der Eingangsadmittanz unter Last, des Umkehrungssatzes, der Regeln für Ketten-, Parallel- und Reihenschaltung samt Torbedingung und der Verstärkung einer Signalkette, durchgerechnet an RC-Glied, zweistufigem RC-Tiefpass, Verstärkerstufen, T-Gliedern und einer Bipolarstufe.
tags: Vierpol, Admittanzform, Impedanzform, Kettenform, Zusammenschaltung
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Eine Verstärkerstufe, ein Filter oder eine Leitung hat einen Eingang und einen Ausgang. Wer solche Blöcke zu einem System zusammensetzt, will nicht jedes Mal ihr Inneres neu durchrechnen, sondern jeden Block durch wenige Zahlen ersetzen, die nur sein Verhalten an den Anschlüssen festhalten. Das Ersatzzweitor aus Eingangsadmittanz, Verstärkung und Ausgangsimpedanz leistet das nur, solange der Ausgang nicht auf den Eingang zurückwirkt; schon im zweistufigen RC-Tiefpass versagt es. Vollständig beschreiben vier Parameter jeden linearen Block mit zwei Anschlusspaaren, und es gibt mehrere gleichwertige Arten, sie anzuordnen. Alles hängt an einem Prinzip:

**Ein lineares Zweitor ist durch zwei lineare Gleichungen zwischen seinen vier Torgrößen vollständig beschrieben; jede Parameterform ordnet dieselben Gleichungen nach einem anderen Paar vorgegebener Größen, und bei einer Zusammenschaltung nimmt man die Form, deren vorgegebene Größen allen Teilen gemeinsam sind: Dann addieren sich die Matrizen, in der Kette multiplizieren sie sich.**

Vorausgesetzt werden das Rechnen mit [Zeigern](/wissen/elektrotechnik/1-semester/mathematische-methoden-der-elektrotechnik/komplexe-zahlen-und-zeiger/zeiger-und-sinussignale.html), Knotenanalyse, Matrizen, Inverse und Determinante aus [Netzwerkgleichungen systematisch aufstellen: modifizierte Knotenanalyse](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/modifizierte-knotenanalyse-ausfuehrlich.html), Testquellen und das Ersatzzweitor aus [Testquellen und Transientenanalyse linearer Schaltungen](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/testquellen-und-transientenanalyse-ausfuehrlich.html) und die Verstärkerstufe aus [Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/ersatzquellen-maschen-und-knotenanalyse-ausfuehrlich.html). Eine erste Einführung mit Kennlinien gibt [Zweitore und ihre Parameter](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/zweitore.html). Auf den Vierpolen bauen die Transistorgrundschaltungen und ihr Frequenzgang auf, in denen jede Stufe als Zweitor in einer Kette steht.

:::grafik
Szene: st1/netzwerkanalyse/05-uebersicht · Vorlage: blockbild
**Abbildung 1:** (a) Ein Zweitor als Kasten mit dem Eingangstor aus den Klemmen 1 und 1′ und dem Ausgangstor aus 2 und 2′; die Ströme $\underline I_1$ und $\underline I_2$ fließen an den oberen Klemmen hinein und an den unteren heraus, die Spannungen $\underline U_1$ und $\underline U_2$ zeigen von oben nach unten. (b) Drei Zusammenschaltungen zweier Zweitore a und b mit der jeweils passenden Form: Kettenschaltung, Ausgang von a an den Eingang von b, $\mathbf A = \mathbf A_\mathrm a\mathbf A_\mathrm b$; Parallelschaltung, beide Tore parallel, $\mathbf Y = \mathbf Y_\mathrm a + \mathbf Y_\mathrm b$; Reihenschaltung, beide Tore in Reihe, $\mathbf Z = \mathbf Z_\mathrm a + \mathbf Z_\mathrm b$. In der Form, deren vorgegebene Größen allen Teilen gemeinsam sind, wird jede Zusammenschaltung zu einer Addition oder Multiplikation der Matrizen.
:::

## Tor, Torbedingung und Zweitor

*Wann darf man eine Schaltung mit vier Anschlüssen durch Spannung und Strom an zwei Anschlusspaaren beschreiben?*

:::grafik
Szene: st1/netzwerkanalyse/05-tor-und-vierpol · Vorlage: schaltbild-vergleich
**Abbildung 2:** Links ein Vierpol, eine Schaltung mit vier Anschlüssen, an dem drei äußere Leitungen beliebig verteilte Ströme führen; nur die Summe aller vier Klemmenströme ist null. Rechts dieselbe Schaltung zwischen einer Signalquelle am Klemmenpaar 1–1′ und einer Last am Klemmenpaar 2–2′: Was an Klemme 1 hineinfließt, kommt an 1′ heraus, ebenso an 2 und 2′. Erst die Torbedingung macht aus vier Klemmen zwei Tore.
:::

Eine Schaltung mit vier Anschlüssen heißt __Vierpol__, Pol hier im Sinn von Anschluss. An seinen Klemmen fließen vier Ströme, von denen nach der Knotenregel für eine Hülle um die Schaltung nur drei frei sind. Fasst man je zwei Klemmen zu einem __Tor__ zusammen, 1 und 1′ zum Eingangstor (Tor 1), 2 und 2′ zum Ausgangstor (Tor 2), so hat jedes Tor genau dann einen einzigen Strom, wenn die __Torbedingung__ gilt: Der Strom, der an der oberen Klemme eines Tores hineinfließt, fließt an der unteren desselben Tores wieder heraus. Dann heißt der Vierpol __Zweitor__.

**Die Akteure:**

- __$\underline U_1$__, __$\underline U_2$__: Torspannungen, als Zeiger von der oberen zur unteren Klemme gezählt; in V. Am RC-Glied dieses Artikels einige Volt, an der Verstärkerstufe Millivolt.
- __$\underline I_1$__, __$\underline I_2$__: Torströme, in die obere Klemme hinein gezählt; in A. Milliampere am RC-Glied, Mikroampere an der Verstärkerstufe.
- __$\underline I_{1'}$__, __$\underline I_{2'}$__: die Ströme, die an den unteren Klemmen 1′ und 2′ herausfließen.

:::formel Definition
$$\underline I_1 = \underline I_{1'}, \qquad \underline I_2 = \underline I_{2'}\,$$
:::

Die Torbedingung ist keine Eigenschaft der Schaltung allein, sondern ihrer Beschaltung. Hängt an jedem Tor ein eigener Zweipol, links eine Signalquelle und rechts eine Last, gilt sie von selbst, denn der Strom, der aus der Quelle in Klemme 1 fließt, kann nur über Klemme 1′ zu ihr zurückkehren (Abbildung 2 rechts). Verbinden äußere Leitungen die beiden Tore oder zwei Zweitore miteinander, kann ein Teil des Stroms einen anderen Rückweg nehmen; beim Zusammenschalten von Zweitoren entscheidet das darüber, ob die Rechenregeln gelten (Abschnitt *Reihenschaltung*). Im Sprachgebrauch wird Vierpol oft gleichbedeutend mit Zweitor benutzt.

:::frage
„Strom kann doch nicht verschwinden. Ist die Torbedingung nicht immer erfüllt?“
Die Knotenregel garantiert nur, dass die Summe aller vier Klemmenströme null ist, nicht, dass jeder Strom am selben Tor zurückkehrt. Gibt es außen einen zweiten Rückweg, etwa über ein anderes Zweitor, fließt ein Teil des Stroms dort zurück. Schaltet man zwei T-Glieder, jedes mit durchgehender unterer Leitung, in Reihe und speist 1 mA in Tor 1 bei offenem Tor 2, fließen in die beiden oberen Klemmen des unteren Glieds je 0,5 mA hinein, aus seiner Klemme 1′ aber 1 mA heraus; erhalten bleibt nur der Gesamtstrom (Abschnitt *Reihenschaltung*).
:::

Beide Ströme werden in das Zweitor hinein gezählt und beide Spannungen von der oberen zur unteren Klemme, an jedem Tor also wie bei einem Verbraucher. Diese Vereinbarung heißt __symmetrisches Zählpfeilsystem__; sie behandelt Eingang und Ausgang gleich.

:::frage
„Warum zählt man auch den Ausgangsstrom in das Zweitor hinein, er fließt doch zur Last heraus?“
Ein Zählpfeil ist eine Vereinbarung, keine Aussage über die tatsächliche Richtung; fließt der Strom anders herum, wird sein Zeiger negativ. Am RC-Glied mit kurzgeschlossenem Ausgang ist $\underline I_2$ bei 1 V am Eingang −1 mA: 1 mA fließt aus Klemme 2 heraus. Die symmetrische Wahl macht die Gleichungen in beiden Toren gleich gebaut, sodass Eigenschaften wie die Umkehrbarkeit als Gleichheit zweier Parameter ablesbar sind (Abschnitt *Reziprozität*). Nur die Kettenform zählt den Ausgangsstrom hinaus, weil er dort als Eingangsstrom des nächsten Glieds weiterläuft (Abschnitt *Kettenform*).
:::

Im Inneren dürfen beliebige lineare Bauelemente liegen, auch gesteuerte Quellen. Deren Steuergröße darf jede Spannung und jeder Strom im Inneren sein, etwa die Gate-Source-Spannung der Verstärkerstufe, die wegen des Source-Widerstands keine Torspannung ist; sie darf nur nicht außerhalb des Zweitors liegen. Ausgeschlossen sind unabhängige Quellen, also Quellen, deren Wert von keiner Größe der Schaltung abhängt: Sie trieben Ströme auch ohne jede Anregung an den Toren, und jede Gleichung bekäme einen festen Zusatzterm. Ein Transistorverstärker erfüllt das im [Kleinsignal-Ersatzschaltbild](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung-ausfuehrlich.html), dem linearen Modell für kleine Änderungen um den Arbeitspunkt: Versorgungsspannungen werden dort zu Kurzschlüssen, der Transistor zu Leitwerten und gesteuerten Quellen. Ein solches Zweitor heißt __linear__; alle Größen sind Zeiger bei einer festen Kreisfrequenz ω.

## Vier Größen, zwei Gleichungen

*Warum genügen vier Zahlen, um ein lineares Zweitor vollständig zu beschreiben, und warum gibt es mehrere Formen?*

Ein konkreter Fall zeigt es: das __RC-Glied__, ein Widerstand $R$ = 1 kΩ in der oberen Leitung zwischen den Klemmen 1 und 2 und ein Kondensator $C$ = 100 nF von Klemme 2 zur durchgehenden unteren Leitung. Bei ω = 10⁴ 1/s hat der Kondensator die Admittanz j·1 mS. Legt man an beide Tore Spannungen an, fließt in Klemme 1 der Strom durch den Widerstand, $(\underline U_1 - \underline U_2)/R$, und in Klemme 2 der Strom, den der Kondensator aufnimmt, abzüglich dessen, was über den Widerstand schon ankommt. Beide Ströme sind Summen aus einem Anteil, der zu $\underline U_1$ proportional ist, und einem, der zu $\underline U_2$ proportional ist:

$$\underline I_1 = 1\ \mathrm{mS}\cdot\underline U_1 - 1\ \mathrm{mS}\cdot\underline U_2, \qquad \underline I_2 = -1\ \mathrm{mS}\cdot\underline U_1 + (1 + j)\ \mathrm{mS}\cdot\underline U_2\,$$

Vier Zahlen, 1, −1, −1 und (1 + j) mS, legen damit für jedes Spannungspaar beide Ströme fest. Mit 1 V am Eingang und 0,5 V am Ausgang fließen 0,5 mA in den Eingang und (−0,5 + 0,5j) mA in den Ausgang; mehr muss man über das RC-Glied nicht wissen, um es in jeder Beschaltung zu berechnen.

Das gilt für jedes lineare Zweitor. Gibt man beide Torspannungen durch ideale Spannungsquellen vor, ist nach dem Überlagerungssatz jeder Strom die Summe der Ströme, die jede Quelle allein hervorruft, und jeder Anteil ist proportional zu seiner Quelle. Zwei lineare Gleichungen mit vier Faktoren beschreiben deshalb das Zweitor vollständig.

Man schreibt sie als Produkt einer Matrix mit einem Spaltenvektor, wie die Knotengleichungen der Knotenanalyse: Die Matrix enthält die vier Faktoren, der Vektor die vorgegebenen Größen, und jede Zeile der Matrix wird elementweise mit dem Vektor multipliziert und aufsummiert. Die erste Zeile des RC-Glieds, (1 mS; −1 mS), ergibt mit dem Vektor (1 V; 0,5 V) den Strom 1 mS · 1 V − 1 mS · 0,5 V, also 0,5 mA.

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

:::frage
„Das Ersatzzweitor kam mit drei Zahlen aus. Warum braucht man jetzt vier?“
Die drei Kenngrößen Eingangsadmittanz, Leerlaufverstärkung und Ausgangsimpedanz setzen voraus, dass der Ausgang nicht auf den Eingang zurückwirkt; die vierte Zahl ist genau diese Rückwirkung, $\underline Y_{12}$. Bei der Verstärkerstufe ist sie null, und drei Zahlen genügen. Beim RC-Glied ist sie −1 mS, so groß wie die Vorwärtsübertragung: Was am Ausgang hängt, verändert, wie viel Strom die Quelle am Eingang liefern muss. Vier Zahlen erfassen jedes lineare Zweitor, mit oder ohne Rückwirkung (Abschnitt *Rückwirkung im Betrieb*).
:::

Welche zwei der vier Torgrößen man vorgibt, ist frei. Aus vier Größen lassen sich auf sechs Arten zwei auswählen, und jede Auswahl ergibt eine Form der __Zweitorgleichungen__ mit eigenen Parametern; die beiden übrigen Größen folgen aus den vorgegebenen:

| Form und vorgegebene Größen | Parameter bestimmt mit |
|---|---|
| Admittanzform $\mathbf Y$: $\underline U_1$, $\underline U_2$ | Kurzschluss an einem Tor |
| Impedanzform $\mathbf Z$: $\underline I_1$, $\underline I_2$ | Leerlauf an einem Tor |
| Kettenform $\mathbf A$: $\underline U_2$, $-\underline I_2$ | Leerlauf und Kurzschluss am Ausgang |
| Hybridform $\mathbf H$: $\underline I_1$, $\underline U_2$ | Kurzschluss am Ausgang, Leerlauf am Eingang |
| inverse Hybridform: $\underline U_1$, $\underline I_2$ | Leerlauf am Ausgang, Kurzschluss am Eingang |
| inverse Kettenform: $\underline U_1$, $-\underline I_1$ | Leerlauf und Kurzschluss am Eingang |

Alle sechs beschreiben dasselbe Zweitor; man wählt die Form nach der Aufgabe. Admittanz-, Impedanz- und Kettenform sind die gebräuchlichsten, weil zu ihnen die drei häufigsten Zusammenschaltungen passen (Abbildung 1); die Hybridform beschreibt Bipolartransistoren besonders knapp (Abschnitt *Hybridform*).

:::frage
„Wozu mehrere Formen, wenn eine das Zweitor schon vollständig beschreibt?“
Aus drei Gründen. In der passenden Form wird eine Zusammenschaltung zu einer Addition oder Multiplikation von Matrizen, in jeder anderen zu einem Gleichungssystem. Nicht jedes Zweitor hat jede Form, etwa die Verstärkerstufe keine Impedanzform (Abschnitt *Umrechnung*). Und jedes Bauteil hat eine Form, in der seine Parameter am direktesten zu messen und zu deuten sind, der Feldeffekttransistor die Admittanzform mit der Steilheit $\underline Y_{21}$, der Bipolartransistor die Hybridform mit der Stromverstärkung β.
:::

## Admittanzform: Ströme aus den Spannungen

*Welche Ströme fließen in ein Zweitor, wenn beide Torspannungen vorgegeben sind, und wie bestimmt man die vier Faktoren?*

:::grafik
Szene: st1/netzwerkanalyse/05-kurzschluss-leerlauf · Vorlage: schaltbild-messung
**Abbildung 3:** Das RC-Glied (1 kΩ längs, 100 nF quer, ω = 10⁴ 1/s) in vier Versuchen. (a) Ausgang kurzgeschlossen, 1 V am Eingang: Der Kondensator ist überbrückt, $\underline I_1$ = 1 mA, $\underline I_2$ = −1 mA; das ergibt $\underline Y_{11}$ = 1 mS und $\underline Y_{21}$ = −1 mS. (b) Eingang kurzgeschlossen, 1 V am Ausgang: $\underline I_1$ = −1 mA, $\underline I_2$ = (1 + j) mA; $\underline Y_{12}$ = −1 mS, $\underline Y_{22}$ = (1 + j) mS. (c) Ausgang offen, 1 mA in den Eingang: $\underline U_1$ = (1 − j) V, $\underline U_2$ = −j V; $\underline Z_{11}$ = (1 − j) kΩ, $\underline Z_{21}$ = −j kΩ. (d) Eingang offen, 1 mA in den Ausgang: beide Spannungen −j V; $\underline Z_{12}$ = $\underline Z_{22}$ = −j kΩ. Admittanzparameter misst man mit kurzgeschlossenem, Impedanzparameter mit offenem Gegentor.
:::

**Die Akteure:**

- __$\underline Y_{11}$__, __$\underline Y_{12}$__, __$\underline Y_{21}$__, __$\underline Y_{22}$__: die __Admittanzparameter__ oder Y-Parameter; in S. Beim RC-Glied 1 mS, −1 mS, −1 mS und (1 + j) mS.
- __$\mathbf Y$__: die __Admittanzmatrix__ oder Leitwertmatrix aus diesen vier Parametern, die Form heißt auch __Leitwertform__. Sie hat immer zwei Zeilen und ist nicht zu verwechseln mit der Knotenleitwertmatrix __$\mathbf Y_\mathrm K$__ der Knotenanalyse, die eine Zeile je Knoten hat.

:::formel Definition
$$\underline I_1 = \underline Y_{11}\,\underline U_1 + \underline Y_{12}\,\underline U_2, \qquad \underline I_2 = \underline Y_{21}\,\underline U_1 + \underline Y_{22}\,\underline U_2\,$$

$$\begin{pmatrix} \underline I_1 \\ \underline I_2 \end{pmatrix} = \mathbf Y\begin{pmatrix} \underline U_1 \\ \underline U_2 \end{pmatrix}, \qquad \mathbf Y = \begin{pmatrix} \underline Y_{11} & \underline Y_{12} \\ \underline Y_{21} & \underline Y_{22} \end{pmatrix}\,$$
:::

**So liest man das:** Die Ströme folgen aus den Spannungen. Wie die Herleitung im vorigen Abschnitt zeigt, bestimmt man jeden Parameter mit einer Spannung an einem Tor, während das andere kurzgeschlossen ist; man definiert die Parameter so, weil eine vorgegebene Spannung null ein Kurzschluss ist und dann in jeder Gleichung ein Glied verschwindet (Abbildung 3 a und b):

$$\underline Y_{11} = \frac{\underline I_1}{\underline U_1}\bigg|_{\underline U_2 = 0}, \qquad \underline Y_{21} = \frac{\underline I_2}{\underline U_1}\bigg|_{\underline U_2 = 0}, \qquad \underline Y_{12} = \frac{\underline I_1}{\underline U_2}\bigg|_{\underline U_1 = 0}, \qquad \underline Y_{22} = \frac{\underline I_2}{\underline U_2}\bigg|_{\underline U_1 = 0}\,$$

$\underline Y_{11}$ heißt __Kurzschluss-Eingangsadmittanz__, $\underline Y_{22}$ __Kurzschluss-Ausgangsadmittanz__, $\underline Y_{21}$ __Kurzschluss-Übertragungsadmittanz__ vorwärts, bei Transistoren __Steilheit__, und $\underline Y_{12}$ Kurzschluss-Übertragungsadmittanz rückwärts. $\underline Y_{12}$ sagt, wie stark eine Spannung am Ausgang auf den Eingang zurückwirkt.

**Kurz gesagt:** Jeder Y-Parameter ist der Strom an einem Tor je Volt an einem Tor, während das jeweils andere Tor kurzgeschlossen ist.

:::frage
„Darf man den Ausgang eines Verstärkers zum Messen mit einem Draht kurzschließen?“
Gemeint ist ein Kurzschluss für das Signal, nicht für den Arbeitspunkt. Ein Draht vom Drain der Verstärkerstufe nach Masse legte auch die Gleichspannung des Drains auf null; der Transistor führte keinen Strom mehr, und seine Steilheit wäre null. Man schließt deshalb nur den Wechselanteil kurz, über einen Kondensator, dessen Impedanz bei der Messfrequenz klein ist gegen die Impedanz am Tor: 10 µF haben bei 1 kHz 15,9 Ω, 0,18 % der 8,90 kΩ am Drain. Im Kleinsignal-Ersatzschaltbild ist der Kurzschluss deshalb die Bedingung, dass die Wechselspannung am Tor null ist.
:::

Die Admittanzgleichungen lassen sich als Schaltung lesen (Abbildung 4). Zwischen den Klemmen 1 und 2 liegt eine Admittanz in der oberen Leitung, ein __Längszweig__, und an jedem Tor eine Admittanz zur durchgehenden unteren Leitung, ein __Querzweig__; zusammen bilden sie ein π. Am Ausgang kommt eine __spannungsgesteuerte Stromquelle__ hinzu, eine ideale Stromquelle, deren Strom proportional zu einer Spannung an anderer Stelle ist, hier zu $\underline U_1$. Sie zieht ihren Strom aus Klemme 2 und führt ihn zur unteren Leitung.

:::grafik
Szene: st1/netzwerkanalyse/05-ersatzschaltbild-y · Vorlage: schaltbild
**Abbildung 4:** Oben das Ersatzschaltbild der Admittanzform: Querzweig $\underline Y_\text{quer1}$ am Eingang, Längszweig $\underline Y_\text{längs}$ zwischen den Klemmen 1 und 2, Querzweig $\underline Y_\text{quer2}$ am Ausgang und eine spannungsgesteuerte Stromquelle $\underline Y_\mathrm g\,\underline U_1$ von Klemme 2 zur unteren Leitung; gestrichelt die Zuordnung zur Steuerspannung $\underline U_1$. Unten drei Fälle: das RC-Glied (0; 1 mS; j·1 mS; keine Quelle), die Verstärkerstufe mit Source-Widerstand (0; 0; 0,112 mS; Quelle 0,494 mS) und die Stufe ohne Source-Widerstand bei ω = 10⁸ 1/s ($j\omega C_{gs}$ = j·10 µS; $j\omega C_{gd}$ = j·2 µS; 125 µS; Quelle 1 mS). Jede Admittanzmatrix ist ein π aus drei Admittanzen mit einer gesteuerten Quelle; bei einem umkehrbaren Zweitor entfällt die Quelle.
:::

**Die Akteure:**

- __$\underline Y_\text{quer1}$__, __$\underline Y_\text{längs}$__, __$\underline Y_\text{quer2}$__: die Admittanzen des π; in S.
- __$\underline Y_\mathrm g$__: Übertragungsadmittanz der gesteuerten Quelle, ihr Strom je Volt an Tor 1; in S.

:::formel Formel
$$\underline Y_\text{quer1} = \underline Y_{11} + \underline Y_{12}, \qquad \underline Y_\text{längs} = -\underline Y_{12}, \qquad \underline Y_\text{quer2} = \underline Y_{22} + \underline Y_{12}, \qquad \underline Y_\mathrm g = \underline Y_{21} - \underline Y_{12}\,$$
:::

**So liest man das:** Aus jeder Admittanzmatrix lässt sich ein Ersatzschaltbild ablesen. Der Längszweig trägt die Rückwirkung; die gesteuerte Quelle trägt den Unterschied zwischen Vorwärts- und Rückwärtsübertragung und entfällt, wenn beide gleich sind. Umgekehrt hat ein π ohne Quelle die Admittanzmatrix mit $\underline Y_\text{quer1} + \underline Y_\text{längs}$ und $\underline Y_\text{längs} + \underline Y_\text{quer2}$ auf der Diagonalen und $-\underline Y_\text{längs}$ daneben. Das Kleinsignal-Ersatzschaltbild eines Transistors ist genau ein solches π mit gesteuerter Quelle (Abbildung 4 unten rechts).

Idee der Herleitung: Man stellt die Knotengleichungen des Ersatzschaltbilds an den Klemmen 1 und 2 auf und vergleicht mit den Admittanzgleichungen.

:::herleitung
**Ausgangspunkt:** die Knotenregel an den Klemmen 1 und 2 des Ersatzschaltbilds, die untere Leitung als Bezug; die Admittanzgleichungen.

**Annahmen:** (i) Die untere Leitung verbindet 1′ und 2′; die Torspannungen sind die Potentiale der Klemmen 1 und 2. (ii) Die Quelle zieht den Strom $\underline Y_\mathrm g\,\underline U_1$ aus Klemme 2.

**Schritt 1**: An Klemme 1 verlässt der Strom $\underline I_1$ den Knoten durch den Querzweig und den Längszweig:

$$\underline I_1 = \underline Y_\text{quer1}\,\underline U_1 + \underline Y_\text{längs}\,(\underline U_1 - \underline U_2)$$

**Schritt 2**: An Klemme 2 fließt $\underline I_2$ durch den Querzweig, durch den Längszweig zu Klemme 1 und in die Quelle:

$$\underline I_2 = \underline Y_\text{quer2}\,\underline U_2 + \underline Y_\text{längs}\,(\underline U_2 - \underline U_1) + \underline Y_\mathrm g\,\underline U_1$$

**Schritt 3** (entscheidender Schritt): Nach den Spannungen geordnet und mit den Admittanzgleichungen verglichen, müssen die Faktoren übereinstimmen:

$$\underline Y_{11} = \underline Y_\text{quer1} + \underline Y_\text{längs}, \qquad \underline Y_{12} = -\underline Y_\text{längs}, \qquad \underline Y_{21} = \underline Y_\mathrm g - \underline Y_\text{längs}, \qquad \underline Y_{22} = \underline Y_\text{längs} + \underline Y_\text{quer2}\,$$

**Ergebnis:** nach den Elementen des Ersatzschaltbilds aufgelöst:

$$\underline Y_\text{quer1} = \underline Y_{11} + \underline Y_{12}, \qquad \underline Y_\text{längs} = -\underline Y_{12}, \qquad \underline Y_\text{quer2} = \underline Y_{22} + \underline Y_{12}, \qquad \underline Y_\mathrm g = \underline Y_{21} - \underline Y_{12}\,$$

**Woher die Faktoren kommen:** Der Längszweig erscheint in beiden Zeilen mit umgekehrtem Vorzeichen, deshalb ist er allein für eine gleiche Rückwärts- und Vorwärtsübertragung verantwortlich; jeder Unterschied muss aus der Quelle kommen.

**Proben:** Einheiten: alle Größen in S. RC-Glied, in mS:

$$\underline Y_\text{quer1} = 1 - 1 = 0, \qquad \underline Y_\text{längs} = 1, \qquad \underline Y_\text{quer2} = (1 + j) - 1 = j, \qquad \underline Y_\mathrm g = -1 - (-1) = 0\,$$

Das ist das RC-Glied selbst.

**Grenzen:** Haben die Tore keine gemeinsame untere Leitung, gilt dasselbe Ersatzschaltbild für das Verhalten an den Toren, solange die Torbedingung erfüllt ist; es beschreibt dann nur die Tore, nicht den inneren Aufbau.
:::

::::beispiel Admittanzmatrix und Ersatzschaltbild von RC-Glied und Verstärkerstufe
**Gegeben:** (a) RC-Glied mit $R$ = 1 kΩ längs und $C$ = 100 nF quer bei ω = 10⁴ 1/s, also j·1 mS für den Kondensator. (b) Die Verstärkerstufe, eine Source-Schaltung mit der Steilheit $g_m$ = 1 mS, dem Ausgangsleitwert $g_o$ = 25 µS, dem Drainwiderstand $R_D$ = 10 kΩ und dem Source-Widerstand $R_S$ = 1 kΩ, als Zweitor zwischen Gate und Masse (Tor 1) und Drain und Masse (Tor 2), $R_D$ im Zweitor, Signalquelle und Last außerhalb; aus den Testquellen im Artikel über Testquellen ist bekannt: Das Gate nimmt keinen Strom auf, bei kurzgeschlossenem Drain fließen je Volt am Gate 0,494 mA in den Drain hinein, und in den Drain sieht man bei kurzgeschlossenem Gate 8,90 kΩ.

**Gesucht:** die Admittanzmatrizen und Ersatzschaltbilder.

**Rechnung:** (a) Ausgang kurzgeschlossen: Der Kondensator liegt am Kurzschluss, der Strom fließt durch $R$ hinein und am Ausgang heraus. Eingang kurzgeschlossen: Der Strom aus Tor 2 fließt durch $R$ in den Kurzschluss am Eingang und durch $C$:

$$\underline Y_{11} = \frac{1}{R} = 1\ \mathrm{mS}, \qquad \underline Y_{21} = -\frac{1}{R} = -1\ \mathrm{mS}, \qquad \underline Y_{12} = -\frac{1}{R} = -1\ \mathrm{mS}, \qquad \underline Y_{22} = \frac{1}{R} + j\omega C = (1 + j)\ \mathrm{mS}\,$$

Ersatzschaltbild: $\underline Y_\text{quer1}$ = 0, $\underline Y_\text{längs}$ = 1 mS, $\underline Y_\text{quer2}$ = j·1 mS, $\underline Y_\mathrm g$ = 0.

(b) Die drei Angaben sind $\underline Y_{11}$, $\underline Y_{21}$ und $\underline Y_{22}$; vom Drain wirkt nichts auf das Gate zurück, $\underline Y_{12}$ ist null:

$$\mathbf Y = \begin{pmatrix} 0 & 0 \\ 0{,}494 & 0{,}112 \end{pmatrix}\mathrm{mS}, \qquad \underline Y_\text{quer2} = 0{,}112\ \mathrm{mS}, \qquad \underline Y_\mathrm g = 0{,}494\ \mathrm{mS}\,$$

Bei offenem Drain ist $\underline I_2$ null, und die zweite Gleichung ergibt die Leerlaufverstärkung, hier mit den ungerundeten Werten:

$$\frac{\underline U_2}{\underline U_1}\bigg|_{\underline I_2 = 0} = -\frac{\underline Y_{21}}{\underline Y_{22}} = -\frac{0{,}49383\ \mathrm{mS}}{0{,}11235\ \mathrm{mS}} = -4{,}40$$

**Ergebnis:** **RC-Glied: $\mathbf Y$ mit 1, −1, −1 und (1 + j) mS, Ersatzschaltbild das RC-Glied selbst; Verstärkerstufe: $\mathbf Y$ mit 0, 0, 0,494 und 0,112 mS, Ersatzschaltbild eine gesteuerte Stromquelle 0,494 mS parallel zu 8,90 kΩ.**

**Einordnung:** Das Ersatzschaltbild der Verstärkerstufe ist die Norton-Form ihres Ersatzzweitors: Eingangsadmittanz $\underline Y_{11}$, Ausgangsimpedanz $1/\underline Y_{22}$ und Leerlaufverstärkung $-\underline Y_{21}/\underline Y_{22}$, −4,40 wie dort. Das Ersatzzweitor aus drei Kenngrößen ist also die Admittanzform mit $\underline Y_{12}$ = 0. Das positive $\underline Y_{21}$ verträgt sich mit der invertierenden Stufe: Der Strom fließt in den Drain hinein, und an einer Last fällt die Spannung deshalb negativ aus.
::::

## Impedanzform: Spannungen aus den Strömen

*Welche Spannungen stellen sich an einem Zweitor ein, wenn beide Torströme vorgegeben sind?*

Gibt man beide Torströme durch ideale Stromquellen vor, sind nach dem Überlagerungssatz beide Spannungen Summen aus Anteilen, die zu $\underline I_1$ und zu $\underline I_2$ proportional sind. Ein vorgegebener Strom null ist ein offenes Tor; die Parameter misst man deshalb im Leerlauf des jeweils anderen Tors (Abbildung 3 c und d).

**Die Akteure:**

- __$\underline Z_{11}$__, __$\underline Z_{12}$__, __$\underline Z_{21}$__, __$\underline Z_{22}$__: die __Impedanzparameter__ oder Z-Parameter; in Ω. Beim RC-Glied (1 − j) kΩ, −j kΩ, −j kΩ und −j kΩ.
- __$\mathbf Z$__: die __Impedanzmatrix__ oder Widerstandsmatrix; die Form heißt auch __Widerstandsform__.

:::formel Definition
$$\underline U_1 = \underline Z_{11}\,\underline I_1 + \underline Z_{12}\,\underline I_2, \qquad \underline U_2 = \underline Z_{21}\,\underline I_1 + \underline Z_{22}\,\underline I_2\,$$

$$\begin{pmatrix} \underline U_1 \\ \underline U_2 \end{pmatrix} = \mathbf Z\begin{pmatrix} \underline I_1 \\ \underline I_2 \end{pmatrix}, \qquad \mathbf Z = \begin{pmatrix} \underline Z_{11} & \underline Z_{12} \\ \underline Z_{21} & \underline Z_{22} \end{pmatrix}\,$$
:::

**So liest man das:** Die Spannungen folgen aus den Strömen. Jeder Parameter ist eine Spannung je Strom bei offenem Gegentor:

$$\underline Z_{11} = \frac{\underline U_1}{\underline I_1}\bigg|_{\underline I_2 = 0}, \qquad \underline Z_{21} = \frac{\underline U_2}{\underline I_1}\bigg|_{\underline I_2 = 0}, \qquad \underline Z_{12} = \frac{\underline U_1}{\underline I_2}\bigg|_{\underline I_1 = 0}, \qquad \underline Z_{22} = \frac{\underline U_2}{\underline I_2}\bigg|_{\underline I_1 = 0}\,$$

$\underline Z_{11}$ heißt __Leerlauf-Eingangsimpedanz__, $\underline Z_{22}$ __Leerlauf-Ausgangsimpedanz__, $\underline Z_{21}$ und $\underline Z_{12}$ __Leerlauf-Übertragungsimpedanz__ vorwärts und rückwärts. Eine Stromquelle am Tor erzwingt die Torbedingung von außen: Was sie in die obere Klemme treibt, nimmt sie an der unteren wieder auf.

**Kurz gesagt:** Jeder Z-Parameter ist die Spannung an einem Tor je Ampere in ein Tor, während das jeweils andere Tor offen ist.

Ein __T-Glied__ aus zwei Längsimpedanzen $\underline Z_\text{längs1}$ und $\underline Z_\text{längs2}$ und einer Querimpedanz $\underline Z_\text{quer}$ dazwischen hat eine übersichtliche Impedanzmatrix, denn bei offenem Ausgang fließt der Eingangsstrom durch $\underline Z_\text{längs1}$ und $\underline Z_\text{quer}$, und der Ausgang greift die Spannung an $\underline Z_\text{quer}$ ab:

$$\mathbf Z = \begin{pmatrix} \underline Z_\text{längs1} + \underline Z_\text{quer} & \underline Z_\text{quer} \\ \underline Z_\text{quer} & \underline Z_\text{quer} + \underline Z_\text{längs2} \end{pmatrix}$$

Fehlen die Längsimpedanzen, bleibt ein __Querglied__, eine Impedanz zwischen zwei durchgehenden Leitungen; dann sind alle vier Einträge gleich der Querimpedanz. Sein Gegenstück ist das __Längsglied__, eine Impedanz in der oberen Leitung bei durchgehender unterer.

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

::::beispiel Impedanzmatrix von T-Glied und RC-Glied
**Gegeben:** (a) ein T-Glied aus drei Widerständen von je 1 kΩ; (b) das RC-Glied mit 1 kΩ und −j·1 kΩ für den Kondensator bei ω = 10⁴ 1/s.

**Gesucht:** die Impedanzmatrizen und für das RC-Glied der Vergleich mit der Admittanzmatrix.

**Rechnung:** (a) Nach der Formel für das T-Glied:

$$\mathbf Z_\text{T-Glied} = \begin{pmatrix} 1 + 1 & 1 \\ 1 & 1 + 1 \end{pmatrix}\mathrm{k\Omega} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}\mathrm{k\Omega}$$

(b) Als T mit nur einer Längsimpedanz, und die Probe, dass das Produkt mit der Admittanzmatrix die Einheitsmatrix ergibt, hier für die erste Zeile:

$$\mathbf Z = \begin{pmatrix} 1 - j & -j \\ -j & -j \end{pmatrix}\mathrm{k\Omega}, \qquad (1 - j)\cdot 1 + (-j)\cdot(-1) = 1, \qquad (1 - j)\cdot(-1) + (-j)\cdot(1 + j) = 0\,$$

**Ergebnis:** **T-Glied: $\mathbf Z_\text{T-Glied}$ mit 2, 1, 1 und 2 kΩ; RC-Glied: $\mathbf Z$ mit (1 − j), −j, −j und −j kΩ, die Inverse seiner Admittanzmatrix.**

**Einordnung:** Beim RC-Glied ist $\underline Y_{11}$ = 1 mS, der Kehrwert von $\underline Z_{11}$ aber (0,5 + 0,5j) mS: Mit kurzgeschlossenem Ausgang ist der Kondensator überbrückt, mit offenem liegt er im Strompfad.
::::

:::fehlvorstellung
„$\underline Y_{11}$ ist der Kehrwert von $\underline Z_{11}$.“ Das liegt nahe, weil bei einem einzelnen Zweipol Admittanz und Impedanz Kehrwerte sind. Bei einem Zweitor gehören die beiden zu verschiedenen Versuchen: $\underline Y_{11}$ wird mit kurzgeschlossenem, $\underline Z_{11}$ mit offenem Ausgang bestimmt. Am RC-Glied ist $\underline Y_{11}$ 1 mS, $1/\underline Z_{11}$ dagegen (0,5 + 0,5j) mS. Kehrwerte sind nur die Matrizen als Ganzes (Abschnitt *Umrechnung*); einzelne Einträge stimmen nur dann überein, wenn eine der beiden Übertragungsimpedanzen null ist.
:::

## Kettenform: der Eingang aus dem Ausgang

*Was muss man am Eingang anlegen, damit am Ausgang eine bestimmte Spannung und ein bestimmter Strom herauskommen?*

Die Kettenform drückt die Eingangsgrößen durch die Ausgangsgrößen aus. Als Ausgangsstrom verwendet sie $-\underline I_2$, den Strom, der aus Klemme 2 heraus zur nächsten Stufe fließt. Der Grund liegt in der Kettenschaltung: Dort ist der Strom, der das eine Zweitor am Ausgang verlässt, der Strom, der in das nächste am Eingang hineinfließt; mit $-\underline I_2$ als Größe gehen die Ausgangsgrößen des einen ohne Vorzeichenwechsel in die Eingangsgrößen des nächsten über (Abschnitt *Kettenschaltung*). Alle übrigen Zählpfeile bleiben symmetrisch.

**Die Akteure:**

- __$\underline A_{11}$__, __$\underline A_{12}$__, __$\underline A_{21}$__, __$\underline A_{22}$__: die __Kettenparameter__, $\underline A_{11}$ und $\underline A_{22}$ ohne Einheit, $\underline A_{12}$ in Ω, $\underline A_{21}$ in S. Beim RC-Glied 1 + j, 1 kΩ, j·1 mS und 1.
- __$\mathbf A$__: die __Kettenmatrix__, im Englischen ABCD-Matrix mit den Elementen A, B, C und D.

:::formel Definition
$$\underline U_1 = \underline A_{11}\,\underline U_2 + \underline A_{12}\,(-\underline I_2), \qquad \underline I_1 = \underline A_{21}\,\underline U_2 + \underline A_{22}\,(-\underline I_2)\,$$

$$\begin{pmatrix} \underline U_1 \\ \underline I_1 \end{pmatrix} = \mathbf A\begin{pmatrix} \underline U_2 \\ -\underline I_2 \end{pmatrix}, \qquad \mathbf A = \begin{pmatrix} \underline A_{11} & \underline A_{12} \\ \underline A_{21} & \underline A_{22} \end{pmatrix}\,$$
:::

**So liest man das:** Die vorgegebenen Größen sitzen beide am Ausgang. Man bestimmt die Parameter mit offenem Ausgang, $\underline I_2$ = 0, und mit kurzgeschlossenem, $\underline U_2$ = 0; es sind dieselben Versuche wie in Abbildung 3 c und a:

$$\underline A_{11} = \frac{\underline U_1}{\underline U_2}\bigg|_{\underline I_2 = 0}, \qquad \underline A_{21} = \frac{\underline I_1}{\underline U_2}\bigg|_{\underline I_2 = 0}, \qquad \underline A_{12} = \frac{\underline U_1}{-\underline I_2}\bigg|_{\underline U_2 = 0}, \qquad \underline A_{22} = \frac{\underline I_1}{-\underline I_2}\bigg|_{\underline U_2 = 0}\,$$

$\underline A_{11}$ ist die __reziproke Leerlauf-Spannungsübertragung__: Ihr Kehrwert ist die Leerlaufverstärkung $\underline A_V$ aus dem Artikel über Testquellen. $\underline A_{21}$ heißt Leerlauf-Übertragungsadmittanz, $\underline A_{12}$ Kurzschluss-Übertragungsimpedanz und $\underline A_{22}$ reziproke Kurzschluss-Stromübertragung.

Längs- und Querglied aus dem Abschnitt *Impedanzform* haben besonders übersichtliche Kettenmatrizen. Das Längsglied mit der Impedanz $\underline Z$ lässt den Strom unverändert durch und senkt die Spannung um $\underline Z$ mal Strom; das Querglied, hier mit seiner Admittanz $\underline Y$ beschrieben, lässt die Spannung unverändert und zweigt den Strom $\underline Y$ mal Spannung ab:

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

::::beispiel Kettenmatrix des RC-Glieds aus Leerlauf und Kurzschluss am Ausgang
**Gegeben:** RC-Glied mit $R$ = 1 kΩ und $C$ = 100 nF bei ω = 10⁴ 1/s, also $j\omega RC$ = j.

**Gesucht:** $\mathbf A$ und die Leerlauf-Spannungsübertragung.

**Rechnung:** Ausgang offen: Derselbe Strom fließt durch $R$ und $C$; die Eingangsspannung ist $1 + j\omega RC$-mal so groß wie die Ausgangsspannung, und der Eingangsstrom ist der Kondensatorstrom:

$$\underline A_{11} = \frac{R + 1/(j\omega C)}{1/(j\omega C)} = 1 + j\omega RC = 1 + j, \qquad \underline A_{21} = j\omega C = j\cdot 1\ \mathrm{mS}\,$$

Ausgang kurzgeschlossen: Der Kondensator ist überbrückt, der ganze Eingangsstrom fließt durch $R$ hinaus:

$$\underline A_{12} = R = 1\ \mathrm{k\Omega}, \qquad \underline A_{22} = 1\,$$

**Ergebnis:** **$\mathbf A$ hat die Einträge 1 + j, 1 kΩ, j·1 mS und 1; die Leerlauf-Spannungsübertragung ist $1/(1 + j)$ = 0,5 − 0,5j, Betrag 0,707, Winkel −45°.**

**Einordnung:** Das ist der bekannte Tiefpass bei seiner Eckkreisfrequenz 1/(RC). Die Determinante, (1 + j) mal 1 minus 1 kΩ mal j·1 mS, ist 1; warum gerade 1, klärt der Abschnitt *Reziprozität*.
::::

## Umrechnung zwischen den Formen

*Wie gewinnt man aus einer Form jede andere, und gibt es jede Form für jedes Zweitor?*

Alle Formen enthalten dieselben zwei Gleichungen; man gewinnt die eine aus der anderen, indem man die Gleichungen nach dem anderen Paar von Größen auflöst. Zwischen Admittanz- und Impedanzform ist das eine Inversion: Die eine Matrix rechnet von den Spannungen zu den Strömen, die andere zurück, und ihr Produkt ist die Einheitsmatrix. Die Inverse einer 2×2-Matrix erhält man, indem man die beiden Diagonaleinträge vertauscht, die beiden Nebeneinträge umpolt und alles durch die __Determinante__ teilt, das Produkt der Diagonaleinträge minus das Produkt der Nebeneinträge ([modifizierte Knotenanalyse](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/modifizierte-knotenanalyse-ausfuehrlich.html)).

**Die Akteure:**

- __$\det\mathbf Y$__, __$\det\mathbf Z$__, __$\det\mathbf A$__: die Determinanten der drei Matrizen; beim RC-Glied j·1 mS², −j·1 kΩ² und 1.

:::formel Formel
$$\mathbf Z = \mathbf Y^{-1} = \frac{1}{\det\mathbf Y}\begin{pmatrix} \underline Y_{22} & -\underline Y_{12} \\ -\underline Y_{21} & \underline Y_{11} \end{pmatrix}, \qquad \mathbf Y = \mathbf Z^{-1} = \frac{1}{\det\mathbf Z}\begin{pmatrix} \underline Z_{22} & -\underline Z_{12} \\ -\underline Z_{21} & \underline Z_{11} \end{pmatrix}\,$$

$$\mathbf A = -\frac{1}{\underline Y_{21}}\begin{pmatrix} \underline Y_{22} & 1 \\ \det\mathbf Y & \underline Y_{11} \end{pmatrix}, \qquad \mathbf Y = \frac{1}{\underline A_{12}}\begin{pmatrix} \underline A_{22} & -\det\mathbf A \\ -1 & \underline A_{11} \end{pmatrix}\,$$

$$\mathbf A = \frac{1}{\underline Z_{21}}\begin{pmatrix} \underline Z_{11} & \det\mathbf Z \\ 1 & \underline Z_{22} \end{pmatrix}, \qquad \mathbf Z = \frac{1}{\underline A_{21}}\begin{pmatrix} \underline A_{11} & \det\mathbf A \\ 1 & \underline A_{22} \end{pmatrix}\,$$

$$\det\mathbf A = \frac{\underline Y_{12}}{\underline Y_{21}} = \frac{\underline Z_{12}}{\underline Z_{21}}$$
:::

**So liest man das:** Jede Umrechnung teilt durch einen Parameter oder eine Determinante. Wird dieser Nenner null, gibt es die Zielform nicht: Die Impedanzform verlangt $\det\mathbf Y \neq 0$ bzw. $\underline A_{21} \neq 0$, die Admittanzform $\det\mathbf Z \neq 0$ bzw. $\underline A_{12} \neq 0$, die Kettenform $\underline Y_{21} \neq 0$ bzw. $\underline Z_{21} \neq 0$. Ein verschwindender Nenner heißt physikalisch, dass sich die vorgegebenen Größen der Zielform nicht unabhängig wählen lassen. Das Querglied hat keine Admittanzform, weil seine Torspannungen gleich sein müssen, das Längsglied keine Impedanzform, weil durch beide Tore derselbe Strom fließt. Die Verstärkerstufe hat keine Impedanzform, weil das Gate keinen Strom aufnimmt: Ein vorgegebener Gatestrom fände keinen Weg. Ein Zweitor ohne Vorwärtsübertragung schließlich, mit $\underline Y_{21}$ = 0, hat keine Kettenform, weil keine Eingangsgröße eine bestimmte Ausgangsspannung erzeugt.

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

::::beispiel Verstärkerstufe: von der Admittanz- zur Kettenform
**Gegeben:** die Admittanzmatrix der Verstärkerstufe mit Source-Widerstand: $\underline Y_{11}$ und $\underline Y_{12}$ null, $\underline Y_{21}$ = 0,49383 mS, $\underline Y_{22}$ = 0,11235 mS.

**Gesucht:** Impedanz- und Kettenmatrix.

**Rechnung:** Die Determinante ist null, weil die erste Zeile null ist:

$$\det\mathbf Y = 0\cdot 0{,}11235 - 0\cdot 0{,}49383 = 0$$

Für die Kettenmatrix wird durch $\underline Y_{21}$ geteilt:

$$\mathbf A = -\frac{1}{0{,}49383\ \mathrm{mS}}\begin{pmatrix} 0{,}11235\ \mathrm{mS} & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} -0{,}2275 & -2{,}025\ \mathrm{k\Omega} \\ 0 & 0 \end{pmatrix}$$

**Ergebnis:** **Die Stufe hat keine Impedanzform; ihre Kettenmatrix hat die Einträge −0,2275, −2,025 kΩ, 0 und 0.**

**Einordnung:** $1/\underline A_{11}$ = −4,396 ist die Leerlaufverstärkung, und $\underline A_{12}/\underline A_{11}$ = 8,90 kΩ die Ausgangsimpedanz bei kurzgeschlossenem Eingang. Die zweite Zeile ist null, weil das Gate bei keinem Zustand des Ausgangs Strom aufnimmt; deshalb ist auch $\det\mathbf A$ null.
::::

## Reziprozität, Rückwirkungsfreiheit und Leistung

*Was verraten die Parameter über das Innere eines Zweitors?*

Beim RC-Glied ist $\underline Y_{12}$ gleich $\underline Y_{21}$, beide −1 mS: 1 V am Ausgang treibt bei kurzgeschlossenem Eingang denselben Strom aus dem Eingang heraus wie 1 V am Eingang bei kurzgeschlossenem Ausgang aus dem Ausgang, je 1 mA. Das ist kein Zufall der Zahlen. Nach dem __Umkehrungssatz__ (Reziprozitätstheorem) gilt es für jedes Zweitor aus Widerständen, Kondensatoren, Spulen, auch gekoppelten, und idealen Übertragern: Vertauscht man das Tor der Anregung mit dem Tor der Messung, bleibt das Verhältnis von Wirkung zu Ursache gleich. Ein solches Zweitor heißt __reziprok__ oder umkehrbar. In jeder Form lässt es sich ablesen:

:::formel Satz
$$\underline Y_{12} = \underline Y_{21} \quad\Longleftrightarrow\quad \underline Z_{12} = \underline Z_{21} \quad\Longleftrightarrow\quad \det\mathbf A = 1$$
:::

**So liest man das:** Die drei Bedingungen sind gleichwertig, soweit die jeweilige Form existiert. Ein reziprokes Zweitor hat nur drei unabhängige Parameter, und sein Ersatzschaltbild ist ein π ohne gesteuerte Quelle (Abbildung 4). Gesteuerte Quellen heben die Reziprozität in der Regel auf, weil ihr Eintragsmuster in der Knotenleitwertmatrix unsymmetrisch ist: Es steht in den Zeilen der Knoten, zwischen denen der Strom fließt, und in den Spalten der Knoten, deren Spannung steuert. Die Verstärkerstufe überträgt mit 0,494 mS vorwärts und mit null rückwärts.

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

:::fehlvorstellung
„Passive Zweitore sind immer reziprok.“ Das liegt nahe, weil alle alltäglichen passiven Netze aus Widerständen, Spulen und Kondensatoren bestehen und die Gegenbeispiele, die man zuerst kennenlernt, Verstärker sind. Die Reziprozität folgt aber aus der Symmetrie der Eintragsmuster, nicht aus der Passivität. Ein __Gyrator__ mit der Admittanzmatrix $\underline Y_{12}$ = 1 mS, $\underline Y_{21}$ = −1 mS und null auf der Diagonalen ist nicht reziprok, nimmt aber bei keiner Beschaltung Wirkleistung auf oder ab: Mit 1 V am Eingang und 0,5 V am Ausgang nimmt Tor 1 0,25 mW auf und Tor 2 gibt 0,25 mW ab. In der Hochfrequenztechnik baut man nicht reziproke Bauteile passiv aus vormagnetisiertem Ferrit: den Gyrator selbst, verlustbehaftete Richtungsleitungen, die Signale nur in einer Richtung durchlassen, und Zirkulatoren mit drei Toren; mit Verstärkern nachgebildet, ersetzt der Gyrator in integrierten Filtern Spulen, denn mit 100 nF am Ausgang sieht sein Eingang eine Spule von 100 mH.
:::

Ein Zweitor heißt __rückwirkungsfrei__, wenn eine Spannung am Ausgang keinen Strom am Eingang hervorruft. Nach der Umrechnung sind dafür, soweit die jeweilige Form existiert, drei Bedingungen gleichwertig, denn $\underline Z_{12}$ ist $-\underline Y_{12}/\det\mathbf Y$ und $\det\mathbf A$ ist $\underline Y_{12}/\underline Y_{21}$:

$$\underline Y_{12} = 0 \quad\Longleftrightarrow\quad \underline Z_{12} = 0 \quad\Longleftrightarrow\quad \det\mathbf A = 0$$

Die Verstärkerstufe mit Source-Widerstand ist rückwirkungsfrei; das Ersatzzweitor mit drei Kenngrößen beschreibt sie deshalb vollständig. Überträgt ein rückwirkungsfreies Zweitor vorwärts, ist also $\underline Y_{21}$ nicht null, dann ist es der Grenzfall eines nicht reziproken Zweitors, wie ihn eine ideale gesteuerte Quelle darstellt.

Schließlich nimmt ein Zweitor an beiden Toren Wirkleistung auf. Mit Amplitudenzeigern ist die Wirkleistung an einem Tor die Hälfte des Realteils von Spannung mal konjugiert komplexem Strom ($\underline I^*$ hat den Imaginärteil mit umgekehrtem Vorzeichen); wegen der symmetrischen Zählpfeile ist sie an beiden Toren aufgenommene Leistung, und das Zweitor nimmt insgesamt

$$P = \tfrac12\,\mathrm{Re}\{\underline U_1\,\underline I_1^* + \underline U_2\,\underline I_2^*\}$$

auf. Es heißt __passiv__, wenn $P$ bei keiner Beschaltung negativ wird, und __aktiv__, wenn $P$ negativ werden kann, das Zweitor also mehr Wirkleistung abgibt, als es aufnimmt. Die zusätzliche Leistung stammt aus der Versorgung, die im Kleinsignal-Ersatzschaltbild nicht mehr vorkommt; dort zeigt sie sich als gesteuerte Quelle. Umgekehrt macht eine gesteuerte Quelle ein Zweitor nicht zwangsläufig aktiv: Der Gyrator lässt sich mit zwei gesteuerten Quellen modellieren und bleibt verlustlos.

:::herleitung
**Ausgangspunkt:** die Wirkleistung eines Zweipols im Verbraucherzählpfeilsystem mit Amplitudenzeigern, $\tfrac12\mathrm{Re}\{\underline U\,\underline I^*\}$ ([Zeiger](/wissen/elektrotechnik/1-semester/mathematische-methoden-der-elektrotechnik/komplexe-zahlen-und-zeiger/zeiger-und-sinussignale.html)).

**Annahmen:** (i) Die Torbedingung gilt. (ii) Im Inneren sind keine weiteren Anschlüsse nach außen.

**Schritt 1**: Wegen der Torbedingung wirkt jedes Tor nach außen wie ein Zweipol: Durch seine beiden Klemmen fließt derselbe Strom, und zwischen ihnen liegt die Torspannung. Mit symmetrischen Zählpfeilen ist jedes Tor ein Verbraucher und nimmt $\tfrac12\mathrm{Re}\{\underline U_k\,\underline I_k^*\}$ auf.

**Schritt 2**: Energie gelangt nur über die beiden Tore ins Innere, also ist die aufgenommene Leistung die Summe:

$$P = \tfrac12\,\mathrm{Re}\{\underline U_1\,\underline I_1^* + \underline U_2\,\underline I_2^*\}$$

**Ergebnis:** wie oben.

**Woher die Faktoren kommen:** Der Faktor 1/2 stammt aus den Amplitudenzeigern, das Pluszeichen zwischen den Toren aus den symmetrischen Zählpfeilen.

**Proben:** RC-Glied: Leistung setzt nur der Widerstand um, $\tfrac12|\underline U_1 - \underline U_2|^2/R$; mit 1 V und 0,5 V sind das 0,125 mW, ebenso aus der Formel mit den Strömen 0,5 mA und (−0,5 + 0,5j) mA. Gyrator: 0,25 mW minus 0,25 mW, null.

**Grenzen:** Mit Effektivwertzeigern entfällt der Faktor 1/2. Ist die Torbedingung verletzt, ist ein Tor kein Zweipol mehr, und die Summe erfasst nicht alle Leistung.
:::

::::beispiel Reziprok, rückwirkungsfrei, aktiv: RC-Glied und Verstärkerstufe
**Gegeben:** RC-Glied wie oben; Verstärkerstufe mit $\underline Y_{21}$ = 0,49383 mS, $\underline Y_{22}$ = 0,11235 mS, Last $R_L$ = 10 kΩ und 10 mV Amplitude am Gate.

**Gesucht:** Reziprozität, Rückwirkung und Leistungsbilanz.

**Rechnung:** (a) RC-Glied: alle drei Bedingungen der Reziprozität,

$$\underline Y_{12} = \underline Y_{21} = -1\ \mathrm{mS}, \qquad \underline Z_{12} = \underline Z_{21} = -j\ \mathrm{k\Omega}, \qquad \det\mathbf A = (1 + j) - 1\ \mathrm{k\Omega}\cdot j\ \mathrm{mS} = 1\,$$

und die aufgenommene Leistung ist die des Widerstands, nie negativ.

(b) Verstärkerstufe: $\underline Y_{12}$ = 0, also rückwirkungsfrei und nicht reziprok. Nach dem Ersatzschaltbild fließt der gesteuerte Strom, 0,49383 mS mal 10 mV, aus dem Ausgangsknoten heraus und zieht ihn an der Parallelschaltung aus 8,901 kΩ und der Last unter null:

$$\begin{aligned} \underline U_2 &= -0{,}49383\ \mathrm{mS}\cdot 10\ \mathrm{mV}\cdot\frac{8{,}901\cdot 10}{18{,}901}\ \mathrm{k\Omega} \\ &= -4{,}938\ \mathrm{\mu A}\cdot 4{,}709\ \mathrm{k\Omega} = -23{,}26\ \mathrm{mV} \end{aligned}$$

Das Gate nimmt nichts auf; am Ausgang gibt das Zweitor an die Last ab:

$$P = 0 - \tfrac12\,\frac{|\underline U_2|^2}{R_L} = -\tfrac12\,\frac{(23{,}26\ \mathrm{mV})^2}{10\ \mathrm{k\Omega}} = -27{,}0\ \mathrm{nW}$$

**Ergebnis:** **RC-Glied reziprok und passiv; Verstärkerstufe rückwirkungsfrei, nicht reziprok und aktiv mit −27,0 nW.**

**Einordnung:** Die 27 nW stammen aus der Versorgungsspannung, die im Arbeitspunkt 1,25 mW in die Stufe liefert (5 V mal 0,25 mA). Das Verhältnis von abgegebener zu aufgenommener Leistung ist im Modell unendlich groß, weil das Gate keine Wirkleistung aufnimmt; beim RC-Glied dagegen kann am Ausgang nie mehr ankommen, als am Eingang hineingeht.
::::

## Rückwirkung im Betrieb: die Eingangsadmittanz unter Last

*Welche Admittanz sieht eine Quelle am Eingang, wenn am Ausgang eine Last hängt, und warum ist das nicht $\underline Y_{11}$?*

:::grafik
Szene: st1/netzwerkanalyse/05-rueckwirkung-cgd · Vorlage: schaltbild-kurve
**Abbildung 5:** (a) Kleinsignal-Ersatzschaltbild der Stufe ohne Source-Widerstand als Zweitor mit Tor 1 zwischen Gate und Masse und Tor 2 zwischen Drain und Masse, bei ω = 10⁸ 1/s: $C_{gs}$ = 100 fF vom Gate nach Masse, $C_{gd}$ = 20 fF vom Gate zum Drain, gesteuerte Quelle $g_m\underline U_1$ mit $g_m$ = 1 mS vom Drain nach Masse, $G_D + g_o$ = 125 µS am Drain; außerhalb die Last $R_L$. (b) Eingangskapazität $C_\mathrm{ein}$ in fF (100 bis 300) über $R_L$ in kΩ (0,1 bis 1000, logarithmisch): 122 fF bei 0,1 kΩ, 138 fF bei 1 kΩ, 209 fF bei 10 kΩ, 268 fF bei 100 kΩ, 279 fF bei 1 MΩ; gestrichelt die Grenzen 120 fF bei kurzgeschlossenem und 280 fF bei offenem Ausgang. Über die Gate-Drain-Kapazität sieht der Eingang die Last.
:::

**Die Akteure:**

- __$C_{gs}$__, __$C_{gd}$__: Gate-Source- und Gate-Drain-Kapazität des Transistors, 100 fF und 20 fF wie im Artikel über die modifizierte Knotenanalyse.
- __$g_m$__: Steilheit des Transistors, 1 mS; seine gesteuerte Quelle liefert $g_m$ mal Gate-Source-Spannung. __$g_o$__: sein Ausgangsleitwert, 25 µS. __$G_D$__: Leitwert des Drainwiderstands $R_D$ = 10 kΩ, 100 µS; mit $g_o$ zusammen 125 µS am Drain.
- __$\underline Y_L$__: Admittanz der Last am Ausgang; 0,1 mS für $R_L$ = 10 kΩ.
- __$\underline Y_\mathrm{ein}$__: Eingangsadmittanz im Betrieb, der Quotient $\underline I_1/\underline U_1$ mit angeschlossener Last; ohne Last ist sie die Eingangsadmittanz des Ersatzzweitors.
- __$C_\mathrm{ein}$__: die Kapazität, die der Imaginärteil von $\underline Y_\mathrm{ein}$ darstellt, Imaginärteil durch ω.

**Das Zusammenspiel:**

**Schritt 1**: $\underline Y_{11}$ ist mit kurzgeschlossenem Ausgang definiert. Im Betrieb hängt dort eine Last, und die Ausgangsspannung ist nicht null.

**Schritt 2**: Die Last nimmt den Strom $\underline Y_L\,\underline U_2$ auf, der aus dem Zweitor herausfließt; also ist $\underline I_2$ gleich $-\underline Y_L\,\underline U_2$. In die zweite Admittanzgleichung eingesetzt, folgt die Ausgangsspannung; bei der Stufe mit 10 kΩ Last ist sie −4,44-mal die Eingangsspannung.

**Schritt 3**: Über $\underline Y_{12}$ treibt diese Ausgangsspannung einen zusätzlichen Strom $\underline Y_{12}\,\underline U_2$ in den Eingang. Die Quelle am Eingang spürt ihn als veränderte Admittanz.

**Schritt 4**: Zusammen ergibt sich die Eingangsadmittanz unter Last. Ohne Rückwirkung, mit $\underline Y_{12}$ = 0, ist sie für jede Last $\underline Y_{11}$; dann ist das Ersatzzweitor aus drei Kenngrößen exakt.

**Schritt 5**: Eine kleine Rückwirkung kann viel bewirken, weil sie mit der Verstärkung multipliziert wird. In der Stufe verbindet nur $C_{gd}$ den Drain mit dem Gate; $\underline Y_{12}$ ist deshalb $-j\omega C_{gd}$, bei 10⁸ 1/s nur −j·2 µS, 0,2 % von $\underline Y_{21}$. Trotzdem wirken die 20 fF der Gate-Drain-Kapazität bei 10 kΩ Last am Eingang wie 20 fF mal (1 + 4,44), also 109 fF. Die Eingangskapazität steigt von 120 fF bei kurzgeschlossenem Ausgang auf 209 fF, bei offenem auf 280 fF (Abbildung 5 b). Diese Vervielfachung heißt __Miller-Effekt__; sie begrenzt die Bandbreite von Verstärkerstufen und wird beim Frequenzgang der Transistorgrundschaltungen genauer untersucht.

:::formel Formel
$$\underline Y_\mathrm{ein} = \frac{\underline I_1}{\underline U_1} = \underline Y_{11} - \frac{\underline Y_{12}\,\underline Y_{21}}{\underline Y_{22} + \underline Y_L}, \qquad \frac{\underline U_2}{\underline U_1} = -\frac{\underline Y_{21}}{\underline Y_{22} + \underline Y_L}\,$$
:::

**So liest man das:** Die Eingangsadmittanz hängt über das Produkt aus Rückwärts- und Vorwärtsübertragung von der Last ab. Mit kurzgeschlossenem Ausgang, $\underline Y_L$ unendlich, bleibt $\underline Y_{11}$; mit offenem, $\underline Y_L$ = 0, ergibt sich $\det\mathbf Y/\underline Y_{22}$, nach der Umrechnung genau $1/\underline Z_{11}$. Jede Last liegt dazwischen. Vertauscht man die Rollen der Tore, hängt ebenso die Ausgangsadmittanz von der Quelle am Eingang ab, mit deren Admittanz $\underline Y_\mathrm{sig}$:

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

**Einordnung:** Die Gate-Drain-Kapazität wirkt mit dem Faktor 1 plus Verstärkungsbetrag, 5,44 mit Last und 9 ohne. Treibt eine Signalquelle mit 10 kΩ das Gate, rückt die Ecke des Tiefpasses aus Quellwiderstand und Eingangskapazität grob abgeschätzt von 159 MHz mit $C_{gs}$ allein auf 76 MHz. Der kleine Realteil, 0,097 µS, entsteht, weil die Verstärkung bei dieser Frequenz schon eine kleine Phasendrehung hat.
::::

:::fehlvorstellung
„$\underline Y_{11}$ ist die Eingangsadmittanz des Zweitors.“ Das liegt nahe, weil $\underline Y_{11}$ Kurzschluss-Eingangsadmittanz heißt und beim rückwirkungsfreien Ersatzzweitor tatsächlich die Eingangsadmittanz ist. Sie ist es aber nur bei kurzgeschlossenem Ausgang. Im Betrieb kommt über die Rückwirkung ein lastabhängiger Anteil hinzu: In der Stufe mit Gate-Drain-Kapazität ist $\underline Y_{11}$ eine Kapazität von 120 fF, mit der Last von 10 kΩ sieht die Quelle 209 fF, das 1,74-Fache. Auch passive Zweitore wirken zurück: Die Eingangsadmittanz des zweistufigen RC-Tiefpasses, im Artikel über Testquellen bei offenem Ausgang zu (0,667 + 0,333j) mS bestimmt, sinkt mit 1 kΩ Last auf (0,600 + 0,300j) mS.
:::

## Kettenschaltung: Matrizen multiplizieren statt Übertragungen

*Wie berechnet man hintereinandergeschaltete Zweitore, und warum ist die Übertragung einer Kette nicht das Produkt der Einzelübertragungen?*

:::grafik
Szene: st1/netzwerkanalyse/05-rc-kette · Vorlage: schaltbild-kurve
**Abbildung 6:** (a) Zwei RC-Glieder (je 1 kΩ längs, 100 nF quer) in Kette, der zweistufige RC-Tiefpass; über jedem Glied seine Kettenmatrix, über beiden das Produkt mit den Einträgen 3j, (2 + j) kΩ, (−1 + 2j) mS und 1 + j. Am Verbindungsknoten der Strom, der das erste Glied als $-\underline I_{2\mathrm a}$ verlässt und als $\underline I_{1\mathrm b}$ in das zweite fließt; daneben die Eingangsimpedanz des zweiten Glieds, (1 − j) kΩ, als Last des ersten. (b) Betrag der Leerlauf-Spannungsübertragung über ω von 10² bis 10⁶ 1/s (logarithmisch): Kette 0,967 bei 10³, 0,333 bei 10⁴ und 0,0097 bei 10⁵ 1/s; gestrichelt das Produkt der Einzelübertragungen, 0,990, 0,500 und 0,0099. Das zweite Glied belastet das erste; deshalb ist die Kette nicht das Produkt der Einzelübertragungen, die Kettenmatrix aber das Produkt der Kettenmatrizen.
:::

**Die Akteure:**

- __$\mathbf A_\mathrm a$__, __$\mathbf A_\mathrm b$__: Kettenmatrizen des ersten und des zweiten Glieds; ihre Torgrößen tragen den Index a bzw. b, etwa $\underline U_{2\mathrm a}$ und $\underline I_{1\mathrm b}$.
- __$\mathbf A$__: Kettenmatrix der ganzen Kette.

Das Produkt zweier Matrizen ist die Matrix, die dasselbe bewirkt wie beide nacheinander. Ihr Eintrag in Zeile i und Spalte k ist die Summe der Produkte aus Zeile i der linken und Spalte k der rechten Matrix. Für das Längsglied mit 1 kΩ und das Querglied mit j·1 mS ergibt das die Kettenmatrix des RC-Glieds; in umgekehrter Reihenfolge entsteht eine andere Matrix, denn beim Matrizenprodukt kommt es auf die Reihenfolge an:

$$\begin{pmatrix} 1 & 1\ \mathrm{k\Omega} \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ j\cdot 1\ \mathrm{mS} & 1 \end{pmatrix} = \begin{pmatrix} 1 + j & 1\ \mathrm{k\Omega} \\ j\cdot 1\ \mathrm{mS} & 1 \end{pmatrix}, \qquad \begin{pmatrix} 1 & 0 \\ j\cdot 1\ \mathrm{mS} & 1 \end{pmatrix}\begin{pmatrix} 1 & 1\ \mathrm{k\Omega} \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1\ \mathrm{k\Omega} \\ j\cdot 1\ \mathrm{mS} & 1 + j \end{pmatrix}\,$$

**Das Zusammenspiel:**

**Schritt 1**: In der __Kettenschaltung__ ist das Ausgangstor des ersten Glieds mit dem Eingangstor des zweiten verbunden. Beide haben dieselbe Spannung, $\underline U_{2\mathrm a}$ gleich $\underline U_{1\mathrm b}$, und der Strom, der das erste Glied an Klemme 2 verlässt, fließt in das zweite an Klemme 1 hinein, $-\underline I_{2\mathrm a}$ gleich $\underline I_{1\mathrm b}$. Die Torbedingung gilt von selbst, weil die beiden Tore nur über zwei Leitungen verbunden sind.

**Schritt 2**: Damit ist der Ausgangsvektor des ersten Glieds, mit $\underline U_{2\mathrm a}$ und $-\underline I_{2\mathrm a}$, genau der Eingangsvektor des zweiten. Dafür steht in der Kettenform $-\underline I_2$: Ohne das Minuszeichen stünde zwischen den Gliedern ein Vorzeichenwechsel.

**Schritt 3**: Setzt man die Kettengleichung des zweiten Glieds in die des ersten ein, steht vor den Ausgangsgrößen der Kette das Produkt der beiden Matrizen, in der Reihenfolge der Glieder.

**Schritt 4**: Jede Einzelübertragung $1/\underline A_{11}$ gilt bei offenem Ausgang. In der Kette ist der Ausgang des ersten Glieds aber mit dem Eingang des zweiten belastet, beim RC-Tiefpass mit (1 − j) kΩ. Die Spannung zwischen den Gliedern ist deshalb je Volt am Eingang nur 0,333 − 0,333j statt 0,5 − 0,5j.

**Schritt 5**: Die Kette überträgt bei ω = 10⁴ 1/s den Betrag 1/3, das Produkt der Einzelübertragungen ergäbe 1/2, um 50 % zu viel. Die Kettenmatrix enthält die Belastung von selbst, weil $\underline A_{21}$ und $\underline A_{22}$ des zweiten Glieds den Strom beschreiben, den es aufnimmt.

:::formel Satz
$$\mathbf A = \mathbf A_\mathrm a\,\mathbf A_\mathrm b$$
:::

**So liest man das:** Die Kettenmatrix einer Kette ist das Produkt der Kettenmatrizen, links das Glied am Eingang; für mehr Glieder ist sie $\mathbf A_\mathrm a\mathbf A_\mathrm b\mathbf A_\mathrm c\cdots$. Mit einer Last $\underline Y_L$ am Ende ist $-\underline I_2$ gleich $\underline Y_L\,\underline U_2$, und es folgen Übertragung und Eingangsadmittanz der Kette:

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

**Einordnung:** Dieselben drei Zahlen lieferte im Artikel über Testquellen die modifizierte Knotenanalyse der ganzen Schaltung; hier entstehen sie aus zwei 2×2-Matrizen. Das Produkt der Einzelübertragungen läge um 50 % zu hoch. Weit unterhalb und oberhalb der Eckfrequenz ist der Fehler klein, 0,967 gegen 0,990 bei 10³ 1/s und 0,0097 gegen 0,0099 bei 10⁵ 1/s, weil dort entweder der Strom ins zweite Glied oder der Spannungsabfall am ersten Widerstand klein ist.

**Variation:** Reihenfolge mit der Verstärkerstufe und 10 kΩ Last: RC-Glied vor der Stufe ergibt 1,644 mit Winkel 135°, die Stufe vor dem RC-Glied nur 0,435 mit Winkel 101°. Gemessen an der Stufe allein, 2,326, lässt das RC-Glied davor das 0,707-Fache durch, dahinter nur das 0,187-Fache: Dort lädt der Kondensator über die 8,90 kΩ der Stufe und den Widerstand des RC-Glieds, parallel zur Last rund 5 kΩ statt 1 kΩ, und die Eckfrequenz sinkt auf ein Fünftel.
::::

:::fehlvorstellung
„Die Übertragung einer Kette ist das Produkt der Einzelübertragungen.“ Das liegt nahe, weil man Blöcke in Signalflussplänen genau so verknüpft. Es gilt aber nur, wenn kein Glied den Ausgang des vorigen belastet oder wenn man jede Einzelübertragung unter der tatsächlichen Last bestimmt. Der zweistufige RC-Tiefpass überträgt bei seiner Eckfrequenz 1/3, nicht 1/2, weil das zweite Glied dem ersten (1 − j) kΩ als Last anbietet. Zwei Verstärkerstufen, deren Gates keinen Strom aufnehmen, multiplizieren ihre Leerlaufverstärkungen dagegen exakt: Zweimal 4,396 ergibt 19,32-fache Verstärkung. Die Kettenmatrix enthält beide Fälle.
:::

Jedes Glied, das aus Längs- und Quergliedern besteht, ein __Kettenleiter__, ist das Produkt ihrer Matrizen, wie das RC-Glied oben. Vertauscht man beim RC-Glied die Reihenfolge (Abbildung 7), liegt der Kondensator am Eingang und der Widerstand am Ausgang: Bei offenem Ausgang fließt durch den Widerstand kein Strom, und das Glied überträgt die Spannung ungeändert, $\underline A_{11}$ = 1. Erst eine Last macht es zum Teiler, mit 1 kΩ auf 0,5, während das RC-Glied dort 0,4 − 0,2j liefert.

:::grafik
Szene: st1/netzwerkanalyse/05-laengs-quer · Vorlage: schaltbild-matrix
**Abbildung 7:** Links ein Längsglied mit der Impedanz $\underline Z$ und seine Kettenmatrix (1; $\underline Z$; 0; 1), daneben ein Querglied mit der Admittanz $\underline Y$ und seine Kettenmatrix (1; 0; $\underline Y$; 1). Rechts zwei Anordnungen aus 1 kΩ und 100 nF bei ω = 10⁴ 1/s: das RC-Glied, Längsglied vor Querglied, mit dem Produkt (1 + j; 1 kΩ; j·1 mS; 1) und offen 0,5 − 0,5j; das umgekehrte Glied, Querglied vor Längsglied, mit (1; 1 kΩ; j·1 mS; 1 + j) und offen 1. Ein Kettenleiter ist das Produkt der Matrizen seiner Längs- und Querglieder in der Reihenfolge der Glieder.
:::

## Parallelschaltung: Admittanzmatrizen addieren sich

*Wie fasst man zwei Zweitore zusammen, deren Eingänge und Ausgänge jeweils parallel liegen?*

:::grafik
Szene: st1/netzwerkanalyse/05-parallelschaltung · Vorlage: schaltbild-matrix
**Abbildung 8:** (a) Zwei Zweitore a und b mit gemeinsamer unterer Leitung, Eingänge parallel, Ausgänge parallel; an beiden liegen dieselben Spannungen $\underline U_1$ und $\underline U_2$, und die Torströme addieren sich. (b) Die Stufe ohne Source-Widerstand bei ω = 10⁸ 1/s als Parallelschaltung: oben das Transistor-Zweitor aus $C_{gs}$, gesteuerter Quelle $g_m\underline U_1$ und $G_D + g_o$ mit den Admittanzen j·10, 0, 1000 und 125 µS; unten das Längsglied $C_{gd}$ mit j·2, −j·2, −j·2 und j·2 µS; rechts die Summe j·12, −j·2, 1000 − j·2 und 125 + j·2 µS. Ein Längsglied zwischen Eingang und Ausgang ist parallel geschaltet und erzeugt die Rückwirkung.
:::

Bei der __Parallelschaltung__ liegen die Eingangstore zweier Zweitore parallel und ebenso die Ausgangstore. Beide Teile haben dann dieselben Torspannungen, und ihre Torströme addieren sich zu den Strömen der Zusammenschaltung. Gemeinsam sind die Spannungen, also ist die Admittanzform die passende.

**Die Akteure:**

- __$\mathbf Y_\mathrm a$__, __$\mathbf Y_\mathrm b$__: Admittanzmatrizen der beiden Teile.

:::formel Satz
$$\mathbf Y = \mathbf Y_\mathrm a + \mathbf Y_\mathrm b$$
:::

**So liest man das:** Alle vier Einträge addieren sich; bei mehr Teilen wird die Summe entsprechend länger, $\mathbf Y_\mathrm a + \mathbf Y_\mathrm b + \mathbf Y_\mathrm c + \cdots$. Ein Längsglied zwischen Eingang und Ausgang, etwa eine Gate-Drain-Kapazität oder ein Rückkopplungswiderstand vom Drain zum Gate, ist ein parallel geschaltetes Zweitor: Es fügt seine Admittanz den Diagonaleinträgen hinzu und zieht sie von den Nebeneinträgen ab, erzeugt also Rückwirkung. Die Regel setzt voraus, dass jedes Teil seine Torbedingung behält. Sicher ist das, wenn beide Teile eine durchgehende untere Leitung haben und diese miteinander verbunden sind, wie bei Schaltungen an gemeinsamer Masse. Dann sind alle unteren Klemmen ein einziger Knoten, jedes Teil ist ein __Dreipol__, eine Schaltung mit drei Anschlüssen, und seine Torgrößen beziehen sich auf den gemeinsamen Anschluss; wie sich der Rückstrom auf 1′ und 2′ verteilt, spielt dann keine Rolle.

**Kurz gesagt:** Die Admittanzmatrix der Parallelschaltung ist die Summe der Admittanzmatrizen, solange jedes Teil seine Torbedingung behält.

Idee der Herleitung: Man setzt die gemeinsamen Spannungen in die Admittanzgleichungen beider Teile ein und addiert die Ströme.

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

::::beispiel Stufe mit Gate-Drain-Kapazität als Parallelschaltung
**Gegeben:** das Transistor-Zweitor der Stufe ohne Source-Widerstand bei ω = 10⁸ 1/s mit $C_{gs}$ = 100 fF, $g_m$ = 1 mS und $G_D + g_o$ = 125 µS; das Längsglied $C_{gd}$ = 20 fF zwischen Gate und Drain.

**Gesucht:** die Admittanzmatrix der ganzen Stufe.

**Rechnung:** Das Transistor-Zweitor ist rückwirkungsfrei, das Längsglied hat die Admittanzmatrix eines Längszweigs; beide haben die Masse als gemeinsame Leitung:

$$\mathbf Y_\mathrm T = \begin{pmatrix} j\,10 & 0 \\ 1000 & 125 \end{pmatrix}\mathrm{\mu S}, \qquad \mathbf Y_\mathrm F = j\,2\begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}\mathrm{\mu S}\,$$

$$\mathbf Y = \mathbf Y_\mathrm T + \mathbf Y_\mathrm F = \begin{pmatrix} j\,12 & -j\,2 \\ 1000 - j\,2 & 125 + j\,2 \end{pmatrix}\mathrm{\mu S}$$

**Ergebnis:** **Dieselbe Matrix wie aus den Kurzschlussversuchen an der ganzen Stufe.**

**Einordnung:** Die gesamte Rückwirkung, −j·2 µS, stammt aus dem Längsglied; das Transistor-Zweitor allein ist rückwirkungsfrei. Ein Rückkopplungswiderstand vom Drain zum Gate würde auf dieselbe Weise einen reellen Anteil hinzufügen.
::::

## Reihenschaltung: Impedanzmatrizen addieren sich, solange die Torbedingung hält

*Wann darf man bei zwei Zweitoren, deren Tore in Reihe liegen, die Impedanzmatrizen addieren?*

:::grafik
Szene: st1/netzwerkanalyse/05-reihenschaltung-t · Vorlage: schaltbild-vergleich
**Abbildung 9:** Zwei T-Glieder aus je drei Widerständen von 1 kΩ, Eingänge in Reihe, Ausgänge in Reihe. (a) Beide mit durchgehender unterer Leitung: Die untere Leitung des oberen Glieds verbindet die oberen Klemmen des unteren Glieds; mit 1 mA in Tor 1 und offenem Tor 2 fließen je 0,5 mA in die beiden oberen Klemmen des unteren Glieds, aber 1 mA aus seiner Klemme 1′ (Strompfeile mit Werten, rot markiert); Potentiale 3,5 V, 2,5 V, 1,5 V und 1,0 V; Impedanzmatrix 3,5, 2,5, 2,5 und 3,5 kΩ statt der Summe 4, 2, 2 und 4 kΩ. (b) Das untere Glied umgedreht, seine durchgehende Leitung oben an der unteren Leitung des oberen Glieds: Impedanzmatrix gleich der Summe. (c) Brune-Test: Eingänge in Reihe mit 1 mA gespeist, Ausgänge offen und noch nicht verbunden; zwischen den zu verbindenden Ausgangsklemmen liegen in (a) 1 V, in (b) 0 V. Ob man Impedanzmatrizen addieren darf, entscheidet die Torbedingung jedes Teils.
:::

**Die Akteure:**

- __$\mathbf Z_\mathrm a$__, __$\mathbf Z_\mathrm b$__: Impedanzmatrizen der beiden Teile; für das T-Glied aus drei 1-kΩ-Widerständen 2, 1, 1 und 2 kΩ.

**Das Zusammenspiel:**

**Schritt 1**: Bei der __Reihenschaltung__ liegen die Eingangstore in Reihe, die untere Eingangsklemme des einen an der oberen des anderen, und ebenso die Ausgangstore. Durch beide Eingangstore fließt derselbe Strom, und ihre Spannungen addieren sich; am Ausgang ebenso.

**Schritt 2**: Gilt in jedem Teil die Impedanzform mit diesen gemeinsamen Strömen, addieren sich die Impedanzmatrizen. Das setzt voraus, dass jedes Teil seine Torbedingung behält: Der Strom, der an seiner oberen Eingangsklemme hineinfließt, muss an seiner unteren herauskommen.

**Schritt 3**: Bei zwei T-Gliedern mit durchgehender unterer Leitung ist das verletzt. Die untere Leitung des oberen Glieds verbindet seine Klemmen 1′ und 2′, und an diesen hängen in der Reihenschaltung die oberen Klemmen 1 und 2 des unteren Glieds. Dessen beide Längswiderstände, zusammen 2 kΩ zwischen diesen Klemmen, werden überbrückt.

**Schritt 4**: Der Strom teilt sich deshalb anders auf, als die Torgrößen annehmen: Mit 1 mA in Tor 1 und offenem Tor 2 fließen je 0,5 mA in die Klemmen 1 und 2 des unteren Glieds, aber 1 mA aus seiner Klemme 1′. Die Summenregel setzt dagegen voraus, dass durch das untere Glied die Torströme der Zusammenschaltung fließen, 1 mA und 0.

**Schritt 5**: Die Impedanzmatrix der Zusammenschaltung hat die Einträge 3,5, 2,5, 2,5 und 3,5 kΩ statt der Summe 4, 2, 2 und 4 kΩ, in jedem Eintrag um 0,5 kΩ daneben.

**Schritt 6**: Dreht man das untere Glied um, liegt seine durchgehende Leitung oben und trifft die durchgehende untere Leitung des oberen Glieds. Die Klemmen, die zwischen den Teilen verbunden werden, sind dann in beiden Teilen ohnehin verbunden, nichts wird überbrückt, und die Summe stimmt.

:::formel Satz
$$\mathbf Z = \mathbf Z_\mathrm a + \mathbf Z_\mathrm b$$
:::

**So liest man das:** Alle vier Einträge addieren sich, bei mehr Teilen ebenso, $\mathbf Z_\mathrm a + \mathbf Z_\mathrm b + \mathbf Z_\mathrm c + \cdots$, solange jedes Teil seine Torbedingung behält. Ob das so ist, zeigt der __Brune-Test__: Man schaltet die Eingänge in Reihe und speist sie, lässt die Ausgänge offen und noch unverbunden und bestimmt die Spannung zwischen den beiden Ausgangsklemmen, die verbunden werden sollen; danach dasselbe mit vertauschten Toren. Ist beide Male keine Spannung vorhanden, fließt nach dem Verbinden kein Ausgleichsstrom, und die Regel gilt. Bei den T-Gliedern liegen dort 1 V bei 1 mA. Für die Parallelschaltung prüft man ebenso, mit parallel gespeisten Eingängen und einzeln kurzgeschlossenen Ausgängen. Fällt der Test schlecht aus, dreht man ein Teil um oder trennt die Leitungen durch einen idealen Übertrager 1 : 1 an einem Tor, der die Spannung weitergibt, die Leitungen aber galvanisch trennt.

**Kurz gesagt:** Die Impedanzmatrix der Reihenschaltung ist die Summe der Impedanzmatrizen, solange jedes Teil seine Torbedingung behält.

Idee der Herleitung: Man setzt die gemeinsamen Ströme in die Impedanzgleichungen beider Teile ein und addiert die Spannungen; beim T-Glied rechnet man die tatsächlichen Ströme nach.

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
**Gegeben:** zwei T-Glieder aus je drei Widerständen von 1 kΩ, Impedanzmatrix je 2, 1, 1 und 2 kΩ.

**Gesucht:** die Impedanzmatrix der Reihenschaltung in beiden Anordnungen und der Brune-Test.

**Rechnung:** Die Summe der Matrizen:

$$\mathbf Z_\mathrm a + \mathbf Z_\mathrm b = \begin{pmatrix} 4 & 2 \\ 2 & 4 \end{pmatrix}\mathrm{k\Omega}$$

Beide mit unterer Masseleitung, mit 1 mA in Tor 1: Potentiale 3,5 V an Klemme 1, 2,5 V am Mittelpunkt des oberen Glieds, 1,5 V auf seiner unteren Leitung und 1,0 V am Mittelpunkt des unteren; in die oberen Klemmen des unteren Glieds fließen je 0,5 mA, aus seiner unteren Leitung 1 mA:

$$\mathbf Z = \begin{pmatrix} 3{,}5 & 2{,}5 \\ 2{,}5 & 3{,}5 \end{pmatrix}\mathrm{k\Omega} \neq \mathbf Z_\mathrm a + \mathbf Z_\mathrm b$$

Brune-Test mit 1 mA, die Ausgänge offen und noch unverbunden: Der Strom fließt durch je einen Längs- und den Querwiderstand beider Glieder. Die untere Leitung des oberen Glieds liegt dann auf 2 V, der Mittelpunkt des unteren auf 1 V. Die zu verbindende Klemme 2′ des oberen Glieds sitzt auf dessen unterer Leitung, die Klemme 2 des unteren hängt stromlos am Mittelpunkt:

$$2\ \mathrm V - 1\ \mathrm V = 1\ \mathrm V$$

Mit umgedrehtem unterem Glied sind beide Klemmen Teil derselben durchgehenden Leitung, und die Spannung ist null.

**Ergebnis:** **Mit beiden Masseleitungen unten 3,5, 2,5, 2,5 und 3,5 kΩ, falsch, und 1 V im Brune-Test; mit umgedrehtem unterem Glied 4, 2, 2 und 4 kΩ, die Summe.**

**Einordnung:** Der Fehler ist kein Rundungsproblem: Die untere Leitung des oberen Glieds legt die beiden Längswiderstände des unteren parallel. In Schaltungen mit gemeinsamer Masse sind deshalb Parallelschaltungen unproblematisch, Reihenschaltungen dagegen nur, wenn die gemeinsame Leitung des einen Teils auf eine durchgehende Leitung des anderen trifft.
::::

Die wichtigste Anwendung der Reihenschaltung ist die __Stromgegenkopplung__: Ein Widerstand in der gemeinsamen Leitung eines Transistors führt einen Teil des Ausgangsstroms als Spannung an den Eingang zurück. Beim [Bipolartransistor](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker-ausfuehrlich.html) ist das der Emitterwiderstand $R_E$ (Abbildung 10). Der Transistor verhält sich für kleine Signale wie ein Zweitor aus dem Eingangswiderstand $r_{BE}$ zwischen Basis und Emitter, einer stromgesteuerten Stromquelle mit dem β-Fachen des Basisstroms vom Kollektor zum Emitter und dem Ausgangswiderstand $r_{CE}$; seine gemeinsame Leitung ist der Emitter. $R_E$ ist ein Querglied, dessen obere Leitung durchgehend ist und am Emitter liegt; damit trifft die gemeinsame Leitung des Transistors auf eine durchgehende Leitung wie beim umgedrehten T-Glied, und die Impedanzmatrizen addieren sich.

:::grafik
Szene: st1/netzwerkanalyse/05-bipolar-re · Vorlage: schaltbild-matrix
**Abbildung 10:** (a) Kleinsignal-Ersatzschaltbild einer Bipolarstufe ohne Emitterkondensator als Reihenschaltung: oben das Transistor-Zweitor mit $r_{BE}$ = 13,71 kΩ zwischen Basis und Emitter, der stromgesteuerten Stromquelle $\beta\,\underline I_1$ mit β = 502,4 vom Kollektor zum Emitter und $r_{CE}$ = 79,57 kΩ; darunter das Querglied $R_E$ = 1 kΩ, dessen obere Leitung am Emitter liegt; am Kollektor die Last $R_C$ = 3,9 kΩ, der Basisspannungsteiler weggelassen. (b) Die Impedanzmatrizen in kΩ, auf vier Stellen gerundet: Transistor 13,71, 0, −39 970 und 79,57; Querglied 1, 1, 1 und 1; Summe 14,71, 1, −39 970 und 80,57. Der Emitterwiderstand addiert sich zu allen vier Einträgen und hebt den Eingangswiderstand von 13,7 kΩ auf 488 kΩ.
:::

::::beispiel Emitterwiderstand als Reihenschaltung: Bipolarstufe ohne Emitterkondensator
**Gegeben:** der Beispieltransistor bei $I_C$ = 0,947 mA mit $r_{BE}$ = 13,713 kΩ, β = 502,38 und $r_{CE}$ = 79,566 kΩ; Emitterwiderstand $R_E$ = 1 kΩ; Kollektorwiderstand $R_C$ = 3,9 kΩ als Last am Ausgang; Tor 1 zwischen Basis und Masse, Tor 2 zwischen Kollektor und Masse.

**Gesucht:** die Impedanzmatrix der Stufe, ihr Eingangswiderstand an der Basis und ihre Spannungsverstärkung mit $R_C$.

**Rechnung:** Transistor-Zweitor bei offenem Kollektor: Der Basisstrom fließt durch $r_{BE}$, und der Strom der gesteuerten Quelle, $\beta\,\underline I_1$, muss durch $r_{CE}$ zurückfließen; bei offener Basis bleibt nur $r_{CE}$:

$$\mathbf Z_\mathrm T = \begin{pmatrix} r_{BE} & 0 \\ -\beta\,r_{CE} & r_{CE} \end{pmatrix} = \begin{pmatrix} 13{,}71 & 0 \\ -39\,970 & 79{,}57 \end{pmatrix}\mathrm{k\Omega}$$

Reihenschaltung mit dem Querglied, auf vier Stellen gerundet:

$$\mathbf Z = \mathbf Z_\mathrm T + R_E\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 14{,}71 & 1 \\ -39\,970 & 80{,}57 \end{pmatrix}\mathrm{k\Omega}$$

Mit der Last am Ausgang folgen die Eingangsimpedanz $\underline Z_\mathrm{ein}$, der Kehrwert der Eingangsadmittanz, und die Verstärkung, hier in der Impedanzform:

:::herleitung
**Ausgangspunkt:** die Impedanzgleichungen und die Last $R_C$ am Ausgang.

**Annahmen:** (i) Die Last ist ein Widerstand zwischen Kollektor und Masse. (ii) $\underline Z_{22} + R_C$ ist nicht null.

**Schritt 1**: Der Strom $\underline I_2$ fließt in den Kollektor hinein, also aus der Last heraus; deshalb ist $\underline U_2$ gleich $-R_C\,\underline I_2$. Eingesetzt in die zweite Impedanzgleichung:

$$\underline I_2 = -\frac{\underline Z_{21}}{\underline Z_{22} + R_C}\,\underline I_1$$

**Schritt 2**: In die erste Impedanzgleichung eingesetzt:

$$\underline U_1 = \Big(\underline Z_{11} - \frac{\underline Z_{12}\,\underline Z_{21}}{\underline Z_{22} + R_C}\Big)\underline I_1$$

**Schritt 3**: Die Ausgangsspannung ist $-R_C$ mal Ausgangsstrom; geteilt durch die Eingangsspannung aus Schritt 2 und mit $\underline Z_{22} + R_C$ erweitert:

$$\underline U_2 = -R_C\,\underline I_2 = \frac{R_C\,\underline Z_{21}}{\underline Z_{22} + R_C}\,\underline I_1, \qquad \frac{\underline U_2}{\underline U_1} = \frac{R_C\,\underline Z_{21}}{(\underline Z_{22} + R_C)\,\underline Z_{11} - \underline Z_{12}\,\underline Z_{21}}\,$$

**Ergebnis:**

$$\underline Z_\mathrm{ein} = \underline Z_{11} - \frac{\underline Z_{12}\,\underline Z_{21}}{\underline Z_{22} + R_C}, \qquad \frac{\underline U_2}{\underline U_1} = \frac{R_C\,\underline Z_{21}}{(\underline Z_{22} + R_C)\,\underline Z_{11} - \underline Z_{12}\,\underline Z_{21}}\,$$

**Woher die Faktoren kommen:** Es ist dieselbe Rechnung wie für die Eingangsadmittanz unter Last, mit Strömen und Spannungen vertauscht.

**Proben:** Ohne Rückwirkung, $\underline Z_{12}$ = 0, bleibt $\underline Z_\mathrm{ein} = \underline Z_{11}$; Einheiten Ω bzw. ohne Einheit.

**Grenzen:** wie bei der Eingangsadmittanz unter Last.
:::

$$\underline Z_\mathrm{ein} = 14{,}71\ \mathrm{k\Omega} + \frac{39\,970}{84{,}47}\ \mathrm{k\Omega} = 487{,}9\ \mathrm{k\Omega}, \qquad \frac{\underline U_2}{\underline U_1} = \frac{3{,}9\cdot(-39\,970)}{84{,}47\cdot 14{,}71 + 39\,970} = -3{,}782\,$$

**Ergebnis:** **Eingangswiderstand an der Basis 487,9 kΩ statt 13,71 kΩ ohne $R_E$; Spannungsverstärkung −3,782.**

**Einordnung:** Dieselbe Verstärkung, −3,782, ergibt die Rechnung mit dem vollständigen nichtlinearen Transistormodell im Artikel über den Transistor als Verstärker. Die bekannten Näherungen $r_{BE} + (\beta + 1)R_E$ = 517 kΩ und $-\beta R_C/(r_{BE} + (\beta + 1)R_E)$ = −3,789 vernachlässigen $r_{CE}$; die Zweitorrechnung enthält ihn ohne Mehraufwand. Der Emitterwiderstand steht auch auf der Nebendiagonalen: $\underline Z_{12}$ = 1 kΩ heißt, dass der Ausgangsstrom am Eingang eine Spannung erzeugt, die Rückwirkung der Gegenkopplung.
::::

## Hybridform und Reihen-Parallel-Schaltung

*Welche Form passt zu Zweitoren, deren Eingänge in Reihe und deren Ausgänge parallel liegen, und warum beschreibt man Bipolartransistoren damit?*

Gibt man den Eingangsstrom und die Ausgangsspannung vor, entsteht die __Hybridform__, so genannt, weil ihre Parameter Leerlauf- und Kurzschlussgrößen mischen und verschiedene Einheiten haben. Für den Bipolartransistor ist sie die gebräuchliche Form: Im Kleinsignalmodell schreibt man seinen Kollektorstrom als β-Faches des Basisstroms. Das ist gleichwertig zur Steilheit mal Basis-Emitter-Spannung, weil der Basisstrom die Basis-Emitter-Spannung geteilt durch $r_{BE}$ ist; physikalisch steuert die Basis-Emitter-Spannung. Sein Ausgang verhält sich wie eine Stromquelle mit großem Innenwiderstand, deren Strom man bei fester Ausgangsspannung angibt. Das Ersatzschaltbild in Abbildung 10 oben ist genau diese Form.

**Die Akteure:**

- __$\underline H_{11}$__ in Ω, __$\underline H_{12}$__ und __$\underline H_{21}$__ ohne Einheit, __$\underline H_{22}$__ in S: die __Hybridparameter__; beim Beispieltransistor 13,71 kΩ, 0, 502,4 und 12,57 µS.
- __$\mathbf H$__: die __Hybridmatrix__.

:::formel Definition
$$\underline U_1 = \underline H_{11}\,\underline I_1 + \underline H_{12}\,\underline U_2, \qquad \underline I_2 = \underline H_{21}\,\underline I_1 + \underline H_{22}\,\underline U_2\,$$
:::

**So liest man das:** Man bestimmt die Parameter mit kurzgeschlossenem Ausgang und mit offenem Eingang:

$$\underline H_{11} = \frac{\underline U_1}{\underline I_1}\bigg|_{\underline U_2 = 0}, \qquad \underline H_{21} = \frac{\underline I_2}{\underline I_1}\bigg|_{\underline U_2 = 0}, \qquad \underline H_{12} = \frac{\underline U_1}{\underline U_2}\bigg|_{\underline I_1 = 0}, \qquad \underline H_{22} = \frac{\underline I_2}{\underline U_2}\bigg|_{\underline I_1 = 0}\,$$

$\underline H_{11}$ ist die Kurzschluss-Eingangsimpedanz, $\underline H_{21}$ die Kurzschluss-Stromübertragung, beim Transistor die Stromverstärkung β, $\underline H_{12}$ die Leerlauf-Spannungsrückwirkung und $\underline H_{22}$ die Leerlauf-Ausgangsadmittanz. Datenblätter nennen sie beim Transistor in Emitterschaltung $h_{ie}$, $h_{fe}$, $h_{re}$ und $h_{oe}$. Reziprok ist ein Zweitor in dieser Form, wenn $\underline H_{12}$ gleich $-\underline H_{21}$ ist, rückwirkungsfrei, wenn $\underline H_{12}$ null ist. Zur Impedanzform führt das Auflösen nach den Spannungen:

$$\mathbf Z = \frac{1}{\underline H_{22}}\begin{pmatrix} \det\mathbf H & \underline H_{12} \\ -\underline H_{21} & 1 \end{pmatrix}$$

Liegen bei zwei Zweitoren die Eingänge in Reihe und die Ausgänge parallel, die __Reihen-Parallel-Schaltung__, sind Eingangsstrom und Ausgangsspannung gemeinsam, und die Hybridmatrizen addieren sich, wieder unter der Bedingung, dass jedes Teil seine Torbedingung behält. Für Eingänge parallel und Ausgänge in Reihe gilt dasselbe mit der inversen Hybridform. Die inverse Kettenform beschreibt eine Kette vom Ausgang zum Eingang hin und wird selten gebraucht.

**Kurz gesagt:** Die Hybridmatrix der Reihen-Parallel-Schaltung ist die Summe der Hybridmatrizen, solange jedes Teil seine Torbedingung behält.

:::herleitung
**Ausgangspunkt:** die Hybridgleichungen, die Impedanzgleichungen und die Verbindungsbedingungen der Reihen-Parallel-Schaltung.

**Annahmen:** (i) Die Formen existieren. (ii) Jedes Teil behält seine Torbedingung.

**Schritt 1**: Mit kurzgeschlossenem Ausgang bzw. offenem Eingang bleibt in jeder Gleichung ein Glied; geteilt durch die vorgegebene Größe sind das die vier Messvorschriften:

$$\underline U_1 = \underline H_{11}\,\underline I_1, \quad \underline I_2 = \underline H_{21}\,\underline I_1 \quad (\underline U_2 = 0), \qquad \underline U_1 = \underline H_{12}\,\underline U_2, \quad \underline I_2 = \underline H_{22}\,\underline U_2 \quad (\underline I_1 = 0)\,$$

**Schritt 2**: Die zweite Hybridgleichung nach $\underline U_2$ aufgelöst und in die erste eingesetzt:

$$\underline U_2 = -\frac{\underline H_{21}}{\underline H_{22}}\,\underline I_1 + \frac{1}{\underline H_{22}}\,\underline I_2, \qquad \underline U_1 = \frac{\underline H_{11}\underline H_{22} - \underline H_{12}\underline H_{21}}{\underline H_{22}}\,\underline I_1 + \frac{\underline H_{12}}{\underline H_{22}}\,\underline I_2\,$$

Abgelesen ist das die Impedanzmatrix. Ihre Nebeneinträge sind $\underline H_{12}/\underline H_{22}$ und $-\underline H_{21}/\underline H_{22}$; sie sind genau dann gleich, das Zweitor also reziprok, wenn $\underline H_{12}$ gleich $-\underline H_{21}$ ist.

**Schritt 3** (entscheidender Schritt): In der Reihen-Parallel-Schaltung führen beide Eingänge denselben Strom, und beide Ausgänge haben dieselbe Spannung; die Eingangsspannungen und die Ausgangsströme addieren sich:

$$\begin{pmatrix} \underline U_1 \\ \underline I_2 \end{pmatrix} = (\mathbf H_\mathrm a + \mathbf H_\mathrm b)\begin{pmatrix} \underline I_1 \\ \underline U_2 \end{pmatrix}$$

**Ergebnis:** die Messvorschriften, die Umrechnung in die Impedanzform und $\mathbf H = \mathbf H_\mathrm a + \mathbf H_\mathrm b$.

**Woher die Faktoren kommen:** Jede Zusammenschaltung addiert die Matrix der Form, deren vorgegebene Größen beiden Teilen gemeinsam sind.

**Proben:** Einheiten: $\underline H_{11}$ steht vor einem Strom in einer Spannungsgleichung, also Ω; $\underline H_{22}$ vor einer Spannung in einer Stromgleichung, also S. Transistor: $\det\mathbf H/\underline H_{22}$ ist $r_{BE}$, $-\underline H_{21}/\underline H_{22}$ ist $-\beta r_{CE}$, wie im Beispiel zur Reihenschaltung.

**Grenzen:** Ist $\underline H_{22}$ null, etwa bei einer idealen gesteuerten Stromquelle ohne Innenleitwert, gibt es keine Impedanzform, die Hybridform aber schon.
:::

::::beispiel Hybridparameter des Beispieltransistors
**Gegeben:** $r_{BE}$ = 13,713 kΩ, β = 502,38 und $r_{CE}$ = 79,566 kΩ bei $I_C$ = 0,947 mA.

**Gesucht:** die Hybridmatrix und die Probe gegen die Impedanzmatrix aus der Reihenschaltung.

**Rechnung:** Bei kurzgeschlossenem Ausgang sieht der Basisstrom nur $r_{BE}$, und in den Kollektor fließt das β-Fache; bei offener Basis bleibt am Ausgang $r_{CE}$, und die Basis bleibt spannungslos:

$$\mathbf H = \begin{pmatrix} 13{,}713\ \mathrm{k\Omega} & 0 \\ 502{,}38 & 12{,}568\ \mathrm{\mu S} \end{pmatrix}$$

Umgerechnet:

$$\underline Z_{11} = \frac{\det\mathbf H}{\underline H_{22}} = 13{,}71\ \mathrm{k\Omega}, \qquad \underline Z_{21} = -\frac{\underline H_{21}}{\underline H_{22}} = -\frac{502{,}38}{12{,}568\ \mathrm{\mu S}} = -39\,970\ \mathrm{k\Omega}, \qquad \underline Z_{22} = \frac{1}{\underline H_{22}} = 79{,}57\ \mathrm{k\Omega}\,$$

**Ergebnis:** **$\mathbf H$ mit 13,71 kΩ, 0, 502,4 und 12,57 µS; daraus die Impedanzmatrix des Transistor-Zweitors.**

**Einordnung:** Datenblätter nennen dieselben Größen; für den BC547C bei 2 mA typisch $h_{ie}$ = 8,7 kΩ, $h_{fe}$ = 600, $h_{oe}$ = 60 µS und $h_{re}$ = 3·10⁻⁴. Die kleine Spannungsrückwirkung $h_{re}$ vernachlässigt das Modell. Die Hybridform hat hier die übersichtlichsten Einträge, weil sie genau die beiden Größen vorgibt, mit denen das Modell den Transistor beschreibt, den Basisstrom und die Kollektor-Emitter-Spannung.
::::

## Zweitore in der Signalverarbeitung

*Wie viel Signal kommt durch eine Kette von Verstärkerstufen zwischen Quelle und Last, und wo geht es verloren?*

:::grafik
Szene: st1/netzwerkanalyse/05-signalkette · Vorlage: blockbild-schaltbild
**Abbildung 11:** Oben eine Signalkette als Blockbild: Sensor oder Antenne als Quelle mit Innenwiderstand, Verstärker, Filter, Leitung und ein A/D-Umsetzer als Last, jeder Block ein Zweitor. Darunter zwei Verstärkerstufen als rückwirkungsfreie Zweitore zwischen einer Signalquelle mit $R_\mathrm{sig}$ = 10 kΩ und einer Last $R_L$ = 10 kΩ: jede Stufe mit $R_G$ = 100 kΩ am Eingang, gesteuerter Stromquelle 0,494 mS mal Eingangsspannung und $R_\mathrm{aus}$ = 8,90 kΩ; an jeder Schnittstelle ein Teiler hervorgehoben. Pegel bei 1 mV Quellenspannung: 0,909 mV am ersten Gate, −3,67 mV am zweiten, 8,53 mV an der Last. An jeder Schnittstelle einer Kette geht Signal in einem Teiler verloren.
:::

Signalverarbeitung ist eine Kette von Zweitoren. Am Anfang steht eine Quelle mit Innenwiderstand, ein Sensor oder eine Antenne; es folgen Verstärker, Filter und Leitungen, und am Ende ein __A/D-Umsetzer__, der die Spannung in Zahlen umsetzt und für die Kette die Last ist (Abbildung 11 oben). Jede Stufe ist ein Zweitor, die ganze Kette eine Kettenschaltung, und mit Kettenmatrizen ist sie exakt zu berechnen. Für rückwirkungsfreie Stufen genügt ein Bild aus drei Größen: Eingangswiderstand, gesteuerte Stromquelle und Ausgangswiderstand, das Ersatzschaltbild der Admittanzform mit $\underline Y_{12}$ = 0. Weil nichts zurückwirkt, sieht jede Stufe vom Rest der Kette nur den Eingangswiderstand der nächsten; an jeder Schnittstelle teilt sich das Signal.

In ausgeführten Verstärkern hängen so mehrere Source-Stufen hintereinander, jede mit einem Spannungsteiler am Gate, der den Arbeitspunkt einstellt, und mit Koppelkondensatoren zwischen den Stufen, die die Gleichspannungen trennen und für das Signal Kurzschlüsse sind. Der Teiler am Gate macht den Eingangswiderstand endlich.

**Die Akteure:**

- __$\underline U_\mathrm{sig}$__, __$R_\mathrm{sig}$__: Leerlaufspannung und Innenwiderstand der Signalquelle; 10 kΩ wie in den vorigen Artikeln.
- __$R_\mathrm{ein}$__, __$R_\mathrm{aus}$__: Eingangs- und Ausgangswiderstand einer rückwirkungsfreien Stufe, die Kehrwerte von $\underline Y_{11}$ und $\underline Y_{22}$; an der Verstärkerstufe 8,90 kΩ am Ausgang.
- __$R_G$__: der Vorspannungsteiler am Gate, 400 kΩ zur Versorgung von 5 V und 133,3 kΩ nach Masse; er stellt 1,25 V ein und wirkt für das Signal als Parallelschaltung beider, 100 kΩ.

:::formel Formel
$$\frac{\underline U_2}{\underline U_\mathrm{sig}} = \frac{R_\mathrm{ein}}{R_\mathrm{sig} + R_\mathrm{ein}}\cdot\Big(-\underline Y_{21}\,\frac{R_\mathrm{aus}\,R_L}{R_\mathrm{aus} + R_L}\Big)$$
:::

**So liest man das:** Zwei Teiler und eine Steilheit: Die Quellenspannung teilt sich zwischen $R_\mathrm{sig}$ und $R_\mathrm{ein}$, und der gesteuerte Strom fließt in die Parallelschaltung aus $R_\mathrm{aus}$ und $R_L$. In einer Kette ist die Last jeder Stufe der Eingangswiderstand der nächsten, und die Gesamtverstärkung ist das Produkt der Faktoren. Wenig geht verloren, wenn jeder Eingangswiderstand groß ist gegen den Ausgangswiderstand davor; jede invertierende Stufe trägt ein Minuszeichen bei.

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

::::beispiel Zwei Verstärkerstufen zwischen Sensor und Last
**Gegeben:** Signalquelle mit $R_\mathrm{sig}$ = 10 kΩ; zwei gleiche Verstärkerstufen mit Vorspannungsteiler, $R_G$ = 100 kΩ am Eingang, $\underline Y_{21}$ = 0,49383 mS, $R_\mathrm{aus}$ = 8,901 kΩ; Last $R_L$ = 10 kΩ.

**Gesucht:** die Gesamtverstärkung und die Verluste an den Schnittstellen.

**Rechnung:** Eingangsteiler, erste Stufe an den 100 kΩ der zweiten, zweite Stufe an der Last:

$$\frac{100}{110} = 0{,}9091, \qquad -0{,}49383\ \mathrm{mS}\cdot\frac{8{,}901\cdot 100}{108{,}9}\ \mathrm{k\Omega} = -4{,}036, \qquad -0{,}49383\ \mathrm{mS}\cdot\frac{8{,}901\cdot 10}{18{,}90}\ \mathrm{k\Omega} = -2{,}326\,$$

$$\frac{\underline U_2}{\underline U_\mathrm{sig}} = 0{,}9091\cdot(-4{,}036)\cdot(-2{,}326) = 8{,}53$$

**Ergebnis:** **Gesamtverstärkung 8,53; aus 1 mV werden 0,909 mV am ersten Gate, −3,67 mV am zweiten und 8,53 mV an der Last.**

**Einordnung:** Das Produkt der Kettenmatrizen beider Stufen, mit Quelle und Last ausgewertet, liefert dieselben 8,53. Ohne Vorspannungsteiler, mit Gates ohne Strom, wären es 10,22. Verloren gehen 9,1 % am Eingang, 8,2 % zwischen den Stufen und 47 % am Ausgang, weil 8,90 kΩ Ausgangswiderstand an 10 kΩ Last fast die Hälfte der Leerlaufspannung kosten; eine Ausgangsstufe mit kleinem Ausgangswiderstand, die Drain-Schaltung, hilft hier.
::::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| vier Parameter | zwei lineare Gleichungen zwischen vier Torgrößen beschreiben das Zweitor vollständig |
| Admittanz-, Impedanz-, Ketten- und Hybridform | dieselben Gleichungen, nach verschiedenen Paaren vorgegebener Größen geordnet |
| Kurzschluss- und Leerlaufversuche | eine vorgegebene Größe null lässt in jeder Gleichung ein Glied verschwinden |
| Umrechnung und Existenz | Auflösen nach dem anderen Paar; die Form fehlt, wo das Paar nicht frei wählbar ist |
| Rückwirkung im Betrieb | im Betrieb ist keine Größe null, und über die Rückwärtsübertragung sieht der Eingang die Last |
| Kettenschaltung | die Ausgangsgrößen des einen Glieds sind die vorgegebenen Größen des nächsten |
| Parallel- und Reihenschaltung | gemeinsame Spannungen bzw. Ströme sind die vorgegebenen Größen, solange die Torbedingung hält |
| Signalkette | rückwirkungsfreie Stufen: an jeder Schnittstelle ein Teiler |

Ein lineares Zweitor ist durch zwei lineare Gleichungen zwischen seinen vier Torgrößen vollständig beschrieben; jede Parameterform ordnet dieselben Gleichungen nach einem anderen Paar vorgegebener Größen, und bei einer Zusammenschaltung nimmt man die Form, deren vorgegebene Größen allen Teilen gemeinsam sind: Dann addieren sich die Matrizen, in der Kette multiplizieren sie sich.

## Bedeutung und Ausblick

Zweitorparameter sind die Sprache, in der Datenblätter, Simulatoren und Entwickler über Verstärker, Filter und Leitungen sprechen. Ein Schaltungssimulator bestimmt sie mit denselben Kurzschluss- und Leerlaufläufen wie in diesem Artikel; Kleinsignaltransistoren werden mit Hybridparametern beschrieben. Bei hohen Frequenzen lassen sich Kurzschlüsse und Leerläufe nicht mehr sauber herstellen; dort misst man mit einem Netzwerkanalysator __Streuparameter__, die das Verhältnis von hin- und rücklaufenden Wellen an einem Bezugswiderstand angeben und sich in die Formen dieses Artikels umrechnen lassen.

Die Grenzen sind die der Linearität und der Torbedingung: Für Netze aus R, L und C gelten Zweitorparameter bei jeder Amplitude, für Transistorschaltungen nur für kleine Signale um einen Arbeitspunkt, und immer für eine feste Frequenz; große Signale verlangen das nichtlineare Modell aus dem Artikel über [Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung-ausfuehrlich.html). Als Nächstes folgen die Bauelemente, deren Kleinsignalmodelle hier schon als Zweitore auftraten, der MOS-Feldeffekttransistor und der Bipolartransistor; die Transistorgrundschaltungen und ihr Frequenzgang mit dem Miller-Effekt setzen dann Stufen als Zweitore zu Verstärkern zusammen.

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
A: Die untere Leitung des oberen Glieds verbindet die oberen Klemmen des unteren und überbrückt dessen Längswiderstände. Mit 1 mA fließen je 0,5 mA in die beiden oberen Klemmen, aber 1 mA aus der unteren: Die Torbedingung ist verletzt. Statt 4, 2, 2 und 4 kΩ ergeben sich 3,5, 2,5, 2,5 und 3,5 kΩ; der Brune-Test zeigt 1 V. Umgedreht stimmt die Summe.
F: Stimmt es, dass jedes passive Zweitor reziprok ist?
A: Nein. Reziprozität folgt aus den symmetrischen Eintragsmustern von R, L und C, nicht aus der Passivität. Ein Gyrator mit $\underline Y_{12}$ = 1 mS und $\underline Y_{21}$ = −1 mS ist verlustlos und damit passiv, aber nicht reziprok; in der Hochfrequenztechnik baut man solche Gyratoren aus vormagnetisiertem Ferrit.
F: Stimmt es, dass $\underline Y_{11}$ der Kehrwert von $\underline Z_{11}$ ist?
A: Nein. $\underline Y_{11}$ wird bei kurzgeschlossenem, $\underline Z_{11}$ bei offenem Ausgang bestimmt; invers sind nur die Matrizen als Ganzes. Beim RC-Glied ist $\underline Y_{11}$ 1 mS, $1/\underline Z_{11}$ dagegen (0,5 + 0,5j) mS.
F: Wie lautet die Admittanzmatrix des RC-Glieds aus 1 kΩ und 100 nF bei ω = 10⁴ 1/s, und wie bestimmt man sie?
A: Mit zwei Kurzschlussversuchen: Ausgang kurzgeschlossen und 1 V am Eingang ergibt 1 mA hinein und −1 mA am Ausgang; Eingang kurzgeschlossen und 1 V am Ausgang ergibt −1 mA am Eingang und (1 + j) mA am Ausgang. Also 1, −1, −1 und (1 + j) mS.
F: Warum hat die Verstärkerstufe mit Source-Widerstand keine Impedanzform, wohl aber eine Kettenmatrix?
A: Ihr Gate nimmt keinen Strom auf; die erste Zeile der Admittanzmatrix ist null, $\det\mathbf Y$ = 0, und ein vorgegebener Gatestrom fände keinen Weg. Die Kettenmatrix verlangt nur $\underline Y_{21}\neq0$: Einträge −0,2275, −2,025 kΩ, 0 und 0; $\det\mathbf A$ = 0 zeigt, dass die Stufe rückwirkungsfrei ist.
F: Wie groß ist die Verstärkung von zwei Verstärkerstufen mit 100 kΩ Vorspannungsteiler zwischen einer 10-kΩ-Quelle und 10 kΩ Last?
A: Eingangsteiler 0,9091, erste Stufe an 100 kΩ −4,036, zweite an 10 kΩ −2,326; zusammen 8,53. Am meisten verliert der Ausgang, weil 8,90 kΩ Ausgangswiderstand an 10 kΩ fast die Hälfte kosten.
F: Warum sind Zweitore aus Widerständen, Kondensatoren und Spulen reziprok?
A: Jedes dieser Bauelemente trägt sich symmetrisch in die Knotenleitwertmatrix ein; mit ihr ist auch die Inverse symmetrisch. Die Übertragungsimpedanzen sind Einträge der Inversen zwischen den Torvektoren, $\underline Z_{21}=\vec t_2^{\,\mathsf T}\mathbf Y_\mathrm K^{-1}\vec t_1$, und wegen der Symmetrie ist $\underline Z_{12}$ gleich $\underline Z_{21}$.
:::

