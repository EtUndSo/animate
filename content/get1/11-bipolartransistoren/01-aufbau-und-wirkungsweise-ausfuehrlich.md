---
title: Der Bipolartransistor – Aufbau und Wirkungsweise
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Bipolartransistoren
order: 110100
summary: Wie aus drei dotierten Schichten ein Bauteil wird, in dem die Basis-Emitter-Spannung einen großen Kollektorstrom festlegt und nur ein kleiner Basisstrom fließt: Aufbau und Zählpfeile, Transistoreffekt mit Transfergleichung, Herkunft von Basisstrom und Stromverstärkung, Strom- und Spannungssicht, Kennlinien, Arbeitsbereiche mit Sättigung, Schalter und pnp-Transistor. Ausführliche Fassung mit allen Herleitungen, der Stromverstärkung aus Dotierung und Geometrie und Beispielen am BC547C.
tags: Bipolartransistor, npn, pnp, Transistoreffekt, Stromverstärkung, aktiver Bereich, Sättigung
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Eine Diode lässt Strom durch oder sperrt ihn; verstärken oder gezielt schalten kann sie nicht. Dafür braucht man ein Bauteil, in dem eine kleine Steuergröße an einem Anschluss einen großen Strom zwischen zwei anderen festlegt. Der __Bipolartransistor__ leistet das mit zwei pn-Übergängen in einem Kristall.
**Ein gesperrter pn-Übergang führt so viel Strom, wie Nachschub an Minoritätsträgern zu ihm gelangt; im Bipolartransistor liefert ein leitender Übergang diesen Nachschub durch eine sehr dünne Basis, sodass die Basis-Emitter-Spannung den Kollektorstrom exponentiell festlegt, die Kollektorspannung ihn kaum beeinflusst und nur ein kleiner, fester Bruchteil als Basisstrom fließt.**
Minoritätsträger sind die seltene Ladungsträgersorte eines Gebiets, etwa Elektronen in einem p-dotierten Gebiet.

Vorausgesetzt werden der pn-Übergang aus [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell.html), die Kennlinie aus [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html) und das Rechnen mit Annahme und Probe aus [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html). Darauf bauen [Arbeitspunkt und Grundschaltungen des Transistors](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/arbeitspunkt-und-grundschaltungen.html) und [Der Transistor als Verstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker.html) auf.

:::grafik
Szene: get1/bipolartransistoren/01-npn-querschnitt · Vorlage: querschnitt-traegerfluesse
**Abbildung 1:** npn-Transistor im Querschnitt im Normalbetrieb, schematisch (Dicken nicht maßstäblich): stark n-dotierter Emitter, dünne p-dotierte Basis, schwach n-dotierter Kollektor, Raumladungszonen grau. Bei 2 mA Kollektorstrom laufen Elektronen (blau) vom Emitter durch die Basis in den Kollektor; über den Basisanschluss kommen nur Löcher (rot) nach, zusammen 4 µA, die Verluste durch Rückinjektion in den Emitter und durch Rekombination ersetzen. Die Pfeile an den Anschlüssen zeigen die technische Stromrichtung. Der Kollektorstrom fließt nicht über die Basis; die Basis ersetzt nur Verluste.
:::

## Aufbau, Schaltsymbol und Zählpfeile

*Woraus besteht ein Bipolartransistor, und wie zählt man seine Ströme und Spannungen?*

:::grafik
Szene: get1/bipolartransistoren/01-aufbau-symbole · Vorlage: aufbau-und-symbol
**Abbildung 2:** (a) npn-Transistor: Schichtfolge Emitter (n⁺, 10¹⁹ cm⁻³), Basis (p, 10¹⁷ cm⁻³, 0,5 µm), Kollektor (n, 10¹⁶ cm⁻³), dazu die Polung im Normalbetrieb und das Schaltsymbol mit den Zählpfeilen: Basis- und Kollektorstrom in den Transistor hinein, Emitterstrom heraus, Spannungen $U_{BE}$, $U_{CB}$ und $U_{CE}$. (b) pnp-Transistor mit umgekehrter Schichtfolge, Emitterpfeil nach innen und Zählpfeilen in Flussrichtung: Emitterstrom hinein, Basis- und Kollektorstrom heraus. Drei Gebiete, zwei Übergänge; der Emitterpfeil zeigt die Richtung des Emitterstroms.
:::

Ein Bipolartransistor besteht aus drei unterschiedlich dotierten Gebieten in einem Kristall, meist Silizium: dem __Emitter__ (E), der __Basis__ (B) und dem __Kollektor__ (C). Dotieren heißt, gezielt Fremdatome einzubauen, die ein Elektron abgeben (Donatoren, n-Gebiet) oder eines binden und so ein Loch erzeugen (Akzeptoren, p-Gebiet). Beim __npn-Transistor__ liegt eine p-dotierte Basis zwischen zwei n-Gebieten, beim __pnp-Transistor__ eine n-dotierte Basis zwischen zwei p-Gebieten (Abbildung 2). Jeder Transistor enthält damit zwei pn-Übergänge, den __Basis-Emitter-Übergang__ und den __Basis-Kollektor-Übergang__.

Die drei Gebiete sind bewusst ungleich. Der Emitter ist am stärksten dotiert, beim Beispieltransistor dieses Artikels mit 10¹⁹ Donatoren pro cm³; die Basis hat 100-mal weniger Akzeptoren, 10¹⁷ cm⁻³, und der Kollektor mit 10¹⁶ cm⁻³ noch einmal zehnmal weniger. Die Basis ist außerdem sehr dünn: Ihr neutraler Teil zwischen den beiden Raumladungszonen ist 0,5 µm weit, ein Hundertstel eines Haars. Der Beispieltransistor entspricht in seinen Kennwerten dem BC547C.

Der Name „bipolar“ besagt, dass beide Ladungsträgersorten beteiligt sind: Beim npn-Transistor tragen Elektronen den Kollektorstrom und Löcher den Basisstrom. In der Praxis überwiegt der npn-Typ, weil Elektronen in Silizium fast dreimal beweglicher sind als Löcher (1250 gegen 450 cm²/(V s) bei 10¹⁶ cm⁻³); bei gleicher Geometrie ist er schneller und verstärkt stärker.

Im __Schaltsymbol__ trägt der Emitter einen Pfeil. Er zeigt die Richtung, in der der Emitterstrom im Betrieb fließt, beim npn-Transistor aus dem Bauteil heraus. Gezählt wird wie in Abbildung 2a: Basis- und Kollektorstrom in den Transistor hinein, Emitterstrom heraus; jede Spannung zählt vom ersten zum zweiten genannten Anschluss, $U_{BE}$ also von der Basis zum Emitter.

**Die Akteure:**

- __$I_C$__: __Kollektorstrom__, in den Kollektor hinein; in A; beim Beispieltransistor typisch 0,1 bis 10 mA. Er ist der Strom, den man steuern will.
- __$I_B$__: __Basisstrom__, in die Basis hinein; in A; beim Beispieltransistor 500-mal kleiner als der Kollektorstrom, also Mikroampere.
- __$I_E$__: __Emitterstrom__, aus dem Emitter heraus; in A.
- __$U_{BE}$__: Spannung von der Basis zum Emitter; in V; im Normalbetrieb 0,6 bis 0,7 V. Sie polt den Basis-Emitter-Übergang in Durchlassrichtung.
- __$U_{CB}$__, __$U_{CE}$__: Spannungen vom Kollektor zur Basis bzw. zum Emitter; in V; im Normalbetrieb einige Volt. Ist $U_{CB}$ positiv, sperrt der Basis-Kollektor-Übergang.

**Das Zusammenspiel:** Der Transistor ist als Ganzes elektrisch neutral; was über Basis und Kollektor hineinfließt, fließt am Emitter heraus. Die Spannung vom Kollektor zum Emitter ist der Weg über die Basis:

:::formel Formel
$$I_E = I_B + I_C$$

$$U_{CE} = U_{CB} + U_{BE}$$
:::

**So liest man das:** Von den drei Strömen sind nur zwei unabhängig, von den drei Spannungen ebenso. Wer Kollektor- und Basisstrom kennt, kennt den Emitterstrom; wer $U_{CE}$ und $U_{BE}$ kennt, kennt $U_{CB}$. Ist $U_{CE}$ größer als $U_{BE}$, ist $U_{CB}$ positiv und der Basis-Kollektor-Übergang gesperrt.

Idee der Herleitung: Knotenregel für eine Hülle um den ganzen Transistor, Maschenregel über die drei Anschlüsse.

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

::::beispiel Ströme und Spannungen am Beispieltransistor bei 2 mA
**Gegeben:** Der Beispieltransistor führt $I_C$ = 2,000 mA bei $I_B$ = 4,00 µA; gemessen werden $U_{CE}$ = 5,00 V und $U_{BE}$ = 0,673 V.

**Gesucht:** Emitterstrom und $U_{CB}$.

**Rechnung:** Knotenregel:

$$I_E = 4{,}00\ \mu\mathrm{A} + 2{,}000\ \mathrm{mA} = 2{,}004\ \mathrm{mA}$$

Maschenregel, nach $U_{CB}$ aufgelöst:

$$U_{CB} = U_{CE} - U_{BE} = 5{,}00\ \mathrm{V} - 0{,}673\ \mathrm{V} = 4{,}33\ \mathrm{V}$$

**Ergebnis:** **Emitterstrom 2,004 mA; der Kollektor liegt 4,33 V über der Basis.**

**Einordnung:** Emitter- und Kollektorstrom unterscheiden sich nur um 0,2 %. Weil $U_{CB}$ positiv ist, sperrt der Basis-Kollektor-Übergang, während der Basis-Emitter-Übergang mit 0,673 V leitet: Das ist der Normalbetrieb.
::::

## Der Transistoreffekt

*Warum fließt durch den gesperrten Basis-Kollektor-Übergang ein großer Strom, und warum legt ihn $U_{BE}$ fest?*

