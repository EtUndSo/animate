---
title: Die Diode und ihre Kennlinie
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Halbleiterbauelemente
order: 100300
summary: Wie aus dem pn-Übergang ein Bauteil mit Anode und Kathode wird und was seine Kennlinie in Durchlassrichtung, in Sperrrichtung und im Durchbruch bestimmt, bis hin zu Z-Diode, Kapazitätsdiode, Fotodiode und Solarzelle. Kompakte Fassung; die ausführliche enthält zusätzlich die reale Kennlinie und den Temperaturgang mit Herleitung, die Abschätzung der Durchbruchspannung und weitere Hintergründe.
tags: Diode, pn-Übergang, Durchlassrichtung, Sperrrichtung, Schleusenspannung, Shockley-Gleichung, Z-Diode
stil: 3
fassung: kompakt
---

## Worum es geht

Eine Diode lässt Strom fast nur in eine Richtung durch; Gleichrichter, Schutzschaltungen, Spannungsreferenzen, Lichtsensoren und Solarzellen beruhen darauf.
Physikalisch ist sie ein pn-Übergang mit zwei Anschlüssen, und ihre Kennlinie folgt aus der Barriere zwischen p- und n-Gebiet: **In Durchlassrichtung senkt die Spannung die Barriere, und der Strom wächst exponentiell, um eine Dekade je 60 mV; in Sperrrichtung bestimmt allein der Nachschub an Ladungsträgern den Strom, und den liefern Wärme kaum, Licht in Maßen und ein sehr starkes Feld im Überfluss.**

Vorausgesetzt wird der Artikel [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html) mit pn-Übergang, Raumladungszone und den beiden Strömen über die Barriere. Darauf bauen [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html) und [Gleichrichtung und Ladungspumpe](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/gleichrichtung-und-ladungspumpe.html) auf.

:::grafik
Szene: get1/halbleiterbauelemente/02-aufbau-symbol · Vorlage: bauteil-querschnitt-symbol
**Abbildung 1:** Die Diode als Bauteil. (a) Querschnitt: Metallkontakt, p-Gebiet, Raumladungszone (grau), n-Gebiet, Metallkontakt. (b) Schaltsymbol mit Anode A und Kathode K; Spannung $U$ und Strom $I$ zählen von A nach K. (c) Gehäuse mit einem Ring auf der Kathodenseite. In Durchlassrichtung fließt der Strom von der Anode zur Kathode, in Pfeilrichtung des Symbols.
:::

## Aufbau, Anschlüsse und Zählpfeile

*Wie wird aus einem pn-Übergang ein Bauteil, und wie zählt man Spannung und Strom?*

Eine Diode ist ein Siliziumplättchen, auf der einen Seite p- und auf der anderen n-dotiert, mit Metallkontakten an beiden Enden (Abbildung 1a). An der Grenze liegt die Raumladungszone, ein weniger als ein Mikrometer breiter Bereich fast ohne bewegliche Ladungsträger; über ihr steht die Barriere, in der Beispieldiode die Diffusionsspannung von 0,714 V ([Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html)). Der Anschluss am p-Gebiet heißt __Anode__ (A), der am n-Gebiet __Kathode__ (K).
Im Schaltsymbol (Abbildung 1b) zeigt ein Dreieck auf einen Querstrich, der für die Kathode steht; das Dreieck weist in die Richtung, in der die Diode leitet. Auf dem Gehäuse markiert ein Ring die Kathode.

Spannung und Strom zählen von der Anode zur Kathode, im Verbraucherzählpfeilsystem ([Zählpfeile und Vorzeichen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/zaehlpfeile-und-vorzeichen.html)); das Produkt aus $U$ und $I$ ist die Leistung, die die Diode aufnimmt. Positives $U$, die Anode auf höherem Potenzial, ist die __Durchlassrichtung__, negatives $U$ die __Sperrrichtung__.

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

**Das Zusammenspiel:** Im __Durchlassbereich__ senkt die Spannung die Barriere, und der Strom der __Majoritätsträger__, der Sorte in der Überzahl (Elektronen im n-, Löcher im p-Gebiet), die sie überwinden, wächst mit jeden 59,5 mV auf das Zehnfache; ab etwa 0,6 V fließen Milliampere.
Im __Sperrbereich__ ist die Barriere höher als im Gleichgewicht; übrig bleibt der Strom der __Minoritätsträger__, der seltenen Sorte (Löcher im n-, Elektronen im p-Gebiet), den ihr Nachschub begrenzt, ideal 15 fA, real einige 10 pA.
Im __Durchbruch__ erzeugt ein sehr starkes Feld in der Zone selbst Ladungsträger, und der Sperrstrom steigt steil an, bei der Beispieldiode ab rund 100 V (Abbildung 2).

