---
title: Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / Netzwerkanalyse
order: 33020100
summary: Wie man Schaltungen mit Dioden und Transistoren berechnet, obwohl deren Kennlinien gekrümmt sind: Bauelemente als Strom, Ladung und Fluss, Linearisierung im Arbeitspunkt, Bestimmung des Arbeitspunkts grafisch und mit dem Newton-Verfahren, Groß- und Kleinsignal-Ersatzschaltbild. Kompakte Fassung mit hergeleiteter Zerlegung in Gleichanteil, Grundwelle und Oberwelle, Linearisierung bei mehreren Steuergrößen, Newton-Verfahren und Kleinsignalrechnung; die ausführliche enthält zusätzlich die Leitwerte von Diode und quadratischem Bauelement im Vergleich, Kapazität und Induktivität mit Beispielen, das Begleitmodell, den Vergleich mit der einfachen Iteration und die Spannungsbegrenzung im Simulator.
tags: nichtlineares Bauelement, Arbeitspunkt, Linearisierung, Kleinsignal, Arbeitsgerade
stil: 3
fassung: kompakt
---

## Worum es geht

Knotenanalyse, Überlagerung und Wechselstromrechnung setzen voraus, dass die doppelte Ursache die doppelte Wirkung hat. Dioden und Transistoren verletzen das: Bei einer Siliziumdiode mit idealer Kennlinie steigt der Strom von 0,6 V auf 0,7 V auf das 48-Fache, bei realen Kleinsignaldioden immerhin auf etwa das Acht- bis Neunfache. Das Thema folgt aus einem Prinzip:

**Ein nichtlineares Bauelement lässt sich nicht als Ganzes linear berechnen, aber für kleine Änderungen um einen festen Arbeitspunkt verhält es sich wie ein lineares Bauelement, dessen Wert die Steigung seiner Kennlinie dort ist; deshalb rechnet man eine nichtlineare Schaltung, die kleine Signale verarbeitet, in zwei Schritten, erst den Arbeitspunkt, dann die kleinen Signale um ihn herum, und auch der erste Schritt, das Newton-Verfahren, besteht aus nichts anderem als wiederholtem Linearisieren.**

Der __Arbeitspunkt__ ist dabei der Ruhezustand der Schaltung, die Gleichspannungen und Gleichströme, die sich ohne Signal einstellen; das __Newton-Verfahren__ ist ein Rechenverfahren, das eine Gleichung schrittweise löst.

Vorausgesetzt werden die [Kirchhoffschen Gesetze](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/kirchhoffsche-gesetze.html), die Ableitung als Steigung und die [Kennlinie der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html); die Diode allein behandelt [Arbeitspunkt und Ersatzschaltung der Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung.html). Darauf bauen die Verfahren für lineare Netze und die Kleinsignalmodelle der Transistoren auf.

:::grafik
Szene: st1/netzwerkanalyse/01-tangente · Vorlage: kennlinie-tangente
**Abbildung 1:** Kennlinie des Beispielbauelements, Strom $I$ in mA über der Spannung $U$ in V von 0,4 bis 1,6 V, null bis 0,5 V, darüber eine Parabel. Markiert ist der Arbeitspunkt bei 1,0 V und 0,25 mA mit der Tangente, Steigung 1 mS. Unter der Spannungsachse eine Sinusspannung von ±50 mV um 1,0 V, rechts neben der Stromachse der Strom, den sie hervorruft: Grundwelle ±50 µA um 0,25 mA, Spitzen bei +52,5 µA und −47,5 µA, von einer Sinuskurve kaum zu unterscheiden. Kleine Änderungen um den Arbeitspunkt sehen von der Kennlinie nur die Tangente.
:::

## Strom, Ladung und Fluss: was ein Bauelement beschreibt

*Welche Größen braucht man, um ein beliebiges Bauelement in einer Schaltung zu beschreiben?*

Beim ohmschen Widerstand ist der Strom der Spannung proportional. Bei der Diode nicht: Nach der Shockley-Gleichung wächst ihr Strom exponentiell mit der Spannung, gemessen in Vielfachen der __Temperaturspannung__ $U_T$ (25,85 mV bei 300 K), und zwar ohne Schwelle; in Sperrrichtung nähert er sich schon nach wenigen Zehntel Volt dem Wert $-I_S$, mit dem winzigen __Sättigungssperrstrom__ $I_S$, bei der Beispieldiode 1,46·10⁻¹⁴ A. Sobald der Strom groß gegen $I_S$ ist, ab etwa 0,1 V, verzehnfacht er sich je 59,5 mV: Die Beispieldiode führt bei 0,5 V 3,7 µA, bei 0,6 V 175 µA und bei 0,7 V 8,4 mA ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html)). Sie ist eine __nichtlineare, spannungsgesteuerte Stromquelle__: Ihre Spannung legt den Strom fest, aber über eine gekrümmte Kennlinie. Allgemein kann der Strom eines Bauelements von mehreren Spannungen abhängen, beim Transistor von zwei; außerdem kann ein Bauelement Ladung speichern und einen magnetischen Fluss führen.

