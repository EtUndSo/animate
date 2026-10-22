---
title: Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / Netzwerkanalyse
order: 33020100
summary: Wie man Schaltungen mit Dioden und Transistoren berechnet, obwohl deren Kennlinien gekrümmt sind, von der Beschreibung jedes Bauelements durch Strom, Ladung und Fluss über die Linearisierung im Arbeitspunkt bis zum Groß- und Kleinsignal-Ersatzschaltbild. Ausführliche Fassung: hergeleitet werden die Zerlegung in Gleichanteil, Grundwelle und Oberwelle, differentieller Leitwert, differentielle Kapazität und Induktivität, das Newton-Verfahren mit Begleitmodell und Konvergenz sowie die Kleinsignalrechnung mit exakter Probe.
tags: nichtlineares Bauelement, Arbeitspunkt, Linearisierung, Kleinsignal, Arbeitsgerade
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Für Schaltungen aus Widerständen, Kondensatoren und Spulen gibt es mächtige Rechenverfahren: Knotenanalyse, Überlagerung, Wechselstromrechnung. Alle setzen voraus, dass die doppelte Ursache die doppelte Wirkung hat. Dioden und Transistoren verletzen das; bei einer Siliziumdiode mit idealer Kennlinie steigt der Strom von 0,6 V auf 0,7 V auf das 48-Fache, bei realen Kleinsignaldioden immerhin auf etwa das Acht- bis Neunfache. Das Thema folgt aus einem Prinzip:

**Ein nichtlineares Bauelement lässt sich nicht als Ganzes linear berechnen, aber für kleine Änderungen um einen festen Arbeitspunkt verhält es sich wie ein lineares Bauelement, dessen Wert die Steigung seiner Kennlinie dort ist; deshalb rechnet man eine nichtlineare Schaltung, die kleine Signale verarbeitet, in zwei Schritten, erst den Arbeitspunkt, dann die kleinen Signale um ihn herum, und auch der erste Schritt, das Newton-Verfahren, besteht aus nichts anderem als wiederholtem Linearisieren.**

Der __Arbeitspunkt__ ist dabei der Ruhezustand der Schaltung, die Gleichspannungen und Gleichströme, die sich ohne Signal einstellen; das __Newton-Verfahren__ ist ein Rechenverfahren, das eine Gleichung schrittweise löst.

Vorausgesetzt werden die [Kirchhoffschen Gesetze](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/kirchhoffsche-gesetze.html), die Ableitung als Steigung einer Kurve und die [Kennlinie der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html). Für die Diode allein behandelt [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html) dieselben Fragen; hier geht es um das allgemeine Verfahren für jedes Bauelement. Darauf bauen die Rechenverfahren für lineare Netze und die Kleinsignalmodelle der Transistoren auf.

:::grafik
Szene: st1/netzwerkanalyse/01-tangente · Vorlage: kennlinie-tangente
**Abbildung 1:** Kennlinie des Beispielbauelements, Strom $I$ in mA über der Spannung $U$ in V von 0,4 bis 1,6 V, null bis 0,5 V, darüber eine Parabel. Markiert ist der Arbeitspunkt bei 1,0 V und 0,25 mA mit der Tangente, Steigung 1 mS. Unter der Spannungsachse eine Sinusspannung von ±50 mV um 1,0 V, rechts neben der Stromachse der Strom, den sie hervorruft: Grundwelle ±50 µA um 0,25 mA, Spitzen bei +52,5 µA und −47,5 µA, von einer Sinuskurve kaum zu unterscheiden. Kleine Änderungen um den Arbeitspunkt sehen von der Kennlinie nur die Tangente.
:::

## Strom, Ladung und Fluss: was ein Bauelement beschreibt

*Welche Größen braucht man, um ein beliebiges Bauelement in einer Schaltung zu beschreiben?*

Ein ohmscher Widerstand hat eine einfache Kennlinie: Der Strom ist der Spannung proportional, der Faktor ist der Leitwert. Bei einer Diode gibt es keinen solchen Faktor. Ihr Strom folgt der Shockley-Gleichung ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html)),

$$I = I_S\left[\exp\!\left(\frac{U}{U_T}\right) - 1\right],$$

mit dem __Sättigungssperrstrom__ $I_S$, bei der Beispieldiode 1,46·10⁻¹⁴ A, und der __Temperaturspannung__ $U_T$, 25,85 mV bei 300 K. In Durchlassrichtung verzehnfacht sich der Strom je 59,5 mV, sobald er groß gegen $I_S$ ist, also ab etwa 0,1 V; in Sperrrichtung nähert er sich schon nach wenigen Zehntel Volt dem kleinen Wert $-I_S$. Das ohmsche Gesetz gilt nicht, und die Diode ist eine __nichtlineare, spannungsgesteuerte Stromquelle__: Ihre Spannung legt den Strom fest, aber über eine gekrümmte Kennlinie.

:::fehlvorstellung
„Unterhalb von 0,7 V fließt durch eine Diode kein Strom.“ Das liegt nahe, weil die Kennlinie im Milliamperemaßstab bis etwa 0,6 V auf der Achse zu liegen scheint. Der Strom wächst aber ohne jede Schwelle exponentiell: Die Beispieldiode führt bei 0,4 V 77 nA, bei 0,5 V 3,7 µA, bei 0,6 V 175 µA und bei 0,7 V 8,4 mA. Die 0,7 V sind die Spannung, bei der der Strom für typische Kleinsignaldioden Milliampere erreicht, keine Grenze ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html)).
:::

Allgemein kann der Strom eines Bauelements von mehreren Spannungen abhängen. Beim Transistor steuern zwei, die Spannung am Steueranschluss und die Spannung am Ausgang; bei der Triode im Einführungsthema waren es Gitter- und Anodenspannung ([Von der Röhre zum integrierten Schaltkreis](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/einfuhrung/geschichte-der-schaltungstechnik.html)). Neben dem Strom kann ein Bauelement Ladung speichern und einen magnetischen Fluss führen, und auch diese hängen im Allgemeinen nichtlinear von den Spannungen bzw. Strömen ab.

:::grafik
Szene: st1/netzwerkanalyse/01-zustandsgroessen · Vorlage: kennlinien-dreifach
**Abbildung 2:** Die drei Kennlinien, die ein Bauelement beschreiben. (a) Strom über Spannung: die Beispieldiode (Exponentialfunktion, 0 bis 0,7 V, 0 bis 8,4 mA) und das Beispielbauelement mit quadratischer Kennlinie (0 bis 1,5 V, 0 bis 1 mA). (b) Ladung über Spannung: die Ladung der Sperrschicht auf der p-Seite der Beispieldiode (negativ wegen der festen Akzeptorrümpfe, null bei 0,714 V, wo die Zone in dieser Näherung verschwindet), von −10 V bis +0,4 V, −133 pC bis −23 pC, zur Durchlassrichtung hin steiler werdend. (c) Flussverkettung über Strom: eine Spule mit Eisenkern, 0 bis 2 A, linear ansteigend bis etwa 0,5 A und dann sättigend bei 10 mVs; gestrichelt eine Hystereseschleife. Jedes Bauelement lässt sich durch Strom, Ladung und Fluss als Funktionen seiner Steuergrößen beschreiben.
:::

**Die Akteure:**

- __$U_1, \ldots, U_n$__: die Steuerspannungen eines Bauelements, etwa Gitter- und Anodenspannung; in V.
- __$I$__: der Strom durch das Bauelement; in A. Er hängt über die Kennlinienfunktion __$f_I$__ von den Steuerspannungen ab.
- __$Q$__: die im Bauelement gespeicherte Ladung; in C. Sie hängt über __$f_Q$__ von den Spannungen ab.
- __$\Psi$__: die __Flussverkettung__ einer Spule, die Summe der magnetischen Flüsse durch alle Windungen, bei gleichem Fluss in jeder Windung der Fluss mal der Zahl der Windungen; in V s (Weber). Sie hängt über __$f_\Psi$__ von den Strömen $I_1, \ldots, I_n$ ab.

:::formel Definition
$$I = f_I(U_1, \ldots, U_n), \qquad Q = f_Q(U_1, \ldots, U_n), \qquad \Psi = f_\Psi(I_1, \ldots, I_n)$$
:::

Man beschreibt Bauelemente durch diese drei Größen, weil jede eine andere Art von Wirkung erfasst: den Strom, der sofort fließt, die Ladung, die gespeichert wird, und den Fluss, der Energie im Magnetfeld hält. Fast jedes Bauelement lässt sich mit ihnen modellieren, und für Schaltungen aus Halbleitern genügen meist die ersten beiden. Die vollständige, nichtlineare Beschreibung heißt __Großsignalverhalten__: Sie gilt für beliebig große Spannungen und Ströme, und mit ihr berechnet man, wo sich eine Schaltung einstellt.

Ladung und Fluss wirken nur, wenn sie sich ändern. Ändert sich die gespeicherte Ladung, fließt ein Strom $I_C$ wie in einem Kondensator, denn Strom ist Ladung je Zeit; ändert sich die Flussverkettung, entsteht nach dem __Induktionsgesetz__, einem Erfahrungsgesetz, eine Spannung $U_L$ wie an einer Spule. Mit Strom- und Spannungspfeil in gleicher Richtung und $\Psi$ im Rechtsschraubensinn zum Strompfeil gezählt gilt:

$$I_C = \frac{dQ}{dt}, \qquad U_L = \frac{d\Psi}{dt}$$