Durchlass- und Sperrbereich beschreibt die __Shockley-Gleichung__:

:::formel Gesetz
$$I = I_S\,\Big[\exp\!\Big(\frac{U}{U_T}\Big) - 1\Big]$$
:::

**So liest man das:** Eingabe ist die Spannung an der Diode, Ausgabe der Strom. Der erste Summand ist der Strom über die abgesenkte Barriere, die −1 der Strom der Minoritätsträger, der nicht von der Spannung abhängt.
Ab etwa 0,1 V ist die −1 vernachlässigbar; unterhalb von etwa −0,1 V ist der Strom gleich $-I_S$. Den Durchbruch enthält die Gleichung nicht.

Das Skript lässt die −1 weg (Gl. 10.1, S. 162), das ist der Grenzfall für den Durchlassbereich. Außerdem nennt es „das Produkt k_B · T“ die thermische Spannung; das ist eine Energie, 25,85 meV. Die Temperaturspannung entsteht erst durch Division durch die Elementarladung:

$$U_T = \frac{k_B\,T}{e} = 25{,}85\ \mathrm{mV}$$

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

- __$U_F$__: __Durchlassspannung__, die Spannung an der leitenden Diode bei einem genannten Strom $I_F$ (F für englisch forward); 0,645 V bei 1 mA für die Beispieldiode im idealen Modell.

Nach der Spannung aufgelöst, sagt die Shockley-Gleichung, welche Spannung ein gegebener Strom braucht:

:::formel Formel
$$U = U_T\,\ln\!\Big(\frac{I}{I_S} + 1\Big)$$
:::

**So liest man das:** Eingabe ist der Strom, Ausgabe die Spannung. Jede Verzehnfachung des Stroms erhöht die Spannung um 59,5 mV, das $\ln 10$-Fache von $U_T$; zwischen 1 µA und 100 mA liegen deshalb nur 0,30 V, von 0,467 V bis 0,764 V.

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

**Schritt 1**: Auf einer linearen Achse sieht man den Strom erst, wenn er einige Prozent des Achsenendes erreicht, und wo das geschieht, legt der Maßstab fest. Ein Prozent von 10 µA erreicht die Beispieldiode bei 0,407 V, ein Prozent von 100 mA bei 0,645 V (Abbildung 3). Einen ausgezeichneten Knick hat die Exponentialfunktion nicht.

**Schritt 2**: In Schaltungen fließen typisch einige Milliampere; auf dieser Skala leitet eine Siliziumdiode ab 0,6 bis 0,7 V. Diesen Erfahrungswert nennt man __Schleusenspannung__. Datenblätter nennen deshalb keine Schwelle, sondern die Durchlassspannung bei einem bestimmten Strom, bei der Kleinsignaldiode 1N4148 höchstens 1 V bei 10 mA, typisch um 0,7 V.

**Schritt 3**: Das Material verschiebt die ganze Kennlinie. Der Sättigungssperrstrom wird von Minoritätsträgern getragen, deren Dichte mit dem Quadrat der Eigenleitungsdichte wächst. Germanium mit 2000-mal mehr freien Ladungsträgern als Silizium hat ein 4·10⁶-mal größeres $I_S$ und braucht für 1 mA nur 0,25 V; Galliumarsenid braucht 1,08 V.

**Schritt 4**: Die Temperatur wirkt an zwei Stellen. Das wachsende $U_T$ im Exponenten allein würde den Strom bei fester Spannung, bei 0,645 V, um 8,3 % je Kelvin senken. $I_S$ wächst aber mit dem Quadrat der Eigenleitungsdichte um 16,6 % je Kelvin, doppelt so schnell. Netto sinkt die Durchlassspannung bei festem Strom, bei 1 mA um 2,1 mV je Kelvin; 50 K Erwärmung kosten 0,1 V. Deshalb taugt eine Diode mit konstantem Strom als Temperatursensor.

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
Das liegt nahe, weil Schaltungsrechnungen mit 0,7 V arbeiten und die Ergebnisse meist passen. Die Spannung an einer leitenden Diode hängt aber vom Strom ab, um 59,5 mV je Dekade, von der Temperatur, um rund −2 mV je Kelvin, und von der Fläche: Eine zehnmal größere Diode braucht für denselben Strom 59,5 mV weniger. Die Beispieldiode liegt bei 1 µA bei 0,467 V und bei 100 mA im idealen Modell bei 0,764 V.
:::

