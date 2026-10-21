---
title: Der Bipolartransistor – Aufbau und Wirkungsweise
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Bipolartransistoren
order: 110100
summary: Wie aus drei dotierten Schichten ein Bauteil wird, in dem die Basis-Emitter-Spannung einen großen Kollektorstrom festlegt und nur ein kleiner Basisstrom fließt: Aufbau, Transistoreffekt mit Transfergleichung, Basisstrom und Stromverstärkung, Kennlinien, Arbeitsbereiche mit Sättigung, Schalter und pnp-Transistor. Kompakte Fassung; die ausführliche enthält zusätzlich die Stromverstärkung aus Dotierung und Geometrie, die Belege für die Spannungssicht, den Inversbetrieb, die Speicherzeit und weitere Beispiele.
tags: Bipolartransistor, npn, pnp, Transistoreffekt, Stromverstärkung, aktiver Bereich, Sättigung
stil: 3
fassung: kompakt
---

## Worum es geht

Eine Diode lässt Strom durch oder sperrt ihn. Zum Verstärken und Schalten braucht man ein Bauteil, in dem eine kleine Steuergröße einen großen Strom festlegt; der __Bipolartransistor__ erreicht das mit zwei pn-Übergängen in einem Kristall.
**Ein gesperrter pn-Übergang führt so viel Strom, wie Nachschub an Minoritätsträgern zu ihm gelangt; im Bipolartransistor liefert ein leitender Übergang diesen Nachschub durch eine sehr dünne Basis, sodass die Basis-Emitter-Spannung den Kollektorstrom exponentiell festlegt, die Kollektorspannung ihn kaum beeinflusst und nur ein kleiner, fester Bruchteil als Basisstrom fließt.**
Minoritätsträger sind die seltene Ladungsträgersorte eines Gebiets, etwa Elektronen in einem p-dotierten Gebiet.

Vorausgesetzt werden der pn-Übergang aus [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html), die Kennlinie aus [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html) und Annahme und Probe aus [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html).

:::grafik
Szene: get1/bipolartransistoren/01-npn-querschnitt · Vorlage: querschnitt-traegerfluesse
**Abbildung 1:** npn-Transistor im Querschnitt im Normalbetrieb, schematisch (Dicken nicht maßstäblich): stark n-dotierter Emitter, dünne p-dotierte Basis, schwach n-dotierter Kollektor, Raumladungszonen grau. Bei 2 mA Kollektorstrom laufen Elektronen (blau) vom Emitter durch die Basis in den Kollektor; über den Basisanschluss kommen nur Löcher (rot) nach, zusammen 4 µA, die Verluste durch Rückinjektion in den Emitter und durch Rekombination ersetzen. Die Pfeile an den Anschlüssen zeigen die technische Stromrichtung. Der Kollektorstrom fließt nicht über die Basis; die Basis ersetzt nur Verluste.
:::

## Aufbau, Schaltsymbol und Zählpfeile

*Woraus besteht ein Bipolartransistor, und wie zählt man seine Ströme und Spannungen?*

:::grafik
Szene: get1/bipolartransistoren/01-aufbau-symbole · Vorlage: aufbau-und-symbol
**Abbildung 2:** (a) npn-Transistor: Schichtfolge Emitter (n⁺, 10¹⁹ cm⁻³), Basis (p, 10¹⁷ cm⁻³, 0,5 µm), Kollektor (n, 10¹⁶ cm⁻³), dazu die Polung im Normalbetrieb und das Schaltsymbol mit den Zählpfeilen des Skripts: Basis- und Kollektorstrom in den Transistor hinein, Emitterstrom heraus, Spannungen $U_{BE}$, $U_{CB}$ und $U_{CE}$. (b) pnp-Transistor mit umgekehrter Schichtfolge, Emitterpfeil nach innen und den Zählpfeilen aus Bild 11.30 des Skripts: Emitterstrom hinein, Basis- und Kollektorstrom heraus. Drei Gebiete, zwei Übergänge; der Emitterpfeil zeigt die Richtung des Emitterstroms.
:::

Drei unterschiedlich dotierte Gebiete in einem Siliziumkristall bilden den Transistor: __Emitter__ (E), __Basis__ (B) und __Kollektor__ (C). Dotiert heißt, dass Fremdatome eingebaut sind, die Elektronen abgeben (n-Gebiet) oder Löcher erzeugen (p-Gebiet). Beim __npn-Transistor__ liegt eine p-Basis zwischen zwei n-Gebieten, beim __pnp-Transistor__ umgekehrt (Abbildung 2). Dazwischen liegen zwei pn-Übergänge, der __Basis-Emitter-Übergang__ und der __Basis-Kollektor-Übergang__.

Die Gebiete sind bewusst ungleich (Skript, S. 175). Beim Beispieltransistor dieses Artikels, der in seinen Kennwerten dem BC547C aus dem Praktikum entspricht, trägt der Emitter 10¹⁹ Donatoren pro cm³, die Basis 100-mal weniger Akzeptoren und der Kollektor noch einmal zehnmal weniger Donatoren. Die neutrale Basis ist nur 0,5 µm weit. Der Name „bipolar“ besagt, dass Elektronen und Löcher beteiligt sind.

Im __Schaltsymbol__ zeigt der Pfeil am Emitter die Richtung des Emitterstroms, beim npn-Transistor aus dem Bauteil heraus. Gezählt wird wie im Skript (Bild 11.1): Basis- und Kollektorstrom hinein, Emitterstrom heraus; Spannungen vom ersten zum zweiten genannten Anschluss.

**Die Akteure:**

- __$I_C$__: __Kollektorstrom__, in den Kollektor hinein; in A; beim Beispieltransistor typisch 0,1 bis 10 mA. Ihn will man steuern.
- __$I_B$__: __Basisstrom__, in die Basis hinein; in A; beim Beispieltransistor 500-mal kleiner als der Kollektorstrom.
- __$I_E$__: __Emitterstrom__, aus dem Emitter heraus; in A.
- __$U_{BE}$__: Spannung von der Basis zum Emitter; in V; im Normalbetrieb 0,6 bis 0,7 V, Basis-Emitter-Übergang in Durchlassrichtung.
- __$U_{CB}$__, __$U_{CE}$__: Spannungen vom Kollektor zur Basis bzw. zum Emitter; in V; im Normalbetrieb einige Volt. Positives $U_{CB}$ sperrt den Basis-Kollektor-Übergang.

**Das Zusammenspiel:** Weil der Transistor als Ganzes neutral bleibt, fließt am Emitter heraus, was an Basis und Kollektor hineinfließt; und die Spannung vom Kollektor zum Emitter führt über die Basis (Skript, S. 176):

:::formel Formel
$$I_E = I_B + I_C$$

$$U_{CE} = U_{CB} + U_{BE}$$
:::

**So liest man das:** Je zwei Ströme und zwei Spannungen legen die dritte Größe fest. Ist $U_{CE}$ größer als $U_{BE}$, ist $U_{CB}$ positiv und der Basis-Kollektor-Übergang gesperrt.

