---
title: Bipolartransistor: Arbeitsbereiche und Transportmodell
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / Bipolartransistor
order: 33040100
summary: Wie der Bipolartransistor als spannungsgesteuerte Stromquelle mit einem kleinen Basisstrom arbeitet und wie das Transportmodell mit zwei Dioden und einer gesteuerten Quelle alle fünf Betriebszustände beschreibt. Ausführliche Fassung mit diskretem und integriertem Aufbau, Zählpfeilen, Kennlinien, Sättigung aus dem Transportmodell, Early-Effekt mit Basisweitenmodulation, Gummel-Plot und Großsignalmodell mit Bahnwiderständen, durchgerechnet an einem integrierten Beispieltransistor.
tags: Bipolartransistor, Arbeitsbereich, Transportmodell, Ebers-Moll, Early-Effekt
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Ein MOSFET steuert seinen Strom über eine Kapazität, ohne Steuerstrom; dafür wächst der Strom nur mit dem Quadrat der Übersteuerung, und man braucht ein Volt Übersteuerung für wenige Milliampere. Der __Bipolartransistor__ steuert seinen Strom über einen leitenden pn-Übergang: exponentiell, 60 mV für den Faktor zehn, mit zwanzigmal mehr Steilheit, also Stromänderung je Volt Steuerspannung, bei gleichem Strom, aber mit einem Steuerstrom, der sich nie ganz vermeiden lässt. Um damit zu rechnen, braucht man ein Modell, das beide pn-Übergänge und alle Betriebszustände abdeckt. Alles hängt an einem Prinzip:

**Der Bipolartransistor ist eine spannungsgesteuerte Stromquelle mit einem Nebenstrom: Die Basis-Emitter-Spannung legt über eine Diodengleichung den Transportstrom vom Kollektor zum Emitter fest, die Basis liefert davon nur den festen Bruchteil $1/B_N$ als Basisstrom, und das Transportmodell fasst beide pn-Übergänge und beide Stromrichtungen in zwei Dioden und einer gesteuerten Quelle zusammen, sodass alle fünf Betriebszustände aus demselben Modell folgen.**

Vorausgesetzt werden der pn-Übergang und die Diodengleichung aus [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell-ausfuehrlich.html) und [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie-ausfuehrlich.html), der physikalische Transistoreffekt aus [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise-ausfuehrlich.html), gesteuerte Quellen als Netzwerkelemente aus [Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung-ausfuehrlich.html) und zum Vergleich die Kennlinien des MOSFET aus [Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien-ausfuehrlich.html). Darauf bauen das Kleinsignalmodell des Bipolartransistors, die bipolaren Grundschaltungen, Stromspiegel und Differenzverstärker auf.

:::grafik
Szene: st1/bipolartransistor/01-einstieg · Vorlage: querschnitt-mit-modell
**Abbildung 1:** Links der npn-Transistor im Normalbetrieb, schematisch: Emitter, dünne Basis, Kollektor, beide Raumladungszonen, die ladungsträgerarmen Zonen der Übergänge, grau. Elektronen (blau) laufen vom Emitter durch die Basis in den Kollektor, 1 mA; über den Basisanschluss kommen Löcher (rot) nach, 10 µA. Rechts das vereinfachte Transportmodell: eine Diode zwischen Basis und Emitter mit 10 µA und eine gesteuerte Stromquelle vom Kollektor zum Emitter mit 1 mA, gesteuert von $U_{BE}$ = 774 mV. Die Basis-Emitter-Spannung legt den Kollektorstrom fest; die Basis liefert nur ein Hundertstel davon.
:::

## Von Grund auf: Diode, Diffusion und gesteuerte Quelle

*Welche drei Dinge muss man kennen, bevor der Transistor verständlich wird?*

:::grafik
Szene: st1/bipolartransistor/01-grundlagen · Vorlage: grundlagen-dreiteilig
**Abbildung 2:** Die drei Grundbausteine. (a) Ein pn-Übergang als Diode mit $I_S$ = 10⁻¹⁶ A: links der Querschnitt mit p-Gebiet, n-Gebiet und grauer Raumladungszone, rechts die Kennlinie linear und halblogarithmisch, 1 mA bei 774 mV, zehnmal so viel je 59,5 mV mehr, in Sperrrichtung nur −10⁻¹⁶ A. (b) Diffusion: Elektronendichte (blau) in einer 0,1 µm dünnen p-Schicht, die von links hoch bis rechts null geradlinig abfällt; Pfeile zeigen den Teilchenstrom bergab, seine Stärke ist dem Gefälle proportional. (c) Das Schaltzeichen der spannungsgesteuerten Stromquelle als Raute mit dem Strom $I$ und einer gestrichelten Zuordnung zur Steuerspannung an anderer Stelle. Eine Diode, die Diffusion durch eine dünne Schicht und eine gesteuerte Quelle: Aus diesen drei Bausteinen besteht das ganze Modell des Bipolartransistors.
:::

### Die Diode: ein pn-Übergang leitet oder sperrt

Ein __pn-Übergang__ ist die Grenze zwischen einem p-dotierten Gebiet, in dem bewegliche Löcher die Ladung tragen, und einem n-dotierten Gebiet mit beweglichen Elektronen (Abbildung 2a); an der Grenze liegt die __Raumladungszone__, ein schmaler Streifen ohne bewegliche Ladungsträger, in dem eine Spannungsstufe die beiden Sorten voneinander fernhält ([Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell-ausfuehrlich.html)). Legt man die p-Seite ein paar Zehntel Volt über die n-Seite, sinkt diese Stufe, und der Strom wächst exponentiell mit der Spannung: Das ist die __Diodengleichung__ mit dem __Sättigungsstrom__ $I_S$ als Vorfaktor und der Temperaturspannung $U_T$ = 25,85 mV als Maßstab,

$$I = I_S\,\Big(\exp\!\Big(\frac{U}{U_T}\Big) - 1\Big)$$

Eine Diode mit $I_S$ = 10⁻¹⁶ A führt bei 774 mV genau 1 mA, bei 833 mV schon 10 mA: Je 59,5 mV mehr verzehnfachen den Strom. Liegt die p-Seite unter der n-Seite, sperrt der Übergang, und es bleibt nur der winzige Sättigungsstrom, 10⁻¹⁶ A ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie-ausfuehrlich.html)). Der Bipolartransistor besteht aus zwei solchen Übergängen, und seine Gleichungen sind Diodengleichungen.

### Minoritätsträger und Diffusion

In einem p-Gebiet sind die Löcher die __Majoritätsträger__, die Sorte in der Überzahl; die wenigen Elektronen dort heißen __Minoritätsträger__. Ein leitender pn-Übergang schickt Elektronen aus dem n-Gebiet ins p-Gebiet und hebt ihre Dichte am Rand der Raumladungszone um denselben Faktor $\exp(U/U_T)$, der in der Diodengleichung steht. Weiter innen sind sie selten, und Teilchen wandern von Orten hoher Dichte zu Orten niedriger Dichte, ohne dass ein Feld sie zieht: __Diffusion__. Der Diffusionsstrom ist dem Dichtegefälle proportional (Abbildung 2b). In einer dünnen Schicht, beim Beispieltransistor 0,1 µm, fällt die Dichte geradlinig ab, und fast alle Elektronen erreichen die andere Seite, bevor sie mit einem Loch rekombinieren; die mittlere Strecke bis zur Rekombination, die __Diffusionslänge__, ist einige Mikrometer lang. Dieser Diffusionsstrom durch eine dünne Schicht ist der Kollektorstrom.

### Die gesteuerte Stromquelle

Ein Widerstand hat einen Strom, der von seiner eigenen Spannung abhängt. Eine __gesteuerte Stromquelle__ ist ein Netzwerkelement, dessen Strom eine Spannung oder ein Strom an anderer Stelle der Schaltung festlegt; gezeichnet wird sie als Raute mit einer gestrichelten Zuordnung zur Steuergröße (Abbildung 2c), und die Netzwerkanalyse behandelt sie wie jedes andere Element ([Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung-ausfuehrlich.html)). Beim Bipolartransistor fließt der Strom zwischen Kollektor und Emitter, gesteuert wird er von der Spannung zwischen Basis und Emitter, und das Steuergesetz ist die Diodengleichung von oben.

Mit diesen drei Bausteinen ist das Modell schon fast fertig: Zwei Dioden teilen sich eine dünne Schicht, durch die Elektronen diffundieren, und eine gesteuerte Quelle beschreibt diesen Strom. Die folgenden Abschnitte setzen das zusammen, vom Aufbau über den Normalbetrieb bis zum vollständigen Transportmodell.


## Aufbau: diskret und integriert

*Woraus besteht ein Bipolartransistor, und warum sieht er als Einzelbauteil anders aus als auf einem Chip?*

:::grafik
Szene: st1/bipolartransistor/01-aufbau-diskret-integriert · Vorlage: technologie-querschnitt
**Abbildung 3:** (a) Diskreter npn-Transistor: stark n-dotiertes Substrat als Kollektorkontakt auf der Rückseite, darauf die schwach n-dotierte Kollektorschicht, die p-dotierte Basis und der stark n-dotierte Emitter; Emitter- und Basiskontakt oben. (b) Integrierter npn-Transistor: p-Substrat, darin eine n-Wanne als Kollektor mit einer vergrabenen, stark n-dotierten Schicht und einem Kollektorkontakt oben, das p-Basisgebiet und der n⁺-Emitter darin; p⁺-Substratkontakte links und rechts; der pn-Übergang zwischen Substrat und Kollektor als gesperrte Diode. (c) Draufsicht von (b) mit der Emitterfläche 2 µm × 10 µm. Die vergrabene Schicht bringt den Kollektor nach oben, die gesperrte Substratdiode trennt die Transistoren voneinander, und die Emitterfläche ist der Skalierungsparameter.
:::

Ein Bipolartransistor besteht aus drei dotierten Gebieten, die zwei pn-Übergänge bilden. __Dotierung__ heißt, dass in das Silizium Fremdatome eingebaut sind, die bewegliche Elektronen (n-Gebiet) oder bewegliche Löcher (p-Gebiet) liefern; ein pn-Übergang ist die Grenzfläche zwischen beiden Sorten mit ihrer Raumladungszone, wie in [Halbleiter und das Bändermodell](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/halbleiter-und-baendermodell-ausfuehrlich.html) beschrieben. Beim __npn-Transistor__ ist die Folge n, p, n: Der __Emitter__ ist stark n-dotiert, die __Basis__ schwach p-dotiert und dünn, der __Kollektor__ schwach n-dotiert. Weil sowohl Elektronen als auch Löcher zum Strom beitragen, heißt das Bauelement „bipolar“; im MOSFET trägt nur eine Sorte.

Abbildung 3a zeigt den diskreten Transistor: Das stark dotierte Substrat ist zugleich der Kollektorkontakt auf der Rückseite, großflächig und deshalb niederohmig, und Kollektor, Basis und Emitter werden Schicht für Schicht darauf aufgewachsen. Für einen Chip taugt dieser Aufbau nicht, denn alle Transistoren säßen auf demselben Substrat und hätten denselben Kollektor. Der integrierte Transistor in Abbildung 3b löst das mit einer n-Wanne im p-Substrat: Eine __vergrabene Schicht__, englisch buried layer, eine stark n-dotierte Lage am Boden der Wanne, verbindet den eigentlichen Kollektor unter dem Emitter niederohmig mit dem Kollektorkontakt, der jetzt oben neben der Basis liegt. Die Elektronen des Kollektorstroms laufen also senkrecht nach unten in die vergrabene Schicht, seitlich durch sie und wieder nach oben zum Kontakt.

Die Wanne und das p-Substrat bilden einen weiteren pn-Übergang, die __Substratdiode__. Das Substrat liegt über p⁺-Kontakte an der negativsten Versorgungsspannung der Schaltung; jeder Kollektor liegt höher, also ist diese Diode immer gesperrt, und durch sie fließt nur ihr Sperrstrom, bei einer Diode mit 10⁻¹⁵ A Sättigungsstrom also 10⁻¹⁵ A gegen 1 mA Kollektorstrom. So ist jeder Transistor von seinen Nachbarn und vom Substrat getrennt. Die Draufsicht in Abbildung 3c zeigt, was vom Transistor elektrisch zählt: Die aktive Fläche liegt unter dem Emitter, beim Beispieltransistor 2 µm × 10 µm = 20 µm². Die __Emitterfläche__ ist der Skalierungsparameter des Bipolartransistors, so wie das Verhältnis $W/L$ beim MOSFET: Alle Ströme sind ihr proportional.