Reale Dioden weichen vom idealen Modell in drei Strombereichen ab.
Bei kleinen Strömen rekombinieren Elektronen und Löcher an Störstellen (Fremdatomen und Gitterfehlern) in der Zone selbst; dieser Strom wächst nur um eine Dekade je 119 mV und überwiegt bei der Beispieldiode unterhalb von 0,27 V, bei Dioden mit kürzerer Lebensdauer bis zu viel größeren Strömen.
Bei großen Strömen, oberhalb von etwa 0,65 V, erreichen die übergetretenen Ladungsträger einen merklichen Teil der Dotierung, bei 0,7 V schon 57 %, und der Strom wächst ebenfalls langsamer (__starke Injektion__).
Schließlich wirken die neutralen Gebiete als ohmscher __Bahnwiderstand__: Bei der Beispieldiode mit 18,9 Ω fallen bei 10 mA weitere 0,19 V ab, sie braucht dann 0,90 V statt 0,70 V; reale Kleinsignaldioden haben Bahnwiderstände unter einem Ohm.
Datenblätter und Simulatoren fassen das mit einem __Emissionskoeffizienten__ zwischen 1 und 2 im Nenner des Exponenten und dem Bahnwiderstand zusammen.

:::frage
„Warum ist der gemessene Sperrstrom einer Siliziumdiode viel größer als $I_S$?“
Weil in der gesperrten Zone selbst Paare entstehen. In ihrem Inneren gibt es fast keine beweglichen Ladungsträger und deshalb keine Rekombination; Störstellen erzeugen ungestört Paare, die das Feld sofort trennt. Bei der Beispieldiode sind das rund 20 pA bei −1 V statt 15 fA, dazu kommen Leckströme an der Oberfläche; die 1N4148 garantiert höchstens 25 nA bei 20 V. Weil dieser Strom an der Eigenleitungsdichte hängt, verdoppelt er sich etwa alle 8 bis 10 K.
:::

## Der Durchbruch

*Warum steigt der Sperrstrom ab einer bestimmten Spannung plötzlich steil an?*

:::grafik
Szene: get1/halbleiterbauelemente/02-durchbruch-mechanismen · Vorlage: banddiagramm-durchbruch
**Abbildung 4:** Die beiden Durchbruchmechanismen im Banddiagramm. (a) Lawine in der Beispieldiode bei rund 100 V: Die Zone ist etwa 5 µm breit; ein Elektron gewinnt im Feld Energie, schlägt beim Stoß ein Elektron aus einer Bindung und erzeugt so ein Paar, und die neuen Ladungsträger tun dasselbe. (b) Zener-Effekt in einem Übergang mit 10¹⁸ cm⁻³: Die Zone ist nur 0,13 µm breit, die Bänder fallen steil, und ein Elektron tunnelt waagrecht vom Valenzband der p-Seite in das 11 nm entfernte Leitungsband der n-Seite.
:::

**Die Akteure:**

- __$N_A$__, __$N_D$__: Dichte der Akzeptoren im p-Gebiet bzw. der Donatoren im n-Gebiet; je 10¹⁶ cm⁻³ in der Beispieldiode.
- __$\varepsilon$__: Permittivität von Silizium; 1,036·10⁻¹² F/cm.
- __$w$__, __$E_\mathrm{max}$__: Weite der Raumladungszone und Betrag des Feldes an der Grenzfläche, wo es am stärksten ist; 0,43 µm und 3,3·10⁴ V/cm ohne Spannung.

**Das Zusammenspiel:** Eine Sperrspannung zieht für einen Augenblick Majoritätsträger von der Grenze ab; weitere Rümpfe liegen frei, und die Zone wird breiter, bis sie die Diffusionsspannung plus die Sperrspannung trägt. In der Zone sitzt dann nur die feste Ladung der Rümpfe, und durch sie wächst das Feld linear bis zur Grenzfläche an. Die Spannung über der Zone ist die Fläche unter diesem Felddreieck.