Idee der Herleitung: Knotenregel für eine Hülle um den Transistor, Maschenregel über die drei Anschlüsse.

:::herleitung
**Ausgangspunkt:** die Knotenregel (Ladungserhaltung) und die Maschenregel (Spannung als Differenz zweier Potenziale) aus [Kirchhoffsche Gesetze](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/kirchhoffsche-gesetze.html).

**Annahmen:** (i) Der Transistor ist als Ganzes neutral; gespeicherte Ladungen, etwa in den Raumladungszonen, treten immer paarweise positiv und negativ auf. (ii) Die Spannungen sind Klemmenspannungen zwischen den Anschlüssen.

**Schritt 1**: Eine geschlossene Hülle um den Transistor schneidet die drei Anschlüsse. Nach (i) sammelt sich darin keine Ladung, die hineinfließenden Ströme sind also gleich den herausfließenden. Mit den Zählpfeilen fließen Basis- und Kollektorstrom hinein, der Emitterstrom heraus:

$$I_B + I_C = I_E$$

**Schritt 2**: Jede Spannung ist eine Differenz der Potenziale $\varphi_C$, $\varphi_B$ und $\varphi_E$ der Anschlüsse. Man ergänzt das Basispotenzial:

$$U_{CE} = \varphi_C - \varphi_E = (\varphi_C - \varphi_B) + (\varphi_B - \varphi_E) = U_{CB} + U_{BE}$$

**Ergebnis:**

$$I_E = I_B + I_C$$

$$U_{CE} = U_{CB} + U_{BE}$$

**Woher die Faktoren kommen:** Alle Faktoren sind 1, weil Ladung erhalten bleibt und Potenzialdifferenzen sich addieren; die Vorzeichen folgen aus den Zählpfeilen.

**Proben:** Einheit A bzw. V. Im Normalbetrieb sind Basis- und Kollektorstrom positiv, der Emitterstrom ist also größer als jeder von beiden.

**Grenzen:** An den Bahnwiderständen der Gebiete fallen bei großen Strömen kleine Spannungen ab; die Spannung direkt am Übergang ist dann etwas kleiner als die Klemmenspannung.
:::

## Der Transistoreffekt

*Warum fließt durch den gesperrten Basis-Kollektor-Übergang ein großer Strom, und warum legt ihn $U_{BE}$ fest?*

:::grafik
Szene: get1/bipolartransistoren/01-transistoreffekt · Vorlage: banddiagramm-abfolge
**Abbildung 3:** (a) Leitungsbandkante $W_L$ entlang des Beispieltransistors ohne äußere Spannung: Stufe von 0,95 eV zwischen Emitter und Basis, 0,77 eV zwischen Basis und Kollektor. (b) Normalbetrieb mit $U_{BE}$ = 0,65 V und $U_{CB}$ = 5 V: Die erste Stufe ist auf 0,30 eV abgesenkt, die zweite auf 5,77 eV vertieft (Achse unterbrochen); Elektronen (blau) kommen über die abgesenkte Stufe, diffundieren durch die Basis und fallen am Basis-Kollektor-Übergang hinab. (c) Elektronendichte in der Basis über dem Ort: am Emitterrand 8,3·10¹³ cm⁻³, am Kollektorrand null, dazwischen eine Gerade; gestrichelt bei 0,70 V mit 5,7·10¹⁴ cm⁻³. Die Stufe am Emitter bestimmt, wie viele Elektronen kommen; die Kante am Kollektor sammelt sie alle ein.
:::

**Die Akteure:**

- __$n(x)$__: Elektronendichte in der Basis am Ort $x$; in cm⁻³. Bei $x$ = 0 grenzt die neutrale Basis an die Basis-Emitter-Zone, bei $x$ = $w_B$ an die Basis-Kollektor-Zone. Die Elektronen sind dort Minoritätsträger neben 10¹⁷ Löchern pro cm³.
- __$n_{B0}$__: Elektronendichte der Basis im Gleichgewicht, nach dem Massenwirkungsgesetz $n_i^2/N_B$ mit der Eigenleitungsdichte $n_i$ = 10¹⁰ cm⁻³ und der Basisdotierung $N_B$; 10³ cm⁻³.
- __$w_B$__: Weite der neutralen Basis; 0,5 µm.
- __$D_n$__: __Diffusionskonstante__ der Elektronen in der Basis; 20,7 cm²/s. Sie misst, wie schnell die Wärmebewegung einen Dichteunterschied ausgleicht.
- __$L_n$__: __Diffusionslänge__, die Strecke, die ein Elektron diffundiert, bevor es nach seiner __Lebensdauer__ $\tau_n$ von 80 ns mit einem Loch rekombiniert; 12,9 µm, 26-mal die Basisweite.
- __$U_T$__: __Temperaturspannung__ $k_B T/e$; 25,85 mV bei 300 K.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Im __aktiven Bereich__, dem Normalbetrieb, leitet der Basis-Emitter-Übergang mit $U_{BE}$ um 0,65 V, und der Basis-Kollektor-Übergang sperrt mit einigen Volt. In Abbildung 3b ist die Stufe vor der Basis dadurch von 0,95 auf 0,30 eV gesunken, die Stufe zum Kollektor auf 5,77 eV gewachsen.

**Schritt 2**: Über die gesenkte Stufe kommen Elektronen aus dem Emitter in die Basis, wie bei der Diode um den Boltzmann-Faktor $\exp(U_{BE}/U_T)$ mehr als im Gleichgewicht. Bei 0,65 V steigt die Elektronendichte am Emitterrand der Basis von 10³ auf 8,3·10¹³ cm⁻³; das sind 0,08 % der Löcherdichte.

**Schritt 3**: In der feldfreien Basis wandern die Elektronen durch __Diffusion__ weiter, die ungeordnete Wärmebewegung, die im Mittel Teilchen von dichten zu dünnen Stellen trägt. Weil die Basis 26-mal dünner ist als die Diffusionslänge, kommt fast jedes Elektron an ihrem anderen Ende an.

**Schritt 4**: Dort zieht das Feld des gesperrten Basis-Kollektor-Übergangs jedes Elektron in den Kollektor; am Kollektorrand der Basis ist die Elektronendichte praktisch null. Das ist der Sperrstrom der Diode mit einem riesigen Nachschub: Statt der Wärme liefert hier der Emitter die Minoritätsträger, bei 0,65 V 8·10¹⁰-mal so viele, wie die Wärme in der Basis bereitstellt.

**Schritt 5**: Zwischen den Rändern fällt die Dichte geradlinig ab (Abbildung 3c). Der Diffusionsstrom ist proportional zu diesem Gefälle, also zur Randdichte am Emitter, die exponentiell mit $U_{BE}$ wächst. Wie tief die Kante ist, spielt keine Rolle: Bei 5 V wie bei 10 V Sperrspannung bleibt die Dichte am Kollektorrand null. Zwischen 1 und 10 V steigt der Kollektorstrom des Beispieltransistors deshalb nur um 13 %, weil die Basis mit wachsender Sperrspannung etwas dünner wird (Early-Effekt).

Daraus folgt die __Transfergleichung__:

