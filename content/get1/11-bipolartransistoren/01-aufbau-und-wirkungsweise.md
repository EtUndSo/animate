---
title: Der Bipolartransistor – Aufbau und Wirkungsweise
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Bipolartransistoren
order: 110100
summary: Von Grund auf – wie aus drei dotierten Schichten ein Bauteil wird, in dem ein kleiner Basisstrom einen großen Kollektorstrom begleitet und steuert. Leitbild sind drei Parkhäuser in einer Reihe, mit einer Rampe vom Emitter in die schmale Basis und einer Absturzkante zum Kollektor. Mit Aufbau, Schaltsymbol und Zählpfeilen, dem Transistoreffekt und der Transfergleichung, Stromverstärkung B und α samt Herkunft aus Rekombination und Rückinjektion, der Frage nach Strom- oder Spannungssteuerung, den Kennlinien, den drei Arbeitsbereichen mit Annahme und Probe, dem Transistor als Schalter und dem pnp-Transistor. Mit Beispiel-Seite.
tags: Bipolartransistor, npn, pnp, Transistoreffekt, Stromverstärkung, aktiver Bereich, Sättigung
---

## Anschaulich

Mit der Diode kann man Strom nur durchlassen oder sperren. Der __Bipolartransistor__ kann mehr: Ein kleiner Strom an einem seiner Anschlüsse geht mit einem
viel größeren Strom an einem anderen einher und steuert ihn. Damit verstärkt man Signale und schaltet Lasten, und aus Milliarden solcher Schalter bestehen
Rechner. Der Name kommt daher, dass beide Sorten von Ladungsträgern beteiligt sind, Elektronen und Löcher.

**Das Leitbild dieses Artikels:** **drei Parkhäuser in einer Reihe.** Es ist das Parkhaus aus den Artikeln über Halbleiter und die Diode, jetzt dreimal
nebeneinander. Links steht das Emitter-Parkhaus, auf dem Oberdeck dicht voller Autos. In der Mitte steht ein sehr schmales Basis-Parkhaus mit wenigen Lücken
im Unterdeck. Rechts liegt das Kollektor-Parkhaus tief unten. Zwischen Emitter und Basis führt eine Rampe hinauf, deren Höhe die Spannung zwischen Basis und
Emitter verstellt; zwischen Basis und Kollektor geht es an einer Kante steil hinab.

Vier Folgerungen:

- **Wer die Rampe schafft, stürzt fast sicher hinab.** Senkt man die Rampe, fahren viele Autos ins Basis-Parkhaus. Weil es so schmal ist, rollen fast alle bis
  zur Kante und stürzen ins Kollektor-Parkhaus, bevor sie eine Lücke finden.
- **Nur wenige bleiben hängen.** Die wenigen Autos, die in der Basis in eine Lücke fallen, und die wenigen Lücken, die zum Emitter hinüberwandern, müssen über
  den Basisanschluss ersetzt werden. Das ist ein kleiner Basisstrom neben einem großen Kollektorstrom.
- **Die Tiefe des Absturzes ist gleichgültig.** Wie tief das Kollektor-Parkhaus liegt, ändert nichts daran, wie viele Autos ankommen; das bestimmt allein die
  Rampe. Der Transistor liefert deshalb einen Strom, der fast nicht von der Kollektorspannung abhängt.
- **Ohne Kante kein Strom.** Hebt man das Kollektor-Parkhaus zu weit an, verschwindet die Kante, und Autos rollen zurück; der Strom wird von außen begrenzt. Das
  ist die Sättigung. Ist die Rampe zu hoch, kommt niemand hinüber: Der Transistor sperrt.

| Im Parkhaus | Im Transistor |
|---|---|
| Emitter-Parkhaus, oben dicht voll | stark n-dotierter Emitter |
| schmales Basis-Parkhaus mit wenigen Lücken | dünne, p-dotierte Basis |
| tief liegendes Kollektor-Parkhaus | n-dotierter Kollektor |
| Rampe vom Emitter in die Basis | Basis-Emitter-Übergang, verstellt durch $U_{BE}$ |
| steile Kante zum Kollektor | gesperrter Basis-Kollektor-Übergang |
| Autos, die durch die Basis rollen und hinabstürzen | Kollektorstrom |
| Autos, die in der Basis in Lücken fallen | Rekombination, ein Teil des Basisstroms |
| Lücken, die ins Emitter-Parkhaus wandern | Rückinjektion, der andere Teil |

:::grafik
Szene: get1/bipolartransistoren/01-drei-parkhaeuser · Vorlage: transistor-parkhaeuser
Drei Parkhäuser im Querschnitt nebeneinander: links das Emitter-Parkhaus mit dicht besetztem Oberdeck, in der Mitte ein schmales Basis-Parkhaus mit wenigen
Lücken im Unterdeck, rechts das tief liegende Kollektor-Parkhaus. Zwischen Emitter und Basis eine Rampe, deren Höhe ein Regler für $U_{BE}$ von $0$ bis
$0{,}75\,\text{V}$ verstellt; zwischen Basis und Kollektor eine Kante, deren Tiefe ein Regler für $U_{CB}$ verstellt. Autos fahren je nach Rampenhöhe über die
Rampe, rollen durch die Basis und stürzen über die Kante; einzelne fallen unterwegs in eine Lücke und werden rot markiert, einzelne Lücken wandern nach links.
Zähler zeigen den Kollektor- und den Basisstrom und ihr Verhältnis $B$. Wird $U_{CB}$ negativ, verschwindet die Kante, Autos rollen zurück, und der Zähler des
Kollektorstroms fällt. Kernaussage: Die Rampe bestimmt, wie viele Autos kommen, fast alle erreichen den Kollektor, und nur wenige bilden den Basisstrom.
(Blau = Elektronen als Autos, rot = Rekombination und Lücken, orange = Rampe und Kante, grau = Parkhäuser.)
:::

## Aufbau, Schaltsymbol und Zählpfeile

Ein Bipolartransistor besteht nach Abschnitt 11.1 des Skripts aus drei unterschiedlich dotierten Bereichen desselben Grundmaterials: dem __Emitter__ (E), der
__Basis__ (B) und dem __Kollektor__ (C). Der Emitter ist am stärksten dotiert, der Kollektor am schwächsten, und die Basis dazwischen ist sehr viel schmaler als
die beiden anderen. Beim __npn-Transistor__ ist die Basis p-dotiert zwischen zwei n-Gebieten, beim __pnp-Transistor__ n-dotiert zwischen zwei p-Gebieten; der
npn-Transistor ist in der Praxis weit häufiger. Der Transistor enthält damit zwei pn-Übergänge, den __Basis-Emitter-Übergang__ und den
__Basis-Kollektor-Übergang__.