:::frage
„Warum muss das Substrat an die negativste Versorgung, warum nicht an Masse oder an die positive?“
Die Substratdiode liegt zwischen dem p-Substrat und jeder n-Wanne. Sie sperrt nur, wenn das Substrat tiefer liegt als jeder Kollektor. Läge das Substrat auf Masse und ein Kollektor im Betrieb darunter, etwa bei −1 V in einer Schaltung mit ±2,5 V, würde diese Diode leiten, und der Kollektorstrom flösse ins Substrat statt zum Kontakt, dazu in die Wannen der Nachbarn. Bei einer Versorgung aus nur einer positiven Spannung ist Masse zugleich die negativste Spannung, und das Substrat liegt dort.
:::

## Schaltsymbol, Zählpfeile und Vorzeichen

*Wie zählt man Ströme und Spannungen am Transistor, damit alle Formeln ohne Sonderfälle gelten?*

:::grafik
Szene: st1/bipolartransistor/01-symbole-zaehlpfeile · Vorlage: aufbau-und-symbol
**Abbildung 4:** (a) npn-Transistor: Schichtfolge n, p, n mit den beiden pn-Übergängen als Dioden, die Emitterdiode von der Basis zum Emitter, die Kollektordiode von der Basis zum Kollektor; daneben das Schaltsymbol mit dem Emitterpfeil nach außen. Zählpfeile: $I_B$ und $I_C$ in den Transistor hinein, $I_E$ ebenfalls hinein gezählt und deshalb negativ; Spannungen $U_{BE}$, $U_{CE}$ und $U_{BC}$. Werte im Normalbetrieb: $U_{BE}$ = 0,774 V, $U_{CE}$ = 2,5 V, $U_{BC}$ = −1,73 V, $I_B$ = 10 µA, $I_C$ = 1,05 mA, $I_E$ = −1,06 mA. (b) pnp-Transistor: Schichtfolge p, n, p, Emitterpfeil nach innen, dieselben Zählpfeile; alle Werte mit umgekehrtem Vorzeichen. Alle Ströme werden in den Transistor hinein gezählt, deshalb ist der Emitterstrom des npn negativ; der pnp ist derselbe Transistor mit umgekehrten Vorzeichen.
:::

Abbildung 4a zeigt die beiden pn-Übergänge des npn-Transistors als Dioden: Die __Emitterdiode__ liegt zwischen Basis und Emitter, die __Kollektordiode__ zwischen Basis und Kollektor, beide mit der Anode an der Basis. Im Schaltsymbol trägt nur der Emitter einen Pfeil; er zeigt die Richtung, in der der Emitterstrom im Normalbetrieb tatsächlich fließt, beim npn aus dem Transistor heraus.

**Die Akteure:**

- __$I_B$__, __$I_C$__, __$I_E$__: Basis-, Kollektor- und Emitterstrom; alle drei werden in den Transistor hinein gezählt. Beim npn im Normalbetrieb sind $I_B$ und $I_C$ positiv, $I_E$ negativ; beim Beispieltransistor 10 µA, 1 mA und −1,01 mA.
- __$U_{BE}$__, __$U_{BC}$__, __$U_{CE}$__: Spannung von der Basis zum Emitter, von der Basis zum Kollektor und vom Kollektor zum Emitter; $U_{CE} = U_{BE} - U_{BC}$. Beim npn im Normalbetrieb ist $U_{BE}$ positiv und $U_{BC}$ negativ.

Dass auch der Emitterstrom hinein gezählt wird, obwohl er heraus fließt, hat einen Grund: Mit drei gleich gerichteten Zählpfeilen gilt die Knotenregel in ihrer knappsten Form, und dieselben Gleichungen beschreiben den npn- und den pnp-Transistor. Der __pnp-Transistor__ in Abbildung 4b hat die Schichtfolge p, n, p; bei ihm sind im Normalbetrieb alle Spannungen und Ströme negativ, der Emitterstrom fließt hinein und der Emitterpfeil zeigt nach innen. Alles Weitere in diesem Artikel ist für den npn-Transistor formuliert; für den pnp dreht man jedes Vorzeichen um.

:::formel Knotengleichung
$$I_E = -\big(I_B + I_C\big)$$
:::

**So liest man das:** Was an Basis und Kollektor hinein fließt, verlässt den Transistor am Emitter. Der Emitterstrom ist dem Betrag nach der größte der drei Ströme, beim Beispieltransistor 1,01 mA.

**Kurz gesagt:** Die Summe der drei in den Transistor hinein gezählten Ströme ist null.

Die Gleichung ist die Knotenregel für den Transistor als Ganzes: Er speichert im stationären Betrieb keine Ladung, also ist die Summe der zufließenden Ströme null.

## Wie die Basis-Emitter-Spannung den Kollektorstrom festlegt

*Warum fließt ein großer Strom durch einen gesperrten Übergang, und welche Rolle spielt dabei die Basis?*

:::grafik
Szene: st1/bipolartransistor/01-kennlinien · Vorlage: kennlinie-semilog-paar
**Abbildung 5:** Kennlinien des Beispieltransistors über $U_{BE}$ von 0,5 bis 0,9 V. (a) Übertragungskennlinie $I_C$ linear: 0,058 mA bei 0,70 V, 0,40 mA bei 0,75 V, 1,0 mA bei 0,774 V, 2,76 mA bei 0,80 V, 19 mA bei 0,85 V; Arbeitspunkt bei 1 mA. (b) Dieselbe Kennlinie halblogarithmisch von 10 nA bis 100 mA: eine Gerade mit 59,5 mV je Dekade. (c) Eingangskennlinie $I_B$: dieselbe Form mit einem Hundertstel der Werte, 10 µA bei 0,774 V und 27,6 µA bei 0,80 V. Übertragungs- und Eingangskennlinie sind dieselbe Exponentialfunktion, um den Faktor 100 verschoben; 60 mV mehr geben zehnmal so viel Strom.
:::

**Die Akteure:**

- __$I_S$__: __Transportsättigungsstrom__, der Vorfaktor der Diodengleichung des Kollektorstroms; in A; beim integrierten Beispieltransistor 10⁻¹⁶ A, proportional zur Emitterfläche.
- __$U_T$__: Temperaturspannung $kT/e$, 25,85 mV bei 300 K; eine Spannungsstufe dieser Höhe ändert jeden Strom um den Faktor $\exp(1) \approx 2{,}72$.
- __$B_N$__: __Stromverstärkung__ im Normalbetrieb, das Verhältnis von Kollektor- zu Basisstrom; dimensionslos; 100 beim Beispieltransistor. Der Index N steht für normal, zur Unterscheidung vom Inversbetrieb.
- __$A$__: Verhältnis von Kollektor- zu Emitterstrom mit Minuszeichen, $-I_C/I_E$; dimensionslos; 0,990.

**Das Zusammenspiel:**

**Schritt 1**: Die beiden Übergänge liegen mit entgegengesetzter Durchlassrichtung in Reihe. Legt man nur eine positive Spannung $U_{CE}$ an und lässt die Basis offen, sperrt die Kollektordiode, und es fließt nur ihr Sperrstrom; der Transistor sperrt.

**Schritt 2**: Eine Basis-Emitter-Spannung von 0,774 V senkt die Barriere der Emitterdiode. Elektronen aus dem stark dotierten Emitter diffundieren in die Basis, weil ihre Dichte dort am Rand der Raumladungszone um den Faktor $\exp(U_{BE}/U_T)$ steigt, hier um den Faktor 10¹³, wie bei jeder Diode ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie-ausfuehrlich.html)).

**Schritt 3** (entscheidender Schritt): Die Basis ist dünner als die Strecke, die ein Elektron im Mittel vor der Rekombination zurücklegt, beim integrierten Transistor 0,1 µm gegen einige Mikrometer. Fast alle Elektronen erreichen deshalb die Raumladungszone der gesperrten Kollektordiode, deren Feld sie in den Kollektor zieht. Der Kollektorstrom ist dieser Diffusionsstrom durch die Basis; er folgt der Diodengleichung mit $U_{BE}$, und $U_{CE}$ kommt darin nicht vor, solange die Kollektordiode sperrt.

**Schritt 4**: Die Basis muss nur ersetzen, was unterwegs verloren geht: die wenigen Elektronen, die in der Basis mit Löchern rekombinieren, und die Löcher, die aus der Basis in den Emitter injiziert werden ([Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise-ausfuehrlich.html) rechnet beides aus Dotierung und Basisweite vor). Beide Verluste wachsen mit demselben Faktor $\exp(U_{BE}/U_T)$ wie der Kollektorstrom, deshalb ist ihr Verhältnis zum Kollektorstrom fest: $1/B_N$, beim Beispieltransistor 10 µA zu 1 mA. Abbildung 5c ist darum Abbildung 5a mit einem Hundertstel der Werte.

:::formel Normalbetrieb
$$I_C = I_S\,\Big(\exp\!\Big(\frac{U_{BE}}{U_T}\Big) - 1\Big)$$

$$I_B = \frac{I_C}{B_N}$$

$$I_E = -\Big(1 + \frac{1}{B_N}\Big)\,I_C$$

$$A = -\frac{I_C}{I_E} = \frac{B_N}{1 + B_N}$$
:::

**So liest man das:** Eingabe ist die Basis-Emitter-Spannung, Ausgabe der Kollektorstrom; je 59,5 mV mehr verzehnfacht er sich, je 17,9 mV verdoppelt er sich. Die −1 ist nur bei Spannungen unter etwa 0,1 V spürbar; bei 0,774 V ist $\exp(U_{BE}/U_T)$ = 10¹³. Basis- und Emitterstrom folgen dem Kollektorstrom mit festen Faktoren; bei $B_N$ = 100 ist der Emitterstrom nur 1 % größer als der Kollektorstrom, und $A$ liegt bei 0,99. Für große $B_N$ sind Kollektor- und Emitterstrom dem Betrag nach fast gleich.

**Kurz gesagt:** Zehnmal so viel Kollektorstrom braucht 60 mV mehr Basis-Emitter-Spannung, bei jedem Ausgangsstrom gleich, solange die Diodengleichung gilt.

Idee der Herleitung: Der Kollektorstrom ist der Diffusionsstrom der Elektronen durch die Basis, also proportional zu ihrer Randdichte, und die wächst nach dem Gesetz des Übergangs exponentiell mit $U_{BE}$; Basis- und Emitterstrom folgen aus den Verlusten und der Knotenregel.