:::formel Formel
$$w = \sqrt{\frac{2\varepsilon\,(U_\mathrm{Diff} - U)}{e}\cdot\frac{N_A + N_D}{N_A\,N_D}}$$

$$E_\mathrm{max} = \frac{2\,(U_\mathrm{Diff} - U)}{w}$$
:::

**So liest man das:** Eingabe ist die Spannung an der Diode, Ausgabe die Weite der Zone und ihr Höchstfeld. Beide wachsen mit der Wurzel der Spannung über der Zone: Bei −5 V sind es 1,22 µm und 9,4·10⁴ V/cm, bei −50 V 3,62 µm und 2,8·10⁵ V/cm. Hoch dotierte Übergänge sind dünn und haben schon bei kleinen Spannungen starke Felder.

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

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Im Sperrbereich begrenzt der Nachschub den Strom: Die Wärme erzeugt nur einige 10 pA, und mehr Sperrspannung erhöht das nur langsam.

**Schritt 2**: Das Feld in der Zone wächst aber mit der Wurzel der Spannung. Ein Ladungsträger, der im Feld mehr Energie als die Bandlücke sammelt, kann beim Stoß ein Elektron aus einer Bindung schlagen. Ab etwa 4·10⁵ V/cm erzeugt jeder Ladungsträger auf seinem Weg durch die Zone im Mittel ein weiteres Paar, die neuen tun dasselbe, und aus einem Ladungsträger wird eine Lawine (Abbildung 4a). Diesen __Lawinendurchbruch__ erreicht die Beispieldiode bei rund 100 V.

**Schritt 3**: In sehr hoch dotierten Übergängen, um 10¹⁸ cm⁻³, ist die Zone nur rund 0,1 µm breit, und wenige Volt ergeben 10⁶ V/cm. Dann liegt das Leitungsband der n-Seite auf gleicher Energie nur 11 nm neben dem Valenzband der p-Seite, und Elektronen gelangen durch die verbotene Zone hindurch, ohne Energie zu brauchen: Sie __tunneln__ (Abbildung 4b). Das ist der __Zener-Effekt__.

**Schritt 4**: In beiden Fällen erzeugt das Feld selbst Ladungsträger, und der äußere Kreis muss den Strom begrenzen. Unter etwa 5 V überwiegt der Zener-Effekt, über etwa 6 V die Lawine. Ihre Temperaturgänge sind entgegengesetzt: Mit der Wärme stoßen die Ladungsträger öfter, und die Lawinenspannung steigt; die Bandlücke schrumpft, und die Zener-Spannung sinkt. Um 5 bis 6 V heben sich beide nahezu auf.

:::fehlvorstellung
„Im Durchbruch wird die Diode zerstört.“
Das liegt nahe, weil das Skript es so formuliert (S. 162) und weil gewöhnliche Dioden ohne Strombegrenzung im Durchbruch tatsächlich ausfallen. Der Durchbruch selbst ist aber umkehrbar: Z-Dioden arbeiten dauernd darin, wie das Skript eine Seite später selbst schreibt (S. 163). Zerstörend ist die Wärme: Bei 100 V und 10 mA setzt eine kleine Diode 1 W um, doppelt so viel, wie typische kleine Gehäuse vertragen. Bei gewöhnlichen Dioden beginnt der Durchbruch zudem oft an den Rändern des Übergangs, wo sich der Strom zusammendrängt.
:::

## Die Z-Diode

*Wie hält eine Diode eine Spannung fest, obwohl der Strom durch sie schwankt?*

:::grafik
Szene: get1/halbleiterbauelemente/02-z-diode-stabilisierung · Vorlage: schaltung-und-kennlinie
**Abbildung 5:** Spannungsstabilisierung mit einer Z-Diode. (a) Schaltung: Eingangsspannung 12 V ± 1 V, Vorwiderstand 330 Ω, Z-Diode 5,6 V parallel zum Lastwiderstand 1 kΩ. (b) Durchbruchast der Z-Diode mit den Arbeitspunkten bei 11, 12 und 13 V Eingangsspannung: 10,3 mA, 13,1 mA und 15,9 mA bei 5,707 V, 5,763 V und 5,819 V. Ein Stromhub von 5,6 mA ändert die Spannung nur um 0,11 V.
:::