:::grafik
Szene: get1/bipolartransistoren/01-transistoreffekt · Vorlage: banddiagramm-abfolge
**Abbildung 3:** (a) Leitungsbandkante $W_L$ entlang des Beispieltransistors ohne äußere Spannung: Stufe von 0,95 eV zwischen Emitter und Basis, 0,77 eV zwischen Basis und Kollektor. (b) Normalbetrieb mit $U_{BE}$ = 0,65 V und $U_{CB}$ = 5 V: Die erste Stufe ist auf 0,30 eV abgesenkt, die zweite auf 5,77 eV vertieft (Achse unterbrochen); Elektronen (blau) kommen über die abgesenkte Stufe, diffundieren durch die Basis und fallen am Basis-Kollektor-Übergang hinab. (c) Elektronendichte in der Basis über dem Ort: am Emitterrand 8,3·10¹³ cm⁻³, am Kollektorrand null, dazwischen eine Gerade; gestrichelt bei 0,70 V mit 5,7·10¹⁴ cm⁻³. Die Stufe am Emitter bestimmt, wie viele Elektronen kommen; die Kante am Kollektor sammelt sie alle ein.
:::

**Die Akteure:**

- __$n(x)$__: Dichte der Elektronen in der Basis am Ort $x$; in cm⁻³. Bei $x$ = 0 beginnt die neutrale Basis am Rand der Basis-Emitter-Zone, bei $x$ = $w_B$ endet sie am Rand der Basis-Kollektor-Zone. In der p-Basis sind die Elektronen Minoritätsträger neben 10¹⁷ Löchern pro cm³.
- __$n_{B0}$__: Elektronendichte der Basis im thermischen Gleichgewicht, nach dem Massenwirkungsgesetz $n_i^2/N_B$ mit der Eigenleitungsdichte $n_i$ = 10¹⁰ cm⁻³ und der Basisdotierung $N_B$; 10³ cm⁻³.
- __$w_B$__: Weite der neutralen Basis; 0,5 µm.
- __$D_n$__: __Diffusionskonstante__ der Elektronen in der Basis; in cm²/s; 20,7 cm²/s. Je größer sie ist, desto schneller gleicht die Wärmebewegung einen Dichteunterschied aus.
- __$\tau_n$__: __Lebensdauer__ eines Elektrons in der Basis, bis es mit einem Loch rekombiniert; 80 ns.
- __$L_n$__: __Diffusionslänge__, die Strecke, die ein Elektron während seiner Lebensdauer im Mittel diffundiert; 12,9 µm, also 26-mal mehr als die Basisweite.
- __$U_T$__: __Temperaturspannung__ $k_B T/e$; 25,85 mV bei 300 K. Eine um $e\,U_T$ niedrigere Stufe erhöht die Dichte dahinter um den Faktor 2,72.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Im Normalbetrieb, dem __aktiven Bereich__, liegt der Basis-Emitter-Übergang in Durchlassrichtung, mit $U_{BE}$ um 0,65 V, und der Basis-Kollektor-Übergang mit einigen Volt in Sperrrichtung. Abbildung 3b zeigt, was das für die Elektronen bedeutet: Die Stufe zwischen Emitter und Basis ist von 0,95 auf 0,30 eV abgesenkt, die Stufe zum Kollektor auf 5,77 eV vertieft.

**Schritt 2**: Über die abgesenkte Stufe gelangen Elektronen aus dem Emitter in die Basis. Wie bei der Diode wächst ihre Zahl mit dem Boltzmann-Faktor der Absenkung, $\exp(U_{BE}/U_T)$: Am Emitterrand der Basis steigt die Elektronendichte von 10³ auf 8,3·10¹³ cm⁻³ bei 0,65 V. Das sind nur 0,08 % der Löcherdichte; die Basis bleibt p-leitend.

**Schritt 3**: In der neutralen Basis treibt kein Feld die Elektronen. Sie bewegen sich durch __Diffusion__: Die ungeordnete Wärmebewegung trägt im Mittel mehr Teilchen von dichten zu dünnen Stellen als umgekehrt. Weil die Basis 26-mal dünner ist als die Diffusionslänge, erreicht fast jedes Elektron ihr anderes Ende, bevor es rekombiniert; die Verluste beziffert der Abschnitt *Der Basisstrom und die Stromverstärkung*.

**Schritt 4**: Am anderen Ende wartet der gesperrte Basis-Kollektor-Übergang. Für die Elektronen geht es dort steil bergab: Das Feld der Raumladungszone zieht jedes ankommende Elektron in den Kollektor, und am Kollektorrand der Basis ist die Elektronendichte praktisch null. Das ist derselbe Vorgang wie beim Sperrstrom der Diode: Ein gesperrter Übergang führt so viel Strom, wie Minoritätsträger zu ihm gelangen. Bei der Diode liefert die Wärme diesen Nachschub, hier der Emitter, bei 0,65 V 8·10¹⁰-mal so viele Elektronen, wie die Wärme in der Basis bereitstellt.

**Schritt 5**: Zwischen den beiden Rändern fällt die Dichte geradlinig ab (Abbildung 3c), denn unterwegs geht fast kein Elektron verloren, und durch jeden Querschnitt fließt derselbe Strom. Der Diffusionsstrom ist proportional zum Gefälle, also zur Randdichte am Emitter, und die wächst exponentiell mit $U_{BE}$. Die Sperrspannung kommt nicht vor: Ob die Kante 5 oder 10 V tief ist, die Dichte am Kollektorrand bleibt null.

:::analogie
Ein gesperrter pn-Übergang verhält sich wie ein Wasserfall: Wie viel Wasser hinabstürzt, bestimmt der Zufluss, nicht die Fallhöhe. Der Transistor ist ein solcher Wasserfall mit regelbarem Zufluss. Ein Wehr am Emitter, dessen Höhe $U_{BE}$ einstellt, lässt Wasser in einen kurzen Kanal, die Basis, und am Ende stürzt alles über die Kante. Mehr Fallhöhe ändert den Durchfluss nicht, nur das Wehr tut es.

| Im Vergleich | Im Transistor |
|---|---|
| Wehr am Zulauf | Stufe am Basis-Emitter-Übergang, abgesenkt durch $U_{BE}$ |
| kurzer Kanal | dünne Basis |
| Verdunstung im Kanal | Rekombination in der Basis |
| Kante und Fallhöhe | gesperrter Basis-Kollektor-Übergang, $U_{CB}$ |
| Durchfluss am Fall | Kollektorstrom |

**Wo der Vergleich nicht stimmt:** Im Kanal fließt das Wasser gerichtet bergab; die Elektronen in der Basis bewegen sich zufällig, und ein Netto-Fluss entsteht nur, weil am Kollektorrand keines zurückkommt. Außerdem wächst der Durchfluss über ein Wehr nicht exponentiell mit dessen Absenkung.
:::

Zusammen ergeben die Schritte die __Transfergleichung__ des Transistors:

:::formel Gesetz
$$I_C = I_S\,\exp\!\Big(\frac{U_{BE}}{U_T}\Big)$$
:::

**So liest man das:** Eingabe ist die Basis-Emitter-Spannung, Ausgabe der Kollektorstrom. $I_S$, der __Sättigungsstrom__ des Transistors, ist der Vorfaktor der Gleichung, anschaulich der Teil des Sperrstroms, den bei $U_{BE}$ = 0 die wenigen thermischen Elektronen der Basis tragen; er wächst mit der Emitterfläche und sinkt mit Dotierung und Weite der Basis, beim Beispieltransistor 10⁻¹⁴ A. Je 17,9 mV mehr verdoppelt sich der Kollektorstrom, je 59,5 mV verzehnfacht er sich. $U_{CB}$ und $U_{CE}$ kommen nicht vor, solange der Basis-Kollektor-Übergang sperrt. Tatsächlich steigt der Strom mit $U_{CE}$ leicht an, beim Beispieltransistor um 1,3 % je Volt, weil die wachsende Raumladungszone die Basis etwas dünner macht (__Early-Effekt__, behandelt in [Der Transistor als Verstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker.html)).

**Kurz gesagt:** Spannungsschritte an der Basis addieren sich, und die Faktoren, um die sie den Kollektorstrom vergrößern, multiplizieren sich, gleich bei welchem Strom man beginnt: 17,9 mV und 59,5 mV mehr, zusammen 77,4 mV, machen den Kollektorstrom zwanzigmal so groß. Das gilt, soweit die Transfergleichung gilt, bei fester Kollektorspannung und Temperatur.

Idee der Herleitung: Der Boltzmann-Faktor legt die Elektronendichte am Emitterrand der Basis fest; das geradlinige Profil in der dünnen Basis macht daraus einen Diffusionsstrom.

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

::::beispiel Kollektorstrom und Randdichte des Beispieltransistors
**Gegeben:** Beispieltransistor: $I_S$ = 10⁻¹⁴ A, $n_{B0}$ = 10³ cm⁻³; $U_T$ = 25,85 mV bei 300 K.

**Gesucht:** (a) der Kollektorstrom bei 0,60 V, 0,65 V und 0,70 V; (b) die Spannung für 2 mA; (c) die Elektronendichte am Emitterrand der Basis bei 0,65 V.

**Rechnung:** (a) Bei 0,65 V:

$$I_C = 10^{-14}\ \mathrm{A}\cdot\exp\!\Big(\frac{0{,}65\ \mathrm{V}}{25{,}85\ \mathrm{mV}}\Big) = 10^{-14}\ \mathrm{A}\cdot8{,}31\cdot10^{10} = 0{,}831\ \mathrm{mA}$$

Ebenso ergeben sich 0,120 mA bei 0,60 V und 5,75 mA bei 0,70 V.

(b) Die Transfergleichung nach $U_{BE}$ aufgelöst:

$$U_{BE} = U_T\,\ln\frac{I_C}{I_S} = 25{,}85\ \mathrm{mV}\cdot\ln\frac{2\ \mathrm{mA}}{10^{-14}\ \mathrm{A}} = 0{,}673\ \mathrm{V}$$

(c) Randdichte nach Schritt 2 der Herleitung:

$$n(0) = 10^{3}\ \mathrm{cm^{-3}}\cdot8{,}31\cdot10^{10} = 8{,}3\cdot10^{13}\ \mathrm{cm^{-3}}$$

**Ergebnis:** **0,120 mA, 0,831 mA und 5,75 mA; 0,673 V für 2 mA; Randdichte 8,3·10¹³ cm⁻³.**