Die Beispieldiode speichert in ihrer __Sperrschicht__, der Zone um den pn-Übergang ohne bewegliche Ladungsträger, eine Ladung, deren Betrag mit der Sperrspannung wächst (Abbildung 2b); im Durchlassbereich kommen die eingespeisten Ladungsträger hinzu: Gespeichert ist im Mittel ihre __Lebensdauer__, die mittlere Zeit bis zur Rekombination, mal dem Strom, bei der Beispieldiode mit 1 µs und 1 mA also rund 1 nC. Bei einer Spule mit Eisenkern wächst die Flussverkettung mit dem Strom erst linear und sättigt dann (Abbildung 2c). Mit der __Hysterese__ des Eisens hängt die Flussverkettung sogar von der Vorgeschichte ab und ist dann gar keine Funktion des Stroms mehr; ein Modell wie $f_\Psi$ beschreibt nur die mittlere Kurve.

## Linearisierung im Arbeitspunkt

*Wie wird aus einer gekrümmten Kennlinie eine lineare Beziehung, und wie klein muss ein Signal dafür sein?*

Als Beispiel dient ein Bauelement mit der einfachsten gekrümmten Kennlinie, einer Parabel. So verhält sich näherungsweise eine __MOS-Diode__, ein MOS-Feldeffekttransistor, dessen Steueranschluss (Gate) mit dem Ausgang (Drain) verbunden ist; trotz des Namens gilt für sie nicht die Diodengleichung.

:::formel Definition
$$I(U) = \begin{cases} 0 & \text{für } U < U_\mathrm{th} \\ k\,(U - U_\mathrm{th})^2 & \text{für } U \ge U_\mathrm{th} \end{cases}$$
:::

Man nimmt dieses Bauelement, weil sich an der Parabel jeder Schritt exakt rechnen lässt; seine Werte sind die eines kleinen integrierten Transistors: Die __Schwellspannung__ $U_\mathrm{th}$, unterhalb derer kein Strom fließt, beträgt 0,5 V, der Faktor $k$ 1 mA/V².

:::grafik
Szene: st1/netzwerkanalyse/01-oberwellen · Vorlage: zeitverlauf-spektrum
**Abbildung 3:** Strom durch das Beispielbauelement im Arbeitspunkt 1,0 V, wenn eine Sinusspannung überlagert ist, über zwei Perioden. Links für 50 mV Amplitude: der Strom schwankt fast sinusförmig um 0,25 mA, mit 50 µA Amplitude. Rechts für 400 mV: oben schmale, hohe, unten breite, flache Halbwellen; zerlegt in Gleichanteil 0,33 mA (statt 0,25 mA), Grundwelle 400 µA und Schwingung doppelter Frequenz 80 µA. Darunter die Spektren als Balken bei 0, f und 2f. Die Krümmung der Kennlinie erzeugt eine Schwingung doppelter Frequenz und verschiebt den Gleichanteil, beide wachsen mit dem Quadrat der Amplitude.
:::

**Die Akteure:**

- __$U_A$__: die Gleichspannung am Bauelement, der Index steht für den Arbeitspunkt; im Beispiel 1,0 V.
- __$\hat u$__: die Amplitude der überlagerten Sinusspannung; 50 mV bis 400 mV.
- __$\omega$__: die Kreisfrequenz des Sinus, $2\pi$ mal die Frequenz.
- __$I_A$__: der Strom ohne Sinusspannung; 0,25 mA.

**Das Zusammenspiel:**

**Schritt 1**: An das Bauelement wird eine Gleichspannung mit einer überlagerten Sinusspannung gelegt, wie ein Signal, das auf einer Vorspannung reitet. Die Gleichspannung liegt im leitenden Bereich, und die Spannung bleibt auch im Minimum über der Schwelle.

**Schritt 2**: Eingesetzt in die Parabel entsteht das Quadrat einer Summe aus Konstante und Sinus: Konstante zum Quadrat, das doppelte Produkt beider und der Sinus zum Quadrat.

**Schritt 3**: Das Quadrat des Sinus ist kein Sinus: Es schwankt zwischen 0 und 1, im Mittel ½, und das mit der doppelten Frequenz. Der Strom enthält deshalb drei Teile: einen Gleichanteil, eine __Grundwelle__ mit der Frequenz des Signals und eine Schwingung mit der doppelten Frequenz, die __zweite Harmonische__ (auch 1. Oberwelle genannt). Ihre Amplitude und eine Erhöhung des Gleichanteils wachsen mit dem Quadrat von $\hat u$.

**Schritt 4**: Die Grundwelle ist $\hat u$ proportional, die beiden anderen Anteile wachsen mit $\hat u^2$. Für kleine Amplituden bleiben sie deshalb immer weiter zurück: Bei 50 mV ist die zweite Harmonische 1,25 µA groß, 2,5 % der Grundwelle von 50 µA, und der Gleichanteil steigt um 0,5 %. Übrig bleibt eine lineare Beziehung zwischen Spannungs- und Stromänderung.

**Schritt 5**: Der Proportionalitätsfaktor ist die Steigung der Kennlinie im Arbeitspunkt, hier 1 mS: Für kleine Änderungen verhält sich das Bauelement wie ein Leitwert dieser Größe. Der Punkt $(U_A, I_A)$ der Kennlinie, um den die Änderungen stattfinden, ist der Arbeitspunkt; die Rechnung mit den Änderungen heißt __Kleinsignalrechnung__.

:::formel Formel
$$I(t) = \begin{aligned} &\underbrace{k\left[(U_A - U_\mathrm{th})^2 + \tfrac12\,\hat u^2\right]}_{\text{Gleichanteil}} \\ &+ \underbrace{2k\,(U_A - U_\mathrm{th})\,\hat u\,\sin\omega t}_{\text{Grundwelle}} \\ &- \underbrace{\tfrac12\,k\,\hat u^2\cos 2\omega t}_{\text{2. Harmonische}} \end{aligned}$$
:::

**So liest man das:** Ohne Signal ist der Gleichanteil der Strom $I_A$ im Arbeitspunkt. Mit Signal steigt der Gleichanteil um $\tfrac12 k \hat u^2$, und eine Schwingung doppelter Frequenz derselben Größe kommt hinzu. Die zweite Harmonische verhält sich zur Grundwelle wie $\hat u$ zu $4(U_A - U_\mathrm{th})$: Klein ist ein Signal, wenn es klein gegen den Abstand des Arbeitspunkts von der Schwelle ist.

**Kurz gesagt:** Das Quadrat einer Sinusschwingung besteht aus einem Gleichanteil und einer Schwingung doppelter Frequenz; deshalb macht eine quadratische Kennlinie aus einem Sinus einen Sinus, eine Gleichanteilverschiebung und eine zweite Harmonische, sonst nichts, solange die Spannung im quadratischen Bereich bleibt.

Idee der Herleitung: Man setzt Gleichspannung plus Sinus in die Parabel ein, multipliziert aus und ersetzt das Quadrat des Sinus über das Additionstheorem.

:::herleitung
**Ausgangspunkt:** die quadratische Kennlinie für Spannungen über der Schwelle und das Additionstheorem $\cos 2x = 1 - 2\sin^2 x$.

**Annahmen:** (i) Die Spannung bleibt in jedem Augenblick über der Schwelle, also $\hat u < U_A - U_\mathrm{th}$. (ii) Das Bauelement folgt seiner Kennlinie ohne Verzögerung; gespeicherte Ladungen spielen keine Rolle.

**Schritt 1**: Spannung eingesetzt:

$$I(t) = k\,\big[(U_A - U_\mathrm{th}) + \hat u\sin\omega t\big]^2$$

**Schritt 2**: Binomische Formel:

$$I(t) = k\,(U_A - U_\mathrm{th})^2 + 2k\,(U_A - U_\mathrm{th})\,\hat u\sin\omega t + k\,\hat u^2\sin^2\omega t$$

**Schritt 3** (entscheidender Schritt): Das Additionstheorem nach $\sin^2$ aufgelöst; das Quadrat zerfällt in eine Konstante und eine Schwingung doppelter Frequenz:

$$\sin^2\omega t = \tfrac12 - \tfrac12\cos 2\omega t$$

**Schritt 4**: Eingesetzt und nach Frequenzen geordnet:

$$I(t) = \begin{aligned} &k\left[(U_A - U_\mathrm{th})^2 + \tfrac12\,\hat u^2\right] \\ &+ 2k\,(U_A - U_\mathrm{th})\,\hat u\sin\omega t \\ &- \tfrac12\,k\,\hat u^2\cos 2\omega t \end{aligned}$$

**Ergebnis:** die Formel oben.

**Woher die Faktoren kommen:** Die 2 der Grundwelle stammt aus dem doppelten Produkt der binomischen Formel, die beiden Faktoren ½ aus dem Additionstheorem. Eine dritte oder höhere Harmonische kann nicht entstehen, weil die Parabel nur bis zur zweiten Potenz geht.

**Proben:** Einheit: A/V² mal V² ist A. Grenzfall $\hat u = 0$: nur $k(U_A - U_\mathrm{th})^2$. Zahlenwert für 50 mV: Gleichanteil 251,25 µA, Grundwelle 50 µA, zweite Harmonische 1,25 µA; eine numerische Zerlegung des Stroms in seine Frequenzanteile ergibt dieselben Werte.

**Grenzen:** Wird $\hat u$ größer als $U_A - U_\mathrm{th}$, sperrt das Bauelement in jedem Minimum für eine Weile, der Strom wird unten abgeschnitten, und es entstehen auch höhere Harmonische; bei 700 mV eine dritte mit 7 µA.
:::

::::beispiel Kleines und großes Signal am Beispielbauelement
**Gegeben:** Kennlinie mit $k$ = 1 mA/V² und $U_\mathrm{th}$ = 0,5 V; Arbeitspunkt $U_A$ = 1,0 V; Sinusamplituden (a) 50 mV, (b) 400 mV.