**Die Akteure:**

- __$U_Z$__: __Z-Spannung__, der Betrag der Spannung im Durchbruch bei einem genannten Strom; 5,6 V bei 5 mA im Beispiel.
- __$r_Z$__: __differentieller Widerstand__, die Steigung des Durchbruchasts, also Spannungsänderung geteilt durch Stromänderung; im Beispiel 20 Ω. Allgemein behandelt ihn der Artikel [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html).

**Das Zusammenspiel:** Eine __Z-Diode__ ist eine Siliziumdiode, die für den Betrieb im Durchbruch gebaut ist. Ihre Dotierung legt die Z-Spannung fest, je nach Typ zwischen etwa 2 V und über 100 V; in Durchlassrichtung verhält sie sich wie eine gewöhnliche Diode.
Im Durchbruch ist ihre Kennlinie steil, und darauf beruht die Stabilisierung (Abbildung 5a): Ein Vorwiderstand nimmt die Differenz zwischen schwankender Eingangsspannung und Z-Spannung auf. Steigt die Eingangsspannung, fließt mehr Strom durch den Vorwiderstand, und fast der ganze zusätzliche Strom geht durch die Z-Diode, deren Spannung sich dabei kaum ändert. Die Last parallel zur Z-Diode sieht eine fast konstante Spannung (Abbildung 5b).

::::beispiel Stabilisierung mit einer 5,6-V-Z-Diode
**Gegeben:** Eingangsspannung 12 V ± 1 V; Vorwiderstand 330 Ω; Lastwiderstand 1 kΩ; Z-Diode mit 5,6 V bei 5 mA und 20 Ω differentiellem Widerstand, ihr Durchbruchast also eine Gerade durch 5,5 V bei null Strom.

**Gesucht:** Ausgangsspannung und Z-Strom bei 11, 12 und 13 V; die Verlustleistung der Z-Diode im ungünstigsten Fall.

**Rechnung:** Auf der Geraden ist der Z-Strom

$$I_Z = \frac{U_A - 5{,}5\ \mathrm{V}}{20\ \Omega}$$

Die Knotenregel am Ausgang: Der Strom durch den Vorwiderstand teilt sich in Laststrom und Z-Strom.

$$\frac{U_E - U_A}{330\ \Omega} = \frac{U_A}{1\ \mathrm{k}\Omega} + \frac{U_A - 5{,}5\ \mathrm{V}}{20\ \Omega}$$

Bei 12 V nach der Ausgangsspannung aufgelöst:

$$U_A = \frac{36{,}36\ \mathrm{mA} + 275\ \mathrm{mA}}{3{,}030\ \mathrm{mS} + 1\ \mathrm{mS} + 50\ \mathrm{mS}} = 5{,}763\ \mathrm{V}, \qquad I_Z = 13{,}1\ \mathrm{mA}$$

Ebenso bei 11 V: 5,707 V und 10,3 mA; bei 13 V: 5,819 V und 15,9 mA. Am meisten Leistung setzt die Z-Diode bei 13 V ohne Last um, wenn der ganze Strom durch sie fließt:

$$I_Z = \frac{13\ \mathrm{V} - 5{,}5\ \mathrm{V}}{330\ \Omega + 20\ \Omega} = 21{,}4\ \mathrm{mA}, \qquad P_Z = 5{,}93\ \mathrm{V}\cdot21{,}4\ \mathrm{mA} = 127\ \mathrm{mW}$$

**Ergebnis:** **Ausgang 5,763 V ± 0,056 V bei 13,1 mA ± 2,8 mA; höchstens 127 mW in der Z-Diode.**

**Einordnung:** Eine Schwankung von ±1 V am Eingang kommt am Ausgang als ±0,056 V an, 17,8-mal kleiner; relativ sind das ±8 % gegen ±1 %. Eine Z-Diode für 0,5 W genügt auch im ungünstigsten Fall.
::::

## Die Kapazitätsdiode

*Warum hängt die Kapazität einer gesperrten Diode von der Spannung ab?*

:::grafik
Szene: get1/halbleiterbauelemente/02-sperrschichtkapazitaet · Vorlage: funktionsgraph
**Abbildung 6:** Sperrschichtkapazität der Beispieldiode zwischen 0 und −25 V: 24,1 pF ohne Spannung, 12,4 pF bei −2 V, 8,5 pF bei −5 V, 6,2 pF bei −10 V und 4,0 pF bei −25 V. Daneben die Zone als Plattenkondensator, dessen Plattenabstand mit der Sperrspannung wächst, von 0,43 µm auf 1,22 µm bei −5 V. Je breiter die Zone, desto kleiner die Kapazität.
:::