**Einordnung:** 100 mV mehr ergeben den 48-fachen Strom, 1 mV mehr schon 3,9 % mehr. Das Datenblatt des BC547C nennt für 2 mA eine Basis-Emitter-Spannung von 0,55 bis 0,70 V; der Beispieltransistor liegt mit 0,673 V darin. Die Randdichte bleibt mit 0,08 % weit unter der Löcherdichte von 10¹⁷ cm⁻³, die Annahme schwacher Injektion hält.
::::

:::fehlvorstellung
„Die Kollektorspannung treibt den Kollektorstrom: Je größer $U_{CE}$, desto größer der Strom, wie an einem Widerstand.“
Das liegt nahe, weil $U_{CE}$ die Spannung ist, an der der Strom fließt. Am Transistor legt aber $U_{BE}$ den Strom fest; der gesperrte Basis-Kollektor-Übergang sammelt die ankommenden Elektronen bei jeder Sperrspannung vollständig ein (Schritt 4). Beim Beispieltransistor steigt der Kollektorstrom bei fester $U_{BE}$ zwischen 1 V und 10 V nur um 13 %, an einem Widerstand stiege er auf das Zehnfache. $U_{CE}$ muss nur groß genug sein, dass der Basis-Kollektor-Übergang sperrt.
:::

:::frage
„Ein Transistor enthält doch zwei pn-Übergänge. Kann man ihn aus zwei Dioden zusammenlöten?“
Nein. Die Elektronen, die die erste Diode in ihr p-Gebiet schickt, rekombinieren dort, im Mittel nach einer Diffusionslänge, bei der Beispieldiode aus dem Diodenartikel 57 µm, und spätestens am Metallkontakt. Bei der zweiten Diode kommt keines an: Durch den Draht fließt nur ein gewöhnlicher Strom, der ihrem gesperrten Übergang keinen Nachschub an Minoritätsträgern bringt. Auch im Kristall muss die Basis viel dünner sein als die Diffusionslänge: Beim Beispieltransistor mit 13 µm Diffusionslänge kämen bei 10 µm Basisweite nur 76 % der Elektronen an, und die Stromverstärkung wäre etwa 3. Mit einem Diodentester lassen sich die beiden Übergänge eines Transistors trotzdem wie zwei Dioden prüfen.
:::

## Der Basisstrom und die Stromverstärkung

*Woher kommt der Basisstrom, und warum ist er 500-mal kleiner als der Kollektorstrom?*

:::grafik
Szene: get1/bipolartransistoren/01-stromaufteilung · Vorlage: stromfluss-bilanz
**Abbildung 4:** Bilanz der Ladungsträger im aktiven Bereich, bezogen auf 10 000 Elektronen, die am Kollektor ankommen: Der Emitter schickt 10 007,6 Elektronen in die Basis, 7,6 davon rekombinieren dort; zugleich gehen 12,5 Löcher aus der Basis in den Emitter. Über den Basisanschluss kommen 20,1 Löcher nach. Kollektor- und Basisstrom stehen im Verhältnis 10 000 zu 20, also rund 500 zu 1.
:::

**Die Akteure:**

- __$B$__: __Stromverstärkung__, das Verhältnis von Kollektor- zu Basisstrom im aktiven Bereich; ohne Einheit; beim Beispieltransistor 500, beim BC547C nach Datenblatt 420 bis 800. Das Formelzeichen $B$ ist nicht der Anschlussname B.
- __$\alpha$__: Verhältnis von Kollektor- zu Emitterstrom; ohne Einheit; knapp unter 1, beim Beispieltransistor 0,998.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Kein Elektron des Kollektorstroms fließt über den Basisanschluss; alle kommen aus dem Emitter und verlassen den Transistor am Kollektor (Abbildung 1). Über den Basisanschluss kommen Löcher, genau so viele, wie der Basis verloren gehen. Im Anschlussdraht fließen dafür Elektronen aus der Basis heraus; die Ladungsbilanz ist dieselbe.

**Schritt 2**: Die abgesenkte Stufe am Basis-Emitter-Übergang wirkt auch für die Löcher der Basis: Ein Teil von ihnen gelangt in den Emitter, die __Rückinjektion__. Weil der Emitter 100-mal stärker dotiert ist als die Basis, sind es wenige; beim Beispieltransistor kommen auf 10 000 Elektronen, die den Kollektor erreichen, 12,5 Löcher, die in den Emitter gehen (Abbildung 4).

**Schritt 3**: Von den Elektronen, die durch die Basis diffundieren, rekombinieren einige mit einem Loch, und jedes verbrauchte Loch muss ersetzt werden. Ein Elektron braucht für die 0,5 µm im Mittel 60 ps, die __Transitzeit__, und lebt 80 ns. Auf 10 000 ankommende Elektronen rekombinieren deshalb 7,6.

**Schritt 4**: Beide Verluste hängen an derselben abgesenkten Stufe: Die Rückinjektion ist ein Löcherstrom über diese Stufe, die Rekombination zehrt am Elektronenstrom, der über sie kommt. Beide wachsen deshalb mit demselben Faktor $\exp(U_{BE}/U_T)$ wie der Kollektorstrom. Der Basisstrom ist so ein fester Bruchteil des Kollektorstroms, hier 20 auf 10 000, und das Verhältnis ist die Stromverstärkung: rund 500.

:::formel Formel
$$B = \frac{I_C}{I_B}, \qquad \alpha = \frac{I_C}{I_E}, \qquad B = \frac{\alpha}{1 - \alpha}$$
:::

**So liest man das:** Die ersten beiden Beziehungen sind Definitionen. Man wählt sie, weil im aktiven Bereich beide Verhältnisse über einen weiten Strombereich fast konstant sind, beim Beispieltransistor auf 10 % genau zwischen 0,3 und 20 mA. Die dritte zeigt, warum $B$ empfindlich ist: Es hängt am kleinen Rest $1 - \alpha$, dem Anteil des Emitterstroms, der als Basisstrom abzweigt. Sinkt dieser Rest von 0,4 % auf 0,2 %, verdoppelt sich $B$ von 249 auf 499. Kleine Unterschiede in Basisweite und Dotierung streuen $B$ deshalb in der Fertigung erheblich; Hersteller messen jeden Transistor und sortieren ihn in Gruppen, beim BC547 in A (110 bis 220), B (200 bis 450) und C (420 bis 800).

Idee der Herleitung: Nach der Knotenregel ist der Basisstrom der Unterschied zwischen Emitter- und Kollektorstrom.

:::herleitung
**Ausgangspunkt:** die Knotenregel aus dem Abschnitt *Aufbau, Schaltsymbol und Zählpfeile* und die Definitionen von $B$ und $\alpha$.

**Annahmen:** (i) aktiver Bereich, Basis- und Kollektorstrom positiv.

**Schritt 1**: Nach der Knotenregel ist der Basisstrom der Unterschied zwischen Emitter- und Kollektorstrom:

$$I_B = I_E - I_C$$

**Schritt 2** (entscheidender Schritt): Nach der Definition von $\alpha$ ist der Emitterstrom der Kollektorstrom geteilt durch $\alpha$; eingesetzt:

$$I_B = \frac{I_C}{\alpha} - I_C = I_C\,\frac{1 - \alpha}{\alpha}$$

**Schritt 3**: Nach der Definition von $B$ teilt man den Kollektorstrom durch diesen Basisstrom:

$$B = \frac{I_C}{I_B} = \frac{\alpha}{1 - \alpha}$$

**Ergebnis:**

$$B = \frac{\alpha}{1 - \alpha}$$

**Woher die Faktoren kommen:** Der Nenner $1 - \alpha$ ist der Anteil des Emitterstroms, der über die Basis abfließt, der Zähler $\alpha$ der Anteil, der am Kollektor ankommt.

**Proben:** Umgekehrt aufgelöst:

$$\alpha = \frac{B}{B + 1}$$

für 500 also 0,998. Grenzfall: Ein verlustfreier Transistor mit $\alpha$ gegen 1 hätte eine unendliche Stromverstärkung.

**Grenzen:** Gilt im aktiven Bereich; in der Sättigung ist das Verhältnis von Kollektor- zu Basisstrom kleiner als $B$ (Abschnitt *Die Arbeitsbereiche*).
:::

::::beispiel Stromverstärkung aus gemessenen Strömen
**Gegeben:** Am Beispieltransistor werden bei $U_{CE}$ = 5 V gemessen: $I_C$ = 2,000 mA und $I_B$ = 4,00 µA.

**Gesucht:** $B$, Emitterstrom und $\alpha$; dazu, wie stark $B$ auf eine kleine Änderung von $\alpha$ reagiert.

**Rechnung:**

$$B = \frac{2{,}000\ \mathrm{mA}}{4{,}00\ \mu\mathrm{A}} = 500, \qquad I_E = 2{,}000\ \mathrm{mA} + 0{,}004\ \mathrm{mA} = 2{,}004\ \mathrm{mA}$$

$$\alpha = \frac{2{,}000\ \mathrm{mA}}{2{,}004\ \mathrm{mA}} = 0{,}998$$

Für $\alpha$ = 0,996 statt 0,998:

$$B = \frac{0{,}996}{1 - 0{,}996} = 249$$

**Ergebnis:** **$B$ = 500 und $\alpha$ = 0,998; zwei Tausendstel weniger $\alpha$ halbieren $B$.**

**Einordnung:** Im Basisstrom steckt der kleine Rest von 0,2 %, um den sich Emitter- und Kollektorstrom unterscheiden. Deshalb streut $B$ so viel stärker als $\alpha$, und Schaltungen, die mit einem festen $B$ rechnen, müssen dessen ganze Spanne vertragen.
::::

Wie groß die beiden Verluste sind, folgt aus Dotierung und Geometrie.

**Die Akteure:**

- __$N_E$__: Dotierung des Emitters; 10¹⁹ cm⁻³.
- __$w_E$__: Dicke des neutralen Emitters bis zum Kontakt; 0,5 µm.
- __$D_p$__: Diffusionskonstante der Löcher im Emitter; 2,6 cm²/s, achtmal kleiner als die der Elektronen in der Basis, weil Löcher schwerer beweglich sind und die hohe Dotierung sie zusätzlich bremst.

:::formel Formel
$$\frac{1}{B} \approx \frac{D_p\,N_B\,w_B}{D_n\,N_E\,w_E} + \frac{w_B^2}{2\,L_n^2}$$
:::

