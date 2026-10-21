---
title: Arbeitspunkt und Ersatzschaltung der Diode
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Halbleiterbauelemente
order: 100400
summary: Wie man Strom und Spannung einer Diode in einer Schaltung findet, obwohl ihre Kennlinie gekrümmt ist: als Schnitt mit der Arbeitsgeraden, mit linearen Ersatzschaltungen samt Probe der Annahmen und für kleine Änderungen mit dem differentiellen Widerstand. Kompakte Fassung; die ausführliche enthält zusätzlich die Herleitung der Iteration und ihrer Konvergenz, die Genauigkeit der Modelle und das Vorgehen von Simulatoren.
tags: Arbeitspunkt, Arbeitsgerade, Lastgerade, Ersatzschaltung, differentieller Widerstand, Diode
stil: 3
fassung: kompakt
---

## Worum es geht

Die Kennlinie einer Diode sagt, welcher Strom zu welcher Spannung gehört, aber nicht, wo die Diode in einer Schaltung tatsächlich arbeitet; das legt erst die übrige Schaltung fest.
**Der Arbeitspunkt ist der Punkt, an dem das Gesetz des Bauteils und die Gesetze des übrigen Netzes zugleich gelten; weil die Diodenkennlinie gekrümmt ist, findet man ihn grafisch, durch Iteration oder mit linearen Ersatzschaltungen, deren Annahmen man am Ergebnis prüfen muss.**

Vorausgesetzt werden [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html), die [Kirchhoffschen Gesetze](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/kirchhoffsche-gesetze.html) und die [Ersatzquellen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/ersatzquellen-thevenin-norton.html).

:::grafik
Szene: get1/halbleiterbauelemente/03-arbeitsgerade · Vorlage: schaltung-und-kennlinie
**Abbildung 1:** (a) Grundschaltung dieses Artikels: Quelle 5 V, Widerstand 1 kΩ und die Beispieldiode; der lineare Rest der Schaltung ist umrahmt. (b) Die Arbeitsgerade des Rests läuft vom Leerlauf (5 V; 0) zum Kurzschluss (0; 5 mA), die Kennlinie der Diode steigt bei 0,6 bis 0,7 V steil an; im Ausschnitt ihr Schnittpunkt bei 0,683 V und 4,32 mA. Der Arbeitspunkt ist dieser Schnittpunkt.
:::

## Die Arbeitsgerade

*Was legt fest, welcher Strom durch die Diode fließt?*

**Die Akteure:**

- __Arbeitspunkt__: das Wertepaar aus Spannung und Strom, mit dem ein Bauteil in einer bestimmten Schaltung arbeitet. Ihn aus der Schaltung zu bestimmen heißt __Arbeitspunktanalyse__, die Schaltung für einen gewünschten Arbeitspunkt zu bemessen __Arbeitspunktsynthese__.
- __$U_0$__, __$R$__: Leerlaufspannung und Innenwiderstand des linearen Rests, also der Schaltung ohne die Diode; in der Grundschaltung 5 V und 1 kΩ.
- __$U$__, __$I$__: Spannung an der Diode und Strom durch sie, beide von der Anode zur Kathode gezählt.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: In jeder Schaltung gelten zugleich die Kennlinien der Bauteile und die Kirchhoffschen Gesetze der Verbindungen. Man teilt die Schaltung deshalb in die Diode und den linearen Rest.

**Schritt 2**: Der Rest wirkt an den Anschlüssen der Diode wie eine [Ersatzspannungsquelle](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/ersatzquellen-thevenin-norton.html) mit $U_0$ und $R$. Welchen Strom er bei welcher Spannung liefert, ist eine Gerade, die __Arbeitsgerade__; sie läuft durch den Leerlauf (kein Strom, volle Spannung $U_0$) und den Kurzschluss (keine Spannung, Strom $U_0/R$). Sie gehört zur übrigen Schaltung, nicht zur Diode: Tauscht man die Diode, bleibt die Gerade gleich.

**Schritt 3**: Die Diode lässt nur Wertepaare auf ihrer Kennlinie zu. Beide Bedingungen gelten zugleich nur im Schnittpunkt, dem Arbeitspunkt; in der Grundschaltung 0,683 V und 4,32 mA (Abbildung 1).