:::formel Gesetz
$$I_C = I_S\,\exp\!\Big(\frac{U_{BE}}{U_T}\Big)$$
:::

**So liest man das:** Die Basis-Emitter-Spannung legt den Kollektorstrom fest. Der __Sättigungsstrom__ $I_S$, beim Beispieltransistor 10⁻¹⁴ A, ist der Vorfaktor, anschaulich der Teil des Sperrstroms, den bei $U_{BE}$ = 0 die thermischen Elektronen der Basis tragen; er wächst mit der Emitterfläche und sinkt mit Dotierung und Weite der Basis. Je 17,9 mV mehr verdoppelt sich der Strom, je 59,5 mV verzehnfacht er sich. Die Kollektorspannung kommt nicht vor, solange der Basis-Kollektor-Übergang sperrt.

Idee der Herleitung: Der Boltzmann-Faktor legt die Randdichte am Emitter fest; das geradlinige Profil in der dünnen Basis macht daraus einen Diffusionsstrom.

:::herleitung
**Ausgangspunkt:** die Boltzmann-Verteilung und das Massenwirkungsgesetz aus [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html), dazu das __Ficksche Gesetz__ der Diffusion: Durch eine Fläche $A$ diffundieren je Sekunde $D_n$ mal Dichtegefälle mal Fläche Elektronen, von hoher zu niedriger Dichte. Als elektrischer Strom:

$$I_\mathrm{Diff} = e\,A\,D_n\,\Big|\frac{\mathrm{d}n}{\mathrm{d}x}\Big|$$

**Annahmen:**
(i) aktiver Bereich: $U_{BE}$ ist viel größer als $U_T$, der Basis-Kollektor-Übergang sperrt mit einigen Zehntelvolt oder mehr;
(ii) schwache Injektion: Die Elektronendichte bleibt klein gegen die Löcherdichte der Basis; beim Beispieltransistor erreicht sie erst bei 100 mA 10 %;
(iii) die neutrale Basis ist feldfrei und viel dünner als die Diffusionslänge, das Verhältnis ist 0,04;
(iv) über die Basis-Emitter-Zone hinweg bleiben die Elektronen Boltzmann-verteilt, wie bei der Herleitung der Diodenkennlinie.

**Schritt 1**: Im Gleichgewicht folgt die Elektronendichte der Basis aus dem Massenwirkungsgesetz, weil dort die Löcherdichte gleich der Dotierung $N_B$ ist:

$$n_{B0} = \frac{n_i^2}{N_B}$$

**Schritt 2**: Mit $U_{BE}$ ist die Stufe zwischen Emitter und Basis um $e\,U_{BE}$ niedriger als im Gleichgewicht. Nach (ii) und (iv) wächst die Dichte am Emitterrand der Basis um den Boltzmann-Faktor dieser Absenkung:

$$n(0) = n_{B0}\,\exp\!\Big(\frac{U_{BE}}{U_T}\Big)$$

**Schritt 3**: Am Kollektorrand ist die Stufe um $e\,U_{CB}$ höher als im Gleichgewicht, die Dichte dort also um den Faktor $\exp(-U_{CB}/U_T)$ kleiner, bei 5 V um 10⁻⁸⁴. Nach (i) gilt deshalb

$$n(w_B) \approx 0$$

**Schritt 4**: Nach (iii) geht in der Basis kein Elektron verloren; durch jeden Querschnitt fließt derselbe Strom. Nach dem Fickschen Gesetz ist dann das Gefälle überall gleich, und das Profil ist eine Gerade:

$$n(x) = n(0)\,\Big(1 - \frac{x}{w_B}\Big)$$

**Schritt 5** (entscheidender Schritt): Das Gefälle hat den Betrag $n(0)/w_B$. Die Elektronen diffundieren zum Kollektor; der technische Strom fließt entgegengesetzt, vom Kollektor durch die Basis zum Emitter, und ist der Kollektorstrom:

$$I_C = e\,A\,D_n\,\frac{n(0)}{w_B}$$

**Schritt 6**: Schritt 1 und Schritt 2 eingesetzt:

$$I_C = \frac{e\,A\,D_n\,n_i^2}{N_B\,w_B}\,\exp\!\Big(\frac{U_{BE}}{U_T}\Big)$$

**Ergebnis:**

$$I_C = I_S\,\exp\!\Big(\frac{U_{BE}}{U_T}\Big)$$

**Woher die Faktoren kommen:** Der Exponentialfaktor ist der Boltzmann-Faktor der abgesenkten Stufe (Schritt 2). Der Sättigungsstrom ist der Vorfaktor aus Schritt 6:

$$I_S = \frac{e\,A\,D_n\,n_i^2}{N_B\,w_B}$$

Darin ist $n_i^2/N_B$ die Elektronendichte der Basis im Gleichgewicht, und $D_n/w_B$ macht aus einer Dichte einen Strom. Eine dünne, schwach dotierte Basis und eine große Fläche ergeben einen großen Sättigungsstrom. $U_{CB}$ fehlt, weil die Dichte am Kollektorrand für jede Sperrspannung null ist (Schritt 3).

**Proben:** Einheit: C mal cm² mal cm²/s mal cm⁻⁶, geteilt durch cm⁻³ mal cm, ergibt C/s, also A. Zahlenwert mit $e$ = 1,602·10⁻¹⁹ C, der Emitterfläche 1,5·10⁻⁴ cm² des Beispieltransistors, $D_n$ = 20,7 cm²/s, $n_i$ = 10¹⁰ cm⁻³, $N_B$ = 10¹⁷ cm⁻³ und $w_B$ = 0,5 µm:

$$e\,A\,D_n\,n_i^2 = 0{,}0497\ \mathrm{A/cm^2}, \qquad N_B\,w_B = 5\cdot10^{12}\ \mathrm{cm^{-2}}, \qquad I_S = 0{,}99\cdot10^{-14}\ \mathrm{A}$$

Grenzfall: Bei $U_{BE}$ = 0 bleibt der Sättigungsstrom übrig, der Anteil des Sperrstroms, den die thermischen Elektronen der Basis tragen; im realen Sperrstrom kommen Löcher aus dem Kollektor und Ladungsträger hinzu, die in der Sperrschicht entstehen.

**Grenzen:** Bei starker Injektion, wenn die Elektronendichte in die Nähe der Löcherdichte kommt, wächst der Strom langsamer als exponentiell. Leitet auch der Basis-Kollektor-Übergang, ist die Dichte am Kollektorrand nicht mehr null (Abschnitt *Die Arbeitsbereiche*). Die Rekombination in der Basis, hier vernachlässigt, macht den Kollektorstrom um 0,08 % kleiner als den Elektronenstrom am Emitter.
:::

::::beispiel Kollektorstrom des Beispieltransistors
**Gegeben:** Beispieltransistor mit $I_S$ = 10⁻¹⁴ A und $n_{B0}$ = 10³ cm⁻³; $U_T$ = 25,85 mV bei 300 K.

**Gesucht:** Kollektorstrom bei 0,65 V und 0,70 V, die Spannung für 2 mA und die Randdichte bei 0,65 V.

**Rechnung:** Bei 0,65 V:

$$I_C = 10^{-14}\ \mathrm{A}\cdot\exp\!\Big(\frac{0{,}65\ \mathrm{V}}{25{,}85\ \mathrm{mV}}\Big) = 10^{-14}\ \mathrm{A}\cdot8{,}31\cdot10^{10} = 0{,}831\ \mathrm{mA}$$

Bei 0,70 V ergeben sich ebenso 5,75 mA. Nach $U_{BE}$ aufgelöst und die Randdichte:

$$U_{BE} = U_T\,\ln\frac{2\ \mathrm{mA}}{10^{-14}\ \mathrm{A}} = 0{,}673\ \mathrm{V}, \qquad n(0) = 10^{3}\ \mathrm{cm^{-3}}\cdot8{,}31\cdot10^{10} = 8{,}3\cdot10^{13}\ \mathrm{cm^{-3}}$$

**Ergebnis:** **0,831 mA bei 0,65 V, 5,75 mA bei 0,70 V; 0,673 V für 2 mA; Randdichte 8,3·10¹³ cm⁻³.**

**Einordnung:** 50 mV mehr ergeben fast den siebenfachen Strom, 1 mV schon 3,9 %. Das Datenblatt des BC547C nennt für 2 mA 0,55 bis 0,70 V; der Beispieltransistor liegt mit 0,673 V darin.
::::

:::frage
„Ein Transistor enthält zwei pn-Übergänge. Kann man ihn aus zwei Dioden zusammenlöten?“
Nein. Die Elektronen, die die erste Diode in ihr p-Gebiet schickt, rekombinieren dort, im Mittel nach einer Diffusionslänge von einigen 10 µm und spätestens am Metallkontakt. Bei der zweiten Diode kommt keines an; durch den Draht fließt nur ein gewöhnlicher Strom, der ihrem gesperrten Übergang keinen Nachschub an Minoritätsträgern bringt. Der Transistoreffekt verlangt zwei Übergänge in einem Kristall, viel enger beieinander als eine Diffusionslänge.
:::

## Der Basisstrom und die Stromverstärkung

*Woher kommt der Basisstrom, und warum ist er 500-mal kleiner als der Kollektorstrom?*

:::grafik
Szene: get1/bipolartransistoren/01-stromaufteilung · Vorlage: stromfluss-bilanz
**Abbildung 4:** Bilanz der Ladungsträger im aktiven Bereich, bezogen auf 10 000 Elektronen, die am Kollektor ankommen: Der Emitter schickt 10 007,6 Elektronen in die Basis, 7,6 davon rekombinieren dort; zugleich gehen 12,5 Löcher aus der Basis in den Emitter. Über den Basisanschluss kommen 20,1 Löcher nach. Kollektor- und Basisstrom stehen im Verhältnis 10 000 zu 20, also rund 500 zu 1.
:::

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Die Elektronen des Kollektorstroms kommen aus dem Emitter und verlassen den Transistor am Kollektor; keines fließt über den Basisanschluss (Abbildung 1). Über ihn kommen Löcher, so viele, wie der Basis verloren gehen.

**Schritt 2**: Die gesenkte Stufe lässt auch Löcher aus der Basis in den Emitter, die __Rückinjektion__. Weil der Emitter 100-mal stärker dotiert ist als die Basis, sind es auf 10 000 Elektronen am Kollektor nur 12,5 Löcher (Abbildung 4).

**Schritt 3**: Unterwegs rekombinieren einige Elektronen mit Löchern der Basis. Ein Elektron braucht für die 0,5 µm im Mittel 60 ps und lebt 80 ns; auf 10 000 ankommende Elektronen rekombinieren deshalb 7,6.

**Schritt 4**: Beide Verluste hängen an derselben Stufe, die Rückinjektion als Löcherstrom über sie, die Rekombination als Bruchteil des Elektronenstroms, der über sie kommt. Beide wachsen deshalb mit demselben Faktor $\exp(U_{BE}/U_T)$ wie der Kollektorstrom, und der Basisstrom ist ein fester Bruchteil davon, 20 auf 10 000.

Dieses Verhältnis ist die Kennzahl des Transistors:

:::formel Definition
$$B = \frac{I_C}{I_B}$$
:::

**So liest man das:** Die __Stromverstärkung__ $B$ (das Formelzeichen, nicht der Anschlussname) gibt an, wie viel größer der Kollektor- als der Basisstrom ist; beim Beispieltransistor 500, beim BC547C nach Datenblatt 420 bis 800. Man definiert sie so, weil das Verhältnis im aktiven Bereich über einen weiten Strombereich fast konstant ist, beim Beispieltransistor auf 10 % genau zwischen 0,3 und 20 mA. Weil der Basisstrom nur ein kleiner Rest ist, 0,2 % des Emitterstroms, streut $B$ stark: Ein Rest von 0,4 % ergäbe nur 249. Hersteller sortieren Transistoren deshalb in Gruppen, beim BC547 von A (110 bis 220) bis C (420 bis 800).

:::frage
„Wenn der Basisstrom den Kollektorstrom nicht verursacht, wozu braucht man ihn dann? Was geschieht bei offener Basis?“
Ohne Nachschub verliert die Basis ständig Löcher, an den Emitter und durch Rekombination. Sie lädt sich negativ auf, die Spannung am Basis-Emitter-Übergang sinkt, die Stufe wächst, und es kommen weniger Elektronen, bis Verlust und Nachschub wieder gleich sind. Bei offener Basis bleibt nur ein Leckstrom, um viele Zehnerpotenzen kleiner als im Betrieb. Der Basisstrom ersetzt also die verlorenen Löcher und hält den Zustand aufrecht, den $U_{BE}$ beschreibt; er ist der Preis des Betriebs, nicht seine Ursache.
:::

## Strom- oder Spannungssteuerung

*Steuert der Basisstrom oder die Basis-Emitter-Spannung den Kollektorstrom?*

Physikalisch steuert die Spannung: $U_{BE}$ legt die Stufe fest und damit, wie viele Elektronen in die Basis gelangen. Das Skript beschreibt den Transistor trotzdem als __stromgesteuerte Stromquelle__, deren Kollektorstrom das $B$-Fache des Basisstroms ist (S. 175). Beides passt zusammen, denn der Basisstrom folgt demselben Exponentialgesetz; geteilt durch $B$ wird aus der Transfergleichung die __Eingangskennlinie__:

:::formel Formel
$$I_B = \frac{I_S}{B}\,\exp\!\Big(\frac{U_{BE}}{U_T}\Big)$$
:::

**So liest man das:** Die Eingangskennlinie ist eine Diodenkennlinie mit dem Sättigungsstrom $I_S/B$; zu jedem Basisstrom gehört genau eine Spannung, zu 4 µA beim Beispieltransistor 0,673 V. Wer also den Basisstrom erzwingt, legt damit auch $U_{BE}$ und den Kollektorstrom fest, 2 mA. Weil sich $U_{BE}$ für Handrechnungen kaum ändert, 60 mV je Zehnfaches des Stroms, ersetzt die Vorlesung den Basis-Emitter-Übergang durch eine feste Spannung, und der Basisstrom bleibt als einfache, lineare Stellgröße.

