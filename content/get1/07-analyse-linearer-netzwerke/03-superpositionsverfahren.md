---
title: Das Superpositionsverfahren
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Analyse linearer Netzwerke
order: 70700
summary: Von Grund auf – warum man ein Netz mit mehreren Quellen lösen darf, indem man jede Quelle allein wirken lässt und die Teilwirkungen addiert, und wo das aufhört. Leitbild sind mehrere Wasserwerke an einem Stadtnetz, die man einzeln stilllegt, um ihren Beitrag zum Druck an einem Hahn zu messen. Mit der genauen Bedeutung von Linearität, dem Überlagerungssatz samt Beweis, Spannungs- und Stromverstärkungen, Transimpedanzen und Transadmittanzen, dem Verfahren in drei Schritten, dem Kreuzterm, an dem die Überlagerung von Leistungen scheitert, einem Gegenbeispiel mit Diode und dem spannungsbasierten R-2R-Digital-Analog-Wandler. Mit Beispiel-Seite.
tags: Superposition, Überlagerungssatz, lineare Netzwerke, mehrere Quellen, Teilströme, Leistung
---

## Anschaulich

Sobald in einem Netz mehrere Quellen gleichzeitig treiben, wird die Rechnung mit Knoten- und Maschenregel schnell unübersichtlich. Das
__Superpositionsverfahren__ (von lateinisch *superponere*, überlagern), auch __Überlagerungsverfahren__ genannt, zerlegt sie: Man lässt jede Quelle
allein wirken, berechnet ihren Beitrag und addiert am Ende alle Beiträge. Dass das erlaubt ist, liegt an der Linearität der Netze — und genau dort
liegen auch seine Grenzen.

**Das Leitbild dieses Artikels:** **Mehrere Wasserwerke an einem Netz.** Wie im vorigen Artikel speisen Türme und Pumpen ein Stadtnetz aus linearen
Rohren, in denen der Druckverlust proportional zum Durchfluss ist. Die Stadtwerke wollen wissen, welches Werk wie viel zum Druck an einem bestimmten Hahn
beiträgt. Sie legen alle Werke bis auf eines still, die Türme auf Höhe null, die Pumpen angehalten, messen und wiederholen das für jedes Werk.

Drei Folgerungen:

- **Die Beiträge addieren sich.** Druck und Durchfluss an jeder Stelle sind die Summe dessen, was jedes Werk allein bewirkt. Ein Werk kann dabei auch
  gegen ein anderes drücken: In einem Rohr, in dem das eine Werk Wasser vorwärts schickt, schickt das andere es vielleicht rückwärts, und es fließt nur der
  Unterschied.
- **Jeder Beitrag ist proportional zu seinem Werk.** Ein doppelt so hoher Turm trägt doppelt so viel Druck bei. Wie viel genau, bestimmt allein das
  Rohrnetz zwischen Werk und Hahn.
- **Die Reibungswärme addiert sich nicht.** Sie wächst in einem Rohr mit dem Quadrat des Durchflusses. Zwei Werke, die jedes allein einen Liter pro
  Sekunde durch ein Rohr schicken, erzeugen zusammen die vierfache Wärme, nicht die doppelte.

:::grafik
Szene: get1/analyse-linearer-netzwerke/03-wasserwerke · Vorlage: wasserwerke-ueberlagerung
Ein Stadtnetz mit zwei Türmen und einer Pumpe, ein Hahn mit Manometer und ein mittleres Rohr mit Durchflussanzeige. Drei Schalter legen die Werke
einzeln still: Der Turm sinkt auf Höhe null, der Kolben der Pumpe stoppt. Mit nur einem aktiven Werk erscheint dessen Beitrag als farbiger Balken am
Manometer und als Pfeil im mittleren Rohr. Schaltet man nacheinander jedes Werk einzeln durch, stapeln sich die Balken zur Gesamthöhe, die das Manometer
mit allen Werken zugleich zeigt; einer der Pfeile im Rohr zeigt rückwärts und wird abgezogen. Ein zweites Feld zeigt am selben Rohr die Reibungswärme:
Die Balken der einzelnen Werke ergeben zusammen nicht die gemessene Wärme. Kernaussage: Drücke und Durchflüsse überlagern sich, die Wärme nicht. (Blau =
Wasser und Drücke, rot = Werke, orange = Beiträge der einzelnen Werke, grau = Rohrnetz.)
:::

## Was linear heißt

Das Verfahren steht und fällt mit einem Begriff, der in der Elektrotechnik ständig vorkommt und eine genaue Bedeutung hat. Eine Zuordnung $f$, die jeder
__Ursache__ eine __Wirkung__ zuordnet, heißt __linear__, wenn sie zwei Eigenschaften hat:

- __Additivität__: Die Wirkung zweier Ursachen zusammen ist die Summe ihrer Wirkungen.
- __Homogenität__: Die $c$-fache Ursache hat die $c$-fache Wirkung, für jede reelle Zahl $c$.

Im Netz ist die Ursache die Liste aller Quellenwerte, ein Vektor $\vec x$ aus den $n$ Quellenspannungen und den $m$ Quellströmen, und die Wirkung eine
einzelne Zahl, etwa die Spannung oder der Strom in einem Zweig:

$$f:\ \mathbb{R}^{n+m} \to \mathbb{R}, \qquad \vec x = (U_{q1}, \dots, U_{qn}, I_{q1}, \dots, I_{qm}) \mapsto \text{Zweigspannung oder Zweigstrom}.$$

Die Einträge von $\vec x$ haben verschiedene Einheiten, Volt und Ampere; das stört nicht, denn jeder Eintrag bekommt unten seinen eigenen Faktor. Beide
Eigenschaften zusammengefasst:

:::formel Definition
$$f(c_1\,\vec x_1 + c_2\,\vec x_2) = c_1\,f(\vec x_1) + c_2\,f(\vec x_2) \qquad\text{für alle } \vec x_1, \vec x_2 \in \mathbb{R}^{n+m},\ c_1, c_2 \in \mathbb{R}.$$
:::

**So liest man das:** Links werden erst die Ursachen gemischt und dann die Wirkung bestimmt, rechts erst die Wirkungen bestimmt und dann ebenso gemischt.
Linear heißt: Beide Reihenfolgen geben dasselbe. Das ohmsche Gesetz ist linear, die Leistung an einem Widerstand nicht. Die Kennlinie einer realen
Quelle ist es nur, wenn man die Quellenspannung als zweite Ursache mitzählt; deshalb gehören alle Quellen in die Liste der Ursachen.