Im __Schaltsymbol__ in Bild 11.1 trägt der Emitter einen Pfeil, beim npn-Transistor nach außen, in die Richtung, in die der Emitterstrom fließt. Gezählt wird wie
im Skript: Basisstrom $I_B$ und Kollektorstrom $I_C$ fließen in den Transistor hinein, der Emitterstrom $I_E$ heraus. Die Spannungen $U_{BE}$, $U_{CB}$ und
$U_{CE}$ zählen jeweils vom ersten zum zweiten genannten Anschluss. Für diese Größen gelten, wie das Skript festhält, eine Knoten- und eine Maschenregel:

:::formel
$$I_E = I_B + I_C, \qquad U_{CE} = U_{CB} + U_{BE}.$$
:::

**So liest man das:** Der Emitterstrom ist die Summe der beiden anderen, weil der Transistor keine Ladung speichert. Die Spannung von Kollektor zu Emitter ist der
Weg über die Basis. Damit sind von den drei Strömen und drei Spannungen jeweils nur zwei unabhängig.

**Im Bild:** Was aus dem Emitter-Parkhaus verschwindet, kommt im Kollektor oder an der Basis wieder heraus, und der Höhenunterschied von Kollektor zu Emitter ist
der über die Basis.

:::herleitung
**Knotenregel.** Man legt eine Hülle um den ganzen Transistor. Im Gleichgewicht sammelt sich darin keine Ladung, also fließt ebenso viel hinein wie heraus, wie
im Artikel über die Kirchhoffschen Gesetze für einen Knoten. Mit den Zählpfeilen fließen $I_B$ und $I_C$ hinein und $I_E$ heraus.

**Maschenregel.** Die drei Anschlüsse bilden eine Masche; nach dem Artikel über Arbeit, Potenzial und Spannung ist jede Spannung eine Potenzialdifferenz:

$$U_{CE} = \varphi_C - \varphi_E = (\varphi_C - \varphi_B) + (\varphi_B - \varphi_E) = U_{CB} + U_{BE}.$$

Im Bild: Der Höhenunterschied zweier Parkhäuser ist derselbe, ob man ihn direkt misst oder über das mittlere.
:::

## Der Transistoreffekt

Im Normalbetrieb, dem __aktiven Bereich__, liegt der Basis-Emitter-Übergang in Durchlassrichtung, mit $U_{BE}$ um $0{,}6$ bis $0{,}7\,\text{V}$, und der
Basis-Kollektor-Übergang in Sperrrichtung, der Kollektor positiv gegen die Basis. Das zeigen die beiden Quellen in Bild 11.1 des Skripts.

Wie bei der Diode lässt die Durchlassspannung viele Elektronen aus dem stark dotierten Emitter in die Basis gelangen. In der p-dotierten Basis sind sie
Minoritätsträger und wandern durch Diffusion weiter. Ein Minoritätsträger legt im Mittel eine bestimmte Strecke zurück, bevor er rekombiniert, die
__Diffusionslänge__; in Silizium sind das Mikrometer bis Millimeter. Die Basis ist viel dünner, deshalb erreichen fast alle Elektronen ihren Rand zum Kollektor,
wie das Skript sagt. Dort fasst sie das Feld des gesperrten Basis-Kollektor-Übergangs und zieht sie in den Kollektor. Dieser Strom heißt auch __Transferstrom__.
Weil er von den Elektronen getragen wird, die der Basis-Emitter-Übergang durchlässt, hängt er wie der Diodenstrom exponentiell von $U_{BE}$ ab:

:::formel Gesetz
$$I_C = I_S\,\exp\frac{U_{BE}}{U_T}.$$
:::

**So liest man das:** Eingabe ist die Basis-Emitter-Spannung, Ausgabe der Kollektorstrom. $I_S$ ist der __Transfersättigungsstrom__ des Transistors, wie bei der
Diode proportional zur Fläche und zu $n_i^2$, und $U_T$ die Temperaturspannung, bei $300\,\text{K}$ gleich $25{,}9\,\text{mV}$. Die Kollektorspannung kommt
in der Gleichung nicht vor: Solange der Basis-Kollektor-Übergang sperrt, sammelt er jedes Elektron ein, das ihn erreicht. Der Kollektor verhält sich deshalb wie
eine Stromquelle, die $U_{BE}$ steuert. Die Gleichung heißt __Transfergleichung__; das Skript nennt sie nicht, sie folgt aber aus der Diodengleichung.

**Im Bild:** Wie viele Autos ins Kollektor-Parkhaus stürzen, entscheidet allein die Höhe der Rampe vom Emitter, nicht die Tiefe des Absturzes.

:::herleitung
**Der Elektronenstrom über den Basis-Emitter-Übergang.** Nach dem Artikel über die Diode wächst der Strom über die Rampe eines pn-Übergangs mit
$\exp(U/U_T)$, wobei die angelegte Spannung die Rampe absenkt. Am Basis-Emitter-Übergang ist das $U_{BE}$; die Elektronen, die der Emitter liefert, wachsen also
mit $\exp(U_{BE}/U_T)$.

**Kein Rückstrom.** Bei der Diode floss der Rückstrom von Minoritätsträgern, die von der anderen Seite herunterrollten. Hier gibt es auf der Kollektorseite der
Basis praktisch keine Elektronen, denn das Feld des gesperrten Übergangs räumt sie sofort ab. Der Rückstrom fehlt deshalb; streng genommen steht $\exp - 1$, und
die Eins ist bei Durchlassspannungen unwichtig.

**Fast alle kommen an.** Weil die Basis viel dünner als die Diffusionslänge ist, erreicht fast jedes Elektron den Kollektor. Der Kollektorstrom ist deshalb bis
auf einen winzigen Bruchteil dieser Elektronenstrom, und die Konstante davor heißt $I_S$. Im Bild: Die Rampe zählt die Autos, die Basis ist zu schmal, um viele zu
verlieren, und die Kante nimmt alle.
:::

::::beispiel Der Kollektorstrom und die Basis-Emitter-Spannung
Ein kleiner Siliziumtransistor mit

