---
title: Die Diode und ihre Kennlinie
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Halbleiterbauelemente
order: 100300
summary: Wie aus dem pn-Übergang ein Bauteil mit Anode und Kathode wird und was seine Kennlinie in Durchlassrichtung, in Sperrrichtung und im Durchbruch bestimmt, bis hin zu Z-Diode, Kapazitätsdiode, Fotodiode und Solarzelle. Ausführliche Fassung mit allen Herleitungen, der realen Kennlinie, dem Temperaturgang und Korrekturen zum Skript.
tags: Diode, pn-Übergang, Durchlassrichtung, Sperrrichtung, Schleusenspannung, Shockley-Gleichung, Z-Diode
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Eine Diode lässt Strom fast nur in eine Richtung durch. Darauf beruhen Gleichrichter in Netzteilen, Schutzdioden an Mikrocontroller-Eingängen, Spannungsreferenzen, Lichtsensoren und Solarzellen.
Physikalisch ist sie ein pn-Übergang mit zwei Anschlüssen, und ihre ganze Kennlinie folgt aus der Barriere zwischen p- und n-Gebiet: **In Durchlassrichtung senkt die Spannung die Barriere, und der Strom wächst exponentiell, um eine Dekade je 60 mV; in Sperrrichtung bestimmt allein der Nachschub an Ladungsträgern den Strom, und den liefern Wärme kaum, Licht in Maßen und ein sehr starkes Feld im Überfluss.**

Vorausgesetzt wird der Artikel [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html) mit pn-Übergang, Raumladungszone, Diffusionsspannung und den beiden Strömen über die Barriere.
Auf diesem Artikel bauen [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html) und [Gleichrichtung und Ladungspumpe](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/gleichrichtung-und-ladungspumpe.html) auf.

:::grafik
Szene: get1/halbleiterbauelemente/02-aufbau-symbol · Vorlage: bauteil-querschnitt-symbol
**Abbildung 1:** Die Diode als Bauteil. (a) Querschnitt: Metallkontakt, p-Gebiet, Raumladungszone (grau), n-Gebiet, Metallkontakt. (b) Schaltsymbol mit Anode A und Kathode K; Spannung $U$ und Strom $I$ zählen von A nach K. (c) Gehäuse mit einem Ring auf der Kathodenseite. In Durchlassrichtung fließt der Strom von der Anode zur Kathode, in Pfeilrichtung des Symbols.
:::

## Aufbau, Anschlüsse und Zählpfeile

*Wie wird aus einem pn-Übergang ein Bauteil, und wie zählt man Spannung und Strom?*

Eine Diode ist ein Siliziumplättchen, das auf der einen Seite p- und auf der anderen n-dotiert ist (Abbildung 1a). An der Grenze liegt die Raumladungszone, ein weniger als ein Mikrometer breiter Bereich fast ohne bewegliche Ladungsträger; über ihr steht die Barriere, in der Beispieldiode die Diffusionsspannung von 0,714 V ([Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html)). Beide Enden tragen Metallkontakte, an denen die Anschlussdrähte sitzen.
Der Anschluss am p-Gebiet heißt __Anode__ (A), der am n-Gebiet __Kathode__ (K). Die Namen stammen aus der Elektrochemie; wie dort tritt der Strom an der Anode in das Bauteil ein und an der Kathode aus, sobald die Diode leitet.

Das Schaltsymbol (Abbildung 1b) ist ein Dreieck, das auf einen Querstrich zeigt. Das Dreieck weist in die Richtung, in der die Diode leitet, von der Anode zur Kathode; der Querstrich steht für die Kathode. Auf dem Gehäuse markiert ein Ring die Kathodenseite (Abbildung 1c).

Spannung und Strom zählen beide von der Anode zur Kathode. Das ist das Verbraucherzählpfeilsystem aus dem Artikel [Zählpfeile und Vorzeichen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/zaehlpfeile-und-vorzeichen.html): Das Produkt aus $U$ und $I$ ist die Leistung, die die Diode aufnimmt.
Positives $U$ heißt, die Anode liegt auf höherem Potenzial als die Kathode; das ist die __Durchlassrichtung__. Negatives $U$ ist die __Sperrrichtung__.

:::frage
„Die Elektronen laufen doch von der Kathode zur Anode. Warum zeigt das Dreieck in die Gegenrichtung?“
Das Symbol folgt der technischen Stromrichtung, also der Richtung, in die positive Ladung fließen würde. In einer leitenden Diode wandern die Elektronen tatsächlich von der Kathode zur Anode und die Löcher von der Anode zur Kathode; beide Bewegungen ergeben einen Strom in Pfeilrichtung. So stimmen Symbol, Zählpfeil und Vorzeichen der Kennlinie überein: In Pfeilrichtung ist $I$ positiv.
:::

## Die Kennlinie im Überblick

*Welcher Strom fließt bei welcher Spannung?*

:::grafik
Szene: get1/halbleiterbauelemente/02-kennlinie-bereiche · Vorlage: kennlinie-bereiche
**Abbildung 2:** Kennlinie der Beispieldiode, schematisch und mit getrennten Maßstäben: im Durchlassbereich Milliampere bis 0,8 V, im Sperrbereich Pikoampere (real einige 10 pA, bei −1 V −20 pA; ideal −15 fA), der Durchbruch bei rund −100 V. Die drei Bereiche liegen auf völlig verschiedenen Skalen.
:::

**Die Akteure:**

- __$I_S$__: __Sättigungssperrstrom__, kurz Sperrstrom; in A; 1,46·10⁻¹⁴ A bei der Beispieldiode dieses Themas (Silizium, je 10¹⁶ Fremdatome pro cm³ auf beiden Seiten, Fläche 0,1 mm², 300 K). Er ist der Betrag der beiden gleich großen Ströme, die im Gleichgewicht über die Barriere fließen.
- __$U_T$__: __Temperaturspannung__; 25,85 mV bei 300 K. Eine um $U_T$ niedrigere Barriere lässt 2,72-mal so viele Ladungsträger hinüber.

**Das Zusammenspiel:** Abbildung 2 zeigt drei Bereiche.
Im __Durchlassbereich__ senkt die Spannung die Barriere. Der Strom der __Majoritätsträger__, der Sorte in der Überzahl (Elektronen im n-, Löcher im p-Gebiet), die sie überwinden, der Strom hinauf, wächst mit jeden 59,5 mV auf das Zehnfache; ab etwa 0,6 V fließen Milliampere.
Im __Sperrbereich__ ist die Barriere höher als im Gleichgewicht. Der Strom hinauf stirbt aus, und es bleibt der Strom hinunter, den der Nachschub an __Minoritätsträgern__ begrenzt, der seltenen Sorte (Löcher im n-, Elektronen im p-Gebiet): ideal 15 fA, real einige 10 pA.
Im __Durchbruch__ wird das Feld in der Zone so stark, dass es selbst Ladungsträger erzeugt; der Sperrstrom steigt steil an, bei der Beispieldiode ab rund 100 V.

Durchlass- und Sperrbereich beschreibt die __Shockley-Gleichung__:

:::formel Gesetz
$$I = I_S\,\Big[\exp\!\Big(\frac{U}{U_T}\Big) - 1\Big]$$
:::

**So liest man das:** Eingabe ist die Spannung an der Diode, Ausgabe der Strom. Der erste Summand ist der Strom hinauf, die −1 der Strom hinunter, der nicht von der Spannung abhängt.
Ab etwa 0,1 V ist die −1 vernachlässigbar, und der Strom wächst rein exponentiell; unterhalb von etwa −0,1 V ist der Strom gleich $-I_S$. Den Durchbruch enthält die Gleichung nicht.

Das Skript schreibt die Gleichung ohne die −1 (Gl. 10.1, S. 162); das ist ihr Grenzfall für den Durchlassbereich.
Ungenau ist dort die Temperaturspannung: Das Skript nennt „das Produkt k_B · T“ die thermische Spannung. $k_B T$ ist aber eine Energie, bei 300 K 25,85 meV; eine Spannung wird daraus erst durch Division durch die Elementarladung:

$$U_T = \frac{k_B\,T}{e} = \frac{1{,}3806\cdot10^{-23}\ \mathrm{J/K}\cdot300\ \mathrm{K}}{1{,}6022\cdot10^{-19}\ \mathrm{C}} = 25{,}85\ \mathrm{mV}$$

Idee der Herleitung: Die Spannung verschiebt nur die Barriere; darauf reagiert allein der Strom hinauf, mit dem Boltzmann-Faktor der Verschiebung.

:::herleitung
**Ausgangspunkt:** das Zwei-Ströme-Bild des pn-Übergangs, ausführlich hergeleitet im Artikel [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html), Abschnitte *Zwei Ströme im Gleichgewicht* und *Durchlass- und Sperrrichtung*. Im Gleichgewicht fließen zwei gleich große Ströme vom Betrag $I_S$ gegeneinander: der Strom der Majoritätsträger hinauf über die Barriere und der Strom der Minoritätsträger hinunter.

**Annahmen:**
(i) die äußere Spannung fällt ganz an der Raumladungszone ab;
(ii) die Majoritätsträger sind bis an die Zone Boltzmann-verteilt;
(iii) der Nachschub an Minoritätsträgern hängt nicht von der Spannung ab;
(iv) schwache Injektion: Die Ladungsträger, die über die Barriere kommen, bleiben auf der anderen Seite selten gegenüber der Dotierung;
(v) in der Zone entstehen und verschwinden keine Paare.

**Schritt 1**: Mit der Spannung $U$ ist die Barriere für die Elektronen nach (i)

$$W_\mathrm{Barriere} = e\,(U_\mathrm{Diff} - U)$$

**Schritt 2** (entscheidender Schritt): Nach (ii) ist der Strom hinauf proportional zum Anteil der Majoritätsträger mit genug Energie, also zum Boltzmann-Faktor der Barriere. Bezogen auf seinen Wert $I_S$ bei $U = 0$ bleibt nur der Faktor der Absenkung:

$$I_\mathrm{hinauf}(U) = I_S\,\exp\!\Big(\frac{U}{U_T}\Big)$$

**Schritt 3**: Nach (iii) bleibt der Strom hinunter beim Gleichgewichtswert:

$$I_\mathrm{hinunter} = I_S$$

**Schritt 4**: Hinauf wandern Elektronen vom n- ins p-Gebiet und Löcher vom p- ins n-Gebiet; beides ist ein Strom von der Anode zur Kathode und zählt positiv. Netto:

$$I = I_\mathrm{hinauf} - I_\mathrm{hinunter} = I_S\,\Big[\exp\!\Big(\frac{U}{U_T}\Big) - 1\Big]$$

**Ergebnis:**

$$I = I_S\,\Big[\exp\!\Big(\frac{U}{U_T}\Big) - 1\Big]$$

**Woher die Faktoren kommen:** $\exp(U/U_T)$ ist der Boltzmann-Faktor der um $U$ abgesenkten Barriere, die −1 der unveränderte Strom hinunter, $I_S$ der Betrag beider Ströme im Gleichgewicht.

**Proben:** Ohne Spannung ist der Strom null. Für große negative Spannungen geht er gegen $-I_S$. Bei 0,6 V: 1,46·10⁻¹⁴ A mal 1,20·10¹⁰ ergibt 0,175 mA.

**Grenzen:** (i) und (iv) versagen oberhalb von etwa 0,65 V, (v) bei kleinen Strömen und im Sperrbereich; den Durchbruch enthält das Modell nicht.
:::

## Die Durchlassspannung

*Ab welcher Spannung leitet eine Diode, und was legt diesen Wert fest?*

**Die Akteure:**

- __$U_F$__: __Durchlassspannung__, die Spannung an der leitenden Diode bei einem genannten Strom $I_F$ (F für englisch forward); in V; 0,645 V bei 1 mA für die Beispieldiode im idealen Modell.

Nach der Spannung aufgelöst, sagt die Shockley-Gleichung, welche Spannung ein gegebener Strom braucht:

:::formel Formel
$$U = U_T\,\ln\!\Big(\frac{I}{I_S} + 1\Big)$$
:::

**So liest man das:** Eingabe ist der Strom, Ausgabe die Spannung. Der Logarithmus staucht: Jede Verzehnfachung des Stroms erhöht die Spannung um 59,5 mV, das $\ln 10$-Fache von $U_T$.
Zwischen 1 µA und 100 mA, fünf Dekaden, liegen deshalb nur 0,30 V, von 0,467 V bis 0,764 V. Ein größeres $I_S$ verschiebt die ganze Kennlinie zu kleineren Spannungen.

Idee der Herleitung: Man löst die Shockley-Gleichung nach der Spannung auf.

:::herleitung
**Ausgangspunkt:** die Shockley-Gleichung.

**Annahmen:** wie dort; außerdem ist der Strom größer als $-I_S$, sonst hat die Gleichung keine Lösung.

**Schritt 1**: Durch $I_S$ teilen und 1 addieren:

$$\frac{I}{I_S} + 1 = \exp\!\Big(\frac{U}{U_T}\Big)$$

**Schritt 2**: Beide Seiten logarithmieren und mit $U_T$ malnehmen:

$$U = U_T\,\ln\!\Big(\frac{I}{I_S} + 1\Big)$$

**Ergebnis:**

$$U = U_T\,\ln\!\Big(\frac{I}{I_S} + 1\Big)$$

**Woher die Faktoren kommen:** Der Logarithmus kehrt die Exponentialfunktion um; $U_T$ ist die Spannung, die den Strom um den Faktor 2,72 ändert, und damit die Einheit, in der die Spannung zählt.

**Proben:** Ohne Strom ist die Spannung null. Für Ströme weit über $I_S$ erhöht eine Verzehnfachung die Spannung um $U_T \ln 10$, also 59,5 mV. Bei 1 mA: 25,85 mV mal $\ln(6{,}86\cdot10^{10})$, also mal 24,95, ergibt 0,645 V.

**Grenzen:** Ein Sperrstrom über $I_S$ kommt im idealen Modell nicht vor; reale Dioden erreichen ihn durch Generation in der Zone und im Durchbruch.
:::

:::grafik
Szene: get1/halbleiterbauelemente/02-schwelle-massstab · Vorlage: kennlinie-lin-zoom
**Abbildung 3:** Dieselbe ideale Kennlinie der Beispieldiode dreimal linear, mit dem Achsenende 10 µA, 1 mA und 100 mA. Markiert ist, wo der Strom 1 % des Achsenendes erreicht: bei 0,407 V, 0,526 V und 0,645 V. Die scheinbare Schwelle wandert mit dem Maßstab, um 59,5 mV je Dekade.
:::

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Auf einer linearen Achse sieht man den Strom erst, wenn er einige Prozent des Achsenendes erreicht. Wo das geschieht, legt nach Formel 2 der Maßstab fest. Ein Prozent des Endwerts, also 0,1 µA von 10 µA, erreicht die Beispieldiode bei 0,407 V; 10 µA von 1 mA bei 0,526 V; 1 mA von 100 mA bei 0,645 V (Abbildung 3).