:::grafik
Szene: st1/netzwerkanalyse/01-zustandsgroessen · Vorlage: kennlinien-dreifach
**Abbildung 2:** Die drei Kennlinien, die ein Bauelement beschreiben. (a) Strom über Spannung: die Beispieldiode (Exponentialfunktion, 0 bis 0,7 V, 0 bis 8,4 mA) und das Beispielbauelement mit quadratischer Kennlinie (0 bis 1,5 V, 0 bis 1 mA). (b) Ladung über Spannung: die Ladung der Sperrschicht auf der p-Seite der Beispieldiode (negativ wegen der festen Akzeptorrümpfe, null bei 0,714 V, wo die Zone in dieser Näherung verschwindet), von −10 V bis +0,4 V, −133 pC bis −23 pC, zur Durchlassrichtung hin steiler werdend. (c) Flussverkettung über Strom: eine Spule mit Eisenkern, 0 bis 2 A, linear ansteigend bis etwa 0,5 A und dann sättigend bei 10 mVs; gestrichelt eine Hystereseschleife, mit der die Flussverkettung auch von der Vorgeschichte abhängt. Jedes Bauelement lässt sich durch Strom, Ladung und Fluss als Funktionen seiner Steuergrößen beschreiben.
:::

**Die Akteure:**

- __$U_1, \ldots, U_n$__: die Steuerspannungen eines Bauelements; in V.
- __$I$__, __$Q$__: Strom durch das Bauelement und gespeicherte Ladung, in A bzw. C; sie hängen über die Kennlinienfunktionen __$f_I$__ und __$f_Q$__ von den Spannungen ab.
- __$\Psi$__: die __Flussverkettung__ einer Spule, die Summe der magnetischen Flüsse durch alle Windungen, bei gleichem Fluss in jeder Windung Fluss mal Windungszahl; in V s. Sie hängt über __$f_\Psi$__ von den Strömen $I_1, \ldots, I_n$ ab.

:::formel Definition
$$I = f_I(U_1, \ldots, U_n), \qquad Q = f_Q(U_1, \ldots, U_n), \qquad \Psi = f_\Psi(I_1, \ldots, I_n)$$
:::

Diese drei Größen erfassen die drei Arten von Wirkung: Strom, der sofort fließt, Ladung, die gespeichert wird, und Fluss, der Energie im Magnetfeld hält. Ihre vollständige, nichtlineare Beschreibung heißt __Großsignalverhalten__. Ladung und Fluss wirken über ihre Änderung: Eine sich ändernde Ladung ist ein Strom $I_C$ wie in einem Kondensator, und eine sich ändernde Flussverkettung erzeugt nach dem __Induktionsgesetz__, einem Erfahrungsgesetz, eine Spannung $U_L$ wie an einer Spule; mit Strom- und Spannungspfeil in gleicher Richtung und $\Psi$ im Rechtsschraubensinn zum Strompfeil gezählt gilt:

$$I_C = \frac{dQ}{dt}, \qquad U_L = \frac{d\Psi}{dt}$$

## Linearisierung im Arbeitspunkt

*Wie wird aus einer gekrümmten Kennlinie eine lineare Beziehung, und wie klein muss ein Signal dafür sein?*

Als Beispiel dient ein Bauelement mit parabelförmiger Kennlinie, wie sie eine __MOS-Diode__ näherungsweise hat, ein MOS-Feldeffekttransistor mit verbundenem Steueranschluss (Gate) und Ausgang (Drain):

:::formel Definition
$$I(U) = \begin{cases} 0 & \text{für } U < U_\mathrm{th} \\ k\,(U - U_\mathrm{th})^2 & \text{für } U \ge U_\mathrm{th} \end{cases}$$
:::

An der Parabel lässt sich jeder Schritt exakt rechnen. Unterhalb der __Schwellspannung__ $U_\mathrm{th}$ = 0,5 V fließt kein Strom; der Faktor $k$ beträgt 1 mA/V², wie bei einem kleinen integrierten Transistor.