$$I_S = 10^{-14}\,\text{A}, \qquad U_T = 25{,}85\,\text{mV}, \qquad B = 200.$$

Der Basisstrom ist, wie der nächste Abschnitt zeigt, ein Zweihundertstel des Kollektorstroms.

**Drei Spannungen.**

| $U_{BE}$ | $I_C$ | $I_B$ |
|---|---|---|
| $0{,}60\,\text{V}$ | $0{,}12\,\text{mA}$ | $0{,}60\,\mu\text{A}$ |
| $0{,}65\,\text{V}$ | $0{,}83\,\text{mA}$ | $4{,}15\,\mu\text{A}$ |
| $0{,}70\,\text{V}$ | $5{,}75\,\text{mA}$ | $28{,}7\,\mu\text{A}$ |

Zum Beispiel bei $0{,}65\,\text{V}$:

$$I_C = 10^{-14}\,\text{A}\cdot\exp\frac{0{,}65\,\text{V}}{0{,}02585\,\text{V}} = 10^{-14}\,\text{A}\cdot8{,}3\cdot10^{10} = 0{,}83\,\text{mA}.$$

**Wie empfindlich.** Schon $18\,\text{mV}$ mehr verdoppeln den Strom, $2{,}5\,\text{mV}$ mehr erhöhen ihn um $10\,\%$:

$$\exp\frac{18\,\text{mV}}{25{,}85\,\text{mV}} = 2{,}0, \qquad \exp\frac{2{,}5\,\text{mV}}{25{,}85\,\text{mV}} = 1{,}10.$$

Für $1\,\text{mA}$ braucht dieser Transistor $0{,}655\,\text{V}$. Erwärmt er sich um ein Kelvin, sinkt die dafür nötige Spannung wie bei der Diode um
etwa $1{,}8\,\text{mV}$; bei fester Spannung steigt der Strom dann um rund $7\,\%$.

**Im Bild:** Wenige Millivolt an der Rampe entscheiden, ob doppelt so viele Autos hinüberkommen.
::::

## Die Stromverstärkung

Ganz ohne Verluste geht der Weg durch die Basis nicht. Der Basisstrom hat zwei Ursachen:

- **Rekombination in der Basis.** Ein kleiner Teil der Elektronen trifft unterwegs auf ein Loch und rekombiniert. Jedes verbrauchte Loch muss über den
  Basisanschluss ersetzt werden.
- **Rückinjektion.** Der leitende Basis-Emitter-Übergang lässt wie jeder pn-Übergang auch Löcher in die Gegenrichtung, aus der Basis in den Emitter. Weil der
  Emitter viel stärker dotiert ist als die Basis, sind es wenige; auch sie liefert der Basisanschluss.

Beide Anteile sind proportional zum Strom der Elektronen, die der Emitter aussendet, und damit zum Kollektorstrom. Ihr Verhältnis ist die Kennzahl des
Transistors, die __Stromverstärkung__ $B$, im Skript Verstärkung genannt. Daneben benutzt man das Verhältnis von Kollektor- zu Emitterstrom $\alpha$:

:::formel
$$B = \frac{I_C}{I_B}, \qquad \alpha = \frac{I_C}{I_E}, \qquad B = \frac{\alpha}{1 - \alpha}.$$
:::

**So liest man das:** $B$ liegt nach dem Skript zwischen $10$ und $1000$, bei kleinen Transistoren meist bei einigen hundert; $\alpha$ ist knapp unter eins. Weil
$\alpha$ so nahe an eins liegt, verändert schon eine winzige Änderung von $\alpha$ den Wert von $B$ stark. Deshalb streut $B$ in der Fertigung beträchtlich, wie
das Skript sagt, und gute Schaltungen müssen mit jedem $B$ eines ganzen Bereichs funktionieren. Für kleine Änderungen um einen Arbeitspunkt benutzt man später
die differentielle Stromverstärkung $\beta$; in diesem Kapitel genügt $B$.

**Im Bild:** Auf jedes Auto, das in der Basis in eine Lücke fällt, und jede Lücke, die ins Emitter-Parkhaus wandert, kommen einige hundert Autos, die in den
Kollektor stürzen.

:::herleitung
**$B$ aus $\alpha$.** Nach der Knotenregel ist der Basisstrom der Unterschied aus Emitter- und Kollektorstrom. Mit $I_E = I_C/\alpha$:

$$I_B = I_E - I_C = I_C\,\Big(\frac{1}{\alpha} - 1\Big) = I_C\,\frac{1 - \alpha}{\alpha}, \qquad B = \frac{I_C}{I_B} = \frac{\alpha}{1 - \alpha}.$$

Umgekehrt ist $\alpha$ gleich $B/(B + 1)$.

**$B$ aus den Verlusten.** Der Emitter sende den Elektronenstrom $I_n$ in die Basis. Davon rekombiniere der Bruchteil $\delta$; die Löcher, die in den Emitter
zurückgehen, seien der Bruchteil $\eta$ von $I_n$. Dann ist

$$I_C = (1 - \delta)\,I_n, \qquad I_B = (\delta + \eta)\,I_n, \qquad B = \frac{1 - \delta}{\delta + \eta} \approx \frac{1}{\delta + \eta}.$$

Eine dünne Basis macht $\delta$ klein, ein stark dotierter Emitter $\eta$. Im Bild: Je schmaler das Basis-Parkhaus und je voller das Emitter-Parkhaus, desto
weniger Autos und Lücken gehen unterwegs verloren.
:::

::::beispiel Stromverstärkung in Zahlen
**(a) Aus gemessenen Strömen.** Ein Transistor führt

$$I_C = 2\,\text{mA}, \qquad I_B = 10\,\mu\text{A}.$$

Dann sind

$$I_E = 2{,}010\,\text{mA}, \qquad B = \frac{2\,\text{mA}}{10\,\mu\text{A}} = 200, \qquad \alpha = \frac{2\,\text{mA}}{2{,}010\,\text{mA}} = 0{,}99502.$$

Zur Probe ergibt $\alpha/(1 - \alpha)$ wieder $200$.

**(b) Wie empfindlich $B$ auf $\alpha$ reagiert.** Drei Werte von $\alpha$:

$$\alpha = 0{,}990: \ B = 99, \qquad \alpha = 0{,}995: \ B = 199, \qquad \alpha = 0{,}996: \ B = 249.$$