**Schritt 2**: Eine Exponentialfunktion sieht in jedem Ausschnitt gleich aus. Die drei Teile von Abbildung 3 zeigen dieselbe Form, jeweils um 0,119 V verschoben; einen ausgezeichneten Knick hat die Kennlinie nicht.

**Schritt 3**: In Schaltungen fließen typisch einige Milliampere. Auf dieser Skala leitet eine Siliziumdiode ab 0,6 bis 0,7 V; diesen Erfahrungswert nennt man __Schleusenspannung__, auch Knie- oder Schwellspannung. Er beschreibt die Kennlinie zusammen mit dem Strombereich der Anwendung und ist kein physikalischer Grenzwert.

**Schritt 4**: Datenblätter nennen deshalb keine Schwelle, sondern die Durchlassspannung bei einem bestimmten Strom. Die Kleinsignaldiode 1N4148 hat höchstens 1 V bei 10 mA; das ist ein garantierter Höchstwert, typische Exemplare liegen um 0,7 V.

::::beispiel Durchlassspannung und scheinbare Schwelle der Beispieldiode
**Gegeben:** Sättigungssperrstrom 1,457·10⁻¹⁴ A, Temperaturspannung 25,85 mV (Zahlenwerk dieses Themas).

**Gesucht:** (a) die Durchlassspannung bei 1 µA, 1 mA und 100 mA; (b) die scheinbare Schwelle für die Achsenenden 10 µA und 100 mA.

**Rechnung:** (a) Mit Formel 2:

$$U(10^{-6}\ \mathrm{A}) = 25{,}85\ \mathrm{mV}\cdot\ln\!\Big(\frac{10^{-6}\ \mathrm{A}}{1{,}457\cdot10^{-14}\ \mathrm{A}} + 1\Big)$$

$$= 25{,}85\ \mathrm{mV}\cdot18{,}04 = 0{,}467\ \mathrm{V}$$

$$U(10^{-3}\ \mathrm{A}) = 25{,}85\ \mathrm{mV}\cdot24{,}95 = 0{,}645\ \mathrm{V}, \qquad U(0{,}1\ \mathrm{A}) = 25{,}85\ \mathrm{mV}\cdot29{,}56 = 0{,}764\ \mathrm{V}$$

(b) Die scheinbare Schwelle liegt dort, wo der Strom 1 % des Achsenendes erreicht. Beim Achsenende 10 µA ist das der Strom 0,1 µA:

$$U(10^{-7}\ \mathrm{A}) = 25{,}85\ \mathrm{mV}\cdot15{,}74 = 0{,}407\ \mathrm{V}$$

Beim Achsenende 100 mA ist es der Strom 1 mA, also 0,645 V aus Teil (a).

**Ergebnis:** **0,467 V, 0,645 V und 0,764 V; die scheinbare Schwelle liegt bei 0,407 V bzw. 0,645 V.**

**Einordnung:** Fünf Dekaden Strom brauchen nur 0,3 V mehr Spannung; deshalb rechnen Schaltungsentwürfe mit rund 0,7 V, und das genügt meist. Die scheinbare Schwelle hängt dagegen allein am Maßstab: Wer Mikroampere misst, sieht dieselbe Diode schon bei 0,4 V leiten.
::::

:::fehlvorstellung
„Die Schleusenspannung von 0,7 V ist eine feste Eigenschaft jeder Siliziumdiode.“
Das liegt nahe, weil Schaltungsrechnungen mit 0,7 V arbeiten und die Ergebnisse meist passen. Die Spannung an einer leitenden Diode hängt aber vom Strom ab, um 59,5 mV je Dekade, und von der Fläche: Eine zehnmal größere Diode hat ein zehnmal größeres $I_S$ und braucht für denselben Strom 59,5 mV weniger. Dazu kommt die Temperatur (nächster Abschnitt). Die Beispieldiode liegt bei 1 µA bei 0,467 V und bei 100 mA im idealen Modell bei 0,764 V.
:::

:::frage
„Warum liegt die Durchlassspannung unter der Diffusionsspannung von 0,714 V?“
Damit Strom fließt, muss die Barriere nicht verschwinden. Bei 0,645 V bleiben von ihr noch 69 mV übrig, das 2,7-Fache von $U_T$; nach der Boltzmann-Verteilung hat dann etwa jeder fünfzehnte Majoritätsträger an der Zone genug Energie, und das genügt für 1 mA. Nähert sich die Spannung am Übergang der Diffusionsspannung, wird die Injektion stark, und das Modell der schwachen Injektion gilt nicht mehr; an den Klemmen kommt außerdem der Spannungsabfall in den neutralen Gebieten hinzu.
:::

### Einfluss des Halbleitermaterials

:::grafik
Szene: get1/halbleiterbauelemente/02-material-vergleich · Vorlage: kennlinienschar
**Abbildung 4:** Ideale Kennlinien gleich aufgebauter Dioden aus Germanium, Silizium und Galliumarsenid, linear bis 10 mA. Bei 1 mA liegen sie bei 0,25 V, 0,65 V und 1,08 V. Je größer die Bandlücke, desto höher die Durchlassspannung.
:::

Germaniumdioden leiten schon bei 0,2 bis 0,3 V, Dioden aus Galliumarsenid erst ab etwa 1 V. Den Unterschied macht der Sättigungssperrstrom.
Er ist der Strom der Minoritätsträger, die aus der Umgebung der Zone an deren Rand gelangen, und deren Dichte ist nach dem Massenwirkungsgesetz das Quadrat der Eigenleitungsdichte geteilt durch die Dotierung. Bei sonst gleichem Aufbau gilt deshalb

$$I_S \propto n_i^2$$

Idee der Herleitung: Der Strom hinunter zählt Minoritätsträger, und ihre Dichte ist proportional zu $n_i^2$.

:::herleitung
**Ausgangspunkt:** Im Gleichgewicht ist $I_S$ der Strom hinunter, gebildet von den Minoritätsträgern, die den Rand der Zone erreichen (Artikel [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html)).

**Annahmen:** (i) gleiche Geometrie, Dotierungen, Beweglichkeiten und Lebensdauern; (ii) das Massenwirkungsgesetz gilt in beiden neutralen Gebieten.

**Schritt 1**: Nach dem Massenwirkungsgesetz sind die Minoritätsträgerdichten

$$p_{n0} = \frac{n_i^2}{N_D}, \qquad n_{p0} = \frac{n_i^2}{N_A}$$

**Schritt 2**: Nach (i) erreicht pro Sekunde in beiden Materialien derselbe Bruchteil dieser Minoritätsträger den Rand der Zone. Der Strom ist deshalb proportional zu ihrer Dichte:

$$I_S \propto \frac{n_i^2}{N_D} + \frac{n_i^2}{N_A} \propto n_i^2$$

**Ergebnis:**

$$I_S \propto n_i^2$$

**Woher die Faktoren kommen:** Das Quadrat stammt aus dem Massenwirkungsgesetz; die Dotierung steht im Nenner, weil viele Majoritätsträger die Minoritätsträger selten machen.

**Proben:** Germanium hat bei 300 K 2·10¹³ statt 10¹⁰ freie Ladungsträger pro cm³, also ein um den Faktor (2·10³)² = 4·10⁶ größeres $I_S$. Nach Formel 2 sinkt die Spannung für jeden Strom um 25,85 mV mal $\ln(4\cdot10^6)$, also um 0,39 V.

**Grenzen:** Beweglichkeiten, Lebensdauern und Zustandsdichten unterscheiden sich zwischen den Materialien. Die Rechnung erfasst nur den beherrschenden Faktor, der Unterschiede um Zehnerpotenzen erzeugt.
:::

Germanium hat 2000-mal mehr freie Ladungsträger als Silizium und deshalb ein 4·10⁶-mal größeres $I_S$; dieselbe Diode aus Germanium braucht für 1 mA nur 0,25 V, eine aus Galliumarsenid 1,08 V (Abbildung 4).
Weil $n_i^2$ exponentiell mit der Bandlücke fällt, steigt die Durchlassspannung mit ihr; wie groß die Schritte genau sind, hängt zusätzlich von den Zustandsdichten der Materialien ab.

## Temperaturabhängigkeit

*Warum sinkt die Durchlassspannung, wenn die Diode warm wird, obwohl $U_T$ im Exponenten wächst?*

:::grafik
Szene: get1/halbleiterbauelemente/02-temperatur · Vorlage: kennlinienschar
**Abbildung 5:** Ideale Kennlinien der Beispieldiode bei 0, 25, 50 und 75 °C, linear bis 2 mA. Bei 1 mA liegen sie bei 0,702 V, 0,649 V, 0,596 V und 0,542 V. Mit steigender Temperatur wandert die Kennlinie nach links, um rund 2 mV je Kelvin.
:::

**Die Akteure:**

- __$T$__: absolute Temperatur; in K; 300 K im Beispielsystem.
- __$W_{g0}$__: Bandlücke von Silizium, von 300 K linear auf 0 K extrapoliert; 1,206 eV. Die Bandlücke schrumpft beim Erwärmen leicht; für den Temperaturgang zählt deshalb dieser extrapolierte Wert, wie schon beim Temperaturgang von $n_i$.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Die Temperatur wirkt an zwei Stellen der Shockley-Gleichung. $U_T$ im Exponenten wächst proportional zur Temperatur; dieselbe Absenkung der Barriere zählt dann weniger Vielfache von $U_T$. Für sich allein würde das den Strom bei fester Spannung senken, bei 0,645 V um 8,3 % je Kelvin.

**Schritt 2**: $I_S$ ist proportional zu $n_i^2$, und $n_i$ wächst bei 300 K um 8,3 % je Kelvin ([Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html)). $I_S$ wächst deshalb um 16,6 % je Kelvin und verdoppelt sich alle 4,2 K.

**Schritt 3**: Der zweite Effekt ist doppelt so stark wie der erste. Bei fester Spannung steigt der Strom deshalb netto um 8,2 % je Kelvin; bei festem Strom sinkt die Spannung, bei 1 mA um 2,13 mV je Kelvin (Abbildung 5).

:::formel Formel
$$\frac{\mathrm{d}U}{\mathrm{d}T}\bigg|_{I} = \frac{U - 3\,U_T - W_{g0}/e}{T}$$
:::

**So liest man das:** Eingabe sind die Spannung beim betrachteten Strom und die Temperatur, Ausgabe die Änderung der Spannung je Kelvin bei festem Strom. Weil $W_{g0}/e$ mit 1,206 V größer ist als jede Durchlassspannung, ist das Ergebnis negativ.
Bei 1 mA (0,645 V) sind es −2,13 mV/K, bei 0,6 V −2,28 mV/K und bei 0,7 V −1,95 mV/K: Je größer der Strom, desto kleiner der Betrag.

Idee der Herleitung: Man leitet Formel 2 bei festem Strom nach der Temperatur ab und setzt für $I_S$ den Temperaturgang von $n_i^2$ ein.

:::herleitung
**Ausgangspunkt:** Formel 2 für Ströme weit über $I_S$,

$$U = \frac{k_B\,T}{e}\,\big(\ln I - \ln I_S\big)$$

zusammen mit $I_S \propto n_i^2$ (Abschnitt *Einfluss des Halbleitermaterials*) und dem Temperaturgang der Eigenleitungsdichte aus dem Artikel [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html):

$$n_i^2 \propto T^3\,\exp\!\Big(-\frac{W_{g0}}{k_B\,T}\Big)$$

**Annahmen:** (i) Die schwache Temperaturabhängigkeit von Beweglichkeiten und Lebensdauern ist vernachlässigt. (ii) Die Bandlücke nimmt um 300 K linear mit der Temperatur ab; ihr linearer Anteil steckt im Vorfaktor, deshalb steht im Exponenten $W_{g0}$.

**Schritt 1**: Logarithmische Ableitung von $I_S$ nach der Temperatur:

$$\frac{\mathrm{d}\ln I_S}{\mathrm{d}T} = \frac{3}{T} + \frac{W_{g0}}{k_B\,T^2}$$

Bei 300 K sind das 1,0 % plus 15,6 %, zusammen 16,6 % je Kelvin.

**Schritt 2** (entscheidender Schritt): $U$ bei festem Strom ableiten; $\ln I$ ist dann konstant, und nach der Produktregel entstehen zwei Summanden:

$$\frac{\mathrm{d}U}{\mathrm{d}T} = \frac{k_B}{e}\,\big(\ln I - \ln I_S\big) - \frac{k_B\,T}{e}\,\frac{\mathrm{d}\ln I_S}{\mathrm{d}T}$$

**Schritt 3**: Der erste Summand ist $U/T$. In den zweiten Schritt 1 einsetzen:

$$\frac{\mathrm{d}U}{\mathrm{d}T} = \frac{U}{T} - \frac{k_B\,T}{e}\,\Big(\frac{3}{T} + \frac{W_{g0}}{k_B\,T^2}\Big) = \frac{U - 3\,U_T - W_{g0}/e}{T}$$

**Ergebnis:**

$$\frac{\mathrm{d}U}{\mathrm{d}T}\bigg|_{I} = \frac{U - 3\,U_T - W_{g0}/e}{T}$$

**Woher die Faktoren kommen:** $U/T$ stammt aus $U_T$ im Exponenten, $3\,U_T$ aus dem Vorfaktor $T^3$ von $n_i^2$, und $W_{g0}/e$ aus dem Boltzmann-Faktor der Bandlücke; dieser Anteil überwiegt.

**Proben:** Einheit V/K. Zahlenwert bei 1 mA: (0,645 − 0,078 − 1,206) V geteilt durch 300 K ergibt −2,13 mV/K. Die genau berechneten Kennlinien von Abbildung 5 fallen von 25 auf 75 °C von 0,649 auf 0,542 V, im Mittel um 2,15 mV/K.

**Grenzen:** Die Formel gilt, solange die ideale Kennlinie gilt; bei großen Strömen kommen Bahnwiderstand und starke Injektion mit eigenen Temperaturgängen hinzu.
:::

::::beispiel Temperaturgang bei 1 mA und die Diode als Thermometer
**Gegeben:** Beispieldiode bei 1 mA, Durchlassspannung 0,645 V bei 300 K; Temperaturspannung 25,85 mV; extrapolierte Bandlücke 1,206 eV.

**Gesucht:** (a) die Änderung der Durchlassspannung je Kelvin; (b) die Spannung bei 75 °C; (c) die Temperaturauflösung eines Thermometers, das diese Spannung auf 1 mV genau misst.

**Rechnung:** (a) Mit Formel 3:

$$\frac{\mathrm{d}U}{\mathrm{d}T} = \frac{0{,}645\ \mathrm{V} - 0{,}078\ \mathrm{V} - 1{,}206\ \mathrm{V}}{300\ \mathrm{K}} = -2{,}13\ \mathrm{mV/K}$$

(b) Von 300 K (26,85 °C) bis 75 °C sind es 48,2 K:

$$U(75\ ^\circ\mathrm{C}) \approx 0{,}645\ \mathrm{V} - 48{,}2\ \mathrm{K}\cdot2{,}13\ \mathrm{mV/K} = 0{,}542\ \mathrm{V}$$

(c) Ein Millivolt entspricht

$$\Delta T = \frac{1\ \mathrm{mV}}{2{,}13\ \mathrm{mV/K}} = 0{,}47\ \mathrm{K}$$

**Ergebnis:** **−2,13 mV/K; 0,542 V bei 75 °C; Auflösung rund 0,5 K.**

**Einordnung:** 50 K Erwärmung kosten 0,1 V, das ist ein Sechstel der Durchlassspannung. Schaltungen, die eine Diodenstrecke als Spannungsreferenz nutzen, driften entsprechend. Umgekehrt dient eine Diode mit konstantem Strom als preiswerter und genauer Temperatursensor, und viele integrierte Temperatursensoren werten genau solche Diodenspannungen aus.
::::

## Die Raumladungszone unter Spannung

*Wie breit wird die Zone, und wie stark ist das Feld in ihr, wenn eine Spannung anliegt?*

:::grafik
Szene: get1/halbleiterbauelemente/02-zone-unter-spannung · Vorlage: raumladung-felddreieck
**Abbildung 6:** Raumladung und Feldstärke der Beispieldiode in der Näherung mit scharf begrenzter Zone, links das p-, rechts das n-Gebiet. (a) Ohne Spannung ist die Zone 0,43 µm breit, das Höchstfeld beträgt 3,3·10⁴ V/cm. (b) Bei −5 V sind es 1,22 µm und 9,4·10⁴ V/cm. Die Fläche unter dem Felddreieck ist die Spannung über der Zone, 0,714 V bzw. 5,714 V.
:::

**Die Akteure:**

- __$N_A$__, __$N_D$__: Dichte der Akzeptoren im p-Gebiet bzw. der Donatoren im n-Gebiet; in cm⁻³; je 10¹⁶ in der Beispieldiode.
- __$\varepsilon$__: Permittivität von Silizium, das 11,7-Fache der elektrischen Feldkonstante; 1,036·10⁻¹² F/cm.
- __$w$__: Weite der Raumladungszone; 0,43 µm ohne Spannung.
- __$E_\mathrm{max}$__: Betrag des Feldes an der Grenzfläche zwischen p- und n-Gebiet, wo es am stärksten ist; in V/cm.

**Das Zusammenspiel:** Legt man eine Sperrspannung an, zieht die Quelle für einen Augenblick Majoritätsträger von der Grenze ab: Elektronen aus dem n-Gebiet zum Pluspol, Löcher aus dem p-Gebiet zum Minuspol. Dadurch liegen weitere Rümpfe frei, die Zone wird breiter, und die Spannung über ihr wächst, bis sie die Diffusionsspannung plus die Sperrspannung trägt.

In der Zone gibt es dann praktisch keine beweglichen Ladungsträger, nur die feste Ladung der Rümpfe: positiv auf der n-Seite, negativ auf der p-Seite (Abbildung 6). Durch jede dieser Schichten wächst das Feld linear an, und zwar umso steiler, je höher die Dotierung ist; an der Grenzfläche ist es am stärksten. Die Spannung über der Zone ist die Fläche unter diesem Felddreieck.

:::formel Formel
$$w = \sqrt{\frac{2\varepsilon\,(U_\mathrm{Diff} - U)}{e}\cdot\frac{N_A + N_D}{N_A\,N_D}}$$

$$E_\mathrm{max} = \frac{2\,(U_\mathrm{Diff} - U)}{w}$$
:::

**So liest man das:** Eingabe ist die Spannung an der Diode, Ausgabe die Weite der Zone und ihr Höchstfeld. Beide wachsen mit der Wurzel der Spannung über der Zone: Bei −5 V trägt sie mit 5,714 V das Achtfache und wird 2,83-mal so breit.
Unterscheiden sich die Dotierungen stark, ist der Bruch mit den Dichten ungefähr der Kehrwert der kleineren; die schwächer dotierte Seite bestimmt dann die Weite. Hoch dotierte Übergänge sind dünn und haben schon bei kleinen Spannungen starke Felder.

Idee der Herleitung: Die Zone ist insgesamt neutral, das Feld wächst linear durch die geladenen Schichten, und die Spannung ist die Fläche des Felddreiecks.

:::herleitung
**Ausgangspunkt:** das Gaußsche Gesetz aus dem Artikel [Kondensator und Kapazität](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/kondensator-und-kapazitaet.html). Angewandt auf eine flache Schachtel, deren Deckflächen parallel zum Übergang liegen und den Abstand $\mathrm{d}x$ haben, ergibt es: Über eine Schicht mit der Ladungsdichte $\rho$ ändert sich das Feld um

$$\mathrm{d}E = \frac{\rho}{\varepsilon}\,\mathrm{d}x$$

**Annahmen:**
(i) Verarmungsnäherung: In der Zone gibt es keine beweglichen Ladungsträger. Die Ladungsdichte ist $+e N_D$ auf der n-Seite (Breite $x_n$) und $-e N_A$ auf der p-Seite (Breite $x_p$); außerhalb ist das Material neutral und feldfrei.
(ii) Über der Zone liegt die Spannung $U_\mathrm{Diff} - U$.
(iii) Der Übergang ist eben und groß gegen die Weite der Zone.

**Schritt 1**: Insgesamt ist die Zone neutral, die Ladungen beider Seiten sind gleich groß:

$$N_D\,x_n = N_A\,x_p, \qquad x_n + x_p = w$$

**Schritt 2**: Vom feldfreien Rand der n-Seite bis zur Grenzfläche wächst das Feld nach dem Ausgangspunkt linear auf

$$E_\mathrm{max} = \frac{e\,N_D\,x_n}{\varepsilon}$$

und fällt auf der p-Seite ebenso linear wieder auf null.

**Schritt 3** (entscheidender Schritt): Die Spannung ist das Integral des Feldes über die Zone, also die Fläche des Dreiecks:

$$U_\mathrm{Diff} - U = \frac{1}{2}\,E_\mathrm{max}\,w$$

Das ist die zweite Formel.

**Schritt 4**: Aus Schritt 1 folgt

$$x_n = \frac{N_A}{N_A + N_D}\,w$$

und damit aus Schritt 2

$$E_\mathrm{max} = \frac{e}{\varepsilon}\cdot\frac{N_A\,N_D}{N_A + N_D}\cdot w$$

**Schritt 5**: In Schritt 3 eingesetzt:

$$U_\mathrm{Diff} - U = \frac{e}{2\,\varepsilon}\cdot\frac{N_A\,N_D}{N_A + N_D}\cdot w^2$$

Nach $w$ aufgelöst, ergibt das die erste Formel.

**Ergebnis:**

$$w = \sqrt{\frac{2\varepsilon\,(U_\mathrm{Diff} - U)}{e}\cdot\frac{N_A + N_D}{N_A\,N_D}}$$

$$E_\mathrm{max} = \frac{2\,(U_\mathrm{Diff} - U)}{w}$$

**Woher die Faktoren kommen:** Die 2 stammt aus der Dreiecksfläche, der Bruch der Dichten aus der Neutralität, $\varepsilon$ aus dem Gaußschen Gesetz: Ein Material mit größerer Permittivität schwächt das Feld der Rümpfe, und die Zone muss breiter werden, um dieselbe Spannung zu tragen.

**Proben:** Einheit: F/cm mal V geteilt durch C mal cm³ ergibt cm², unter der Wurzel also cm. Ohne Spannung ergibt die Formel 0,430 µm und 3,3·10⁴ V/cm. Die genaue numerische Lösung im Artikel [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html) liefert 3,2·10⁴ V/cm, weil die Ränder der Zone dort über einige 10 nm verschmiert sind.

**Grenzen:** Nähert sich die Spannung der Diffusionsspannung, wird die Zone sehr dünn; dann sind die beweglichen Ladungsträger nicht mehr vernachlässigbar, und die Näherung versagt.
:::

::::beispiel Weite und Höchstfeld der Beispieldiode in Sperrrichtung
**Gegeben:** Dotierungen je 10¹⁶ cm⁻³, also ein Bruch der Dichten von 2·10⁻¹⁶ cm³; Permittivität 1,036·10⁻¹² F/cm; Diffusionsspannung 0,714 V.

**Gesucht:** Weite und Höchstfeld bei −5 V und bei −50 V.

**Rechnung:** Bei −5 V liegen 5,714 V über der Zone:

$$w = \sqrt{\frac{2\cdot1{,}036\cdot10^{-12}\ \mathrm{F/cm}\cdot5{,}714\ \mathrm{V}}{1{,}602\cdot10^{-19}\ \mathrm{C}}\cdot2\cdot10^{-16}\ \mathrm{cm^3}} = 1{,}22\cdot10^{-4}\ \mathrm{cm}$$

$$E_\mathrm{max} = \frac{2\cdot5{,}714\ \mathrm{V}}{1{,}216\cdot10^{-4}\ \mathrm{cm}} = 9{,}4\cdot10^{4}\ \mathrm{V/cm}$$

Bei −50 V sind es 50,714 V:

$$w = 3{,}62\cdot10^{-4}\ \mathrm{cm}, \qquad E_\mathrm{max} = \frac{2\cdot50{,}714\ \mathrm{V}}{3{,}622\cdot10^{-4}\ \mathrm{cm}} = 2{,}8\cdot10^{5}\ \mathrm{V/cm}$$

**Ergebnis:** **1,22 µm und 9,4·10⁴ V/cm bei −5 V; 3,62 µm und 2,8·10⁵ V/cm bei −50 V.**

**Einordnung:** Die zehnfache Spannung ergibt nur ein dreimal so starkes Feld. Stark ist es trotzdem: Luft schlägt bei etwa 3·10⁴ V/cm durch, und diesen Wert erreicht die Zone schon ohne äußere Spannung.
::::

## Die reale Kennlinie

*Wo weicht eine reale Diode vom idealen Modell ab, und warum?*

:::grafik
Szene: get1/halbleiterbauelemente/02-kennlinie-real · Vorlage: kennlinie-semilog-anteile
**Abbildung 7:** Kennlinie der Beispieldiode halblogarithmisch: ideal (gestrichelt), Diffusionsanteil, Rekombinationsanteil und die reale Kennlinie mit starker Injektion und Bahnwiderstand. Unterhalb von 0,27 V, also unter etwa 1 nA, überwiegt die Rekombination in der Zone; zwischen etwa 0,1 µA und 1 mA folgt die reale Kennlinie der idealen; darüber biegt sie ab und braucht bei 10 mA 0,90 V statt 0,70 V.
:::

**Die Akteure:**

- __$\tau$__: __Lebensdauer__, die mittlere Zeit, bis ein Ladungsträger rekombiniert; 1 µs in der Beispieldiode.
- __$U_\mathrm{pn}$__: Spannung am Übergang selbst, ohne den Anteil, der in den neutralen Gebieten abfällt; in V.
- __$R_B$__: __Bahnwiderstand__, der ohmsche Widerstand der neutralen Gebiete und Kontakte; in Ω.
- __$m$__: __Emissionskoeffizient__, eine reine Zahl zwischen 1 und 2; in Datenblättern und Simulatoren meist n bzw. N genannt.

**Das Zusammenspiel:** Von den fünf Annahmen der Shockley-Gleichung versagen bei realen Dioden drei, jede in einem anderen Strombereich (Abbildung 7).

**Kleine Ströme: Rekombination in der Zone.** Das ideale Modell lässt die Ladungsträger die Zone durchqueren, ohne dass sie dort rekombinieren. Im Kristall gibt es aber __Störstellen__, Fremdatome und Gitterfehler mit Energieniveaus mitten in der Bandlücke, an denen sich ein Elektron und ein Loch treffen und verschwinden. Mit Durchlassspannung sind in der Zone beide Sorten zugleich vorhanden, in ihrer Mitte gleich viele, und dort rekombinieren sie am häufigsten.
Weil dort jede der beiden Dichten nur mit $\exp(U_\mathrm{pn}/(2U_T))$ wächst, nimmt dieser Strom nur um eine Dekade je 119 mV zu. Sein Vorfaktor hängt aber an $n_i$ statt an $n_i^2$ und ist deshalb vergleichsweise groß: Bei der Beispieldiode überwiegt die Rekombination unterhalb von 0,27 V, also bei Strömen unter etwa 1 nA. Dioden mit kürzerer Lebensdauer und mehr Störstellen zeigen diesen Bereich bis zu viel größeren Strömen.

**Große Ströme: starke Injektion.** Oberhalb von etwa 0,65 V erreichen die Minoritätsträger, die über die Barriere kommen, am Rand der Zone einen merklichen Teil der Dotierung: 8 % bei 0,65 V, 57 % bei 0,7 V. Dann sind dort Elektronen und Löcher ähnlich häufig. Ihr Produkt wächst mit $\exp(U_\mathrm{pn}/U_T)$ (Herleitung unten), jede einzelne Dichte und mit ihr der Strom also wieder nur mit $\exp(U_\mathrm{pn}/(2U_T))$.

**Sehr große Ströme: Bahnwiderstand.** Die neutralen Gebiete leiten wie ein ohmscher Widerstand. Am Übergang liegt deshalb nur die Klemmenspannung abzüglich des Spannungsabfalls $R_B I$.
Die Beispieldiode mit je 100 µm schwach dotierter Bahn hat 18,9 Ω; bei 10 mA fallen daran 0,19 V ab, und die Kennlinie biegt in der halblogarithmischen Darstellung ab. Reale Dioden haben deshalb hoch dotierte Bahngebiete und kurze Wege; ihr Bahnwiderstand liegt meist unter einigen Ohm.

**Sperrbereich: Generation in der Zone.** Rückwärts wirkt derselbe Mechanismus. Im Inneren der gesperrten Zone gibt es praktisch keine beweglichen Ladungsträger und deshalb keine Rekombination; die Störstellen erzeugen dort ungestört Paare, die das Feld sofort trennt. Nur an den beiden Rändern, wo noch Majoritätsträger vorhanden sind, ist die Erzeugung gebremst.
Bei −1 V liefert das 20 pA, 1400-mal mehr als $I_S$. Weil die Zone mit der Sperrspannung breiter wird, wächst dieser Strom langsam mit, auf 64 pA bei −5 V. Dazu kommen Leckströme an der Oberfläche des Kristalls; Datenblätter kleiner Siliziumdioden nennen deshalb Sperrströme bis in den Nanoamperebereich, die 1N4148 höchstens 25 nA bei 20 V.
Weil der Generationsstrom an $n_i$ hängt, wächst er um 8,3 % je Kelvin und verdoppelt sich etwa alle 8 bis 10 K.

Rekombination in Durchlass- und Generation in Sperrrichtung beschreibt eine gemeinsame Formel:

:::formel Formel
$$I_\mathrm{RG} = \frac{e\,n_i\,A\,w_\mathrm{eff}}{2\,\tau}\,\Big[\exp\!\Big(\frac{U_\mathrm{pn}}{2\,U_T}\Big) - 1\Big]$$

$$w_\mathrm{eff} = w - 2\,d\ \ (\text{Sperrrichtung}), \qquad w_\mathrm{eff} = \frac{\pi\,U_T}{E_\mathrm{max}}\ \ (\text{Durchlassrichtung})$$
:::

**So liest man das:** Eingabe ist die Spannung am Übergang, Ausgabe der zusätzliche Strom durch Paare, die in der Zone verschwinden (positiv) oder entstehen (negativ). $A$ ist die Fläche des Übergangs, $w_\mathrm{eff}$ der Teil der Zone, in dem die Störstellen mit der größten Rate arbeiten.
In Sperrrichtung ist das die Zone nach Formel 4 ohne zwei Randschichten der Breite $d$, in denen noch Majoritätsträger vorhanden sind; bei der Beispieldiode ist $d$ = 0,215 µm, bei −1 V bleiben 0,236 µm von 0,666 µm, und die Klammer ist −1. In Durchlassrichtung ist es nur die dünne Schicht um die Mitte, in der Elektronen und Löcher gleich häufig sind, bei 0,3 V 0,032 µm.

Idee der Herleitung: Man berechnet die Netto-Rate der Rekombination über Störstellen in der Mitte der Zone, wo sie am größten ist, und nimmt sie für die ganze Zone.

:::herleitung
**Ausgangspunkt:** die Netto-Rekombinationsrate über Störstellen in der Mitte der Bandlücke nach Shockley, Read und Hall, für gleiche Lebensdauern von Elektronen und Löchern:

$$R = \frac{n\,p - n_i^2}{\tau\,(n + p + 2\,n_i)}$$

Positives $R$ bedeutet, dass mehr Paare verschwinden als entstehen. Die Idee dahinter: Eine Störstelle fängt erst ein Elektron und dann ein Loch ein, oder sie gibt beide ab; im Gleichgewicht, wenn das Produkt der Dichten gleich $n_i^2$ ist, heben sich Einfang und Abgabe auf. Die vollständige Herleitung geht über ET1 hinaus.

**Annahmen:**
(i) Störstellen in der Mitte der Bandlücke, gleiche Lebensdauer $\tau$ für beide Sorten;
(ii) Elektronen und Löcher sind in der Zone jeweils Boltzmann-verteilt bezogen auf das Gebiet, aus dem sie kommen;
(iii) Potenzial und Weite der Zone folgen aus der Verarmungsnäherung (Formel 4).

**Schritt 1**: Nach (ii) ist die Elektronendichte an jedem Ort der Zone um den Boltzmann-Faktor ihrer Höhe über dem n-Gebiet kleiner als $N_D$, die Löcherdichte um den Faktor ihrer Höhe gegenüber dem p-Gebiet kleiner als $N_A$. Beide Höhen ergeben zusammen die ganze Barriere, deshalb fällt im Produkt der Ort heraus. Mit der Diffusionsspannung aus dem Artikel [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html):

$$n\,p = N_D\,N_A\,\exp\!\Big(-\frac{U_\mathrm{Diff} - U_\mathrm{pn}}{U_T}\Big) = n_i^2\,\exp\!\Big(\frac{U_\mathrm{pn}}{U_T}\Big)$$

**Schritt 2** (entscheidender Schritt): Bei festem Produkt ist die Summe $n + p$ im Nenner am kleinsten, wo beide Dichten gleich sind; dort ist die Rate am größten, mit

$$n = p = n_i\,\exp\!\Big(\frac{U_\mathrm{pn}}{2\,U_T}\Big)$$

**Schritt 3**: Eingesetzt, mit der Abkürzung $x$ für $\exp(U_\mathrm{pn}/(2U_T))$:

$$R_\mathrm{max} = \frac{n_i^2\,(x^2 - 1)}{\tau\,(2\,n_i\,x + 2\,n_i)}$$

$$= \frac{n_i}{2\,\tau}\cdot\frac{(x - 1)(x + 1)}{x + 1} = \frac{n_i}{2\,\tau}\,(x - 1)$$

**Schritt 4**: In Sperrrichtung ist das Produkt der Dichten viel kleiner als $n_i^2$. Im Inneren der Zone sind beide Dichten kleiner als $n_i$, und dort gilt $R = -n_i/(2\tau)$: Die Störstellen erzeugen Paare mit der größten Rate. An den Rändern liegt die Dichte der Majoritätsträger aber noch über $n_i$, und die Rate ist auf den Betrag $n_i^2/(\tau\,n)$ gebremst. Unter $n_i$ fällt die Majoritätsdichte erst, wenn das Potenzial gegenüber dem neutralen Gebiet um $U_T \ln(N/n_i)$ gefallen ist, bei der Beispieldiode um 0,357 V. In der Verarmungsnäherung fällt das Potenzial vom Rand aus mit dem Quadrat des Abstands; dafür braucht es die Strecke

$$d = \sqrt{\frac{2\,\varepsilon\,U_T\,\ln(N/n_i)}{e\,N}}$$

mit der Dotierung $N$ der jeweiligen Seite, bei der Beispieldiode 0,215 µm. Mit der größten Rate arbeitet also nur die Weite

$$w_\mathrm{eff} = w - 2\,d$$

**Schritt 5**: In Durchlassrichtung ist die Rate nur dort groß, wo beide Dichten ähnlich sind. Misst man das Potenzial $\psi$ von der Stelle aus, an der sie gleich sind, ist die Elektronendichte um den Faktor $\exp(\psi/U_T)$ größer und die Löcherdichte um denselben Faktor kleiner als dort. Für Spannungen weit über $U_T$ wird die Rate damit

$$R \approx \frac{n_i}{2\,\tau}\,\exp\!\Big(\frac{U_\mathrm{pn}}{2\,U_T}\Big)\cdot\frac{1}{\cosh(\psi/U_T)}$$

Nahe der Mitte ist das Feld fast gleich $E_\mathrm{max}$, das Potenzial ändert sich also um $E_\mathrm{max}$ je Längeneinheit. Das Integral über den Ort ist

$$\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{\cosh(E_\mathrm{max}\,x/U_T)} = \frac{\pi\,U_T}{E_\mathrm{max}}$$

Die Zone wirkt also wie eine Schicht dieser Dicke mit der größten Rate:

$$w_\mathrm{eff} = \frac{\pi\,U_T}{E_\mathrm{max}}$$

**Schritt 6**: Für jedes Paar, das in der Zone verschwindet, kommt ein Elektron aus dem n- und ein Loch aus dem p-Gebiet; der äußere Kreis transportiert dafür eine Elementarladung. Der Strom ist deshalb $e$ mal größte Rate mal effektives Volumen $A\,w_\mathrm{eff}$:

$$I_\mathrm{RG} = e\,A\,w_\mathrm{eff}\cdot\frac{n_i}{2\,\tau}\,\Big[\exp\!\Big(\frac{U_\mathrm{pn}}{2\,U_T}\Big) - 1\Big]$$

**Ergebnis:**

$$I_\mathrm{RG} = \frac{e\,n_i\,A\,w_\mathrm{eff}}{2\,\tau}\,\Big[\exp\!\Big(\frac{U_\mathrm{pn}}{2\,U_T}\Big) - 1\Big]$$

**Woher die Faktoren kommen:** $n_i/(2\tau)$ ist die größte Netto-Rate der Störstellen, $A\,w_\mathrm{eff}$ das Volumen, in dem sie erreicht wird; die 2 im Exponenten entsteht, weil in der Mitte jede Dichte nur mit der Wurzel des Produkts wächst, und das $\pi$ aus dem Integral über $1/\cosh$.

**Proben:** Einheit: C mal cm⁻³ mal cm² mal cm geteilt durch s ergibt A. Ohne Spannung ist der Strom null. Bei −1 V ist $w_\mathrm{eff}$ = 0,666 µm − 0,430 µm = 0,236 µm; 1,602·10⁻¹² C/cm mal 2,36·10⁻⁵ cm geteilt durch 2 µs ergibt 18,9 pA. Die Rate genau über die Zone integriert ergibt 19,9 pA, bei 0,3 V 0,93 nA statt geschätzter 0,85 nA.

**Grenzen:** Die Schätzung in Durchlassrichtung setzt voraus, dass die Schicht dünn ist gegen die Zone; nahe der Diffusionsspannung gilt die Verarmungsnäherung nicht mehr. Leckströme an der Oberfläche enthält die Formel nicht.
:::

Diffusion und Rekombination laufen nebeneinander, ihre Ströme addieren sich. Eine Summe zweier Exponentialfunktionen ist in der halblogarithmischen Darstellung keine Gerade mehr. Man beschreibt die reale Kennlinie deshalb über ihre örtliche Steigung, den Emissionskoeffizienten:

$$m = \frac{1}{U_T}\cdot\frac{\mathrm{d}U_\mathrm{pn}}{\mathrm{d}\ln I}$$

Man definiert ihn so, weil er unmittelbar angibt, das Wievielfache von $U_T$ ein Faktor 2,72 im Strom kostet. Diffusion allein ergibt m = 1, Rekombination in der Zone und starke Injektion ergeben m = 2. Die Beispieldiode hat m = 1,3 bei 1 nA, 1,04 bei 0,1 µA, 1,01 bei 0,1 mA und wieder 1,3 bei 10 mA, dort wegen der starken Injektion.
Datenblätter und Schaltungssimulatoren nähern die reale Kennlinie mit einem einzigen Emissionskoeffizienten und dem Bahnwiderstand an:

$$I = I_S\,\Big[\exp\!\Big(\frac{U - R_B\,I}{m\,U_T}\Big) - 1\Big]$$

$I_S$ und $m$ sind darin angepasste Werte: Bei m über 1 liegt dieses $I_S$ um Größenordnungen über dem physikalischen Sättigungssperrstrom, im Simulatormodell der 1N4148 bei einigen Nanoampere. In LTspice heißen m und $R_B$ N und Rs. Wie man mit einer solchen Kennlinie in Schaltungen rechnet, zeigt der Artikel [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html).

::::beispiel Rekombination, Generation und Bahnwiderstand der Beispieldiode
**Gegeben:** Sättigungssperrstrom 1,457·10⁻¹⁴ A; Fläche 10⁻³ cm²; Lebensdauer 1 µs; Höchstfeld 2,53·10⁴ V/cm bei 0,3 V und effektive Weite 0,236 µm bei −1 V (Formel 5); Bahnen von je 100 µm mit den Leitfähigkeiten 2,00 S/cm (n-Gebiet) und 0,72 S/cm (p-Gebiet).

**Gesucht:** (a) Rekombinations- und Diffusionsstrom bei 0,3 V; (b) der Sperrstrom bei −1 V; (c) Bahnwiderstand und Klemmenspannung bei 10 mA.

**Rechnung:** (a) Das Produkt aus Elementarladung, Eigenleitungsdichte und Fläche:

$$e\,n_i\,A = 1{,}602\cdot10^{-19}\ \mathrm{C}\cdot10^{10}\ \mathrm{cm^{-3}}\cdot10^{-3}\ \mathrm{cm^2}$$

$$= 1{,}602\cdot10^{-12}\ \mathrm{C/cm}$$

Effektive Weite in Durchlassrichtung:

$$w_\mathrm{eff} = \frac{\pi\cdot25{,}85\ \mathrm{mV}}{2{,}53\cdot10^{4}\ \mathrm{V/cm}} = 3{,}21\cdot10^{-6}\ \mathrm{cm}$$

Vorfaktor und Ströme:

$$\frac{e\,n_i\,A\,w_\mathrm{eff}}{2\,\tau} = \frac{1{,}602\cdot10^{-12}\ \mathrm{C/cm}\cdot3{,}21\cdot10^{-6}\ \mathrm{cm}}{2\cdot10^{-6}\ \mathrm{s}} = 2{,}57\cdot10^{-12}\ \mathrm{A}$$

$$I_\mathrm{RG} = 2{,}57\cdot10^{-12}\ \mathrm{A}\cdot\big[\exp(5{,}80) - 1\big] = 0{,}85\ \mathrm{nA}, \qquad I_\mathrm{Diff} = 1{,}457\cdot10^{-14}\ \mathrm{A}\cdot\big[\exp(11{,}60) - 1\big] = 1{,}6\ \mathrm{nA}$$

(b) Bei −1 V ist die Klammer −1:

$$I_\mathrm{RG} = -\frac{1{,}602\cdot10^{-12}\ \mathrm{C/cm}\cdot2{,}36\cdot10^{-5}\ \mathrm{cm}}{2\cdot10^{-6}\ \mathrm{s}} = -18{,}9\ \mathrm{pA}$$

(c) Die beiden Bahnen sind ohmsche Widerstände in Reihe:

$$R_B = \frac{0{,}01\ \mathrm{cm}}{2{,}00\ \mathrm{S/cm}\cdot10^{-3}\ \mathrm{cm^2}} + \frac{0{,}01\ \mathrm{cm}}{0{,}72\ \mathrm{S/cm}\cdot10^{-3}\ \mathrm{cm^2}}$$

$$= 5{,}0\ \Omega + 13{,}9\ \Omega = 18{,}9\ \Omega$$

Bei 10 mA liegen am Übergang nach Formel 2 0,705 V, mit starker Injektion 0,713 V (Zahlenwerk); dazu kommen

$$R_B\,I = 18{,}9\ \Omega\cdot10\ \mathrm{mA} = 0{,}19\ \mathrm{V}$$

**Ergebnis:** **(a) 0,85 nA Rekombination gegen 1,6 nA Diffusion bei 0,3 V; (b) rund −19 pA statt −15 fA; (c) 18,9 Ω und 0,90 V bei 10 mA.**

**Einordnung:** Die genaue Integration im Zahlenwerk ergibt 0,93 nA und −19,9 pA, die Schätzung trifft also auf 10 %. Bei 0,3 V liefert die Rekombination schon halb so viel Strom wie die Diffusion, unterhalb von 0,27 V mehr. Die 0,90 V bei 10 mA stammen vor allem von den schwach dotierten, 100 µm langen Bahnen der Beispieldiode; reale Kleinsignaldioden haben Bahnwiderstände unter einem Ohm, die 1N4148 liegt bei 10 mA typisch um 0,7 V.
::::

## Der Durchbruch

*Warum steigt der Sperrstrom ab einer bestimmten Spannung plötzlich steil an?*

:::grafik
Szene: get1/halbleiterbauelemente/02-durchbruch-mechanismen · Vorlage: banddiagramm-durchbruch
**Abbildung 8:** Die beiden Durchbruchmechanismen im Banddiagramm. (a) Lawine in der Beispieldiode bei rund 100 V: Die Zone ist etwa 5 µm breit; ein Elektron gewinnt im Feld Energie, schlägt beim Stoß ein Elektron aus einer Bindung und erzeugt so ein Paar, und die neuen Ladungsträger tun dasselbe. (b) Zener-Effekt in einem Übergang mit 10¹⁸ cm⁻³: Die Zone ist nur 0,13 µm breit, die Bänder fallen steil, und ein Elektron tunnelt waagrecht vom Valenzband der p-Seite in das 11 nm entfernte Leitungsband der n-Seite.
:::

