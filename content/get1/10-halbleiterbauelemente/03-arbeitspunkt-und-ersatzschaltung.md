---
title: Arbeitspunkt und Ersatzschaltung der Diode
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Halbleiterbauelemente
order: 100400
summary: Von Grund auf – wie man in einer Schaltung den Betriebszustand einer Diode findet, obwohl ihre Kennlinie gekrümmt ist: als Schnitt von Kennlinie und Arbeitsgerade, durch Iteration wie im Simulator oder mit linearen Ersatzschaltungen. Leitbild ist ein Rückschlagventil am Ende einer Zuleitung von einem Wasserturm. Mit Arbeitspunkt, Analyse und Synthese, der Arbeitsgerade als Kennlinie der Ersatzquelle, der Eindeutigkeit des Arbeitspunkts, den Ersatzschaltungen ideale Diode, Diode mit Durchlassspannung und Knickkennlinie, dem differentiellen Widerstand für kleine Änderungen sowie dem Verfahren für Schaltungen mit mehreren Dioden mit Annahmen, Probe und Potenzialbetrachtung. Mit Beispiel-Seite.
tags: Arbeitspunkt, Arbeitsgerade, Lastgerade, Ersatzschaltung, differentieller Widerstand, Diode
---

## Anschaulich

In einem Netz aus Widerständen gibt das Ohmsche Gesetz zu jeder Spannung den Strom. Bei einer Diode geht das nicht so einfach: Ihre Kennlinie ist gekrümmt,
und welcher Strom fließt, hängt davon ab, was der Rest der Schaltung bei welcher Spannung liefern kann. Dieser Artikel zeigt drei Wege zum Ergebnis:
grafisch, numerisch und mit vereinfachten linearen Ersatzschaltungen.

**Das Leitbild dieses Artikels:** **ein Rückschlagventil am Ende einer Zuleitung.** Ein Wasserturm speist über eine lange, enge Zuleitung ein
Rückschlagventil, wie in den vorigen Artikeln das Bild der Diode von außen. Seine Feder gibt erst ab einem Mindestdruck nach, darüber öffnet es rasch weiter.
Gefragt ist, welcher Druck am Ventil liegt und wie viel Wasser fließt. Das Ventil allein sagt nur, wie viel es bei welchem Druck durchlässt. Die Zuleitung
allein sagt nur, wie viel bei welchem Gegendruck an ihrem Ende ankommt. Beides muss zugleich stimmen.

Drei Folgerungen:

- **Zwei Bedingungen, ein Punkt.** In einem Diagramm aus Druck und Durchfluss ist das Ventil eine steigende Kurve, die Zuleitung eine fallende. Ihr
  Schnittpunkt ist der Zustand, in dem sich alles einstellt: der Arbeitspunkt.
- **Die Zuleitung ist eine Gerade.** Ist das Ventil zu, steht am Ende der volle Turmdruck, und es fließt nichts. Mündet die Leitung frei, fließt das Meiste,
  bei Druck null. Dazwischen nimmt der Durchfluss gleichmäßig ab, weil die Leitung linear ist.
- **Einfache Ventilmodelle genügen oft.** Für Rechnungen von Hand ersetzt man das Ventil durch ein offenes Rohr, durch ein Rohr, das erst ab einem festen
  Druck öffnet, oder zusätzlich mit einer kleinen Engstelle. Bei mehreren Ventilen rät man, welche offen sind, rechnet und prüft.

:::grafik
Szene: get1/halbleiterbauelemente/03-ventil-zuleitung · Vorlage: arbeitspunkt-ventil
Links ein Wasserturm, aus dem eine lange, enge Zuleitung zu einem Rückschlagventil mit Feder führt; dahinter fließt das Wasser frei ab. Ein Regler stellt die
Höhe des Turms ein, ein zweiter die Enge der Zuleitung. Am Ventil zeigt ein Manometer den Druck, ein Pfeil im Rohr den Durchfluss. Rechts ein Diagramm mit dem
Druck am Ventil nach rechts und dem Durchfluss nach oben: die fallende Gerade der Zuleitung vom vollen Turmdruck auf der Druckachse bis zum größten Durchfluss
auf der Durchflussachse, und die Kennlinie des Ventils, flach bis zum Öffnungsdruck und dann steil. Ihr Schnittpunkt leuchtet als Arbeitspunkt; dreht man an
den Reglern, wandert die Gerade, und der Punkt gleitet auf der Kennlinie. Kernaussage: Der Betriebszustand ist der Punkt, an dem Zuleitung und Ventil
dasselbe sagen. (Rot = Ventil und seine Kennlinie, blau = Wasser und Gerade der Zuleitung, orange = Arbeitspunkt, grau = Achsen und Turm.)
:::

## Was ein Arbeitspunkt ist

Das Skript definiert in Abschnitt 10.4.1: Der __Arbeitspunkt__ (AP) eines Bauteils ist der Punkt auf seiner Kennlinie, der durch den Strom durch das Bauteil
und die Spannung über ihm festgelegt ist. Man schreibt ihn als Wertepaar aus Spannung und Strom, $(U_\text{AP}, I_\text{AP})$.

Zwei Aufgaben kommen dabei vor. Die __Arbeitspunktanalyse__ bestimmt die Arbeitspunkte der Bauteile einer gegebenen Schaltung. Die __Arbeitspunktsynthese__
geht umgekehrt vor: Man wählt und bemisst die Bauteile so, dass sich ein gewünschter Arbeitspunkt einstellt, etwa der Strom durch eine Leuchtdiode.

In linearen Netzen liefern die Verfahren der Kapitel 7 bis 9 die Arbeitspunkte. Mit nichtlinearen Bauteilen wie Dioden bleibt, wie das Skript sagt, bei
kleinen Netzen die grafische Lösung, bei großen die numerische, und für die Rechnung von Hand braucht man vereinfachte lineare Ersatzschaltungen.

**Im Bild:** Der Arbeitspunkt ist das Paar aus Druck am Ventil und Durchfluss, das sich einstellt, wenn man den Turm anschließt.

## Die Arbeitsgerade

Alles außer dem betrachteten Bauteil ist oft ein lineares Netz aus Quellen und Widerständen. Nach dem Artikel über Ersatzquellen verhält es sich an den
beiden Klemmen des Bauteils wie eine Ersatzspannungsquelle: eine Quelle mit der __Leerlaufspannung__ $U_{LL}$ in Reihe mit dem __Innenwiderstand__ $R_i$; ihr
__Kurzschlussstrom__ ist $I_{KS}$, der Quotient aus beiden. Liegt am Bauteil die Spannung $U$ und fließt in es der Strom $I$, beide im Verbraucherzählpfeilsystem
des Bauteils gezählt, so muss gelten:

:::formel
$$I = \frac{U_{LL} - U}{R_i}.$$
:::

**So liest man das:** Eingabe ist die Spannung am Bauteil, Ausgabe der Strom, den das übrige Netz bei dieser Spannung liefert. Das ist eine fallende Gerade, die
__Arbeitsgerade__ oder __Lastgerade__, mit der Steigung $-1/R_i$. Sie schneidet die Spannungsachse bei $U_{LL}$, im Leerlauf, wenn kein Strom fließt, und die
Stromachse bei $I_{KS}$, im Kurzschluss, wenn am Bauteil keine Spannung liegt; mit diesen zwei Punkten zeichnet man sie, wie das Skript empfiehlt. Sie hängt
nicht vom Bauteil ab und zeigt alle Zustände, die das übrige Netz überhaupt zulässt. Der Arbeitspunkt ist ihr Schnittpunkt mit der Kennlinie des Bauteils.

Das Skript zeigt das in Bild 10.13 an einer Quelle $U$ mit einem Widerstand $R$ in Reihe und einem Widerstand $R_1$ als Bauteil; dort sind $U_{LL}$ und $R_i$
einfach $U$ und $R$. Die Gleichung 10.2 ist die Kennlinie von $R_1$, eine Gerade durch den Ursprung, und 10.4 die Arbeitsgerade. Die Bildunterschrift „Kennlinie
und Schematische Aufbau“ ist dort aus Bild 10.11 übernommen.

**Im Bild:** Je mehr Gegendruck das Ventil hält, desto weniger Wasser kommt durch die Zuleitung; ist es ganz zu, steht der volle Turmdruck an.

:::herleitung
**Die Ersatzquelle.** Ein lineares Netz mit Quellen ist an zwei Klemmen nach dem Artikel über Ersatzquellen gleichwertig zu einer Quelle $U_{LL}$ in Reihe mit
$R_i$. Mit dem Bauteil an den Klemmen bilden beide eine Masche, und nach der Maschenregel ist die Quellenspannung die Summe der Spannung am Innenwiderstand und
der am Bauteil:

$$U_{LL} = R_i\,I + U.$$

**Nach dem Strom aufgelöst** ergibt sich die Formel. Für die beiden Achsenpunkte setzt man einmal den Strom und einmal die Spannung null; der zweite Punkt
ergibt den Kurzschlussstrom $U_{LL}/R_i$.

**Im Skript.** Für die Quelle $U$ mit $R$ ist das Gleichung 10.3, die Summe der Spannungen an $R$ und $R_1$, nach dem Strom aufgelöst Gleichung 10.4. Im Bild:
Der Druckverlust in der Zuleitung ist Durchfluss mal Enge, und was übrig bleibt, liegt am Ventil.
:::

::::beispiel Die Arbeitsgerade des Referenznetzes
Das Referenznetz aus dem Artikel über Ersatzquellen: $U_q$ speist über $R_1$ einen Mittelknoten M, $R_2$ führt von M nach B, $R_3$ von M zur Klemme A.

$$U_q = 12\,\text{V}, \qquad R_1 = 6\,\text{k}\Omega, \qquad R_2 = 3\,\text{k}\Omega, \qquad R_3 = 2\,\text{k}\Omega.$$

**Die Ersatzquelle.** Wie dort berechnet:

$$U_{LL} = 4\,\text{V}, \qquad I_{KS} = 1\,\text{mA}, \qquad R_i = 4\,\text{k}\Omega.$$

**Die Arbeitsgerade** geht also von $(4\,\text{V}, 0)$ nach $(0, 1\,\text{mA})$:

$$I = \frac{4\,\text{V} - U}{4\,\text{k}\Omega}.$$

**Ein Widerstand als Bauteil.** Mit $R_L = 4\,\text{k}\Omega$ an den Klemmen ist dessen Kennlinie die Ursprungsgerade mit der Steigung $1/R_L$. Gleichsetzen:

$$\frac{U}{4\,\text{k}\Omega} = \frac{4\,\text{V} - U}{4\,\text{k}\Omega}, \qquad U_\text{AP} = 2\,\text{V}, \qquad I_\text{AP} = 0{,}5\,\text{mA}.$$

Das ist das Ergebnis, das der Artikel über Ersatzquellen mit dem ganzen Netz gerechnet hat. Im Diagramm schneiden sich die beiden Geraden genau in der Mitte
der Arbeitsgeraden.

**Im Bild:** Ein Turm von $4$ mit einer Zuleitung der Enge $4\,\text{k}\Omega$; am Ende ein gleich enges Rohr, und der Druck teilt sich halb und halb.
::::

## Der Arbeitspunkt der Diode

Ist das Bauteil eine Diode, tritt an die Stelle der Ursprungsgeraden ihre Kennlinie, die Shockley-Gleichung aus dem vorigen Artikel.

**Die zwei Akteure:**

- die Arbeitsgerade des übrigen Netzes, mit $U_{LL}$ in Volt und $R_i$ in Ohm;
- die Kennlinie der Diode mit dem Sättigungssperrstrom $I_S$ und der Temperaturspannung $U_T$; Spannung $U$ und Strom $I$ zählen von der Anode zur Kathode.

**Das Zusammenspiel:** *Welches Paar aus Spannung und Strom erfüllt beide Bedingungen zugleich?*

:::formel Satz
$$I_S\,\Big(\exp\frac{U_\text{AP}}{U_T} - 1\Big) = \frac{U_{LL} - U_\text{AP}}{R_i}, \qquad I_\text{AP} = \frac{U_{LL} - U_\text{AP}}{R_i}.$$
:::

**So liest man das:** Links steht der Strom, den die Diode bei der Spannung $U_\text{AP}$ führt, rechts der, den das Netz bei dieser Spannung liefert. Die
Gleichung hat für jedes positive $R_i$ genau eine Lösung, weil die Kennlinie steigt und die Gerade fällt. Das Skript schreibt, je nach Kennlinie ergäben sich
ein oder mehrere Schnittpunkte, und gleich danach, der Arbeitspunkt sei eindeutig; für Dioden gilt das Zweite. Mehrere Schnittpunkte gibt es nur bei
Kennlinien, die stellenweise fallen, wie bei Tunneldioden; dazu verweist das Skript auf das Fach Grundlagen elektronischer Materialien und Bauelemente.
Eine Formel für $U_\text{AP}$ aus elementaren Funktionen gibt es nicht. Man liest den Schnittpunkt im Diagramm ab, wie in der Abbildung zu Abschnitt 10.4.3 des
Skripts, oder rechnet ihn numerisch aus.