Ein Tausendstel mehr $\alpha$ macht $B$ um ein Viertel größer; das ist die Streuung, mit der Schaltungen leben müssen.

**(c) Aus den Verlusten.** Rekombinieren $0{,}3\,\%$ der Elektronen in der Basis und gehen Löcher im Umfang von $0{,}2\,\%$ in den Emitter zurück:

$$B = \frac{1 - 0{,}003}{0{,}003 + 0{,}002} = 199.$$

**Im Bild:** Ein halbes Prozent Verluste unterwegs, und auf jeden verlorenen Platz kommen rund zweihundert Autos im Kollektor.
::::

## Strom- oder spannungsgesteuert?

Die Transfergleichung sagt, dass $U_{BE}$ den Kollektorstrom steuert. Das Skript beschreibt den Transistor dagegen als stromgesteuerte Stromquelle, kurz CCCS,
nach dem Artikel über Zweitore: Der Basisstrom steuert den Kollektorstrom. Beides stimmt, denn der Basisstrom ist ein fester Bruchteil des Kollektorstroms und
folgt deshalb demselben Gesetz. Das ist die __Eingangskennlinie__:

$$I_B = \frac{I_S}{B}\,\exp\frac{U_{BE}}{U_T}.$$

**So liest man das:** Physikalisch ist die Spannung am Basis-Emitter-Übergang die Ursache. Sie legt fest, wie viele Elektronen hinübergehen, und der Basisstrom
ist die Folge der Rekombination und Rückinjektion. In einer Schaltung kann man aber beides vorgeben. Gibt man eine Spannung vor, folgt der Kollektorstrom
exponentiell und empfindlich: $18\,\text{mV}$ verdoppeln ihn, ein Kelvin Erwärmung erhöht ihn um $7\,\%$, und ein anderes Exemplar mit doppeltem $I_S$ führt den
doppelten Strom. Gibt man einen Basisstrom vor, folgt der Kollektorstrom linear über $B$, unabhängig von $I_S$ und kaum von der Temperatur, dafür mit der Streuung
von $B$. Rechnet man von Hand mit festem $U_{BE}$ wie bei der Diode, bleibt nur der Basisstrom als Stellgröße; daher stammt die Stromsicht der Vorlesung. Gute
Schaltungen machen sich von beidem unabhängig, wie der nächste Artikel zeigt.

**Im Bild:** Die Höhe der Rampe entscheidet, wie viele Autos kommen, und mit ihnen, wie viele Lücken die Basis ersetzen muss. Man kann die Rampe einstellen oder
die Zahl der Ersatzlücken vorgeben; das eine legt das andere fest.

:::herleitung
Man teilt die Transfergleichung durch $B$; nach der Definition von $B$ steht links der Basisstrom:

$$I_B = \frac{I_C}{B} = \frac{I_S}{B}\,\exp\frac{U_{BE}}{U_T}.$$

Die Eingangskennlinie ist also die Kennlinie einer Diode mit dem Sättigungsstrom $I_S/B$; deshalb ähnelt sie, wie das Skript sagt, der einer pn-Diode, mit einer
Durchlassspannung um $0{,}6\,\text{V}$. Im Bild: Rampe und Ersatzlücken hängen fest zusammen; wer das eine kennt, kennt das andere.
:::

::::beispiel Zwei Sichten auf denselben Arbeitspunkt
Der Transistor von oben, mit

$$I_S = 10^{-14}\,\text{A}, \qquad B = 200, \qquad U_{BE} = 0{,}65\,\text{V}.$$

**Spannungssicht.** Die Transfergleichung ergibt $0{,}83\,\text{mA}$ und daraus der Basisstrom:

$$I_B = \frac{0{,}83\,\text{mA}}{200} = 4{,}15\,\mu\text{A}.$$

**Stromsicht.** Wer den Basisstrom $4{,}15\,\mu\text{A}$ vorgibt, erhält über $B$ dieselben $0{,}83\,\text{mA}$ und, aus der Eingangskennlinie, dieselbe Spannung.

**Doppelter Strom.** In der Spannungssicht braucht man $18\,\text{mV}$ mehr, in der Stromsicht den doppelten Basisstrom.

**Was streut.** Ein zweites Exemplar habe den doppelten Sättigungsstrom und eine größere Verstärkung:

$$I_S = 2\cdot10^{-14}\,\text{A}, \qquad B = 300.$$

Bei derselben Spannung führt es $1{,}66\,\text{mA}$, beim selben Basisstrom $1{,}25\,\text{mA}$. Beide Sichten liefern also unterschiedlich große Abweichungen, je nachdem, welcher Kennwert stärker streut.

**Im Bild:** Dasselbe Parkhaus, einmal über die Rampenhöhe, einmal über die Zahl der Ersatzlücken eingestellt.
::::

## Die Kennlinien

Das Verhalten eines Transistors beschreibt man durch drei Kennlinien, wie in Bild 11.3 des Skripts:

- Die **Eingangskennlinie** zeigt $I_B$ über $U_{BE}$, nach dem vorigen Abschnitt eine Diodenkennlinie mit dem Knie um $0{,}6\,\text{V}$.
- Die **Stromsteuerkennlinie** oder Übertragungskennlinie zeigt $I_C$ über $I_B$, für kleine und mittlere Ströme eine Gerade durch den Ursprung mit der Steigung
  $B$. In der doppelt logarithmischen Darstellung von Bild 11.3b ist sie eine Gerade der Steigung eins, und $B$ zeigt sich als ihr Abstand von der Diagonale,
  nicht als Steigung, wie das Skript schreibt. Bei sehr großen Strömen sinkt $B$, weil dann so viele Elektronen in der Basis sind wie Löcher; das Skript sagt
  dazu, der Transistor gehe in Sättigung, meint aber nicht den Sättigungsbereich der nächsten Zeile.
- Die **Ausgangskennlinie** zeigt $I_C$ über $U_{CE}$, für jeden Basisstrom eine eigene Kurve. Oberhalb einiger Zehntelvolt verläuft sie fast waagrecht, wie
  die Kennlinie einer Stromquelle, nach der Transfergleichung. Bei echten Transistoren steigt sie dort leicht an, weil eine größere Kollektorspannung die
  Sperrschicht verbreitert und die Basis wirksam dünner macht, der __Early-Effekt__. Nahe null fällt sie steil ab, weil der Kollektor dann nicht mehr positiv
  gegen die Basis ist. Die eingezeichnete Linie $U_{CE} = U_{BE}$ ist die Grenze, an der $U_{CB}$ nach der Maschenregel null ist.