:::herleitung
**Ausgangspunkt:** Gesetz des Übergangs und Diffusionsstrom aus [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie-ausfuehrlich.html): Am Rand der Raumladungszone eines leitenden Übergangs ist die Dichte der Minoritätsträger, der seltenen Ladungsträgersorte des Gebiets, um $\exp(U/U_T)$ erhöht, und der Diffusionsstrom ist proportional zum Dichtegefälle. Die vollständige Rechnung mit Dotierung, Basisweite und Diffusionskonstante steht in [Der Bipolartransistor – Aufbau und Wirkungsweise](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/aufbau-und-wirkungsweise-ausfuehrlich.html).
**Annahmen:** (i) Normalbetrieb: Emitterdiode leitet, Kollektordiode sperrt; (ii) die Basis ist dünn gegen die Diffusionslänge der Elektronen, beim Beispiel 0,1 µm gegen einige Mikrometer, sodass die Rekombination in der Basis klein bleibt; (iii) schwache Injektion: Die Elektronendichte in der Basis bleibt klein gegen die Dotierung, beim Beispiel bis in den Bereich von 10 mA; (iv) stationärer Betrieb, keine Ladungsspeicherung.
**Schritt 1**: Elektronendichte am emitterseitigen Rand der Basis nach dem Gesetz des Übergangs, mit der Gleichgewichtsdichte $n_{B0}$ der Elektronen in der Basis:
$$n_B(0) = n_{B0}\,\exp\!\Big(\frac{U_{BE}}{U_T}\Big)$$
**Schritt 2**: Am kollektorseitigen Rand ist die Dichte praktisch null, weil das Feld der gesperrten Kollektordiode jedes ankommende Elektron abzieht; dazwischen fällt die Dichte nach (ii) geradlinig ab, über die Basisweite $W_B$. Das Gefälle ist $n_B(0)/W_B$.
**Schritt 3** (entscheidender Schritt): Der Diffusionsstrom der Elektronen durch die Basis ist proportional zu diesem Gefälle; mit der Emitterfläche $A_E$, der Diffusionskonstante $D_n$ und der Elementarladung $e$ gilt
$$I_C = e\,A_E\,D_n\,\frac{n_B(0)}{W_B} = \underbrace{\frac{e\,A_E\,D_n\,n_{B0}}{W_B}}_{I_S}\,\exp\!\Big(\frac{U_{BE}}{U_T}\Big)$$
Dieser Strom fließt vollständig in den Kollektor, nicht in die Basis, weil er die Basis nur durchquert. Die −1 der Diodengleichung ergibt sich, wenn man den Gleichgewichtsanteil $n_{B0}$ mitführt; sie ist nur ohne Durchlassspannung von Bedeutung.
**Schritt 4**: Die Basis liefert Löcher für zwei Verluste: Rekombination in der Basis und Injektion von Löchern in den Emitter. Beide sind proportional zur Überschussdichte $n_B(0)$ bzw. zur entsprechenden Randdichte im Emitter, also beide proportional zu $\exp(U_{BE}/U_T)$. Ihr Verhältnis zum Kollektorstrom ist deshalb eine Zahl, die nur von Dotierungen und Abmessungen abhängt:
$$I_B = \frac{I_C}{B_N}$$
**Schritt 5**: Knotenregel für den Transistor und Auflösen nach $I_E$ und $A$:
$$I_E = -(I_B + I_C) = -\Big(1 + \frac{1}{B_N}\Big)\,I_C$$
$$A = -\frac{I_C}{I_E} = \frac{1}{1 + 1/B_N} = \frac{B_N}{1 + B_N}$$
**Ergebnis:**
$$I_C = I_S\,\Big(\exp\!\Big(\frac{U_{BE}}{U_T}\Big) - 1\Big)$$
$$I_B = \frac{I_C}{B_N}$$

$$I_E = -\Big(1 + \frac{1}{B_N}\Big)\,I_C$$
**Woher die Faktoren kommen:** Die Exponentialfunktion stammt aus dem Gesetz des Übergangs (Schritt 1), $I_S$ aus Fläche, Diffusionskonstante, Gleichgewichtsdichte und Basisweite (Schritt 3): Eine dünnere Basis und eine größere Emitterfläche geben mehr Strom bei gleicher Spannung. $B_N$ ist das Verhältnis zweier Diffusionsströme, die mit derselben Exponentialfunktion wachsen (Schritt 4).
**Proben:** Einheit: A, weil $I_S$ in A ist. Grenzfall $U_{BE}$ = 0: $I_C$ = 0. Vorzeichen: $I_C$ > 0 in den Kollektor hinein, $I_E$ < 0. Zahlenwert: $I_S$ = 10⁻¹⁶ A, $U_{BE}$ = 773,8 mV: $\exp(29{,}93)$ = 10¹³, also 1,00 mA; $I_B$ = 10 µA, $I_E$ = −1,01 mA.
**Grenzen:** Leitet auch die Kollektordiode, fällt Annahme (i); dann gilt das Transportmodell (Abschnitt *Das Transportmodell*). Bei starker Injektion (iii) wächst der Strom langsamer als exponentiell, und bei kleinen Strömen kommt ein zusätzlicher Basisstrom aus der Raumladungszone hinzu.
:::

::::beispiel Ströme des Beispieltransistors im Normalbetrieb
**Gegeben:** Integrierter npn-Transistor mit $I_S$ = 10⁻¹⁶ A und $B_N$ = 100; $U_T$ = 25,85 mV; Kollektordiode gesperrt.

**Gesucht:** (a) die Basis-Emitter-Spannung für 1 mA Kollektorstrom sowie Basis- und Emitterstrom; (b) der Kollektorstrom bei 18 mV und bei 60 mV mehr.

**Rechnung:** (a) Diodengleichung nach $U_{BE}$ aufgelöst (die −1 ist bei 10¹³ bedeutungslos):

$$U_{BE} = U_T\,\ln\frac{I_C}{I_S} = 25{,}85\ \mathrm{mV}\cdot\ln\big(10^{13}\big)$$

$$U_{BE} = 25{,}85\ \mathrm{mV}\cdot29{,}93 = 773{,}8\ \mathrm{mV}$$

$$I_B = \frac{1\ \mathrm{mA}}{100} = 10\ \mathrm{\mu A}, \qquad I_E = -(1\ \mathrm{mA} + 10\ \mathrm{\mu A}) = -1{,}01\ \mathrm{mA}$$

(b) Jede Spannungsstufe multipliziert den Strom mit $\exp(\Delta U/U_T)$:

$$\exp\!\Big(\frac{18\ \mathrm{mV}}{25{,}85\ \mathrm{mV}}\Big) = 2{,}01, \qquad \exp\!\Big(\frac{60\ \mathrm{mV}}{25{,}85\ \mathrm{mV}}\Big) = 10{,}2$$

Also 2,0 mA bei 792 mV und 10,2 mA bei 834 mV.

**Ergebnis:** **773,8 mV für 1 mA, dazu 10 µA Basisstrom und −1,01 mA Emitterstrom; 18 mV mehr verdoppeln, 60 mV mehr verzehnfachen den Strom.**

**Einordnung:** Die ganze Spanne von 0,1 mA bis 10 mA liegt zwischen 714 und 833 mV; deshalb rechnet man von Hand oft mit einer festen Spannung um 0,7 bis 0,8 V. Der diskrete Transistor mit 10⁻¹⁴ A braucht für 1 mA nur 655 mV, vor allem wegen seiner 750-mal größeren Emitterfläche; der Faktor 100 im Strom kostet 119 mV.
::::

:::fehlvorstellung
„Der Basisstrom fließt durch den Transistor und wird $B_N$-fach verstärkt; der Kollektorstrom ist der verstärkte Basisstrom.“ Das liegt nahe, weil Datenblätter die Stromverstärkung an erster Stelle nennen und der Kollektorstrom in jeder Rechnung als $B_N$-faches des Basisstroms geschrieben wird. Tatsächlich fließt der Kollektorstrom vom Emitter durch die Basis in den Kollektor, ohne den Basisanschluss zu berühren; seine Größe bestimmt $U_{BE}$ über die Diodengleichung (Schritt 3). Der Basisstrom ersetzt nur Verluste und ist deshalb ein fester Bruchteil, 10 µA bei 1 mA. Beide Ströme haben dieselbe Ursache; die Gleichung mit $B_N$ verknüpft zwei Wirkungen, sie beschreibt keine Verstärkung eines Stroms.
:::

:::frage
„Wenn $U_{BE}$ den Strom festlegt, wozu braucht man dann überhaupt $B_N$?“
Weil der Basisstrom in jeder Schaltung von irgendwoher kommen muss. Die Quelle, die die Basis treibt, muss 10 µA liefern, und über einen Basiswiderstand von 10 kΩ fallen dabei 0,1 V ab, die an $U_{BE}$ fehlen; der Eingangswiderstand des Transistors ist endlich. In Stromspiegeln und Differenzverstärkern erzeugt der Basisstrom Fehler von der Größe $1/B_N$. Die Spannung steuert, der Strom ist der Preis dafür; $B_N$ sagt, wie hoch er ist.
:::

Die beiden Gebiete, die den Strom tragen, sind nicht gleichwertig. Vertauscht man Emitter und Kollektor, also leitet die Kollektordiode und sperrt die Emitterdiode, arbeitet der Transistor im __Inversbetrieb__: Der Kollektor injiziert Elektronen, der Emitter sammelt sie ein. Weil der Kollektor viel schwächer dotiert ist als die Basis es für eine gute Injektion bräuchte, geht ein großer Teil des Basisstroms in die Löcherinjektion vom Basis- ins Kollektorgebiet, und die Stromverstärkung $B_I$ ist klein, beim Beispieltransistor 2 statt 100. Der Inversbetrieb wird fast nie absichtlich benutzt, kommt aber in jedem gesättigten Transistor als Anteil vor; deshalb braucht das Modell ihn.

## Die fünf Betriebszustände

*Welche Zustände kann der Transistor einnehmen, und woran erkennt man sie?*

:::grafik
Szene: st1/bipolartransistor/01-arbeitsbereiche · Vorlage: zustandsebene-und-kennlinienfeld
**Abbildung 6:** (a) Die Ebene aus $U_{BE}$ und $U_{BC}$, je von −1 bis 1 V, in vier farbige Quadranten geteilt: gesperrt (beide negativ), aktiv normal ($U_{BE}$ > 0, $U_{BC}$ < 0), Sättigung (beide positiv), invers ($U_{BE}$ < 0, $U_{BC}$ > 0); der Ursprung ist der stromlose Zustand, die Diagonale $U_{BC}$ = $U_{BE}$ die Linie $U_{CE}$ = 0. Der Arbeitspunkt (0,774 V, −1,73 V) liegt im aktiven Quadranten, der Sättigungspunkt (0,797 V, 0,697 V) nahe der Diagonale. (b) Ausgangskennlinienfeld $I_C$ über $U_{CE}$ von 0 bis 3 V für $U_{BE}$ = 0,70, 0,75, 0,774 und 0,80 V: steiler Anstieg bis etwa 0,1 V, danach fast waagerechte Geraden mit schwacher Steigung; der Sättigungsbereich links der Grenze bei 0,1 bis 0,3 V ist grau hinterlegt. Welche der beiden Dioden leitet, legt den Betriebszustand fest; im Kennlinienfeld ist die Sättigung der schmale Streifen links, der aktive Bereich sind die flachen Geraden.
:::

Jede der beiden Dioden kann leiten oder sperren. Das gibt vier Zustände, dazu den Sonderfall ohne jede Spannung (Abbildung 6a):

| Zustand | Dioden (Emitter, Kollektor) | Verhalten |
|---|---|---|
| stromlos | beide 0 V | keine Ströme |
| gesperrt | sperrt, sperrt | nur Sperrströme, um 10⁻¹⁶ A; Schalter aus |
| aktiv (normal) | leitet, sperrt | Stromquelle, $I_C$ aus $U_{BE}$; Verstärker |
| Sättigung | leitet, leitet | $U_{CE}$ um 0,1 V, Strom vom äußeren Kreis begrenzt; Schalter ein |
| invers | sperrt, leitet | Emitter und Kollektor vertauscht, $B_I$ = 2; kaum genutzt |

Der aktive Zustand heißt auch Verstärkungsbereich oder vorwärtsaktiv; er ist der Zustand für alle Verstärkerschaltungen, und die Formeln des vorigen Abschnitts gelten genau dort. Im Ausgangskennlinienfeld (Abbildung 6b) erkennt man ihn an den fast waagerechten Kennlinien: $U_{CE}$ ändert den Strom kaum, weil die Kollektordiode sperrt, solange $U_{CE}$ größer als etwa $U_{BE}$ minus 0,5 V ist. Links davon, bei $U_{CE}$ unter etwa 0,3 V, liegt die Basis um mehr als 0,5 V über dem Kollektor, die Kollektordiode leitet, und die Kennlinien brechen steil ein: der __Sättigungsbereich__. Dort bestimmt der äußere Kreis den Strom, und der Transistor ist ein geschlossener Schalter mit rund 0,1 V Restspannung. Wie die beiden leitenden Dioden das zusammen bewirken, zeigt das Transportmodell im übernächsten Abschnitt.

:::fehlvorstellung
„Sättigung heißt beim Bipolartransistor dasselbe wie beim MOSFET: der flache Teil der Kennlinie.“ Das liegt nahe, weil beide Bauelemente ein Kennlinienfeld mit einem steilen und einem flachen Teil haben. Die Wörter sind aber vertauscht: Beim MOSFET heißt der flache Teil Sättigungs- oder Abschnürbereich und ist der Verstärkerbereich ([Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien-ausfuehrlich.html)); beim Bipolartransistor heißt der flache Teil aktiver Bereich, und Sättigung ist der steile Teil links, in dem beide Dioden leiten und der Transistor als Schalter mit 0,1 V Restspannung arbeitet. Der Verstärkerbereich des MOSFET entspricht also dem aktiven Bereich des Bipolartransistors, und der ohmsche Bereich des MOSFET der bipolaren Sättigung.
:::