**Gesucht:** Gleichanteil, Grundwelle, zweite Harmonische und ihr Verhältnis zur Grundwelle.

**Rechnung:** Abstand von der Schwelle 0,5 V. (a) 50 mV:

$$2k\,(U_A - U_\mathrm{th})\,\hat u = 2\cdot 1\ \mathrm{mA/V^2}\cdot 0{,}5\ \mathrm{V}\cdot 0{,}05\ \mathrm{V} = 50\ \mu\mathrm{A}$$

$$\tfrac12\,k\,\hat u^2 = \tfrac12\cdot 1\ \mathrm{mA/V^2}\cdot(0{,}05\ \mathrm{V})^2 = 1{,}25\ \mu\mathrm{A}$$

Gleichanteil 250 µA + 1,25 µA = 251,25 µA; Verhältnis:

$$\frac{\hat u}{4\,(U_A - U_\mathrm{th})} = \frac{0{,}05\ \mathrm{V}}{2\ \mathrm{V}} = 2{,}5\ \%$$

(b) 400 mV: Grundwelle 400 µA, zweite Harmonische 80 µA, Verhältnis 20 %, Gleichanteil 250 µA + 80 µA = 330 µA.

**Ergebnis:** **(a) 50 µA Grundwelle, 1,25 µA zweite Harmonische (2,5 %), Gleichanteil +0,5 %; (b) 400 µA, 80 µA (20 %), Gleichanteil +32 %.**

**Einordnung:** Bei 50 mV ist der Strom bis auf 2,5 % ein Abbild der Spannung, bei 400 mV ist er deutlich verzerrt, und der Gleichanteil hat sich um 32 % verschoben, knapp ein Drittel. Die Grenze zwischen beiden Fällen ist der Abstand zur Schwelle, 0,5 V, nicht die Gleichspannung von 1 V.
::::

Für kleine Signale hängt also nur noch die Steigung der Kennlinie im Arbeitspunkt davon ab, wie das Bauelement auf Änderungen reagiert. Sie bekommt einen eigenen Namen:

**Die Akteure:**

- __$u$__, __$i$__: kleine Änderungen von Spannung und Strom gegenüber dem Arbeitspunkt, als Momentanwerte; in V bzw. A. Kleinbuchstaben kennzeichnen in der Schaltungstechnik solche Änderungen.
- __$g$__: der __differentielle Leitwert__, die Steigung der Kennlinie im Arbeitspunkt; in S; beim Beispielbauelement 1 mS. Sein Kehrwert $r = 1/g$ heißt __differentieller Widerstand__, 1 kΩ.

:::formel Definition
$$g = \left.\frac{dI}{dU}\right|_{U_A}$$
:::

Man definiert ihn so, weil die Tangente die Gerade ist, die sich der Kennlinie im Arbeitspunkt am engsten anschmiegt; ihre Steigung ist genau der Faktor der Grundwelle aus Schritt 5. Mit ihm gilt für kleine Änderungen

$$i \approx g\,u,$$

und der Fehler schrumpft mindestens mit dem Quadrat von $u$; die Kleinsignalrechnung rechnet mit dieser Tangente, als wäre sie exakt. Für die Parabel ist der differentielle Leitwert $2k(U_A - U_\mathrm{th})$, und er hängt stark vom Arbeitspunkt ab: 0,2 mS bei 0,6 V, 1 mS bei 1,0 V, 2 mS bei 1,5 V.

**Kurz gesagt:** An einer glatten Kennlinie ist die Stromänderung für kleine Änderungen näherungsweise die Steigung mal die Spannungsänderung; der Fehler schrumpft mindestens mit dem Quadrat der Änderung.

:::fehlvorstellung
„Der Widerstand eines Bauelements im Arbeitspunkt ist Spannung durch Strom.“ Das liegt nahe, weil man Widerstände so berechnet. Spannung durch Strom ist der __statische Widerstand__, der Kehrwert der Steigung der Geraden vom Ursprung zum Arbeitspunkt; er sagt, welcher Strom bei welcher Spannung insgesamt fließt. Für Änderungen zählt die Steigung der Kennlinie selbst, deren Kehrwert der differentielle Widerstand ist. Beim Beispielbauelement sind das 4 kΩ statisch gegen 1 kΩ differentiell, ein Faktor 4; ein Signal sieht nur den differentiellen Wert.
:::

:::fehlvorstellung
„Ein Signal ist klein, wenn es klein gegen die Gleichspannung am Bauelement ist.“ Das liegt nahe, weil die Gleichspannung die einzige sichtbare Spannung ist. Maßgeblich ist aber, auf welcher Spannungsskala sich die Steigung der Kennlinie ändert. Beim Beispielbauelement ist das der Abstand zur Schwelle: Für 1 % zweite Harmonische darf die Amplitude 20 mV betragen, 2 % der Gleichspannung von 1 V. Bei der Diode ist die Skala die Temperaturspannung: Für 1 % darf die Amplitude nur rund 1 mV betragen, knapp anderthalb Promille der Durchlassspannung von 0,7 V.
:::

Dieselbe Rechnung lässt sich für die Diode durchführen. Weil die Exponentialfunktion ihre eigene Ableitung ist, wird ihr differentieller Leitwert besonders übersichtlich:

$$g_\mathrm{Diode} = \frac{I + I_S}{U_T} \approx \frac{I}{U_T}, \qquad g_\mathrm{Parabel} = \frac{2\,I}{U - U_\mathrm{th}}$$

**So liest man das:** Nach der Shockley-Gleichung hängt der differentielle Leitwert der Diode, bis auf den winzigen Beitrag von $I_S$, nur vom Strom und über $U_T$ von der Temperatur ab, nicht von Fläche oder Material. Beim quadratischen Bauelement teilt man den doppelten Strom durch den Abstand zur Schwelle. Bei gleichem Strom von 0,25 mA ist die Diode 9,7-mal steiler: 9,67 mS gegen 1 mS.

**Kurz gesagt:** Bei der Diode ist der differentielle Leitwert die Summe aus Strom und Sättigungssperrstrom geteilt durch die Temperaturspannung, beim quadratischen Bauelement oberhalb der Schwelle der doppelte Strom geteilt durch den Abstand zur Schwelle.

Idee der Herleitung: Man leitet beide Kennlinien ab und drückt das Ergebnis durch den Strom aus.

:::herleitung
**Ausgangspunkt:** die Shockley-Gleichung ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html)) und die quadratische Kennlinie; der differentielle Leitwert als Ableitung.

**Annahmen:** (i) ideale Kennlinien; (ii) beim quadratischen Bauelement liegt der Arbeitspunkt über der Schwelle.

**Schritt 1**: Ableitung der Shockley-Gleichung; die Ableitung der Exponentialfunktion ist sie selbst, geteilt durch $U_T$:

$$g_\mathrm{Diode} = \frac{dI}{dU} = \frac{I_S}{U_T}\exp\!\left(\frac{U}{U_T}\right)$$

**Schritt 2** (entscheidender Schritt): Die Exponentialfunktion durch den Strom ausgedrückt, aus der Shockley-Gleichung:

$$I_S\exp\!\left(\frac{U}{U_T}\right) = I + I_S$$

In Schritt 1 eingesetzt:

$$g_\mathrm{Diode} = \frac{I + I_S}{U_T}$$

**Schritt 3**: Ableitung der Parabel und Ersatz von $k(U - U_\mathrm{th})$ durch $I/(U - U_\mathrm{th})$:

$$g_\mathrm{Parabel} = 2k\,(U - U_\mathrm{th}) = \frac{2\,k\,(U - U_\mathrm{th})^2}{U - U_\mathrm{th}} = \frac{2\,I}{U - U_\mathrm{th}}$$

**Ergebnis:**

$$g_\mathrm{Diode} = \frac{I + I_S}{U_T} \approx \frac{I}{U_T}, \qquad g_\mathrm{Parabel} = \frac{2\,I}{U - U_\mathrm{th}}$$

**Woher die Faktoren kommen:** $U_T$ ist die Spannung, um die sich die Exponentialfunktion um den Faktor $\exp(1)$ ändert; die 2 der Parabel ist der Exponent der Kennlinie.

**Proben:** Einheit: A/V = S. Zahlenwerte bei 0,25 mA: (0,25 mA + 1,46·10⁻¹⁴ A)/25,85 mV = 9,67 mS; 2 · 0,25 mA/0,5 V = 1 mS.

**Grenzen:** Bei großen Strömen begrenzt der Bahnwiderstand der Diode, der Widerstand ihrer neutralen Gebiete und Anschlüsse, die Steigung; beim MOSFET weicht die Kennlinie bei kurzen Kanälen von der Parabel ab.
:::

::::beispiel Differentieller Leitwert von Diode und quadratischem Bauelement bei gleichem Strom
**Gegeben:** Strom 0,25 mA; Beispieldiode mit $I_S$ = 1,46·10⁻¹⁴ A, $U_T$ = 25,85 mV; Beispielbauelement mit $k$ = 1 mA/V², $U_\mathrm{th}$ = 0,5 V.

**Gesucht:** Spannung, differentieller Leitwert und differentieller Widerstand beider Bauelemente.

**Rechnung:** Diode, Spannung und Leitwert:

$$U = U_T\ln\!\left(\frac{I}{I_S} + 1\right) = 25{,}85\ \mathrm{mV}\cdot\ln\!\left(1{,}71\cdot 10^{10}\right) = 0{,}609\ \mathrm{V}$$

$$g_\mathrm{Diode} \approx \frac{0{,}25\ \mathrm{mA}}{25{,}85\ \mathrm{mV}} = 9{,}67\ \mathrm{mS}, \qquad r = 103\ \Omega$$

Quadratisches Bauelement:

$$U = U_\mathrm{th} + \sqrt{\frac{I}{k}} = 0{,}5\ \mathrm{V} + 0{,}5\ \mathrm{V} = 1{,}0\ \mathrm{V}, \qquad g_\mathrm{Parabel} = \frac{2\cdot 0{,}25\ \mathrm{mA}}{0{,}5\ \mathrm{V}} = 1\ \mathrm{mS}$$

**Ergebnis:** **Diode 0,609 V, 9,67 mS (103 Ω); quadratisches Bauelement 1,0 V, 1 mS (1 kΩ).**

**Einordnung:** Je Milliampere Strom liefert die Diode 38,7 mS Leitwert, das quadratische Bauelement in diesem Arbeitspunkt 4 mS. Derselbe Unterschied trennt Bipolartransistor und MOSFET: Bei gleichem Strom ist die Steuerwirkung des Bipolartransistors deutlich größer als die eines MOSFET im quadratischen Bereich seiner Kennlinie.
::::

### Mehrere Steuergrößen, Ladung und Fluss

*Wie linearisiert man, wenn ein Strom von mehreren Spannungen abhängt, und was wird dabei aus Ladung und Fluss?*

Die Triode aus dem Einführungsthema zeigt, was bei zwei Steuerspannungen geschieht. Ändert sich nur die Gitterspannung, ändert sich der Strom um 1,6 mA je Volt; ändert sich nur die Anodenspannung, um 16 µS mal die Änderung. Ändern sich beide ein wenig, addieren sich die beiden Beiträge näherungsweise, wie der Weg in zwei Teilschritten in Abbildung 4 zeigt. Jede der beiden Steigungen ist eine __partielle Ableitung__: die Steigung der Kennlinie nach einer Spannung, während die anderen festgehalten werden.

:::grafik
Szene: st1/netzwerkanalyse/01-zwei-steuergroessen · Vorlage: kennlinienfeld-schritte
**Abbildung 4:** Anodenstrom der Triode in mA über der Gitterspannung von −3 V bis −1 V für die Anodenspannungen 250 V und 256,25 V; Arbeitspunkt bei −2 V und 250 V mit 1,2 mA. Ein Weg in zwei Teilschritten führt zum neuen Punkt: erst 0,1 V mehr am Gitter, entlang der 250-V-Kurve, Stromzuwachs 0,164 mA, wo die Tangente mit 1,6 mA/V 0,16 mA vorhersagt; dann 6,25 V mehr an der Anode, senkrecht hinauf zur 256,25-V-Kurve, Stromzuwachs 0,106 mA, wo 16 µS mal 6,25 V 0,10 mA ergeben. Zusammen 0,269 mA gegen 0,26 mA aus den Steigungen; eine Lupe zeigt den Bereich um −1,9 V. Bei kleinen Änderungen mehrerer Steuergrößen ist die Gesamtänderung näherungsweise die Summe der Beiträge, jeder mit seiner eigenen Steigung.
:::

**Die Akteure:**

- __$u_1, \ldots, u_n$__: kleine Änderungen der Steuerspannungen gegenüber dem Arbeitspunkt; __$i_1, \ldots, i_n$__ entsprechend der Steuerströme einer Spule.
- __$g_j$__, __$C_j$__, __$L_j$__: die partiellen Ableitungen von Strom, Ladung und Flussverkettung nach der $j$-ten Steuergröße im Arbeitspunkt: __differentieller Leitwert__, __differentielle Kapazität__ und __differentielle Induktivität__.
- __$I_A$__, __$Q_A$__, __$\Psi_A$__: Strom, Ladung und Flussverkettung im Arbeitspunkt.

:::formel Definition
$$g_j = \frac{\partial I}{\partial U_j}, \qquad C_j = \frac{\partial Q}{\partial U_j}, \qquad L_j = \frac{\partial \Psi}{\partial I_j}$$
:::

Man definiert sie so, weil sie im linearisierten Modell die Rolle linearer Bauelemente übernehmen: Gehört die Steuergröße zum eigenen Anschlusspaar, sind es Leitwert, Kondensator und Spule; gehört sie zu einem anderen, wie die Gitterspannung beim Anodenstrom der Triode, sind es gesteuerte Quellen. In beiden Fällen hängen ihre Werte vom Arbeitspunkt ab.

:::formel Formel
$$I \approx I_A + \sum_{j=1}^{n} g_j\,u_j$$

$$Q \approx Q_A + \sum_{j=1}^{n} C_j\,u_j$$

$$\Psi \approx \Psi_A + \sum_{j=1}^{n} L_j\,i_j$$
:::

**So liest man das:** Jede Steuergröße trägt mit ihrer eigenen Steigung zur Änderung bei, und die Beiträge addieren sich. Der Fehler wächst mit dem Quadrat der Änderungen, wie die zweite Harmonische im vorigen Abschnitt.

**Kurz gesagt:** Bei kleinen Änderungen mehrerer Steuergrößen ist die Gesamtänderung näherungsweise die Summe der Einzeländerungen, jede mit ihrer eigenen Steigung.

Idee der Herleitung: Man ändert die Steuergrößen nacheinander, jede um ein kleines Stück, und ersetzt die Kennlinie auf jedem Teilstück durch ihre Tangente.

:::herleitung
**Ausgangspunkt:** die Kennlinienfunktion $f_I(U_1, \ldots, U_n)$ des Stroms mit stetigen partiellen Ableitungen erster und zweiter Ordnung; für Ladung und Fluss geht es genauso.

**Annahmen:** (i) Die Änderungen $u_j$ sind so klein, dass sich die Steigungen auf dem Weg vom Arbeitspunkt zum neuen Punkt kaum ändern. (ii) Die Funktion ist glatt, ohne Knick.

**Schritt 1**: Man geht vom Arbeitspunkt in $n$ Teilschritten zum neuen Punkt und ändert in jedem nur eine Steuergröße. Der Zwischenpunkt $P_j$ hat die ersten $j$ Steuergrößen schon geändert, die übrigen noch nicht; $P_0$ ist der Arbeitspunkt, $P_n$ der neue Punkt. Die Gesamtänderung ist die Summe der Teiländerungen:

$$I - I_A = \sum_{j=1}^{n}\big[f_I(P_j) - f_I(P_{j-1})\big]$$

**Schritt 2** (entscheidender Schritt): In jedem Teilschritt ändert sich nur eine Größe; die Änderung ist ihre Steigung mal der Schrittweite, bis auf einen Rest, der mit dem Quadrat der Schrittweite schrumpft:

$$f_I(P_j) - f_I(P_{j-1}) = \left.\frac{\partial f_I}{\partial U_j}\right|_{P_{j-1}} u_j + \text{Rest}_j$$

**Schritt 3**: Die Steigungen an den Zwischenpunkten weichen von denen im Arbeitspunkt nur um Glieder erster Ordnung ab, mit $u_j$ multipliziert also um Glieder zweiter Ordnung; sie und die Reste werden weggelassen:

$$I \approx I_A + \sum_{j=1}^{n}\frac{\partial f_I}{\partial U_j}\Big|_{P_0}\,u_j$$

**Ergebnis:** die Formel oben, mit $g_j$, $C_j$ und $L_j$ als Steigungen.

**Woher die Faktoren kommen:** Jeder Summand stammt aus einem Teilschritt; dass sich die Beiträge einfach addieren, liegt daran, dass gemischte Glieder wie $u_1 u_2$ von zweiter Ordnung sind.

**Proben:** Eine Steuergröße: $i \approx g\,u$ wie zuvor. Zahlenwert Triode: 0,1 V am Gitter und 6,25 V an der Anode ergeben 0,16 mA + 0,1 mA = 0,26 mA. Einheiten: S·V = A, F·V = C, H·A = V s.

**Grenzen:** An einem Knick der Kennlinie, etwa bei einer aus Geradenstücken zusammengesetzten Ersatzkennlinie, gibt es keine eindeutige Tangente; dort versagt die Linearisierung. An der Schwelle des Beispielbauelements gibt es zwar eine Tangente, aber mit der Steigung null: Die Linearisierung sagt dort keine Stromänderung voraus, obwohl für eine positive Änderung $u$ der Strom $k\,u^2$ fließt. Bei Hysterese hängt die Steigung zusätzlich von der Vorgeschichte ab.
:::

Für die Ladung hat die differentielle Kapazität eine anschauliche Bedeutung: Hängt die Ladung nur von einer Spannung ab und ändert sich diese mit der Zeit, ist der Ladestrom die Steigung der Ladungskennlinie mal die Änderungsgeschwindigkeit der Spannung, genau wie beim gewöhnlichen [Kondensator](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/kondensator-und-kapazitaet.html):

$$I_C = \frac{dQ}{dt} = \frac{dQ}{dU}\cdot\frac{dU}{dt} = C(U)\,\frac{dU}{dt}$$

**Kurz gesagt:** Hängt die Ladung nur von einer Spannung ab, ist der Ladestrom die Steigung der Ladungskennlinie mal die Änderungsgeschwindigkeit der Spannung.

:::grafik
Szene: st1/netzwerkanalyse/01-kapazitaet-induktivitaet · Vorlage: kennlinie-gestapelt
**Abbildung 5:** Links oben die Ladung der Sperrschicht der Beispieldiode über der Spannung von −10 V bis +0,4 V (−133 pC bis −23 pC) mit Tangenten bei 0 V und −5 V; darunter ihre Steigung, die Sperrschichtkapazität: 6,2 pF bei −10 V, 8,5 pF bei −5 V, 15,6 pF bei −1 V, 24,1 pF bei 0 V, 36,3 pF bei +0,4 V. Rechts oben die Flussverkettung der Spule mit Eisenkern über dem Strom von 0 bis 2 A; darunter ihre Steigung: 10 mH bei 0 A, 7,9 mH bei 0,5 A, 4,2 mH bei 1 A, 0,7 mH bei 2 A. Kapazität und Induktivität sind die Steigungen der Ladungs- und der Flusskennlinie und hängen vom Arbeitspunkt ab.
:::