**Im Bild:** Die Ursache sind die Höhen aller Türme und die Fördermengen aller Pumpen, die Wirkung ist der Druck an einem Hahn. Linear heißt: Zwei
Einstellungen der Werke einzeln messen und die Drücke addieren gibt dasselbe wie beide Einstellungen zugleich.

::::beispiel Linear oder nicht?
**(a) Das ohmsche Gesetz.** An einem Widerstand von $50\,\Omega$ ist der Strom eine Funktion der Spannung:

$$I(U) = \frac{U}{50\,\Omega}, \qquad I(2\,\text{V}) = 40\,\text{mA}, \qquad I(3\,\text{V}) = 60\,\text{mA}, \qquad I(5\,\text{V}) = 100\,\text{mA}.$$

Die Wirkung der Summe ist die Summe der Wirkungen: linear.

**(b) Die Leistung.** Am selben Widerstand:

$$P(U) = \frac{U^2}{50\,\Omega}, \qquad P(2\,\text{V}) + P(3\,\text{V}) = 0{,}08\,\text{W} + 0{,}18\,\text{W} = 0{,}26\,\text{W}, \qquad P(5\,\text{V}) = 0{,}5\,\text{W}.$$

Die Summe der Wirkungen ist nur gut halb so groß wie die Wirkung der Summe: nicht linear.

**(c) Die Kennlinie einer realen Quelle.** Mit $12\,\text{V}$ und $2\,\Omega$ hängt die Klemmenspannung vom Strom ab:

$$U(I) = 12\,\text{V} - 2\,\Omega\cdot I, \qquad U(1\,\text{A}) + U(2\,\text{A}) = 10\,\text{V} + 8\,\text{V} = 18\,\text{V}, \qquad U(3\,\text{A}) = 6\,\text{V}.$$

Als Funktion des Stroms allein ist das nicht linear, wegen des festen Anteils $12\,\text{V}$. Zählt man die Quellenspannung als zweite Ursache mit, ist es
linear: Zwei Zustände mit je $12\,\text{V}$ und $1\,\text{A}$ beziehungsweise $2\,\text{A}$ ergeben zusammen den Zustand mit $24\,\text{V}$ und $3\,\text{A}$,

$$U(U_q, I) = U_q - 2\,\Omega\cdot I, \qquad U(24\,\text{V}, 3\,\text{A}) = 18\,\text{V} = U(12\,\text{V}, 1\,\text{A}) + U(12\,\text{V}, 2\,\text{A}).$$

**Im Bild:** Ein lineares Rohr verliert bei der Summe zweier Durchflüsse die Summe der Druckverluste, seine Reibungswärme aber nicht; und ein Turm muss
mitgezählt werden, wenn sich Drücke addieren sollen.
::::

## Der Überlagerungssatz

**Die Akteure:**

- ein lineares Netz aus Widerständen mit $n$ idealen Spannungsquellen $U_{q1}, \dots, U_{qn}$ und $m$ idealen Stromquellen $I_{q1}, \dots, I_{qm}$ (Bild 7.65
  des Skripts); die Innenwiderstände realer Quellen zählen zu den Widerständen;
- eine beliebige Spannung $U_{AB}$ zwischen zwei Knoten A und B und ein beliebiger Strom $I_{CD}$, etwa in einer Verbindung zwischen zwei Knoten C und D;
- für jede Quelle ein fester Faktor: für $U_{AB}$ die __Spannungsverstärkungen__ $a_\nu$ ohne Einheit und die __Transimpedanzen__ $Z_\mu$ in Ohm, für $I_{CD}$
  die __Transadmittanzen__ $Y_\nu$ in Siemens und die __Stromverstärkungen__ $c_\mu$ ohne Einheit.

**Das Zusammenspiel:** *Wie hängt eine Spannung oder ein Strom irgendwo im Netz von allen Quellen zugleich ab?*

:::formel Satz
$$U_{AB} = \sum_{\nu=1}^{n} a_\nu\,U_{q\nu} + \sum_{\mu=1}^{m} Z_\mu\,I_{q\mu}, \qquad I_{CD} = \sum_{\nu=1}^{n} Y_\nu\,U_{q\nu} + \sum_{\mu=1}^{m} c_\mu\,I_{q\mu}.$$
:::

**So liest man das:** Jeder Summand ist die __Teilwirkung__ einer Quelle, also der Wert, den $U_{AB}$ oder $I_{CD}$ hätte, wenn nur diese Quelle wirkte. Die
Gesamtwirkung ist die Summe der Teilwirkungen. Die Faktoren sagen, wie empfindlich die Größe auf die einzelne Quelle reagiert, und sie hängen nur von den
Widerständen ab, nicht von den Quellenwerten.

Die Namen beschreiben, was wohin wirkt. Eine Spannungsverstärkung macht aus einer Quellenspannung eine Spannung, eine Stromverstärkung aus einem
Quellstrom einen Strom. Eine Transimpedanz macht aus einem Strom an einer Stelle eine Spannung an einer anderen, *trans* heißt hinüber; __Impedanz__ ist der
Name für einen Widerstand in der Wechselstromtechnik, bei Gleichstrom ist es ein gewöhnlicher Widerstand. Eine Transadmittanz, ein Leitwert, macht
umgekehrt aus einer Spannung einen Strom. Das Skript nennt die Stromverstärkungen $b_i$; hier heißen sie $c_\mu$, weil $b_k$ weiter unten die Bits eines
Wandlers bezeichnet. Seine Summe über die Stromquellen endet beim Index $i$; gemeint ist $m$.

**Im Bild:** Der Druck am Hahn ist die Summe der Drücke, die jedes Werk allein dort erzeugt, jeder mit dem Faktor, den das Rohrnetz zwischen Werk und Hahn
festlegt.

:::herleitung
**Zwei Teilzustände.** Man betrachtet zwei Zustände des Netzes. Im ersten wirkt nur die Quelle 1, alle anderen sind stillgelegt, Spannungsquellen als
Kurzschluss, Stromquellen als Unterbrechung; seine Zweigströme und -spannungen heißen $I'_k$ und $U'_k$. Im zweiten wirken alle Quellen außer der Quelle
1, die nun stillgelegt ist; seine Größen heißen $I''_k$ und $U''_k$. Behauptet wird: Die Summen erfüllen alle Gleichungen des vollständigen Netzes.