:::grafik
Szene: st1/netzwerkanalyse/01-oberwellen · Vorlage: zeitverlauf-spektrum
**Abbildung 3:** Strom durch das Beispielbauelement im Arbeitspunkt 1,0 V, wenn eine Sinusspannung überlagert ist, über zwei Perioden. Links für 50 mV Amplitude: der Strom schwankt fast sinusförmig um 0,25 mA, mit 50 µA Amplitude. Rechts für 400 mV: oben schmale, hohe, unten breite, flache Halbwellen; zerlegt in Gleichanteil 0,33 mA (statt 0,25 mA), Grundwelle 400 µA und Schwingung doppelter Frequenz 80 µA. Darunter die Spektren als Balken bei 0, f und 2f. Die Krümmung der Kennlinie erzeugt eine Schwingung doppelter Frequenz und verschiebt den Gleichanteil, beide wachsen mit dem Quadrat der Amplitude.
:::

**Die Akteure:**

- __$U_A$__: die Gleichspannung am Bauelement, der Index steht für den Arbeitspunkt; 1,0 V.
- __$\hat u$__, __$\omega$__: Amplitude und Kreisfrequenz ($2\pi$ mal Frequenz) der überlagerten Sinusspannung.
- __$I_A$__: der Strom ohne Sinusspannung; 0,25 mA.

**Das Zusammenspiel:**

**Schritt 1**: An das Bauelement wird eine Gleichspannung mit einer überlagerten Sinusspannung gelegt; die Spannung bleibt auch im Minimum über der Schwelle.

**Schritt 2**: Eingesetzt in die Parabel entsteht das Quadrat einer Summe: Konstante zum Quadrat, doppeltes Produkt aus Konstante und Sinus, Sinus zum Quadrat.

**Schritt 3**: Das Quadrat des Sinus schwankt zwischen 0 und 1 mit doppelter Frequenz. Der Strom enthält deshalb einen Gleichanteil, eine __Grundwelle__ mit der Signalfrequenz und eine __zweite Harmonische__ mit doppelter Frequenz; diese und eine Erhöhung des Gleichanteils wachsen mit $\hat u^2$.

**Schritt 4**: Die Grundwelle wächst nur mit $\hat u$; für kleine Amplituden bleiben die anderen Anteile deshalb weit zurück. Bei 50 mV beträgt die zweite Harmonische 1,25 µA, 2,5 % der Grundwelle von 50 µA, und der Gleichanteil steigt um 0,5 %.

**Schritt 5**: Übrig bleibt eine lineare Beziehung, und ihr Faktor ist die Steigung der Kennlinie, hier 1 mS. Der Punkt $(U_A, I_A)$, um den die Änderungen stattfinden, ist der Arbeitspunkt; die Rechnung mit den Änderungen heißt __Kleinsignalrechnung__.

:::formel Formel
$$I(t) = \begin{aligned} &\underbrace{k\left[(U_A - U_\mathrm{th})^2 + \tfrac12\,\hat u^2\right]}_{\text{Gleichanteil}} \\ &+ \underbrace{2k\,(U_A - U_\mathrm{th})\,\hat u\,\sin\omega t}_{\text{Grundwelle}} \\ &- \underbrace{\tfrac12\,k\,\hat u^2\cos 2\omega t}_{\text{2. Harmonische}} \end{aligned}$$
:::

**So liest man das:** Ohne Signal ist der Gleichanteil der Strom $I_A$ im Arbeitspunkt; mit Signal kommen eine Erhöhung $\tfrac12 k\hat u^2$ und eine Schwingung doppelter Frequenz derselben Größe hinzu. Die zweite Harmonische verhält sich zur Grundwelle wie $\hat u$ zu $4(U_A - U_\mathrm{th})$: Ein Signal ist klein, wenn es klein gegen den Abstand des Arbeitspunkts von der Schwelle ist.

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

**Gesucht:** Grundwelle, zweite Harmonische und Gleichanteil.

**Rechnung:** Abstand von der Schwelle 0,5 V. (a) 50 mV:

$$2k\,(U_A - U_\mathrm{th})\,\hat u = 2\cdot 1\ \mathrm{mA/V^2}\cdot 0{,}5\ \mathrm{V}\cdot 0{,}05\ \mathrm{V} = 50\ \mu\mathrm{A}$$

$$\tfrac12\,k\,\hat u^2 = \tfrac12\cdot 1\ \mathrm{mA/V^2}\cdot(0{,}05\ \mathrm{V})^2 = 1{,}25\ \mu\mathrm{A}$$

Gleichanteil 250 µA + 1,25 µA = 251,25 µA. (b) 400 mV: Grundwelle 400 µA, zweite Harmonische 80 µA, Gleichanteil 250 µA + 80 µA = 330 µA.

**Ergebnis:** **(a) zweite Harmonische 2,5 % der Grundwelle, Gleichanteil +0,5 %; (b) 20 % und +32 %.**

**Einordnung:** Die achtfache Amplitude macht die Grundwelle achtmal, die zweite Harmonische 64-mal so groß. Die Grenze zwischen klein und groß ist der Abstand zur Schwelle, 0,5 V, nicht die Gleichspannung von 1 V.
::::