**Schritt 4**: Die Kennlinie steigt überall, die Gerade fällt; deshalb schneiden sie sich genau einmal, und der Arbeitspunkt ist eindeutig.

:::formel Formel
$$I = \frac{U_0 - U}{R}$$
:::

**So liest man das:** Eingabe ist die Spannung an der Diode, Ausgabe der Strom, den der Rest der Schaltung dabei liefert. Je mehr Spannung die Diode übernimmt, desto weniger bleibt für den Widerstand. Die Steigung ist $-1/R$; eine größere Quellenspannung verschiebt die Gerade parallel nach rechts.

Idee der Herleitung: Maschenregel und ohmsches Gesetz für den Rest der Schaltung, nach dem Strom aufgelöst.

:::herleitung
**Ausgangspunkt:** die Maschenregel und das [ohmsche Gesetz](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/ohmscher-widerstand.html), angewandt auf die Masche aus Quelle, Widerstand und Diode.

**Annahmen:** (i) Der Rest der Schaltung ist linear; dann lässt er sich durch seine Ersatzspannungsquelle mit $U_0$ und $R$ ersetzen. (ii) Spannung und Strom der Diode zählen im Verbraucherzählpfeilsystem.

**Schritt 1**: Maschenregel: Die Quellenspannung teilt sich auf Widerstand und Diode auf.

$$U_0 = U_R + U$$

**Schritt 2**: Ohmsches Gesetz am Widerstand, durch den derselbe Strom fließt wie durch die Diode:

$$U_R = R\,I$$

**Schritt 3** (entscheidender Schritt): Eingesetzt und nach dem Strom aufgelöst; die Diode kommt dabei nur über ihre Spannung vor:

$$I = \frac{U_0 - U}{R}$$

**Ergebnis:**

$$I = \frac{U_0 - U}{R}$$

**Woher die Faktoren kommen:** $U_0 - U$ ist die Spannung, die für den Widerstand übrig bleibt, und durch $R$ geteilt ergibt sie den Strom.

**Proben:** Leerlauf: Liegt an der Diode die volle Quellenspannung, ist der Strom null. Kurzschluss: Ist ihre Spannung null, fließt $U_0/R$, in der Grundschaltung 5 mA. Einheit A.

**Grenzen:** Ist der Rest nichtlinear, etwa weil er weitere Dioden enthält, gibt es keine Gerade; dann helfen die Ersatzschaltungen weiter unten.
:::

:::frage
„Warum rechnet man den Arbeitspunkt nicht einfach aus?“
Weil die Gleichung, die man durch Einsetzen der Shockley-Gleichung in die Arbeitsgerade erhält, den Strom zugleich linear und im Logarithmus enthält. Eine solche Mischung lässt sich mit den gewohnten Funktionen nicht nach dem Strom auflösen. Man liest den Schnittpunkt grafisch ab, rechnet iterativ, also abwechselnd mit Gerade und Kennlinie, was schon nach zwei Runden auf 1 µV genau ist, oder man ersetzt die Diode durch eine lineare Ersatzschaltung.
:::

::::beispiel Arbeitspunkt der Grundschaltung
**Gegeben:** Quelle 5 V, Widerstand 1 kΩ, Beispieldiode mit dem Sättigungssperrstrom 1,4572·10⁻¹⁴ A und der Temperaturspannung 25,852 mV (Zahlenwerk, so genau angegeben, weil die Rechnung auf Mikrovolt geht).

**Gesucht:** die Punkte der Arbeitsgeraden und der Arbeitspunkt.

**Rechnung:** Leerlauf und Kurzschluss:

$$I(U = 5\ \mathrm{V}) = 0, \qquad I(U = 0) = \frac{5\ \mathrm{V}}{1\ \mathrm{k}\Omega} = 5\ \mathrm{mA}$$

Schätzung mit 0,7 V an der Diode, Strom aus der Arbeitsgeraden:

$$I_1 = \frac{5\ \mathrm{V} - 0{,}7\ \mathrm{V}}{1\ \mathrm{k}\Omega} = 4{,}300\ \mathrm{mA}$$

Spannung, die die Diode bei diesem Strom tatsächlich hat, mit der nach $U$ aufgelösten Shockley-Gleichung:

$$U_1 = 25{,}852\ \mathrm{mV}\cdot\ln\!\Big(\frac{4{,}300\ \mathrm{mA}}{1{,}4572\cdot10^{-14}\ \mathrm{A}}\Big) = 0{,}68276\ \mathrm{V}$$

Mit dieser Spannung wieder die Arbeitsgerade:

$$I_2 = \frac{5\ \mathrm{V} - 0{,}68276\ \mathrm{V}}{1\ \mathrm{k}\Omega} = 4{,}317\ \mathrm{mA}$$

Die Kennlinie liefert daraus 0,68287 V; eine weitere Runde ändert die Spannung um weniger als 1 µV.

**Ergebnis:** **Arbeitspunkt 0,683 V und 4,317 mA.**

**Einordnung:** Von 5 V bleiben nur 0,68 V an der Diode; den Strom bestimmt fast ganz der Widerstand. Deshalb konvergiert das Verfahren so schnell: Ein Fehler in der geschätzten Spannung ändert den Strom nur wenig, und der Logarithmus der Kennlinie staucht ihn weiter.
::::

## Lineare Ersatzschaltungen

*Wie rechnet man mit Dioden von Hand, ohne Kennlinie und Iteration?*

:::grafik
Szene: get1/halbleiterbauelemente/03-ersatzschaltungen · Vorlage: kennlinie-modelle
**Abbildung 2:** Drei Modelle über der realen Kennlinie (grau), darunter ihre Ersatzschaltbilder. (a) Ideale Diode: leitend ein Kurzschluss, sperrend eine Unterbrechung. (b) Diode mit Durchlassspannung 0,6 V: leitend eine Spannungsquelle. (c) Knickkennlinie: leitend eine Spannungsquelle mit Widerstand. Jedes Modell ersetzt die Diode je Zustand durch lineare Bauteile.
:::

**Die Akteure:**

- __$U_{F0}$__: Durchlassspannung des Modells, ab der die Modelldiode leitet; meist 0,6 oder 0,7 V für Silizium.
- __$r_F$__: Widerstand des Modells im leitenden Zustand; einige Ohm.

**Das Zusammenspiel:** Die gekrümmte Kennlinie wird stückweise durch Geraden ersetzt. Dann ist die Diode in jedem Zustand ein lineares Bauteil, leitend eine Spannungsquelle, sperrend eine Unterbrechung, und man rechnet wie mit jedem linearen Netz (Skript, Bild 10.15 und 10.17). Dafür muss man vorher annehmen, in welchem Zustand die Diode ist, und das Ergebnis prüfen.

:::formel Definition
$$U = U_{F0} + r_F\,I \quad\text{für } I > 0$$

$$I = 0 \quad\text{für } U < U_{F0}$$
:::

**So liest man das:** Das ist die __Knickkennlinie__. Mit $r_F$ = 0 wird daraus die __Diode mit Durchlassspannung__, mit $U_{F0}$ = 0 und $r_F$ = 0 die __ideale Diode__, ein Schalter. Man definiert die Modelle so, weil jedes Stück eine Gerade ist, also einem linearen Bauteil entspricht, und der Unterschied zwischen beiden Richtungen erhalten bleibt.

Als Durchlassspannung nimmt man die Spannung der echten Kennlinie beim erwarteten Strom: 0,645 V bei 1 mA, 0,705 V bei 10 mA für die Beispieldiode. In der Grundschaltung liefert das 0,7 V-Modell 4,30 mA statt 4,317 mA, das 0,6 V-Modell 4,40 mA, die ideale Diode 5 mA, 16 % zu viel. Je kleiner die Quellenspannung, desto stärker zählt die Wahl: Bei 1 V liegt das 0,7 V-Modell schon um ein Fünftel daneben.

## Schaltungen mit mehreren Dioden

*Wie findet man heraus, welche Dioden leiten und welche sperren?*

:::grafik
Szene: get1/halbleiterbauelemente/03-schutzdioden · Vorlage: schaltung-potenziale
**Abbildung 3:** Eingangsschutz eines Logikbausteins: Die Eingangsspannung gelangt über 1 kΩ zum Knoten A; D1 führt von A zur Versorgung 5 V, D2 von Masse nach A; die Last von 10 kΩ liegt zwischen A und Masse. Bei 9 V Eingangsspannung: Unter der Annahme „beide sperren“ läge A auf 8,18 V und an D1 lägen 3,18 V, ein Widerspruch; mit „D1 leitet“ liegt A auf 5,6 V, durch D1 fließen 2,84 mA, an D2 liegen −5,6 V. Die Probe an den Potenzialen zeigt, welche Diode leiten muss.
:::

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Man nimmt für jede Diode einen Zustand an, leitend oder sperrend, möglichst plausibel, und setzt die passende Ersatzschaltung ein.