::::beispiel Kapazität einer Sperrschicht und Induktivität einer sättigenden Spule
**Gegeben:** (a) Sperrschicht der Beispieldiode mit der Kapazität $C_\mathrm{S0}$ = 24,10 pF bei 0 V und der Diffusionsspannung $U_\mathrm{Diff}$ = 0,714 V, der inneren Spannungsstufe des pn-Übergangs; ihre Kapazität bei der Spannung $U$ ist (Formel aus [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html), wo sie $C_j$ heißt)

$$C_\mathrm{S}(U) = \frac{C_\mathrm{S0}}{\sqrt{1 - U/U_\mathrm{Diff}}}$$

(b) Spule mit der Modellkennlinie

$$\Psi(I) = \Psi_\mathrm{max}\tanh\frac{L_0\,I}{\Psi_\mathrm{max}}, \qquad L_0 = 10\ \mathrm{mH}, \qquad \Psi_\mathrm{max} = 10\ \mathrm{mV\,s}$$

**Gesucht:** (a) Kapazität bei −1 V und der Ladestrom bei einer Spannungsänderung von 1 V/µs; (b) differentielle Induktivität bei 0 A und 2 A.

**Rechnung:** (a)

$$C_\mathrm{S}(-1\ \mathrm{V}) = \frac{24{,}10\ \mathrm{pF}}{\sqrt{1 + 1/0{,}714}} = 15{,}55\ \mathrm{pF}$$

$$I_C = 15{,}55\ \mathrm{pF}\cdot 1\ \frac{\mathrm{V}}{\mu\mathrm{s}} = 15{,}55\ \mu\mathrm{A}$$

(b) Die Ableitung von $\tanh x$ ist $1/\cosh^2 x$:

$$L(I) = \frac{L_0}{\cosh^2(L_0 I/\Psi_\mathrm{max})}, \qquad L(0) = 10\ \mathrm{mH}, \qquad L(2\ \mathrm{A}) = \frac{10\ \mathrm{mH}}{14{,}15} = 0{,}71\ \mathrm{mH}$$

**Ergebnis:** **(a) 15,55 pF, 15,55 µA; (b) 10 mH bei 0 A, 0,71 mH bei 2 A.**

**Einordnung:** Die Sperrschicht wird bei höherer Sperrspannung breiter und ihre Kapazität kleiner; darauf beruht die Kapazitätsdiode zum Abstimmen von Schwingkreisen. Die gesättigte Spule hat bei 2 A nur noch ein Vierzehntel ihrer Induktivität: Eine Stromänderung von 1 A/ms induziert dort 0,71 V statt 10 V.
::::

:::frage
„Warum schreibt man Kleinsignalgrößen klein, aber die differentielle Kapazität groß?“
Kleinbuchstaben wie $u$ und $i$ kennzeichnen Größen, die sich um den Arbeitspunkt ändern; ein differentieller Leitwert wird oft ebenfalls klein geschrieben, $g$ oder $r$, weil er nur für Änderungen gilt. Kapazität und Induktivität schreibt man auch als differentielle Werte groß: Ein gewöhnlicher Kondensator und eine gewöhnliche Spule sind von sich aus linear, ihre Werte gelten für Gleich- und Wechselanteile gleichermaßen, und eine eigene Schreibweise für den differentiellen Wert hat sich nicht eingebürgert. Wo es darauf ankommt, schreibt man den Arbeitspunkt dazu, etwa $C(U_A)$.
:::

## Den Arbeitspunkt finden

*Wo stellt sich eine Schaltung mit einem nichtlinearen Bauelement ein, und wie rechnet man das aus, wenn keine Formel die Lösung liefert?*

Der Arbeitspunkt ist der Zustand, in dem das Gesetz des Bauelements und die Kirchhoffschen Gesetze der übrigen Schaltung zugleich gelten. Als Beispiel speist eine __reale Stromquelle__, eine ideale Stromquelle von 0,5 mA mit einem parallelen Innenwiderstand von 4 kΩ, das Beispielbauelement. Gleichwertig wäre eine Spannungsquelle von 2 V mit 4 kΩ in Reihe ([Ersatzquellen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/ersatzquellen-thevenin-norton.html)).

:::grafik
Szene: st1/netzwerkanalyse/01-arbeitspunkt-grafisch · Vorlage: schaltung-und-kennlinie
**Abbildung 6:** (a) Die Schaltung: Stromquelle 0,5 mA, parallel der Innenwiderstand 4 kΩ und das Beispielbauelement, Knotenspannung $U$. (b) Strom über Spannung: die Gerade der Quelle von 0,5 mA bei 0 V bis 0 mA bei 2 V und die Kennlinie des Bauelements, null bis 0,5 V, dann parabelförmig steigend; Schnittpunkt bei 1,0 V und 0,25 mA. Der Arbeitspunkt ist der einzige Punkt, an dem das Angebot der Quelle und die Kennlinie des Bauelements übereinstimmen.
:::

**Die Akteure:**

- __$I_q$__: Strom der idealen Quelle; 0,5 mA.
- __$G_q$__: Innenleitwert der Quelle, Kehrwert des Innenwiderstands $R_q$; 0,25 mS bei 4 kΩ.
- __$U$__: Knotenspannung, zugleich die Spannung am Bauelement; gesucht.
- __$F(U)$__: __Fehlerstrom__, die Summe der Ströme, die den Knoten bei der Spannung $U$ verlassen, minus dem zufließenden Quellstrom; im Arbeitspunkt null.

**Das Zusammenspiel:** Der Quellstrom teilt sich auf den Innenleitwert und das Bauelement auf. Bei der Spannung $U$ fließen durch den Innenleitwert $G_q U$, für das Bauelement bleibt $I_q - G_q U$: Was die Quelle dem Bauelement anbietet, ist eine fallende Gerade von 0,5 mA bei 0 V bis null bei 2 V, der Leerlaufspannung. Das Bauelement nimmt bei jeder Spannung den Strom seiner Kennlinie auf, einer steigenden Kurve. Beide Bedingungen gelten nur im Schnittpunkt, bei 1,0 V und 0,25 mA (Abbildung 6). Weil die Gerade fällt und die Kennlinie nirgends fällt, gibt es höchstens einen Schnittpunkt; weil die Kennlinie bei 0 V unter und bei 2 V über der Geraden liegt, gibt es genau einen. Für die Diode heißt diese Gerade in der Spannungsquellenform __Arbeitsgerade__ ([Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html)).

Rechnerisch ist der Arbeitspunkt die Nullstelle des Fehlerstroms, also die Spannung, bei der die Knotenregel erfüllt ist:

:::formel Definition
$$F(U) = I(U) + G_q\,U - I_q, \qquad F(U_A) = 0$$
:::

Man definiert den Fehlerstrom so, weil er misst, wie weit eine geschätzte Spannung von der Lösung entfernt ist, gemessen in dem Strom, der am Knoten zu viel abfließt. Beim Beispielbauelement führt $F = 0$ auf eine quadratische Gleichung mit den Lösungen 1,0 V und −0,25 V; die zweite liegt unter der Schwelle, wo der Strom des Bauelements null ist, und scheidet aus. Bei der Diode dagegen steht die Spannung zugleich linear und im Exponenten, und eine solche Gleichung lässt sich nicht mit Grundrechenarten und den üblichen Funktionen lösen; für eine einzelne Masche gibt es zwar eine geschlossene Lösung mit der Lambertschen W-Funktion, aber diese Sonderfunktion wertet man selbst numerisch aus. In Schaltungen mit vielen Knoten entstehen gekoppelte nichtlineare Gleichungen. Man löst den Arbeitspunkt deshalb grundsätzlich numerisch.

:::grafik
Szene: st1/netzwerkanalyse/01-newton · Vorlage: funktion-tangenten
**Abbildung 7:** Der Fehlerstrom $F(U)$ in mA über der Spannung von 0 bis 2,2 V: von −0,5 mA bei 0 V gerade ansteigend auf −0,375 mA bei 0,5 V, dann parabelförmig durch null bei 1,0 V bis 2,25 mA bei 2 V. Eingezeichnet die Tangenten des Newton-Verfahrens: bei 0 V (Steigung 0,25 mS, Nullstelle 2 V), bei 2 V (3,25 mS, Nullstelle 1,308 V), bei 1,308 V (1,865 mS, Nullstelle 1,051 V) und bei 1,051 V (Nullstelle 1,0019 V). Jede Tangente ist die bei der jeweiligen Schätzung linearisierte Schaltung, und ihre Nullstellen laufen schnell auf 1,0 V zu.
:::

**Das Zusammenspiel:**

**Schritt 1**: Man beginnt mit einer Schätzung $U^{(0)}$ für die Spannung, etwa 0 V. Die Schätzungen werden fortlaufend nummeriert: $U^{(\nu)}$ ist die Schätzung nach $\nu$ Schritten; die Klammer unterscheidet die Nummer von einer Potenz.

**Schritt 2**: Man ersetzt den Fehlerstrom bei der Schätzung durch seine Tangente. Ihre Steigung ist $g(U^{(\nu)}) + G_q$, der Leitwert des Knotens, wenn das Bauelement durch seinen differentiellen Leitwert bei der Schätzung ersetzt wird. Die Tangente ist also die bei der Schätzung linearisierte Schaltung.