Idee der Herleitung: Man teilt die Transfergleichung durch $B$.

:::herleitung
**Ausgangspunkt:** die Transfergleichung und die Definition von $B$.

**Annahmen:** (i) aktiver Bereich; (ii) $B$ hängt nicht vom Strom ab; auf 10 % genau gilt das zwischen etwa 0,3 und 20 mA (Abschnitt *Die Kennlinien*).

**Schritt 1** (entscheidender Schritt): Nach der Definition von $B$ ist der Basisstrom der Kollektorstrom geteilt durch $B$, und nach (ii) ist $B$ eine Konstante:

$$I_B = \frac{I_C}{B} = \frac{I_S}{B}\,\exp\!\Big(\frac{U_{BE}}{U_T}\Big)$$

**Ergebnis:**

$$I_B = \frac{I_S}{B}\,\exp\!\Big(\frac{U_{BE}}{U_T}\Big)$$

**Woher die Faktoren kommen:** Der Exponentialfaktor stammt aus der Stufe am Basis-Emitter-Übergang, $1/B$ aus den beiden Verlusten (Abschnitt *Der Basisstrom und die Stromverstärkung*).

**Proben:** Einheit A. Bei 0,65 V: 10⁻¹⁴ A mal 8,31·10¹⁰ durch 500 ergibt 1,66 µA.

**Grenzen:** Bei sehr kleinen Strömen ist der Basisstrom größer als nach dieser Formel, weil Ladungsträger auch in der Basis-Emitter-Zone rekombinieren.
:::

:::fehlvorstellung
„Der Basisstrom öffnet den Transistor wie ein Ventil; die Elektronen des Kollektorstroms kommen über die Basis herein.“
Das legen das Wort Steuerstrom und die Wasseranalogie des Skripts nahe (S. 176, Bild 11.2), in der ein Wasserstrahl aus der Basis eine Klappe aufdrückt. Die Elektronen des Kollektorstroms kommen aber aus dem Emitter und gehen nie über den Basisanschluss (Abbildung 1); über ihn fließen nur Löcher für die Verluste, bei 2 mA Kollektorstrom 4 µA. Als Rechenmodell bleibt die Stromsicht richtig, weil der Basisstrom eindeutig mit $U_{BE}$ verknüpft ist.
:::

## Die Kennlinien

*Wie liest man Eingangs-, Steuer- und Ausgangskennlinie eines Transistors?*

:::grafik
Szene: get1/bipolartransistoren/01-kennlinien · Vorlage: kennlinien-drei
**Abbildung 5:** Kennlinien des Beispieltransistors, berechnet. (a) Eingangskennlinie bei $U_{CE}$ = 5 V: $I_B$ über $U_{BE}$ von 0,5 bis 0,75 V, 20 µA bei 0,714 V. (b) Stromsteuerkennlinie doppelt logarithmisch: $I_C$ über $I_B$ von 1 nA bis 1 mA, eine Gerade der Steigung 1, um den Faktor 500 über der Diagonalen; bei kleinen und großen Strömen sinkt $B$ (an das Datenblatt des BC547C angepasst: 260 bei 10 µA, 500 bei 2 mA, 285 bei 100 mA Kollektorstrom). (c) Ausgangskennlinienfeld: $I_C$ über $U_{CE}$ von 0 bis 10 V für $I_B$ = 2, 4, 6, 8 und 10 µA; oberhalb von etwa 0,3 V fast waagrecht mit leichtem Anstieg (für 4 µA 1,88 mA bei 0,5 V, 2,00 mA bei 5 V, 2,13 mA bei 10 V), darunter steiler Abfall; markiert $U_{CE,\mathrm{sat}}$ = 0,2 V und die Grenzlinie $U_{CB}$ = 0 bei 0,65 bis 0,70 V. Eine Diodenkennlinie am Eingang, eine Gerade dazwischen, Stromquellenäste am Ausgang.
:::

Das Skript beschreibt den Transistor mit drei Kennlinien (S. 176, Bild 11.3 auf S. 177). Die **Eingangskennlinie** (Abbildung 5a) ist die Diodenkennlinie aus dem vorigen Abschnitt; auf linearer Achse scheint sie bei etwa 0,6 V einzusetzen, das Skript nennt diesen Wert $U_{BE,\mathrm{ein}}$. Eine Schwelle gibt es nicht: Bei 0,55 V fließen schon 35 nA Basisstrom und 17 µA Kollektorstrom.

Die **Stromsteuerkennlinie** (Abbildung 5b) ist im mittleren Bereich eine Gerade mit der Steigung $B$. Trägt man sie doppelt logarithmisch auf wie das Skript (Bild 11.3b), hat sie die Steigung 1, und $B$ ist ihr senkrechter Abstand von der Diagonalen. Dass sie bei großen Strömen abbiegt, nennt das Skript „Sättigung“; was das Bild dort zeigt, ist ein Rückgang von $B$ bei hohen Stromdichten, beim BC547C von typisch 520 bei 2 mA auf 300 bei 100 mA, nicht der Sättigungsbereich des nächsten Abschnitts.

Die **Ausgangskennlinien** (Abbildung 5c) verlaufen oberhalb von etwa 0,3 V fast waagrecht: Der Transistor wirkt als Stromquelle, deren Strom die Basisseite vorgibt. Unterhalb von etwa 0,2 V fallen sie steil ab, weil der Basis-Kollektor-Übergang zu leiten beginnt.

## Die Arbeitsbereiche

*Was geschieht, wenn der Basis-Kollektor-Übergang nicht mehr sperrt, und wie findet man den Bereich eines Transistors?*

Jeder der beiden Übergänge kann leiten oder sperren:

| Bereich und Übergänge | Verhalten |
|---|---|
| aktiver Bereich: Basis-Emitter-Übergang leitet, Basis-Kollektor-Übergang sperrt | Stromquelle mit $B$-fachem Basisstrom; Verstärker |
| Sättigung: beide Übergänge leiten | $U_{CE}$ nur 0,1 bis 0,2 V, den Strom begrenzt der äußere Kreis; Schalter ein |
| Sperrbereich: beide Übergänge sperren | fast kein Strom; Schalter aus |
| Inversbetrieb: nur der Basis-Kollektor-Übergang leitet | Emitter und Kollektor vertauscht; selten genutzt |

Für Handrechnungen gibt das Skript jedem Bereich ein Modell (S. 176), mit $U_{BE,\mathrm{ein}}$ = 0,6 V und der __Sättigungsspannung__ $U_{CE,\mathrm{sat}}$ = 0,2 V. Wie bei der Diode nimmt man einen Bereich an, rechnet mit seinem Modell und prüft die Bedingung:

| Bereich | Modell | Probe |
|---|---|---|
| Sperrbereich | $I_B$ = $I_C$ = 0 | $U_{BE}$ < 0,6 V |
| aktiv | $U_{BE}$ = 0,6 V, $I_C$ = $B\,I_B$ | $U_{CE}$ ≥ 0,2 V |
| Sättigung | $U_{BE}$ = 0,6 V, $U_{CE}$ = 0,2 V | $I_C$ ≤ $B\,I_B$ |