**Die Akteure:**

- __$U_\mathrm{BR}$__: __Durchbruchspannung__, der Betrag der Sperrspannung, ab der der Strom steil ansteigt; in V; rund 100 V bei der Beispieldiode.
- __$E_\mathrm{krit}$__: kritische Feldstärke der Lawine; bei Dotierungen um 10¹⁶ cm⁻³ etwa 4·10⁵ V/cm, Literaturwerte liegen zwischen 3 und 5·10⁵ V/cm.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Im Sperrbereich begrenzt der Nachschub den Strom. Die Wärme erzeugt in und neben der Zone nur einige 10 pA, und mehr Sperrspannung erhöht das nur langsam, mit der Breite der Zone.

**Schritt 2**: Das Feld in der Zone wächst nach Formel 4 mit der Wurzel der Spannung: 9,4·10⁴ V/cm bei −5 V, 2,8·10⁵ V/cm bei −50 V.

**Schritt 3**: Im Feld gewinnt ein Ladungsträger zwischen zwei Stößen mit dem Gitter Energie. Sammelt er mehr als die Bandlücke, etwa das Anderthalbfache, kann er beim Stoß ein Elektron aus einer Bindung schlagen; es entsteht ein neues Paar. Diese __Stoßionisation__ wird mit dem Feld rasch häufiger. Ab etwa 4·10⁵ V/cm erzeugt jeder Ladungsträger auf seinem Weg durch die Zone im Mittel ein weiteres Paar; die neuen Ladungsträger tun dasselbe, und aus einem Ladungsträger wird eine Lawine (Abbildung 8a). Das ist der __Lawinendurchbruch__; in der Beispieldiode setzt er bei rund 100 V ein.

**Schritt 4**: In sehr hoch dotierten Übergängen, um 10¹⁸ cm⁻³, ist die Zone nur rund 0,1 µm breit, und schon wenige Volt ergeben 10⁶ V/cm. Die Bänder fallen dann so steil, dass das Leitungsband der n-Seite auf gleicher Energie nur etwa 11 nm neben dem Valenzband der p-Seite liegt. Über diese Strecke gelangen Elektronen durch die verbotene Zone hindurch, ohne dafür Energie zu brauchen: Sie __tunneln__ (Abbildung 8b; [Der Tunneleffekt](/wissen/elektrotechnik/4-semester/grundlagen-elektronischer-materialien-und-bauelemente/quantenmechanik/tunneleffekt.html)). Das ist der __Zener-Effekt__.

**Schritt 5**: In beiden Fällen erzeugt das Feld selbst Ladungsträger, so viele, dass der äußere Kreis den Strom begrenzen muss. Bei Durchbruchspannungen unter etwa 5 V überwiegt der Zener-Effekt mit einem weichen Knick, über etwa 6 V die Lawine mit einem scharfen; dazwischen wirken beide.

**Schritt 6**: Die Temperaturgänge sind entgegengesetzt. Beim Erwärmen schwingt das Gitter stärker, die Ladungsträger stoßen öfter und gewinnen zwischen zwei Stößen weniger Energie: Die Lawine braucht ein stärkeres Feld, die Durchbruchspannung steigt. Die Bandlücke dagegen schrumpft, die Tunnelstrecke wird kürzer: Die Zener-Spannung sinkt. Um 5 bis 6 V heben sich beide Gänge nahezu auf.

:::formel Formel
$$U_\mathrm{BR} \approx \frac{\varepsilon\,E_\mathrm{krit}^2}{2\,e}\cdot\frac{N_A + N_D}{N_A\,N_D} - U_\mathrm{Diff}$$
:::

**So liest man das:** Eingabe sind die Dotierungen und die kritische Feldstärke, Ausgabe der Betrag der Sperrspannung beim Durchbruch. Halbe Dotierung ergibt bei gleicher kritischer Feldstärke die doppelte Durchbruchspannung; Dioden für hohe Sperrspannungen sind deshalb schwach dotiert und haben breite Zonen. Weil die Feldstärke quadratisch eingeht, ist das Ergebnis eine Abschätzung.

Idee der Herleitung: Man setzt in Formel 4 das Höchstfeld gleich der kritischen Feldstärke und löst nach der Spannung auf.

:::herleitung
**Ausgangspunkt:** Formel 4 für Weite und Höchstfeld der Zone.

**Annahmen:** (i) Der Durchbruch setzt ein, sobald das Höchstfeld die kritische Feldstärke erreicht; (ii) diese hängt nur von der Dotierung ab; (iii) Verarmungsnäherung.

**Schritt 1**: Die Weite aus der ersten Formel in die zweite eingesetzt und quadriert:

$$E_\mathrm{max}^2 = \frac{4\,(U_\mathrm{Diff} - U)^2}{w^2} = \frac{2\,e\,(U_\mathrm{Diff} - U)}{\varepsilon}\cdot\frac{N_A\,N_D}{N_A + N_D}$$

**Schritt 2** (entscheidender Schritt): Beim Durchbruch ist das Höchstfeld gleich $E_\mathrm{krit}$ und die Spannung gleich $-U_\mathrm{BR}$:

$$E_\mathrm{krit}^2 = \frac{2\,e\,(U_\mathrm{Diff} + U_\mathrm{BR})}{\varepsilon}\cdot\frac{N_A\,N_D}{N_A + N_D}$$

**Schritt 3**: Nach $U_\mathrm{BR}$ aufgelöst:

$$U_\mathrm{BR} = \frac{\varepsilon\,E_\mathrm{krit}^2}{2\,e}\cdot\frac{N_A + N_D}{N_A\,N_D} - U_\mathrm{Diff}$$

**Ergebnis:**

$$U_\mathrm{BR} \approx \frac{\varepsilon\,E_\mathrm{krit}^2}{2\,e}\cdot\frac{N_A + N_D}{N_A\,N_D} - U_\mathrm{Diff}$$

**Woher die Faktoren kommen:** Das Quadrat der Feldstärke entsteht, weil Feld und Weite beide mit der Wurzel der Spannung wachsen; der Bruch der Dichten sagt, dass eine schwach dotierte Seite eine breite Zone und damit eine hohe Spannung erlaubt.

**Proben:** Einheit: F/cm mal V²/cm² geteilt durch C mal cm³ ergibt V. Für die Beispieldiode mit 4·10⁵ V/cm: 103,5 V über der Zone, also 102,7 V Sperrspannung.

**Grenzen:** Die kritische Feldstärke ist nur auf etwa 10 % genau bekannt, die Durchbruchspannung deshalb auf etwa 20 %. Bei Dotierungen um 10¹⁸ cm⁻³ setzt vorher der Zener-Effekt ein; an gekrümmten Rändern des Übergangs ist das Feld stärker, und der Durchbruch beginnt dort früher.
:::

::::beispiel Durchbruchspannung der Beispieldiode und Dotierung einer 5,6-V-Z-Diode
**Gegeben:** Beispieldiode mit je 10¹⁶ cm⁻³ (Bruch der Dichten 2·10⁻¹⁶ cm³), Permittivität 1,036·10⁻¹² F/cm, kritische Feldstärke 4·10⁵ V/cm; für die Z-Diode eine Durchbruchspannung von 5,6 V und eine Tunnelfeldstärke von 10⁶ V/cm.

**Gesucht:** (a) die Durchbruchspannung der Beispieldiode; (b) die symmetrische Dotierung, bei der das Feld bei 5,6 V die Tunnelfeldstärke erreicht, die Weite der Zone und die Tunnelstrecke.

**Rechnung:** (a) Der erste Faktor von Formel 6:

$$\frac{1{,}036\cdot10^{-12}\ \mathrm{F/cm}\cdot(4\cdot10^{5}\ \mathrm{V/cm})^2}{2\cdot1{,}602\cdot10^{-19}\ \mathrm{C}} = 5{,}17\cdot10^{17}\ \mathrm{V/cm^3}$$

Mit dem Bruch der Dichten und der Diffusionsspannung:

$$U_\mathrm{BR} = 5{,}17\cdot10^{17}\ \mathrm{V/cm^3}\cdot2\cdot10^{-16}\ \mathrm{cm^3} - 0{,}714\ \mathrm{V} = 102{,}7\ \mathrm{V}$$

Mit 3,5·10⁵ bzw. 4,5·10⁵ V/cm ergeben sich 78 V bzw. 130 V.

(b) Schritt 2 der Herleitung, nach den Dichten aufgelöst. Bei Dotierungen um 10¹⁸ cm⁻³ beträgt die Diffusionsspannung 0,95 V:

$$\frac{N_A\,N_D}{N_A + N_D} = \frac{1{,}036\cdot10^{-12}\ \mathrm{F/cm}\cdot(10^{6}\ \mathrm{V/cm})^2}{2\cdot1{,}602\cdot10^{-19}\ \mathrm{C}\cdot(0{,}95\ \mathrm{V} + 5{,}6\ \mathrm{V})} = 4{,}9\cdot10^{17}\ \mathrm{cm^{-3}}$$

Bei gleichen Dotierungen ist der Bruch die halbe Dotierung; also sind es je 9,9·10¹⁷ cm⁻³. Weite nach der zweiten Formel von Formel 4:

$$w = \frac{2\cdot6{,}55\ \mathrm{V}}{10^{6}\ \mathrm{V/cm}} = 1{,}31\cdot10^{-5}\ \mathrm{cm}$$

Die Bänder fallen in der Zone um $e E$ je Längeneinheit. Die waagrechte Strecke zwischen Valenzbandkante und Leitungsbandkante gleicher Energie ist deshalb die Bandlücke geteilt durch diesen Abfall:

$$d = \frac{W_g}{e\,E} = \frac{1{,}12\ \mathrm{V}}{10^{6}\ \mathrm{V/cm}} = 1{,}12\cdot10^{-6}\ \mathrm{cm}$$

**Ergebnis:** **(a) rund 100 V (78 bis 130 V je nach kritischer Feldstärke); (b) je etwa 10¹⁸ cm⁻³, eine 131 nm breite Zone und eine Tunnelstrecke von 11 nm.**

**Einordnung:** Die 1N4148 garantiert mindestens 100 V Durchbruchspannung bei 100 µA, dieselbe Größenordnung wie die Abschätzung. Für eine Z-Diode mit wenigen Volt muss die Dotierung hundertmal höher sein; die Zone schrumpft dann so weit, dass Elektronen sie durchtunneln können.
::::

:::fehlvorstellung
„Im Durchbruch wird die Diode zerstört.“
Das liegt nahe, weil das Skript es so formuliert (S. 162) und weil gewöhnliche Dioden ohne Strombegrenzung im Durchbruch tatsächlich ausfallen. Der Durchbruch selbst ist aber umkehrbar: Sinkt die Sperrspannung, hören Stoßionisation und Tunneln sofort auf, und Z-Dioden arbeiten dauernd im Durchbruch, wie das Skript eine Seite später selbst schreibt (S. 163). Zerstörend ist die Wärme: Bei 100 V und 10 mA setzt eine kleine Diode 1 W um, doppelt so viel wie die 0,5 W, für die typische kleine Gehäuse ausgelegt sind. Bei gewöhnlichen Dioden beginnt der Durchbruch zudem oft an den Rändern des Übergangs, wo das Feld am stärksten ist; der Strom drängt sich dort zusammen und erhitzt eine kleine Stelle. Datenblätter lassen den Betrieb im Durchbruch deshalb nur bei Bauteilen zu, die dafür gebaut sind.
:::

## Die Z-Diode

*Wie hält eine Diode eine Spannung fest, obwohl der Strom durch sie schwankt?*

:::grafik
Szene: get1/halbleiterbauelemente/02-z-diode-stabilisierung · Vorlage: schaltung-und-kennlinie
**Abbildung 9:** Spannungsstabilisierung mit einer Z-Diode. (a) Schaltung: Eingangsspannung 12 V ± 1 V, Vorwiderstand 330 Ω, Z-Diode 5,6 V parallel zum Lastwiderstand 1 kΩ. (b) Durchbruchast der Z-Diode mit den Arbeitspunkten bei 11, 12 und 13 V Eingangsspannung: 10,3 mA, 13,1 mA und 15,9 mA bei 5,707 V, 5,763 V und 5,819 V. Ein Stromhub von 5,6 mA ändert die Spannung nur um 0,11 V.
:::

**Die Akteure:**

- __$U_Z$__: __Z-Spannung__, der Betrag der Spannung im Durchbruch bei einem genannten Strom; 5,6 V bei 5 mA im Beispiel.
- __$r_Z$__: __differentieller Widerstand__ der Z-Diode, die Steigung des Durchbruchasts, also Spannungsänderung geteilt durch Stromänderung; je nach Typ von einigen Ohm bis über 100 Ω, am kleinsten bei Z-Spannungen um 6 bis 8 V; im Beispiel 20 Ω. Allgemein behandelt ihn der Artikel [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html).
- __$U_E$__, __$U_A$__: schwankende Eingangsspannung und stabilisierte Ausgangsspannung.
- __$R_V$__, __$R_L$__: Vorwiderstand und Lastwiderstand, im Beispiel 330 Ω und 1 kΩ.

**Das Zusammenspiel:** Eine __Z-Diode__ ist eine Siliziumdiode, die für den Betrieb im Durchbruch gebaut ist. Ihre Dotierung legt die Z-Spannung fest, je nach Typ zwischen etwa 2 V und über 100 V, und ihr Übergang bricht gleichmäßig auf der ganzen Fläche durch. In Durchlassrichtung verhält sie sich wie eine gewöhnliche Diode.
Im Durchbruch ist ihre Kennlinie steil: Der Strom ändert sich um Milliampere, die Spannung nur um Millivolt bis wenige Zehntel Volt.

In der Stabilisierungsschaltung (Abbildung 9a) nimmt der Vorwiderstand die Differenz zwischen der schwankenden Eingangsspannung und der Z-Spannung auf. Steigt die Eingangsspannung, fließt mehr Strom durch den Vorwiderstand; fast der ganze zusätzliche Strom geht durch die Z-Diode, deren Spannung sich dabei kaum ändert. An der Last bleibt die Spannung fast konstant: Steigt die Eingangsspannung von 11 auf 13 V, wächst der Z-Strom von 10,3 auf 15,9 mA, die Ausgangsspannung aber nur von 5,707 auf 5,819 V (Abbildung 9b).

:::formel Formel
$$\frac{\Delta U_E}{\Delta U_A} = 1 + R_V\,\Big(\frac{1}{r_Z} + \frac{1}{R_L}\Big)$$
:::