:::frage
„Wie kann die Kollektordiode leiten, wenn $U_{CE}$ doch positiv ist, der Kollektor also über dem Emitter liegt?“
Für die Kollektordiode zählt $U_{BC}$, die Spannung von der Basis zum Kollektor, und nicht $U_{CE}$. Liegt die Basis bei 0,8 V und der Kollektor bei 0,1 V, ist $U_{CE}$ positiv, aber die Basis liegt 0,7 V über dem Kollektor, und die Diode von der Basis zum Kollektor leitet. Die Grenze liegt bei $U_{CE} = U_{BE} - U_{BC}$ mit $U_{BC}$ um 0,5 V, also bei $U_{CE}$ um 0,3 V.
:::

## Das Transportmodell

*Wie beschreibt man beide Übergänge und beide Stromrichtungen mit einem Modell?*

:::grafik
Szene: st1/bipolartransistor/01-transportmodell · Vorlage: ersatzschaltbild-paar
**Abbildung 7:** (a) Das Transportmodell: Von der Basis zum Kollektor die Kollektordiode mit dem Strom $I_{B,I}$, von der Basis zum Emitter die Emitterdiode mit $I_{B,N}$, zwischen Kollektor und Emitter die gesteuerte Stromquelle mit dem Transportstrom $I_T = B_N I_{B,N} - B_I I_{B,I}$, vom Kollektor zum Emitter gerichtet. Werte im Arbeitspunkt bei $U_{CE}$ = 2,5 V: $I_{B,N}$ = 10 µA, $I_{B,I}$ praktisch null, $I_T$ = 1,05 mA. (b) Das vereinfachte Transportmodell für den Normalbetrieb: nur die Emitterdiode mit $I_B$ und die Quelle $I_C = B_N I_B$; $I_E = -(1 + B_N)\,I_B$ = −1,01 mA ohne Early-Faktor. Zwei Dioden beschreiben die Basis, eine gesteuerte Quelle den Transportstrom durch sie; im Normalbetrieb bleiben eine Diode und eine Quelle übrig.
:::

Der vorige Abschnitt gilt nur, solange die Kollektordiode sperrt. In der Sättigung und im Inversbetrieb injiziert auch der Kollektor, und der Strom durch die Basis hat zwei Anteile mit entgegengesetzter Richtung. Das __Transportmodell__ in Abbildung 7a beschreibt beide Fälle zugleich: Es ist die Form des __Ebers-Moll-Modells__, mit der Schaltungssimulatoren rechnen.

**Die Akteure:**

- __$I_{B,N}$__: Strom der Emitterdiode, der Anteil des Basisstroms, der zur Injektion vom Emitter gehört; in A; 10 µA im Arbeitspunkt.
- __$I_{B,I}$__: Strom der Kollektordiode, der Anteil des Basisstroms, der zur Injektion vom Kollektor gehört; im Normalbetrieb praktisch null, in der Sättigung von der Größe von $I_{B,N}$.
- __$B_I$__: Stromverstärkung im Inversbetrieb; 2 beim Beispieltransistor.
- __$I_T$__: __Transportstrom__, der Strom, der tatsächlich vom Kollektor zum Emitter durch die Basis fließt; positiv in dieser Richtung; 1,05 mA im Arbeitspunkt.

**Das Zusammenspiel:** Jede der beiden Dioden injiziert nach ihrer eigenen Diodengleichung, und jede Injektion erzeugt zwei Ströme: den Strom, der die Basis durchquert und am anderen Übergang eingesammelt wird, und den Verluststrom, den die Basis nachliefern muss. Die Emitterinjektion liefert $B_N I_{B,N}$ als Transportstrom vom Kollektor zum Emitter, die Kollektorinjektion $B_I I_{B,I}$ in die Gegenrichtung; beide fließen durch dieselbe Basis, also zieht man sie ab. Die Basis sieht die Summe beider Verlustströme. Weil der Transportstrom in beide Richtungen durch dieselbe dünne Basis mit derselben Dotierung läuft, hat er in beiden Richtungen denselben Vorfaktor $I_S$; nur die Verluste, also $B_N$ und $B_I$, sind verschieden.

:::formel Transportmodell
$$I_{B,N} = \frac{I_S}{B_N}\Big(\exp\!\Big(\frac{U_{BE}}{U_T}\Big) - 1\Big), \qquad I_{B,I} = \frac{I_S}{B_I}\Big(\exp\!\Big(\frac{U_{BC}}{U_T}\Big) - 1\Big)$$

$$I_T = B_N\,I_{B,N} - B_I\,I_{B,I} = I_S\,\big[\exp(U_{BE}/U_T) - \exp(U_{BC}/U_T)\big]$$

$$I_B = I_{B,N} + I_{B,I}$$

$$I_C = I_T - I_{B,I}$$

$$I_E = -I_T - I_{B,N}$$
:::

**So liest man das:** Eingabe sind die beiden Diodenspannungen, Ausgabe alle drei Anschlussströme. Der Transportstrom ist die Differenz zweier Exponentialfunktionen; er hängt nur von den Spannungen ab, nicht von $B_N$ und $B_I$. Die Stromverstärkungen legen nur fest, wie viel Basisstrom jede Injektion kostet. Im Normalbetrieb ist $\exp(U_{BC}/U_T)$ winzig, $I_{B,I}$ wird $-I_S/B_I$, also −5·10⁻¹⁷ A, und das Modell schrumpft auf Abbildung 7b: eine Diode mit $I_B$ und eine Quelle mit $B_N I_B$. Die Schreibweise des Transportstroms über die beiden Basisströme sieht wie eine stromgesteuerte Quelle aus; sie ist nur die Umformung der rechten Seite, und die Quelle bleibt spannungsgesteuert.

**Kurz gesagt:** Der Basisstrom ist die Summe der Ströme beider Dioden, der Transportstrom die Differenz ihrer verstärkten Ströme.

Idee der Herleitung: Man überlagert die beiden Injektionen, die der Emitter und der Kollektor je nach ihrer Diodengleichung erzeugen, und zählt an jedem Anschluss zusammen, was ankommt.

:::herleitung
**Ausgangspunkt:** Die Diodengleichung des Normalbetriebs aus dem Abschnitt *Wie die Basis-Emitter-Spannung den Kollektorstrom festlegt*: Eine leitende Emitterdiode erzeugt den Transportstrom $I_S(\exp(U_{BE}/U_T) - 1)$ durch die Basis und den Verluststrom $1/B_N$ davon.
**Annahmen:** (i) Beide Übergänge sind unabhängig voneinander durch ihre Spannung beschrieben, und die Basis ist so dünn, dass der Transportstrom nur vom Dichtegefälle zwischen ihren beiden Rändern abhängt (dünne Basis); (ii) schwache Injektion an beiden Übergängen; (iii) Überlagerung: Die Elektronendichte in der Basis ist die Summe der Beiträge beider Ränder, weil die Diffusionsgleichung linear ist; (iv) stationär.
**Schritt 1**: Die Emitterdiode allein (Kollektordiode mit $U_{BC}$ = 0) liefert nach dem Ausgangspunkt
$$I_{T,N} = I_S\,\Big(\exp\!\Big(\frac{U_{BE}}{U_T}\Big) - 1\Big), \qquad I_{B,N} = \frac{I_{T,N}}{B_N}$$
**Schritt 2**: Die Kollektordiode allein ($U_{BE}$ = 0) injiziert Elektronen vom Kollektor in die Basis; sie diffundieren zum Emitter und werden dort eingesammelt. Das Dichtegefälle ist dasselbe wie in Schritt 1, nur gespiegelt, weil es durch dieselbe Basis mit derselben Gleichgewichtsdichte $n_{B0}$ und derselben Weite $W_B$ läuft; der Vorfaktor ist deshalb wieder $I_S$. Die Verluste sind andere, weil der Kollektor schwächer dotiert ist als der Emitter und mehr Löcher aus der Basis aufnimmt: Verstärkung $B_I$ statt $B_N$.
$$I_{T,I} = I_S\,\Big(\exp\!\Big(\frac{U_{BC}}{U_T}\Big) - 1\Big), \qquad I_{B,I} = \frac{I_{T,I}}{B_I}$$
**Schritt 3** (entscheidender Schritt): Nach (iii) addieren sich die Elektronendichten, also auch die Diffusionsströme. Der Strom von Schritt 1 fließt vom Kollektor zum Emitter, der von Schritt 2 umgekehrt; der Netto-Transportstrom vom Kollektor zum Emitter ist die Differenz:
$$I_T = I_{T,N} - I_{T,I} = I_S\,\big[\exp(U_{BE}/U_T) - \exp(U_{BC}/U_T)\big]$$
$$I_T = B_N\,I_{B,N} - B_I\,I_{B,I}$$
Die beiden −1 heben sich auf; die letzte Form folgt durch Einsetzen von Schritt 1 und 2.
**Schritt 4**: Zählen an den Anschlüssen. Die Basis liefert beide Verlustströme. In den Kollektor fließt hinein, was die Quelle aus ihm abzieht, abzüglich des Stroms, der von der Basis über die Kollektordiode in den Kollektor kommt, denn er stammt aus der Basis, nicht aus dem Kollektoranschluss. Am Emitter kommt der Transportstrom an und zusätzlich der Strom der Emitterdiode; beide verlassen den Transistor:
$$I_B = I_{B,N} + I_{B,I}$$

$$I_C = I_T - I_{B,I}$$
$$I_E = -I_T - I_{B,N}$$
**Ergebnis:**
$$I_T = I_S\,\big[\exp(U_{BE}/U_T) - \exp(U_{BC}/U_T)\big]$$
$$I_B = I_{B,N} + I_{B,I}$$

$$I_C = I_T - I_{B,I}$$
$$I_E = -I_T - I_{B,N}$$
**Woher die Faktoren kommen:** Das gemeinsame $I_S$ beider Richtungen stammt aus Schritt 2 (gleiche Basis, gleiches Gefälle); $B_N$ und $B_I$ aus den verschiedenen Verlusten der beiden Übergänge; das Minuszeichen im Transportstrom aus der Gegenrichtung in Schritt 3.
**Proben:** Knotenregel: Die Summe der drei Anschlussströme ist null, weil sich $I_{B,N}$, $I_{B,I}$ und $I_T$ in ihr paarweise aufheben. Normalbetrieb ($U_{BC}$ stark negativ): $I_{B,I} \to -I_S/B_I \approx 0$, und die Formeln des vorigen Abschnitts bleiben übrig. Zahlenwert: $U_{BE}$ = 773,8 mV, $U_{BC}$ = −1,73 V: $I_{B,N}$ = 10 µA, $I_{B,I}$ = −5·10⁻¹⁷ A, $I_T$ = 1,00 mA ohne und 1,05 mA mit Early-Effekt.
**Grenzen:** Bei starker Injektion (ii) wächst der Transportstrom langsamer als exponentiell; die Spannungsabhängigkeit der Basisweite kommt als Early-Faktor hinzu (Abschnitt *Der Early-Effekt*); Ladungsspeicherung bei schnellen Änderungen (iv) braucht zusätzliche Kapazitäten.
:::

::::beispiel Das Transportmodell im Normal- und im Inversbetrieb
**Gegeben:** Beispieltransistor mit $I_S$ = 10⁻¹⁶ A, $B_N$ = 100, $B_I$ = 2, $U_T$ = 25,85 mV, ohne Early-Effekt. (a) Normalbetrieb: $U_{BE}$ = 773,8 mV, $U_{BC}$ = −1,73 V. (b) Inversbetrieb: $U_{BC}$ = 773,8 mV, $U_{BE}$ = −1 V.

**Gesucht:** die Ströme beider Dioden, der Transportstrom und die drei Anschlussströme.

**Rechnung:** (a) Die Emitterdiode leitet, $\exp(U_{BE}/U_T)$ = 10¹³; die Kollektordiode sperrt, $\exp(U_{BC}/U_T)$ ist kleiner als 10⁻²⁹:

$$I_{B,N} = \frac{10^{-16}\ \mathrm A}{100}\cdot10^{13} = 10\ \mathrm{\mu A}, \qquad I_{B,I} = \frac{10^{-16}\ \mathrm A}{2}\cdot(0 - 1) = -5\cdot10^{-17}\ \mathrm A$$

$$I_T = 100\cdot10\ \mathrm{\mu A} - 2\cdot(-5\cdot10^{-17}\ \mathrm A) = 1{,}00\ \mathrm{mA}$$