:::grafik
Szene: get1/bipolartransistoren/01-arbeitsgerade · Vorlage: kennlinienfeld-arbeitsgerade
**Abbildung 6:** Modellkennlinien des Beispieltransistors nach dem Skript ($B$ = 500, waagrecht ab $U_{CE,\mathrm{sat}}$ = 0,2 V) für $I_B$ = 2, 8 und 20 µA, dazu die Arbeitsgerade eines Kollektorwiderstands von 2,2 kΩ an 10 V von (10 V, 0) nach (0, 4,55 mA). Arbeitspunkte: 2 µA bei 7,8 V und 1,0 mA (aktiv), 8 µA bei 1,2 V und 4,0 mA (aktiv), 20 µA bei 0,2 V und 4,45 mA (Sättigung; die Modellkennlinie läge bei 10 mA). Die Bereiche sind farbig hinterlegt. Ab 8,9 µA bleibt der Arbeitspunkt in der Sättigung stehen; mehr Basisstrom ändert den Kollektorstrom nicht.
:::

**Die Akteure:**

- __$U_{CC}$__, __$R_C$__: Versorgungsspannung und Kollektorwiderstand des Kollektorkreises; 10 V und 2,2 kΩ im Beispiel.
- __$U_{BC}$__: Spannung von der Basis zum Kollektor, der Gegenwert von $U_{CB}$; positiv, wenn der Basis-Kollektor-Übergang in Durchlassrichtung liegt.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Was am Kollektorwiderstand abfällt, fehlt an $U_{CE}$; alle möglichen Arbeitspunkte liegen auf der __Arbeitsgeraden__ in Abbildung 6. Mehr Basisstrom bringt im aktiven Bereich $B$-mal mehr Kollektorstrom und senkt $U_{CE}$: Bei 8 µA bleiben 1,2 V.

**Schritt 2**: Sinkt $U_{CE}$ unter $U_{BE}$, liegt der Kollektor tiefer als die Basis. Ab etwa 0,5 V Durchlassspannung, also ab $U_{CE}$ um 0,2 V, leitet der Basis-Kollektor-Übergang merklich und lässt Löcher aus der Basis in den schwach dotierten Kollektor.

**Schritt 3**: Damit teilt sich der Basisstrom: Ein Teil ersetzt die Verluste durch Rückinjektion und Rekombination, der Rest fließt über den Basis-Kollektor-Übergang ab, bei 20 µA Basisstrom 9,6 und 10,4 µA. Der Kollektorstrom wächst nicht mehr mit und bleibt bei dem Wert, den der Kollektorkreis zulässt, rund 4,5 mA statt 10 mA. Daher der Name __Sättigung__.

**Schritt 4**: $U_{CE}$ ist jetzt der Unterschied zweier Durchlassspannungen, $U_{BE}$ minus $U_{BC}$, beim Beispieltransistor 0,696 V minus 0,552 V, also 0,144 V. Das Skript rechnet mit 0,2 V.

Strom und Grenze der Sättigung folgen aus der Maschenregel des Kollektorkreises:

:::formel Formel
$$I_{C,\mathrm{sat}} = \frac{U_{CC} - U_{CE,\mathrm{sat}}}{R_C}, \qquad I_B \ge \frac{I_{C,\mathrm{sat}}}{B}$$
:::

**So liest man das:** Der Kollektorkreis bestimmt den Strom in der Sättigung, und ab dem Basisstrom $I_{C,\mathrm{sat}}/B$ ist sie erreicht; mehr Basisstrom ändert nichts mehr. Mit 10 V, 2,2 kΩ und $B$ = 500 sind es 4,45 mA ab 8,9 µA.

Idee der Herleitung: Maschenregel mit dem Sättigungsmodell, dann die Bedingung der Sättigung nach dem Basisstrom aufgelöst.

:::herleitung
**Ausgangspunkt:** die Maschenregel und das Modell der Sättigung aus der Tabelle.

**Annahmen:** (i) In der Sättigung gilt das Modell des Skripts, $U_{CE}$ = 0,2 V; (ii) der Kollektorkreis besteht aus $U_{CC}$ und $R_C$.

**Schritt 1**: Maschenregel im Kollektorkreis:

$$U_{CC} = R_C\,I_C + U_{CE}$$

**Schritt 2**: In der Sättigung nach (i) eingesetzt und nach dem Strom aufgelöst:

$$I_{C,\mathrm{sat}} = \frac{U_{CC} - U_{CE,\mathrm{sat}}}{R_C}$$

**Schritt 3** (entscheidender Schritt): Die Bedingung der Sättigung verlangt, dass der Transistor mindestens diesen Strom liefern könnte, dass also $B$ mal Basisstrom nicht kleiner ist als $I_{C,\mathrm{sat}}$. Nach dem Basisstrom aufgelöst:

$$I_B \ge \frac{I_{C,\mathrm{sat}}}{B}$$

**Ergebnis:**

$$I_{C,\mathrm{sat}} = \frac{U_{CC} - U_{CE,\mathrm{sat}}}{R_C}, \qquad I_B \ge \frac{I_{C,\mathrm{sat}}}{B}$$

**Woher die Faktoren kommen:** $U_{CC} - U_{CE,\mathrm{sat}}$ ist die Spannung, die für den Widerstand bleibt; $1/B$ übersetzt Kollektor- in Basisstrom.

**Proben:** Einheit A. Grenzfall: Ohne Kollektorwiderstand begrenzt nichts den Strom, $I_{C,\mathrm{sat}}$ wird unendlich, und der Transistor erreicht die Sättigung nie. Zahlenwert: 9,8 V durch 2,2 kΩ ergibt 4,455 mA, geteilt durch 500 ergibt 8,91 µA.

**Grenzen:** Die Sättigungsspannung hängt in Wirklichkeit vom Strom und vom Verhältnis der Ströme ab; im Beispiel ergibt das vollständige Modell 0,144 V statt 0,2 V, der Kollektorstrom ändert sich dadurch nur um 0,6 %.
:::

::::beispiel Ein Transistor an 10 V und 2,2 kΩ in allen drei Bereichen
**Gegeben:** Beispieltransistor mit $B$ = 500, Kollektor über $R_C$ = 2,2 kΩ an $U_{CC}$ = 10 V, Emitter an Masse; eine Stromquelle gibt 0, 2, 8 oder 20 µA in die Basis. Modellwerte 0,6 V und 0,2 V.

**Gesucht:** Bereich, Kollektorstrom und $U_{CE}$.

**Rechnung:** Ohne Basisstrom sperrt der Transistor, $U_{CE}$ = 10 V. Bei 2 µA und 8 µA, Annahme aktiv:

$$I_C = 500\cdot2\ \mu\mathrm{A} = 1{,}00\ \mathrm{mA},\ U_{CE} = 7{,}8\ \mathrm{V}, \qquad I_C = 4{,}00\ \mathrm{mA},\ U_{CE} = 10\ \mathrm{V} - 8{,}8\ \mathrm{V} = 1{,}2\ \mathrm{V}$$