**Im Bild:** Das Ventil lässt umso mehr durch, je größer der Druck ist; die Zuleitung liefert umso weniger, je größer der Gegendruck ist. Deshalb treffen sie
sich genau einmal.

:::herleitung
**Eine Funktion für den Unterschied.** Für jede Spannung $U$ sei $g(U)$ der Strom der Diode minus dem Strom, den das Netz liefert:

$$g(U) = I_S\,\Big(\exp\frac{U}{U_T} - 1\Big) - \frac{U_{LL} - U}{R_i}.$$

Ein Arbeitspunkt ist eine Nullstelle von $g$.

**Höchstens eine.** Der erste Teil wächst mit $U$, der zweite wird mit wachsendem $U$ kleiner und zählt mit Minus; also wächst $g$ streng. Eine streng wachsende
Funktion nimmt den Wert null höchstens einmal an.

**Mindestens eine.** Für sehr negatives $U$ ist der Diodenstrom fast $-I_S$, der Netzstrom aber groß und positiv, also $g$ negativ; für großes $U$ überwiegt die
Exponentialfunktion, und $g$ ist positiv. Weil $g$ stetig ist, hat es nach dem Zwischenwertsatz dazwischen eine Nullstelle. Im Bild: Eine steigende und eine
fallende Kurve, die links und rechts in verkehrter Reihenfolge liegen, müssen sich dazwischen genau einmal kreuzen.
:::

Numerisch löst man die Gleichung, indem man abwechselnd die Arbeitsgerade und die nach der Spannung umgestellte Kennlinie aus dem vorigen Artikel benutzt. Mit
einem Startwert $U^{(0)}$, etwa $0{,}6\,\text{V}$, und der Schrittnummer $k$:

$$U^{(k+1)} = U_T\,\ln\Big(1 + \frac{U_{LL} - U^{(k)}}{R_i\,I_S}\Big).$$

**So liest man das:** Aus der geschätzten Spannung folgt mit der Arbeitsgerade ein Strom, aus diesem mit der umgestellten Kennlinie eine bessere Spannung. Das
Verfahren konvergiert schnell, weil die Diodenspannung kaum vom Strom abhängt: Jeder Schritt verkleinert den Fehler etwa um den Faktor
$U_T/(I_\text{AP}R_i)$, bei üblichen Schaltungen ein Hundertstel oder weniger. Schaltungssimulatoren arbeiten nach einem verwandten Verfahren, dem
Newton-Verfahren, das in jedem Schritt die Kennlinie durch ihre Tangente ersetzt und ein lineares Gleichungssystem löst, wie im Artikel über das
Knotenpotentialverfahren angekündigt.

**Im Bild:** Man rät einen Druck am Ventil, fragt die Zuleitung, wie viel dann käme, und fragt das Ventil, welchen Druck dieser Durchfluss verlangt. Weil der
Druck am Ventil sich kaum mit dem Durchfluss ändert, stimmt schon die zweite Antwort fast.

:::herleitung
**Der Fixpunkt.** Erfüllt eine Spannung die Gleichung des Satzes, liefert die Vorschrift wieder dieselbe Spannung: Der Arbeitspunkt ist ihr Fixpunkt.

**Wie schnell der Fehler schrumpft.** Ändert man die Eingabe $U^{(k)}$ ein wenig, ändert sich zuerst der Strom um das $-1/R_i$-Fache, dann die Spannung um das
$U_T/(I + I_S)$-Fache davon, die Steigung der umgestellten Kennlinie:

$$\frac{dU^{(k+1)}}{dU^{(k)}} = -\frac{U_T}{(I + I_S)\,R_i}.$$

Nahe am Arbeitspunkt multipliziert jeder Schritt den Fehler also mit diesem Faktor; ist sein Betrag klein gegen eins, konvergiert das Verfahren rasch. Im Bild:
Die Antwort des Ventils hängt so schwach vom Durchfluss ab, dass ein falscher Durchfluss kaum einen falschen Druck ergibt.
:::

::::beispiel Eine Diode am Referenznetz
Statt $R_L$ hängt eine Siliziumdiode an den Klemmen, die Anode an A, die Kathode an B:

$$U_{LL} = 4\,\text{V}, \qquad R_i = 4\,\text{k}\Omega, \qquad I_S = 10^{-14}\,\text{A}, \qquad U_T = 25{,}85\,\text{mV}.$$

**Grafisch.** Die Arbeitsgerade von $(4\,\text{V}, 0)$ nach $(0, 1\,\text{mA})$ trifft die Kennlinie dort, wo sie steil wird, bei etwa $0{,}65\,\text{V}$ und
etwas über $0{,}8\,\text{mA}$.

**Numerisch.** Ab dem Startwert $0\,\text{V}$, der denkbar schlechtesten Schätzung:

| Schritt | Strom aus der Geraden | Spannung aus der Kennlinie |
|---|---|---|
| 1 | $1{,}0000\,\text{mA}$ | $0{,}65479\,\text{V}$ |
| 2 | $0{,}83630\,\text{mA}$ | $0{,}65017\,\text{V}$ |
| 3 | $0{,}83746\,\text{mA}$ | $0{,}65020\,\text{V}$ |
| 4 | $0{,}83745\,\text{mA}$ | $0{,}65020\,\text{V}$ |

Zum Beispiel der erste Schritt:

$$U^{(1)} = 0{,}02585\,\text{V}\cdot\ln\Big(1 + \frac{4\,\text{V}}{4\,\text{k}\Omega\cdot10^{-14}\,\text{A}}\Big) = 0{,}02585\,\text{V}\cdot25{,}33 = 0{,}6548\,\text{V}.$$

Nach drei Schritten steht der Arbeitspunkt auf fünf Stellen fest:

$$U_\text{AP} = 0{,}6502\,\text{V}, \qquad I_\text{AP} = 0{,}8374\,\text{mA}.$$

Der Faktor, um den jeder Schritt den Fehler verkleinert, ist hier

$$\frac{U_T}{I_\text{AP}\,R_i} = \frac{0{,}02585\,\text{V}}{0{,}8374\,\text{mA}\cdot4\,\text{k}\Omega} = 0{,}0077.$$

**Im Bild:** Man rät „kein Druck am Ventil“, bekommt den vollen Durchfluss von $1\,\text{mA}$, und das Ventil verlangt dafür $0{,}655$; der nächste Durchfluss ist
schon fast der richtige.
::::