Die Kurven in Bild 11.3c gehören zu $B$ um $1600$, etwa $9\,\text{mA}$ bei $5\,\mu\text{A}$ und $31\,\text{mA}$ bei $20\,\mu\text{A}$, mehr als die $10$ bis $1000$
des Textes; das Bild ist schematisch.

**Im Bild:** Eingangskennlinie: wie viele Ersatzlücken je Rampenhöhe; Stromsteuerkennlinie: Kollektorautos je Ersatzlücke; Ausgangskennlinie: Kollektorautos je
Absturztiefe, gleich viele, solange es eine Kante gibt.

:::grafik
Szene: get1/bipolartransistoren/01-kennlinien · Vorlage: transistor-kennlinien
Drei verbundene Diagramme eines Transistors mit $I_S = 10^{-14}\,\text{A}$ und $B = 200$: links die Eingangskennlinie $I_B$ über $U_{BE}$ bis $0{,}75\,\text{V}$
mit dem Knie um $0{,}6\,\text{V}$; in der Mitte die Stromsteuerkennlinie $I_C$ über $I_B$ als Gerade der Steigung $200$, umschaltbar auf doppelt logarithmische
Achsen mit der Steigung eins und dem Abstand $B$, und mit einem Abknicken bei großen Strömen; rechts das Ausgangskennlinienfeld $I_C$ über $U_{CE}$ bis
$12\,\text{V}$ für $I_B = 0$, $5$, $10$, $15$ und $20\,\mu\text{A}$, mit der Linie $U_{CE} = U_{BE}$ und der Grenze $U_{CE,\text{sat}} = 0{,}2\,\text{V}$. Ein Regler
für $U_{BE}$ bewegt einen Punkt auf allen drei Kurven zugleich. Ein Schalter blendet den Early-Effekt ein, der die waagrechten Äste leicht ansteigen lässt.
Kernaussage: Eine Diodenkennlinie am Eingang, eine Gerade dazwischen und Stromquellenäste am Ausgang. (Rot = Kennlinien, blau = Arbeitspunkt, orange =
Bereichsgrenzen, grau = Achsen.)
:::

## Die drei Arbeitsbereiche

Für die Rechnung von Hand legt das Skript, wie bei der Diode, drei Arbeitsbereiche mit einfachen Modellen fest. In jedem ersetzt man den Transistor durch ein
lineares Modell, rechnet und prüft danach eine Bedingung. Die beiden Grenzwerte des Skripts sind $0{,}6\,\text{V}$ für $U_{BE,\text{ein}}$ und $0{,}2\,\text{V}$
für $U_{CE,\text{sat}}$:

:::formel Definition
$$\begin{cases} I_B = I_C = 0, & U_{BE} < U_{BE,\text{ein}}, \\ I_C = B\,I_B, & U_{CE} \ge U_{CE,\text{sat}}, \\ U_{CE} = U_{CE,\text{sat}}, & I_C \le B\,I_B. \end{cases}$$
:::

**So liest man das:** Die erste Zeile ist der __Sperrbereich__, die zweite der __aktive Bereich__, die dritte der __Sättigungsbereich__. Links steht jeweils das
Modell, mit dem man rechnet, rechts die Bedingung, die das Ergebnis erfüllen muss. Im aktiven und im Sättigungsbereich leitet der Basis-Emitter-Übergang, und
man setzt $U_{BE}$ gleich $U_{BE,\text{ein}}$. In der Sprache der Übergänge: Im Sperrbereich sperren beide, im aktiven Bereich leitet nur der Basis-Emitter-Übergang,
in der Sättigung leiten beide. Die vierte Möglichkeit, nur der Basis-Kollektor-Übergang leitet, vertauscht Emitter und Kollektor mit sehr kleiner Verstärkung;
dieser __Inversbetrieb__ kommt selten vor.

**Im Bild:** Sperrbereich: Die Rampe ist zu hoch. Aktiver Bereich: Die Rampe ist abgesenkt, und die Kante ist tief. Sättigung: Das Kollektor-Parkhaus ist bis auf
die Höhe der Basis gehoben, es gibt keine Kante mehr, und die Straßen außen begrenzen den Verkehr.

:::herleitung
**Aktiver Bereich.** Die Transfergleichung und damit $I_C = BI_B$ gelten, solange der Basis-Kollektor-Übergang sperrt. Das ist der Fall, solange $U_{CE}$ nicht
unter einige Zehntelvolt fällt; das Modell setzt die Grenze bei $U_{CE,\text{sat}}$.

**Sättigung.** Kann die äußere Schaltung den Strom $BI_B$ nicht liefern, etwa weil der Kollektorwiderstand dafür mehr Spannung bräuchte, als die Quelle hat,
sinkt $U_{CE}$, bis auch der Basis-Kollektor-Übergang leitet. Dann bestimmt die äußere Schaltung den Kollektorstrom, und er bleibt unter $BI_B$; die Spannung
bleibt bei rund $U_{CE,\text{sat}}$.

**Sperrbereich.** Unter $U_{BE,\text{ein}}$ ist der Exponentialterm so klein, dass man beide Ströme null setzt, wie im Modell der Stufe 2 bei der Diode. Im Bild:
Erst wenn die Rampe niedrig genug ist, kommt merklicher Verkehr hinüber.
:::

::::beispiel Ein Transistor in allen drei Bereichen
Ein npn-Transistor mit $B = 200$; der Kollektor liegt über $R_C$ an der Versorgung, der Emitter an Masse, und eine Stromquelle gibt den Basisstrom vor:

$$U_{CC} = 12\,\text{V}, \qquad R_C = 2\,\text{k}\Omega.$$

Im aktiven Bereich gilt am Kollektor die Maschenregel:

$$U_{CE} = U_{CC} - R_C\,I_C.$$

**$I_B = 0$.** Kein Basisstrom, Sperrbereich; $U_{CE}$ ist $12\,\text{V}$.

**$I_B = 10\,\mu\text{A}$.** Annahme aktiv:

$$I_C = 200\cdot10\,\mu\text{A} = 2\,\text{mA}, \qquad U_{CE} = 12\,\text{V} - 2\,\text{k}\Omega\cdot2\,\text{mA} = 8\,\text{V}.$$