**So liest man das:** Eingabe sind Dotierungen, Dicken und Materialwerte, Ausgabe der Kehrwert der Stromverstärkung. Der erste Bruch ist die Rückinjektion je Elektron am Kollektor, der zweite die Rekombination in der Basis. Ein Emitter, der viel stärker dotiert ist als die Basis, macht den ersten klein, eine Basis, die viel dünner ist als die Diffusionslänge, den zweiten. Beim Beispieltransistor sind es 1,25 und 0,76 Tausendstel, zusammen 2 Tausendstel, also $B$ ≈ 500. Eine doppelt so dicke Basis ergäbe $B$ ≈ 180, ein Emitter mit nur 10¹⁸ cm⁻³ ein $B$ unter 100.

Idee der Herleitung: Man rechnet den Löcherstrom in den Emitter wie den Elektronenstrom durch die Basis und die Rekombination als gespeicherte Ladung geteilt durch die Lebensdauer.

:::herleitung
**Ausgangspunkt:** die Herleitung der Transfergleichung (Boltzmann-Verteilung, Massenwirkungsgesetz, Ficksches Gesetz) und die Rekombinationsrate: Von $N$ Minoritätsträgern rekombinieren im Mittel $N/\tau_n$ je Sekunde.

**Annahmen:**
(i) wie bei der Transfergleichung;
(ii) kurzer Emitter: Er ist dünner als die Diffusionslänge der Löcher dort, und am Emitterkontakt ist die Löcherdichte auf ihren Gleichgewichtswert gesunken;
(iii) Rekombination nur in der neutralen Basis, nicht in den Raumladungszonen.

**Schritt 1**: Für die Löcher im Emitter gilt dieselbe Rechnung wie für die Elektronen in der Basis, mit ihrer Gleichgewichtsdichte $n_i^2/N_E$ und der Dicke $w_E$. Der Strom der Rückinjektion ist

$$I_{pE} = \frac{e\,A\,D_p\,n_i^2}{N_E\,w_E}\,\exp\!\Big(\frac{U_{BE}}{U_T}\Big)$$

**Schritt 2**: Geteilt durch den Kollektorstrom aus der Transfergleichung kürzen sich $e$, $A$, $n_i^2$ und die Exponentialfunktion:

$$\frac{I_{pE}}{I_C} = \frac{D_p\,N_B\,w_B}{D_n\,N_E\,w_E}$$

**Schritt 3**: Die Elektronen in der Basis bilden nach dem geradlinigen Profil ein Dreieck mit der Fläche $n(0)\,w_B/2$. Mit $e\,A$ multipliziert ist das ihre Ladung:

$$Q_B = \frac{e\,A\,n(0)\,w_B}{2}$$

**Schritt 4**: Teilt man diese Ladung durch den Strom, der sie durch die Basis trägt, den Kollektorstrom aus Schritt 5 der Transfergleichung, erhält man die mittlere Aufenthaltsdauer eines Elektrons in der Basis, die Transitzeit $\tau_t$:

$$\tau_t = \frac{Q_B}{I_C} = \frac{e\,A\,n(0)\,w_B/2}{e\,A\,D_n\,n(0)/w_B} = \frac{w_B^2}{2\,D_n}$$

**Schritt 5** (entscheidender Schritt): Nach der Rekombinationsrate verschwinden je Sekunde $Q_B/\tau_n$ an Ladung, und jedes rekombinierte Elektron verbraucht ein Loch. Bezogen auf den Kollektorstrom, mit der Diffusionslänge $L_n$, deren Quadrat $D_n\,\tau_n$ ist:

$$\frac{I_{rB}}{I_C} = \frac{Q_B/\tau_n}{Q_B/\tau_t} = \frac{\tau_t}{\tau_n} = \frac{w_B^2}{2\,D_n\,\tau_n} = \frac{w_B^2}{2\,L_n^2}$$

**Schritt 6**: Der Basisstrom ist die Summe beider Verluste. Geteilt durch den Kollektorstrom, wobei man vernachlässigt, dass dieser um die Rekombination kleiner ist als der Elektronenstrom am Emitter:

$$\frac{1}{B} = \frac{I_{pE} + I_{rB}}{I_C} \approx \frac{D_p\,N_B\,w_B}{D_n\,N_E\,w_E} + \frac{w_B^2}{2\,L_n^2}$$

**Ergebnis:**

$$\frac{1}{B} \approx \frac{D_p\,N_B\,w_B}{D_n\,N_E\,w_E} + \frac{w_B^2}{2\,L_n^2}$$

**Woher die Faktoren kommen:** $N_B/N_E$ stammt aus den Gleichgewichtsdichten der Minoritätsträger auf beiden Seiten, $w_B/w_E$ aus den beiden Gefällen, $D_p/D_n$ aus den Beweglichkeiten. Die 2 im zweiten Bruch stammt aus der Dreiecksfläche, der Hälfte von Grundseite mal Höhe (Schritt 3).

**Proben:** Beide Brüche sind einheitenlos. Mit den Zahlen des Beispieltransistors ergibt sich ein $B$ von 498,6, mit der exakten numerischen Lösung der Diffusionsgleichung 498,5, gerundet beide 499. Grenzfall: Eine beliebig dünne Basis und ein beliebig hoch dotierter Emitter ergäben eine unendliche Stromverstärkung.

**Grenzen:** In realen Emittern mit 10¹⁹ cm⁻³ und mehr verkleinert die hohe Dotierung die Bandlücke und vergrößert so die Rückinjektion; reale Werte von $B$ liegen deshalb unter dieser Abschätzung. Bei kleinen Strömen kommt Rekombination in der Basis-Emitter-Zone hinzu (Abschnitt *Die Kennlinien*).
:::

::::beispiel Stromverstärkung aus Dotierung und Geometrie des Beispieltransistors
**Gegeben:** Elektronen in der Basis mit $D_n$ = 20,7 cm²/s (Beweglichkeit 800 cm²/(V s)), Löcher im Emitter mit $D_p$ = 2,59 cm²/s (100 cm²/(V s)); $N_E$ = 10¹⁹ cm⁻³, $N_B$ = 10¹⁷ cm⁻³, $w_E$ = $w_B$ = 0,5 µm; $\tau_n$ = 80 ns.

**Gesucht:** Rückinjektion, Transitzeit, Rekombination und $B$.

**Rechnung:** Rückinjektion je Elektron am Kollektor:

$$\frac{D_p\,N_B\,w_B}{D_n\,N_E\,w_E} = \frac{2{,}59}{20{,}7}\cdot\frac{10^{17}}{10^{19}}\cdot\frac{0{,}5\ \mu\mathrm{m}}{0{,}5\ \mu\mathrm{m}} = 0{,}125\cdot0{,}01\cdot1 = 1{,}250\cdot10^{-3}$$

Transitzeit und Rekombination:

$$\tau_t = \frac{(0{,}5\cdot10^{-4}\ \mathrm{cm})^2}{2\cdot20{,}7\ \mathrm{cm^2/s}} = 60{,}4\ \mathrm{ps}, \qquad \frac{\tau_t}{\tau_n} = \frac{60{,}4\ \mathrm{ps}}{80\ \mathrm{ns}} = 0{,}756\cdot10^{-3}$$

Zusammen:

$$\frac{1}{B} = 1{,}250\cdot10^{-3} + 0{,}756\cdot10^{-3} = 2{,}006\cdot10^{-3}, \qquad B = 499$$

**Ergebnis:** **Rückinjektion 1,25 Tausendstel, Rekombination 0,76 Tausendstel: $B$ ≈ 500.**

**Einordnung:** Die Rückinjektion überwiegt; sie sinkt mit stärkerer Emitterdotierung. Die Rekombination ist klein, weil ein Elektron für die Basis nur 60 ps braucht, weniger als ein Tausendstel seiner Lebensdauer. Variation: Mit 1 µm Basisweite steigt die Rekombination auf das Vierfache und die Rückinjektion auf das Doppelte; $B$ fällt auf 180. Der Wert 500 liegt mitten in der Gruppe C des BC547.
::::

:::frage
„Wenn der Basisstrom den Kollektorstrom nicht verursacht, wozu braucht man ihn dann? Was geschieht bei offener Basis?“
Ohne Nachschub verliert die Basis ständig Löcher, an den Emitter und durch Rekombination. Sie lädt sich dadurch negativ auf, die Spannung am Basis-Emitter-Übergang sinkt, die Stufe wächst, und es kommen weniger Elektronen. Das geht so lange, bis Verlust und Nachschub wieder gleich sind; bei offener Basis bleibt nur ein Leckstrom, um viele Zehnerpotenzen kleiner als im Betrieb. Der Basisstrom hält also den Zustand aufrecht, den $U_{BE}$ beschreibt: Er ersetzt die verlorenen Löcher, die sonst die Stufe anheben würden. Er ist der laufende Preis des Betriebs, nicht dessen Ursache.
:::

:::frage
„Warum ist der Kollektor so schwach dotiert? Man könnte Emitter und Kollektor doch vertauschen.“
Vertauscht arbeitet der Transistor im __Inversbetrieb__, mit dem Kollektor als Emitter. Die Basis ist dann zehnmal stärker dotiert als der Gegenpart, und auf jedes Elektron, das der Kollektor in die Basis schickt, gehen 0,56 Löcher zurück in den Kollektor; die Stromverstärkung fällt beim Beispieltransistor von 500 auf 1,8. Die schwache Dotierung hat einen anderen Zweck: Die Raumladungszone des gesperrten Übergangs liegt zu neun Zehnteln im Kollektor, 0,82 von 0,91 µm bei 5 V. Die Basis wird so kaum dünner, und hohe Sperrspannungen sind möglich; der BC547 verträgt 45 V zwischen Kollektor und Emitter.
:::

## Strom- oder Spannungssteuerung

*Steuert der Basisstrom oder die Basis-Emitter-Spannung den Kollektorstrom?*