**Die Akteure:**

- __$C_j$__: __Sperrschichtkapazität__ (j für englisch junction, Übergang), die Änderung der Ladung in der Zone je Änderung der Spannung; $C_{j0}$ ist ihr Wert ohne Spannung, 24,1 pF bei der Beispieldiode.

**Das Zusammenspiel:** Die Zone besteht aus zwei Schichten fester Ladung mit entgegengesetztem Vorzeichen. Ändert man die Sperrspannung ein wenig, legt die Quelle an beiden Rändern einige Rümpfe zusätzlich frei oder deckt sie wieder zu; die Ladung ändert sich also im Abstand $w$, wie bei einem [Plattenkondensator](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/kondensator-und-kapazitaet.html) mit diesem Plattenabstand. Weil die Zone mit der Sperrspannung breiter wird, sinkt die Kapazität.

:::formel Gesetz
$$C_j = \frac{\varepsilon\,A}{w(U)} = \frac{C_{j0}}{\sqrt{1 - U/U_\mathrm{Diff}}}$$
:::

**So liest man das:** Eingabe ist die Spannung, in Sperrrichtung negativ, Ausgabe die Kapazität; $A$ ist die Fläche des Übergangs. Vervierfacht sich die Spannung über der Zone, halbiert sich die Kapazität: Bei −2 V sinkt sie von 24,1 auf 12,4 pF, bei −10 V auf 6,2 pF (Abbildung 6).

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

Dioden, die man gezielt so nutzt, heißen __Kapazitätsdioden__ (Skript, Bild 10.9, S. 163). Man betreibt sie nur in Sperrrichtung, damit kein Strom fließt, und stimmt mit ihrer Steuerspannung Schwingkreise in Radioempfängern und Oszillatoren ab, ohne bewegte Teile.

## Fotodiode und Solarzelle

*Wie erzeugt Licht in einer Diode einen Strom, und warum kann eine beleuchtete Diode Leistung abgeben?*

:::grafik
Szene: get1/halbleiterbauelemente/02-fotodiode-quadranten · Vorlage: kennlinienschar-quadranten
**Abbildung 7:** Kennlinien der Beispieldiode bei vier Bestrahlungsstärken: Fotostrom 0, 11,7, 23,3 und 35 µA (bis 1000 W/m²). Im dritten Quadranten arbeitet sie als Fotodiode, im vierten als Solarzelle; markiert sind Kurzschlussstrom −35 µA, Leerlaufspannung 0,558 V und der Punkt größter Leistung bei 0,481 V und −33,2 µA. Daneben das Ersatzschaltbild: Stromquelle parallel zur Diode. Licht verschiebt die Kennlinie um den Fotostrom nach unten.
:::

**Die Akteure:**

- __$I_\mathrm{ph}$__: __Fotostrom__, der Strom der Paare, die das Licht erzeugt und das Feld der Zone trennt; proportional zur Lichtleistung.
- __$U_L$__, __$I_K$__: __Leerlaufspannung__ und __Kurzschlussstrom__ der beleuchteten Diode.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Ein Photon mit mehr Energie als die Bandlücke kann ein Elektron aus einer Bindung ins Leitungsband heben; es entsteht ein Paar (__innerer Fotoeffekt__). Entscheidend ist die Energie des einzelnen Photons; das meint das Skript mit der „Energie der Strahlung (antiproportional zur Wellenlänge)“ (S. 163). Silizium reagiert deshalb nur auf Licht unterhalb von 1107 nm Wellenlänge; längerwelliges Licht erzeugt praktisch keinen Fotostrom, auch wenn es hell ist.

**Schritt 2**: Entsteht das Paar in der Zone oder nahe daneben, trennt es das Feld: Das Elektron läuft ins n-Gebiet, das Loch ins p-Gebiet. Das Licht vergrößert also den Nachschub an Minoritätsträgern, und der Fotostrom fließt in der Diode von der Kathode zur Anode, in Sperrrichtung.