Für kleine Signale kommt es also nur auf die Steigung im Arbeitspunkt an. Mit __$u$__ und __$i$__ für kleine Änderungen von Spannung und Strom gegenüber dem Arbeitspunkt (Kleinbuchstaben kennzeichnen solche Änderungen) braucht man dafür eine einzige Größe:

:::formel Definition
$$g = \left.\frac{dI}{dU}\right|_{U_A}$$
:::

Der __differentielle Leitwert__ $g$ ist die Steigung der Tangente, der Geraden, die sich der Kennlinie im Arbeitspunkt am engsten anschmiegt; sein Kehrwert ist der __differentielle Widerstand__. Mit ihm gilt für kleine Änderungen

$$i \approx g\,u,$$

und der Fehler schrumpft mindestens mit dem Quadrat von $u$; die Kleinsignalrechnung rechnet mit dieser Tangente, als wäre sie exakt. Beim Beispielbauelement ist $g$ die Ableitung der Parabel, $2k(U_A - U_\mathrm{th})$ = 1 mS, und er hängt stark vom Arbeitspunkt ab: 0,2 mS bei 0,6 V, 2 mS bei 1,5 V. Bei der Diode ist die Ableitung der Exponentialfunktion wieder die Exponentialfunktion, geteilt durch $U_T$; deshalb ist ihr differentieller Leitwert der Strom plus $I_S$, geteilt durch $U_T$, praktisch also der Strom geteilt durch die Temperaturspannung: bei gleichem Strom von 0,25 mA 9,67 mS, fast zehnmal so viel.

**Kurz gesagt:** An einer glatten Kennlinie ist die Stromänderung für kleine Änderungen näherungsweise die Steigung mal die Spannungsänderung; der Fehler schrumpft mindestens mit dem Quadrat der Änderung.

:::frage
„Ist der Widerstand im Arbeitspunkt nicht schlicht Spannung durch Strom?“
Das ist der statische Widerstand, der Kehrwert der Steigung der Geraden vom Ursprung zum Arbeitspunkt; er sagt, welcher Strom insgesamt fließt. Ein Signal ändert Spannung und Strom aber entlang der Kennlinie, und dafür zählt deren Steigung, deren Kehrwert der differentielle Widerstand ist. Beim Beispielbauelement sind das 4 kΩ statisch gegen 1 kΩ differentiell, ein Faktor 4.
:::

:::fehlvorstellung
„Ein Signal ist klein, wenn es klein gegen die Gleichspannung am Bauelement ist.“ Das liegt nahe, weil die Gleichspannung die einzige sichtbare Spannung ist. Maßgeblich ist aber die Spannungsskala, auf der sich die Steigung ändert. Beim Beispielbauelement ist das der Abstand zur Schwelle: Für 1 % zweite Harmonische darf die Amplitude 20 mV betragen. Bei der Diode ist es die Temperaturspannung von 25,85 mV: Für 1 % darf die Amplitude nur rund 1 mV betragen, knapp anderthalb Promille der Durchlassspannung von 0,7 V.
:::

Hängt ein Strom von mehreren Spannungen ab, wie bei der Triode aus dem Einführungsthema ([Von der Röhre zum integrierten Schaltkreis](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/einfuhrung/geschichte-der-schaltungstechnik.html)), hat jede Spannung ihre eigene Steigung, die __partielle Ableitung__ bei festgehaltenen übrigen Spannungen: bei der Triode 1,6 mA/V für die Gitter- und 16 µS für die Anodenspannung. Ändern sich beide ein wenig, addieren sich die Beiträge näherungsweise, wie der Weg in zwei Teilschritten in Abbildung 4 zeigt.

:::grafik
Szene: st1/netzwerkanalyse/01-zwei-steuergroessen · Vorlage: kennlinienfeld-schritte
**Abbildung 4:** Anodenstrom der Triode in mA über der Gitterspannung von −3 V bis −1 V für die Anodenspannungen 250 V und 256,25 V; Arbeitspunkt bei −2 V und 250 V mit 1,2 mA. Ein Weg in zwei Teilschritten führt zum neuen Punkt: erst 0,1 V mehr am Gitter, entlang der 250-V-Kurve, Stromzuwachs 0,164 mA, wo die Tangente mit 1,6 mA/V 0,16 mA vorhersagt; dann 6,25 V mehr an der Anode, senkrecht hinauf zur 256,25-V-Kurve, Stromzuwachs 0,106 mA, wo 16 µS mal 6,25 V 0,10 mA ergeben. Zusammen 0,269 mA gegen 0,26 mA aus den Steigungen; eine Lupe zeigt den Bereich um −1,9 V. Bei kleinen Änderungen mehrerer Steuergrößen ist die Gesamtänderung näherungsweise die Summe der Beiträge, jeder mit seiner eigenen Steigung.
:::

