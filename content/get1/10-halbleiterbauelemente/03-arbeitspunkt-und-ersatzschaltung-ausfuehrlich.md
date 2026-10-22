---
title: Arbeitspunkt und Ersatzschaltung der Diode
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Halbleiterbauelemente
order: 100400
summary: Wie man den Strom und die Spannung einer Diode in einer Schaltung findet, obwohl ihre Kennlinie gekrümmt ist: als Schnitt mit der Arbeitsgeraden, durch Iteration, mit linearen Ersatzschaltungen samt Probe der Annahmen und für kleine Änderungen mit dem differentiellen Widerstand. Ausführliche Fassung mit allen Herleitungen, der Genauigkeit der Modelle und dem Vorgehen von Schaltungssimulatoren.
tags: Arbeitspunkt, Arbeitsgerade, Lastgerade, Ersatzschaltung, differentieller Widerstand, Diode
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Die Kennlinie einer Diode sagt, welcher Strom zu welcher Spannung gehört, aber nicht, wo die Diode in einer Schaltung tatsächlich arbeitet. Das legt erst die übrige Schaltung fest.
**Der Arbeitspunkt ist der Punkt, an dem das Gesetz des Bauteils und die Gesetze des übrigen Netzes zugleich gelten; weil die Diodenkennlinie gekrümmt ist, findet man ihn grafisch, durch Iteration oder mit linearen Ersatzschaltungen, deren Annahmen man am Ergebnis prüfen muss.**

Vorausgesetzt werden [Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html), die [Kirchhoffschen Gesetze](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/kirchhoffsche-gesetze.html) und die [Ersatzquellen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/ersatzquellen-thevenin-norton.html).
Auf diesem Artikel bauen [Gleichrichtung und Ladungspumpe](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/gleichrichtung-und-ladungspumpe.html) und der [Arbeitspunkt des Transistors](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/arbeitspunkt-und-grundschaltungen.html) auf.

:::grafik
Szene: get1/halbleiterbauelemente/03-arbeitsgerade · Vorlage: schaltung-und-kennlinie
**Abbildung 1:** (a) Grundschaltung dieses Artikels: Quelle 5 V, Widerstand 1 kΩ und die Beispieldiode; der lineare Rest der Schaltung ist umrahmt. (b) Die Arbeitsgerade des Rests läuft vom Leerlauf (5 V; 0) zum Kurzschluss (0; 5 mA), die Kennlinie der Diode steigt bei 0,6 bis 0,7 V steil an; im Ausschnitt ihr Schnittpunkt bei 0,683 V und 4,32 mA. Der Arbeitspunkt ist dieser Schnittpunkt.
:::

## Was ein Arbeitspunkt ist

*Was legt fest, welcher Strom durch ein Bauteil in einer Schaltung fließt?*

**Die Akteure:**

- __Arbeitspunkt__: das Wertepaar aus Spannung $U$ und Strom $I$, mit dem ein Bauteil in einer bestimmten Schaltung arbeitet; ein Punkt auf seiner Kennlinie.
- __Arbeitspunktanalyse__: aus gegebener Schaltung den Arbeitspunkt bestimmen.
- __Arbeitspunktsynthese__: die Schaltung so bemessen, dass sich ein gewünschter Arbeitspunkt einstellt, etwa einen Vorwiderstand wählen.

**Das Zusammenspiel:** In jeder Schaltung gelten zwei Arten von Gesetzen zugleich. Jedes Bauteil gehorcht seiner eigenen Kennlinie, beim Widerstand dem ohmschen Gesetz, bei der Diode der Shockley-Gleichung. Die Verbindungen erzwingen die Kirchhoffschen Gesetze: Die Spannungen jeder Masche ergeben null, die Ströme jedes Knotens ebenso. Der Arbeitspunkt ist die Lösung, die alle diese Gleichungen zugleich erfüllt.

Bestehen alle Bauteile aus Widerständen und Quellen, sind alle Gleichungen linear, und man löst sie wie gewohnt. Ein Beispiel ist ein Widerstand, der über einen zweiten Widerstand an einer Quelle hängt: Seine Kennlinie ist eine Gerade durch den Ursprung, die Maschenregel liefert eine zweite Gerade, und beide schneiden sich im Arbeitspunkt. Mit einer Diode wird eine der beiden Linien gekrümmt; daran hängt alles Folgende.

## Die Arbeitsgerade

*Warum ist das, was die übrige Schaltung der Diode erlaubt, eine Gerade?*

**Die Akteure:**

- __$U_0$__, __$R$__: Leerlaufspannung und Innenwiderstand des linearen Rests, also der Schaltung ohne die Diode, gesehen von den Anschlüssen der Diode; in der Grundschaltung die Quelle mit 5 V und der Widerstand mit 1 kΩ.
- __$U$__, __$I$__: Spannung an der Diode und Strom durch sie, beide von der Anode zur Kathode gezählt ([Zählpfeile](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/zaehlpfeile-und-vorzeichen.html)).

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Man teilt die Schaltung in das nichtlineare Bauteil, die Diode, und den linearen Rest.

**Schritt 2**: Der Rest wirkt an den Anschlüssen der Diode wie eine [Ersatzspannungsquelle](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/ersatzquellen-thevenin-norton.html): eine Quelle $U_0$ mit dem Innenwiderstand $R$. Welche Spannung er bei welchem Strom liefert, ist eine Gerade, die __Arbeitsgerade__ (auch Lastgerade). Sie läuft durch zwei leicht zu findende Punkte: den Leerlauf, in dem kein Strom fließt und die volle Spannung $U_0$ anliegt, und den Kurzschluss, in dem die Spannung null ist und der Strom $U_0/R$ (Abbildung 1b).