**Schritt 2**: Man berechnet das lineare Netz.

**Schritt 3** (Probe): Jede leitend angenommene Diode muss einen positiven Strom führen, jede sperrend angenommene eine Spannung unter $U_{F0}$ haben. Sonst war die Annahme falsch, und man rechnet mit einer neuen. Bei $n$ Dioden gibt es $2^n$ Kombinationen.

**Schritt 4**: Viele scheiden ohne Rechnung aus, wenn man die [Potenziale](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/elektrische-feldstarke-und-potenzial/arbeit-potenzial-und-spannung.html) betrachtet: Liegt die Anode einer angeblich sperrenden Diode um mehr als 0,6 V über ihrer Kathode, muss sie leiten.

::::beispiel Schutzdioden am Eingang bei +9 V
**Gegeben:** Schaltung aus Abbildung 3: Vorwiderstand 1 kΩ, Last 10 kΩ, Versorgung 5 V; Modell mit Durchlassspannung 0,6 V; Eingangsspannung 9 V.

**Gesucht:** Zustände der Dioden, Potenzial von A und Strom durch D1.

**Rechnung:** Annahme „beide sperren“: Vorwiderstand und Last bilden einen Spannungsteiler.

$$\varphi_A = 9\ \mathrm{V}\cdot\frac{10\ \mathrm{k}\Omega}{11\ \mathrm{k}\Omega} = 8{,}18\ \mathrm{V}$$

An D1 läge damit die Differenz zu den 5 V der Versorgung, 3,18 V, mehr als 0,6 V: Widerspruch. Neue Annahme „D1 leitet, D2 sperrt“; A liegt 0,6 V über der Versorgung:

$$\varphi_A = 5\ \mathrm{V} + 0{,}6\ \mathrm{V} = 5{,}6\ \mathrm{V}$$

Ströme durch Vorwiderstand und Last und, nach der Knotenregel, durch D1:

$$I_R = \frac{9\ \mathrm{V} - 5{,}6\ \mathrm{V}}{1\ \mathrm{k}\Omega} = 3{,}40\ \mathrm{mA}, \qquad I_L = \frac{5{,}6\ \mathrm{V}}{10\ \mathrm{k}\Omega} = 0{,}56\ \mathrm{mA}$$

$$I_{D1} = 3{,}40\ \mathrm{mA} - 0{,}56\ \mathrm{mA} = 2{,}84\ \mathrm{mA}$$

Probe: Der Strom durch D1 ist positiv; an D2, deren Anode an Masse liegt, liegen −5,6 V. Beides passt.

**Ergebnis:** **D1 leitet mit 2,84 mA, D2 sperrt, A liegt auf 5,6 V.**

**Einordnung:** Die Dioden halten den Eingang zwischen −0,6 V und 5,6 V, wie es Schutzschaltungen von Logikbausteinen tun. Mit den exakten Kennlinien liegt A auf 5,671 V und D1 führt 2,76 mA; das Modell trifft den Strom auf 3 %.
::::

:::fehlvorstellung
„Wenn die Rechnung mit der Annahme ‚Diode leitet‘ ein Ergebnis liefert, stimmt es.“
Das liegt nahe, weil eine lineare Rechnung immer ein Ergebnis liefert. Das gilt aber auch für jede falsche Annahme: Im Beispiel liefert „beide sperren“ glatt 8,18 V am Knoten A. Ob das physikalisch möglich ist, entscheidet erst die Probe, hier die 3,18 V an einer angeblich sperrenden Diode.
:::

## Der differentielle Widerstand

*Wie reagiert eine Diode auf kleine Änderungen um ihren Arbeitspunkt?*