Dasselbe gilt für Ladung und Fluss, und die Steigungen heißen dann __differentielle Kapazität__ und __differentielle Induktivität__:

:::formel Definition
$$g_j = \frac{\partial I}{\partial U_j}, \qquad C_j = \frac{\partial Q}{\partial U_j}, \qquad L_j = \frac{\partial \Psi}{\partial I_j}$$
:::

:::formel Formel
$$I \approx I_A + \sum_{j=1}^{n} g_j\,u_j$$

$$Q \approx Q_A + \sum_{j=1}^{n} C_j\,u_j$$

$$\Psi \approx \Psi_A + \sum_{j=1}^{n} L_j\,i_j$$
:::

**So liest man das:** Jede Steuergröße trägt mit ihrer eigenen Steigung bei; $I_A$, $Q_A$ und $\Psi_A$ sind die Werte im Arbeitspunkt, $u_j$ und $i_j$ die kleinen Änderungen. Gehört die Steuergröße zum eigenen Anschlusspaar, verhalten sich $g_j$, $C_j$ und $L_j$ wie gewöhnliche Leitwerte, Kondensatoren und Spulen; gehört sie zu einem anderen, wie gesteuerte Quellen. In beiden Fällen hängen ihre Werte vom Arbeitspunkt ab. Die Sperrschicht der Beispieldiode etwa hat ohne Spannung 24,1 pF und bei 1 V Sperrspannung 15,6 pF.

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

## Den Arbeitspunkt finden

*Wo stellt sich eine Schaltung mit einem nichtlinearen Bauelement ein, und wie rechnet man das aus, wenn keine Formel die Lösung liefert?*

Der Arbeitspunkt ist der Zustand, in dem das Gesetz des Bauelements und die Kirchhoffschen Gesetze zugleich gelten. Im Beispiel speist eine __reale Stromquelle__, eine ideale Stromquelle von 0,5 mA mit parallelem Innenwiderstand von 4 kΩ, das Beispielbauelement.

:::grafik
Szene: st1/netzwerkanalyse/01-arbeitspunkt-grafisch · Vorlage: schaltung-und-kennlinie
**Abbildung 5:** (a) Die Schaltung: Stromquelle 0,5 mA, parallel der Innenwiderstand 4 kΩ und das Beispielbauelement, Knotenspannung $U$. (b) Strom über Spannung: die Gerade der Quelle von 0,5 mA bei 0 V bis 0 mA bei 2 V und die Kennlinie des Bauelements, null bis 0,5 V, dann parabelförmig steigend; Schnittpunkt bei 1,0 V und 0,25 mA. Der Arbeitspunkt ist der einzige Punkt, an dem das Angebot der Quelle und die Kennlinie des Bauelements übereinstimmen.
:::

**Die Akteure:**

- __$I_q$__, __$G_q$__: Strom der idealen Quelle und ihr Innenleitwert; 0,5 mA und 0,25 mS (4 kΩ).
- __$U$__: Knotenspannung, zugleich die Spannung am Bauelement; gesucht.
- __$F(U)$__: __Fehlerstrom__, der Strom, der bei der Spannung $U$ am Knoten zu viel abfließt; im Arbeitspunkt null.

**Das Zusammenspiel:** Durch den Innenleitwert fließen $G_q U$, für das Bauelement bleibt $I_q - G_q U$, eine fallende Gerade von 0,5 mA bei 0 V bis null bei 2 V. Das Bauelement nimmt den Strom seiner steigenden Kennlinie auf. Beides gilt nur im Schnittpunkt, bei 1,0 V und 0,25 mA. Weil die Gerade fällt und die Kennlinie nirgends fällt, gibt es höchstens einen; weil die Kennlinie bei 0 V unter und bei 2 V über der Geraden liegt, genau einen.

:::formel Definition
$$F(U) = I(U) + G_q\,U - I_q, \qquad F(U_A) = 0$$
:::

Der Fehlerstrom misst, wie weit eine Schätzung von der Lösung entfernt ist. Beim Beispielbauelement ließe sich $F = 0$ als quadratische Gleichung lösen, bei der Diode nicht mit den üblichen Funktionen: Dort steht die Spannung zugleich linear und im Exponenten. In Schaltungen mit vielen Knoten entstehen gekoppelte nichtlineare Gleichungen. Man rechnet deshalb numerisch.