**Schritt 3**: Die Diode lässt nur Wertepaare auf ihrer Kennlinie zu.

**Schritt 4**: Beide Bedingungen gelten zugleich nur im Schnittpunkt. Er ist der Arbeitspunkt, in der Grundschaltung 0,683 V und 4,32 mA.

**Schritt 5**: Die Kennlinie der Diode steigt überall, die Arbeitsgerade fällt; deshalb schneiden sie sich genau einmal, und der Arbeitspunkt ist eindeutig.

:::formel Formel
$$I = \frac{U_0 - U}{R}$$
:::

**So liest man das:** Eingabe ist die Spannung an der Diode, Ausgabe der Strom, den der Rest der Schaltung dabei liefert. Je mehr Spannung die Diode übernimmt, desto weniger bleibt für den Widerstand und desto kleiner wird der Strom. Die Steigung ist $-1/R$, in der Grundschaltung −1 mA je Volt; ein kleinerer Widerstand macht die Gerade steiler, eine größere Quellenspannung verschiebt sie parallel nach rechts.

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

:::fehlvorstellung
„Die Arbeitsgerade ist eine Eigenschaft der Diode.“
Das liegt nahe, weil man sie in dasselbe Diagramm zeichnet wie die Kennlinie der Diode. Sie beschreibt aber allein die übrige Schaltung: Tauscht man die Diode gegen eine andere, bleibt die Gerade dieselbe und nur der Schnittpunkt wandert; ändert man die Quelle oder den Widerstand, ändert sich die Gerade, und die Kennlinie bleibt. In der Grundschaltung verschieben 6 V statt 5 V die Gerade parallel, der Strom steigt von 4,32 auf etwa 5,3 mA.
:::

## Der Arbeitspunkt der Diode

*Wie findet man den Schnittpunkt, wenn die Kennlinie gekrümmt ist?*

Grafisch wie in Abbildung 1: Man zeichnet die Arbeitsgerade in das Kennlinienfeld aus dem Datenblatt und liest den Schnittpunkt ab. Das ist anschaulich, aber nur so genau wie die Zeichnung, und bei einer Quellenspannung von 5 V steht die Diodenkennlinie im Diagramm fast senkrecht.

Rechnerisch setzt man die Shockley-Gleichung in die Arbeitsgerade ein. Daraus folgt eine einzige Gleichung für den Strom:

$$U_0 = R\,I + U_T\,\ln\!\Big(\frac{I}{I_S} + 1\Big)$$

:::frage
„Warum rechnet man den Arbeitspunkt nicht einfach aus?“
Weil die Gleichung den Strom zugleich linear und im Logarithmus enthält. Eine solche Mischung lässt sich mit Grundrechenarten, Potenzen, Exponentialfunktion und Logarithmus nicht nach dem Strom auflösen. Es gibt zwar eine geschlossene Lösung mit der Lambertschen W-Funktion (Vertiefung unten), doch in der Praxis rechnet man iterativ oder mit Ersatzschaltungen.
:::

Iterieren heißt, abwechselnd die beiden Gesetze anzuwenden. Man rät eine Diodenspannung, berechnet mit der Arbeitsgeraden den Strom und mit der umgestellten Kennlinie aus diesem Strom eine bessere Spannung:

:::formel Formel
$$U_{k+1} = U_T\,\ln\!\Big(\frac{U_0 - U_k}{R\,I_S} + 1\Big)$$
:::

**So liest man das:** Eingabe ist die geschätzte Spannung $U_k$, Ausgabe die verbesserte $U_{k+1}$. Der Bruch ist der Strom der Arbeitsgeraden, geteilt durch $I_S$. Weil der Logarithmus den Strom stark staucht, wirkt sich ein Fehler der Schätzung kaum aus: Jeder Schritt verkleinert ihn auf das $U_T/(R\,I)$-Fache, also $U_T$ geteilt durch die Spannung am Widerstand; in der Grundschaltung 25,85 mV geteilt durch 4,32 V, also auf das 0,006-Fache.

Idee der Herleitung: Man stellt die Shockley-Gleichung nach der Spannung um, setzt den Strom der Arbeitsgeraden ein und schätzt mit der Ableitung, wie stark ein Fehler der Schätzung durchschlägt.

:::herleitung
**Ausgangspunkt:** die Arbeitsgerade und die Shockley-Gleichung, nach der Spannung aufgelöst ([Die Diode und ihre Kennlinie](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html)):

$$U = U_T\,\ln\!\Big(\frac{I}{I_S} + 1\Big)$$

**Annahmen:** (i) ideale Kennlinie nach Shockley; (ii) der Arbeitspunkt liegt im Durchlassbereich, der Strom ist also groß gegen $I_S$; (iii) am Widerstand fällt viel mehr Spannung ab als $U_T$.

**Schritt 1**: Den Strom aus der Arbeitsgeraden einsetzen; das ergibt die Abbildung $g$, die einer Spannung eine neue Spannung zuordnet:

$$g(U) = U_T\,\ln\!\Big(\frac{U_0 - U}{R\,I_S} + 1\Big)$$

Der Arbeitspunkt ist ihr Fixpunkt, die Spannung, die $g$ unverändert lässt.

**Schritt 2** (entscheidender Schritt): Ein kleiner Fehler $\Delta U$ der Schätzung wird um die Ableitung von $g$ verstärkt. Nach der Kettenregel:

$$g'(U) = -\frac{U_T}{U_0 - U + R\,I_S} \approx -\frac{U_T}{R\,I}$$