**Schritt 3**: Die ganze Kennlinie verschiebt sich um den Fotostrom nach unten (Abbildung 7); im Ersatzschaltbild ist das eine [Stromquelle](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/ideale-und-reale-quellen.html) parallel zur Diode. In Sperrrichtung ist der Strom fast genau der negative Fotostrom, proportional zum Licht: der __Fotodiodenbetrieb__ in Lichtschranken und Lichtsensoren.

**Schritt 4**: Zwischen Kurzschluss und Leerlauf ist die Spannung positiv und der Strom negativ, ihr Produkt also negativ: Im Verbraucherzählpfeilsystem heißt das, die Diode gibt Leistung ab. So arbeitet die __Solarzelle__.

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

:::frage
„Macht Licht die Fotodiode leitend, so wie ein Schalter, der sich schließt?“
Nein. Ein Fotowiderstand verhält sich so, eine Fotodiode nicht: Sie wird zu einer Stromquelle in Sperrrichtung, deren Strom das Licht festlegt, fast unabhängig von der Spannung. Eine Silizium-Fotodiode liefert bei 1 mW Licht von 850 nm rund 0,55 mA, gleich ob 0 V, −1 V oder −5 V anliegen; sie braucht dafür nicht einmal eine äußere Spannungsquelle.
:::

Aus der Gleichung der beleuchteten Diode folgen ihre beiden Grenzfälle:

:::formel Formel
$$U_L = U_T\,\ln\!\Big(\frac{I_\mathrm{ph}}{I_S} + 1\Big)$$

$$I_K = -I_\mathrm{ph}$$
:::

**So liest man das:** Der Kurzschlussstrom ist der negative Fotostrom und wächst proportional zum Licht. Die Leerlaufspannung wächst dagegen nur logarithmisch, um 59,5 mV je Verzehnfachung des Lichts. Das ist das Ergebnis des Solarzellenversuchs im Skript (S. 164 f.): Die Spannung hängt kaum von der Einstrahlung ab, der Strom wächst proportional. Mit den dort genannten 0,5 V ist vermutlich die Leerlaufspannung gemeint; bei voller Sonne liegt sie bei Siliziumzellen zwischen 0,6 und 0,7 V, die Spannung im Punkt größter Leistung bei etwa 0,5 V.

Idee der Herleitung: Leerlauf heißt kein Strom, Kurzschluss heißt keine Spannung; beides setzt man in die Gleichung der beleuchteten Diode ein.

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

**Gesucht:** Kurzschlussstrom und Leerlaufspannung bei 1000 W/m² und bei 100 W/m².

**Rechnung:** Fotostrom bei voller Sonne:

$$I_\mathrm{ph} = 35\ \mathrm{mA/cm^2}\cdot10^{-3}\ \mathrm{cm^2} = 35\ \mu\mathrm{A}$$

Leerlaufspannung nach Formel 6:

$$U_L = 25{,}85\ \mathrm{mV}\cdot\ln\!\Big(\frac{35\cdot10^{-6}\ \mathrm{A}}{1{,}457\cdot10^{-14}\ \mathrm{A}} + 1\Big)$$

$$= 25{,}85\ \mathrm{mV}\cdot21{,}60 = 0{,}558\ \mathrm{V}$$

Bei 100 W/m² ist der Fotostrom zehnmal kleiner, 3,5 µA, und die Leerlaufspannung

$$U_L = 25{,}85\ \mathrm{mV}\cdot19{,}30 = 0{,}499\ \mathrm{V}$$

**Ergebnis:** **35 µA und 0,558 V bei voller Sonne; 3,5 µA und 0,499 V bei einem Zehntel.**

**Einordnung:** Ein Zehntel des Lichts kostet 90 % des Stroms, aber nur 59,5 mV Spannung. Die größte Leistung gibt die Zelle zwischen beiden Grenzfällen ab, bei 0,481 V und 33,2 µA: 16 µW aus 0,1 mW Licht, ein Wirkungsgrad von 16 %.
::::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Durchlassspannung 0,6 bis 0,7 V, 59,5 mV je Dekade | Die Spannung senkt die Barriere, und der Strom folgt dem Boltzmann-Faktor. |
| Material und Temperatur | Sie ändern den Nachschub an Minoritätsträgern über $n_i^2$ und verschieben die ganze Kennlinie. |
| Sperrstrom und Kapazitätsdiode | Wärme liefert kaum Nachschub; die Zone bleibt fast leer, und ihre Weite folgt der Spannung. |
| Durchbruch und Z-Diode | Ein sehr starkes Feld erzeugt selbst Ladungsträger, durch Stoßionisation oder Tunneln. |
| Fotodiode und Solarzelle | Licht liefert zusätzlichen Nachschub, proportional zur Lichtleistung. |