**Schritt 3**: Man sucht die Nullstelle der Tangente. Der Fehlerstrom $F(U^{(\nu)})$ fließt dazu durch den linearisierten Knoten; die Spannungsänderung, die ihn ausgleicht, ist Fehlerstrom durch Leitwert.

**Schritt 4**: Die Nullstelle der Tangente ist die neue Schätzung, und man wiederholt Schritt 2 und 3, bis sich die Spannung nicht mehr ändert.

**Schritt 5**: Im Beispiel liefert der Start bei 0 V die Folge 0, 2, 1,308, 1,051, 1,0019, 1,000003 V. Die Fehler betragen −1, 1, 0,31, 0,051, 0,0019 und 3·10⁻⁶ V: Nahe der Lösung verdoppelt jeder Schritt etwa die Zahl der richtigen Stellen.

:::formel Formel
$$\begin{aligned} U^{(\nu+1)} &= U^{(\nu)} - \frac{F(U^{(\nu)})}{g(U^{(\nu)}) + G_q} \\ &= U^{(\nu)} - \frac{I(U^{(\nu)}) + G_q\,U^{(\nu)} - I_q}{g(U^{(\nu)}) + G_q} \end{aligned}$$
:::

**So liest man das:** Ist der Fehlerstrom positiv, fließt am Knoten zu viel ab, und die Spannung wird gesenkt; ist er negativ, wird sie angehoben. Wie weit, bestimmt der Leitwert der linearisierten Schaltung: Ein steiles Bauelement braucht nur eine kleine Spannungsänderung, um denselben Fehlerstrom auszugleichen.

**Kurz gesagt:** Das Newton-Verfahren nimmt die Nullstelle der Tangente als nächste Schätzung; nahe einer einfachen Nullstelle einer glatten Funktion verdoppelt jeder Schritt etwa die Zahl der richtigen Stellen.

Idee der Herleitung: Man ersetzt den Fehlerstrom durch seine Tangente bei der Schätzung, löst nach der Nullstelle auf und schätzt mit dem nächsten Glied der Reihe, wie schnell der Fehler schrumpft.

:::herleitung
**Ausgangspunkt:** der Fehlerstrom $F(U)$ und seine Tangente bei der Schätzung $U^{(\nu)}$; die Ableitung von $F$ ist $g(U) + G_q$, denn $G_q U$ hat die Steigung $G_q$ und $I(U)$ die Steigung $g(U)$.

**Annahmen:** (i) $F$ ist bei der Lösung glatt, und seine Steigung ist dort nicht null (einfache Nullstelle). (ii) Die Schätzung liegt nahe genug an der Lösung, damit die Krümmung den Schritt nicht in die falsche Richtung lenkt.

**Schritt 1**: Tangente bei $U^{(\nu)}$:

$$F(U) \approx F(U^{(\nu)}) + \big[g(U^{(\nu)}) + G_q\big]\,(U - U^{(\nu)})$$

**Schritt 2**: Nullstelle der Tangente:

$$U^{(\nu+1)} = U^{(\nu)} - \frac{F(U^{(\nu)})}{g(U^{(\nu)}) + G_q}$$

**Schritt 3** (entscheidender Schritt): Wie schnell schrumpft der Fehler $e_\nu$, der Abstand der Schätzung $U^{(\nu)}$ von der Lösung $U_A$? Man entwickelt $F$ um die Lösung bis zur zweiten Ordnung; weil $F$ dort null ist, gilt

$$F(U^{(\nu)}) \approx F'(U_A)\,e_\nu + \tfrac12\,F''(U_A)\,e_\nu^2$$

$$F'(U^{(\nu)}) \approx F'(U_A) + F''(U_A)\,e_\nu$$

Eingesetzt in Schritt 2 und bis zur zweiten Ordnung gerechnet:

$$\begin{aligned} e_{\nu+1} &\approx e_\nu - \frac{F'(U_A)\,e_\nu + \tfrac12\,F''(U_A)\,e_\nu^2}{F'(U_A) + F''(U_A)\,e_\nu} \\ &= \frac{\tfrac12\,F''(U_A)\,e_\nu^2}{F'(U_A) + F''(U_A)\,e_\nu} \approx \frac{F''(U_A)}{2\,F'(U_A)}\,e_\nu^2 \end{aligned}$$

**Ergebnis:**

$$U^{(\nu+1)} = U^{(\nu)} - \frac{F(U^{(\nu)})}{g(U^{(\nu)}) + G_q}$$