**Schritt 3**: Im Arbeitspunkt der Grundschaltung ist $R\,I$ = 4,32 V, also

$$|g'| = \frac{25{,}85\ \mathrm{mV}}{4{,}32\ \mathrm{V}} = 0{,}006$$

Jeder Schritt schrumpft den Fehler damit auf ein Hundertsiebzigstel.

**Ergebnis:**

$$U_{k+1} = U_T\,\ln\!\Big(\frac{U_0 - U_k}{R\,I_S} + 1\Big), \qquad \Big|\frac{\Delta U_{k+1}}{\Delta U_k}\Big| \approx \frac{U_T}{R\,I}$$

**Woher die Faktoren kommen:** Der Logarithmus kehrt die Exponentialfunktion um; $U_T/(R\,I)$ ist das Verhältnis von Temperaturspannung zur Spannung am Widerstand, so klein, weil die Kennlinie viel steiler ist als die Arbeitsgerade.

**Proben:** Im Fixpunkt ist $g(U) = U$, beide Gesetze gelten. Start bei 0,7 V: Die Folge erreicht nach zwei Schritten 0,68287 V, auf 1 µV genau (Beispiel unten).

**Grenzen:** Annahme (iii) ist die Bedingung für die Konvergenz. Bei sehr kleinen Quellenspannungen, etwa 0,5 V an 1 kΩ, fallen am Widerstand nur 3 mV ab; der Faktor ist dann 8, und die Iteration divergiert. Dann konvergiert die umgekehrte Reihenfolge, die die Arbeitsgerade nach der Spannung umstellt und mit der Exponentialfunktion rechnet; im Normalfall wächst bei ihr der Fehler mit jedem Schritt. Die Reihenfolge der beiden Gesetze ist also nicht beliebig.
:::

:::grafik
Szene: get1/halbleiterbauelemente/03-iteration · Vorlage: kennlinie-iteration
**Abbildung 2:** Fixpunktiteration im Ausschnitt um den Arbeitspunkt: Von der Schätzung 0,7 V führt die Arbeitsgerade zu 4,300 mA, die Kennlinie zurück zu 0,68276 V, die Gerade zu 4,3172 mA; danach liegt jeder Schritt im Rahmen der Zeichengenauigkeit im Arbeitspunkt 0,68287 V und 4,3171 mA. Jeder Schritt verkleinert den Fehler auf etwa ein Hundertsiebzigstel.
:::

::::beispiel Arbeitspunkt der Grundschaltung, grafisch und iterativ
**Gegeben:** Quelle 5 V, Widerstand 1 kΩ, Beispieldiode mit dem Sättigungssperrstrom 1,4572·10⁻¹⁴ A und der Temperaturspannung 25,852 mV (so genau angegeben, weil die Rechnung auf Mikrovolt geht).

**Gesucht:** die Punkte der Arbeitsgeraden und der Arbeitspunkt.

**Rechnung:** Leerlauf und Kurzschluss:

$$I(U = 5\ \mathrm{V}) = 0, \qquad I(U = 0) = \frac{5\ \mathrm{V}}{1\ \mathrm{k}\Omega} = 5\ \mathrm{mA}$$

Iteration mit dem Startwert 0,7 V. Schritt 1, Strom aus der Arbeitsgeraden und neue Spannung:

$$I_1 = \frac{5\ \mathrm{V} - 0{,}7\ \mathrm{V}}{1\ \mathrm{k}\Omega} = 4{,}300\ \mathrm{mA}, \qquad U_1 = 25{,}852\ \mathrm{mV}\cdot\ln\!\Big(\frac{4{,}300\ \mathrm{mA}}{1{,}4572\cdot10^{-14}\ \mathrm{A}}\Big) = 0{,}68276\ \mathrm{V}$$

Schritt 2:

$$I_2 = \frac{5\ \mathrm{V} - 0{,}68276\ \mathrm{V}}{1\ \mathrm{k}\Omega} = 4{,}3172\ \mathrm{mA}, \qquad U_2 = 0{,}68287\ \mathrm{V}$$

Ein dritter Schritt ändert die Spannung um weniger als 1 µV.

**Ergebnis:** **Arbeitspunkt 0,683 V und 4,317 mA; die Diode setzt 2,95 mW um.**

**Einordnung:** Von 5 V bleiben nur 0,68 V an der Diode; der Strom wird fast ganz vom Widerstand bestimmt. Erwärmt sich die Diode auf 75 °C, sinkt ihre Spannung auf 0,586 V, der Strom steigt aber nur um 2 % auf 4,41 mA: Weil am Widerstand 4,3 V abfallen, ändert eine Verschiebung der Diodenspannung um 0,1 V den Strom nur um 0,1 V geteilt durch 4,3 V.
::::

:::frage
„Kann es mehrere Arbeitspunkte geben?“
Bei einer gewöhnlichen pn-Diode nicht: Ihre Kennlinie steigt überall, die Arbeitsgerade fällt, und eine steigende und eine fallende Linie schneiden sich höchstens einmal. Mehrere Schnittpunkte gibt es nur bei Bauteilen mit einem fallenden Ast in der Kennlinie, etwa der Tunneldiode, einer extrem hoch dotierten Diode; dann kann die Gerade sie dreimal schneiden. Welcher Schnittpunkt sich einstellt, hängt dann von der Stabilität und von der Vorgeschichte ab; die Schaltung zeigt eine Hysterese.
:::