:::grafik
Szene: get1/bipolartransistoren/01-zwei-sichten · Vorlage: zwei-schnitte
**Abbildung 5:** Derselbe Kollektorstrom aus zwei Richtungen gesehen, gemeinsame lineare y-Achse $I_C$ bis 3 mA. Links über $U_{BE}$ von 0,55 bis 0,70 V: der exponentielle Anstieg der Transfergleichung. Rechts über $I_B$ von 0 bis 6 µA: eine Gerade mit der Steigung 500. Markiert ist in beiden derselbe Arbeitspunkt, 0,65 V, 1,66 µA und 0,83 mA; gestrichelt ein zweites Exemplar mit doppeltem Sättigungsstrom (links um 17,9 mV nach links verschoben) und $B$ = 700 (rechts steiler). Beide Kennlinien beschreiben denselben Zustand, aber sie streuen verschieden.
:::

Die Transfergleichung beschreibt den Transistor über $U_{BE}$. Oft beschreibt man ihn dagegen als __stromgesteuerte Stromquelle__: Der Basisstrom, in dieser Sicht Steuerstrom genannt, legt den Kollektorstrom fest, $B$-mal so groß. Beide Beschreibungen ergeben dieselben Zahlen, denn der Basisstrom folgt demselben Gesetz wie der Kollektorstrom (Abbildung 5). Teilt man die Transfergleichung durch $B$, erhält man die __Eingangskennlinie__:

:::formel Formel
$$I_B = \frac{I_S}{B}\,\exp\!\Big(\frac{U_{BE}}{U_T}\Big)$$
:::

**So liest man das:** Eingabe ist $U_{BE}$, Ausgabe der Basisstrom. Die Eingangskennlinie ist die Kennlinie einer Diode mit dem Sättigungsstrom $I_S/B$, beim Beispieltransistor 2·10⁻¹⁷ A. Sie lässt sich umkehren: Zu jedem Basisstrom gehört genau eine Spannung, zu 1,66 µA gehören 0,65 V.

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

Welche der beiden Größen ist die Ursache? Physikalisch die Spannung: $U_{BE}$ legt die Höhe der Stufe fest und damit, wie viele Elektronen in die Basis gelangen; der Basisstrom ersetzt die Löcher, die dabei verloren gehen. Zwei Beobachtungen stützen diese Sicht. Die Transfergleichung gilt über viele Zehnerpotenzen des Stroms mit derselben Steigung, die nur von der Temperatur abhängt, während $B$ mit dem Strom, der Temperatur und dem Exemplar schwankt. Und Hersteller machen $B$ so groß wie möglich: Superbeta-Transistoren in den Eingängen von Präzisions-Operationsverstärkern erreichen 5000 bei 1 µA. Im Grenzfall unendlicher Stromverstärkung flösse gar kein Basisstrom, und der Transistor arbeitete trotzdem, gesteuert allein über $U_{BE}$.

Die Stromsicht ist trotzdem kein Fehler. Weil sich die Eingangskennlinie umkehren lässt, legt ein erzwungener Basisstrom auch $U_{BE}$ fest und damit den Kollektorstrom: Gibt eine Schaltung 4 µA in die Basis, stellt sich $U_{BE}$ auf 0,673 V ein, und es fließen 2 mA. Für Handrechnungen kommt hinzu, dass sich $U_{BE}$ kaum ändert, 60 mV je Zehnfaches des Stroms. Ersetzt man den Basis-Emitter-Übergang deshalb wie bei der Diode durch eine feste Spannung von 0,6 bis 0,7 V, bleibt der Basisstrom als einzige Größe, die die äußere Schaltung einstellt, und alle Gleichungen werden linear. Darauf beruhen das Rechenmodell im Abschnitt *Die Arbeitsbereiche* und die Schaltungen in [Zweitore](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/zweitore.html), in denen der Transistor als gesteuerte Quelle erscheint.

::::beispiel Ein Arbeitspunkt in beiden Sichten
**Gegeben:** Beispieltransistor mit $I_S$ = 10⁻¹⁴ A und $B$ = 500 bei $U_{BE}$ = 0,65 V; ein zweites Exemplar desselben Typs mit $I_S$ = 2·10⁻¹⁴ A und $B$ = 700.

**Gesucht:** Kollektor- und Basisstrom in beiden Sichten; die Abweichung des zweiten Exemplars, wenn die Schaltung die Spannung bzw. den Basisstrom festhält.

**Rechnung:** Spannungssicht, mit der Transfergleichung und der Definition von $B$:

$$I_C = 0{,}831\ \mathrm{mA}, \qquad I_B = \frac{0{,}831\ \mathrm{mA}}{500} = 1{,}66\ \mu\mathrm{A}$$

Stromsicht: Wer 1,66 µA vorgibt, erhält über $B$ dieselben 0,831 mA und aus der Eingangskennlinie dieselben 0,65 V. Das zweite Exemplar bei fester Spannung und bei festem Basisstrom:

$$I_C = 2\cdot10^{-14}\ \mathrm{A}\cdot8{,}31\cdot10^{10} = 1{,}66\ \mathrm{mA}, \qquad I_C = 700\cdot1{,}66\ \mu\mathrm{A} = 1{,}16\ \mathrm{mA}$$

**Ergebnis:** **Beide Sichten liefern 0,831 mA und 1,66 µA; das zweite Exemplar weicht bei fester Spannung um 100 %, bei festem Basisstrom um 40 % ab.**

**Einordnung:** Keine der beiden Ansteuerungen ist für sich robust. Bei fester Spannung wirken die Streuung von $I_S$ und die Temperatur: 10 K wärmer, und der Strom steigt auf rund das 2,2-Fache, weil der Sättigungsstrom mit der Zahl der thermischen Ladungsträger wächst. Bei festem Basisstrom wirkt die Streuung von $B$, das außerdem um 0,5 bis 1 % je Kelvin steigt. Gute Schaltungen machen den Arbeitspunkt mit Gegenkopplung von beidem unabhängig ([Arbeitspunkt und Grundschaltungen des Transistors](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/arbeitspunkt-und-grundschaltungen.html)).
::::

:::fehlvorstellung
„Der Basisstrom öffnet den Transistor wie ein Ventil; die Elektronen des Kollektorstroms kommen über die Basis herein.“
Das legen das Wort Steuerstrom und eine verbreitete Wasseranalogie nahe, in der ein Wasserstrahl aus der Basis eine Klappe aufdrückt. Die Elektronen des Kollektorstroms kommen aber aus dem Emitter und gehen nie über den Basisanschluss (Abbildung 1). Über ihn fließen nur die Löcher, die Rückinjektion und Rekombination ersetzen, bei 2 mA Kollektorstrom 4 µA. Als Rechenmodell bleibt die Stromsicht richtig, weil der Basisstrom eindeutig mit $U_{BE}$ verknüpft ist.
:::

## Die Kennlinien

*Wie liest man Eingangs-, Steuer- und Ausgangskennlinie eines Transistors?*

:::grafik
Szene: get1/bipolartransistoren/01-kennlinien · Vorlage: kennlinien-drei
**Abbildung 6:** Kennlinien des Beispieltransistors, berechnet. (a) Eingangskennlinie bei $U_{CE}$ = 5 V: $I_B$ über $U_{BE}$ von 0,5 bis 0,75 V, 20 µA bei 0,714 V. (b) Stromsteuerkennlinie doppelt logarithmisch: $I_C$ über $I_B$ von 1 nA bis 1 mA, eine Gerade der Steigung 1, um den Faktor 500 über der Diagonalen; bei kleinen und großen Strömen sinkt $B$ (an das Datenblatt des BC547C angepasst: 260 bei 10 µA, 500 bei 2 mA, 285 bei 100 mA Kollektorstrom). (c) Ausgangskennlinienfeld: $I_C$ über $U_{CE}$ von 0 bis 10 V für $I_B$ = 2, 4, 6, 8 und 10 µA; oberhalb von etwa 0,3 V fast waagrecht mit leichtem Anstieg (für 4 µA 1,88 mA bei 0,5 V, 2,00 mA bei 5 V, 2,13 mA bei 10 V), darunter steiler Abfall; markiert $U_{CE,\mathrm{sat}}$ = 0,2 V und die Grenzlinie $U_{CB}$ = 0 bei 0,65 bis 0,70 V. Eine Diodenkennlinie am Eingang, eine Gerade dazwischen, Stromquellenäste am Ausgang.
:::

Drei Kennlinien beschreiben das Verhalten; Abbildung 6 zeigt sie für den Beispieltransistor.

Die **Eingangskennlinie** (Abbildung 6a) ist die Diodenkennlinie aus dem vorigen Abschnitt. Auf linearer Achse scheint der Strom erst ab etwa 0,6 V einzusetzen; diesen Wert nennt man $U_{BE,\mathrm{ein}}$. Eine Schwelle gibt es aber nicht: Bei 0,55 V fließen 35 nA Basisstrom und 17 µA Kollektorstrom, bei 0,50 V noch 5 nA und 2,5 µA; sie verschwinden nur auf den Skalen in Mikro- und Milliampere.

Die **Stromsteuerkennlinie** (Abbildung 6b) zeigt $I_C$ über $I_B$: im mittleren Strombereich eine Gerade durch den Ursprung mit der Steigung $B$. Doppelt logarithmisch aufgetragen wie in Abbildung 6b ist $B$ aber nicht ihre Steigung: Auf logarithmischen Achsen hat jede Proportionalität die Steigung 1, und $B$ erscheint als senkrechter Abstand von der Diagonalen. Bei großen Strömen biegt die Kurve ab. Ein häufiger Fehler ist, dazu zu sagen, der Transistor „geht in Sättigung“; tatsächlich ist es ein Rückgang von $B$: Bei hohen Stromdichten reichen die Ladungsträgerdichten an die Dotierungen heran, und die Annahme schwacher Injektion versagt. Wo das beginnt, hängt von Fläche und Dotierung ab; der Modelltransistor erreicht es erst um 1 A, der BC547C früher, sein Datenblatt nennt typisch 520 bei 2 mA und 300 bei 100 mA. Mit dem Sättigungsbereich aus dem Abschnitt *Die Arbeitsbereiche* hat das nichts zu tun. Auch bei sehr kleinen Strömen sinkt $B$, beim BC547C auf typisch 270 bei 10 µA, weil die Rekombination in der Basis-Emitter-Zone den Basisstrom erhöht.