:::grafik
Szene: st1/netzwerkanalyse/01-newton · Vorlage: funktion-tangenten
**Abbildung 6:** Der Fehlerstrom $F(U)$ in mA über der Spannung von 0 bis 2,2 V: von −0,5 mA bei 0 V gerade ansteigend auf −0,375 mA bei 0,5 V, dann parabelförmig durch null bei 1,0 V bis 2,25 mA bei 2 V. Eingezeichnet die Tangenten des Newton-Verfahrens: bei 0 V (Steigung 0,25 mS, Nullstelle 2 V), bei 2 V (3,25 mS, Nullstelle 1,308 V), bei 1,308 V (1,865 mS, Nullstelle 1,051 V) und bei 1,051 V (Nullstelle 1,0019 V). Jede Tangente ist die bei der jeweiligen Schätzung linearisierte Schaltung, und ihre Nullstellen laufen schnell auf 1,0 V zu.
:::

**Das Zusammenspiel:**

**Schritt 1**: Man beginnt mit einer Schätzung $U^{(0)}$, etwa 0 V; $U^{(\nu)}$ ist die Schätzung nach $\nu$ Schritten, die Klammer unterscheidet die Nummer von einer Potenz.

**Schritt 2**: Man ersetzt den Fehlerstrom durch seine Tangente bei der Schätzung. Ihre Steigung $g(U^{(\nu)}) + G_q$ ist der Leitwert des Knotens, wenn das Bauelement durch seinen differentiellen Leitwert ersetzt wird: Die Tangente ist die linearisierte Schaltung.

**Schritt 3**: Die Nullstelle der Tangente liegt um die Spannungsänderung neben der Schätzung, die den Fehlerstrom im linearisierten Knoten ausgleicht: Fehlerstrom durch Leitwert, mit umgekehrtem Vorzeichen.

**Schritt 4**: Sie wird zur neuen Schätzung, und man wiederholt, bis sich die Spannung nicht mehr ändert.

**Schritt 5**: Im Beispiel entsteht die Folge 0, 2, 1,308, 1,051, 1,0019, 1,000003 V; die Fehler betragen −1, 1, 0,31, 0,051, 0,0019 und 3·10⁻⁶ V.

:::formel Formel
$$\begin{aligned} U^{(\nu+1)} &= U^{(\nu)} - \frac{F(U^{(\nu)})}{g(U^{(\nu)}) + G_q} \\ &= U^{(\nu)} - \frac{I(U^{(\nu)}) + G_q\,U^{(\nu)} - I_q}{g(U^{(\nu)}) + G_q} \end{aligned}$$
:::

**So liest man das:** Fließt am Knoten zu viel ab, wird die Spannung gesenkt, sonst angehoben; wie weit, bestimmt der Leitwert der linearisierten Schaltung. Jeder Schritt löst also eine lineare Schaltung; in Schaltungen mit vielen Knoten ist das ein lineares Gleichungssystem für alle Knotenspannungen, und so berechnen Simulatoren den Arbeitspunkt.

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

Schritt von 2 V: Strom 2,25 mA, differentieller Leitwert 3 mS:

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

**Ergebnis:** **Arbeitspunkt 1,000 V, 0,25 mA, nach fünf Schritten auf sechs Stellen genau.**

**Einordnung:** Nahe der Lösung ist jeder neue Fehler etwa das 0,8-Fache (in 1/V) des Quadrats des vorigen: Aus 0,0019 V werden 2,9·10⁻⁶ V. Der erste Schritt ist die Lösung der bei 0 V linearisierten Schaltung, in der das gesperrte Bauelement fehlt.
::::

:::frage
„Findet das Newton-Verfahren immer den Arbeitspunkt?“
Nicht ohne Hilfe. Bei einer Diode an 5 V über 1 kΩ führt der Start bei 0 V im ersten Schritt auf 5 V, wo das Modell 10⁷⁰ A ergibt; danach sinkt die Spannung je Schritt nur um fast genau die Temperaturspannung, und die Lösung 0,683 V ist erst nach gut 170 Schritten erreicht. Simulatoren begrenzen deshalb den Spannungsschritt an pn-Übergängen; dann genügen rund zehn Schritte. Hat eine Schaltung mehrere Lösungen, entscheidet der Startwert, welche gefunden wird.
:::

## Großsignal- und Kleinsignal-Ersatzschaltbild

*Wie rechnet man mit der linearisierten Schaltung, und was geschieht dabei mit den Quellen?*

Die Quelle liefere zusätzlich einen kleinen Signalstrom von 10 µA Amplitude. Gesucht ist die Schwankung der Spannung am Bauelement.