**So liest man das:** Eingabe sind die drei Widerstände, Ausgabe der __Glättungsfaktor__: um wie viel kleiner eine Schwankung der Eingangsspannung am Ausgang ankommt. Ein großer Vorwiderstand und eine steile Z-Diode stabilisieren gut, im Beispiel um den Faktor 17,8.
Der Vorwiderstand darf aber nicht zu groß werden: Bei der kleinsten Eingangsspannung und der größten Last muss noch ein Strom durch die Z-Diode fließen, sonst verlässt sie den Durchbruch.

Idee der Herleitung: Man ersetzt den Durchbruchast durch eine Gerade und wendet die Knotenregel auf die Änderungen an.

:::herleitung
**Ausgangspunkt:** die Knotenregel aus dem Artikel [Kirchhoffsche Gesetze](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/kirchhoffsche-gesetze.html) am Ausgangsknoten: Der Strom durch den Vorwiderstand teilt sich in Laststrom und Z-Strom.

$$\frac{U_E - U_A}{R_V} = \frac{U_A}{R_L} + I_Z$$

**Annahmen:** (i) Die Z-Diode bleibt im Durchbruch; (ii) dort ist ihr Ast eine Gerade mit der Steigung $1/r_Z$, eine Spannungsänderung $\Delta U_A$ ändert ihren Strom also um $\Delta U_A/r_Z$; (iii) die Last ist ohmsch.

**Schritt 1**: Die Gleichung gilt vor und nach einer Änderung der Eingangsspannung. Die Differenz beider Fassungen:

$$\frac{\Delta U_E - \Delta U_A}{R_V} = \frac{\Delta U_A}{R_L} + \frac{\Delta U_A}{r_Z}$$

**Schritt 2** (entscheidender Schritt): Mit $R_V$ malnehmen und alle Terme mit $\Delta U_A$ zusammenfassen:

$$\Delta U_E = \Delta U_A\,\Big[1 + R_V\,\Big(\frac{1}{r_Z} + \frac{1}{R_L}\Big)\Big]$$

**Ergebnis:**

$$\frac{\Delta U_E}{\Delta U_A} = 1 + R_V\,\Big(\frac{1}{r_Z} + \frac{1}{R_L}\Big)$$

**Woher die Faktoren kommen:** Die Klammer ist der Leitwert der Parallelschaltung aus Z-Diode und Last; zusammen mit dem Vorwiderstand bildet sie einen Spannungsteiler für die Änderungen.

**Proben:** Ohne Z-Diode, mit unendlich großem $r_Z$, bleibt der gewöhnliche Spannungsteiler aus Vorwiderstand und Last. Eine ideale Z-Diode mit $r_Z$ gegen null hält die Spannung vollständig fest. Zahlenwert: 1 plus 330 Ω mal (0,05 + 0,001)/Ω ergibt 17,8.

**Grenzen:** Wird der Z-Strom null, gilt Annahme (i) nicht mehr, und die Schaltung wird zum bloßen Spannungsteiler.
:::

::::beispiel Stabilisierung mit einer 5,6-V-Z-Diode
**Gegeben:** Eingangsspannung 12 V ± 1 V; Vorwiderstand 330 Ω; Lastwiderstand 1 kΩ; Z-Diode mit 5,6 V bei 5 mA und 20 Ω differentiellem Widerstand, ihr Durchbruchast also als Gerade durch 5,5 V bei null Strom.

**Gesucht:** Ausgangsspannung, Z-Strom und Verlustleistung der Z-Diode bei 11, 12 und 13 V; der Glättungsfaktor; die Verlustleistung ohne Last bei 13 V.

**Rechnung:** Auf der Geraden ist der Z-Strom

$$I_Z = \frac{U_A - 5{,}5\ \mathrm{V}}{r_Z}$$

Damit wird die Knotenregel aus der Herleitung nach $U_A$ aufgelöst:

$$U_A = \frac{U_E/R_V + 5{,}5\ \mathrm{V}/r_Z}{1/R_V + 1/R_L + 1/r_Z}$$

Bei 12 V:

$$U_A = \frac{36{,}36\ \mathrm{mA} + 275\ \mathrm{mA}}{3{,}030\ \mathrm{mS} + 1\ \mathrm{mS} + 50\ \mathrm{mS}} = 5{,}763\ \mathrm{V}, \qquad I_Z = \frac{5{,}763\ \mathrm{V} - 5{,}5\ \mathrm{V}}{20\ \Omega} = 13{,}1\ \mathrm{mA}$$

Ebenso bei 11 V: 5,707 V und 10,3 mA; bei 13 V: 5,819 V und 15,9 mA. Die Verlustleistung ist Spannung mal Strom, bei 13 V also 5,819 V mal 15,9 mA, 93 mW. Glättungsfaktor nach Formel 7:

$$\frac{\Delta U_E}{\Delta U_A} = 1 + 330\ \Omega\cdot\Big(\frac{1}{20\ \Omega} + \frac{1}{1000\ \Omega}\Big) = 17{,}8$$

Ohne Last fließt bei 13 V der ganze Strom durch die Z-Diode:

$$I_Z = \frac{13\ \mathrm{V} - 5{,}5\ \mathrm{V}}{330\ \Omega + 20\ \Omega} = 21{,}4\ \mathrm{mA}, \qquad P_Z = 5{,}93\ \mathrm{V}\cdot21{,}4\ \mathrm{mA} = 127\ \mathrm{mW}$$

**Ergebnis:** **Ausgang 5,763 V ± 0,056 V bei 13,1 mA ± 2,8 mA; Glättungsfaktor 17,8; höchstens 127 mW in der Z-Diode.**

**Einordnung:** Eine Schwankung von ±8 % am Eingang kommt am Ausgang als ±1 % an. Eine Z-Diode für 0,5 W genügt auch im ungünstigsten Fall. Mehr Stabilität bringen ein größerer Vorwiderstand mit höherer Eingangsspannung, eine Z-Diode mit kleinerem differentiellem Widerstand oder ein integrierter Spannungsregler.
::::

:::frage
„Warum heißt sie Zener-Diode, wenn bei 12 V gar kein Zener-Effekt wirkt?“
Der Name stammt aus der Frühzeit: Clarence Zener beschrieb 1934 das Tunneln in starken Feldern, und als man um 1950 Dioden mit steilem Durchbruch baute, schrieb man ihn diesem Effekt zu. Messungen zeigten bald, dass oberhalb von etwa 6 V die Lawine wirkt. Der Name blieb; korrekt und in Datenblättern üblich ist der Oberbegriff Z-Diode, und Hersteller nennen die Typen über 6 V auch Lawinendioden.
:::

## Die Kapazitätsdiode

*Warum hängt die Kapazität einer gesperrten Diode von der Spannung ab?*

:::grafik
Szene: get1/halbleiterbauelemente/02-sperrschichtkapazitaet · Vorlage: funktionsgraph
**Abbildung 10:** Sperrschichtkapazität der Beispieldiode zwischen 0 und −25 V: 24,1 pF ohne Spannung, 12,4 pF bei −2 V, 8,5 pF bei −5 V, 6,2 pF bei −10 V und 4,0 pF bei −25 V. Daneben die Zone als Plattenkondensator, dessen Plattenabstand mit der Sperrspannung wächst, von 0,43 µm auf 1,22 µm bei −5 V. Je breiter die Zone, desto kleiner die Kapazität.
:::

**Die Akteure:**

- __$C_j$__: __Sperrschichtkapazität__ (j für englisch junction, Übergang), die Änderung der Ladung in der Zone je Änderung der Spannung; in pF.
- __$C_{j0}$__: ihr Wert ohne Spannung; 24,1 pF bei der Beispieldiode.

**Das Zusammenspiel:** Die Zone besteht aus zwei Schichten fester Ladung mit entgegengesetztem Vorzeichen, wie die beiden Platten eines Kondensators. Ändert man die Sperrspannung ein wenig, legt die Quelle an beiden Rändern der Zone einige Rümpfe zusätzlich frei oder deckt sie mit Majoritätsträgern wieder zu.
Die Ladung ändert sich also an den Rändern, im Abstand $w$ voneinander, wie bei einem Plattenkondensator mit diesem Plattenabstand ([Kondensator und Kapazität](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/kondensator-und-kapazitaet.html)). Anders als dort wächst der Abstand aber mit der Sperrspannung, nach Formel 4 mit ihrer Wurzel; deshalb sinkt die Kapazität, wenn die Sperrspannung steigt.

:::formel Gesetz
$$C_j = \frac{\varepsilon\,A}{w(U)} = \frac{C_{j0}}{\sqrt{1 - U/U_\mathrm{Diff}}}$$
:::

**So liest man das:** Eingabe ist die Spannung, in Sperrrichtung negativ, Ausgabe die Kapazität. Die erste Form ist die Formel des Plattenkondensators mit der Zonenweite als Plattenabstand, die zweite zeigt die Spannungsabhängigkeit.
Vervierfacht sich die Spannung über der Zone, halbiert sich die Kapazität: Bei −2 V liegen 2,714 V statt 0,714 V über der Zone, und die Kapazität sinkt von 24,1 auf 12,4 pF. Die Formel gilt in Sperrrichtung; in Durchlassrichtung überwiegt die gespeicherte Ladung der übergetretenen Ladungsträger (Vertiefung unten).

Idee der Herleitung: Man schreibt die Ladung einer Seite der Zone als Funktion ihrer Weite und leitet nach der Spannung ab.

:::herleitung
**Ausgangspunkt:** die Formel für Weite und Höchstfeld der Zone. Weil die Ladung hier nicht proportional zur Spannung wächst, zählt für kleine Änderungen die Ladungsänderung je Spannungsänderung:

$$C_j = \Big|\frac{\mathrm{d}Q}{\mathrm{d}U}\Big|$$

**Annahmen:** wie bei Weite und Höchstfeld; die Spannung ändert sich so langsam, dass die Zone ihr folgt.

**Schritt 1**: Die Ladung der n-Seite ist Ladungsdichte mal Volumen. Mit der Breite $x_n$ der n-Seite aus der Herleitung von Weite und Höchstfeld:

$$Q = e\,N_D\,x_n\,A = e\,A\,\frac{N_A\,N_D}{N_A + N_D}\,w$$

**Schritt 2**: Nach derselben Formel ist das Quadrat der Weite proportional zur Spannung über der Zone:

$$w^2 = \frac{2\,\varepsilon\,(U_\mathrm{Diff} - U)}{e}\cdot\frac{N_A + N_D}{N_A\,N_D}$$

Abgeleitet nach der Spannung:

$$2\,w\,\frac{\mathrm{d}w}{\mathrm{d}U} = -\frac{2\,\varepsilon}{e}\cdot\frac{N_A + N_D}{N_A\,N_D}$$

**Schritt 3** (entscheidender Schritt): Die Ladung aus Schritt 1 nach der Spannung ableiten und Schritt 2 einsetzen; der Bruch der Dichten kürzt sich heraus:

$$\frac{\mathrm{d}Q}{\mathrm{d}U} = e\,A\,\frac{N_A\,N_D}{N_A + N_D}\cdot\frac{\mathrm{d}w}{\mathrm{d}U} = -\frac{\varepsilon\,A}{w}$$

**Schritt 4**: Damit hängt die Weite so von der Spannung ab:

$$w(U) = w_0\,\sqrt{1 - \frac{U}{U_\mathrm{Diff}}}$$

mit der Weite $w_0$ ohne Spannung. Mit dem Wert ohne Spannung

$$C_{j0} = \frac{\varepsilon\,A}{w_0}$$

folgt die zweite Form.

**Ergebnis:**

$$C_j = \frac{\varepsilon\,A}{w(U)} = \frac{C_{j0}}{\sqrt{1 - U/U_\mathrm{Diff}}}$$

**Woher die Faktoren kommen:** $\varepsilon A/w$ ist der Plattenkondensator mit dem Abstand der beiden Ränder; die Wurzel stammt aus dem Felddreieck, in dem die Weite mit der Wurzel der Spannung wächst.

**Proben:** Einheit: F/cm mal cm² geteilt durch cm ergibt F. Zahlenwert: 1,036·10⁻¹² F/cm mal 10⁻³ cm² geteilt durch 4,30·10⁻⁵ cm ergibt 24,1 pF.

**Grenzen:** Nähert sich die Spannung der Diffusionsspannung, wächst die Formel über alle Grenzen; dort gilt die Verarmungsnäherung nicht mehr.
:::

Dioden, die man gezielt so nutzt, heißen __Kapazitätsdioden__ oder Varaktoren (Skript, Bild 10.9, S. 163). Nimmt ihre Dotierung zum Übergang hin zu, hängt die Kapazität stärker von der Spannung ab als mit der Wurzel.
Man betreibt sie nur in Sperrrichtung, damit kein Strom fließt, und stimmt mit ihrer Steuerspannung Schwingkreise in Radioempfängern und Oszillatoren ab, ohne bewegte Teile.

::::beispiel Sperrschichtkapazität der Beispieldiode
**Gegeben:** Permittivität 1,036·10⁻¹² F/cm, Fläche 10⁻³ cm², Weite ohne Spannung 4,30·10⁻⁵ cm, Diffusionsspannung 0,714 V.

**Gesucht:** die Kapazität ohne Spannung und bei −2 V, −5 V und −10 V.

**Rechnung:** Ohne Spannung:

$$C_{j0} = \frac{1{,}036\cdot10^{-12}\ \mathrm{F/cm}\cdot10^{-3}\ \mathrm{cm^2}}{4{,}30\cdot10^{-5}\ \mathrm{cm}} = 24{,}1\ \mathrm{pF}$$

Bei −2 V mit der zweiten Form von Formel 8:

$$C_j = \frac{24{,}1\ \mathrm{pF}}{\sqrt{1 + 2\ \mathrm{V}/0{,}714\ \mathrm{V}}} = \frac{24{,}1\ \mathrm{pF}}{1{,}950} = 12{,}4\ \mathrm{pF}$$

Ebenso bei −5 V mit der Wurzel 2,829 und bei −10 V mit der Wurzel 3,874:

$$C_j(-5\ \mathrm{V}) = 8{,}5\ \mathrm{pF}, \qquad C_j(-10\ \mathrm{V}) = 6{,}2\ \mathrm{pF}$$

**Ergebnis:** **24,1 pF, 12,4 pF, 8,5 pF und 6,2 pF.**

**Einordnung:** Zwischen 0 und −10 V ändert sich die Kapazität um den Faktor 3,9. Die 1N4148 hat wegen ihrer viel kleineren Fläche nur 4 pF ohne Spannung; bei Audiofrequenzen spielen solche Kapazitäten keine Rolle, bei Hochfrequenz und in schnellen Schaltungen sehr wohl.
::::