:::grafik
Szene: get1/halbleiterbauelemente/03-kleinsignal · Vorlage: kennlinie-tangente
**Abbildung 4:** (a) Kennlinie der Beispieldiode um den Arbeitspunkt 4,32 mA mit der Tangente, Steigung 1/(6,0 Ω). Ein kleiner Spannungshub von ±0,6 mV erzeugt einen unverzerrten Stromhub von ±0,1 mA; ein großer von ±20 mV wird sichtbar verzerrt. (b) Kleinsignal-Ersatzschaltbild: Die Diode ist durch ihren differentiellen Widerstand ersetzt. Für kleine Änderungen verhält sich die Diode wie ein Widerstand $U_T/I$.
:::

**Die Akteure:**

- __$u$__, __$i$__: kleine Änderungen von Spannung und Strom um den Arbeitspunkt.
- __$r_d$__: __differentieller Widerstand__, die Spannungsänderung je Stromänderung im Arbeitspunkt; 25,9 Ω bei 1 mA.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Schwankt eine Spannung in der Schaltung ein wenig, bewegt sich der Arbeitspunkt ein kleines Stück auf der Kennlinie.

**Schritt 2**: Auf einem kurzen Stück ist die Kennlinie fast gerade; man ersetzt sie dort durch ihre Tangente (Abbildung 4a).

**Schritt 3**: Für die Änderungen ist die Diode damit ein Widerstand, der Kehrwert der Steigung. Im __Kleinsignal-Ersatzschaltbild__ ersetzt man sie durch $r_d$ und rechnet mit den Änderungen linear (Abbildung 4b).

:::formel Formel
$$r_d = \frac{\mathrm{d}U}{\mathrm{d}I} = \frac{U_T}{I + I_S} \approx \frac{U_T}{I}$$
:::

**So liest man das:** Eingabe ist der Strom im Arbeitspunkt, Ausgabe der differentielle Widerstand: 25,9 Ω bei 1 mA, 6,0 Ω in der Grundschaltung, 2,6 Ω bei 10 mA. Er hängt weder vom Material noch von der Fläche ab, nur vom Strom und von der Temperatur. __Kleinsignal__ heißt: Die Spannungsänderungen sind klein gegen $U_T$; bei 1 mV ist die Tangente auf 2 % genau, bei 10 mV nur noch auf 22 %.

Idee der Herleitung: Man leitet die Shockley-Gleichung nach der Spannung ab, nimmt den Kehrwert und schätzt mit der nächsten Ordnung der Reihe, wie groß „klein“ sein darf.

:::herleitung
**Ausgangspunkt:** die Shockley-Gleichung ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html)):

$$I = I_S\,\Big[\exp\!\Big(\frac{U}{U_T}\Big) - 1\Big]$$

**Annahmen:** (i) ideale Kennlinie; (ii) die Änderungen sind so langsam, dass die Diode in jedem Augenblick ihrer Kennlinie folgt.

**Schritt 1**: Ableitung nach der Spannung; die Exponentialfunktion ist ihre eigene Ableitung:

$$\frac{\mathrm{d}I}{\mathrm{d}U} = \frac{I_S}{U_T}\,\exp\!\Big(\frac{U}{U_T}\Big)$$

**Schritt 2** (entscheidender Schritt): Nach der Shockley-Gleichung ist $I_S\exp(U/U_T)$ gleich $I + I_S$; die Ableitung hängt damit nur vom Strom ab:

$$\frac{\mathrm{d}I}{\mathrm{d}U} = \frac{I + I_S}{U_T}$$

**Schritt 3**: Kehrwert:

$$r_d = \frac{U_T}{I + I_S} \approx \frac{U_T}{I}$$

**Schritt 4**: Wie klein ist klein? Für eine Änderung $u$ um den Arbeitspunkt mit dem Strom $I$ ist die exakte Stromänderung

$$i = (I + I_S)\,\Big[\exp\!\Big(\frac{u}{U_T}\Big) - 1\Big] = \frac{u}{r_d}\,\Big(1 + \frac{u}{2\,U_T} + \ldots\Big)$$

Die Tangente unterschätzt den Strom also um rund $u/(2U_T)$; genau gerechnet sind es 2 % bei 1 mV, 10 % bei 5 mV und 22 % bei 10 mV. __Kleinsignal__ heißt deshalb: Spannungsänderungen klein gegen $U_T$.

**Ergebnis:**

$$r_d = \frac{\mathrm{d}U}{\mathrm{d}I} = \frac{U_T}{I + I_S} \approx \frac{U_T}{I}$$