Die **Ausgangskennlinien** (Abbildung 6c) zeigen $I_C$ über $U_{CE}$, eine für jeden Basisstrom. Oberhalb von etwa 0,3 V verlaufen sie fast waagrecht: Am Ausgang wirkt der Transistor wie eine Stromquelle, deren Strom die Basisseite festlegt (Abschnitt *Der Transistoreffekt*). Der leichte Anstieg ist der Early-Effekt. Unterhalb von etwa 0,2 V fallen die Kurven steil ab, weil der Basis-Kollektor-Übergang zu leiten beginnt.

Achtung: Schematische Kennlinienbilder zeichnen die Grenzlinie, auf der $U_{CE}$ gleich $U_{BE}$ ist, oft bei mehreren Volt. Da sich $U_{BE}$ kaum ändert, liegt sie tatsächlich bei 0,6 bis 0,7 V, und der Knick realer Kennlinien liegt mit 0,1 bis 0,3 V noch darunter.

## Die Arbeitsbereiche

*Was geschieht, wenn der Basis-Kollektor-Übergang nicht mehr sperrt, und wie findet man heraus, in welchem Bereich ein Transistor arbeitet?*

Jeder der beiden Übergänge kann leiten oder sperren; daraus ergeben sich vier Betriebsarten:

| Bereich und Übergänge | Verhalten |
|---|---|
| aktiver Bereich: Basis-Emitter-Übergang leitet, Basis-Kollektor-Übergang sperrt | Stromquelle mit $B$-fachem Basisstrom; Verstärker |
| Sättigung: beide Übergänge leiten | $U_{CE}$ nur 0,1 bis 0,2 V, den Strom begrenzt der äußere Kreis; Schalter ein |
| Sperrbereich: beide Übergänge sperren | fast kein Strom; Schalter aus |
| Inversbetrieb: nur der Basis-Kollektor-Übergang leitet | Emitter und Kollektor vertauscht, Stromverstärkung 1,8; selten genutzt |

Für die Rechnung von Hand ersetzt man den Transistor, wie die Diode, in jedem Bereich durch ein einfaches Modell, mit $U_{BE,\mathrm{ein}}$ = 0,6 V und der __Sättigungsspannung__ $U_{CE,\mathrm{sat}}$ = 0,2 V. Man nimmt einen Bereich an, rechnet mit seinem Modell und prüft die Bedingung; trifft sie nicht zu, war die Annahme falsch, wie in [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html):

| Bereich | Modell | Probe |
|---|---|---|
| Sperrbereich | $I_B$ = $I_C$ = 0 | $U_{BE}$ < 0,6 V |
| aktiv | $U_{BE}$ = 0,6 V, $I_C$ = $B\,I_B$ | $U_{CE}$ ≥ 0,2 V |
| Sättigung | $U_{BE}$ = 0,6 V, $U_{CE}$ = 0,2 V | $I_C$ ≤ $B\,I_B$ |

:::grafik
Szene: get1/bipolartransistoren/01-arbeitsgerade · Vorlage: kennlinienfeld-arbeitsgerade
**Abbildung 7:** Modellkennlinien des Beispieltransistors ($B$ = 500, waagrecht ab $U_{CE,\mathrm{sat}}$ = 0,2 V) für $I_B$ = 2, 8 und 20 µA, dazu die Arbeitsgerade eines Kollektorwiderstands von 2,2 kΩ an 10 V von (10 V, 0) nach (0, 4,55 mA). Arbeitspunkte: 2 µA bei 7,8 V und 1,0 mA (aktiv), 8 µA bei 1,2 V und 4,0 mA (aktiv), 20 µA bei 0,2 V und 4,45 mA (Sättigung; die Modellkennlinie läge bei 10 mA). Die Bereiche sind farbig hinterlegt. Ab 8,9 µA bleibt der Arbeitspunkt in der Sättigung stehen; mehr Basisstrom ändert den Kollektorstrom nicht.
:::

**Die Akteure:**

- __$U_{CC}$__: Versorgungsspannung des Kollektorkreises; 10 V im Beispiel.
- __$R_C$__: Kollektorwiderstand zwischen Versorgung und Kollektor; 2,2 kΩ.
- __$U_{BC}$__: Spannung von der Basis zum Kollektor, also der Gegenwert von $U_{CB}$; positiv, sobald der Basis-Kollektor-Übergang in Durchlassrichtung liegt.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Was am Kollektorwiderstand abfällt, fehlt an $U_{CE}$; die Punkte, die der Kollektorkreis zulässt, liegen auf der __Arbeitsgeraden__ in Abbildung 7. Mehr Basisstrom bedeutet im aktiven Bereich $B$-mal mehr Kollektorstrom und deshalb weniger $U_{CE}$: Bei 8 µA bleiben noch 1,2 V.

**Schritt 2**: Sinkt $U_{CE}$ unter $U_{BE}$, liegt der Kollektor tiefer als die Basis, und der Basis-Kollektor-Übergang ist in Durchlassrichtung gepolt. Merklich leitet er ab einer Durchlassspannung von etwa 0,5 V, also ab $U_{CE}$ um 0,2 V. Er lässt dann Löcher aus der Basis in den schwach dotierten Kollektor.

**Schritt 3**: Jetzt teilt sich der Basisstrom. Ein Teil ersetzt wie bisher die Verluste durch Rückinjektion und Rekombination, der Rest fließt als Löcherstrom über den Basis-Kollektor-Übergang ab (Abbildung 8); beim Beispieltransistor mit 20 µA Basisstrom sind es 9,6 µA und 10,4 µA. Der Kollektorstrom wächst deshalb nicht mehr mit dem Basisstrom und bleibt bei dem Wert, den der Kollektorkreis zulässt, rund 4,5 mA statt 500 mal 20 µA, also 10 mA. Daher der Name __Sättigung__.

**Schritt 4**: $U_{CE}$ ist jetzt die Differenz zweier Durchlassspannungen, $U_{BE}$ minus $U_{BC}$. Beim Beispieltransistor sind das 0,696 V minus 0,552 V, also 0,144 V. Das einfache Modell rechnet mit 0,2 V; das Datenblatt des BC547C nennt typisch 0,09 V bei 10 mA und 0,5 mA Basisstrom.

Die Grenze zur Sättigung und den Strom in ihr liefert die Maschenregel des Kollektorkreises:

:::formel Formel
$$I_{C,\mathrm{sat}} = \frac{U_{CC} - U_{CE,\mathrm{sat}}}{R_C}, \qquad I_B \ge \frac{I_{C,\mathrm{sat}}}{B}$$
:::

**So liest man das:** Eingabe sind Versorgung, Kollektorwiderstand und Stromverstärkung, Ausgabe der Kollektorstrom in der Sättigung und der Basisstrom, ab dem sie erreicht ist. Darüber ändert mehr Basisstrom den Kollektorstrom nicht mehr. Ein größerer Widerstand oder ein größeres $B$ senkt die Grenze. Mit 10 V, 2,2 kΩ und $B$ = 500 sind es 4,45 mA ab 8,9 µA.

Idee der Herleitung: Maschenregel im Kollektorkreis mit dem Sättigungsmodell, dann die Bedingung der Sättigung nach dem Basisstrom aufgelöst.

:::herleitung
**Ausgangspunkt:** die Maschenregel und das Modell der Sättigung aus der Tabelle.

**Annahmen:** (i) In der Sättigung gilt das einfache Modell, $U_{CE}$ = 0,2 V; (ii) der Kollektorkreis besteht aus $U_{CC}$ und $R_C$.

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
**Gegeben:** Beispieltransistor mit $B$ = 500, Kollektor über $R_C$ = 2,2 kΩ an $U_{CC}$ = 10 V, Emitter an Masse; eine Stromquelle gibt den Basisstrom vor: 0, 2, 8 und 20 µA. Modellwerte: 0,6 V und 0,2 V.

**Gesucht:** Bereich, Kollektorstrom und $U_{CE}$ für jeden Basisstrom.

**Rechnung:** Ohne Basisstrom sperrt der Transistor: kein Kollektorstrom, $U_{CE}$ = 10 V. Bei 2 µA, Annahme aktiv:

$$I_C = 500\cdot2\ \mu\mathrm{A} = 1{,}00\ \mathrm{mA}, \qquad U_{CE} = 10\ \mathrm{V} - 2{,}2\ \mathrm{k\Omega}\cdot1{,}00\ \mathrm{mA} = 7{,}8\ \mathrm{V}$$

Das ist mehr als 0,2 V; die Annahme hält. Bei 8 µA ebenso:

$$I_C = 4{,}00\ \mathrm{mA}, \qquad U_{CE} = 10\ \mathrm{V} - 8{,}8\ \mathrm{V} = 1{,}2\ \mathrm{V}$$

Bei 20 µA verlangte die Annahme aktiv 10 mA und damit 22 V am Widerstand; $U_{CE}$ wäre −12 V, ein Widerspruch. Annahme Sättigung:

$$I_C = \frac{10\ \mathrm{V} - 0{,}2\ \mathrm{V}}{2{,}2\ \mathrm{k\Omega}} = 4{,}46\ \mathrm{mA} \le 500\cdot20\ \mu\mathrm{A} = 10\ \mathrm{mA}$$

Die Probe hält.

**Ergebnis:** **0 µA: gesperrt, 10 V; 2 µA: aktiv, 1,00 mA bei 7,8 V; 8 µA: aktiv, 4,00 mA bei 1,2 V; 20 µA: gesättigt, 4,45 mA bei 0,2 V.**

**Einordnung:** Die Grenze liegt bei 8,9 µA; darüber steigt der Kollektorstrom nicht mehr. Bei 20 µA ist der Transistor 2,2-fach übersteuert: Er könnte 10 mA liefern, der Widerstand lässt 4,45 mA zu. Das vollständige Transistormodell ergibt hier 0,144 V und 4,48 mA; die einfache Rechnung trifft den Strom also gut.
::::