:::vertiefung
**Wie ein Schaltungssimulator den Arbeitspunkt findet.**
Programme wie LTspice lösen bei der Arbeitspunktanalyse (.op) die Gleichungen aller Knoten zugleich mit dem Newton-Verfahren: Sie ersetzen jede Kennlinie im aktuellen Schätzpunkt durch ihre Tangente, lösen das so entstandene lineare Netz und wiederholen das. Von 0,7 V aus erreicht Newton den Arbeitspunkt der Grundschaltung in vier Schritten auf 1 µV genau.
Von 0 V aus braucht das reine Verfahren 171 Schritte: Dort ist die Kennlinie so flach, dass der erste Schritt auf 5 V springt, wo die Exponentialfunktion astronomisch groß ist, und jeder folgende kommt nur um rund 26 mV zurück. Simulatoren brechen nach einer festen Zahl von Schritten ab und begrenzen deshalb die Spannungsänderung an pn-Übergängen je Schritt.
Für die Masche aus Quelle, Widerstand und Diode gibt es auch eine geschlossene Lösung mit der Lambertschen W-Funktion, der Umkehrfunktion von $x\,\exp(x)$; sie liefert 4,31713 mA, dasselbe wie die Iteration.
:::

## Lineare Ersatzschaltungen

*Wie rechnet man mit Dioden von Hand, ohne Kennlinie und Iteration?*

:::grafik
Szene: get1/halbleiterbauelemente/03-ersatzschaltungen · Vorlage: kennlinie-modelle
**Abbildung 3:** Drei Modelle über der realen Kennlinie (grau), darunter ihre Ersatzschaltbilder. (a) Ideale Diode: leitend ein Kurzschluss, sperrend eine Unterbrechung. (b) Diode mit Durchlassspannung 0,6 V: leitend eine Spannungsquelle. (c) Knickkennlinie: leitend eine Spannungsquelle mit Widerstand. Jedes Modell ersetzt die Diode je Zustand durch lineare Bauteile.
:::

**Die Akteure:**

- __$U_{F0}$__: Durchlassspannung des Modells, die Spannung, ab der die Modelldiode leitet; meist 0,6 oder 0,7 V für Silizium.
- __$r_F$__: Widerstand des Modells im leitenden Zustand, der Kehrwert der Steigung der Knickkennlinie im Diagramm Strom über Spannung; einige Ohm.

**Das Zusammenspiel:** Die gekrümmte Kennlinie wird stückweise durch Geraden ersetzt. Dann ist die Diode in jedem Zustand ein lineares Bauteil: leitend eine Spannungsquelle, gegebenenfalls mit Widerstand; sperrend eine Unterbrechung. Mit diesen Ersatzschaltungen rechnet man wie mit jedem linearen Netz.
Der Preis ist, dass man vorher wissen muss, in welchem Zustand die Diode ist, und das Ergebnis anschließend prüfen muss (Abschnitt *Schaltungen mit mehreren Dioden*).

:::formel Definition
$$U = U_{F0} + r_F\,I \quad\text{für } I > 0$$

$$I = 0 \quad\text{für } U < U_{F0}$$
:::

**So liest man das:** Das ist die __Knickkennlinie__: Leitet die Diode, fällt an ihr die Durchlassspannung $U_{F0}$ plus ein Anteil proportional zum Strom ab; sperrt sie, fließt kein Strom. Mit $r_F$ = 0 wird daraus die __Diode mit Durchlassspannung__, mit $U_{F0}$ = 0 und $r_F$ = 0 die __ideale Diode__, ein Schalter, der in Durchlassrichtung schließt.
Man definiert die Modelle so, weil jedes Stück eine Gerade ist und eine Gerade einem linearen Bauteil entspricht; zugleich bleibt die wichtigste Eigenschaft der Diode erhalten, der Unterschied zwischen beiden Richtungen.

**Welche Durchlassspannung?** Man nimmt die Spannung der echten Kennlinie bei dem Strom, den man erwartet. Für die Beispieldiode sind das 0,645 V bei 1 mA und 0,705 V bei 10 mA; deshalb rechnen viele mit 0,7 V, manche mit 0,6 V. Für eine Knickkennlinie legt man eine Gerade durch zwei Punkte des erwarteten Strombereichs, etwa durch 1 mA und 10 mA: Das ergibt $U_{F0}$ = 0,638 V und $r_F$ = 6,6 Ω.

:::grafik
Szene: get1/halbleiterbauelemente/03-modellvergleich · Vorlage: kennlinie-ausschnitt
**Abbildung 4:** Arbeitsgerade der Grundschaltung zwischen 0 und 0,8 V mit den Schnittpunkten der Modelle: ideale Diode 5,00 mA bei 0 V, 0,6 V-Modell 4,40 mA, 0,7 V-Modell 4,30 mA, exakt 4,317 mA bei 0,683 V. Weil die Gerade flach verläuft, hängt der Strom kaum vom Modell ab.
:::

Abbildung 4 zeigt, warum die groben Modelle meist genügen: Die Arbeitsgerade ist flach, weil die Quellenspannung groß gegen die Durchlassspannung ist. Ein Fehler in der Diodenspannung ändert den Strom nur um diesen Fehler geteilt durch den Widerstand. Die ideale Diode verschiebt den Strom um 16 %, das 0,6 V-Modell um 2 %, das 0,7 V-Modell um 0,4 %.
Bei kleinen Quellenspannungen wächst der Fehler: Mit 1 V statt 5 V fließen exakt 0,38 mA bei 0,62 V. Das 0,7 V-Modell liegt dann um ein Fünftel daneben, das 0,6 V-Modell um 5 %, und die ideale Diode ist mit dem 2,6-Fachen unbrauchbar. Die Durchlassspannung des Modells muss deshalb zum Strom passen.