- **Knotenregel.** An jedem Knoten ist die Summe der $I'_k$ null und die der $I''_k$ auch, also auch die Summe der $I'_k + I''_k$.
- **Maschenregel.** Ebenso für die Spannungen jeder Masche.
- **Widerstände.** Aus den beiden ohmschen Gesetzen folgt das für die Summe; hier geht ein, dass das ohmsche Gesetz linear ist:

$$U'_k = R_k\,I'_k, \qquad U''_k = R_k\,I''_k, \qquad U'_k + U''_k = R_k\,(I'_k + I''_k).$$

- **Quellen.** Eine Spannungsquelle hat in dem Zustand, in dem sie wirkt, ihre Spannung $U_q$, im anderen ist sie ein Kurzschluss mit der Spannung null;
  die Summe ist $U_q$, wie im vollständigen Netz. Eine Stromquelle führt in einem Zustand ihren Strom, im anderen als Unterbrechung null, zusammen $I_q$.

Das vollständige Netz hat genau eine Lösung, wie im Artikel über die Kirchhoffschen Gesetze und im vorigen Artikel begründet. Also ist die Summe der
beiden Teilzustände diese Lösung. Zerlegt man den zweiten Teilzustand ebenso weiter, bis jede Quelle allein steht, ist jede Größe die Summe der
Teilwirkungen aller Quellen. Im Bild: Rohr für Rohr addieren sich die Durchflüsse und Druckverluste der beiden Zustände, weil jedes lineare Rohr für die
Summe der Durchflüsse die Summe der Druckverluste hat.

**Proportional.** Wirkt nur eine Quelle, etwa $U_{q1}$, und multipliziert man alle Ströme und Spannungen ihrer Lösung mit einer Zahl $c$, erfüllen sie
wieder Knoten-, Maschenregel und ohmsches Gesetz, nun mit der Quellenspannung $c\,U_{q1}$; die stillgelegten Quellen bleiben bei null. Wegen der
Eindeutigkeit ist das die Lösung für $c\,U_{q1}$. Die Teilwirkung ist also proportional zu $U_{q1}$, mit einem Faktor, der nur von den Widerständen abhängt:
für eine Spannung $a_1 U_{q1}$, für einen Strom $Y_1 U_{q1}$. Ebenso für jede Stromquelle, mit $Z_\mu$ und $c_\mu$.
Zusammen ergibt das die beiden Formeln. Im Bild: Ein doppelt so hoher Turm, allein am Netz, verdoppelt jeden Durchfluss und jeden Druck.

**Warum gerade so stilllegen.** Die Quellen-Zeile zeigt den Grund: Jede Quelle muss in genau einem Teilzustand mit ihrem vollen Wert vorkommen und in
allen anderen mit dem Wert null. Eine Spannungsquelle mit dem Wert null ist ein Kurzschluss, eine Stromquelle mit dem Wert null eine Unterbrechung.
:::

::::beispiel Ladegerät und Batterie an einem Verbraucher
In einem Wohnmobil versorgen ein Ladegerät und eine kleine Bleibatterie gemeinsam einen Kühlschrank. Alle drei liegen zwischen einem Knoten K und Masse;
gesucht sind die Spannung $U$ am Verbraucher und der Strom $I_B$ aus dem Pluspol der Batterie.

$$U_{q1} = 14\,\text{V}, \qquad R_{q1} = 0{,}5\,\Omega, \qquad U_{q2} = 12\,\text{V}, \qquad R_{q2} = 0{,}1\,\Omega, \qquad R_L = 2\,\Omega.$$

**Nur das Ladegerät.** Die Batterie wird zum Draht, ihr Innenwiderstand bleibt und liegt parallel zur Last:

$$R_{q2} \parallel R_L = \frac{0{,}1\cdot2}{2{,}1}\,\Omega \approx 0{,}0952\,\Omega, \qquad U' = 14\,\text{V}\cdot\frac{0{,}0952\,\Omega}{0{,}5\,\Omega + 0{,}0952\,\Omega} = 2{,}24\,\text{V}.$$

**Nur die Batterie.** Das Ladegerät wird zum Draht:

$$R_{q1} \parallel R_L = \frac{0{,}5\cdot2}{2{,}5}\,\Omega = 0{,}4\,\Omega, \qquad U'' = 12\,\text{V}\cdot\frac{0{,}4\,\Omega}{0{,}1\,\Omega + 0{,}4\,\Omega} = 9{,}6\,\text{V}.$$

**Überlagert.** Die Faktoren sind die Spannungsverstärkungen $0{,}16$ und $0{,}8$:

$$U = U' + U'' = 0{,}16\cdot14\,\text{V} + 0{,}8\cdot12\,\text{V} = 11{,}84\,\text{V}.$$

**Der Batteriestrom.** Wirkt nur das Ladegerät, liegen $2{,}24\,\text{V}$ an der stillgelegten Batterie, und durch ihren Innenwiderstand fließt Strom
*in* sie hinein; wirkt nur die Batterie, fließt Strom heraus:

$$I'_B = -\frac{2{,}24\,\text{V}}{0{,}1\,\Omega} = -22{,}4\,\text{A}, \qquad I''_B = \frac{12\,\text{V} - 9{,}6\,\text{V}}{0{,}1\,\Omega} = 24\,\text{A}, \qquad I_B = 1{,}6\,\text{A}.$$

Zwei große Teilströme heben sich bis auf $1{,}6\,\text{A}$ auf: Die Batterie hilft dem Ladegerät noch leicht. Die Probe mit dem vollständigen Netz gibt
dasselbe, denn

$$I_B = \frac{12\,\text{V} - 11{,}84\,\text{V}}{0{,}1\,\Omega} = 1{,}6\,\text{A}.$$

**Im Bild:** Zwei Türme an einem Abnehmer. Arbeitet nur der höhere, drückt er Wasser auch in den stillgelegten niedrigeren hinein; arbeitet nur der
niedrigere, fließt aus ihm viel heraus. Zusammen bleibt ein kleiner Rest.
::::