:::grafik
Szene: get1/halbleiterbauelemente/03-arbeitsgerade · Vorlage: arbeitsgerade-kennlinie
Links das Referenznetz als graue Box mit den Klemmen A und B, daneben ihre Ersatzquelle mit $U_{LL} = 4\,\text{V}$ und $R_i = 4\,\text{k}\Omega$; an den Klemmen
wahlweise ein Widerstand $R_L = 4\,\text{k}\Omega$ oder eine Diode mit der Anode an A. Rechts das Diagramm mit $U$ nach rechts bis $4\,\text{V}$ und $I$ nach oben
bis $1\,\text{mA}$: die Arbeitsgerade von $(4\,\text{V}, 0)$ nach $(0, 1\,\text{mA})$, die Ursprungsgerade des Widerstands mit dem Schnittpunkt
$(2\,\text{V}, 0{,}5\,\text{mA})$ und die Diodenkennlinie mit dem Schnittpunkt $(0{,}650\,\text{V}, 0{,}837\,\text{mA})$. Ein Regler für $U_q$ von $6$ bis
$18\,\text{V}$ verschiebt die Arbeitsgerade parallel, ein Regler für $R_3$ dreht sie um den Leerlaufpunkt; die Arbeitspunkte gleiten mit. Ein Knopf
„iterieren“ zeichnet die Schritte des Verfahrens als Treppe zwischen Gerade und Kennlinie, die nach zwei Stufen im Schnittpunkt ankommt. Kernaussage: Der
Arbeitspunkt ist der Schnitt der Arbeitsgeraden mit der Kennlinie, und die Iteration findet ihn in wenigen Schritten. (Rot = Kennlinien, blau = Arbeitsgerade,
orange = Arbeitspunkte und Iterationstreppe, grau = Achsen und Netz.)
:::

## Lineare Ersatzschaltungen

Sind mehrere Dioden im Spiel, wird die grafische Lösung unhandlich. Für die Rechnung von Hand ersetzt man deshalb jede Diode durch lineare Bauteile, die ihre
Kennlinie stückweise durch Geraden annähern, eine __stückweise lineare Ersatzschaltung__. Das Skript zeigt in Abschnitt 10.5 zwei Stufen; eine dritte
kommt hier hinzu, jede genauer als die vorige:

- **Stufe 1: die ideale Diode.** Leitend ist sie ein Kurzschluss, sperrend eine Unterbrechung, wie in den Bildern 10.14 und 10.15 des Skripts. Die Kennlinie
  wird zur senkrechten Stromachse für positive Ströme und zur waagrechten Spannungsachse für negative Spannungen.
- **Stufe 2: mit Durchlassspannung.** Leitend ist sie eine Spannungsquelle $U_F$, im Skript $0{,}6\,\text{V}$, sperrend wieder eine Unterbrechung, wie in den
  Bildern 10.16 und 10.17. Das Skript nennt $U_F$ auch Fluss- oder Vorwärtsspannung.
- **Stufe 3: die Knickkennlinie.** Leitend kommt ein Widerstand $r_D$ in Reihe hinzu, und die Kennlinie steigt ab $U_F$ schräg an. So erfasst man die Krümmung
  in einem gewählten Strombereich und bei großen Strömen den Bahnwiderstand.

:::formel
$$I > 0 \;\Rightarrow\; U = U_F + r_D\,I, \qquad U < U_F \;\Rightarrow\; I = 0.$$
:::

**So liest man das:** Die beiden Bedingungen beschreiben alle drei Stufen: Stufe 2 ohne den Widerstand $r_D$, Stufe 1 zusätzlich ohne die Spannung $U_F$,
genau wie die Bedingungen im Skript. Eine leitende Diode wird durch eine Spannungsquelle ersetzt, in Stufe 3 mit Widerstand, eine sperrende durch eine Unterbrechung. Welcher Zustand
vorliegt, muss man annehmen und prüfen; darum geht der letzte Abschnitt. Die Werte der Stufe 3 wählt man so, dass die Gerade die echte Kennlinie bei einem
Strom $I_0$ berührt, in dessen Nähe man den Arbeitspunkt erwartet:

$$r_D = \frac{U_T}{I_0}, \qquad U_F = U(I_0) - r_D\,I_0.$$

**Im Bild:** Stufe 1 ist ein Ventil ohne Feder, Stufe 2 eines, dessen Feder beim Druck $U_F$ schlagartig ganz nachgibt, Stufe 3 eines mit Feder und einer
Engstelle dahinter.

:::herleitung
**Die Modelle sind Festlegungen.** Die Bedingungen folgen nicht aus der Physik, sondern legen ein vereinfachtes Bauteil fest; wie gut es die echte Kennlinie
trifft, zeigt das Beispiel.

**Die Tangente der Stufe 3.** Die nach der Spannung aufgelöste Kennlinie aus dem vorigen Artikel hat bei $I_0$ die Steigung $U_T/(I_0 + I_S)$, also fast
$U_T/I_0$. Die Tangente dort lautet

$$U \approx U(I_0) + \frac{U_T}{I_0}\,(I - I_0) = \Big(U(I_0) - \frac{U_T}{I_0}\,I_0\Big) + \frac{U_T}{I_0}\,I.$$

Die Klammer ist $U_F$, der Faktor vor $I$ ist $r_D$. Im Bild: Die Engstelle wird so gewählt, dass das Modellventil beim erwarteten Durchfluss so viel Druck
verlangt wie das echte und auf kleine Änderungen ebenso reagiert.
:::

::::beispiel Drei Modelle im Vergleich
Leitet die Diode, ersetzt man sie durch $U_F$ und $r_D$; mit der Ersatzquelle des übrigen Netzes ergibt die Maschenregel

$$I = \frac{U_{LL} - U_F}{R_i + r_D}.$$

Die Diode hat wieder den Sättigungsstrom $10^{-14}\,\text{A}$. Stufe 3 wird bei $1\,\text{mA}$ angelegt, also mit

$$I_0 = 1\,\text{mA}, \qquad r_D = 25{,}9\,\Omega, \qquad U_F = 0{,}629\,\text{V}.$$

**(a) Am Referenznetz,** $4\,\text{V}$ und $4\,\text{k}\Omega$, exakt $0{,}8374\,\text{mA}$:

| Modell | Strom | Fehler |
|---|---|---|
| Stufe 1 | $1{,}000\,\text{mA}$ | $+19\,\%$ |
| Stufe 2 mit $0{,}6\,\text{V}$ | $0{,}850\,\text{mA}$ | $+1{,}5\,\%$ |
| Stufe 2 mit $0{,}7\,\text{V}$ | $0{,}825\,\text{mA}$ | $-1{,}5\,\%$ |
| Stufe 3, angelegt bei $1\,\text{mA}$ | $0{,}8374\,\text{mA}$ | unter $0{,}01\,\%$ |