::::beispiel Die drei Modelle in der Grundschaltung
**Gegeben:** Grundschaltung mit 5 V und 1 kΩ; exakter Arbeitspunkt 0,683 V und 4,317 mA; Knickkennlinie mit 0,638 V und 6,6 Ω.

**Gesucht:** der Strom mit jedem Modell und seine Abweichung.

**Rechnung:** Ideale Diode, leitend ein Kurzschluss:

$$I = \frac{5\ \mathrm{V}}{1\ \mathrm{k}\Omega} = 5{,}00\ \mathrm{mA}$$

Diode mit Durchlassspannung, leitend eine Quelle:

$$I = \frac{5\ \mathrm{V} - 0{,}6\ \mathrm{V}}{1\ \mathrm{k}\Omega} = 4{,}40\ \mathrm{mA}, \qquad I = \frac{5\ \mathrm{V} - 0{,}7\ \mathrm{V}}{1\ \mathrm{k}\Omega} = 4{,}30\ \mathrm{mA}$$

Knickkennlinie, Quelle mit Widerstand in Reihe zum Vorwiderstand:

$$I = \frac{5\ \mathrm{V} - 0{,}638\ \mathrm{V}}{1\ \mathrm{k}\Omega + 6{,}6\ \Omega} = 4{,}333\ \mathrm{mA}, \qquad U = 0{,}638\ \mathrm{V} + 6{,}6\ \Omega\cdot4{,}333\ \mathrm{mA} = 0{,}667\ \mathrm{V}$$

**Ergebnis:** **5,00 mA (+16 %), 4,40 mA (+1,9 %), 4,30 mA (−0,4 %) und 4,33 mA (+0,4 %) gegen exakt 4,317 mA.**

**Einordnung:** Für den Strom genügt hier jedes Modell außer der idealen Diode; für die Spannung an der Diode liegt die Knickkennlinie 16 mV daneben, das 0,7 V-Modell 17 mV. Eine Knickkennlinie ist nur so gut wie der Bereich, für den man sie anpasst: Als Tangente bei 1 mA, mit 25,9 Ω, läge sie im Arbeitspunkt 47 mV zu hoch.
::::

Mit denselben Mitteln bemisst man Schaltungen, die __Arbeitspunktsynthese__: Soll durch die Beispieldiode an 5 V ein Strom von 5 mA fließen, braucht sie nach ihrer Kennlinie dort 0,687 V, und der Vorwiderstand muss die übrigen 4,313 V tragen; mit dem 0,7 V-Modell ergäben sich 860 Ω statt 863 Ω.

::::beispiel Vorwiderstand für 5 mA
**Gegeben:** Quelle 5 V, Beispieldiode, gewünschter Strom 5 mA.

**Gesucht:** der Vorwiderstand und der Strom mit den nächstgelegenen Normwerten.

**Rechnung:** Durchlassspannung bei 5 mA:

$$U = 25{,}85\ \mathrm{mV}\cdot\ln\!\Big(\frac{5\ \mathrm{mA}}{1{,}457\cdot10^{-14}\ \mathrm{A}}\Big) = 0{,}687\ \mathrm{V}$$

Vorwiderstand nach der Arbeitsgeraden:

$$R = \frac{5\ \mathrm{V} - 0{,}687\ \mathrm{V}}{5\ \mathrm{mA}} = 863\ \Omega$$

Widerstände gibt es nur in Normwerten, abgestuft nach der Reihe E24; die nächsten sind 820 Ω und 910 Ω. Mit ihnen ergeben sich, wieder iterativ gerechnet, 5,26 mA und 4,74 mA.

**Ergebnis:** **863 Ω; mit 820 Ω fließen 5,26 mA, mit 910 Ω 4,74 mA.**

**Einordnung:** Die Abweichung des Stroms folgt fast genau der des Widerstands, um 5 %, weil die Diodenspannung sich dabei nur um gut 1 mV ändert.
::::

## Schaltungen mit mehreren Dioden

*Wie findet man heraus, welche Dioden leiten und welche sperren?*

:::grafik
Szene: get1/halbleiterbauelemente/03-schutzdioden · Vorlage: schaltung-potenziale
**Abbildung 5:** Eingangsschutz eines Logikbausteins: Die Eingangsspannung gelangt über 1 kΩ zum Knoten A; D1 führt von A zur Versorgung 5 V, D2 von Masse nach A; die Last von 10 kΩ liegt zwischen A und Masse. Bei 9 V Eingangsspannung: Unter der Annahme „beide sperren“ läge A auf 8,18 V und an D1 lägen 3,18 V, ein Widerspruch; mit „D1 leitet“ liegt A auf 5,6 V, durch D1 fließen 2,84 mA, an D2 liegen −5,6 V. Die Probe an den Potenzialen zeigt, welche Diode leiten muss.
:::

Mit einer Diode weiß man meist, ob sie leitet. Mit mehreren hängt der Zustand jeder Diode von den anderen ab, und die Ersatzschaltung, die man einsetzen darf, hängt vom Zustand ab, den man erst berechnen will. Man löst das, indem man rät und prüft.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Man nimmt für jede Diode einen Zustand an, leitend oder sperrend, möglichst plausibel.

**Schritt 2**: Man ersetzt jede Diode durch die Ersatzschaltung ihres Zustands, mit dem 0,6 V-Modell also eine leitende Diode durch eine Quelle von 0,6 V und eine sperrende durch eine Unterbrechung, und berechnet das lineare Netz.