Das ist mehr als $0{,}2\,\text{V}$; die Annahme hält.

**$I_B = 25\,\mu\text{A}$.** Annahme aktiv:

$$I_C = 5\,\text{mA}, \qquad U_{CE} = 12\,\text{V} - 10\,\text{V} = 2\,\text{V}.$$

Auch diese Annahme hält.

**$I_B = 50\,\mu\text{A}$.** Annahme aktiv: $10\,\text{mA}$ verlangten $20\,\text{V}$ an $R_C$, und $U_{CE}$ wäre $-8\,\text{V}$, ein Widerspruch. Also Sättigung:

$$I_C = \frac{12\,\text{V} - 0{,}2\,\text{V}}{2\,\text{k}\Omega} = 5{,}9\,\text{mA} \le B\,I_B = 10\,\text{mA}.$$

Die Probe hält. Die Grenze zwischen aktivem Bereich und Sättigung liegt bei einem Basisstrom von $5{,}9\,\text{mA}/200$, also $29{,}5\,\mu\text{A}$.

**Im Bild:** Mehr Ersatzlücken in der Basis bringen mehr Autos in den Kollektor, bis die Straße am Kollektor nicht mehr hergibt; dann füllt sich das
Kollektor-Parkhaus bis zur Kante.
::::

Zwischen Sperrbereich und Sättigung springt der Transistor, wenn man ihn als __Schalter__ benutzt: aus bei null Basisstrom, ein bei so viel Basisstrom, dass er
sicher sättigt. In beiden Zuständen verliert er wenig Leistung, sperrend fließt kein Strom, gesättigt liegen nur $U_{CE,\text{sat}}$ an; und er schaltet, wie
das Skript sagt, sehr schnell und ohne Verschleiß. Damit er auch mit der kleinsten Verstärkung $B_\text{min}$ eines Typs sicher sättigt, muss der Basisstrom
mindestens betragen:

$$I_B \ge \frac{U_{CC} - U_{CE,\text{sat}}}{B_\text{min}\,R_C}.$$

**So liest man das:** Der Bruch ist der Kollektorstrom in der Sättigung, geteilt durch die kleinste Verstärkung. Praktisch gibt man das Zwei- bis Fünffache, die
__Übersteuerung__, damit Streuung, Alterung und Temperatur nicht schaden. Liegt im Kollektorkreis noch eine Last mit eigener Spannung, zieht man auch sie im
Zähler ab.

**Im Bild:** So viele Ersatzlücken, dass der Verkehr auch bei der schwächsten Basis noch mehr Autos bringen könnte, als die Straße zum Kollektor aufnimmt.

:::herleitung
In der Sättigung bestimmt der Kollektorkreis den Strom: Die Spannung $U_{CC} - U_{CE,\text{sat}}$ liegt an $R_C$. Die Bedingung der Sättigung, $I_C \le BI_B$,
muss auch für die kleinste Verstärkung gelten; nach $I_B$ aufgelöst ergibt sich die Formel. Im Bild: Die Basis muss mehr Verkehr anbieten, als abfließen kann.
:::

::::beispiel Eine Leuchtdiode schalten
Ein Logikausgang mit $5\,\text{V}$ soll eine Leuchtdiode mit etwa $20\,\text{mA}$ schalten; er selbst darf nur wenige Milliampere liefern. Leuchtdiode und
Transistor liegen in Reihe mit $R_C$ an $5\,\text{V}$, der Logikausgang speist die Basis über $R_B$:

$$U_{LED} = 2{,}0\,\text{V}, \qquad I_{LED} = 20\,\text{mA}, \qquad B_\text{min} = 100, \qquad U_{BE} = 0{,}7\,\text{V}.$$

**Kollektorwiderstand.** In der Sättigung bleiben für $R_C$:

$$R_C = \frac{5\,\text{V} - 2{,}0\,\text{V} - 0{,}2\,\text{V}}{20\,\text{mA}} = 140\,\Omega.$$

Mit dem Normwert $150\,\Omega$ fließen $18{,}7\,\text{mA}$.

**Basisstrom.** Mindestens $20\,\text{mA}/100$, also $0{,}2\,\text{mA}$; mit dreifacher Übersteuerung $0{,}6\,\text{mA}$:

$$R_B = \frac{5\,\text{V} - 0{,}7\,\text{V}}{0{,}6\,\text{mA}} = 7{,}2\,\text{k}\Omega.$$

Mit dem Normwert $6{,}8\,\text{k}\Omega$ fließen $0{,}63\,\text{mA}$; selbst $B = 100$ böte $63\,\text{mA}$, weit mehr als die $18{,}7\,\text{mA}$, die der
Kollektorkreis zulässt.

**Verluste.** Im gesättigten Transistor fallen nur

$$P = 0{,}2\,\text{V}\cdot18{,}7\,\text{mA} = 3{,}7\,\text{mW}$$

an. Der Logikausgang liefert $0{,}63\,\text{mA}$ statt $19\,\text{mA}$.

**Im Bild:** Ein kleiner Ersatzstrom von $0{,}6\,\text{mA}$ öffnet die Rampe so weit, dass mehr kommen könnte, als die Straße zur Leuchtdiode aufnimmt.
::::

:::grafik
Szene: get1/bipolartransistoren/01-arbeitsbereiche · Vorlage: lastgerade-transistor
Das Ausgangskennlinienfeld eines Transistors mit $B = 200$ für Basisströme von $0$ bis $50\,\mu\text{A}$, darüber die Arbeitsgerade der Schaltung mit
$U_{CC} = 12\,\text{V}$ und $R_C = 2\,\text{k}\Omega$ von $(12\,\text{V}, 0)$ nach $(0, 6\,\text{mA})$. Ein Regler für $I_B$ schiebt den Arbeitspunkt längs der
Geraden: bei null im Sperrbereich unten rechts, bei $10$ und $25\,\mu\text{A}$ im aktiven Bereich bei $8$ und $2\,\text{V}$, ab $29{,}5\,\mu\text{A}$ in der Sättigung
links, wo er bei $5{,}9\,\text{mA}$ und $0{,}2\,\text{V}$ stehen bleibt, obwohl der Basisstrom weiter steigt. Die drei Bereiche sind farbig hinterlegt, daneben
ein kleines Bild der drei Parkhäuser im jeweiligen Zustand und ein zweiter Reiter mit der Schaltung der Leuchtdiode. Kernaussage: Auf der Arbeitsgeraden wandert
der Transistor vom Sperren über den aktiven Bereich in die Sättigung. (Rot = Arbeitspunkt, blau = Kennlinien, orange = Arbeitsgerade, grau = Bereiche und
Achsen.)
:::