:::grafik
Szene: st1/netzwerkanalyse/01-ersatzschaltbilder · Vorlage: schaltbild-vergleich
**Abbildung 7:** (a) Großsignal-Ersatzschaltbild im Arbeitspunkt: Gleichstromquelle 0,5 mA, Innenwiderstand 4 kΩ, das Bauelement mit seiner Kennlinie; Knotenspannung 1,0 V, Ströme 0,25 mA und 0,25 mA. (b) Kleinsignal-Ersatzschaltbild: nur die Signalquelle $i_q$ (Amplitude 10 µA), der Innenleitwert 0,25 mS, das Bauelement ersetzt durch den Leitwert $g$ = 1 mS (gleichbedeutend mit einer Stromquelle $g\,u$, gesteuert von der eigenen Spannung) und für schnelle Signale die Kapazität $C(U_A)$; die Gleichstromquelle fehlt, an ihrer Stelle eine Unterbrechung. Die Kleinsignalspannung hat die Amplitude 8 mV. Im Kleinsignalbild steht nur, was sich ändert.
:::

**Die Akteure:**

- __$i_q$__: der Signalanteil des Quellstroms, hier ein Sinus mit der Amplitude $\hat\imath_q$ von 10 µA.
- __$u$__: die Änderung der Knotenspannung; gesucht, besonders ihre Amplitude $\hat u$.
- __Großsignal-Ersatzschaltbild__: die Schaltung mit Gleichgrößen und vollständigen Kennlinien; aus ihm folgt der Arbeitspunkt. __Kleinsignal-Ersatzschaltbild__: die linearisierte Schaltung für die Änderungen.

**Das Zusammenspiel:**

**Schritt 1**: Aus dem Großsignal-Ersatzschaltbild folgt der Arbeitspunkt, 1,0 V und 0,25 mA.

**Schritt 2**: Das Bauelement wird durch seinen differentiellen Leitwert ersetzt, 1 mS, bei schnellen Signalen zusätzlich durch seine differentielle Kapazität.

**Schritt 3**: Was sich nicht ändert, fällt weg: Eine konstante Stromquelle wird zur Unterbrechung, eine konstante Spannungsquelle zum Kurzschluss, denn ihre Änderungen sind null. Lineare Bauelemente bleiben.

**Schritt 4**: Der Signalstrom teilt sich auf 1 mS und 0,25 mS auf; die Spannung schwankt um 10 µA durch 1,25 mS, 8 mV.

**Schritt 5**: Die Lösung ist Arbeitspunkt plus Änderung, linear gerechnet 1,0 V ± 8 mV; exakt ergeben sich +7,95 mV und −8,05 mV.

:::formel Formel
$$u \approx \frac{i_q}{g + G_q}$$
:::

**So liest man das:** Der Signalstrom verteilt sich auf alle Leitwerte am Knoten, und der differentielle Leitwert des Bauelements zählt wie ein gewöhnlicher Leitwert. Mehr Strom im Arbeitspunkt macht das Bauelement steiler und die Signalspannung kleiner.

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
**Gegeben:** Arbeitspunkt 1,0 V, 0,25 mA; $g$ = 1 mS, $G_q$ = 0,25 mS; Signalstrom (a) 10 µA, (b) 0,2 mA Amplitude.

**Gesucht:** die Spannungsschwankung linear und exakt.

**Rechnung:** (a) linear:

$$\hat u \approx \frac{\hat\imath_q}{g + G_q} = \frac{10\ \mu\mathrm{A}}{1{,}25\ \mathrm{mS}} = 8\ \mathrm{mV}$$

Exakt, aus der quadratischen Knotengleichung mit 0,51 mA und 0,49 mA Quellstrom: +7,949 mV und −8,052 mV. (b) linear ±160 mV, exakt +143,5 mV und −188,4 mV.

**Ergebnis:** **(a) 8 mV, exakt im Mittel 8,0007 mV; (b) deutliche Abweichung und Unsymmetrie.**

**Einordnung:** Bei 10 µA weicht jede Halbwelle um 0,6 % von der linearen Rechnung ab, der Mittelwert beider Ausschläge um weniger als ein Zehntausendstel, denn 8 mV sind klein gegen den Abstand zur Schwelle von 0,5 V. Bei 0,2 mA beträgt die Schwankung knapp ein Drittel dieses Abstands, und die Parabel biegt die Antwort: nach oben weniger, nach unten mehr.
::::

:::fehlvorstellung
„Im Kleinsignal-Ersatzschaltbild bleiben die Batterien und Gleichstromquellen stehen.“ Das liegt nahe, weil sie in der Schaltung vorhanden sind. Das Kleinsignalbild rechnet aber nur mit Änderungen, und eine konstante Quelle ändert sich nicht: Eine Gleichspannungsquelle wirkt deshalb wie ein Kurzschluss, eine Gleichstromquelle wie eine Unterbrechung. Ihre Wirkung steckt im Arbeitspunkt und damit im Wert von $g$.
:::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Diode und quadratisches Bauelement | Strom als gekrümmte Funktion der Steuerspannung |
| Oberwellen | große Signale spüren die Krümmung, kleine nur die Tangente |
| differentieller Leitwert, Kapazität, Induktivität | die Steigung im Arbeitspunkt ist das lineare Ersatzbauelement |
| Newton-Verfahren | wiederholtes Linearisieren: jede Tangente ist eine lineare Ersatzschaltung |
| Kleinsignal-Ersatzschaltbild | lineare Schaltung nur für die Änderungen, konstante Quellen werden null |