:::frage
„Warum liegt die Grenze bei 0,2 V und nicht dort, wo $U_{CB}$ null wird?“
Bei $U_{CB}$ = 0, beim Beispieltransistor mit 8 µA also bei 0,69 V, liegt am Basis-Kollektor-Übergang keine Spannung: Er sammelt die ankommenden Elektronen weiter ein, schickt aber selbst keine Ladungsträger zurück. In Durchlassrichtung leitet ein pn-Übergang merklich erst ab etwa 0,45 bis 0,5 V, und dann ist $U_{CE}$ auf 0,2 bis 0,25 V gesunken. Beim Beispieltransistor mit 8 µA Basisstrom fließen bei 0,3 V erst 0,25 % des Basisstroms über den Basis-Kollektor-Übergang ab, bei 0,25 V 1,7 %, bei 0,2 V 11 % und bei 0,145 V die Hälfte. Oberhalb von etwa 0,25 V arbeitet der Transistor deshalb praktisch wie im aktiven Bereich, obwohl sein Kollektor schon tiefer liegt als die Basis; die 0,2 V des einfachen Modells liegen dort, wo die Sättigung merklich einsetzt.
:::

:::grafik
Szene: get1/bipolartransistoren/01-saettigung-fluesse · Vorlage: querschnitt-traegerfluesse
**Abbildung 8:** Trägerflüsse im Beispieltransistor in der Sättigung bei 20 µA Basisstrom, schematisch wie Abbildung 1: Beide Übergänge leiten ($U_{BE}$ = 0,696 V, $U_{BC}$ = 0,552 V, $U_{CE}$ = 0,144 V). Der Elektronenstrom vom Emitter zum Kollektor ist kaum verändert (4,5 mA); von den 20 µA Basisstrom ersetzen 9,6 µA die Verluste durch Rückinjektion und Rekombination, 10,4 µA fließen als Löcher über den Basis-Kollektor-Übergang in den Kollektor (roter Pfeil). Die Elektronendichte am Kollektorrand der Basis steigt nur auf 0,4 % der Randdichte am Emitter. Der überschüssige Basisstrom fließt in den Kollektor ab, statt den Kollektorstrom zu erhöhen.
:::

:::fehlvorstellung
„In der Sättigung liefert der Transistor seinen größten Strom.“
Das liegt nahe, weil Sättigung im Alltag „mehr geht nicht“ bedeutet. Den Strom begrenzt aber der Kollektorkreis, nicht der Transistor: Im Beispiel könnte er mit 20 µA Basisstrom 10 mA liefern, der Widerstand lässt nur 4,45 mA zu. Mit einem kleineren Kollektorwiderstand flösse beim selben Basisstrom mehr. Kennzeichen der Sättigung sind die kleine Spannung $U_{CE}$ und ein Kollektorstrom unter $B\,I_B$, nicht ein großer Strom.
:::

## Der Transistor als Schalter

*Wie viel Basisstrom braucht ein Transistor, damit er sicher durchschaltet?*

Als __Schalter__ wechselt der Transistor zwischen Sperrbereich und Sättigung. Gesperrt fließt fast kein Strom, gesättigt liegen nur 0,1 bis 0,2 V an ihm; in beiden Zuständen ist die __Verlustleistung__, das Produkt aus $U_{CE}$ und Kollektorstrom, klein. Er schaltet ohne bewegte Teile und deshalb ohne Verschleiß.

Damit er sicher sättigt, muss die Sättigungsbedingung auch für das Exemplar mit der kleinsten Stromverstärkung seines Typs gelten, beim BC547C 420, gemessen bei 2 mA. Bei größeren Strömen kann $B$ noch kleiner sein, typisch 300 bei 100 mA. Man setzt deshalb $B_\mathrm{min}$ statt $B$ ein und gibt das Zwei- bis Fünffache des so berechneten Basisstroms, die __Übersteuerung__. Sie deckt den Rückgang von $B$ bei größeren Strömen, Temperatur und Alterung ab und senkt $U_{CE}$ unter die 0,2 V des Modells.

::::beispiel Leuchtdiode an einem 3,3-V-Mikrocontroller
**Gegeben:** Ein Mikrocontroller-Ausgang liefert 3,3 V. Eine rote Leuchtdiode mit 2,0 V bei 20 mA soll an 5 V leuchten. Transistor BC547C mit $B_\mathrm{min}$ = 420 (Datenblatt); Modellwerte $U_{CE,\mathrm{sat}}$ = 0,2 V und $U_{BE}$ = 0,7 V; Übersteuerung fünffach; Widerstände aus der Normreihe E12.

:::grafik
Szene: get1/bipolartransistoren/01-led-schalter · Vorlage: schaltplan
**Abbildung 9:** Schaltplan: Mikrocontroller-Ausgang (3,3 V) über $R_B$ = 12 kΩ an die Basis eines BC547C, Emitter an Masse; vom Kollektor über $R_C$ = 150 Ω und die Leuchtdiode an +5 V. Eingetragen: Basisstrom 0,217 mA, Kollektorstrom 18,7 mA, $U_{CE}$ um 0,1 V. Ein Ausgangsstrom von einem Prozent des Laststroms schaltet die Leuchtdiode.
:::

**Gesucht:** Kollektor- und Basiswiderstand, Basisstrom, Verlustleistung im Transistor.

**Rechnung:** Kollektorwiderstand aus der Masche über Versorgung, Leuchtdiode, Widerstand und Transistor (Abbildung 9):

$$R_C = \frac{5\ \mathrm{V} - 2{,}0\ \mathrm{V} - 0{,}2\ \mathrm{V}}{20\ \mathrm{mA}} = 140\ \Omega \;\rightarrow\; 150\ \Omega, \qquad I_C = \frac{2{,}8\ \mathrm{V}}{150\ \Omega} = 18{,}7\ \mathrm{mA}$$

Basisstrom mindestens und mit Übersteuerung:

$$I_{B,\mathrm{min}} = \frac{18{,}7\ \mathrm{mA}}{420} = 44{,}4\ \mu\mathrm{A}, \qquad 5\cdot44{,}4\ \mu\mathrm{A} = 0{,}222\ \mathrm{mA}$$

Basiswiderstand und tatsächlicher Basisstrom:

$$R_B = \frac{3{,}3\ \mathrm{V} - 0{,}7\ \mathrm{V}}{0{,}222\ \mathrm{mA}} = 11{,}7\ \mathrm{k\Omega} \;\rightarrow\; 12\ \mathrm{k\Omega}, \qquad I_B = \frac{2{,}6\ \mathrm{V}}{12\ \mathrm{k\Omega}} = 0{,}217\ \mathrm{mA}$$

Verlustleistung mit den Modellwerten, im Kollektorkreis und an der Basis-Emitter-Strecke:

$$P_{CE} = 0{,}2\ \mathrm{V}\cdot18{,}7\ \mathrm{mA} = 3{,}7\ \mathrm{mW}, \qquad P_{BE} = 0{,}7\ \mathrm{V}\cdot0{,}217\ \mathrm{mA} = 0{,}15\ \mathrm{mW}$$

**Ergebnis:** **150 Ω und 12 kΩ; der Ausgang liefert 0,217 mA, der Transistor schaltet 18,7 mA und setzt rund 3,9 mW in Wärme um.**

**Einordnung:** Der Ausgang muss nur ein Prozent des Laststroms liefern. Das vollständige Transistormodell ergibt bei dieser 4,9-fachen Übersteuerung $U_{CE}$ = 0,11 V, 19,3 mA und zusammen 2,3 mW; die 0,2 V des einfachen Modells liegen auf der sicheren Seite. Auch ein kleineres $B$ bei 18,7 mA ist gedeckt: Selbst mit 300 statt 420 bliebe die Übersteuerung mehr als dreifach.
::::

:::frage
„Wie schnell schaltet ein Transistor?“
Einschalten geht schnell: Beim Modelltransistor brauchen die Elektronen für die Basis 60 ps. Beim BC547 fällt die Stromverstärkung für schnelle Signale bei typisch 300 MHz auf 1; das entspricht einer Verzögerung von rund 0,5 ns, zusammengesetzt aus der Transitzeit, die beim realen Transistor länger ist, und dem Umladen der Sperrschichtkapazitäten. Langsamer ist das Ausschalten aus der Sättigung. Zuerst muss die überschüssige Ladung abfließen, die der leitende Basis-Kollektor-Übergang vor allem in den Kollektor gebracht hat, und so lange bleibt der Transistor leitend. Diese __Speicherzeit__ beträgt beim ähnlichen 2N3904 laut Datenblatt bis zu 200 ns, gemessen bei 10 mA Kollektorstrom mit 1 mA Basisstrom zum Einschalten und 1 mA zum Ausräumen. Eine große Übersteuerung kostet deshalb Schaltgeschwindigkeit.
:::

## Der pnp-Transistor

*Was ändert sich, wenn man die Dotierfolge umkehrt?*

Beim pnp-Transistor sind Emitter und Kollektor p-dotiert, die Basis n-dotiert (Abbildung 2b). Den Transferstrom tragen jetzt Löcher: Der Basis-Emitter-Übergang lässt sie aus dem Emitter in die Basis, sie diffundieren hindurch, und der gesperrte Basis-Kollektor-Übergang sammelt sie ein. Damit kehren sich alle Spannungen und Ströme um. Im Betrieb liegt der Emitter höher als die Basis und die Basis höher als der Kollektor; der Strom fließt in den Emitter hinein und aus Basis und Kollektor heraus. Das Symbol zeigt es mit dem Emitterpfeil nach innen.

Hier zählt man die Ströme beim pnp-Transistor in dieser Flussrichtung (Abbildung 2b), sodass sie im Betrieb positiv sind, und behält die Richtungen der Spannungen bei. $U_{BE}$ und $U_{CE}$ werden dadurch negativ, mit $U_{BE,\mathrm{ein}}$ = −0,6 V und $U_{CE,\mathrm{sat}}$ = −0,2 V:

| Bereich | Modell | Probe |
|---|---|---|
| Sperrbereich | $I_B$ = $I_C$ = 0 | $U_{BE}$ > −0,6 V |
| aktiv | $U_{BE}$ = −0,6 V, $I_C$ = $B\,I_B$ | $U_{CE}$ ≤ −0,2 V |
| Sättigung | $U_{BE}$ = −0,6 V, $U_{CE}$ = −0,2 V | $I_C$ ≤ $B\,I_B$ |