In Durchlassrichtung senkt die Spannung die Barriere, und der Strom wächst exponentiell, um eine Dekade je 60 mV; in Sperrrichtung bestimmt allein der Nachschub an Ladungsträgern den Strom, und den liefern Wärme kaum, Licht in Maßen und ein sehr starkes Feld im Überfluss.

## Bedeutung und Ausblick

Dioden stecken in fast jedem elektronischen Gerät, vom Gleichrichter im Netzteil bis zum Kamerasensor. Im Praktikum begegnet die Kennlinie als Basis-Emitter-Strecke des Transistors BC547C; ihr Temperaturgang von rund −2 mV/K ist ein wichtiger Grund, warum Transistorschaltungen eine Gegenkopplung brauchen, eine Rückführung, die den Arbeitspunkt stabilisiert. Wie man mit der gekrümmten Kennlinie in Schaltungen rechnet, zeigt der nächste Artikel, [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html).

**In der ausführlichen Fassung:** der Einfluss des Halbleitermaterials und der Temperaturgang mit Herleitung, die reale Kennlinie mit Rekombinations- und Generationsstrom und dem Emissionskoeffizienten, die Abschätzung der Durchbruchspannung und der Dotierung einer Z-Diode, der Glättungsfaktor der Stabilisierungsschaltung, Grenzwellenlänge und Empfindlichkeit einer Fotodiode, der Punkt größter Leistung einer Solarzelle, das Schaltverhalten und die Leuchtdiode. [Zur ausführlichen Fassung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie-ausfuehrlich.html)

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
F: Warum steigt die Spannung an einer Siliziumdiode zwischen 1 µA und 100 mA nur um 0,3 V?
A: Weil der Strom über die Barriere mit dem Boltzmann-Faktor ihrer Absenkung wächst: Jede Verzehnfachung kostet nur 59,5 mV. Fünf Dekaden ergeben 0,30 V, bei der Beispieldiode von 0,467 auf 0,764 V.
F: Stimmt es, dass eine Siliziumdiode erst ab 0,7 V leitet?
A: Nein. Die scheinbare Schwelle hängt vom Maßstab ab: Auf einer Achse bis 10 µA scheint die Beispieldiode ab 0,407 V zu leiten, auf einer Achse bis 100 mA ab 0,645 V. Datenblätter nennen deshalb die Durchlassspannung bei einem bestimmten Strom.
F: Warum sinkt die Durchlassspannung bei Erwärmung, obwohl die Temperaturspannung im Exponenten wächst?
A: Weil der Sättigungssperrstrom mit dem Quadrat der Eigenleitungsdichte um 16,6 % je Kelvin wächst, doppelt so schnell, wie der Exponent den Strom bei 1 mA bremst (8,3 % je Kelvin). Bei festem Strom sinkt die Spannung deshalb, bei 1 mA um rund 2 mV je Kelvin.
F: Stimmt es, dass eine Diode im Durchbruch zerstört wird?
A: Nein. Der Durchbruch ist umkehrbar; Z-Dioden arbeiten dauernd darin. Zerstörend ist die Wärme aus Spannung mal Strom.
F: Wie groß ist die Leerlaufspannung der Beispieldiode als Solarzelle bei 35 µA Fotostrom, und wie ändert sie sich bei einem Zehntel des Lichts?
A: 25,85 mV mal ln(35 µA geteilt durch 1,457·10⁻¹⁴ A plus 1) ergibt 0,558 V. Bei einem Zehntel des Lichts sind es 59,5 mV weniger, 0,499 V, während der Kurzschlussstrom auf ein Zehntel sinkt.
F: Warum sinkt die Kapazität einer Kapazitätsdiode mit steigender Sperrspannung?
A: Die Zone wirkt wie ein Plattenkondensator, dessen Plattenabstand ihre Weite ist, und diese wächst mit der Wurzel der Spannung über der Zone. Bei der Beispieldiode sinkt die Kapazität von 24,1 pF ohne Spannung auf 6,2 pF bei −10 V.
:::