**Schritt 3** (Probe): Jede leitend angenommene Diode muss einen positiven Strom führen, jede sperrend angenommene eine Spannung unter $U_{F0}$ haben. Ein negativer Strom durch eine „leitende“ Diode oder mehr als 0,6 V an einer „sperrenden“ ist ein Widerspruch.

**Schritt 4**: Bei einem Widerspruch war die Annahme falsch; man wählt eine neue und rechnet erneut. Sind alle Proben erfüllt, ist die Lösung gefunden. Weil jede Diode zwei Zustände hat, gibt es bei $n$ Dioden $2^n$ Kombinationen.

**Schritt 5**: Viele Kombinationen scheiden ohne Rechnung aus, wenn man die Potenziale betrachtet: Die Spannung an einer Diode ist die Differenz der [Potenziale](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/elektrische-feldstarke-und-potenzial/arbeit-potenzial-und-spannung.html) von Anode und Kathode. Liegt die Anode einer angeblich sperrenden Diode um mehr als 0,6 V über ihrer Kathode, muss sie leiten.

::::beispiel Schutzdioden am Eingang bei +9 V und −3 V
**Gegeben:** Schaltung aus Abbildung 5: Vorwiderstand 1 kΩ, Last 10 kΩ, Versorgung 5 V; Modell mit Durchlassspannung 0,6 V; Eingangsspannung (a) +9 V, (b) −3 V.

**Gesucht:** Zustände der Dioden, Potenzial von A und Diodenströme.

**Rechnung:** (a) Annahme „beide sperren“: Dann bilden Vorwiderstand und Last einen Spannungsteiler.

$$\varphi_A = 9\ \mathrm{V}\cdot\frac{10\ \mathrm{k}\Omega}{11\ \mathrm{k}\Omega} = 8{,}18\ \mathrm{V}$$

An D1 läge damit die Differenz zu den 5 V der Versorgung, 3,18 V, mehr als 0,6 V: Widerspruch, D1 muss leiten. Neue Annahme „D1 leitet, D2 sperrt“; A liegt 0,6 V über der Versorgung:

$$\varphi_A = 5\ \mathrm{V} + 0{,}6\ \mathrm{V} = 5{,}6\ \mathrm{V}$$

Ströme durch Vorwiderstand und Last und, nach der Knotenregel, durch D1:

$$I_R = \frac{9\ \mathrm{V} - 5{,}6\ \mathrm{V}}{1\ \mathrm{k}\Omega} = 3{,}40\ \mathrm{mA}, \qquad I_L = \frac{5{,}6\ \mathrm{V}}{10\ \mathrm{k}\Omega} = 0{,}56\ \mathrm{mA}$$

$$I_{D1} = 3{,}40\ \mathrm{mA} - 0{,}56\ \mathrm{mA} = 2{,}84\ \mathrm{mA}$$

Probe: Der Strom durch D1 ist positiv; an D2, deren Anode an Masse liegt, liegen −5,6 V, weniger als 0,6 V. Beides passt.

(b) Bei −3 V läge A mit „beide sperren“ auf −2,73 V; an D2 lägen dann +2,73 V, Widerspruch. Mit „D2 leitet“ liegt A auf −0,6 V:

$$I_R = \frac{-3\ \mathrm{V} - (-0{,}6\ \mathrm{V})}{1\ \mathrm{k}\Omega} = -2{,}40\ \mathrm{mA}, \qquad I_L = \frac{-0{,}6\ \mathrm{V}}{10\ \mathrm{k}\Omega} = -0{,}06\ \mathrm{mA}$$

D2 führt von Masse nach A die Differenz, 2,34 mA; an D1 liegen −5,6 V.

**Ergebnis:** **(a) D1 leitet mit 2,84 mA, A liegt auf 5,6 V; (b) D2 leitet mit 2,34 mA, A liegt auf −0,6 V.**

**Einordnung:** Die Dioden halten den Eingang zwischen −0,6 V und 5,6 V, wie es Schutzschaltungen von Logikbausteinen tun; der Vorwiderstand begrenzt den Strom. Mit den exakten Kennlinien liegt A bei 9 V auf 5,671 V und D1 führt 2,76 mA, das Modell trifft den Strom also auf 3 %.
::::

:::fehlvorstellung
„Wenn die Rechnung mit der Annahme ‚Diode leitet‘ ein Ergebnis liefert, stimmt es.“
Das liegt nahe, weil eine lineare Rechnung immer ein Ergebnis liefert. Ein Ergebnis gibt es aber auch für jede falsche Annahme: Im Beispiel liefert „beide sperren“ bei 9 V glatt 8,18 V am Knoten A. Ob es physikalisch möglich ist, entscheidet erst die Probe, hier die 3,18 V an einer angeblich sperrenden Diode. Eine Ersatzschaltung gilt nur in dem Zustand, für den man sie eingesetzt hat.
:::

## Der differentielle Widerstand

*Wie reagiert eine Diode auf kleine Änderungen um ihren Arbeitspunkt?*

:::grafik
Szene: get1/halbleiterbauelemente/03-kleinsignal · Vorlage: kennlinie-tangente
**Abbildung 6:** (a) Kennlinie der Beispieldiode um den Arbeitspunkt 4,32 mA mit der Tangente, Steigung 1/(6,0 Ω). Ein kleiner Spannungshub von ±0,6 mV erzeugt einen unverzerrten Stromhub von ±0,1 mA; ein großer von ±20 mV wird sichtbar verzerrt. (b) Kleinsignal-Ersatzschaltbild: Die Diode ist durch ihren differentiellen Widerstand ersetzt. Für kleine Änderungen verhält sich die Diode wie ein Widerstand $U_T/I$.
:::