$$e_{\nu+1} \approx \frac{F''(U_A)}{2\,F'(U_A)}\,e_\nu^2$$

**Woher die Faktoren kommen:** Der Nenner ist die Steigung der Tangente, der Leitwert der linearisierten Schaltung. Das Quadrat im Fehler entsteht, weil die Tangente den Fehlerstrom bis auf Glieder zweiter Ordnung richtig wiedergibt.

**Proben:** Einheit: A/S = V. Ist die Schätzung schon die Lösung, ist der Fehlerstrom null, und die Spannung bleibt. Beim Beispielbauelement ist die zweite Ableitung von $F$ gleich $2k$ = 2 mS/V und die erste $g + G_q$ = 1,25 mS, der Faktor also 0,8 1/V; die Folge der Beispiel-Tabelle nähert sich ihm: 0,54, 0,74, 0,80 1/V.

**Grenzen:** Weit weg von der Lösung kann ein Schritt weit überschießen oder in einen Bereich führen, in dem die Tangente nichts taugt (Frage-Kasten unten); bei einem Knick der Kennlinie, etwa einer aus Geradenstücken zusammengesetzten Ersatzkennlinie, ist die Tangente nicht eindeutig.
:::

::::beispiel Newton-Verfahren für den Arbeitspunkt des Beispielbauelements
**Gegeben:** $I_q$ = 0,5 mA, $G_q$ = 0,25 mS; Kennlinie mit $k$ = 1 mA/V², $U_\mathrm{th}$ = 0,5 V; Startwert 0 V.

**Gesucht:** die Folge der Schätzungen bis zur Lösung.

**Rechnung:** Schritt von 0 V: Das Bauelement sperrt, Strom und differentieller Leitwert sind null:

$$\Delta U = -\frac{0 + 0 - 0{,}5\ \mathrm{mA}}{0 + 0{,}25\ \mathrm{mS}} = 2\ \mathrm{V}$$

Schritt von 2 V: $I$ = 2,25 mA, $g$ = 3 mS:

$$\Delta U = -\frac{2{,}25\ \mathrm{mA} + 0{,}5\ \mathrm{mA} - 0{,}5\ \mathrm{mA}}{3{,}25\ \mathrm{mS}} = -0{,}692\ \mathrm{V}$$

Weiter ebenso:

| $\nu$ | $U^{(\nu)}$ in V | $F(U^{(\nu)})$ in mA | $g + G_q$ in mS | Fehler in V |
|---|---|---|---|---|
| 0 | 0 | −0,5 | 0,25 | −1 |
| 1 | 2 | 2,25 | 3,25 | 1 |
| 2 | 1,3077 | 0,479 | 1,865 | 0,31 |
| 3 | 1,0508 | 0,066 | 1,352 | 0,051 |
| 4 | 1,0019 | 0,0024 | 1,254 | 0,0019 |
| 5 | 1,000003 | 3,6·10⁻⁶ | 1,250 | 2,9·10⁻⁶ |
| 6 | 1,000000 | 8·10⁻¹² | 1,250 | 7·10⁻¹² |

**Ergebnis:** **Arbeitspunkt 1,000 V, 0,25 mA, nach fünf Schritten auf sechs Stellen genau.**

**Einordnung:** Der erste Schritt von 0 V ist zugleich die Lösung der bei 0 V linearisierten Schaltung, in der das gesperrte Bauelement fehlt: 0,5 mA durch 0,25 mS ergeben 2 V. Ein solcher Startwert ist ein üblicher Weg, die Iteration zu beginnen. Nahe der Lösung ist jeder neue Fehler etwa das 0,8-Fache (in 1/V) des Quadrats des vorigen: Aus 0,0019 V werden 2,9·10⁻⁶ V.
::::

Jeder Newton-Schritt löst eine lineare Schaltung. Ersetzt man im Bauelementgesetz die Kennlinie durch ihre Tangente bei der Schätzung, so wird aus dem Bauelement ein Leitwert $g(U^{(\nu)})$ parallel zu einer konstanten Stromquelle:

$$I \approx g(U^{(\nu)})\,U + I_{\mathrm{eq},\nu}$$

$$I_{\mathrm{eq},\nu} = I(U^{(\nu)}) - g(U^{(\nu)})\,U^{(\nu)}$$

Diese lineare Ersatzschaltung für einen Iterationsschritt heißt __Begleitmodell__. Die Knotenregel mit ihr ergibt genau die neue Schätzung aus der Formel oben, denn sie ist nichts anderes als die Tangente in Schaltungsform. In einer Schaltung mit vielen Knoten wird aus dem Leitwert $g + G_q$ eine Matrix von Leitwerten, und jeder Schritt ist die Lösung eines linearen Gleichungssystems für alle Knotenspannungen; so berechnen Schaltungssimulatoren den Arbeitspunkt. Die Verfahren, mit denen man solche linearen Systeme aufstellt und löst, sind der Inhalt der folgenden Themen.

:::vertiefung
**Warum das Newton-Verfahren schneller ist als die einfache Iteration.** Man kann den Arbeitspunkt auch finden, indem man die Kennlinie nach der Spannung auflöst und abwechselnd einsetzt, wie es [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html) für die Diode tut. Beim Beispielbauelement lautet die Vorschrift: neue Spannung gleich Schwelle plus Wurzel aus (Quellstrom minus $G_q$ mal alte Spannung) durch $k$. Nahe der Lösung multipliziert jeder Schritt den Fehler nur mit einem festen Faktor, hier $-G_q/g$ = −0,25, also mit wechselndem Vorzeichen: nach acht Schritten ab 0 V bleibt ein Fehler von 1,3·10⁻⁵ V. Das Newton-Verfahren erreicht nach sechs Schritten 7·10⁻¹² V, weil es die Steigung benutzt und dadurch den Fehler quadriert statt nur verkleinert. Dafür braucht es in jedem Schritt die Ableitung, die die Kennlinienmodelle eines Simulators mitliefern.
:::

:::frage
„Findet das Newton-Verfahren immer den Arbeitspunkt?“
Nicht ohne Hilfe. Bei der Diode an 5 V über 1 kΩ führt der Start bei 0 V im ersten Schritt auf 5 V, wo das Modell einen Strom von 10⁷⁰ A ergibt; danach senkt jeder Schritt die Spannung nur um fast genau die Temperaturspannung, 25,85 mV, und die Lösung 0,683 V ist erst nach gut 170 Schritten erreicht. Simulatoren begrenzen deshalb den Spannungsschritt an pn-Übergängen: Oberhalb von etwa 0,72 V wird ein großer Schritt logarithmisch verkürzt, und dieselbe Rechnung braucht rund zehn Schritte. Hat eine Schaltung mehrere Lösungen, etwa eine Kippstufe mit zwei stabilen Zuständen, entscheidet der Startwert, welche gefunden wird.
:::

## Großsignal- und Kleinsignal-Ersatzschaltbild

*Wie rechnet man mit der linearisierten Schaltung, und was geschieht dabei mit den Quellen?*

Die Quelle liefere jetzt zusätzlich zu den 0,5 mA einen kleinen Signalstrom, etwa eine Schwankung von 10 µA Amplitude. Gesucht ist, wie stark die Spannung am Bauelement dadurch schwankt.

:::grafik
Szene: st1/netzwerkanalyse/01-ersatzschaltbilder · Vorlage: schaltbild-vergleich
**Abbildung 8:** (a) Großsignal-Ersatzschaltbild im Arbeitspunkt: Gleichstromquelle 0,5 mA, Innenwiderstand 4 kΩ, das Bauelement mit seiner Kennlinie; Knotenspannung 1,0 V, Ströme 0,25 mA und 0,25 mA. (b) Kleinsignal-Ersatzschaltbild: nur die Signalquelle $i_q$ (Amplitude 10 µA), der Innenleitwert 0,25 mS, das Bauelement ersetzt durch den Leitwert $g$ = 1 mS (gleichbedeutend mit einer Stromquelle $g\,u$, gesteuert von der eigenen Spannung) und für schnelle Signale die Kapazität $C(U_A)$; die Gleichstromquelle fehlt, an ihrer Stelle eine Unterbrechung. Die Kleinsignalspannung hat die Amplitude 8 mV. Im Kleinsignalbild steht nur, was sich ändert.
:::

**Die Akteure:**

- __$i_q$__: der Signalanteil des Quellstroms, hier ein Sinus mit der Amplitude $\hat\imath_q$ von 10 µA.
- __$u$__: die Änderung der Knotenspannung gegenüber dem Arbeitspunkt; gesucht, besonders ihre Amplitude $\hat u$.
- __Großsignal-Ersatzschaltbild__: die Schaltung mit allen Gleichgrößen und den vollständigen Kennlinien; aus ihm folgt der Arbeitspunkt.
- __Kleinsignal-Ersatzschaltbild__: die linearisierte Schaltung für die Änderungen; jedes nichtlineare Bauelement ist durch seine differentiellen Werte im Arbeitspunkt ersetzt.

**Das Zusammenspiel:**

**Schritt 1**: Aus dem Großsignal-Ersatzschaltbild berechnet man den Arbeitspunkt: 1,0 V und 0,25 mA.

**Schritt 2**: Jedes nichtlineare Bauelement wird durch seine differentiellen Werte im Arbeitspunkt ersetzt, hier durch den Leitwert 1 mS, bei schnellen Signalen zusätzlich durch seine differentielle Kapazität.

**Schritt 3**: Alle Größen, die sich nicht ändern, fallen weg: Eine konstante Stromquelle wird zur Unterbrechung, denn ihre Stromänderung ist null; eine konstante Spannungsquelle wird zum Kurzschluss, denn ihre Spannungsänderung ist null. Lineare Bauelemente wie der Innenwiderstand bleiben, wie sie sind.

**Schritt 4**: Die lineare Schaltung für die Änderungen wird gelöst: Der Signalstrom von 10 µA teilt sich auf 1 mS und 0,25 mS auf, und die Spannung schwankt um 10 µA durch 1,25 mS, 8 mV; durch das Bauelement fließen davon 8 µA, durch den Innenleitwert 2 µA.

**Schritt 5**: Die vollständige Lösung ist Arbeitspunkt plus Änderung, linear gerechnet 1,0 V ± 8 mV. Die exakte Rechnung mit der Parabel ergibt +7,95 mV und −8,05 mV, im Mittel 8,0007 mV.

:::formel Formel
$$u \approx \frac{i_q}{g + G_q}$$
:::

**So liest man das:** Der Signalstrom verteilt sich auf alle Leitwerte am Knoten, und der differentielle Leitwert des Bauelements zählt dabei wie ein gewöhnlicher Leitwert. Ein steileres Bauelement, also ein Arbeitspunkt mit mehr Strom, drückt die Signalspannung herunter.

**Kurz gesagt:** Für kleine Signale ist die Lösung näherungsweise die Summe aus Arbeitspunkt und Kleinsignallösung, und die Kleinsignallösung für eine Summe von Signalen ist exakt die Summe der einzelnen Kleinsignallösungen.

Idee der Herleitung: Man schreibt die Knotenregel für Arbeitspunkt plus Änderung, zieht die Knotenregel des Arbeitspunkts ab und ersetzt den Strom des Bauelements durch seine Tangente.

:::herleitung
**Ausgangspunkt:** die Knotenregel mit dem Quellstrom $I_q + i_q$ und der Knotenspannung $U_A + u$.

**Annahmen:** (i) Das Signal ist so klein, dass die Tangente gilt. (ii) Das Signal ist so langsam, dass Kapazitäten keinen Strom aufnehmen; sonst kommt $C\,du/dt$ hinzu.

**Schritt 1**: Knotenregel für Arbeitspunkt plus Änderung:

$$I(U_A + u) + G_q\,(U_A + u) = I_q + i_q$$

**Schritt 2**: Tangente des Bauelements:

$$I(U_A + u) \approx I(U_A) + g\,u$$

**Schritt 3** (entscheidender Schritt): Die Knotenregel des Arbeitspunkts abgezogen,

$$I(U_A) + G_q\,U_A = I_q,$$

fallen alle Gleichgrößen heraus:

$$g\,u + G_q\,u \approx i_q$$

**Ergebnis:**

$$u \approx \frac{i_q}{g + G_q}$$

**Woher die Faktoren kommen:** Dass die Gleichstromquelle verschwindet, zeigt Schritt 3: Sie steht in der Gleichung des Arbeitspunkts und hebt sich heraus. Übrig bleibt eine Knotenregel nur für Änderungen.

**Proben:** Einheit: A/S = V. Zahlenwert: 10 µA/1,25 mS = 8 mV, exakt 8,0007 mV im Mittel. Grenzfall $g = 0$, gesperrtes Bauelement: Das Signal sieht nur den Innenleitwert, 40 mV.

**Grenzen:** Bei großem Signal versagt die Tangente: 0,2 mA Signalstrom ergeben exakt +143,5 mV und −188,4 mV statt ±160 mV. Bei schnellen Signalen nimmt die Kapazität Strom auf.
:::

::::beispiel Kleinsignalrechnung und exakte Probe
**Gegeben:** Arbeitspunkt 1,0 V, 0,25 mA; $g$ = 1 mS, $G_q$ = 0,25 mS; Signalstrom (a) 10 µA, (b) 0,2 mA Amplitude; (c) parallel eine Kapazität von 1 pF (angenommen).

**Gesucht:** die Spannungsschwankung linear und exakt; die Frequenz, ab der die Kapazität mitspielt.

**Rechnung:** (a) linear:

$$\hat u \approx \frac{\hat\imath_q}{g + G_q} = \frac{10\ \mu\mathrm{A}}{1{,}25\ \mathrm{mS}} = 8\ \mathrm{mV}$$

Exakt löst man die quadratische Gleichung des Knotens mit 0,51 mA und 0,49 mA Quellstrom: +7,949 mV und −8,052 mV.

(b) linear ±160 mV, exakt +143,5 mV und −188,4 mV.

(c) Der Strom durch die Kapazität ist $\omega C$ mal die Spannungsamplitude, der durch die Leitwerte $g + G_q$ mal dieselbe Amplitude; beide sind gleich groß, wenn

$$f = \frac{g + G_q}{2\pi\,C} = \frac{1{,}25\ \mathrm{mS}}{2\pi\cdot 1\ \mathrm{pF}} = 199\ \mathrm{MHz}$$

Dort sinkt die Spannungsamplitude auf 8 mV/√2 = 5,66 mV, und durch Leitwerte und Kapazität fließen je 7,07 µA, um 90° gegeneinander verschoben; zusammengesetzt ergeben sie wieder 10 µA.

**Ergebnis:** **(a) 8 mV, exakt im Mittel 8,0007 mV; (b) deutliche Abweichung und Unsymmetrie; (c) unterhalb von einigen MHz vernachlässigbar, bei 199 MHz gleich groß wie der Leitwertstrom.**

**Einordnung:** Bei 10 µA weicht jede Halbwelle um 0,6 % von der linearen Rechnung ab, der Mittelwert beider Ausschläge um weniger als ein Zehntausendstel, und die Schwankung ist mit 8 mV klein gegen den Abstand zur Schwelle, 0,5 V. Bei 0,2 mA sind es ±160 mV, knapp ein Drittel dieses Abstands, und die Parabel biegt die Antwort sichtbar: nach oben weniger, nach unten mehr. Bei 1 MHz nimmt die Kapazität nur 0,05 µA auf.
::::

:::fehlvorstellung
„Im Kleinsignal-Ersatzschaltbild bleiben die Batterien und Gleichstromquellen stehen.“ Das liegt nahe, weil sie in der Schaltung ja vorhanden sind. Das Kleinsignalbild rechnet aber nur mit Änderungen, und eine konstante Quelle ändert sich nicht: Eine Gleichspannungsquelle hält ihre Spannung fest, ihre Spannungsänderung ist null, also wirkt sie wie ein Kurzschluss; eine Gleichstromquelle hält ihren Strom fest, ihre Stromänderung ist null, also wirkt sie wie eine Unterbrechung. Ihre Wirkung steckt im Arbeitspunkt und damit in den Werten von $g$ und $C$, wie Schritt 3 der Herleitung zeigt.
:::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Diode, quadratisches Bauelement, Triode | Strom als gekrümmte Funktion der Steuerspannungen |
| Ladung und Fluss | gespeicherte Größen mit eigenen Kennlinien, wirksam über ihre Änderung |
| Oberwellen | die Krümmung erzeugt bei großen Signalen Gleichanteilverschiebung und doppelte Frequenz |
| differentieller Leitwert, Kapazität, Induktivität | für kleine Änderungen gilt die Tangente, ihre Steigung ist das lineare Ersatzbauelement |
| Arbeitspunkt | Schnittpunkt von Kennlinie und Quellengerade, Nullstelle des Fehlerstroms |
| Newton-Verfahren | wiederholtes Linearisieren: jede Tangente ist eine lineare Ersatzschaltung |
| Kleinsignal-Ersatzschaltbild | lineare Schaltung nur für die Änderungen, konstante Quellen werden null |

Ein nichtlineares Bauelement lässt sich nicht als Ganzes linear berechnen, aber für kleine Änderungen um einen festen Arbeitspunkt verhält es sich wie ein lineares Bauelement, dessen Wert die Steigung seiner Kennlinie dort ist; deshalb rechnet man eine nichtlineare Schaltung, die kleine Signale verarbeitet, in zwei Schritten, erst den Arbeitspunkt, dann die kleinen Signale um ihn herum, und auch der erste Schritt, das Newton-Verfahren, besteht aus nichts anderem als wiederholtem Linearisieren.

## Bedeutung und Ausblick

Schaltungssimulatoren wie SPICE arbeiten genau so. Die Arbeitspunktanalyse löst das nichtlineare Großsignalproblem mit dem Newton-Verfahren und Begleitmodellen; die Wechselstromanalyse linearisiert im gefundenen Arbeitspunkt und berechnet die Kleinsignalantwort bei jeder Frequenz; die Zeitbereichsanalyse wiederholt das Newton-Verfahren in jedem Zeitschritt. Jeder Kleinsignalverstärker wird so berechnet: Man stellt mit Gleichgrößen einen Arbeitspunkt ein, in dem das Bauelement steil genug ist, und rechnet das Signal mit dem Kleinsignalmodell.

Die Linearisierung hat zwei Grenzen. Große Signale erzeugen Oberwellen und verschieben den Gleichanteil; und wo die Steigung null ist, etwa an der Schwelle des Beispielbauelements, oder die Kennlinie einen Knick hat, gibt die Tangente das Verhalten nicht wieder. Die folgenden Themen liefern die Werkzeuge für den linearen Teil: Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse, mit denen man Kleinsignal-Ersatzschaltbilder wie auch jeden Newton-Schritt systematisch löst.

:::kern
- Ein Bauelement wird durch Strom, Ladung und Flussverkettung als Funktionen seiner Steuergrößen beschrieben; Ladung und Fluss wirken über $I_C = dQ/dt$ und $U_L = d\Psi/dt$.
- Nichtlinear heißt: kein fester Faktor zwischen Spannung und Strom; die Diode ist eine nichtlineare, spannungsgesteuerte Stromquelle.
- Eine quadratische Kennlinie macht aus einem Sinus Grundwelle, Gleichanteilverschiebung und zweite Harmonische; Verhältnis zweite Harmonische zu Grundwelle $\hat u/[4(U_A - U_\mathrm{th})]$.
- Für kleine Änderungen gilt die Tangente: $i \approx g\,u$ mit $g = dI/dU$ im Arbeitspunkt; ebenso $C = \partial Q/\partial U$ und $L = \partial\Psi/\partial I$.
- Klein heißt klein gegen die Spannungsskala der Krümmung: gegen $U_A - U_\mathrm{th}$ beim quadratischen Bauelement, gegen $U_T$ bei der Diode.
- Der Arbeitspunkt ist die Nullstelle des Fehlerstroms; grafisch der Schnittpunkt von Kennlinie und Quellengerade.
- Newton-Verfahren: $U^{(\nu+1)} = U^{(\nu)} - F(U^{(\nu)})/F'(U^{(\nu)})$; jeder Schritt löst die linearisierte Schaltung, nahe der Lösung verdoppelt sich die Zahl der richtigen Stellen etwa.
- Kleinsignal-Ersatzschaltbild: Bauelemente durch differentielle Werte ersetzen, konstante Spannungsquellen kurzschließen, konstante Stromquellen auftrennen.
:::

:::quiz
F: Warum gilt für eine Diode das ohmsche Gesetz nicht?
A: Weil ihr Strom exponentiell mit der Spannung wächst, oberhalb von etwa 0,1 V je 59,5 mV auf das Zehnfache. Es gibt keinen festen Faktor $R$; die Diode ist eine nichtlineare, spannungsgesteuerte Stromquelle.
F: Warum entsteht an einer quadratischen Kennlinie aus einem Sinus eine Schwingung doppelter Frequenz?
A: Weil das Quadrat des Sinus in einen Gleichanteil und einen Kosinus doppelter Frequenz zerfällt, $\sin^2 x = \tfrac12 - \tfrac12\cos 2x$. Dieser Anteil und die Verschiebung des Gleichanteils wachsen mit $\hat u^2$, die Grundwelle nur mit $\hat u$.
F: Wie groß sind Grundwelle und zweite Harmonische beim Beispielbauelement ($k$ = 1 mA/V², 0,5 V über der Schwelle) für 50 mV Amplitude?
A: Grundwelle $2k(U_A - U_\mathrm{th})\hat u$ = 50 µA, zweite Harmonische $\tfrac12 k\hat u^2$ = 1,25 µA, also 2,5 % der Grundwelle.
F: Stimmt es, dass ein Signal klein ist, wenn es klein gegen die Gleichspannung am Bauelement ist?
A: Nein. Maßgeblich ist die Spannungsskala, auf der sich die Steigung ändert: bei der Diode $U_T$ = 25,85 mV, so dass für 1 % zweite Harmonische nur 1 mV erlaubt ist, beim quadratischen Bauelement der Abstand zur Schwelle, 0,5 V, mit 20 mV für 1 %.
F: Stimmt es, dass der Widerstand im Arbeitspunkt Spannung durch Strom ist?
A: Nein, das ist der statische Widerstand. Für Signale zählt der differentielle Widerstand, der Kehrwert der Steigung: beim Beispielbauelement 1 kΩ statt 4 kΩ.
F: Warum hat die Diode bei 0,25 mA einen fast zehnmal größeren differentiellen Leitwert als das quadratische Bauelement?
A: Weil ihre Kennlinie exponentiell ist: $g \approx I/U_T$ = 9,67 mS, während die Parabel $g = 2I/(U - U_\mathrm{th})$ = 1 mS liefert. Die Spannungsskala der Diode, 25,85 mV, ist viel kleiner als der Abstand zur Schwelle von 0,5 V.
F: Warum findet man den Arbeitspunkt einer Diodenschaltung nicht einfach durch Umformen?
A: Weil die Spannung zugleich linear und im Exponenten steht; eine solche Gleichung lässt sich mit den üblichen Funktionen nicht auflösen, und in Schaltungen mit vielen Knoten entstehen gekoppelte nichtlineare Gleichungen. Man löst numerisch, etwa mit dem Newton-Verfahren.
F: Warum ist jeder Newton-Schritt die Lösung einer linearen Schaltung?
A: Weil man den Fehlerstrom durch seine Tangente ersetzt; deren Steigung $g(U^{(\nu)}) + G_q$ ist der Leitwert der Schaltung mit dem Bauelement als Leitwert $g(U^{(\nu)})$ parallel zu einer Ersatzstromquelle, dem Begleitmodell. Die Nullstelle der Tangente ist die Lösung dieser linearen Schaltung.
F: Was wird im Kleinsignal-Ersatzschaltbild aus einer Gleichspannungsquelle und einer Gleichstromquelle, und warum?
A: Die Spannungsquelle wird zum Kurzschluss, die Stromquelle zur Unterbrechung, weil ihre Änderungen null sind und das Kleinsignalbild nur Änderungen enthält; ihre Wirkung steckt im Arbeitspunkt.
F: Eine Quelle mit 0,25 mS Innenleitwert speist ein Bauelement mit $g$ = 1 mS im Arbeitspunkt. Wie groß ist die Spannungsschwankung bei 10 µA Signalstrom?
A: $\hat u \approx \hat\imath_q/(g + G_q)$ = 10 µA/1,25 mS = 8 mV; davon fließen 8 µA durch das Bauelement und 2 µA durch den Innenleitwert.
:::