## Der pnp-Transistor

Kehrt man die Dotierfolge um, entsteht nach Abschnitt 11.7 des Skripts der __pnp-Transistor__: ein p-dotierter Emitter, eine n-dotierte Basis und ein
p-dotierter Kollektor. Der Emitter sendet jetzt Löcher durch die Basis, und alle Spannungen und Ströme kehren sich um. Im Symbol zeigt der Emitterpfeil nach
innen; in Bild 11.30 fließt der Emitterstrom hinein, Basis- und Kollektorstrom fließen heraus, und $U_{BE,\text{ein}}$ und $U_{CE,\text{sat}}$ sind negativ. Mit
Basis- und Kollektorstrom in dieser Flussrichtung gezählt, aus dem Transistor heraus, gelten die drei Bereiche gespiegelt:

$$\begin{cases} I_B = I_C = 0, & U_{BE} > -0{,}6\,\text{V}, \\ I_C = B\,I_B, & U_{CE} \le -0{,}2\,\text{V}, \\ U_{CE} = -0{,}2\,\text{V}, & I_C \le B\,I_B. \end{cases}$$

**So liest man das:** Spannungen tauschen ihr Vorzeichen, die Ungleichungen für sie drehen sich um, die Ströme laufen in der Gegenrichtung. Das Skript schreibt
für die Sättigung $I_C \ge I_B\cdot B$. Das stimmt nur, wenn man die Ströme wie beim npn-Transistor in den Transistor hinein zählt, wo sie negativ werden; mit
den Pfeilen von Bild 11.30 gilt wie beim npn-Transistor das Kleiner-gleich. Das Skript sagt außerdem, auch hier sei die Basis schwächer dotiert als Kollektor und
Emitter. Nach Abschnitt 11.1 ist aber der Kollektor am schwächsten dotiert, und das gilt für beide Typen. Man braucht pnp-Transistoren etwa, wenn ein Verbraucher an
Masse hängt und an der positiven Versorgung geschaltet werden soll, und in Gegentaktstufen zusammen mit npn-Transistoren; das Skript verweist dafür auf
Schaltungstechnik 1 und 2.

**Im Bild:** Dieselben drei Parkhäuser, aber für Lücken statt für Autos: Lücken wandern über die Rampe vom Emitter in die Basis und fallen dann in den Kollektor.

:::herleitung
Jede Aussage über den npn-Transistor gilt für den pnp-Transistor, wenn man p- und n-Dotierung, Elektronen und Löcher vertauscht. Dabei kehren alle
Übergangsspannungen ihr Vorzeichen um, und alle Ströme fließen in der Gegenrichtung. Zählt man die Ströme in der neuen Flussrichtung, sind ihre Werte positiv
und erfüllen dieselben Beziehungen wie beim npn-Transistor; die Spannungen werden negativ, und jede Ungleichung für eine Spannung kehrt sich um. Im Bild: Ein
Parkhaus, auf den Kopf gestellt, mit Lücken statt Autos, funktioniert genauso.
:::

::::beispiel Ein pnp-Transistor schaltet an der Versorgung
Der Emitter liegt an $+12\,\text{V}$, ein Verbraucher $R_C$ vom Kollektor nach Masse; die Basis zieht ein Widerstand $R_B$ nach Masse; $B = 200$:

$$R_C = 1\,\text{k}\Omega, \qquad R_B = 47\,\text{k}\Omega, \qquad U_{BE} = -0{,}7\,\text{V}.$$

**Basisstrom,** aus der Basis heraus nach Masse:

$$I_B = \frac{12\,\text{V} - 0{,}7\,\text{V}}{47\,\text{k}\Omega} = 0{,}240\,\text{mA}.$$

**Annahme aktiv.** $I_C$ wäre $48{,}1\,\text{mA}$; an $R_C$ lägen dann $48\,\text{V}$, mehr als die Versorgung hat, ein Widerspruch.

**Sättigung.** Am Verbraucher liegen $12\,\text{V}$ bis auf die $0{,}2\,\text{V}$ des Transistors:

$$I_C = \frac{12\,\text{V} - 0{,}2\,\text{V}}{1\,\text{k}\Omega} = 11{,}8\,\text{mA} \le B\,I_B = 48{,}1\,\text{mA}, \qquad U_{CE} = -0{,}2\,\text{V}.$$

Der Emitterstrom, in den Transistor hinein, ist $12{,}04\,\text{mA}$. Bis zu einem Basiswiderstand von rund $190\,\text{k}\Omega$ bliebe der Transistor gesättigt.

**Im Bild:** Lücken stürzen in Massen in den Kollektor, mehr als der Verbraucher abnehmen kann; der Transistor ist ganz durchgeschaltet.
::::

## Bedeutung und Ausblick

Der Bipolartransistor hat zwei Gesichter. Im aktiven Bereich ist er eine gesteuerte Stromquelle und damit ein Verstärker; zwischen Sperrbereich und Sättigung ist
er ein Schalter. Beide beruhen auf demselben Effekt: Die Spannung am Basis-Emitter-Übergang schickt Ladungsträger durch eine Basis, die zu dünn ist, um viele zu
verlieren, und der gesperrte Kollektorübergang sammelt sie ein.

Der nächste Artikel zeigt, wie man einen Transistor in seinen Arbeitspunkt bringt und dort hält, unabhängig von der Streuung von $B$ und von der Temperatur, und
welche drei Grundschaltungen es gibt. Danach folgt der Transistor als Verstärker für kleine Signale. Der andere große Transistortyp, der MOSFET, der in der
Digitaltechnik vorherrscht, gehört nach dem Skript nicht zu dieser Vorlesung.