**Die Akteure:**

- __$u$__, __$i$__: kleine Änderungen von Spannung und Strom um den Arbeitspunkt; klein geschrieben wie zeitabhängige Größen.
- __$r_d$__: __differentieller Widerstand__, die Spannungsänderung je Stromänderung im Arbeitspunkt; in Ω; 25,9 Ω bei 1 mA.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Schwankt eine Spannung in der Schaltung ein wenig, etwa durch ein Signal oder eine unruhige Versorgung, bewegt sich der Arbeitspunkt ein kleines Stück auf der Kennlinie.

**Schritt 2**: Auf einem kurzen Stück ist jede glatte Kurve fast gerade. Man ersetzt die Kennlinie dort durch ihre Tangente (Abbildung 6a).

**Schritt 3**: Die Steigung dieser Tangente legt fest, wie stark der Strom auf eine Spannungsänderung reagiert. Ihr Kehrwert ist der differentielle Widerstand.

**Schritt 4**: Für die Änderungen ist die Diode damit ein gewöhnlicher Widerstand. Man ersetzt sie im __Kleinsignal-Ersatzschaltbild__ durch $r_d$ und rechnet mit den Änderungen wie in einem linearen Netz (Abbildung 6b).

:::formel Formel
$$r_d = \frac{\mathrm{d}U}{\mathrm{d}I} = \frac{U_T}{I + I_S} \approx \frac{U_T}{I}$$
:::

**So liest man das:** Eingabe ist der Strom im Arbeitspunkt, Ausgabe der differentielle Widerstand. Er sinkt umgekehrt proportional zum Strom: 25,9 kΩ bei 1 µA, 25,9 Ω bei 1 mA, 6,0 Ω im Arbeitspunkt der Grundschaltung, 2,6 Ω bei 10 mA.
Er hängt weder vom Material noch von der Fläche der Diode ab, nur vom Strom und von der Temperatur. Davon zu unterscheiden ist der statische Wert, Spannung durch Strom: im Arbeitspunkt der Grundschaltung 158 Ω, sechsundzwanzigmal mehr.

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

**Gesucht:** differentieller und statischer Widerstand, Schwankung der Diodenspannung und des Stroms.

**Rechnung:** Differentieller und statischer Widerstand:

$$r_d = \frac{25{,}85\ \mathrm{mV}}{4{,}317\ \mathrm{mA}} = 5{,}99\ \Omega, \qquad \frac{U}{I} = \frac{0{,}683\ \mathrm{V}}{4{,}317\ \mathrm{mA}} = 158\ \Omega$$

Im Kleinsignal-Ersatzschaltbild bilden der Widerstand und $r_d$ einen Spannungsteiler für die Schwankung:

$$u = 0{,}1\ \mathrm{V}\cdot\frac{5{,}99\ \Omega}{1000\ \Omega + 5{,}99\ \Omega} = 0{,}595\ \mathrm{mV}, \qquad i = \frac{0{,}1\ \mathrm{V}}{1006\ \Omega} = 0{,}0994\ \mathrm{mA}$$

Die Schwankung an der Diode ist mit 0,6 mV klein gegen $U_T$; die Tangente ist also auf 1 % genau. Die exakte Rechnung mit der Kennlinie ergibt denselben Wert, 0,595 mV.

**Ergebnis:** **$r_d$ = 6,0 Ω gegen 158 Ω statisch; ±0,1 V an der Quelle ergeben ±0,6 mV an der Diode und ±0,1 mA Strom.**

**Einordnung:** Die Spannung an der Diode bleibt fast konstant: Von der Schwankung fallen 99,4 % am Widerstand ab, obwohl die Diode die volle Stromschwankung führt; an ihr kommt nur etwa ein Hundertsiebzigstel an, derselbe Faktor, auf den die Iteration den Fehler je Schritt verkleinert. Darauf beruhen Spannungsreferenzen aus Dioden und die Stabilisierung mit der [Z-Diode](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/diode-und-kennlinie.html), deren differentieller Widerstand im Durchbruch dieselbe Rolle spielt.
::::

:::fehlvorstellung
„Der Widerstand einer leitenden Diode ist Spannung durch Strom.“
Das liegt nahe, weil man Widerstände so berechnet. Bei der Diode ergibt das im Arbeitspunkt der Grundschaltung 158 Ω, für Änderungen wirkt sie aber wie 6,0 Ω. Der statische Wert beschreibt nur den einen Punkt; wie die Diode auf ein Signal oder eine Schwankung reagiert, sagt allein die Steigung der Kennlinie. Ein ohmscher Widerstand hat beide Werte gleich, eine Diode nicht.
:::

:::frage
„Warum hängt der differentielle Widerstand nicht von der Größe der Diode ab?“
Eine zehnmal größere Diode hat ein zehnmal größeres $I_S$ und braucht für denselben Strom 59,5 mV weniger Spannung; ihre Kennlinie ist nur nach links verschoben. Die Form der Exponentialfunktion bleibt gleich: Je $U_T$ mehr Spannung wächst der Strom um den Faktor 2,72, egal wo er anfängt. Deshalb haben alle idealen Dioden bei 1 mA denselben differentiellen Widerstand, 25,9 Ω; reale weichen durch den Emissionskoeffizienten und den Bahnwiderstand davon ab.
:::