**Woher die Faktoren kommen:** $U_T$ ist die Spannung, die den Strom um den Faktor 2,72 ändert, und je mehr Strom fließt, desto mehr Ampere entspricht dieser Faktor; $I_S$ fällt heraus, weil die Ableitung einer Exponentialfunktion wieder sie selbst ist.

**Proben:** Einheit V/A = Ω. Bei 1 mA: 25,85 mV durch 1 mA ergibt 25,9 Ω.

**Grenzen:** Bei schnellen Änderungen kommen die Kapazitäten der Diode hinzu; bei großen Strömen der Bahnwiderstand, der sich zu $r_d$ addiert.
:::

::::beispiel Kleine Änderungen in der Grundschaltung
**Gegeben:** Grundschaltung mit 5 V und 1 kΩ, Arbeitspunkt 0,683 V und 4,317 mA; die Quelle schwankt um ±0,1 V.

**Gesucht:** differentieller und statischer Widerstand, Schwankung der Diodenspannung.

**Rechnung:** Differentieller und statischer Widerstand:

$$r_d = \frac{25{,}85\ \mathrm{mV}}{4{,}317\ \mathrm{mA}} = 5{,}99\ \Omega, \qquad \frac{U}{I} = \frac{0{,}683\ \mathrm{V}}{4{,}317\ \mathrm{mA}} = 158\ \Omega$$

Im Kleinsignal-Ersatzschaltbild bilden der Widerstand und $r_d$ einen Spannungsteiler für die Schwankung:

$$u = 0{,}1\ \mathrm{V}\cdot\frac{5{,}99\ \Omega}{1000\ \Omega + 5{,}99\ \Omega} = 0{,}595\ \mathrm{mV}$$

**Ergebnis:** **$r_d$ = 6,0 Ω gegen 158 Ω statisch; ±0,1 V an der Quelle ergeben nur ±0,6 mV an der Diode.**

**Einordnung:** Die exakte Rechnung mit der Kennlinie ergibt denselben Wert. An der Diode kommt nur ein Hundertsiebzigstel der Schwankung an; darauf beruhen Spannungsreferenzen aus Dioden und die Stabilisierung mit der Z-Diode.
::::

:::fehlvorstellung
„Der Widerstand einer leitenden Diode ist Spannung durch Strom.“
Das liegt nahe, weil man Widerstände so berechnet. Im Arbeitspunkt der Grundschaltung ergibt das 158 Ω, auf Änderungen reagiert die Diode aber wie 6,0 Ω. Der statische Wert beschreibt nur den einen Punkt; wie die Diode auf ein Signal oder eine Schwankung reagiert, sagt allein die Steigung der Kennlinie.
:::

:::frage
„Warum hängt der differentielle Widerstand nicht von der Größe der Diode ab?“
Eine zehnmal größere Diode hat ein zehnmal größeres $I_S$ und braucht für denselben Strom 59,5 mV weniger Spannung; ihre Kennlinie ist nur nach links verschoben. Die Form der Exponentialfunktion bleibt gleich: Je $U_T$ mehr Spannung wächst der Strom um den Faktor 2,72, egal wo er anfängt. Deshalb haben alle idealen Dioden bei 1 mA denselben differentiellen Widerstand, 25,9 Ω; reale weichen durch den Emissionskoeffizienten und den Bahnwiderstand davon ab.
:::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Arbeitsgerade | das Gesetz des linearen Rests, an den Anschlüssen der Diode als Ersatzquelle gesehen |
| Schnittpunkt und Eindeutigkeit | Beide Gesetze gelten nur dort; steigende Kennlinie und fallende Gerade schneiden sich einmal. |
| Ersatzschaltungen und Probe | Das Gesetz der Diode wird stückweise linear; ob das gewählte Stück gilt, zeigt erst der Arbeitspunkt. |
| differentieller Widerstand | das Gesetz der Diode in der Umgebung des Arbeitspunkts, als Tangente |

Der Arbeitspunkt ist der Punkt, an dem das Gesetz des Bauteils und die Gesetze des übrigen Netzes zugleich gelten; weil die Diodenkennlinie gekrümmt ist, findet man ihn grafisch, durch Iteration oder mit linearen Ersatzschaltungen, deren Annahmen man am Ergebnis prüfen muss.

## Bedeutung und Ausblick