$$I_B = 10\ \mathrm{\mu A}, \qquad I_C = I_T - I_{B,I} = 1{,}00\ \mathrm{mA}, \qquad I_E = -I_T - I_{B,N} = -1{,}01\ \mathrm{mA}$$

(b) Jetzt leitet die Kollektordiode mit demselben Faktor 10¹³, die Emitterdiode sperrt:

$$I_{B,I} = \frac{10^{-16}\ \mathrm A}{2}\cdot10^{13} = 0{,}50\ \mathrm{mA}, \qquad I_{B,N} \approx 0, \qquad I_T = -2\cdot0{,}50\ \mathrm{mA} = -1{,}00\ \mathrm{mA}$$

$$I_B = 0{,}50\ \mathrm{mA}, \qquad I_C = -1{,}00\ \mathrm{mA} - 0{,}50\ \mathrm{mA} = -1{,}50\ \mathrm{mA}, \qquad I_E = +1{,}00\ \mathrm{mA}$$

**Ergebnis:** **(a) 10 µA, 1,00 mA, −1,01 mA; (b) in den Emitter fließen 1,00 mA hinein, aus dem Kollektor 1,50 mA heraus; die Basis braucht dafür 0,50 mA: Stromverstärkung 2.**

**Einordnung:** In beiden Fällen fließt 1 mA durch die Basis, weil dieselbe Spannung an der jeweils leitenden Diode liegt und der Transportstrom nur von der Basis abhängt. Der Unterschied liegt im Preis: 10 µA Basisstrom im Normalbetrieb, 500 µA im Inversbetrieb. Ein Transistor, der versehentlich verkehrt herum eingebaut ist, arbeitet also, aber mit der Verstärkung 2.
::::

## Sättigung: beide Dioden leiten

*Warum bleibt der Kollektorstrom in der Sättigung stehen, obwohl mehr Basisstrom fließt, und woher kommt die kleine Restspannung?*

:::grafik
Szene: st1/bipolartransistor/01-saettigung-stroeme · Vorlage: mengenpfeile-schaltung
**Abbildung 8:** Der Beispieltransistor als Transportmodell in einer Schaltung: Basis aus einer Stromquelle mit 50 µA, Kollektor über 1 kΩ an 2,5 V, Emitter an Masse. Mengenpfeile mit Werten: 24,7 µA in die Emitterdiode, 25,3 µA in die Kollektordiode, Transportstrom 2,42 mA, Kollektorstrom 2,40 mA, Emitterstrom −2,45 mA; Spannungen 797 mV an der Emitterdiode, 697 mV an der Kollektordiode, $U_{CE}$ = 100 mV, 2,40 V am Widerstand. Daneben klein derselbe Transistor mit 10 µA Basisstrom im aktiven Bereich: Kollektordiode stromlos, $U_{CE}$ = 1,47 V, 1,03 mA. In der Sättigung teilt sich der Basisstrom auf beide Dioden; der Kollektorstrom bleibt bei dem Wert, den der Widerstand zulässt, und $U_{CE}$ ist die Differenz zweier Durchlassspannungen.
:::

**Die Akteure:**

- __$U_{CC}$__: Versorgungsspannung des Kollektorkreises; 2,5 V im Beispiel.
- __$R_L$__: Lastwiderstand zwischen Versorgung und Kollektor; 1 kΩ.
- __$U_\mathrm{CE,sat}$__: __Sättigungsspannung__, die Kollektor-Emitter-Spannung, die in der Sättigung übrig bleibt; beim Beispiel 100 mV bei 50 µA Basisstrom.

**Das Zusammenspiel:**

**Schritt 1**: Der Kollektorkreis lässt höchstens den Strom zu, bei dem die ganze Versorgung am Widerstand abfällt: Was der Transistor zieht, fehlt an $U_{CE}$. Mit 2,5 V und 1 kΩ sind das rund 2,4 mA, wenn am Transistor 0,1 V bleiben (Abbildung 8).

**Schritt 2**: Mehr Basisstrom hebt $U_{BE}$ und damit den Transportstrom; $U_{CE}$ sinkt. Bei 10 µA liegen noch 1,47 V am Transistor, die Kollektordiode ist mit $U_{BC}$ = −0,70 V gesperrt. Bei 23 µA sind es 217 mV, und die Kollektordiode hat mit 578 mV Durchlassspannung zu leiten begonnen.

**Schritt 3** (entscheidender Schritt): Ab jetzt teilt sich der Basisstrom. Was über die Kollektordiode abfließt, $I_{B,I}$, treibt den Transportstrom nicht, sondern senkt ihn sogar um $B_I I_{B,I}$. Bei 50 µA gehen 24,7 µA in die Emitterdiode und 25,3 µA in die Kollektordiode; der Transportstrom ist 2,42 mA, der Kollektorstrom 2,40 mA. Ohne Sättigung wären es 5 mA.

**Schritt 4**: Die beiden Dioden stellen sich so ein, dass genau der Strom fließt, den der Widerstand zulässt. Die Emitterdiode liegt bei 797 mV, die Kollektordiode bei 697 mV, und die Differenz ist die Sättigungsspannung: 100 mV. Mehr Basisstrom drückt sie nur noch logarithmisch, auf 75 mV bei 100 µA, und hebt den Kollektorstrom nur noch um das, was die kleinere Restspannung am Widerstand freigibt, von 2,40 auf 2,43 mA.

:::formel Sättigungsspannung
$$U_\mathrm{CE,sat} = U_T\,\ln\frac{1 + \dfrac{1 + I_C/I_B}{B_I}}{1 - \dfrac{I_C}{B_N\,I_B}}$$
:::

**So liest man das:** Eingabe ist das Verhältnis von Kollektor- zu Basisstrom, das der äußere Kreis erzwingt; Ausgabe die Restspannung. Nähert sich $I_C/I_B$ der Stromverstärkung $B_N$, geht der Nenner gegen null und die Spannung gegen unendlich: Das ist die Grenze zum aktiven Bereich. Je kleiner $I_C/I_B$, also je mehr Basisstrom bei gleichem Kollektorstrom, desto kleiner die Restspannung; bei offenem Kollektor bleiben $U_T \ln(1 + 1/B_I)$ = 10,5 mV. Ein kleines $B_I$ hält die Restspannung klein. Diese Form gilt ohne Early-Effekt; mit ihm sind es beim Beispiel 100,5 statt 100,6 mV bei 50 µA.

Idee der Herleitung: Man schreibt Kollektor- und Basisstrom des Transportmodells mit beiden Exponentialfunktionen, bildet ihr Verhältnis und löst nach dem Quotienten der beiden Exponentialfunktionen auf, der $\exp(U_{CE}/U_T)$ ist.

:::herleitung
**Ausgangspunkt:** das Transportmodell aus dem Abschnitt *Das Transportmodell*.
**Annahmen:** (i) beide Dioden leiten, sodass die −1 in beiden Diodengleichungen entfällt; (ii) kein Early-Effekt; (iii) der äußere Kreis gibt das Verhältnis $k = I_C/I_B$ vor.
**Schritt 1**: Abkürzungen für die beiden Exponentialfunktionen:
$$x = \exp\!\Big(\frac{U_{BE}}{U_T}\Big), \qquad y = \exp\!\Big(\frac{U_{BC}}{U_T}\Big)$$
$$\frac{x}{y} = \exp\!\Big(\frac{U_{BE} - U_{BC}}{U_T}\Big) = \exp\!\Big(\frac{U_{CE}}{U_T}\Big)$$
**Schritt 2**: Kollektor- und Basisstrom aus dem Transportmodell:
$$I_C = I_T - I_{B,I} = I_S\,x - I_S\,y\,\Big(1 + \frac{1}{B_I}\Big)$$
$$I_B = \frac{I_S\,x}{B_N} + \frac{I_S\,y}{B_I}$$
**Schritt 3** (entscheidender Schritt): Das Verhältnis $k = I_C/I_B$ einsetzen; $I_S$ kürzt sich:
$$x - y\,\Big(1 + \frac{1}{B_I}\Big) = k\,\Big(\frac{x}{B_N} + \frac{y}{B_I}\Big)$$
Nach $x$ und $y$ geordnet:
$$x\,\Big(1 - \frac{k}{B_N}\Big) = y\,\Big(1 + \frac{1 + k}{B_I}\Big)$$
**Schritt 4**: Auflösen und logarithmieren:
$$\exp\!\Big(\frac{U_{CE}}{U_T}\Big) = \frac{x}{y} = \frac{1 + (1 + k)/B_I}{1 - k/B_N}$$
**Ergebnis:**
$$U_\mathrm{CE,sat} = U_T\,\ln\frac{1 + (1 + I_C/I_B)/B_I}{1 - I_C/(B_N\,I_B)}$$
**Woher die Faktoren kommen:** Der Zähler stammt aus dem Strom der Kollektordiode, der den Kollektorstrom mindert und den Basisstrom erhöht; der Nenner aus dem Anteil des Basisstroms, der die Emitterdiode treibt. Der Logarithmus kommt daher, dass die Spannung der Exponent ist.
**Proben:** Einheit: V, weil der Logarithmus dimensionslos ist. Grenzfall $k \to B_N$: Nenner null, $U_{CE} \to \infty$, also kein Sättigungszustand; Grenzfall $k$ = 0: $U_T \ln(1 + 1/B_I)$ = 10,5 mV. Vorzeichen: positiv, weil der Zähler größer als der Nenner ist. Zahlenwert: $k$ = 48,0, $B_I$ = 2, $B_N$ = 100: Zähler 25,5, Nenner 0,520, Quotient 49,0, $\ln$ = 3,89, also 100,6 mV; numerisch mit Early-Effekt 100,5 mV.
**Grenzen:** Mit den Widerständen der Zuleitungen im Transistor, den Bahnwiderständen, beim Beispiel 20 Ω am Kollektor und 5 Ω am Emitter, kommt zur Restspannung ihr Spannungsabfall hinzu, bei 2,4 mA rund 60 mV; bei starker Injektion ändert sich der Transportstrom.
:::

::::beispiel Sättigung bei 50 µA Basisstrom
**Gegeben:** Beispieltransistor ($I_S$ = 10⁻¹⁶ A, $B_N$ = 100, $B_I$ = 2, $U_A$ = 50 V) mit der Basis an einer Stromquelle von 50 µA, dem Kollektor über $R_L$ = 1 kΩ an $U_{CC}$ = 2,5 V und dem Emitter an Masse.

**Gesucht:** die Aufteilung des Basisstroms, Kollektorstrom und Sättigungsspannung.

**Rechnung:** Im aktiven Bereich wären es 100 · 50 µA = 5 mA; der Widerstand lässt aber höchstens 2,5 mA zu. Also leiten beide Dioden, und die zwei Unbekannten $U_{BE}$ und $U_{BC}$ folgen aus zwei Gleichungen: Der Basisstrom ist 50 µA, und der Kollektorstrom ist $(U_{CC} - U_{CE})/R_L$. Die numerische Lösung ist $U_{BE}$ = 797,2 mV und $U_{BC}$ = 696,6 mV; Probe mit den Diodengleichungen:

$$I_{B,N} = \frac{10^{-16}\ \mathrm A}{100}\,\exp\!\Big(\frac{797{,}2}{25{,}85}\Big) = 24{,}7\ \mathrm{\mu A}, \qquad I_{B,I} = \frac{10^{-16}\ \mathrm A}{2}\,\exp\!\Big(\frac{696{,}6}{25{,}85}\Big) = 25{,}3\ \mathrm{\mu A}$$

Summe 50,0 µA. Transportstrom mit Early-Faktor $1 + 0{,}1\ \mathrm V/50\ \mathrm V$ und Kollektorstrom:

$$I_T = \big(100\cdot24{,}7 - 2\cdot25{,}3\big)\ \mathrm{\mu A}\cdot1{,}002 = 2{,}42\ \mathrm{mA}, \qquad I_C = 2{,}42\ \mathrm{mA} - 25{,}3\ \mathrm{\mu A} = 2{,}40\ \mathrm{mA}$$

Probe am Widerstand: 2,5 V − 2,40 mA · 1 kΩ = 0,10 V, und tatsächlich ist $U_{CE}$ = 797,2 − 696,6 = 100,6 mV. Über die geschlossene Formel mit $k$ = 2,40 mA / 50 µA = 48,0:

$$U_\mathrm{CE,sat} = 25{,}85\ \mathrm{mV}\cdot\ln\frac{1 + 49{,}0/2}{1 - 48{,}0/100}$$