Zum Beispiel Stufe 2 mit $0{,}6\,\text{V}$:

$$I = \frac{4\,\text{V} - 0{,}6\,\text{V}}{4\,\text{k}\Omega} = 0{,}85\,\text{mA}.$$

**(b) An einer Batterie,** $1{,}5\,\text{V}$ mit $100\,\Omega$, exakt $0{,}708\,\text{V}$ und $7{,}92\,\text{mA}$:

| Modell | Strom | Fehler |
|---|---|---|
| Stufe 1 | $15{,}0\,\text{mA}$ | $+90\,\%$ |
| Stufe 2 mit $0{,}6\,\text{V}$ | $9{,}00\,\text{mA}$ | $+14\,\%$ |
| Stufe 2 mit $0{,}7\,\text{V}$ | $8{,}00\,\text{mA}$ | $+1\,\%$ |
| Stufe 3, angelegt bei $1\,\text{mA}$ | $6{,}92\,\text{mA}$ | $-13\,\%$ |
| Stufe 3, angelegt bei $8\,\text{mA}$ | $7{,}92\,\text{mA}$ | unter $0{,}01\,\%$ |

**Was daraus folgt.** Stufe 1 taugt nur, wenn die Spannungen im Netz groß gegen $0{,}6\,\text{V}$ sind. Stufe 2 ist robust, wenn $U_F$ zum Strombereich
passt. Stufe 3 ist sehr genau, aber nur nahe dem Strom, bei dem man sie angelegt hat; bei achtfachem Strom ist sie schlechter als Stufe 2.

**Im Bild:** Ein Modellventil mit der Engstelle für kleine Durchflüsse verlangt bei großem Durchfluss viel zu viel Druck; das echte Ventil öffnet dann weiter.
::::

:::grafik
Szene: get1/halbleiterbauelemente/03-ersatzschaltungen · Vorlage: stueckweise-linear
Ein Diagramm mit der echten Kennlinie der Diode, $I_S = 10^{-14}\,\text{A}$, von $0$ bis $0{,}8\,\text{V}$ und $0$ bis $15\,\text{mA}$. Drei Tasten blenden die Stufen
ein: Stufe 1 als senkrechte Linie auf der Stromachse, Stufe 2 als senkrechte Linie bei $U_F$ mit einem Regler von $0{,}5$ bis $0{,}8\,\text{V}$, Stufe 3 als
Tangente, deren Berührpunkt ein Regler für $I_0$ längs der Kennlinie verschiebt. Daneben jeweils das Ersatzschaltbild aus idealer Diode, Spannungsquelle
$U_F$ und Widerstand $r_D$. Zwei Arbeitsgeraden sind eingezeichnet, die des Referenznetzes und die der Batterie mit $1{,}5\,\text{V}$ und $100\,\Omega$; an ihren
Schnittpunkten mit Kennlinie und Modell stehen Strom und Fehler in Prozent. Kernaussage: Jede Stufe ersetzt die Kurve durch Geraden, und die Tangente der
Stufe 3 trifft nur in der Nähe ihres Berührpunkts. (Rot = echte Kennlinie, blau = Modelle, orange = Arbeitspunkte und Fehler, grau = Achsen.)
:::

## Der differentielle Widerstand

Die Steigung der Kennlinie im Arbeitspunkt bestimmt, wie die Diode auf kleine Änderungen antwortet. Sie heißt __differentieller Widerstand__, im Unterschied
zum Quotienten aus Spannung und Strom, der für eine Diode wenig aussagt:

:::formel
$$r_d = \frac{dU}{dI} = \frac{U_T}{I + I_S} \approx \frac{U_T}{I_\text{AP}}.$$
:::

**So liest man das:** Eingabe ist der Strom im Arbeitspunkt, Ausgabe ein Widerstand in Ohm. Er ist keine feste Eigenschaft der Diode, sondern hängt vom
Arbeitspunkt ab: bei $0{,}1\,\text{mA}$ sind es $259\,\Omega$, bei $1\,\text{mA}$ $25{,}9\,\Omega$, bei $10\,\text{mA}$ $2{,}6\,\Omega$. Ändern sich die
Spannungen im Netz nur wenig, verhält sich die Diode für diese Änderungen wie ein Widerstand $r_d$. Für die kleinen Änderungen, das __Kleinsignal__, ersetzt man
das Netz durch seine Ersatzquelle mit der Änderung $\Delta U_{LL}$ und die Diode durch $r_d$:

$$\Delta I = \frac{\Delta U_{LL}}{R_i + r_d}, \qquad \Delta U = r_d\,\Delta I.$$

Mit diesem Gedanken berechnet man später Transistorverstärker. Die Z-Diode im vorigen Artikel hatte mit $r_Z$ denselben Kennwert im Durchbruch. Bei großen
Strömen kommt zu $r_d$ noch der Bahnwiderstand hinzu.

**Im Bild:** Wie stark der Druck am Ventil steigt, wenn etwas mehr Wasser kommt. Bei großem Durchfluss steht es weit offen und gibt fast ohne Druckanstieg nach.

:::herleitung
**Ableiten.** Die nach der Spannung aufgelöste Kennlinie ist $U = U_T\ln(1 + I/I_S)$; nach der Kettenregel ist ihre Ableitung

$$\frac{dU}{dI} = \frac{U_T}{I_S}\cdot\frac{1}{1 + I/I_S} = \frac{U_T}{I + I_S}.$$

Weil $I_S$ winzig gegen jeden Durchlassstrom ist, bleibt $U_T/I_\text{AP}$.

**Die kleinen Änderungen.** Nahe am Arbeitspunkt ersetzt man die Kennlinie durch ihre Tangente; dann hängen die Änderungen von Spannung und Strom über $r_d$
zusammen wie an einem Widerstand. Das übrige Netz ist linear, also gilt für die Änderungen die Maschenregel mit $\Delta U_{LL}$ und $R_i$:

$$\Delta U_{LL} = R_i\,\Delta I + r_d\,\Delta I.$$

Im Bild: Für einen kleinen Zusatzdruck am Turm zählt nur, wie nachgiebig Zuleitung und Ventil gerade sind.
:::

::::beispiel Kleine Änderung am Referenznetz
Die Diode am Referenznetz, im Arbeitspunkt $0{,}6502\,\text{V}$ und $0{,}8374\,\text{mA}$. Ihr differentieller Widerstand:

$$r_d = \frac{25{,}85\,\text{mV}}{0{,}8374\,\text{mA}} = 30{,}9\,\Omega.$$

**Die Quelle steigt** von $12$ auf $12{,}3\,\text{V}$. Die Leerlaufspannung ist ein Drittel davon, also wächst sie um