Die Ungleichungen für die Spannungen kehren sich um, die für die Ströme nicht, weil die Ströme in ihrer Flussrichtung gezählt werden. Falsch wäre es, für die Sättigung zu verlangen, dass $I_C$ mindestens $B\,I_B$ ist. Das stimmt nur, wenn man die Ströme wie beim npn-Transistor in den Transistor hinein zählt, wo sie negativ werden; mit Pfeilen in Flussrichtung wie in Abbildung 2b gilt wie beim npn-Transistor, dass $I_C$ höchstens $B\,I_B$ ist. Auch bei der Dotierung bleibt die Reihenfolge: Bei beiden Typen ist der Kollektor am schwächsten dotiert, aus den Gründen, die der Frage-Kasten zum Inversbetrieb nennt.

Gebraucht wird der pnp-Transistor, wo der Strom von der positiven Versorgung aus geschaltet werden soll, etwa wenn die Last an Masse liegt, und in Gegentaktstufen: Ein npn- und ein pnp-Transistor übernehmen abwechselnd die positive und die negative Halbwelle, wie in der Endstufe eines einfachen Audioverstärkers. Der Komplementärtyp zum BC547C ist der BC557C.

::::beispiel pnp-Transistor schaltet eine Last an 5 V
**Gegeben:** Emitter an +5 V, Last 100 Ω vom Kollektor nach Masse; BC557C mit $B_\mathrm{min}$ = 420; Basis über $R_B$ an einem Logikausgang, der 0 V (ein) oder 5 V (aus) liefert; Modellwerte $U_{BE}$ = −0,7 V und $U_{CE,\mathrm{sat}}$ = −0,2 V; Übersteuerung vierfach; Normreihe E12.

**Gesucht:** Laststrom, Basiswiderstand, Basis- und Emitterstrom; das Verhalten beim Ausschalten.

**Rechnung:** Laststrom in der Sättigung:

$$I_C = \frac{5\ \mathrm{V} - 0{,}2\ \mathrm{V}}{100\ \Omega} = 48\ \mathrm{mA}$$

Basisstrom, aus der Basis heraus zum Logikausgang, und Basiswiderstand:

$$I_{B,\mathrm{min}} = \frac{48\ \mathrm{mA}}{420} = 0{,}114\ \mathrm{mA}, \qquad R_B = \frac{5\ \mathrm{V} - 0{,}7\ \mathrm{V}}{4\cdot0{,}114\ \mathrm{mA}} = 9{,}4\ \mathrm{k\Omega} \;\rightarrow\; 10\ \mathrm{k\Omega}$$

$$I_B = \frac{4{,}3\ \mathrm{V}}{10\ \mathrm{k\Omega}} = 0{,}43\ \mathrm{mA}, \qquad I_E = 48\ \mathrm{mA} + 0{,}43\ \mathrm{mA} = 48{,}4\ \mathrm{mA}$$

Probe der Sättigung:

$$B_\mathrm{min}\,I_B = 420\cdot0{,}43\ \mathrm{mA} = 181\ \mathrm{mA} \ge 48\ \mathrm{mA}$$

Liefert der Ausgang 5 V, ist $U_{BE}$ = 0, und der Transistor sperrt.

**Ergebnis:** **48 mA durch die Last mit $R_B$ = 10 kΩ und 0,43 mA Basisstrom; mit 5 V an der Basis sperrt der Transistor.**

**Einordnung:** Alle Ströme sind positiv, weil sie in Flussrichtung gezählt werden; nur die Spannungen sind negativ. Ein 3,3-V-Ausgang könnte diesen Transistor nicht ausschalten: Zwischen Emitter und Ausgang lägen 1,7 V, die Emitter-Basis-Strecke leitet mit etwa 0,7 V, und durch $R_B$ flössen noch 0,1 mA, genug für 42 bis 50 mA Kollektorstrom.
::::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| dünne Basis | Fast jedes Elektron erreicht den Kollektor, bevor es rekombiniert. |
| gesperrter Kollektorübergang | Er sammelt jeden Nachschub ein, gleich wie hoch die Sperrspannung ist; daher die flachen Ausgangskennlinien. |
| Transfergleichung | Die Stufe am Emitter bestimmt den Nachschub, exponentiell in $U_{BE}$. |
| Basisstrom und Stromverstärkung | Zwei kleine Verluste an derselben Stufe, Rückinjektion und Rekombination; deshalb ein fester Bruchteil des Nachschubs. |
| Strom- und Spannungssicht | Beide Ströme wachsen mit derselben Stufe am Emitter; wer einen festlegt, legt beide fest. |
| Sättigung | Leitet auch der Kollektorübergang, fließt überschüssiger Basisstrom in den Kollektor ab, und der äußere Kreis begrenzt den Strom. |
| pnp-Transistor | Derselbe Mechanismus mit Löchern als Nachschub. |

Ein gesperrter pn-Übergang führt so viel Strom, wie Nachschub an Minoritätsträgern zu ihm gelangt; im Bipolartransistor liefert ein leitender Übergang diesen Nachschub durch eine sehr dünne Basis, sodass die Basis-Emitter-Spannung den Kollektorstrom exponentiell festlegt, die Kollektorspannung ihn kaum beeinflusst und nur ein kleiner, fester Bruchteil als Basisstrom fließt.

## Bedeutung und Ausblick

Bipolartransistoren verstärken etwa in Audioverstärkern die Signale, schalten Leuchtdioden, Relais und Motoren und stecken in analogen Schaltkreisen wie Operationsverstärkern; digitale Schaltkreise bestehen dagegen fast ganz aus MOSFETs, die der Artikel [Der MOSFET](/wissen/elektrotechnik/4-semester/grundlagen-elektronischer-materialien-und-bauelemente/bauelemente/mosfet.html) behandelt. Im aktiven Bereich ist der Transistor eine gesteuerte Stromquelle, zwischen Sperrbereich und Sättigung ein Schalter; beides beruht auf demselben Nachschub durch die dünne Basis.

Die Grenzen des einfachen Modells zeigen sich in der Steigung der Ausgangskennlinien (Early-Effekt) und bei kleinen Signalen; beides behandelt [Der Transistor als Verstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/transistor-als-verstaerker.html). Bei hohen Frequenzen begrenzen Transitzeit und Sperrschichtkapazitäten die Verstärkung. Der nächste Artikel, [Arbeitspunkt und Grundschaltungen des Transistors](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/arbeitspunkt-und-grundschaltungen.html), zeigt, wie man einen Transistor trotz der Streuung von $B$ und $I_S$ in einen festen Arbeitspunkt bringt.

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
A: Der gesperrte Basis-Kollektor-Übergang sammelt jedes ankommende Elektron ein, die Dichte am Kollektorrand der Basis ist bei jeder Sperrspannung null. Den Strom bestimmt die Randdichte am Emitter und damit $U_{BE}$; zwischen 1 und 10 V steigt er beim Beispieltransistor nur um 13 %.
F: Wie groß ist der Kollektorstrom des Beispieltransistors bei 0,70 V, und wie viel mehr Spannung verdoppelt ihn?
A: $10^{-14}$ A mal $\exp(0{,}70\ \mathrm{V}/25{,}85\ \mathrm{mV})$ ergibt 5,75 mA. Verdoppeln kostet 17,9 mV, verzehnfachen 59,5 mV.
F: Warum muss der Emitter viel stärker dotiert sein als die Basis, und warum muss die Basis dünn sein?
A: Die Löcher, die über den Basis-Emitter-Übergang in den Emitter gehen, sind proportional zu $N_B/N_E$; ein stark dotierter Emitter hält diese Rückinjektion klein. Die Rekombination in der Basis ist das Verhältnis von Transitzeit zu Lebensdauer; eine dünne Basis macht die Transitzeit klein, beim Beispieltransistor 60 ps gegen 80 ns.
F: Woraus ergibt sich beim Beispieltransistor eine Stromverstärkung von 500?
A: Auf 10 000 Elektronen am Kollektor kommen 12,5 Löcher Rückinjektion und 7,6 rekombinierte Elektronen, zusammen rund 20 Löcher, die über die Basis nachfließen; 10 000 durch 20 ergibt 500. Damit ist $\alpha$ = 0,998.
F: Stimmt es, dass die Elektronen des Kollektorstroms über die Basis hereinkommen und der Basisstrom den Transistor öffnet?
A: Nein. Die Elektronen kommen aus dem Emitter und verlassen den Transistor am Kollektor; über den Basisanschluss fließen nur Löcher, die Verluste ersetzen, bei 2 mA Kollektorstrom 4 µA. Die Ursache ist $U_{BE}$; weil der Basisstrom eindeutig dazugehört, darf man trotzdem mit ihm rechnen.
F: Warum streut $B$ in der Fertigung so stark, obwohl $\alpha$ fast gleich bleibt?
A: $B$ ist $\alpha/(1 - \alpha)$ und hängt damit am kleinen Rest $1 - \alpha$. Sinkt er von 0,4 % auf 0,2 %, verdoppelt sich $B$ von 249 auf 499; deshalb werden Transistoren in Gruppen sortiert, beim BC547C 420 bis 800.
F: In welchem Bereich arbeitet der Beispieltransistor mit 2,2 kΩ an 10 V bei 20 µA Basisstrom?
A: Annahme aktiv verlangte 10 mA und $U_{CE}$ = −12 V, ein Widerspruch. Annahme Sättigung: 9,8 V durch 2,2 kΩ ergibt 4,45 mA, weniger als 500 mal 20 µA; die Probe hält, der Transistor ist gesättigt.
F: Stimmt es, dass der Transistor in der Sättigung seinen größten Strom liefert?
A: Nein. In der Sättigung begrenzt der äußere Kreis den Strom unter $B\,I_B$; im Beispiel könnte der Transistor 10 mA liefern, der Widerstand lässt 4,45 mA zu. Der überschüssige Basisstrom fließt über den leitenden Basis-Kollektor-Übergang in den Kollektor ab.
F: Was ändert sich beim pnp-Transistor, und welche Sättigungsbedingung gilt für Ströme in Flussrichtung?
A: Dotierung, Ladungsträger, Spannungen und Ströme kehren sich um; $U_{BE,\mathrm{ein}}$ und $U_{CE,\mathrm{sat}}$ sind negativ. Mit den Strömen in Flussrichtung wie in Abbildung 2b gilt in der Sättigung wie beim npn-Transistor, dass $I_C$ höchstens $B\,I_B$ ist; „mindestens“ stimmt nur für hineingezählte, negative Ströme.
:::