$$U_\mathrm{CE,sat} = 25{,}85\ \mathrm{mV}\cdot\ln 49{,}0 = 100{,}6\ \mathrm{mV}$$

**Ergebnis:** **24,7 µA in die Emitterdiode, 25,3 µA in die Kollektordiode; $I_C$ = 2,40 mA statt 5 mA; $U_\mathrm{CE,sat}$ = 100 mV.**

**Einordnung:** Die Hälfte des Basisstroms ist in der Sättigung nutzlos, sie fließt über die Kollektordiode ab. Das stört einen Schalter nicht; es kostet nur Steuerstrom. Mit 100 µA sinkt die Restspannung auf 75 mV und der Strom steigt auf 2,43 mA: Ein Schalter wird durch mehr Basisstrom etwas besser, aber nur logarithmisch.

**Variation:** Mit 10 µA Basisstrom bleibt der Transistor aktiv: 1,03 mA, $U_{CE}$ = 1,47 V, Kollektordiode mit −0,70 V gesperrt. Die Grenze liegt bei etwa 24 µA, dem Quotienten aus 2,4 mA und 100.
::::

## Der Early-Effekt

*Warum steigt der Kollektorstrom im aktiven Bereich doch leicht mit der Kollektorspannung?*

:::grafik
Szene: st1/bipolartransistor/01-early-effekt · Vorlage: kennlinienfeld-extrapolation
**Abbildung 9:** (a) Ausgangskennlinien für $U_{BE}$ = 0,75, 0,774 und 0,80 V über $U_{CE}$ von −50 V bis 5 V mit Achsenbruch: Im aktiven Bereich sind sie Geraden, für 1 mA mit der Steigung 20 µS, also 1,00 mA bei 0 V, 1,02 mA bei 1 V, 1,05 mA bei 2,5 V und 1,10 mA bei 5 V; nach links verlängert treffen sich alle bei −$U_A$ = −50 V. (b) Die Basis im Querschnitt: Zwischen den beiden Raumladungszonen liegt die neutrale Basis der Weite $W_B$; bei $U_{CB}$ = 5 V dringt die Kollektor-Raumladungszone tiefer in die Basis als bei 1 V, und die neutrale Basis wird schmaler. Daneben der Elektronenverlauf in der Basis als Gerade, die bei kürzerer Basis steiler wird. Mehr Kollektorspannung verbreitert die Kollektor-Raumladungszone, verkürzt die Basis und steigert den Strom; alle Tangenten treffen sich bei −$U_A$.
:::

**Die Akteure:**

- __$W_B$__: neutrale Basisweite zwischen den beiden Raumladungszonen; beim integrierten Transistor um 0,1 µm. Sie steht im Nenner von $I_S$.
- __$U_A$__: __Early-Spannung__, die Spannung, bei der die verlängerten Ausgangskennlinien die Spannungsachse schneiden; 50 V beim Beispieltransistor. Sie entspricht $1/\lambda$ beim MOSFET, dessen Beispieltransistor mit λ = 0,1 1/V einer Early-Spannung von nur 10 V entspricht.

**Das Zusammenspiel:** Die Raumladungszone der gesperrten Kollektordiode wird breiter, je höher die Sperrspannung $U_{CB}$ ist, wie bei jeder Diode; sie wächst zu beiden Seiten, also auch in die Basis hinein (Abbildung 9b). Die neutrale Basis wird schmaler, das Dichtegefälle der Elektronen steiler, und nach der Herleitung des Kollektorstroms ist $I_S$ umgekehrt proportional zu $W_B$. Mehr Kollektorspannung heißt also mehr Strom bei gleicher $U_{BE}$. Der Effekt ist klein, weil die Zone vor allem in den schwach dotierten Kollektor wächst, aber messbar: 10 % zwischen 0 und 5 V beim Beispiel. Die Basisströme ändern sich dabei nicht, denn die Rückinjektion in den Emitter hängt nur von $U_{BE}$ ab, und die Rekombination in der kürzeren Basis nimmt sogar ab. Deshalb wächst mit $U_{CE}$ auch das Verhältnis $I_C/I_B$, von 100 auf 105 bei 2,5 V.

:::formel Early-Effekt
$$I_C = I_S\,\Big(\exp\!\Big(\frac{U_{BE}}{U_T}\Big) - 1\Big)\,\Big(1 + \frac{U_{CE}}{U_A}\Big)$$
:::

**So liest man das:** Zur Diodengleichung kommt ein Faktor, der linear mit $U_{CE}$ wächst; bei $U_{CE} = U_A$ hätte sich der Strom verdoppelt, bei $-U_A$ wäre er null, deshalb der gemeinsame Schnittpunkt. Je größer $U_A$, desto flacher die Kennlinien und desto besser die Stromquelle. Üblich ist $U_{CE}$ im Faktor; genauer wäre $U_{CB}$, denn die Sperrspannung der Kollektordiode treibt den Effekt, aber der Unterschied beträgt beim Beispiel nur $U_{BE}/U_A$, also 1,5 %.

**Kurz gesagt:** Im linearisierten Modell wächst der Kollektorstrom je Volt Kollektor-Emitter-Spannung um den Bruchteil $1/U_A$ seines Werts bei null Volt, beim Beispiel um ein Fünfzigstel.

Idee der Herleitung: Man lässt die Basisweite linear mit $U_{CB}$ schrumpfen, setzt sie in $I_S$ ein und linearisiert den Kehrwert.

:::herleitung
**Ausgangspunkt:** der Ausdruck für $I_S$ mit der Basisweite $W_B$ im Nenner aus der Herleitung des Kollektorstroms (Abschnitt *Wie die Basis-Emitter-Spannung den Kollektorstrom festlegt*) und die Sperrschichtweite einer Diode, die mit der Sperrspannung wächst ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie-ausfuehrlich.html)).
**Annahmen:** (i) Die Kollektor-Raumladungszone dringt mit wachsender Sperrspannung in die Basis ein; über den betrachteten Bereich genügt eine lineare Näherung; (ii) die Änderung der Basisweite ist klein gegen die Basisweite ($U_{CB} \ll U_A$); (iii) $U_{BE} \ll U_A$, sodass $U_{CB}$ durch $U_{CE}$ ersetzt werden darf.
**Schritt 1**: Lineare Näherung der Basisweite mit der Weite $W_{B0}$ bei $U_{CB}$ = 0 und der Early-Spannung als Maß für die Steigung:
$$W_B(U_{CB}) = W_{B0}\,\Big(1 - \frac{U_{CB}}{U_A}\Big), \qquad U_A = \frac{W_{B0}}{-\,\mathrm dW_B/\mathrm dU_{CB}}$$
Eine Zone, die bei 5 V um 1 % der Basisweite eindringt, ergibt $U_A$ = 500 V; beim Beispiel sind es 2 % je Volt, also 50 V.
**Schritt 2**: Einsetzen in $I_S$, das umgekehrt proportional zu $W_B$ ist:
$$I_S(U_{CB}) = \frac{I_{S0}}{1 - U_{CB}/U_A}$$
**Schritt 3** (entscheidender Schritt): Linearisieren nach (ii), denn $1/(1 - z) \approx 1 + z$ für kleine $z$:
$$I_C = I_{S0}\,\Big(\exp\!\Big(\frac{U_{BE}}{U_T}\Big) - 1\Big)\,\Big(1 + \frac{U_{CB}}{U_A}\Big)$$
**Schritt 4**: Nach (iii) darf die Basis-Emitter-Spannung gegen die Early-Spannung vernachlässigt werden:
$$U_{CB} = U_{CE} - U_{BE} \approx U_{CE}$$
**Ergebnis:**
$$I_C = I_S\,\Big(\exp\!\Big(\frac{U_{BE}}{U_T}\Big) - 1\Big)\,\Big(1 + \frac{U_{CE}}{U_A}\Big)$$
**Woher die Faktoren kommen:** Der Faktor stammt aus dem Nenner $W_B$ von $I_S$ (Schritt 2); $U_A$ ist eine Eigenschaft der Dotierungen: Je stärker die Basis und je schwächer der Kollektor dotiert ist, desto weniger dringt die Zone in die Basis ein und desto größer ist $U_A$.
**Proben:** Einheit: dimensionsloser Faktor. Grenzfall $U_A \to \infty$: Diodengleichung ohne Spannungsabhängigkeit. Vorzeichen: Der Strom wächst mit $U_{CE}$. Zahlenwert: $U_{CE}$ = 5 V, $U_A$ = 50 V: Faktor 1,10, also 1,10 mA statt 1,00 mA; die exakte Form $1/(1 - U_{CB}/U_A)$ gäbe mit $U_{CB}$ = 4,23 V den Faktor 1,092.
**Grenzen:** Bei großem $U_{CB}$ versagt (ii), und die Zone kann die Basis ganz durchdringen (Durchgriff, englisch punch-through); dann steigt der Strom steil an. Bei starker Injektion verschiebt der Transportstrom selbst die Zone.
:::

::::beispiel Kollektorstrom mit Early-Effekt
**Gegeben:** Beispieltransistor mit $I_S$ = 10⁻¹⁶ A, $U_A$ = 50 V und $B_N$ = 100 bei $U_{BE}$ = 773,8 mV.

**Gesucht:** Kollektorstrom und Verhältnis $I_C/I_B$ bei $U_{CE}$ = 1 V, 2,5 V und 5 V sowie die Steigung der Ausgangskennlinie.

**Rechnung:** Ohne Early-Effekt fließen 1,00 mA; der Basisstrom bleibt 10 µA:

$$I_C(1\ \mathrm V) = 1{,}00\ \mathrm{mA}\cdot1{,}02 = 1{,}02\ \mathrm{mA}, \qquad I_C(2{,}5\ \mathrm V) = 1{,}05\ \mathrm{mA}, \qquad I_C(5\ \mathrm V) = 1{,}10\ \mathrm{mA}$$

$$\frac{I_C}{I_B} = 102, \quad 105, \quad 110, \qquad \frac{\mathrm dI_C}{\mathrm dU_{CE}} = \frac{1{,}00\ \mathrm{mA}}{50\ \mathrm V} = 20\ \mathrm{\mu S}$$

**Ergebnis:** **1,02 mA, 1,05 mA und 1,10 mA; die Kennlinie steigt mit 20 µS, das entspricht 50 kΩ.**

**Einordnung:** Die Stromquelle ist nicht ideal, aber gut: 50 kΩ Innenwiderstand bei 1 mA. Der Beispiel-MOSFET der MOSFET-Artikel hat bei 1 mA und λ = 0,1 1/V nur 10 kΩ. Datenblätter nennen $B$ deshalb immer mit der Messbedingung $U_{CE}$, denn $I_C/I_B$ steigt bei 5 V um 10 %.
::::

## Gummel-Plot und Stromverstärkung

*Warum ist die Stromverstärkung im Datenblatt eine Kurve über dem Strom und keine Zahl?*

:::grafik
Szene: st1/bipolartransistor/01-gummel-plot · Vorlage: kennlinie-semilog-gestapelt
**Abbildung 10:** (a) Gummel-Plot: $I_C$ und $I_B$ logarithmisch von 10⁻¹² bis 10⁻¹ A über $U_{BE}$ von 0,4 bis 1,0 V. $I_C$ ist bis etwa 0,8 V eine Gerade mit 59,5 mV je Dekade und knickt darüber ab: 2,62 mA bei 0,80 V statt 2,76 mA, 14,7 mA bei 0,85 V statt 19 mA, 60 mA bei 0,90 V statt 132 mA. $I_B$ hat zwei Teile: unten eine flachere Gerade mit 119 mV je Dekade, der Rekombinationsstrom der Raumladungszone, oben eine Gerade parallel zu $I_C$ im Abstand des Faktors 100; der Abstand beider Kurven ist die Stromverstärkung. (b) $B$ über $I_C$, logarithmisch von 1 nA bis 100 mA: 3 bei 1 nA, 9 bei 10 nA, 24 bei 100 nA, 50 bei 1 µA, 76 bei 10 µA, 91 bei 100 µA, Maximum 95 bei 0,85 mA, 83 bei 10 mA, 62 bei 30 mA, 33 bei 100 mA; gestrichelt der Modellwert 100. Die Stromverstärkung ist nur in der Mitte konstant: Bei kleinen Strömen frisst der Rekombinationsstrom der Raumladungszone den Basisstrom, bei großen die starke Injektion den Kollektorstrom.
:::