$$\Delta U_{LL} = \frac{0{,}3\,\text{V}}{3} = 0{,}1\,\text{V}.$$

**Kleinsignal.**

$$\Delta I = \frac{0{,}1\,\text{V}}{4000\,\Omega + 30{,}9\,\Omega} = 24{,}81\,\mu\text{A}, \qquad \Delta U = 30{,}9\,\Omega\cdot24{,}81\,\mu\text{A} = 0{,}77\,\text{mV}.$$

**Zum Vergleich exakt.** Der neue Arbeitspunkt, mit der Iteration berechnet, liegt um $24{,}81\,\mu\text{A}$ und $0{,}755\,\text{mV}$ höher; das Kleinsignalmodell
trifft den Strom genau und die Spannung auf eineinhalb Prozent.

**Was es zeigt.** Hundert Millivolt mehr an der Quelle ändern die Diodenspannung um weniger als ein Millivolt; eine Diode mit Vorwiderstand liefert eine recht
feste Spannung, eine einfache Spannungsreferenz.

**Im Bild:** Ein etwas höherer Turm schiebt etwas mehr Wasser durch; das weit geöffnete Ventil verlangt dafür kaum mehr Druck.
::::

## Schaltungen mit mehreren Dioden

Das Skript gibt für Schaltungen mit Dioden ein Verfahren in vier Schritten an:

1. Für jede Diode wählt man eine Ersatzschaltung, meist die der Stufe 2.
2. Man nimmt möglichst plausibel an, welche Diode leitet und welche sperrt.
3. Man ersetzt die Dioden durch ihre Ersatzschaltungen und berechnet die nun lineare Schaltung.
4. Man prüft die Annahmen an den Ergebnissen.

Geprüft wird jede Diode gegen ihr Modell:

- Eine als leitend angenommene Diode muss einen positiven Strom führen; ein negativer Strom widerspricht der Annahme.
- Eine als sperrend angenommene Diode darf höchstens die Durchlassspannung sehen; liegt mehr an ihr, würde sie leiten.

Bei einem Widerspruch ändert man die Annahme. Mit $n$ Dioden gibt es $2^n$ Kombinationen; gut geraten spart Arbeit. Die __Potenzialbetrachtung__ des Skripts
schließt viele Kombinationen ohne Rechnung aus: Man fragt, welche Potenziale eine Annahme erzwingt, und liest die Spannungen an den übrigen Dioden ab.

Findet man eine widerspruchsfreie Kombination, braucht man nicht weiterzusuchen: Mit den echten, streng steigenden Kennlinien hat ein Netz aus Quellen,
positiven Widerständen und Dioden genau einen Zustand, und das Modell gibt ihn näherungsweise wieder.

**Im Bild:** Bei mehreren Ventilen rät man, welche offen stehen. Ein offenes Ventil, durch das das Wasser rückwärts fließen müsste, ist falsch geraten, ebenso
ein geschlossenes, an dem mehr als der Öffnungsdruck steht.

:::herleitung
**Beweisidee für die Eindeutigkeit.** Angenommen, ein Netz hätte zwei Zustände. Die Unterschiede ihrer Zweigspannungen und Zweigströme erfüllen ebenfalls die
Knoten- und die Maschenregel, weil beide Regeln linear sind. Nach dem Satz von Tellegen aus dem Artikel über Zweitore ist dann die Summe der Produkte aus
Spannungs- und Stromunterschied über alle Zweige null:

$$\sum_j \Delta U_j\,\Delta I_j = 0.$$

**Jeder Summand ist mindestens null.** Bei einer Spannungsquelle ist der Spannungsunterschied null, bei einer Stromquelle der Stromunterschied. Bei einem
Widerstand ist der Summand $R\,\Delta I^2$, bei einer Diode mit streng steigender Kennlinie haben Spannungs- und Stromunterschied dasselbe Vorzeichen. Eine
Summe aus Gliedern, die nicht negativ sind, ist nur null, wenn jedes null ist; also sind alle Ströme in Widerständen und alle Diodengrößen in beiden Zuständen
gleich. Im Bild: Zwei verschiedene Gleichgewichte würden sich in jedem Rohr und jedem Ventil gegenseitig überbieten, und das geht nicht auf.
:::

::::beispiel Eine Diodenweiche
Zwei Quellen versorgen über je eine Diode einen gemeinsamen Verbraucher, etwa ein Netzteil und eine Batterie; die Anoden zeigen zu den Quellen, die Kathoden
zum gemeinsamen Knoten A. Jede Quelle hat einen Innenwiderstand, der Verbraucher liegt von A nach Masse:

$$U_1 = 5\,\text{V}, \qquad U_2 = 2\,\text{V}, \qquad R_1 = R_2 = 1\,\text{k}\Omega, \qquad R_L = 10\,\text{k}\Omega, \qquad U_F = 0{,}6\,\text{V}.$$

**Annahme 1: beide leiten.** Dann ersetzt man beide durch $0{,}6\,\text{V}$. Die Knotenregel an A, mit $U_A$ als Spannung von A nach Masse:

$$\frac{5\,\text{V} - 0{,}6\,\text{V} - U_A}{1\,\text{k}\Omega} + \frac{2\,\text{V} - 0{,}6\,\text{V} - U_A}{1\,\text{k}\Omega} = \frac{U_A}{10\,\text{k}\Omega}, \qquad U_A = 2{,}762\,\text{V}.$$

Daraus die Diodenströme:

$$I_{D1} = \frac{4{,}4\,\text{V} - 2{,}762\,\text{V}}{1\,\text{k}\Omega} = 1{,}638\,\text{mA}, \qquad I_{D2} = \frac{1{,}4\,\text{V} - 2{,}762\,\text{V}}{1\,\text{k}\Omega} = -1{,}362\,\text{mA}.$$

$D_2$ müsste rückwärts leiten: Widerspruch.

**Annahme 2: $D_1$ leitet, $D_2$ sperrt.** Jetzt fließt durch $R_2$ nichts, und $U_1 - U_F$ teilt sich auf $R_1$ und $R_L$ auf:

$$U_A = 4{,}4\,\text{V}\cdot\frac{10\,\text{k}\Omega}{11\,\text{k}\Omega} = 4{,}0\,\text{V}, \qquad I_{D1} = \frac{4{,}4\,\text{V} - 4{,}0\,\text{V}}{1\,\text{k}\Omega} = 0{,}4\,\text{mA}.$$

**Probe.** $I_{D1}$ ist positiv. An $D_2$ liegt von der Anode, auf $2\,\text{V}$, zur Kathode, auf $4{,}0\,\text{V}$:

$$U_{D2} = 2\,\text{V} - 4{,}0\,\text{V} = -2{,}0\,\text{V},$$

weniger als $0{,}6\,\text{V}$, sie sperrt also wirklich. Die Arbeitspunkte sind $(0{,}6\,\text{V}, 0{,}4\,\text{mA})$ für $D_1$ und $(-2{,}0\,\text{V}, 0)$ für
$D_2$: Die höhere Quelle versorgt den Verbraucher, die niedrigere ist abgekoppelt und wird nicht rückwärts geladen.

**Im Bild:** Zwei Türme speisen über Rückschlagventile ein gemeinsames Becken. Der höhere drückt das Ventil des niedrigeren zu, und nur er liefert.
::::

Ohne Rechnung hätte die Potenzialbetrachtung genügt: Leitet $D_1$, liegt A bei etwa $4\,\text{V}$, und $D_2$ mit $2\,\text{V}$ an der Anode kann nicht leiten. Die
beiden Rechenbeispiele des Skripts sind richtig gerechnet; die Spannung $-1{,}3\,\text{V}$ im ersten ist auf $-1{,}27\,\text{V}$ gerundet. Bild 10.22 trägt aber
die Unterschrift „Rechenbeispiel 2“ und zeigt die Schaltung des ersten, mit $14\,\text{V}$ statt $15\,\text{V}$; der Text dazu gehört ebenfalls zum ersten
Beispiel. In Gleichung 10.5 steht $I_{R1}$ statt $I_{D1}$, und der Verweis auf „Abbildung 10.14b(l)“ führt ins Leere: Die Diodenschaltung zu Abschnitt 10.4.3 hat
keine Nummer, Bild 10.14 ist die Kennlinie der idealen Diode.

::::beispiel Ein Spannungsbegrenzer
Eine Eingangsspannung $U_E$ speist über $R = 1\,\text{k}\Omega$ den Knoten A. Von A führen zwei Dioden gegeneinander nach Masse: $D_1$ mit der Anode an A, $D_2$
mit der Anode an Masse. Ausgang ist die Spannung $U_A$ von A nach Masse; $U_F = 0{,}6\,\text{V}$.

**Potenzialbetrachtung.** Von den vier Kombinationen fällt eine sofort weg: Leiten beide, müsste A zugleich auf $+0{,}6\,\text{V}$ und auf $-0{,}6\,\text{V}$ liegen.
Leitet $D_1$, liegt A auf $+0{,}6\,\text{V}$, und an $D_2$ liegen $-0{,}6\,\text{V}$, sie sperrt; ebenso umgekehrt.

**(a) $U_E = 5\,\text{V}$.** $D_1$ leitet:

$$U_A = 0{,}6\,\text{V}, \qquad I_{D1} = \frac{5\,\text{V} - 0{,}6\,\text{V}}{1\,\text{k}\Omega} = 4{,}4\,\text{mA}.$$

Der Strom ist positiv, die Annahme hält.

**(b) $U_E = 0{,}3\,\text{V}$.** Beide sperren; ohne Strom ist $U_A$ gleich $U_E$, und an $D_1$ liegen $0{,}3\,\text{V}$, an $D_2$ $-0{,}3\,\text{V}$, beides
unter $0{,}6\,\text{V}$.

**(c) $U_E = -5\,\text{V}$.** $D_2$ leitet, $U_A$ ist $-0{,}6\,\text{V}$, und $4{,}4\,\text{mA}$ fließen von Masse durch $D_2$ und $R$ zur Quelle.

**Die Übertragungskennlinie.** Zwischen $-0{,}6$ und $+0{,}6\,\text{V}$ folgt der Ausgang dem Eingang, darüber und darunter bleibt er bei $\pm0{,}6\,\text{V}$. So
schützt man empfindliche Eingänge vor zu großen Spannungen.

**Im Bild:** Zwei Überdruckventile gegeneinander: Steigt oder fällt der Druck zu weit, öffnet eines und hält ihn bei seinem Öffnungsdruck.
::::

:::grafik
Szene: get1/halbleiterbauelemente/03-mehrere-dioden · Vorlage: annahmen-pruefen
Links die Diodenweiche: Quelle $5\,\text{V}$ mit $1\,\text{k}\Omega$ und $D_1$, Quelle $2\,\text{V}$ mit $1\,\text{k}\Omega$ und $D_2$, beide Kathoden am Knoten A, von
dort $R_L = 10\,\text{k}\Omega$ nach Masse. Zwei Schalter legen für jede Diode die Annahme fest, „leitet“ oder „sperrt“; die Diode wird dann durch eine
Spannungsquelle von $0{,}6\,\text{V}$ oder eine Unterbrechung ersetzt, $U_A$ und die Diodengrößen erscheinen als Zahlen, und neben jeder Diode zeigt ein grüner
Haken oder ein rotes Kreuz, ob die Probe besteht. Nur die Kombination „$D_1$ leitet, $D_2$ sperrt“ wird ganz grün. Rechts der Begrenzer mit $R = 1\,\text{k}\Omega$
und den beiden gegeneinander geschalteten Dioden; ein Regler für $U_E$ von $-5$ bis $+5\,\text{V}$ bewegt einen Punkt auf der Übertragungskennlinie, die bei
$\pm0{,}6\,\text{V}$ abknickt, und die leitende Diode leuchtet. Kernaussage: Annehmen, ersetzen, rechnen, prüfen; nur eine Kombination ist widerspruchsfrei.
(Rot = Dioden und ihr Zustand, blau = Spannungen und Kennlinie, orange = Prüfergebnis, grau = Schaltung.)
:::

## Bedeutung und Ausblick

Die drei Wege gelten für jedes nichtlineare Bauteil: grafisch für ein einzelnes, numerisch für viele, stückweise linear für die Rechnung von Hand. Dazu kommt
das Kleinsignal: Um einen Arbeitspunkt herum verhält sich ein gekrümmtes Bauteil wie ein Widerstand, und für kleine Änderungen wird die ganze Schaltung
linear. Auf diesem Gedanken beruht die Berechnung von Verstärkern; beim Transistor im nächsten Kapitel ist der Eingang ein pn-Übergang wie die Diode, mit
einem differentiellen Widerstand derselben Form.

Der nächste Artikel wendet das Modell der Stufe 2 auf die wichtigsten Diodenschaltungen des Skripts an, die Gleichrichter und die Ladungspumpe.