Schaltungssimulatoren rechnen bei der Wechselstromanalyse (.ac) genau so: Sie bestimmen den Arbeitspunkt und ersetzen jede Diode durch ihr Kleinsignalmodell: den differentiellen Widerstand, dazu die Kapazitäten und den Bahnwiderstand, soweit das Diodenmodell sie enthält. Ihr Ergebnis hängt deshalb nicht von der eingetragenen Signalamplitude ab; die Zeitbereichsanalyse (.tran) rechnet dagegen mit der vollständigen Kennlinie.

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Arbeitsgerade | das Gesetz des linearen Rests, an den Anschlüssen der Diode als Ersatzquelle gesehen |
| Schnittpunkt und Eindeutigkeit | Beide Gesetze gelten nur dort; steigende Kennlinie und fallende Gerade schneiden sich einmal. |
| Iteration | abwechselnd beide Gesetze anwenden, bis sie übereinstimmen |
| Ersatzschaltungen und Probe | Das Gesetz der Diode wird stückweise linear; ob das gewählte Stück gilt, zeigt erst der Arbeitspunkt. |
| Potenzialbetrachtung | die Gesetze der Diode als Bedingungen an die Potenziale ihrer Anschlüsse |
| differentieller Widerstand | das Gesetz der Diode in der Umgebung des Arbeitspunkts, als Tangente |

Der Arbeitspunkt ist der Punkt, an dem das Gesetz des Bauteils und die Gesetze des übrigen Netzes zugleich gelten; weil die Diodenkennlinie gekrümmt ist, findet man ihn grafisch, durch Iteration oder mit linearen Ersatzschaltungen, deren Annahmen man am Ergebnis prüfen muss.

## Bedeutung und Ausblick

Dasselbe Vorgehen trägt durch die ganze Elektronik: Den Arbeitspunkt eines Transistors findet man mit seiner Arbeitsgeraden im Kennlinienfeld, und Verstärker berechnet man im Kleinsignal mit differentiellen Widerständen ([Arbeitspunkt und Grundschaltungen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/bipolartransistoren/arbeitspunkt-und-grundschaltungen.html)).
In der Simulation, etwa mit LTspice, begegnet die Unterscheidung von Arbeitspunkt und Kleinsignal als Arbeitspunktanalyse und Wechselstromanalyse.
Der nächste Artikel, [Gleichrichtung und Ladungspumpe](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/halbleiterbauelemente/gleichrichtung-und-ladungspumpe.html), wendet die Ersatzschaltungen auf Schaltungen mit Wechselspannung und Kondensatoren an.

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
F: Durch welche zwei Punkte zeichnet man die Arbeitsgerade, und warum ist sie eine Gerade?
A: Durch den Leerlauf, Strom null bei der Spannung $U_0$, und den Kurzschluss, Spannung null beim Strom $U_0/R$. Sie ist eine Gerade, weil der Rest der Schaltung linear ist und an den Anschlüssen wie eine Ersatzspannungsquelle wirkt.
F: Stimmt es, dass die Arbeitsgerade eine Eigenschaft der Diode ist?
A: Nein. Sie beschreibt nur die übrige Schaltung; tauscht man die Diode, bleibt die Gerade gleich und nur der Schnittpunkt wandert.
F: Warum erreicht die Iteration den Arbeitspunkt schon nach zwei Schritten auf 1 µV genau?
A: Weil jeder Schritt den Fehler auf das $U_T/(R\,I)$-Fache verkleinert, $U_T$ geteilt durch die Spannung am Widerstand, in der Grundschaltung auf das 0,006-Fache. Der Logarithmus der Kennlinie staucht den Fehler des geschätzten Stroms fast auf null.
F: Welchen Strom liefert das 0,7 V-Modell in der Grundschaltung mit 5 V und 1 kΩ, und wie genau ist das?
A: (5 V − 0,7 V) durch 1 kΩ ergibt 4,30 mA. Exakt sind es 4,317 mA, das Modell liegt also um 0,4 % daneben.
F: Wann genügt die ideale Diode als Modell?
A: Wenn die übrigen Spannungen groß gegen die Durchlassspannung sind; sie verschiebt den Strom etwa um die Durchlassspannung geteilt durch die Spannung am Vorwiderstand. In der Grundschaltung mit 5 V sind das schon 16 %, bei 1 V ist sie unbrauchbar.
F: Stimmt es, dass eine Rechnung mit der Annahme „Diode leitet“ richtig ist, sobald sie ein Ergebnis liefert?
A: Nein. Jede Annahme liefert ein Ergebnis; erst die Probe entscheidet. Eine „leitende“ Diode braucht einen positiven Strom, eine „sperrende“ eine Spannung unter $U_{F0}$.
F: Woran erkennt man ohne Rechnung, dass eine Diode leiten muss?
A: An den Potenzialen: Liegt ihre Anode unter der Annahme „sperrt“ mehr als 0,6 V über ihrer Kathode, ist die Annahme falsch. Bei den Schutzdioden mit 9 V Eingangsspannung lägen an D1 3,18 V.
F: Stimmt es, dass der Widerstand einer leitenden Diode Spannung durch Strom ist?
A: Nein, nicht für Änderungen. Im Arbeitspunkt der Grundschaltung ergibt Spannung durch Strom 158 Ω, auf kleine Änderungen reagiert die Diode aber wie 6,0 Ω, der differentielle Widerstand.
F: Warum ist der differentielle Widerstand bei 1 mA 25,9 Ω, und wie groß ist er bei 10 mA?
A: Er ist $U_T/I$, weil der Strom je 25,85 mV um den Faktor 2,72 wächst; die Steigung der Kennlinie beträgt bei 1 mA deshalb 1 mA je 25,85 mV. Bei 10 mA ist er zehnmal kleiner, 2,6 Ω.
:::