Ein nichtlineares Bauelement lässt sich nicht als Ganzes linear berechnen, aber für kleine Änderungen um einen festen Arbeitspunkt verhält es sich wie ein lineares Bauelement, dessen Wert die Steigung seiner Kennlinie dort ist; deshalb rechnet man eine nichtlineare Schaltung, die kleine Signale verarbeitet, in zwei Schritten, erst den Arbeitspunkt, dann die kleinen Signale um ihn herum, und auch der erste Schritt, das Newton-Verfahren, besteht aus nichts anderem als wiederholtem Linearisieren.

## Bedeutung und Ausblick

Schaltungssimulatoren wie SPICE arbeiten genau so: Die Arbeitspunktanalyse löst das Großsignalproblem mit dem Newton-Verfahren, die Wechselstromanalyse linearisiert im Arbeitspunkt. Jeder Kleinsignalverstärker wird so berechnet, mit einem Arbeitspunkt aus Gleichgrößen und dem Signal im Kleinsignalmodell. Die folgenden Themen liefern die Verfahren für den linearen Teil: Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse.

**In der ausführlichen Fassung:** die Fehlvorstellung einer 0,7-V-Schwelle der Diode, der differentielle Leitwert von Diode und quadratischem Bauelement im Vergleich mit Herleitung, Sperrschichtkapazität und sättigende Spule mit Beispielen, die Schreibweise der Kleinsignalgrößen, das Begleitmodell eines Newton-Schritts, der Vergleich mit der einfachen Iteration, die Spannungsbegrenzung im Simulator genauer und die Kapazität im Kleinsignalbild. [Zur ausführlichen Fassung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung-ausfuehrlich.html)

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
F: Warum entsteht an einer quadratischen Kennlinie aus einem Sinus eine Schwingung doppelter Frequenz?
A: Weil das Quadrat des Sinus in einen Gleichanteil und einen Kosinus doppelter Frequenz zerfällt, $\sin^2 x = \tfrac12 - \tfrac12\cos 2x$. Dieser Anteil und die Verschiebung des Gleichanteils wachsen mit $\hat u^2$, die Grundwelle nur mit $\hat u$.
F: Stimmt es, dass ein Signal klein ist, wenn es klein gegen die Gleichspannung am Bauelement ist?
A: Nein. Maßgeblich ist die Spannungsskala der Krümmung: bei der Diode $U_T$ = 25,85 mV, so dass für 1 % zweite Harmonische nur 1 mV erlaubt ist, beim quadratischen Bauelement der Abstand zur Schwelle, 0,5 V, mit 20 mV für 1 %.
F: Wie groß sind differentieller Leitwert und statischer Widerstand des Beispielbauelements bei 1,0 V ($k$ = 1 mA/V², $U_\mathrm{th}$ = 0,5 V)?
A: $g = 2k(U_A - U_\mathrm{th})$ = 1 mS, also 1 kΩ differentiell; statisch 1,0 V/0,25 mA = 4 kΩ.
F: Warum ist jeder Newton-Schritt die Lösung einer linearen Schaltung?
A: Weil man den Fehlerstrom durch seine Tangente ersetzt; ihre Steigung $g(U^{(\nu)}) + G_q$ ist der Leitwert der Schaltung, in der das Bauelement durch seinen differentiellen Leitwert ersetzt ist, und ihre Nullstelle ist die Spannung, die den Fehlerstrom in dieser linearen Schaltung ausgleicht.
F: Stimmt es, dass Gleichspannungsquellen im Kleinsignal-Ersatzschaltbild stehen bleiben?
A: Nein. Ihre Spannungsänderung ist null, sie werden zu Kurzschlüssen; Gleichstromquellen werden zu Unterbrechungen. Ihre Wirkung steckt im Arbeitspunkt.
F: Eine Quelle mit 0,25 mS Innenleitwert speist ein Bauelement mit $g$ = 1 mS im Arbeitspunkt. Wie stark schwankt die Spannung bei 10 µA Signalstrom?
A: $\hat u \approx \hat\imath_q/(g + G_q)$ = 10 µA/1,25 mS = 8 mV; davon fließen 8 µA durch das Bauelement und 2 µA durch den Innenleitwert.
:::