:::kern
- Der Arbeitspunkt ist das Paar aus Spannung und Strom, das sich in der Schaltung auf der Kennlinie einstellt.
- Das übrige lineare Netz ist eine Ersatzquelle; seine Arbeitsgerade ist $I=(U_{LL}-U)/R_i$, durch Leerlauf- und Kurzschlusspunkt.
- Der Arbeitspunkt ist der Schnitt von Arbeitsgerade und Kennlinie; bei Dioden gibt es genau einen.
- Numerisch wechselt man zwischen Gerade und umgestellter Kennlinie; jeder Schritt verkleinert den Fehler um den Faktor $U_T/(I\,R_i)$.
- Ersatzschaltungen: ideale Diode, mit Durchlassspannung $U_F$, mit zusätzlichem $r_D$ als Tangente.
- Die Knickkennlinie ist nur nahe ihrem Berührpunkt genauer als Stufe 2.
- Differentieller Widerstand: $r_d=U_T/I_\text{AP}$; für kleine Änderungen wirkt die Diode wie dieser Widerstand.
- Mehrere Dioden: annehmen, ersetzen, rechnen, prüfen; leitend heißt positiver Strom, sperrend weniger als $U_F$.
- Eine widerspruchsfreie Annahme ist die Lösung; die Potenzialbetrachtung schließt Kombinationen ohne Rechnung aus.
:::

:::quiz
F: Was ist ein Arbeitspunkt, und was unterscheidet Arbeitspunktanalyse und -synthese?
A: Der Arbeitspunkt ist das Paar aus Spannung und Strom auf der Kennlinie, das sich in der Schaltung einstellt. Die Analyse bestimmt ihn für eine gegebene Schaltung, die Synthese bemisst die Bauteile so, dass sich ein gewünschter Arbeitspunkt einstellt.
F: Woher kommt die Arbeitsgerade, und wie zeichnet man sie?
A: Das übrige lineare Netz ist eine Ersatzquelle mit $U_{LL}$ und $R_i$; die Maschenregel ergibt $I=(U_{LL}-U)/R_i$. Man zeichnet sie durch den Leerlaufpunkt $(U_{LL},0)$ und den Kurzschlusspunkt $(0,I_{KS})$; beim Referenznetz von $(4\,\text{V},0)$ nach $(0,1\,\text{mA})$, und ein Widerstand von $4\,\text{k}\Omega$ schneidet sie bei $2\,\text{V}$ und $0{,}5\,\text{mA}$.
F: Warum hat eine Diode an einem linearen Netz genau einen Arbeitspunkt?
A: Der Unterschied aus Diodenstrom und Netzstrom wächst streng mit der Spannung, ist für sehr negative Spannungen negativ und für große positiv; nach dem Zwischenwertsatz hat er genau eine Nullstelle. Mehrere Schnittpunkte gibt es nur bei Kennlinien, die stellenweise fallen.
F: Wie findet man den Arbeitspunkt numerisch, und warum geht das so schnell?
A: Man rechnet abwechselnd mit der Arbeitsgeraden den Strom und mit der umgestellten Kennlinie die Spannung. Jeder Schritt verkleinert den Fehler um den Faktor $U_T/(I\,R_i)$, am Referenznetz $0{,}0077$; nach drei Schritten steht $(0{,}6502\,\text{V}, 0{,}8374\,\text{mA})$ auf fünf Stellen fest.
F: Welche drei Ersatzschaltungen der Diode gibt es?
A: Stufe 1, die ideale Diode: leitend ein Kurzschluss, sperrend eine Unterbrechung. Stufe 2: leitend eine Spannungsquelle $U_F$, im Skript $0{,}6\,\text{V}$. Stufe 3: zusätzlich ein Widerstand $r_D$, als Tangente an die Kennlinie bei einem erwarteten Strom $I_0$ mit $r_D=U_T/I_0$.
F: Wann taugt welche Stufe?
A: Stufe 1 nur bei Spannungen groß gegen $0{,}6\,\text{V}$: am Referenznetz $+19\,\%$, an einer $1{,}5$-V-Batterie mit $100\,\Omega$ $+90\,\%$. Stufe 2 ist robust, mit passendem $U_F$ um ein Prozent genau. Stufe 3 ist nahe ihrem Berührpunkt fast exakt, bei achtfachem Strom aber mit $-13\,\%$ schlechter als Stufe 2.
F: Was ist der differentielle Widerstand, und wofür braucht man ihn?
A: Die Steigung der Kennlinie im Arbeitspunkt, $r_d=U_T/I_\text{AP}$, bei $0{,}84\,\text{mA}$ also $30{,}9\,\Omega$. Für kleine Änderungen wirkt die Diode wie dieser Widerstand: $0{,}1\,\text{V}$ mehr Leerlaufspannung am Referenznetz ergeben $24{,}8\,\mu\text{A}$ mehr Strom und nur $0{,}77\,\text{mV}$ mehr Diodenspannung.
F: Wie berechnet man eine Schaltung mit mehreren Dioden?
A: Man wählt Ersatzschaltungen, nimmt für jede Diode an, ob sie leitet oder sperrt, ersetzt sie und rechnet linear. Dann prüft man: Leitende Dioden brauchen einen positiven Strom, sperrende dürfen höchstens $U_F$ sehen; bei einem Widerspruch ändert man die Annahme. Bei $n$ Dioden gibt es $2^n$ Kombinationen.
F: Was zeigt die Diodenweiche, und warum muss man nach einer widerspruchsfreien Lösung nicht weitersuchen?
A: Die Annahme, beide Dioden leiten, ergibt für $D_2$ einen negativen Strom von $-1{,}36\,\text{mA}$; mit $D_2$ gesperrt liegt A auf $4{,}0\,\text{V}$, $D_1$ führt $0{,}4\,\text{mA}$, und an $D_2$ liegen $-2{,}0\,\text{V}$. Nach dem Satz von Tellegen hat ein Netz aus Quellen, positiven Widerständen und Dioden mit steigenden Kennlinien nur einen Zustand.
F: Was leistet die Potenzialbetrachtung am Begrenzer, und welche Unstimmigkeiten hat das Skript in diesem Abschnitt?
A: Am Begrenzer schließt sie ohne Rechnung aus, dass beide Dioden leiten, weil A nicht zugleich auf $+0{,}6$ und $-0{,}6\,\text{V}$ liegen kann; der Ausgang bleibt zwischen $\pm0{,}6\,\text{V}$. Im Skript trägt Bild 10.13 eine kopierte Unterschrift, der Verweis auf Abbildung 10.14b(l) führt ins Leere, Gleichung 10.5 schreibt $I_{R1}$ statt $I_{D1}$, und Bild 10.22 gehört zum ersten statt zum zweiten Rechenbeispiel, mit $14$ statt $15\,\text{V}$.
:::