:::kern
- Drei Zonen: stark dotierter Emitter, dünne Basis, schwach dotierter Kollektor; zwei pn-Übergänge.
- Am Transistor gelten $I_E=I_B+I_C$ und $U_{CE}=U_{CB}+U_{BE}$.
- Im aktiven Bereich leitet der Basis-Emitter-Übergang, der Basis-Kollektor-Übergang sperrt.
- Transfergleichung: $I_C=I_Se^{U_{BE}/U_T}$, unabhängig von der Kollektorspannung.
- Der Basisstrom stammt aus Rekombination in der Basis und Rückinjektion in den Emitter; $B=I_C/I_B$, typisch einige hundert.
- $\alpha=I_C/I_E$ ist knapp eins, und $B=\alpha/(1-\alpha)$ reagiert stark auf kleine Änderungen von $\alpha$.
- Physikalisch steuert $U_{BE}$; weil $I_B$ ein fester Bruchteil ist, kann man ebenso mit dem Basisstrom rechnen.
- Sperrbereich, aktiver Bereich und Sättigung: annehmen, rechnen, prüfen.
- Als Schalter braucht der Transistor genug Basisstrom für die kleinste Verstärkung, mit Übersteuerung.
- Beim pnp-Transistor kehren sich alle Spannungen und Ströme um.
:::

:::quiz
F: Woraus besteht ein Bipolartransistor, und welche Rolle spielt die Dotierung?
A: Aus drei Zonen, Emitter, Basis und Kollektor, mit zwei pn-Übergängen. Der Emitter ist am stärksten dotiert, damit kaum Löcher aus der Basis zurückkommen, der Kollektor am schwächsten, und die Basis ist sehr dünn, damit kaum Elektronen in ihr rekombinieren.
F: Was geschieht im aktiven Bereich, und warum hängt der Kollektorstrom kaum von der Kollektorspannung ab?
A: Der leitende Basis-Emitter-Übergang lässt Elektronen in die dünne Basis, sie diffundieren zum Kollektorrand, und das Feld des gesperrten Basis-Kollektor-Übergangs zieht sie in den Kollektor. Dieser Übergang sammelt jedes ankommende Elektron ein, gleich wie stark er gesperrt ist; daher $I_C=I_Se^{U_{BE}/U_T}$ ohne $U_{CE}$.
F: Wie empfindlich reagiert der Kollektorstrom auf $U_{BE}$?
A: Exponentiell: Mit $I_S=10^{-14}\,\text{A}$ fließen bei $0{,}60\,\text{V}$ $0{,}12\,\text{mA}$, bei $0{,}70\,\text{V}$ $5{,}75\,\text{mA}$. $18\,\text{mV}$ mehr verdoppeln den Strom, und ein Kelvin Erwärmung erhöht ihn bei fester Spannung um etwa $7\,\%$.
F: Woher kommt der Basisstrom, und wie groß ist $B$?
A: Aus der Rekombination eines kleinen Teils der Elektronen in der Basis und aus der Rückinjektion von Löchern in den Emitter; beide sind proportional zum Kollektorstrom. Mit $0{,}3\,\%$ und $0{,}2\,\%$ Verlust ist $B=(1-\delta)/(\delta+\eta)\approx199$; das Skript nennt $10$ bis $1000$.
F: Was ist $\alpha$, und warum streut $B$ so stark?
A: $\alpha=I_C/I_E$ ist knapp eins, bei $2\,\text{mA}$ und $10\,\mu\text{A}$ Basisstrom $0{,}995$. Aus der Knotenregel folgt $B=\alpha/(1-\alpha)$, und weil der Nenner so klein ist, macht ein Tausendstel mehr $\alpha$ den Wert $B$ von $199$ auf $249$.
F: Ist der Transistor strom- oder spannungsgesteuert?
A: Physikalisch steuert $U_{BE}$ die Zahl der Elektronen, der Basisstrom ist ihre Folge; weil er ein fester Bruchteil $1/B$ ist, folgt er demselben Gesetz, $I_B=(I_S/B)e^{U_{BE}/U_T}$. Man kann deshalb ebenso mit dem Basisstrom rechnen; mit festem $U_{BE}$ wie bei der Diode bleibt er die einzige Stellgröße, daher die Stromsicht der Vorlesung.
F: Was zeigen die drei Kennlinien, und was ist an der Darstellung des Skripts zu präzisieren?
A: Die Eingangskennlinie ist eine Diodenkennlinie mit Knie um $0{,}6\,\text{V}$, die Stromsteuerkennlinie eine Gerade $I_C=BI_B$, die Ausgangskennlinie oberhalb weniger Zehntelvolt fast waagrecht wie eine Stromquelle. In der doppelt logarithmischen Darstellung ist $B$ der Abstand, nicht die Steigung; das Abfallen von $B$ bei großen Strömen ist nicht der Sättigungsbereich; und Bild 11.3c entspricht $B$ um $1600$.
F: Wie bestimmt man den Arbeitsbereich eines Transistors?
A: Man nimmt einen Bereich an, rechnet mit seinem Modell und prüft die Bedingung: Sperrbereich mit $I_B=I_C=0$ bei $U_{BE}<U_{BE,\text{ein}}$, aktiv mit $I_C=BI_B$ bei $U_{CE}\ge U_{CE,\text{sat}}$, Sättigung mit $U_{CE}=U_{CE,\text{sat}}$ bei $I_C\le BI_B$. Mit $12\,\text{V}$, $2\,\text{k}\Omega$ und $B=200$ ist der Transistor bei $25\,\mu\text{A}$ aktiv mit $2\,\text{V}$ und bei $50\,\mu\text{A}$ gesättigt mit $5{,}9\,\text{mA}$.
F: Wie legt man einen Transistor als Schalter aus?
A: Der Kollektorkreis legt den Strom in der Sättigung fest, und der Basisstrom muss ihn auch mit der kleinsten Verstärkung tragen, $I_B\ge(U_{CC}-U_{CE,\text{sat}})/(B_\text{min}R_C)$, mit zwei- bis fünffacher Übersteuerung. Für eine Leuchtdiode mit $20\,\text{mA}$ an $5\,\text{V}$ ergeben sich $150\,\Omega$ und $6{,}8\,\text{k}\Omega$, und der Transistor verliert nur $3{,}7\,\text{mW}$.
F: Was ändert sich beim pnp-Transistor, und welche Unstimmigkeiten hat das Skript dort?
A: Dotierung, Ladungsträger, Spannungen und Ströme kehren sich um; $U_{BE,\text{ein}}$ und $U_{CE,\text{sat}}$ sind negativ, und mit den Strömen in Flussrichtung gelten dieselben Beziehungen. Das Skript schreibt für die Sättigung $I_C\ge I_B\cdot B$, was nur mit hineingezählten, negativen Strömen stimmt, und nennt die Basis schwächer dotiert als den Kollektor, entgegen seinem Abschnitt 11.1.
:::