:::grafik
Szene: get1/analyse-linearer-netzwerke/03-teilbilder · Vorlage: superposition-teilbilder
Nach Bild 7.67 und 7.68 des Skripts, an Ladegerät und Batterie der Beispiel-Seite: oben das vollständige Netz mit $U_{q1} = 14\,\text{V}$ und
$R_{q1} = 0{,}5\,\Omega$ links, $R_L = 2\,\Omega$ in der Mitte, $U_{q2} = 12\,\text{V}$ und $R_{q2} = 0{,}1\,\Omega$ rechts, alle zwischen Knoten K und Masse,
Spannungspfeile der Quellen und von $U$ nach unten, $I_B$ aus dem Pluspol der Batterie nach oben. Darunter zwei Teilbilder: links ist $U_{q2}$ durch einen
Draht ersetzt, Anzeige $U' = 2{,}24\,\text{V}$ und $I'_B = -22{,}4\,\text{A}$ mit umgedrehtem Pfeil; rechts ist $U_{q1}$ durch einen Draht ersetzt, Anzeige
$U'' = 9{,}6\,\text{V}$ und $I''_B = 24\,\text{A}$. Ein Pluszeichen führt zu $U = 11{,}84\,\text{V}$ und $I_B = 1{,}6\,\text{A}$. Ein Regler verstellt
$U_{q1}$, und nur das linke Teilbild ändert sich, proportional. Kernaussage: Jede Quelle allein, dann addieren — mit Vorzeichen. (Rot = Quellen und
ihre Drähte, blau = Spannungen, orange = Teilströme, grau = Widerstände.)
:::

## Das Verfahren in drei Schritten

Aus dem Satz wird ein Rezept, im Skript die Vorgehensweise des Superpositionsverfahrens:

1. **Stilllegen.** Alle Quellen bis auf eine werden stillgelegt: ideale Spannungsquellen durch einen Kurzschluss ersetzt, mit dem Innenwiderstand null,
   ideale Stromquellen durch eine Unterbrechung, mit dem Innenleitwert null. Innenwiderstände realer Quellen bleiben stehen.
2. **Teilwirkung.** Im verbleibenden Netz mit nur einer Quelle berechnet man die gesuchte Größe, meist mit Reihen- und Parallelschaltung, Spannungs- und
   Stromteiler. Das wiederholt man für jede Quelle, immer mit denselben Zählpfeilen für die gesuchte Größe.
3. **Überlagern.** Die Teilwirkungen werden mit ihren Vorzeichen addiert; die Striche zählen die Quellen:

$$U = U' + U'' + U''' + \dots, \qquad I = I' + I'' + I''' + \dots$$

**So liest man das:** Jedes Teilproblem hat nur eine Quelle und lässt sich oft ohne Gleichungssystem lösen, mit den Teilerregeln; das macht das Verfahren
übersichtlich. Gleiche Zählpfeile in allen Teilbildern sind Pflicht, sonst stimmen die Vorzeichen der Summe nicht, und eine Teilwirkung darf negativ sein.
Eine Folge ist besonders nützlich: Ein Widerstand in Reihe mit einer idealen Stromquelle ändert an keiner anderen Größe etwas, er verschiebt nur die
Spannung an der Stromquelle selbst.

**Im Bild:** Werk für Werk messen, die anderen stillgelegt, dann zusammenzählen. Ein enges Rohr zwischen einer Spritzenpumpe und dem Netz ändert nichts
am Rest, denn die Pumpe drückt ihren Durchfluss in jedem Fall hindurch.

:::herleitung
**Rezept aus dem Satz.** Schritt 1 und 2 bestimmen die Summanden des Überlagerungssatzes einzeln, Schritt 3 addiert sie. Gleiche Zählpfeile sind nötig,
weil die Knoten- und Maschenregeln in der Herleitung des Satzes in allen Teilzuständen für dieselben Zweigrichtungen gelten.

**Widerstand vor der Stromquelle.** In einem Zweig aus einer idealen Stromquelle und einem Widerstand $R_s$ in Reihe legt die Quelle den Zweigstrom fest,
gleichgültig, wie groß $R_s$ ist. Man wählt die Maschen so, dass nur eine durch diesen Zweig läuft, wie es mit einem Baum aus dem Artikel über
topologische Grundbegriffe immer geht. Diese eine Masche enthält die Spannung an der Stromquelle, die sich frei einstellt, und bestimmt nur sie; alle
anderen Gleichungen enthalten vom Zweig nur den festen Strom. Deshalb hängt außer der Spannung an der Stromquelle keine Größe von $R_s$ ab. Im Bild: Die
Pumpe drückt durch ein engeres Rohr einfach stärker.
:::

::::beispiel Spannungsquelle und Stromquelle an einem Knoten
Eine Spannungsquelle $U_q$ speist über $R_a$ einen Knoten K, von dem $R_b$ nach Masse führt; eine Stromquelle $I_q$ schiebt über einen Vorwiderstand $R_s$
Strom von Masse in den Knoten K.

$$U_q = 10\,\text{V}, \qquad R_a = 2\,\text{k}\Omega, \qquad R_b = 3\,\text{k}\Omega, \qquad I_q = 2\,\text{mA}, \qquad R_s = 5\,\text{k}\Omega.$$

**Direkt, mit der Knotenregel.** Am Knoten K fließen der Strom aus der Spannungsquelle und der Quellstrom zu, durch $R_b$ fließt Strom ab:

$$\frac{10\,\text{V} - U_K}{2\,\text{k}\Omega} + 2\,\text{mA} = \frac{U_K}{3\,\text{k}\Omega}, \qquad U_K = 8{,}4\,\text{V}.$$

**Überlagert.** Nur die Spannungsquelle, die Stromquelle als Unterbrechung: der unbelastete Teiler. Nur die Stromquelle, die Spannungsquelle als Draht:
$R_a$ und $R_b$ liegen parallel, und der Quellstrom fließt durch beide.

$$U'_K = 10\,\text{V}\cdot\frac{3\,\text{k}\Omega}{2\,\text{k}\Omega + 3\,\text{k}\Omega} = 6\,\text{V}, \qquad U''_K = 2\,\text{mA}\cdot\frac{2\cdot3}{2 + 3}\,\text{k}\Omega = 2{,}4\,\text{V}, \qquad U_K = 8{,}4\,\text{V}.$$

Die Spannungsverstärkung ist $0{,}6$, die Transimpedanz $1{,}2\,\text{k}\Omega$, und $R_s$ kommt nirgends vor.

**Ein Strom mit zwei Vorzeichen.** Der Strom $I_a$ durch $R_a$, von der Spannungsquelle zum Knoten gezählt: Allein treibt die Spannungsquelle Strom zum
Knoten, allein drückt die Stromquelle Strom zurück:

$$I'_a = \frac{10\,\text{V} - 6\,\text{V}}{2\,\text{k}\Omega} = 2\,\text{mA}, \qquad I''_a = -\frac{2{,}4\,\text{V}}{2\,\text{k}\Omega} = -1{,}2\,\text{mA}, \qquad I_a = 0{,}8\,\text{mA}.$$