:::vertiefung
**Warum eine Diode nicht sofort sperrt.**
In Durchlassrichtung sind in den neutralen Gebieten ständig übergetretene Minoritätsträger unterwegs, bis sie nach im Mittel einer Lebensdauer rekombinieren. Bei konstantem Strom ist deshalb im Mittel die Ladung Lebensdauer mal Strom gespeichert, bei der Beispieldiode mit 1 µs und 1 mA also 1 nC.
Schaltet der äußere Kreis plötzlich auf Sperrrichtung um, muss diese Ladung erst abfließen. Solange sie am Rand der Zone liegt, bleibt die Barriere abgesenkt, und die Diode leitet rückwärts, nur durch den äußeren Kreis begrenzt. Das dauert in der Größenordnung der Lebensdauer: bei der Beispieldiode einige Zehntel Mikrosekunden, bei der 1N4148 mit ihrer kurzen Lebensdauer 4 ns.
Für kleine Spannungsänderungen wirkt die gespeicherte Ladung wie ein zusätzlicher Kondensator, die __Diffusionskapazität__. Weil der Strom und mit ihm die Ladung je $U_T$ um den Faktor 2,72 wächst, liegt sie in der Größenordnung von Lebensdauer mal Strom geteilt durch $U_T$; die genaue Rechnung ergibt bei der Beispieldiode und 1 mA etwa 19 nF, weit mehr als die Sperrschichtkapazität.
:::

## Fotodiode und Solarzelle

*Wie erzeugt Licht in einer Diode einen Strom, und warum kann eine beleuchtete Diode Leistung abgeben?*

:::grafik
Szene: get1/halbleiterbauelemente/02-fotodiode-quadranten · Vorlage: kennlinienschar-quadranten
**Abbildung 11:** Kennlinien der Beispieldiode bei vier Bestrahlungsstärken: Fotostrom 0, 11,7, 23,3 und 35 µA (bis 1000 W/m²). Im dritten Quadranten arbeitet sie als Fotodiode, im vierten als Solarzelle; markiert sind Kurzschlussstrom −35 µA, Leerlaufspannung 0,558 V und der Punkt größter Leistung bei 0,481 V und −33,2 µA. Daneben das Ersatzschaltbild: Stromquelle parallel zur Diode. Licht verschiebt die Kennlinie um den Fotostrom nach unten.
:::

**Die Akteure:**

- __$\lambda$__: Wellenlänge des Lichts; in nm.
- __$I_\mathrm{ph}$__: __Fotostrom__, der Strom der Paare, die das Licht erzeugt und das Feld der Zone trennt; in µA, proportional zur Lichtleistung.
- __$\eta$__: __Quantenausbeute__, der Anteil der einfallenden Photonen, die ein getrenntes Paar liefern; 0,8 im Beispiel.
- __$U_L$__, __$I_K$__: __Leerlaufspannung__ und __Kurzschlussstrom__ der beleuchteten Diode.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Licht besteht aus Photonen, deren Energie das Planck-Wirkungsquantum mal Lichtgeschwindigkeit geteilt durch die Wellenlänge ist (Schulphysik). Ist sie größer als die Bandlücke, kann ein Photon ein Elektron aus einer Bindung ins Leitungsband heben, und es entsteht ein Paar. Das ist der __innere Fotoeffekt__; Silizium nutzt ihn für Licht unterhalb von 1107 nm, also für sichtbares Licht und nahes Infrarot.

**Schritt 2**: Entsteht das Paar in der Zone oder in einigen 10 µm Abstand, so nah, wie ein Minoritätsträger bis zu seiner Rekombination diffundiert, trennt es das Feld der Zone: Das Elektron läuft ins n-Gebiet, das Loch ins p-Gebiet. Das ist die Richtung des Stroms hinunter; das Licht vergrößert den Nachschub an Minoritätsträgern. Der Fotostrom fließt in der Diode von der Kathode zur Anode, also in Sperrrichtung, und zählt negativ.

**Schritt 3**: Er addiert sich zu dem Strom, den die Diode ohne Licht führt. Die ganze Kennlinie verschiebt sich um den Fotostrom nach unten (Abbildung 11); im Ersatzschaltbild ist das eine [Stromquelle](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/ideale-und-reale-quellen.html) parallel zur Diode.

**Schritt 4**: In Sperrrichtung, im dritten Quadranten, ist der Strom fast genau gleich dem negativen Fotostrom: unabhängig von der Spannung und proportional zum Licht. Das ist der __Fotodiodenbetrieb__ zum Messen von Licht, etwa in Lichtschranken, Fernbedienungsempfängern und Glasfaserempfängern.

**Schritt 5**: Zwischen Kurzschluss und Leerlauf ist die Spannung positiv und der Strom negativ, die Diode arbeitet im vierten Quadranten. Das Produkt aus Spannung und Strom ist dann negativ, im Verbraucherzählpfeilsystem heißt das: Die Diode gibt Leistung ab. So arbeitet die __Solarzelle__. Im Leerlauf gleicht der Strom hinauf über die gesenkte Barriere den Fotostrom gerade aus.

:::formel Gesetz
$$I = I_S\,\Big[\exp\!\Big(\frac{U}{U_T}\Big) - 1\Big] - I_\mathrm{ph}$$
:::

**So liest man das:** Eingabe sind Spannung und Fotostrom, Ausgabe der Strom der beleuchteten Diode. Ohne Licht bleibt die Shockley-Gleichung; mit Licht verschiebt sich die Kennlinie um $I_\mathrm{ph}$ nach unten, ohne ihre Form zu ändern.

Idee der Herleitung: Das Licht erzeugt zusätzliche Minoritätsträger und vergrößert damit den Strom hinunter; der Strom hinauf bleibt unberührt.

:::herleitung
**Ausgangspunkt:** das Zwei-Ströme-Bild aus der Herleitung der Shockley-Gleichung.

**Annahmen:** (i) Das Licht erzeugt Paare in und neben der Zone mit einer Rate, die nicht von der Spannung abhängt; (ii) jedes Paar, das in der Zone entsteht oder deren Rand erreicht, wird getrennt; (iii) schwache Injektion: Auch mit Licht bleiben die Minoritätsträger selten gegenüber der Dotierung.

**Schritt 1**: Die vom Licht erzeugten Minoritätsträger fallen wie die thermisch erzeugten über die Barriere hinunter. Der Strom hinunter wird

$$I_\mathrm{hinunter} = I_S + I_\mathrm{ph}$$

**Schritt 2** (entscheidender Schritt): Der Strom hinauf hängt nur von der Höhe der Barriere ab, und die legt nach (iii) weiterhin die Spannung fest:

$$I_\mathrm{hinauf} = I_S\,\exp\!\Big(\frac{U}{U_T}\Big)$$

**Schritt 3**: Netto:

$$I = I_S\,\exp\!\Big(\frac{U}{U_T}\Big) - I_S - I_\mathrm{ph}$$

**Ergebnis:**

$$I = I_S\,\Big[\exp\!\Big(\frac{U}{U_T}\Big) - 1\Big] - I_\mathrm{ph}$$

**Woher die Faktoren kommen:** Der Fotostrom ist ein zusätzlicher Strom hinunter; er steht deshalb mit demselben Vorzeichen wie die −1.

**Proben:** Ohne Licht ergibt sich die Shockley-Gleichung. Ohne Spannung fließt genau der negative Fotostrom. Einheit A.

**Grenzen:** Bei starkem Licht verformt der Bahnwiderstand die Kennlinie, bei schwachem Licht die Rekombination in der Zone; dazu kommen Leckpfade parallel zum Übergang. Reale Solarzellen haben deshalb einen kleineren Füllfaktor als die ideale.
:::

Wie groß der Fotostrom ist und bis zu welcher Wellenlänge er entsteht, folgt aus der Energie der Photonen:

:::formel Formel
$$\lambda_g = \frac{h\,c}{W_g}$$

$$I_\mathrm{ph} = \eta\,\frac{e\,\lambda}{h\,c}\,P$$
:::

**So liest man das:** $\lambda_g$ ist die __Grenzwellenlänge__, oberhalb der die Photonen zu wenig Energie haben: 1107 nm für Silizium. $P$ ist die Lichtleistung, $h$ das Planck-Wirkungsquantum und $c$ die Lichtgeschwindigkeit. Der Fotostrom wächst proportional zur Lichtleistung und bei gleicher Leistung mit der Wellenlänge, weil längerwelliges Licht aus mehr Photonen mit je weniger Energie besteht. Den Quotienten aus Fotostrom und Lichtleistung nennt man __Empfindlichkeit__, in A/W.

Das Skript verlangt, „die Energie der Strahlung“ müsse mindestens die Bandlücke erreichen (S. 163); gemeint ist die Energie jedes einzelnen Photons. Oberhalb von 1107 nm erzeugt Licht in Silizium praktisch keinen Fotostrom, auch wenn es hell ist.

Idee der Herleitung: Man zählt die Photonen pro Sekunde und rechnet jedem getrennten Paar eine Elementarladung im Stromkreis zu.

:::herleitung
**Ausgangspunkt:** die Energie eines Photons (Schulphysik):

$$W_\mathrm{ph} = \frac{h\,c}{\lambda}$$

**Annahmen:** (i) Ein Photon erzeugt höchstens ein Paar; (ii) jedes getrennte Paar bewegt eine Elementarladung durch den äußeren Kreis; (iii) der Anteil $\eta$ der Photonen liefert ein getrenntes Paar.

**Schritt 1**: Ein Paar entsteht nur, wenn die Photonenenergie mindestens die Bandlücke erreicht. Diese Bedingung nach der Wellenlänge aufgelöst:

$$\lambda \le \frac{h\,c}{W_g} = \lambda_g$$

**Schritt 2**: Die Lichtleistung $P$ ist Photonenenergie mal Photonen pro Sekunde; deshalb treffen pro Sekunde

$$\frac{P}{W_\mathrm{ph}} = \frac{P\,\lambda}{h\,c}$$

Photonen ein.

**Schritt 3** (entscheidender Schritt): Nach (ii) und (iii) trägt jedes dieser Photonen mit der Wahrscheinlichkeit $\eta$ eine Elementarladung bei:

$$I_\mathrm{ph} = \eta\,e\,\frac{P\,\lambda}{h\,c}$$

**Ergebnis:**

$$\lambda_g = \frac{h\,c}{W_g}$$

$$I_\mathrm{ph} = \eta\,\frac{e\,\lambda}{h\,c}\,P$$

**Woher die Faktoren kommen:** $h c/\lambda$ ist die Energie eines Photons; durch sie geteilt wird aus der Leistung eine Photonenzahl, und $e$ macht daraus einen Strom.

**Proben:** Einheiten: J s mal m/s geteilt durch J ergibt m; C mal m mal W geteilt durch J s mal m/s ergibt A. Zahlenwert: 1239,8 nm eV geteilt durch 1,12 eV ergibt 1107 nm.

**Grenzen:** Kurzwelliges Licht wird dicht an der Oberfläche absorbiert, wo viele Paare rekombinieren, bevor das Feld sie trennt; Licht knapp unter der Grenzwellenlänge dringt tief ein und wird nur zum Teil absorbiert. Beides verringert $\eta$.
:::

::::beispiel Fotostrom einer Siliziumfotodiode bei 850 nm
**Gegeben:** Lichtleistung 1 mW bei 850 nm; Quantenausbeute 0,8; Bandlücke 1,12 eV; der Wert von $h c$ in praktischen Einheiten ist 1239,8 nm eV.

**Gesucht:** die Photonenenergie, die Zahl der Photonen pro Sekunde, der Fotostrom, die Empfindlichkeit und die Grenzwellenlänge.

**Rechnung:** Photonenenergie und Photonenstrom:

$$W_\mathrm{ph} = \frac{1239{,}8\ \mathrm{nm\,eV}}{850\ \mathrm{nm}} = 1{,}459\ \mathrm{eV}, \qquad \frac{P}{W_\mathrm{ph}} = \frac{10^{-3}\ \mathrm{W}}{1{,}459\cdot1{,}602\cdot10^{-19}\ \mathrm{J}} = 4{,}28\cdot10^{15}\ \mathrm{s^{-1}}$$

Fotostrom nach Formel 10:

$$I_\mathrm{ph} = 0{,}8\cdot1{,}602\cdot10^{-19}\ \mathrm{C}\cdot4{,}28\cdot10^{15}\ \mathrm{s^{-1}} = 0{,}548\ \mathrm{mA}$$

Die Empfindlichkeit ist damit 0,548 A/W. Grenzwellenlänge:

$$\lambda_g = \frac{1239{,}8\ \mathrm{nm\,eV}}{1{,}12\ \mathrm{eV}} = 1107\ \mathrm{nm}$$

**Ergebnis:** **1,459 eV je Photon, 4,28·10¹⁵ Photonen pro Sekunde, 0,548 mA, 0,548 A/W; Grenzwellenlänge 1107 nm.**

**Einordnung:** Datenblätter von Silizium-PIN-Fotodioden nennen bei 850 nm 0,55 bis 0,56 A/W. Bei −1 V und bei −5 V fließt derselbe Strom; die Fotodiode wirkt als Stromquelle, deren Strom das Licht festlegt.
::::

:::fehlvorstellung
„Licht macht die Fotodiode leitend, und der Fotostrom fließt in Durchlassrichtung.“
Das liegt nahe, weil eine Fotodiode in einer Lichtschranke bei Licht Strom durchlässt wie ein Schalter, der schließt, und weil ein Fotowiderstand sich tatsächlich so verhält. Der Fotostrom fließt aber in der Diode von der Kathode zur Anode, in Sperrrichtung; die Diode wird zu einer Stromquelle, deren Strom das Licht festlegt, fast unabhängig von der Sperrspannung. Sie liefert ihn sogar ohne jede äußere Spannung: 0,548 mA bei 1 mW und 850 nm, gleich bei 0 V, −1 V oder −5 V.
:::

Aus Formel 9 folgen die beiden Grenzfälle der beleuchteten Diode:

:::formel Formel
$$U_L = U_T\,\ln\!\Big(\frac{I_\mathrm{ph}}{I_S} + 1\Big)$$

$$I_K = -I_\mathrm{ph}$$
:::

**So liest man das:** Der Kurzschlussstrom ist der negative Fotostrom und wächst proportional zum Licht. Die Leerlaufspannung wächst dagegen nur logarithmisch, um 59,5 mV je Verzehnfachung des Lichts: Bei zehnmal weniger Licht liefert eine Solarzelle fast dieselbe Spannung, aber ein Zehntel des Stroms.
Das ist das Ergebnis des Versuchs im Skript, bei dem eine Lampe in veränderlichem Abstand eine Solarzelle beleuchtet und ein Potentiometer die Last einstellt (S. 164 f.). Mit den dort genannten 0,5 V ist vermutlich die Leerlaufspannung gemeint; bei voller Sonne liegt sie bei Siliziumzellen zwischen 0,6 und 0,7 V, die Spannung im Punkt größter Leistung bei etwa 0,5 V.

Idee der Herleitung: Leerlauf heißt kein Strom, Kurzschluss heißt keine Spannung; beides setzt man in Formel 9 ein.

:::herleitung
**Ausgangspunkt:** die Gleichung der beleuchteten Diode.

**Annahmen:** wie dort.

**Schritt 1**: Im Leerlauf fließt kein Strom:

$$0 = I_S\,\Big[\exp\!\Big(\frac{U_L}{U_T}\Big) - 1\Big] - I_\mathrm{ph}$$

**Schritt 2** (entscheidender Schritt): Nach der Exponentialfunktion auflösen und logarithmieren; der Strom hinauf gleicht dann den Fotostrom aus:

$$\exp\!\Big(\frac{U_L}{U_T}\Big) = \frac{I_\mathrm{ph}}{I_S} + 1 \quad\Rightarrow\quad U_L = U_T\,\ln\!\Big(\frac{I_\mathrm{ph}}{I_S} + 1\Big)$$

**Schritt 3**: Im Kurzschluss ist die Spannung null, und die eckige Klammer verschwindet:

$$I_K = -I_\mathrm{ph}$$

**Ergebnis:**

$$U_L = U_T\,\ln\!\Big(\frac{I_\mathrm{ph}}{I_S} + 1\Big)$$

$$I_K = -I_\mathrm{ph}$$

**Woher die Faktoren kommen:** Der Logarithmus kehrt die Exponentialfunktion des Stroms hinauf um; $I_S$ steht im Nenner, weil ein großer Sperrstrom den Fotostrom schon bei kleiner Spannung ausgleicht.

**Proben:** Ohne Licht ist die Leerlaufspannung null. Zehnmal mehr Licht erhöht sie um $U_T \ln 10$, also 59,5 mV.

**Grenzen:** Rekombination in der Zone senkt die Leerlaufspannung bei schwachem Licht etwas; bei der Beispieldiode und 10 W/m² um 1,3 mV.
:::

::::beispiel Die Beispieldiode als Solarzelle
**Gegeben:** Fläche 0,1 mm², Sättigungssperrstrom 1,457·10⁻¹⁴ A, Temperaturspannung 25,85 mV; bei voller Sonne (1000 W/m²) eine Fotostromdichte von 35 mA/cm², wie bei guten Siliziumzellen.

**Gesucht:** Kurzschlussstrom und Leerlaufspannung bei 1000 W/m² und bei 100 W/m²; der Punkt größter Leistung, der Füllfaktor und der Wirkungsgrad.

**Rechnung:** Fotostrom bei voller Sonne:

$$I_\mathrm{ph} = 35\ \mathrm{mA/cm^2}\cdot10^{-3}\ \mathrm{cm^2} = 35\ \mu\mathrm{A}$$

Leerlaufspannung nach Formel 11:

$$U_L = 25{,}85\ \mathrm{mV}\cdot\ln\!\Big(\frac{35\cdot10^{-6}\ \mathrm{A}}{1{,}457\cdot10^{-14}\ \mathrm{A}} + 1\Big)$$

$$= 25{,}85\ \mathrm{mV}\cdot21{,}60 = 0{,}558\ \mathrm{V}$$

Bei 100 W/m² sind es 3,5 µA und 25,85 mV mal 19,30, also 0,499 V.
Die abgegebene Leistung ist Spannung mal Fotostrom abzüglich des Diodenstroms; sie ist am größten, wo ihre Ableitung nach der Spannung null ist:

$$\frac{\mathrm{d}}{\mathrm{d}U}\Big(U\,\Big[I_\mathrm{ph} - I_S\,\Big(\exp\!\Big(\frac{U}{U_T}\Big) - 1\Big)\Big]\Big) = 0$$

Nach der Produktregel:

$$I_\mathrm{ph} + I_S - I_S\,\exp\!\Big(\frac{U}{U_T}\Big) - \frac{U}{U_T}\,I_S\,\exp\!\Big(\frac{U}{U_T}\Big) = 0$$

Geordnet:

$$\exp\!\Big(\frac{U}{U_T}\Big)\cdot\Big(1 + \frac{U}{U_T}\Big) = \frac{I_\mathrm{ph}}{I_S} + 1$$

Numerisch gelöst: 0,481 V. Dort fließen 35 µA minus 1,8 µA, also 33,2 µA, und die Leistung ist

$$P = 0{,}481\ \mathrm{V}\cdot33{,}2\ \mu\mathrm{A} = 16{,}0\ \mu\mathrm{W}$$

Füllfaktor und Wirkungsgrad, mit 0,1 mW Lichtleistung auf 0,1 mm²:

$$\mathrm{FF} = \frac{16{,}0\ \mu\mathrm{W}}{0{,}558\ \mathrm{V}\cdot35\ \mu\mathrm{A}} = 0{,}82, \qquad \frac{16{,}0\ \mu\mathrm{W}}{0{,}1\ \mathrm{mW}} = 16\ \%$$

**Ergebnis:** **35 µA und 0,558 V bei voller Sonne, 3,5 µA und 0,499 V bei einem Zehntel; größte Leistung 16 µW bei 0,481 V, Füllfaktor 0,82, Wirkungsgrad 16 %.**

**Einordnung:** Ein Zehntel des Lichts kostet nur 59,5 mV Spannung, aber 90 % des Stroms, genau wie das Skript es beschreibt. Der Füllfaktor gibt an, wie gut das Rechteck aus Leerlaufspannung und Kurzschlussstrom ausgenutzt wird; handelsübliche Siliziumzellen liegen bei ähnlichen Werten. Eine Solarzelle von 10 cm mal 10 cm mit demselben Aufbau liefert nach derselben Rechnung 3,5 A bei derselben Leerlaufspannung von 0,558 V, denn Fotostrom und Sättigungssperrstrom wachsen beide mit der Fläche.
::::

:::vertiefung
**Die Leuchtdiode: der umgekehrte Vorgang.**
In Durchlassrichtung rekombinieren die übergetretenen Ladungsträger. In Silizium geht die Energie dabei fast ganz als Wärme an das Gitter, denn Silizium hat eine __indirekte Bandlücke__ ([Reale Bandstrukturen](/wissen/elektrotechnik/4-semester/grundlagen-elektronischer-materialien-und-bauelemente/bandstruktur/reale-bandstrukturen-direkt-indirekt.html)): Elektronen am unteren Rand des Leitungsbands und Löcher am oberen Rand des Valenzbands haben verschiedene Kristallimpulse, die Größe, die im Kristall die Rolle des Impulses spielt, und ein Photon allein kann diesen Unterschied nicht aufnehmen.
In Galliumarsenid, Galliumnitrid und verwandten Verbindungen liegen beide Ränder beim selben Impuls, die Bandlücke ist direkt, und die Rekombination erzeugt meist ein Photon mit etwa der Energie der Bandlücke. Seine Wellenlänge ist die Grenzwellenlänge nach Formel 10: Galliumarsenid mit 1,42 eV strahlt bei 873 nm im nahen Infrarot; rote Leuchtdioden haben Bandlücken um 1,9 eV, blaue um 2,7 eV.
Weil die Durchlassspannung mit der Bandlücke steigt (Abschnitt *Einfluss des Halbleitermaterials*), brauchen rote Leuchtdioden etwa 2 V und blaue etwa 3 V.
:::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Durchlassspannung 0,6 bis 0,7 V, 59,5 mV je Dekade | Die Spannung senkt die Barriere, und der Strom hinauf folgt dem Boltzmann-Faktor. |
| Material und Temperatur | Sie ändern den Nachschub an Minoritätsträgern über $n_i^2$ und verschieben damit die ganze Kennlinie. |
| Sperrstrom im Pikoamperebereich | Wärme erzeugt in und neben der Zone nur wenige Paare. |
| Durchbruch und Z-Diode | Ein sehr starkes Feld erzeugt selbst Ladungsträger, durch Stoßionisation oder Tunneln. |
| Kapazitätsdiode | Ohne Nachschub bleibt die Zone leer; ihre Weite folgt der Spannung und ihre Kapazität der Weite. |
| Fotodiode und Solarzelle | Licht liefert zusätzlichen Nachschub, proportional zur Lichtleistung. |
| reale Kennlinie | Rekombination in der Zone, starke Injektion und Bahnwiderstand verändern, wie viel von der Spannung die Barriere erreicht und was sie dort bewirkt. |

In Durchlassrichtung senkt die Spannung die Barriere, und der Strom wächst exponentiell, um eine Dekade je 60 mV; in Sperrrichtung bestimmt allein der Nachschub an Ladungsträgern den Strom, und den liefern Wärme kaum, Licht in Maßen und ein sehr starkes Feld im Überfluss.

## Bedeutung und Ausblick

Dioden stecken in fast jedem elektronischen Gerät, vom Gleichrichter im Netzteil über Spannungsreferenzen und abstimmbare Oszillatoren bis zu Kamerasensoren und Solarmodulen.
Im Praktikum begegnet die Kennlinie als Basis-Emitter-Strecke des Transistors BC547C ([Bipolartransistor](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise.html)); ihr Temperaturgang von rund −2 mV/K ist ein wichtiger Grund, warum Transistorschaltungen eine Gegenkopplung brauchen, eine Rückführung, die den Arbeitspunkt stabilisiert. Die Herleitung der Kennlinie aus den Grundgleichungen des Halbleiters zeigt der Artikel [Die Diode – der pn-Übergang unter Spannung](/wissen/elektrotechnik/4-semester/grundlagen-elektronischer-materialien-und-bauelemente/bauelemente/diode-pn-uebergang-spannung.html) im Modul GEMB.
Schottky-Dioden aus einem Metall-Halbleiter-Kontakt, die schneller schalten und schon bei 0,2 bis 0,4 V leiten, behandelt dieser Artikel nicht.
Wie man mit der gekrümmten Kennlinie in Schaltungen rechnet, zeigt der nächste Artikel, [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html).

:::kern
- Anode ist die p-, Kathode die n-Seite; das Dreieck im Symbol zeigt die Durchlassrichtung des Stroms.
- Ideale Kennlinie: $I = I_S\,[\exp(U/U_T) - 1]$, mit $U_T$ = 25,85 mV bei 300 K.
- Eine Dekade Strom kostet 59,5 mV; eine feste Schwellspannung gibt es nicht, Datenblätter nennen die Durchlassspannung bei einem Strom.
- Bei festem Strom sinkt die Durchlassspannung um rund 2 mV je Kelvin, weil $I_S$ um 16,6 % je Kelvin wächst.
- Real: Rekombination in der Zone bei kleinen, starke Injektion und Bahnwiderstand bei großen Strömen; der Sperrstrom stammt aus der Generation in der Zone (pA bis nA).
- Durchbruch durch Lawine (über etwa 6 V, positiver Temperaturgang) oder Zener-Effekt (unter etwa 5 V, negativer Temperaturgang); er ist umkehrbar, zerstörend ist nur die Wärme.
- Sperrschichtkapazität: $C_j = \varepsilon A / w(U)$; sie sinkt mit der Sperrspannung.
- Licht verschiebt die Kennlinie um $-I_\mathrm{ph}$; Fotodiode im dritten, Solarzelle im vierten Quadranten, Leerlaufspannung plus 59,5 mV je Dekade Licht.
:::

:::quiz
F: Warum zeigt das Dreieck im Diodensymbol zur Kathode?
A: Es zeigt die technische Stromrichtung in Durchlassrichtung, von der Anode (p-Seite) zur Kathode (n-Seite). Die Elektronen laufen dabei von der Kathode zur Anode, die Löcher umgekehrt; beides ergibt einen Strom in Pfeilrichtung.
F: Warum steigt die Spannung an einer Siliziumdiode zwischen 1 µA und 100 mA nur um 0,3 V?
A: Weil der Strom hinauf mit dem Boltzmann-Faktor der Barrierenabsenkung wächst: Jede Verzehnfachung kostet nur 59,5 mV. Fünf Dekaden ergeben 0,30 V, bei der Beispieldiode von 0,467 auf 0,764 V.
F: Stimmt es, dass eine Siliziumdiode erst ab 0,7 V leitet?
A: Nein. Die scheinbare Schwelle hängt vom Maßstab ab: Auf einer Achse bis 10 µA scheint die Beispieldiode ab 0,407 V zu leiten, auf einer Achse bis 100 mA ab 0,645 V. Datenblätter nennen deshalb die Durchlassspannung bei einem bestimmten Strom.
F: Warum sinkt die Durchlassspannung bei Erwärmung, obwohl die Temperaturspannung im Exponenten wächst?
A: Weil der Sättigungssperrstrom mit $n_i^2$ um 16,6 % je Kelvin wächst, doppelt so schnell, wie der Exponent den Strom bei 1 mA bremst (8,3 % je Kelvin). Bei festem Strom sinkt die Spannung deshalb, bei 1 mA um 2,13 mV je Kelvin.
F: Warum ist der Sperrstrom realer Siliziumdioden viel größer als $I_S$?
A: Im Inneren der gesperrten Zone gibt es keine beweglichen Ladungsträger und deshalb keine Rekombination; Störstellen erzeugen dort ungestört Paare, die das Feld trennt. Bei der Beispieldiode sind das rund 20 pA bei −1 V statt 15 fA.
F: Warum steigt der Strom im Lawinendurchbruch so steil an?
A: Ladungsträger, die im Feld genug Energie sammeln, erzeugen beim Stoß neue Paare, und die neuen Ladungsträger tun dasselbe. Ab etwa 4·10⁵ V/cm erzeugt jeder Ladungsträger auf seinem Weg durch die Zone im Mittel ein weiteres Paar; dann wächst ihre Zahl lawinenartig, und der Strom steigt steil.
F: Stimmt es, dass eine Diode im Durchbruch zerstört wird?
A: Nein. Der Durchbruch ist umkehrbar; Z-Dioden arbeiten dauernd darin. Zerstörend ist die Wärme aus Spannung mal Strom, bei gewöhnlichen Dioden oft örtlich am Rand des Übergangs konzentriert.
F: Eine Z-Diode mit 20 Ω differentiellem Widerstand stabilisiert über einen Vorwiderstand von 330 Ω eine Last von 1 kΩ. Um wie viel ändert sich die Ausgangsspannung, wenn die Eingangsspannung um 2 V steigt?
A: Der Glättungsfaktor ist 1 plus 330 Ω mal (1/20 Ω + 1/1000 Ω), also 17,8. Die Ausgangsspannung steigt um 2 V geteilt durch 17,8, also um 0,11 V.
F: Warum sinkt die Kapazität einer Kapazitätsdiode mit steigender Sperrspannung?
A: Die Zone wirkt wie ein Plattenkondensator, dessen Plattenabstand ihre Weite ist, und diese wächst mit der Wurzel der Spannung über der Zone. Bei der Beispieldiode sinkt die Kapazität von 24,1 pF ohne Spannung auf 8,5 pF bei −5 V.
F: Stimmt es, dass der Fotostrom in Durchlassrichtung fließt?
A: Nein. Das Feld der Zone treibt die vom Licht erzeugten Elektronen ins n- und die Löcher ins p-Gebiet; der Strom fließt in der Diode von der Kathode zur Anode, in Sperrrichtung. Die Kennlinie verschiebt sich um den Fotostrom nach unten, und im vierten Quadranten gibt die Diode Leistung ab.
:::