Dasselbe Vorgehen trägt durch die ganze Elektronik, vom [Arbeitspunkt des Transistors](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/arbeitspunkt-und-grundschaltungen.html) bis zur Wechselstromanalyse in LTspice, die jede Diode durch ihr Kleinsignalmodell ersetzt, im Kern den differentiellen Widerstand. Der nächste Artikel, [Gleichrichtung und Ladungspumpe](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/gleichrichtung-und-ladungspumpe.html), wendet die Ersatzschaltungen auf Wechselspannungen an.

**In der ausführlichen Fassung:** die Iteration mit Herleitung, warum sie so schnell konvergiert, die Genauigkeit der Modelle im Vergleich, die Bemessung eines Vorwiderstands, mehrere Arbeitspunkte bei der Tunneldiode, das Vorgehen von Schaltungssimulatoren und die Schutzdioden auch bei negativer Eingangsspannung. [Zur ausführlichen Fassung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/arbeitspunkt-und-ersatzschaltung-ausfuehrlich.html)

:::kern
- Der Arbeitspunkt ist der Schnittpunkt der Bauteilkennlinie mit der Arbeitsgeraden des übrigen Netzes.
- Arbeitsgerade: $I = (U_0 - U)/R$, durch den Leerlauf bei $U_0$ und den Kurzschluss bei $U_0/R$.
- Eine steigende Kennlinie schneidet die fallende Gerade genau einmal; weil sich die Gleichung nicht nach dem Strom auflösen lässt, löst man grafisch, iterativ oder mit Ersatzschaltungen.
- Ersatzschaltungen: ideale Diode (Schalter), Diode mit Durchlassspannung $U_{F0}$ (Quelle), Knickkennlinie (Quelle mit $r_F$); jede gilt nur im angenommenen Zustand.
- Probe: Leitende Dioden brauchen einen positiven Strom, sperrende eine Spannung unter $U_{F0}$; ein Widerspruch verlangt eine neue Annahme.
- Differentieller Widerstand: $r_d = U_T/I$, 25,9 Ω bei 1 mA; nicht zu verwechseln mit Spannung durch Strom.
- Kleinsignal heißt: Spannungsänderungen klein gegen $U_T$; 1 mV ergibt 2 % Fehler der Tangente.
:::

:::quiz
F: Warum ist der Arbeitspunkt der Schnittpunkt von Kennlinie und Arbeitsgerade?
A: Die Kennlinie enthält alle Wertepaare, die die Diode zulässt, die Arbeitsgerade alle, die die übrige Schaltung zulässt. Beide Gesetze gelten zugleich nur im Schnittpunkt.
F: Stimmt es, dass die Arbeitsgerade eine Eigenschaft der Diode ist?
A: Nein. Sie beschreibt nur die übrige Schaltung; tauscht man die Diode, bleibt die Gerade gleich und nur der Schnittpunkt wandert.
F: Welchen Strom liefert das 0,7 V-Modell in der Grundschaltung mit 5 V und 1 kΩ, und wie genau ist das?
A: (5 V − 0,7 V) durch 1 kΩ ergibt 4,30 mA. Exakt sind es 4,317 mA, das Modell liegt also um 0,4 % daneben.
F: Stimmt es, dass eine Rechnung mit der Annahme „Diode leitet“ richtig ist, sobald sie ein Ergebnis liefert?
A: Nein. Jede Annahme liefert ein Ergebnis; erst die Probe entscheidet. Eine „leitende“ Diode braucht einen positiven Strom, eine „sperrende“ eine Spannung unter $U_{F0}$.
F: Stimmt es, dass der Widerstand einer leitenden Diode Spannung durch Strom ist?
A: Nein, nicht für Änderungen. Im Arbeitspunkt der Grundschaltung ergibt Spannung durch Strom 158 Ω, auf kleine Änderungen reagiert die Diode aber wie 6,0 Ω, der differentielle Widerstand.
F: Warum ist der differentielle Widerstand bei 1 mA 25,9 Ω, und wie groß ist er bei 10 mA?
A: Er ist $U_T/I$, weil der Strom je 25,85 mV um den Faktor 2,72 wächst; die Steigung der Kennlinie beträgt bei 1 mA deshalb 1 mA je 25,85 mV. Bei 10 mA ist er zehnmal kleiner, 2,6 Ω.
:::