Die Probe mit dem vollständigen Netz:

$$I_a = \frac{10\,\text{V} - 8{,}4\,\text{V}}{2\,\text{k}\Omega} = 0{,}8\,\text{mA}.$$

**Der Vorwiderstand.** $R_s$ ändert nur die Spannung $U_{Iq}$, die die Stromquelle aufbringen muss, um ihren Strom von Masse über $R_s$ auf das Potenzial von
K zu heben:

$$U_{Iq} = U_K + R_s\,I_q = 8{,}4\,\text{V} + 10\,\text{V} = 18{,}4\,\text{V}.$$

**Im Bild:** Ein Turm und eine Pumpe speisen denselben Abzweig. Was die Pumpe dort beiträgt, hängt nicht davon ab, wie eng das Rohr zwischen ihr und dem
Abzweig ist; sie muss nur stärker drücken.
::::

## Warum sich Leistungen nicht überlagern

Die Leistung an einem Widerstand $R$ mit dem Strom $I$ ist $R I^2$, quadratisch im Strom und damit nicht linear. Setzt sich der Strom aus zwei
Teilwirkungen $I'$ und $I''$ zusammen, mit den Teilleistungen $P'$ und $P''$, die jede für sich entstünden, dann ist

:::formel
$$P = R\,(I' + I'')^2 = P' + P'' + 2R\,I'\,I''.$$
:::

**So liest man das:** Die Summe der Teilleistungen verfehlt die wahre Leistung um den __Kreuzterm__ $2R\,I'\,I''$. Er verschwindet nur, wenn eine der beiden
Teilwirkungen null ist. Haben die Teilströme gleiches Vorzeichen, ist die wahre Leistung größer als die Summe, bei entgegengesetztem kleiner, unter
Umständen fast null. Man überlagert deshalb immer zuerst Ströme und Spannungen und berechnet erst danach die Leistung. Das Skript sagt es allgemein: Wo
die Wirkung nicht linear von der Ursache abhängt, wie bei der Leistung, gilt das Überlagerungsprinzip nicht.

**Im Bild:** Die Reibungswärme in einem Rohr wächst mit dem Quadrat des Durchflusses. Schicken zwei Werke Wasser in dieselbe Richtung, entsteht mehr Wärme
als die Summe; drücken sie gegeneinander, steht das Wasser fast, und es entsteht kaum Wärme, obwohl jedes allein viel erzeugte.

:::herleitung
**Binomische Formel.** Mit dem Gesamtstrom aus dem Überlagerungssatz und der Leistung $R I^2$:

$$P = R\,(I' + I'')^2 = R\,I'^2 + 2R\,I'\,I'' + R\,I''^2.$$

Die beiden äußeren Glieder sind die Teilleistungen, das mittlere ist der Kreuzterm. Mit Spannungen gilt dasselbe, ausgehend von $U^2/R$.
:::

::::beispiel Verluste in Batterie und Verbraucher
Ladegerät und Batterie am Kühlschrank wie oben: Durch den Innenwiderstand der Batterie, $0{,}1\,\Omega$, fließen die Teilströme $-22{,}4\,\text{A}$ und
$24\,\text{A}$, zusammen $1{,}6\,\text{A}$.

**Teilleistungen gegen wahre Leistung:**

$$P' = 0{,}1\,\Omega\cdot(22{,}4\,\text{A})^2 \approx 50{,}2\,\text{W}, \qquad P'' = 0{,}1\,\Omega\cdot(24\,\text{A})^2 = 57{,}6\,\text{W},$$

$$P = 0{,}1\,\Omega\cdot(1{,}6\,\text{A})^2 = 0{,}256\,\text{W}.$$

Der Kreuzterm ist hier stark negativ und frisst fast alles auf:

$$2R\,I'\,I'' = 2\cdot0{,}1\,\Omega\cdot(-22{,}4\,\text{A})\cdot24\,\text{A} \approx -107{,}5\,\text{W}.$$

Die Summe der Teilleistungen, knapp $108\,\text{W}$, wäre mehr als vierhundertmal so groß wie die wahre Leistung.

**Am Verbraucher** haben die Teilspannungen $2{,}24\,\text{V}$ und $9{,}6\,\text{V}$ gleiches Vorzeichen, und die Summe der Teilleistungen ist zu klein:

$$P' + P'' = \frac{(2{,}24\,\text{V})^2 + (9{,}6\,\text{V})^2}{2\,\Omega} \approx 48{,}6\,\text{W}, \qquad P = \frac{(11{,}84\,\text{V})^2}{2\,\Omega} \approx 70{,}1\,\text{W}.$$

**Im Bild:** In der Leitung zum niedrigeren Turm drücken die beiden Werke gegeneinander, das Wasser steht fast still; in der Leitung zum Abnehmer drücken
sie in dieselbe Richtung.
::::

Eine Ausnahme kennt die Wechselstromtechnik, worauf das Skript hinweist: Haben zwei Teilströme verschiedene Frequenzen, mittelt sich der Kreuzterm über
die Zeit heraus, und die mittleren Leistungen addieren sich doch. Das gehört zu einem späteren Kapitel. Bei Gleichstrom gibt es nichts zu mitteln; der
Kreuzterm bleibt, außer eine der Teilwirkungen ist null.

:::herleitung
**Zwei Sinusströme.** Mit den Scheitelwerten $\hat\imath_1$, $\hat\imath_2$ und den Kreisfrequenzen $\omega_1$, $\omega_2$ ist der Momentanwert des Stroms und
der Kreuzterm der Momentanleistung

$$i(t) = \hat\imath_1 \sin(\omega_1 t) + \hat\imath_2 \sin(\omega_2 t), \qquad 2R\,\hat\imath_1\hat\imath_2\,\sin(\omega_1 t)\sin(\omega_2 t).$$

**Produkt in Summe.** Nach dem Additionstheorem für den Kosinus ist das Produkt zweier Sinusfunktionen eine Differenz zweier Kosinusfunktionen:

$$2\sin(\omega_1 t)\sin(\omega_2 t) = \cos\big((\omega_1 - \omega_2)\,t\big) - \cos\big((\omega_1 + \omega_2)\,t\big).$$

Für verschiedene Frequenzen schwingen beide Kosinusfunktionen um null, und ihr Mittelwert über eine lange Zeit geht gegen null. Bei gleicher Frequenz ist
der erste Kosinus konstant eins, und der Kreuzterm bleibt.
:::

## Nur in linearen Netzen

Der Beweis des Satzes brauchte an einer Stelle die Linearität der Bauteile: Für jeden Widerstand musste aus den ohmschen Gesetzen der beiden Teilzustände
das ohmsche Gesetz für ihre Summe folgen. Ein Bauteil, dessen Kennlinie keine Gerade durch den Ursprung ist, verletzt das, und dann gilt die Überlagerung
nicht.

Das wichtigste Beispiel ist die __Diode__, ein Halbleiterbauteil, das Strom praktisch nur in einer Richtung leitet und bei Silizium erst oberhalb einer
__Schwellspannung__ von etwa $0{,}7\,\text{V}$ nennenswert. In einem Netz mit Dioden darf man die Quellen nicht einzeln wirken lassen und addieren; man
muss sie gemeinsam betrachten.

**Im Bild:** Ein Rückschlagventil, das erst ab einem Mindestdruck öffnet. Jedes Werk allein schafft diesen Druck vielleicht nicht, beide zusammen schon,
und dann fließt Wasser, wo die Summe der Einzelmessungen nichts versprach.

::::beispiel Zwei halbe Volt vor einer Diode
Zwei Spannungsquellen mit je $0{,}5\,\text{V}$ liegen in Reihe mit einem Widerstand von $100\,\Omega$ und einer Diode in Durchlassrichtung. Die Diode wird
vereinfacht beschrieben: Unterhalb von $0{,}7\,\text{V}$ sperrt sie, darüber fallen an ihr genau $0{,}7\,\text{V}$ ab.

**Einzeln.** Wirkt nur eine Quelle, die andere als Draht, liegt höchstens $0{,}5\,\text{V}$ an der Diode, und sie sperrt:

$$I' = 0, \qquad I'' = 0.$$

**Gemeinsam.** Beide Quellen zusammen bringen $1\,\text{V}$; die Diode leitet, und am Widerstand bleiben $0{,}3\,\text{V}$:

$$I = \frac{1\,\text{V} - 0{,}7\,\text{V}}{100\,\Omega} = 3\,\text{mA}.$$

Die Summe der Teilwirkungen ist null, die Wirkung beider Quellen $3\,\text{mA}$: Die Überlagerung versagt.

**Im Bild:** Zwei Werke vor einem Ventil, das erst ab einem Mindestdruck öffnet; jedes allein bleibt darunter.
::::

## Anwendung: der spannungsbasierte Digital-Analog-Wandler

Ein __Digital-Analog-Wandler__ macht aus einer Binärzahl eine Spannung. Bild 7.69 des Skripts zeigt eine Bauform mit einem __R-2R-Netzwerk__, das im
Artikel über die Zusammenschaltung von Widerständen schon als Stromteiler vorkam; hier wird es mit Spannungen betrieben.

- Längs liegt zwischen aufeinanderfolgenden Knoten $0, 1, \dots, N-1$ jeweils ein Widerstand $R$.
- Von jedem Knoten $k$ führt ein Zweig $2R$ zu einem Umschalter. Er legt ihn je nach dem __Bit__ $b_k$, einer Binärstelle mit dem Wert 0 oder 1, an Masse
  oder an die Referenzspannung $U_\text{ref}$.
- Am linken Ende schließt ein Widerstand $2R$ nach Masse ab. Am rechten Ende, beim höchstwertigen Bit (englisch *most significant bit*, MSB), wird die
  Ausgangsspannung $U_\text{aus}$ abgegriffen.
- Ein Operationsverstärker, ein Verstärker mit sehr hochohmigem Eingang, übernimmt sie, ohne Strom zu ziehen; der Ausgang bleibt unbelastet.

Jede Schalterstellung ist eine Spannungsquelle mit $0$ oder $U_\text{ref}$. Nach dem Überlagerungssatz trägt jedes Bit für sich bei, mit einem Faktor, der
nur von seinem Platz im Netz abhängt, und das R-2R-Netz macht diese Faktoren zu Zweierpotenzen:

:::formel
$$U_\text{aus} = U_\text{ref}\sum_{k=0}^{N-1} \frac{b_k}{2^{N-k}} \qquad = U_\text{ref}\Big(\frac{b_{N-1}}{2} + \frac{b_{N-2}}{4} + \dots + \frac{b_0}{2^N}\Big).$$
:::

**So liest man das:** Das höchstwertige Bit trägt die Hälfte von $U_\text{ref}$ bei, das nächste ein Viertel, das niedrigstwertige den Bruchteil
$1/2^N$. Die Ausgangsspannung ist die Binärzahl, als Bruchteil von $U_\text{ref}$ gelesen: $N$ Bits ergeben $2^N$ Stufen im Abstand $U_\text{ref}/2^N$, von null
bis knapp unter $U_\text{ref}$.

**Im Bild:** Türme an einer Kette von Rohren, jeder an einer anderen Stelle. Je weiter vom Hahn entfernt ein Turm einspeist, desto öfter wird sein Beitrag
auf dem Weg zum Hahn halbiert.

:::herleitung
**Am linken Ende.** Am Knoten 0 liegen der Abschluss $2R$ nach Masse und der Zweig $2R$ zur Quelle $b_0 U_\text{ref}$ parallel: zwei reale
Spannungsquellen mit gleichem Innenwiderstand, die eine mit null Volt. Nach dem Artikel über ideale und reale Quellen ist ihre Ersatzquelle der mit den
Leitwerten gewichtete Mittelwert, bei gleichen Widerständen der einfache Mittelwert, hinter der Parallelschaltung der beiden Widerstände:

$$U_0^* = \frac{0 + b_0\,U_\text{ref}}{2}, \qquad R^* = 2R \parallel 2R = R.$$

**Eine Stufe weiter.** Mit dem Längswiderstand $R$ zum nächsten Knoten wird daraus eine Quelle $U_0^*$ hinter $2R$, parallel zum Zweig $2R$ des Knotens 1
mit $b_1 U_\text{ref}$. Wieder sind es zwei gleiche Innenwiderstände:

$$U_1^* = \frac{U_0^* + b_1\,U_\text{ref}}{2}, \qquad R^* = R.$$

**Bis zum Ausgang.** Jede Stufe halbiert, was von links kommt, und addiert die Hälfte des eigenen Bits. Bit $k$ geht am Knoten $k$ mit dem Faktor
$\frac12$ ein und wird an den Knoten $k+1$ bis $N-1$ noch $N-1-k$-mal halbiert, insgesamt $N-k$-mal. Weil der Ausgang unbelastet ist, liegt dort die
Ersatzspannung des letzten Knotens:

$$U_\text{aus} = U_{N-1}^* = \sum_{k=0}^{N-1} \frac{b_k\,U_\text{ref}}{2^{N-k}}.$$

Die Bits wirken unabhängig voneinander und addieren sich: die Überlagerung, mit Faktoren, die nur vom Platz im Netz abhängen.
:::

Das Skript rechnet die Teilwirkungen in einem Ersatzschaltbild mit sieben Quellen $U_0$ bis $U_6$ einzeln aus (Bild 7.70). Für $U_5$, die zweithöchste
Stelle, steht dort $\frac38\,U_5$. Das ist die Spannung am Knoten 5, wenn nur $U_5$ wirkt: Links von ihm liegen $2R$, rechts $R$ und der Zweig $2R$ des
letzten Knotens, zusammen $3R$. Bis zum Ausgang teilen $R$ und dieser Zweig sie noch einmal:

$$U_5\cdot\frac{2R \parallel 3R}{2R + 2R \parallel 3R} = \frac38\,U_5, \qquad U_\text{aus} = \frac38\,U_5\cdot\frac{2R}{R + 2R} = \frac14\,U_5,$$

wie es die Zweierpotenzen verlangen.

::::beispiel Ein 4-Bit-Wandler mit dem Wort 1011
Ein Wandler mit vier Bits und der Referenzspannung $8\,\text{V}$ erhält das Wort 1011:

$$N = 4, \qquad U_\text{ref} = 8\,\text{V}, \qquad b_3 = 1, \qquad b_2 = 0, \qquad b_1 = 1, \qquad b_0 = 1.$$

**Überlagert.** Jedes gesetzte Bit trägt seinen Bruchteil bei:

$$U_\text{aus} = 8\,\text{V}\cdot\Big(\frac12 + \frac04 + \frac18 + \frac1{16}\Big) = 4\,\text{V} + 0\,\text{V} + 1\,\text{V} + 0{,}5\,\text{V} = 5{,}5\,\text{V}.$$

**Von links aufgerollt.** Die Ersatzspannungen der Knoten 0 bis 3, jeweils der Mittelwert aus der vorigen und der eigenen Bitspannung:

$$U_0^* = \frac{0 + 8\,\text{V}}{2} = 4\,\text{V}, \qquad U_1^* = \frac{4\,\text{V} + 8\,\text{V}}{2} = 6\,\text{V}, \qquad U_2^* = \frac{6\,\text{V} + 0}{2} = 3\,\text{V}, \qquad U_3^* = \frac{3\,\text{V} + 8\,\text{V}}{2} = 5{,}5\,\text{V}.$$

Beide Wege geben $5{,}5\,\text{V}$, elf Stufen zu je $0{,}5\,\text{V}$, denn 1011 ist die Dualzahl für elf. Das größte Wort 1111 ergäbe $7{,}5\,\text{V}$.

**Im Bild:** Vier Türme an einer Rohrkette; der am Hahn trägt die Hälfte seines Drucks bei, der nächste ein Viertel, der übernächste ein Achtel.
::::

:::grafik
Szene: get1/analyse-linearer-netzwerke/03-r2r-wandler · Vorlage: r2r-spannungswandler
Nach Bild 7.69 des Skripts als 4-Bit-Wandler: Abschluss $2R$ nach Masse am Knoten 0, Längswiderstände $R$ zwischen den Knoten 0 bis 3, an jedem Knoten ein
Zweig $2R$ zu einem Umschalter zwischen Masse und $U_\text{ref} = 8\,\text{V}$, am Knoten 3 der Ausgang mit einem Operationsverstärker und der Anzeige
$U_\text{aus}$. Vier Schalter für die Bits $b_3$ bis $b_0$, anfangs 1011. Rechts ein Balkendiagramm der Teilwirkungen, $4\,\text{V}$, $2\,\text{V}$,
$1\,\text{V}$ und $0{,}5\,\text{V}$ für gesetzte Bits, gestapelt zur Ausgangsspannung $5{,}5\,\text{V}$. Ein zweiter Modus „aufrollen" lässt von links
nach rechts an jedem Knoten die Ersatzquelle $R$ mit der Mittelwertspannung erscheinen. Kernaussage: Jedes Bit trägt unabhängig bei, mit einer Zweierpotenz
als Faktor. (Rot = Quellen und Schalter, blau = Ausgangsspannung, orange = Teilwirkungen und Ersatzquellen, grau = Widerstände.)
:::

## Bedeutung und Ausblick

Überlagerung ist das Kennzeichen aller linearen Systeme, weit über Widerstandsnetze hinaus. Die Durchbiegung einer Brücke unter mehreren Fahrzeugen ist
die Summe der Durchbiegungen unter jedem einzelnen, solange der Stahl elastisch und die Verformung klein bleibt; Wellen durchdringen einander, ohne sich
zu stören. In der Wechselstromtechnik und der Signal- und Systemtheorie zerlegt man ein Signal in Sinusschwingungen verschiedener Frequenz, behandelt jede
für sich und setzt die Antworten wieder zusammen. Auch Netze mit Dioden und Transistoren rechnet man für kleine Änderungen um einen festen
Arbeitspunkt linear, mit der Tangente an die Kennlinie, und dort gilt die Überlagerung wieder.

Für lineare Netze stehen nun drei Werkzeuge nebeneinander, die stets dasselbe Ergebnis liefern: die Kirchhoffschen Gleichungen für alle Größen auf
einmal, die Ersatzquelle für das Verhalten an zwei Klemmen und die Überlagerung für Netze mit mehreren Quellen. Das Skript stellt für das R-2R-Netzwerk eine
Datei für das Schaltungssimulationsprogramm LTspice bereit. Der nächste Artikel fragt, wie viel Leistung ein Widerstand aufnimmt und bei welcher Last eine
Quelle die größte Leistung abgibt: Energieumsetzung und Leistungsanpassung.

:::kern
- __Linear__ heißt additiv und homogen: Die Wirkung der Summe ist die Summe der Wirkungen.
- __Überlagerungssatz__: Jede Spannung und jeder Strom eines linearen Netzes ist die Summe der Teilwirkungen der einzelnen Quellen.
- Jede Teilwirkung ist proportional zu ihrer Quelle; der Faktor hängt nur von den Widerständen ab.
- Stilllegen: Spannungsquellen als Kurzschluss, Stromquellen als Unterbrechung; Innenwiderstände bleiben.
- In allen Teilbildern dieselben Zählpfeile, die Teilwirkungen mit Vorzeichen addieren.
- Leistungen überlagern sich nicht: $P=P'+P''+2RI'I''$.
- Mit nichtlinearen Bauteilen wie Dioden gilt die Überlagerung nicht.
- Im R-2R-Wandler trägt Bit $k$ den Anteil $U_\text{ref}/2^{N-k}$ bei.
:::

:::quiz
F: Was heißt linear genau, und warum ist die Kennlinie einer realen Quelle nur mit der Quellenspannung als zweiter Ursache linear?
A: Linear heißt additiv und homogen, $f(c_1\vec x_1+c_2\vec x_2)=c_1f(\vec x_1)+c_2f(\vec x_2)$. Bei $U=12\,\text{V}-2\,\Omega\cdot I$ ergeben $U(1\,\text{A})$ und $U(2\,\text{A})$ zusammen $18\,\text{V}$, $U(3\,\text{A})$ aber $6\,\text{V}$; der feste Anteil der Quelle stört. Zählt man $U_q$ als Ursache mit, liefert der Zustand mit $24\,\text{V}$ und $3\,\text{A}$ genau die $18\,\text{V}$.
F: Was besagt der Überlagerungssatz, und was bedeuten seine Faktoren?
A: Jede Spannung und jeder Strom eines linearen Netzes ist eine Summe über alle Quellen, $U_{AB}=\sum a_\nu U_{q\nu}+\sum Z_\mu I_{q\mu}$ und entsprechend mit $Y_\nu$ und $c_\mu$ für einen Strom. Jeder Summand ist die Teilwirkung einer Quelle; die Faktoren hängen nur von den Widerständen ab — Spannungs- und Stromverstärkungen ohne Einheit, Transimpedanzen in Ohm, Transadmittanzen in Siemens.
F: Warum ergibt die Summe zweier Teilzustände die Lösung des vollständigen Netzes?
A: Knoten- und Maschenregel sind Summen und gelten deshalb auch für die Summe der Teilzustände; das ohmsche Gesetz ist linear und gilt ebenso. Jede Quelle kommt in einem Teilzustand mit ihrem vollen Wert vor und im anderen mit null, die Summe hat also überall die richtigen Quellenwerte. Weil das Netz genau eine Lösung hat, ist die Summe diese Lösung.
F: Warum legt man beim Überlagern Spannungsquellen durch einen Kurzschluss und Stromquellen durch eine Unterbrechung still?
A: Jede Quelle muss in genau einem Teilzustand mit vollem Wert und in allen anderen mit dem Wert null vorkommen. Eine Spannungsquelle mit null Volt hält bei jedem Strom die Spannung null, wie ein Draht; eine Stromquelle mit null Ampere lässt bei jeder Spannung nichts durch, wie eine Unterbrechung. Innenwiderstände realer Quellen bleiben stehen.
F: Wie verteilen sich Spannung und Batteriestrom bei Ladegerät (14 V, 0,5 Ω) und Batterie (12 V, 0,1 Ω) an 2 Ω?
A: Das Ladegerät allein bringt $2{,}24\,\text{V}$, die Batterie allein $9{,}6\,\text{V}$, zusammen $11{,}84\,\text{V}$. Durch die Batterie fließen allein vom Ladegerät $22{,}4\,\text{A}$ hinein, allein von ihr selbst $24\,\text{A}$ heraus; überlagert bleibt $1{,}6\,\text{A}$ heraus, wie die Probe am vollständigen Netz bestätigt.
F: Warum braucht man in allen Teilbildern dieselben Zählpfeile, und was bedeutet eine negative Teilwirkung?
A: Addiert werden die Teilwirkungen derselben Größe, und die Regeln im Beweis gelten für feste Zweigrichtungen. Eine negative Teilwirkung heißt, dass diese Quelle gegen den Zählpfeil treibt: Durch $R_a$ treibt die Spannungsquelle allein $2\,\text{mA}$ zum Knoten, die Stromquelle allein $1{,}2\,\text{mA}$ zurück, zusammen $0{,}8\,\text{mA}$.
F: Warum hat ein Widerstand in Reihe mit einer idealen Stromquelle keinen Einfluss auf das übrige Netz?
A: Die Stromquelle legt den Zweigstrom fest, gleichgültig, wie groß der Widerstand ist. Nur die Masche durch diesen Zweig enthält die frei einstellbare Spannung an der Stromquelle und bestimmt nur sie. Am Knoten mit $10\,\text{V}$ über $2\,\text{k}\Omega$, $3\,\text{k}\Omega$ und $2\,\text{mA}$ bleibt die Spannung bei $8{,}4\,\text{V}$; mit $5\,\text{k}\Omega$ Vorwiderstand muss die Stromquelle $18{,}4\,\text{V}$ aufbringen.
F: Warum darf man Leistungen nicht überlagern?
A: Die Leistung ist quadratisch im Strom, $P=R(I'+I'')^2=P'+P''+2RI'I''$, und der Kreuzterm fehlt in der Summe der Teilleistungen. Im Innenwiderstand der Batterie ergäben die Teilströme $50{,}2\,\text{W}$ und $57{,}6\,\text{W}$, tatsächlich sind es $0{,}256\,\text{W}$. Nur bei Wechselströmen verschiedener Frequenz mittelt sich der Kreuzterm über die Zeit heraus.
F: Warum versagt die Überlagerung bei einer Diode?
A: Der Beweis braucht für jedes Bauteil, dass die Kennlinie der Summe die Summe der Kennlinien ist, und das gilt nur für Geraden durch den Ursprung. Eine Diode sperrt unterhalb von etwa $0{,}7\,\text{V}$: Zwei Quellen mit je $0{,}5\,\text{V}$ treiben einzeln keinen Strom, zusammen über $100\,\Omega$ aber $3\,\text{mA}$.
F: Warum gewichtet das R-2R-Netz die Bits mit Zweierpotenzen, und welcher Fehler steht dazu im Skript?
A: Von links aufgerollt liegen an jedem Knoten zwei gleiche Widerstände $2R$ mit zwei Spannungen parallel; ihre Ersatzquelle ist $R$ mit dem Mittelwert, also halbiert jede Stufe, was von links kommt. Bit $k$ trägt $U_\text{ref}/2^{N-k}$ bei; das Wort 1011 an $8\,\text{V}$ ergibt $5{,}5\,\text{V}$. Im Skript ist die Teilwirkung von $U_5$ mit $\frac38\,U_5$ angegeben — das ist die Spannung am Knoten 5; am Ausgang sind es $\frac14\,U_5$.
:::