Der __Gummel-Plot__ trägt Kollektor- und Basisstrom logarithmisch über $U_{BE}$ auf (Abbildung 10a). Im idealen Modell sind das zwei parallele Geraden mit 59,5 mV je Dekade im festen Abstand $B_N$. Beim wirklichen Transistor weichen beide Kurven an den Enden ab, und die Stromverstärkung in Abbildung 10b ist nur zwischen etwa 0,1 mA und 3 mA nahe ihrem Höchstwert.

**Die Akteure:**

- __$I_{SE}$__: Sättigungsstrom des __Rekombinationsstroms__ der Basis-Emitter-Raumladungszone; 10⁻¹³ A beim Beispiel, drei Größenordnungen über $I_S$.
- __$n_E$__: Emissionskoeffizient dieses Stroms; 2, weil die Rekombinationsrate in der Mitte der Zone, wo Elektronen- und Löcherdichte gleich groß sind, zu dieser gemeinsamen Dichte proportional ist, und die ist die Wurzel aus dem Produkt beider Dichten, das mit $\exp(U_{BE}/U_T)$ wächst.
- __$I_{KF}$__: __Knickstrom__ der starken Injektion; 50 mA beim Beispiel. Oberhalb davon wächst der Kollektorstrom nur noch mit $\exp(U_{BE}/(2U_T))$.

**Das Zusammenspiel:** Bei kleinen Strömen kommt zum Basisstrom ein Anteil hinzu, den das Transportmodell nicht kennt: In der Raumladungszone der Emitterdiode rekombinieren Elektronen und Löcher, und die Basis muss auch diese Löcher nachliefern. Dieser Strom wächst nur mit der halben Spannung im Exponenten, also mit 119 mV je Dekade; bei 1 mA ist er mit 3 % des Basisstroms unerheblich, bei 1 µA ist er so groß wie der ideale Basisstrom, und bei 1 nA macht er 97 % aus. Die Stromverstärkung fällt deshalb von 95 auf 50 bei 1 µA und auf 3 bei 1 nA. Bei großen Strömen geschieht das Gegenteil mit dem Kollektorstrom: Übersteigt die Elektronendichte in der Basis die Dotierung, verlangt die Neutralität zusätzliche Löcher in der Basis, die Basis wird effektiv höher dotiert, und der Transportstrom wächst nur noch mit der Wurzel der Exponentialfunktion. Der Basisstrom folgt weiter der idealen Geraden, also fällt $B$: 83 bei 10 mA, 33 bei 100 mA.

:::formel Stromverstärkung bei kleinen Strömen
$$B = \frac{I_C}{I_B} = \frac{I_C}{\dfrac{I_C}{B_N} + I_{SE}\,\sqrt{\dfrac{I_C}{I_S}}}$$
:::

**So liest man das:** Der Nenner enthält den idealen Basisstrom und den Rekombinationsstrom, der mit der Wurzel des Kollektorstroms wächst. Bei großem $I_C$ gewinnt der erste Summand, und $B$ nähert sich $B_N$; bei kleinem $I_C$ gewinnt die Wurzel, und $B$ fällt proportional zu $\sqrt{I_C}$. Gleich groß sind beide beim Kollektorstrom $B_N^2 I_{SE}^2/I_S$, beim Beispiel bei 1 µA.

Idee der Herleitung: Man ersetzt in der Diodengleichung des Rekombinationsstroms die Spannung durch den Kollektorstrom.

:::herleitung
**Ausgangspunkt:** Diodengleichung des Kollektorstroms und ein zusätzlicher Basisstrom aus der Raumladungszone mit dem Emissionskoeffizienten $n_E$ = 2, wie er bei jeder Diode bei kleinen Strömen auftritt ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie-ausfuehrlich.html)).
**Annahmen:** (i) $U_{BE} \gg U_T$, sodass die −1 entfällt; (ii) schwache Injektion; (iii) Normalbetrieb.
**Schritt 1**: Basisstrom als Summe aus idealem Anteil und Rekombinationsstrom:
$$I_B = \frac{I_S}{B_N}\,\exp\!\Big(\frac{U_{BE}}{U_T}\Big) + I_{SE}\,\exp\!\Big(\frac{U_{BE}}{2\,U_T}\Big)$$
**Schritt 2** (entscheidender Schritt): Die Spannung durch den Kollektorstrom ausdrücken; aus der Diodengleichung des Kollektorstroms folgt
$$\exp\!\Big(\frac{U_{BE}}{2\,U_T}\Big) = \sqrt{\frac{I_C}{I_S}}$$
und damit
$$I_B = \frac{I_C}{B_N} + I_{SE}\,\sqrt{\frac{I_C}{I_S}}$$
**Ergebnis:**
$$B = \frac{I_C}{I_C/B_N + I_{SE}\sqrt{I_C/I_S}}$$
**Woher die Faktoren kommen:** Die Wurzel stammt aus dem Emissionskoeffizienten 2 des Rekombinationsstroms (Schritt 2).
**Proben:** Einheit: dimensionslos. Grenzfall $I_{SE}$ = 0: $B = B_N$. Zahlenwert: $I_C$ = 1 µA: $\sqrt{10^{10}}$ = 10⁵, Rekombinationsstrom 10 nA, idealer Basisstrom 10 nA, $B$ = 50.
**Grenzen:** Bei großen Strömen fällt $B$ aus einem anderen Grund, der starken Injektion; die Beschreibung mit dem Knickstrom $I_{KF}$ geht über diesen Artikel hinaus. Ihre Idee: Der Transportstrom wird durch die Basisladung geteilt, die mit dem Strom selbst wächst; oberhalb von $I_{KF}$ wird daraus $\sqrt{I_{KF}\,I_S\exp(U_{BE}/U_T)}$, während der Basisstrom weiter exponentiell wächst; $B$ fällt dann umgekehrt proportional zu $I_C$, auf $I_{KF} B_N/I_C$. Beim Beispiel mit $I_{KF}$ = 50 mA: 83 bei 10 mA, 33 bei 100 mA.
:::

## Das statische Großsignalmodell

*Was liegt zwischen den Anschlüssen und dem inneren Transistor, und was davon muss man mitnehmen?*

:::grafik
Szene: st1/bipolartransistor/01-grossignalmodell · Vorlage: ersatzschaltbild-paar
**Abbildung 11:** (a) Vollständiges statisches Großsignalmodell: Die äußeren Anschlüsse B′, E′ und C′ führen über die Bahnwiderstände $R_B$ = 100 Ω, $R_E$ = 5 Ω und $R_C$ = 20 Ω zu den inneren Knoten; innen die Emitterdiode mit $I_{B,N}$, parallel dazu die Rekombinationsdiode mit $I_{B,E}$, die Kollektordiode mit $I_{B,I}$ und die Quelle $I_T$; dazu die gesperrte Substratdiode vom Substrat zum Kollektor. Bei 1 mA fallen 1 mV an $R_B$, 5 mV an $R_E$ und 20 mV an $R_C$ ab. (b) Vereinfachtes Großsignalmodell: nur $R_B$ bleibt, Emitter und Kollektor liegen direkt an den inneren Knoten. Zwischen den Anschlüssen und dem inneren Transistor liegen Bahnwiderstände; der Emitterwiderstand wirkt als Stromgegenkopplung und wird deshalb technologisch klein gemacht, sodass im Modell nur der Basiswiderstand bleibt.
:::

Das Transportmodell beschreibt den inneren Transistor. Abbildung 11a ergänzt ihn zum __statischen Großsignalmodell__: die Rekombinationsdiode $I_{B,E}$ parallel zur Emitterdiode für den Basisstrom bei kleinen Strömen, die Substratdiode des integrierten Transistors und die __Bahnwiderstände__, die Widerstände der dotierten Gebiete zwischen den Kontakten und dem aktiven Bereich unter dem Emitter. Beim Beispieltransistor sind es 100 Ω für den schmalen Weg durch die Basis, 5 Ω für den Emitter und 20 Ω für den Weg durch die vergrabene Schicht zum Kollektorkontakt.

Die drei Widerstände wirken verschieden. Der Basiswiderstand führt nur den Basisstrom: 1 mV bei 10 µA, bedeutungslos. Der Kollektorwiderstand führt den Kollektorstrom, aber am Kollektor hängt der Strom kaum von der Spannung ab: 20 mV weniger $U_{CE}$ ändern nichts, solange der Transistor aktiv bleibt; erst in der Sättigung zählen die 20 mV zur Restspannung. Der Emitterwiderstand führt den Emitterstrom, und sein Spannungsabfall liegt in Reihe mit der steuernden Spannung: Von außen angelegten 773,8 mV kommen an der inneren Diode nur 773,8 mV minus 5 mV an, und 5 mV weniger bedeuten den Faktor 0,82, die Exponentialfunktion von −5/25,85. Der Transistor regelt sich selbst herunter, eine __Stromgegenkopplung__: Mehr Strom senkt die innere Steuerspannung. Bei 10 mA sind es 50 mV; weil der kleinere Strom den Abfall wieder verringert, stellt sich bei fester äußerer Spannung der Faktor 0,40 ein. Deshalb minimiert die Technologie Emitter- und Kollektorwiderstand mit der vergrabenen Schicht und großen Kontakten, und im vereinfachten Modell in Abbildung 11b bleibt nur $R_B$ übrig, weil er später für das Rauschen und das Hochfrequenzverhalten zählt.

Idee der Herleitung: Man setzt die innere Basis-Emitter-Spannung als äußere Spannung minus die Abfälle an $R_E$ und $R_B$ in die Diodengleichung ein.

:::herleitung
**Ausgangspunkt:** Diodengleichung des Normalbetriebs und das Ohmsche Gesetz an den Bahnwiderständen.
**Annahmen:** (i) Normalbetrieb, der Basisstrom ist $I_C/B_N$; (ii) der Emitterstrom wird durch $-I_C$ genähert, der Fehler ist $1/B_N$; (iii) kein Early-Effekt.
**Schritt 1**: Maschengleichung vom äußeren Basis- zum äußeren Emitteranschluss:
$$U_{B'E'} = I_B\,R_B + U_{BE} + |I_E|\,R_E \approx U_{BE} + I_C\,\Big(\frac{R_B}{B_N} + R_E\Big)$$
**Schritt 2** (entscheidender Schritt): Einsetzen in die Diodengleichung; die innere Spannung sinkt mit dem Strom:
$$I_C = I_S\,\exp\!\Big(\frac{U_{B'E'} - I_C\,(R_B/B_N + R_E)}{U_T}\Big)$$
**Ergebnis:** Die Gleichung ist implizit; für eine feste äußere Spannung löst man sie numerisch, für einen festen Strom liest man die nötige äußere Spannung direkt ab.
**Woher die Faktoren kommen:** $R_E$ zählt voll, weil der ganze Emitterstrom durch ihn fließt; $R_B$ nur mit $1/B_N$, weil nur der Basisstrom durch ihn fließt.
**Proben:** Grenzfall $R_E = R_B$ = 0: Diodengleichung. Zahlenwert: 1 mA, $R_E$ = 5 Ω, $R_B$ = 100 Ω: innere Spannung 773,8 mV, äußere 779,8 mV; bei fester äußerer Spannung 773,8 mV fließen 0,826 mA.
**Grenzen:** Bei großen Strömen kommt die starke Injektion hinzu; bei schnellen Änderungen die Kapazitäten der Übergänge.
:::

::::beispiel Was der Emitterwiderstand kostet
**Gegeben:** Beispieltransistor mit $I_S$ = 10⁻¹⁶ A, $B_N$ = 100, Bahnwiderstände $R_B$ = 100 Ω, $R_E$ = 5 Ω, $R_C$ = 20 Ω; $U_T$ = 25,85 mV.

**Gesucht:** die äußere Basis-Emitter-Spannung für 1 mA und für 10 mA, und der Strom, der bei fester äußerer Spannung von 773,8 mV mit Widerständen noch fließt.

**Rechnung:** Innere Spannung für 1 mA ist 773,8 mV; dazu die Abfälle:

$$U_{B'E'} = 773{,}8\ \mathrm{mV} + 1\ \mathrm{mA}\cdot5\ \Omega + 10\ \mathrm{\mu A}\cdot100\ \Omega$$

$$U_{B'E'} = 773{,}8 + 5{,}0 + 1{,}0 = 779{,}8\ \mathrm{mV}$$