Beide Male mehr als 0,2 V; die Annahme hält. Bei 20 µA verlangte die Annahme aktiv 10 mA, also 22 V am Widerstand und $U_{CE}$ = −12 V, ein Widerspruch. Annahme Sättigung:

$$I_C = \frac{10\ \mathrm{V} - 0{,}2\ \mathrm{V}}{2{,}2\ \mathrm{k\Omega}} = 4{,}46\ \mathrm{mA} \le 500\cdot20\ \mu\mathrm{A} = 10\ \mathrm{mA}$$

**Ergebnis:** **0 µA gesperrt; 2 µA aktiv mit 1,00 mA bei 7,8 V; 8 µA aktiv mit 4,00 mA bei 1,2 V; 20 µA gesättigt mit 4,45 mA bei 0,2 V.**

**Einordnung:** Ab 8,9 µA steigt der Kollektorstrom nicht mehr. Bei 20 µA ist der Transistor 2,2-fach übersteuert; das vollständige Modell des Zahlenwerks ergibt 0,144 V und 4,48 mA, die einfache Rechnung trifft den Strom also gut.
::::

:::frage
„Warum liegt die Grenze bei 0,2 V und nicht dort, wo $U_{CB}$ null wird?“
Bei $U_{CB}$ = 0, mit 8 µA Basisstrom bei 0,69 V, liegt am Basis-Kollektor-Übergang keine Spannung: Er sammelt die Elektronen weiter ein, schickt aber selbst nichts zurück. In Durchlassrichtung leitet ein pn-Übergang merklich erst ab etwa 0,45 bis 0,5 V, und dann ist $U_{CE}$ auf 0,2 bis 0,25 V gesunken. Beim Beispieltransistor fließen bei 0,3 V erst 0,25 % des Basisstroms über den Basis-Kollektor-Übergang ab, bei 0,25 V 1,7 %, bei 0,2 V 11 %. Oberhalb von etwa 0,25 V arbeitet der Transistor deshalb praktisch wie im aktiven Bereich.
:::

:::fehlvorstellung
„In der Sättigung liefert der Transistor seinen größten Strom.“
Das liegt nahe, weil Sättigung im Alltag „mehr geht nicht“ bedeutet. Den Strom begrenzt aber der Kollektorkreis: Im Beispiel könnte der Transistor mit 20 µA Basisstrom 10 mA liefern, der Widerstand lässt nur 4,45 mA zu, und mit einem kleineren Widerstand flösse beim selben Basisstrom mehr. Kennzeichen der Sättigung sind die kleine Spannung $U_{CE}$ und ein Kollektorstrom unter $B\,I_B$.
:::

## Der Transistor als Schalter

*Wie viel Basisstrom braucht ein Transistor, damit er sicher durchschaltet?*

Als __Schalter__ wechselt der Transistor zwischen Sperrbereich und Sättigung (Skript, S. 175 und 178): gesperrt fast kein Strom, gesättigt nur 0,1 bis 0,2 V, in beiden Zuständen wenig Verlustleistung und kein Verschleiß. Sicher gesättigt ist er, wenn die Sättigungsbedingung auch für das kleinste $B$ seines Typs gilt, beim BC547C 420 bei 2 mA; weil $B$ bei größeren Strömen sinkt und mit Temperatur und Alterung schwankt, gibt man das Zwei- bis Fünffache, die __Übersteuerung__.

::::beispiel Leuchtdiode an einem 3,3-V-Mikrocontroller
**Gegeben:** Mikrocontroller-Ausgang mit 3,3 V; rote Leuchtdiode mit 2,0 V bei 20 mA an 5 V; BC547C mit $B_\mathrm{min}$ = 420; Modellwerte 0,2 V und $U_{BE}$ = 0,7 V; Übersteuerung fünffach; Normreihe E12.

:::grafik
Szene: get1/bipolartransistoren/01-led-schalter · Vorlage: schaltplan
**Abbildung 7:** Schaltplan: Mikrocontroller-Ausgang (3,3 V) über $R_B$ = 12 kΩ an die Basis eines BC547C, Emitter an Masse; vom Kollektor über $R_C$ = 150 Ω und die Leuchtdiode an +5 V. Eingetragen: Basisstrom 0,217 mA, Kollektorstrom 18,7 mA, $U_{CE}$ um 0,1 V. Ein Ausgangsstrom von einem Prozent des Laststroms schaltet die Leuchtdiode.
:::

**Gesucht:** $R_C$, $R_B$ und Basisstrom.

**Rechnung:** Kollektorwiderstand und Laststrom (Abbildung 7):

$$R_C = \frac{5\ \mathrm{V} - 2{,}0\ \mathrm{V} - 0{,}2\ \mathrm{V}}{20\ \mathrm{mA}} = 140\ \Omega \;\rightarrow\; 150\ \Omega, \qquad I_C = \frac{2{,}8\ \mathrm{V}}{150\ \Omega} = 18{,}7\ \mathrm{mA}$$

Basisstrom mit fünffacher Übersteuerung und Basiswiderstand:

$$I_B = 5\cdot\frac{18{,}7\ \mathrm{mA}}{420} = 0{,}222\ \mathrm{mA}, \qquad R_B = \frac{3{,}3\ \mathrm{V} - 0{,}7\ \mathrm{V}}{0{,}222\ \mathrm{mA}} = 11{,}7\ \mathrm{k\Omega} \;\rightarrow\; 12\ \mathrm{k\Omega}$$

Mit dem Normwert fließt

$$I_B = \frac{2{,}6\ \mathrm{V}}{12\ \mathrm{k\Omega}} = 0{,}217\ \mathrm{mA}$$

**Ergebnis:** **150 Ω und 12 kΩ; der Ausgang liefert 0,217 mA, der Transistor schaltet 18,7 mA.**

**Einordnung:** Der Ausgang liefert ein Prozent des Laststroms. Im Transistor werden mit den Modellwerten rund 3,9 mW zu Wärme, 3,7 mW im Kollektorkreis und 0,15 mW an der Basis-Emitter-Strecke; das vollständige Modell ergibt bei dieser Übersteuerung 0,11 V und zusammen 2,3 mW.
::::

## Der pnp-Transistor

*Was ändert sich, wenn man die Dotierfolge umkehrt?*

Beim pnp-Transistor sind Emitter und Kollektor p-dotiert und die Basis n-dotiert (Abbildung 2b; Skript, S. 193). Den Transferstrom tragen Löcher, und alle Spannungen und Ströme kehren sich um: Der Emitter liegt höher als die Basis, die Basis höher als der Kollektor, und der Strom fließt in den Emitter hinein und aus Basis und Kollektor heraus. Das Skript zählt die Ströme in dieser Richtung, sodass sie positiv sind, behält die Spannungsrichtungen bei und erhält negative Grenzwerte (S. 194):

| Bereich | Modell | Probe |
|---|---|---|
| Sperrbereich | $I_B$ = $I_C$ = 0 | $U_{BE}$ > −0,6 V |
| aktiv | $U_{BE}$ = −0,6 V, $I_C$ = $B\,I_B$ | $U_{CE}$ ≤ −0,2 V |
| Sättigung | $U_{BE}$ = −0,6 V, $U_{CE}$ = −0,2 V | $I_C$ ≤ $B\,I_B$ |

Die Ungleichungen für die Spannungen kehren sich um, die für die Ströme nicht. Das Skript verlangt für die Sättigung dagegen, dass $I_C$ mindestens $B\,I_B$ ist (S. 194); das stimmt nur für hineingezählte, negative Ströme, nicht für die Pfeile seines Bildes 11.30. Auch die Angabe, die Basis sei schwächer dotiert als der Kollektor (S. 193), widerspricht Abschnitt 11.1: Der Kollektor ist bei beiden Typen am schwächsten dotiert. Gebraucht wird der pnp-Transistor, um Lasten an Masse von der positiven Versorgung aus zu schalten, und in Gegentaktstufen wie der Endstufe des Praktikumsverstärkers.

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| dünne Basis und Transfergleichung | Die Stufe am Emitter bestimmt den Nachschub, und fast jedes Elektron erreicht den Kollektor. |
| flache Ausgangskennlinien | Der gesperrte Kollektorübergang sammelt jeden Nachschub ein, gleich wie hoch die Sperrspannung ist. |
| Basisstrom und Stromverstärkung | Zwei kleine Verluste an derselben Stufe; deshalb ein fester Bruchteil, und Strom- und Spannungssicht passen zusammen. |
| Sättigung | Leitet auch der Kollektorübergang, fließt überschüssiger Basisstrom in den Kollektor ab, und der äußere Kreis begrenzt den Strom. |
| pnp-Transistor | Derselbe Mechanismus mit Löchern als Nachschub. |

Ein gesperrter pn-Übergang führt so viel Strom, wie Nachschub an Minoritätsträgern zu ihm gelangt; im Bipolartransistor liefert ein leitender Übergang diesen Nachschub durch eine sehr dünne Basis, sodass die Basis-Emitter-Spannung den Kollektorstrom exponentiell festlegt, die Kollektorspannung ihn kaum beeinflusst und nur ein kleiner, fester Bruchteil als Basisstrom fließt.

## Bedeutung und Ausblick

Bipolartransistoren verstärken im Audioverstärker des Praktikums die Signale und schalten Leuchtdioden, Relais und Motoren. Der nächste Artikel, [Arbeitspunkt und Grundschaltungen des Transistors](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/arbeitspunkt-und-grundschaltungen.html), zeigt, wie man einen Transistor trotz der Streuung von $B$ und $I_S$ in einen festen Arbeitspunkt bringt; Early-Effekt und Kleinsignalverhalten behandelt [Der Transistor als Verstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker.html).

**In der ausführlichen Fassung:** die Stromverstärkung aus Dotierung und Geometrie, das Stromverhältnis $\alpha$, die Belege für die Spannungssicht, Inversbetrieb und schwach dotierter Kollektor, die Trägerflüsse in der Sättigung, die Schaltgeschwindigkeit, ein pnp-Schalter, die Korrekturen zu Bild 11.3 und weitere Beispiele. [Zur ausführlichen Fassung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise-ausfuehrlich.html)

:::kern
- Drei Gebiete: stark dotierter Emitter, dünne Basis, schwach dotierter Kollektor; im aktiven Bereich leitet der Basis-Emitter-Übergang, der Basis-Kollektor-Übergang sperrt.
- Knotenregel am Transistor: $I_E = I_B + I_C$; die Spannungen addieren sich über die Basis.
- Transfergleichung: $I_C = I_S\exp(U_{BE}/U_T)$; der gesperrte Kollektorübergang sammelt den Nachschub ein, $U_{CE}$ wirkt kaum.
- Der Basisstrom ersetzt Löcher, die durch Rückinjektion in den Emitter und Rekombination in der Basis verloren gehen.
- Stromverstärkung $B = I_C/I_B$, einige hundert; weil der Basisstrom nur ein kleiner Rest des Emitterstroms ist, streut $B$ stark.
- Physikalisch steuert $U_{BE}$; weil zu jedem Basisstrom genau eine Spannung gehört, darf man mit dem Basisstrom rechnen.
- Sättigung: Beide Übergänge leiten, $U_{CE}$ beträgt nur 0,1 bis 0,2 V, und der äußere Kreis begrenzt den Strom unter $B\,I_B$; Schalter brauchen Basisstrom für $B_\mathrm{min}$ mit Übersteuerung.
- pnp: alles umgekehrt; mit Strömen in Flussrichtung gelten dieselben Beziehungen, die Spannungsbedingungen kehren sich um.
:::

:::quiz
F: Warum fließt durch den gesperrten Basis-Kollektor-Übergang ein großer Strom?
A: Ein gesperrter Übergang führt so viel Strom, wie Minoritätsträger zu ihm gelangen. Der leitende Basis-Emitter-Übergang schickt Elektronen in die Basis, und weil die Basis 26-mal dünner ist als die Diffusionslänge, erreicht fast jedes den Kollektorrand, wo das Feld es in den Kollektor zieht.
F: Warum hängt der Kollektorstrom kaum von $U_{CE}$ ab?
A: Der gesperrte Basis-Kollektor-Übergang sammelt jedes ankommende Elektron ein; die Dichte am Kollektorrand ist bei jeder Sperrspannung null. Den Strom bestimmt die Randdichte am Emitter und damit $U_{BE}$; zwischen 1 und 10 V steigt er beim Beispieltransistor nur um 13 %.
F: Wie groß ist der Kollektorstrom des Beispieltransistors bei 0,70 V, und wie viel mehr Spannung verdoppelt ihn?
A: $10^{-14}$ A mal $\exp(0{,}70\ \mathrm{V}/25{,}85\ \mathrm{mV})$ ergibt 5,75 mA. Verdoppeln kostet 17,9 mV.
F: Stimmt es, dass die Elektronen des Kollektorstroms über die Basis hereinkommen und der Basisstrom den Transistor öffnet?
A: Nein. Die Elektronen kommen aus dem Emitter und verlassen den Transistor am Kollektor; über die Basis fließen nur Löcher, die Verluste ersetzen, bei 2 mA Kollektorstrom 4 µA. Die Ursache ist $U_{BE}$; weil der Basisstrom eindeutig dazugehört, darf man trotzdem mit ihm rechnen.
F: In welchem Bereich arbeitet der Beispieltransistor mit 2,2 kΩ an 10 V bei 20 µA Basisstrom?
A: Annahme aktiv verlangte 10 mA und $U_{CE}$ = −12 V, ein Widerspruch. Annahme Sättigung: 9,8 V durch 2,2 kΩ ergibt 4,45 mA, weniger als 500 mal 20 µA; die Probe hält, der Transistor ist gesättigt.
F: Stimmt es, dass der Transistor in der Sättigung seinen größten Strom liefert?
A: Nein. In der Sättigung begrenzt der äußere Kreis den Strom unter $B\,I_B$; im Beispiel könnte der Transistor 10 mA liefern, der Widerstand lässt 4,45 mA zu.
:::