Für 10 mA ist die innere Spannung 833,3 mV, die Abfälle sind 50 mV und 10 mV: 893,3 mV. Bei fester äußerer Spannung 773,8 mV muss der Strom die implizite Gleichung erfüllen; die numerische Lösung ist 0,826 mA, und als Probe die innere Spannung

$$U_{BE} = 773{,}8 - 0{,}826\cdot5 - 0{,}00826\cdot100 = 768{,}8\ \mathrm{mV}$$

und damit

$$I_C = 1\ \mathrm{mA}\cdot\exp\!\Big(\frac{-5{,}0\ \mathrm{mV}}{25{,}85\ \mathrm{mV}}\Big) = 0{,}824\ \mathrm{mA}$$

im Rahmen der Rundung. Bei fester äußerer Spannung von 833,3 mV, der inneren Spannung für 10 mA ohne Widerstände, wären es nur 3,98 mA, also 40 %.

**Ergebnis:** **779,8 mV statt 773,8 mV für 1 mA; 893 mV statt 833 mV für 10 mA; bei fester Spannung bleiben 83 % bzw. 40 % des Stroms.**

**Einordnung:** 5 Ω klingen nach nichts, aber die Steuerung ist exponentiell mit 25,85 mV als Maßstab; 5 mV sind ein Fünftel davon. Derselbe Mechanismus wird in Verstärkerschaltungen absichtlich mit einem äußeren Emitterwiderstand eingesetzt, um den Arbeitspunkt zu stabilisieren ([Arbeitspunkt und Grundschaltungen des Transistors](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/arbeitspunkt-und-grundschaltungen-ausfuehrlich.html)); im Transistor selbst ist er nur Verlust.
::::

:::fehlvorstellung
„Weil $I_E \approx I_C$ gilt, kann man den Basisstrom in Rechnungen weglassen.“ Das liegt nahe, weil er nur 1 % des Emitterstroms ausmacht und in der Knotengleichung tatsächlich kaum zählt. Weglassen darf man ihn aber nur dort, wo er mit dem Kollektorstrom verglichen wird. Am Eingang ist er die ganze Last: Die treibende Quelle muss 10 µA liefern, über 10 kΩ Quellwiderstand kosten sie 100 mV. In einem Stromspiegel mit zwei Transistoren fehlen am Ausgang 2 % des Referenzstroms, weil zwei Basisströme abgezweigt werden. Und in der Sättigung entscheidet gerade der Basisstrom, wie klein die Restspannung wird (Abschnitt *Sättigung: beide Dioden leiten*).
:::

## Bipolartransistor und MOSFET im Vergleich

*Wo unterscheiden sich die beiden Transistoren, wenn man sie in derselben Schaltung einsetzen will?*

| Größe | Bipolar | MOSFET |
|---|---|---|
| Gesetz | exponentiell in $U_{BE}$ | quadratisch in $U_{GS} - U_{th}$ |
| Faktor 10 im Strom | 60 mV mehr $U_{BE}$ | $U_{GS} - U_{th}$ von 1 V auf 3,16 V |
| Steuerstrom | 10 µA bei 1 mA | null |
| Steilheit je Strom | 38,7 1/V, nämlich $1/U_T$ | 2 1/V bei $U_{GS} - U_{th}$ = 1 V |
| Verstärker | aktiver Bereich | Sättigung |
| Schalter | Sättigung, um 0,1 V | ohmscher Bereich |
| Widerstand am Ausgang | 50 kΩ bei 1 mA | 10 kΩ bei 1 mA |
| Skalierung | Fläche des Emitters | $W/L$ |

Bei gleichem Strom hat der Bipolartransistor beim Beispiel die 19-fache Steilheit des MOSFET, und die Steilheit je Strom ist eine Naturkonstante, $1/U_T$, unabhängig von der Technologie. Zusammen mit der dünnen Basis ergibt das höhere Verstärkung und höhere Grenzfrequenzen bei gleicher Strukturgröße. Der Preis ist der Basisstrom: Er macht Bipolarschaltungen niederohmiger am Eingang als ihre MOS-Gegenstücke und verbietet das verlustfreie Halten einer Ladung auf einem Gate, das die Digitaltechnik braucht.

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Diodengleichung des Kollektorstroms | die Spannung an der Emitterdiode steuert den Transportstrom |
| Basisstrom $I_C/B_N$ | der Nebenstrom: ein fester Bruchteil, der die Verluste ersetzt |
| Zählpfeile und Knotengleichung | drei Ströme, die sich zu null ergänzen, für npn und pnp gleich |
| Transportmodell mit zwei Dioden | beide Übergänge injizieren, beide Richtungen durch dieselbe Basis |
| Sättigung mit 0,1 V Restspannung | zwei leitende Dioden, deren Differenz der äußere Kreis festlegt |
| Early-Effekt | der Vorfaktor der Diodengleichung hängt über die Basisweite von $U_{CE}$ ab |
| Gummel-Plot | der Bruchteil $1/B_N$ ist nur in der Mitte fest |
| Bahnwiderstände | die steuernde Spannung ist die innere, nicht die äußere |

Der Bipolartransistor ist eine spannungsgesteuerte Stromquelle mit einem Nebenstrom: Die Basis-Emitter-Spannung legt über eine Diodengleichung den Transportstrom vom Kollektor zum Emitter fest, die Basis liefert davon nur den festen Bruchteil $1/B_N$ als Basisstrom, und das Transportmodell fasst beide pn-Übergänge und beide Stromrichtungen in zwei Dioden und einer gesteuerten Quelle zusammen, sodass alle fünf Betriebszustände aus demselben Modell folgen.

## Bedeutung und Ausblick

Bipolartransistoren tragen heute vor allem die Hochfrequenztechnik: Eine Bipolar- oder BiCMOS-Technologie, die Bipolar- und CMOS-Transistoren auf einem Chip vereint, mit 180 oder 250 nm Strukturbreite liefert Schaltungen für Funksysteme bei 60 GHz und für Fahrzeugradar bei 77 GHz, wofür reine CMOS-Technologien Strukturen unter 65 nm brauchen und entsprechend teurer sind. Im Messlabor zeigt ein Kennlinienschreiber genau das Ausgangskennlinienfeld aus Abbildung 6b, und aus der Steigung im aktiven Bereich liest man die Early-Spannung ab. Das Transportmodell gilt für schwache Injektion und langsame Änderungen; starke Injektion und Rekombination in der Raumladungszone beschreibt der Gummel-Abschnitt, die Kapazitäten der Übergänge kommen im Kleinsignalmodell hinzu. Der nächste Artikel linearisiert das Transportmodell im Arbeitspunkt: Steilheit $I_C/U_T$, Eingangswiderstand $B_N U_T/I_C$ und Ausgangswiderstand $U_A/I_C$.

:::kern
- Alle drei Ströme werden in den Transistor hinein gezählt: $I_E = -(I_B + I_C)$; beim npn ist $I_E$ negativ, beim pnp sind alle Vorzeichen umgekehrt.
- Die Basis-Emitter-Spannung steuert den Kollektorstrom exponentiell: $I_C = I_S\exp(U_{BE}/U_T)$, 60 mV je Dekade.
- Der Basisstrom ersetzt nur Verluste und ist der feste Bruchteil $I_C/B_N$; der Kollektorstrom fließt nicht über die Basis.
- Fünf Zustände nach Leiten und Sperren beider Dioden; Verstärker im aktiven Zustand, Schalter in der Sättigung, in der beide Dioden leiten.
- Transportmodell: $I_T = B_N I_{B,N} - B_I I_{B,I}$ und $I_B = I_{B,N} + I_{B,I}$; die Quelle ist spannungsgesteuert.
- In der Sättigung teilt sich der Basisstrom auf beide Dioden, der äußere Kreis bestimmt den Strom, und $U_\mathrm{CE,sat}$ ist die Differenz zweier Durchlassspannungen, um 0,1 V.
- Early-Effekt: Faktor $(1 + U_{CE}/U_A)$ durch die spannungsabhängige Basisweite; $U_A$ = 50 V beim Beispiel.
:::

:::quiz
F: Warum legt die Basis-Emitter-Spannung den Kollektorstrom fest und nicht die Kollektor-Emitter-Spannung?
A: Der Kollektorstrom ist der Diffusionsstrom der Elektronen durch die dünne Basis; sein Antrieb ist die Randdichte am Emitterübergang, die mit $\exp(U_{BE}/U_T)$ wächst. Der gesperrte Kollektorübergang sammelt alles ein, was ankommt, gleichgültig, wie hoch seine Sperrspannung ist; $U_{CE}$ wirkt nur über die Basisweite schwach mit.
F: Warum ist der Basisstrom ein fester Bruchteil des Kollektorstroms?
A: Beide Verluste, die die Basis ersetzt, Rekombination in der Basis und Löcherinjektion in den Emitter, wachsen mit demselben Faktor $\exp(U_{BE}/U_T)$ wie der Kollektorstrom; ihr Verhältnis hängt nur von Dotierungen und Abmessungen ab, beim Beispiel 1/100.
F: Warum bleibt der Kollektorstrom in der Sättigung stehen, obwohl der Basisstrom weiter steigt?
A: Der äußere Kreis lässt nur $(U_{CC} - U_{CE})/R_L$ zu. Sobald die Kollektordiode leitet, fließt der zusätzliche Basisstrom über sie ab und senkt den Transportstrom sogar um $B_I I_{B,I}$; bei 50 µA gehen 25,3 µA diesen Weg, und $I_C$ bleibt bei 2,40 mA statt 5 mA.
F: Warum treffen sich alle verlängerten Ausgangskennlinien in einem Punkt?
A: Der Early-Faktor $(1 + U_{CE}/U_A)$ multipliziert jede Kennlinie mit derselben Geraden, die bei $U_{CE} = -U_A$ null wird; dort schneiden sich alle, beim Beispiel bei −50 V.
F: Stimmt es, dass der Kollektorstrom der verstärkte Basisstrom ist?
A: Nein. Der Kollektorstrom fließt vom Emitter durch die Basis in den Kollektor und wird von $U_{BE}$ bestimmt; der Basisstrom ersetzt nur Verluste. Beide haben dieselbe Ursache, deshalb sind sie proportional, aber keiner erzeugt den anderen.
F: Stimmt es, dass Sättigung beim Bipolartransistor dasselbe bedeutet wie beim MOSFET?
A: Nein. Beim MOSFET ist der Sättigungsbereich der flache Verstärkerbereich; beim Bipolartransistor ist Sättigung der steile Bereich links, in dem beide Dioden leiten und der Transistor als Schalter mit 0,1 V Restspannung arbeitet.
F: Stimmt es, dass man den Basisstrom immer vernachlässigen darf, weil $I_E \approx I_C$ gilt?
A: Nein. Nur gegenüber dem Kollektorstrom ist er klein. Am Eingang ist er die ganze Last (10 µA, über 10 kΩ 100 mV), in Stromspiegeln erzeugt er Fehler von $2/B_N$, und in der Sättigung bestimmt er die Restspannung.
F: Warum ist die Stromverstärkung im Inversbetrieb so viel kleiner?
A: Der Kollektor ist schwächer dotiert als der Emitter; als Injektor verliert er einen großen Teil des Basisstroms an die Löcherinjektion aus der Basis in sein Gebiet. Beim Beispiel kostet 1 mA Transportstrom invers 0,5 mA Basisstrom, $B_I$ = 2 statt 100.
F: Wie groß sind Kollektor-, Basis- und Emitterstrom des Beispieltransistors bei $U_{BE}$ = 0,80 V und $U_{CE}$ = 2,5 V?
A: $I_C$ = 10⁻¹⁶ A · exp(800/25,85) · 1,05 = 2,76 mA · 1,05 = 2,89 mA; $I_B$ = 2,76 mA / 100 = 27,6 µA (ohne Early-Faktor); $I_E$ = −(2,89 + 0,028) mA = −2,92 mA.
F: Warum fällt die Stromverstärkung bei kleinen Strömen ab?
A: Zum idealen Basisstrom kommt der Rekombinationsstrom der Basis-Emitter-Raumladungszone, der nur mit $\exp(U_{BE}/(2U_T))$ wächst und deshalb bei kleinen Spannungen relativ größer wird: bei 1 µA ist er so groß wie der ideale Basisstrom, $B$ = 50 statt 100.
:::
